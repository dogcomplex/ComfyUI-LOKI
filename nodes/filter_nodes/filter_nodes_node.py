import argparse
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import os
# No requests import needed here directly

# Import the batch query node for its static method
from ..llm_query_api_batch.llm_query_api_batch_node import LLMQueryAPIBatchNode, DEFAULT_LLM_API_URL, DEFAULT_LLM_MODEL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, DEFAULT_BATCH_SIZE, DEFAULT_TEMPERATURE

# Default system prompt specific to this node's batch filtering purpose
SYSTEM_PROMPT_FILTER_BATCH = """You are an expert at analyzing ComfyUI nodes and determining their relevance to specific workflow tasks. Your job is to evaluate each node's description and determine how useful it would be for a given workflow goal. Please analyze the node based on: 1. Direct relevance to the workflow goal 2. Utility as a supporting node for the workflow 3. Specific features that would help achieve the goal. Rate the node's applicability from 0-100 where: 0-20: Not relevant, 21-40: Marginally relevant, 41-60: Moderately useful, 61-80: Very useful, 81-100: Essential for this workflow.

You will be given multiple nodes to analyze in one request. You must respond with only a valid JSON array containing one JSON object (with 'score' and 'reason') for each node provided in the prompt, in the same order. Format: [{'score': number, 'reason': 'string'}, ...]"""


class FilterNodesNode:
    """
    Parses node documentation, evaluates relevance using an LLM
    (via LLMQueryAPIBatchNode's static method), filters based on score,
    and formats the output markdown.
    """
    NODE_OUTPUT_DIR = Path(__file__).parent / "output"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("*", {}),
                "node_markdown_content": ("STRING", {"multiline": True}),
                "workflow_prompt": ("STRING", {"multiline": True, "default": "Describe the desired workflow..."}),
                "relevance_threshold": ("INT", {"default": 40, "min": 0, "max": 100}),
                "output_filename_prefix": ("STRING", {"default": "filtered_nodes"}),
            },
            "optional": {
                 "llm_batch_size": ("INT", {"default": DEFAULT_BATCH_SIZE, "min": 1, "max": 16}),
                 "batch_system_prompt": ("STRING", {"multiline": True, "default": SYSTEM_PROMPT_FILTER_BATCH}),
                 "api_url": ("STRING", {"default": DEFAULT_LLM_API_URL}),
                 "model": ("STRING", {"default": DEFAULT_LLM_MODEL}),
                 "temperature": ("FLOAT", {"default": DEFAULT_TEMPERATURE, "min": 0.0, "max": 2.0, "step": 0.1}),
                 "max_retries": ("INT", {"default": DEFAULT_MAX_RETRIES, "min": 0}),
                 "timeout": ("INT", {"default": DEFAULT_TIMEOUT, "min": 10}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("filtered_markdown", "output_filepath")
    FUNCTION = "filter_nodes_batch"
    CATEGORY = "utils/docs"
    OUTPUT_NODE = True

    def __init__(self):
        self.output_dir = FilterNodesNode.NODE_OUTPUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # --- Helper Functions (Adapted from original script) ---

    def parse_node_metadata(self, text: str) -> dict:
        """Extract metadata from node description section"""
        metadata = {}
        lines = text.split('\n')
        # Look for specific patterns used in list_installed_nodes markdown
        for line in lines:
             if line.startswith('**Source:**'):
                  match = re.search(r'`(.*?)`', line)
                  if match: metadata['module'] = match.group(1)
             elif line.startswith('**Author:**'): # If available from manager list markdown
                  metadata['author'] = line.split('**Author:**')[1].strip()
             elif line.startswith('**Repository/Reference:**'):
                  match = re.search(r'\[(.*?)\]\(.*?\)', line) # Link format
                  if match: metadata['repository'] = match.group(1)
                  else: metadata['repository'] = line.split('**Repository/Reference:**')[1].strip() # Plain text format
             elif line.startswith('**Install Type:**'): # If available
                  metadata['install_type'] = line.split('**Install Type:**')[1].strip()
        return metadata


    def parse_node_blocks(self, text: str) -> List[Tuple[str, str, dict]]:
        """Parse markdown text into list of (node_name, full_block_text, metadata) tuples"""
        nodes = []
        current_node_name = None
        current_node_lines = []
        node_delimiter = "\n---\n" # Assuming this separates nodes in input markdown

        # Split by the delimiter, handling potential starting/ending delimiters
        blocks = [block.strip() for block in text.split(node_delimiter) if block.strip()]

        for block in blocks:
             lines = block.split('\n')
             node_name = "Unknown Node"
             metadata_text = block # Assume whole block might contain metadata initially
             description = block # Default description is the whole block

             # Find the node name (usually in H3)
             for line in lines:
                  if line.startswith('### '):
                       # Extract name, potentially including the backticked name
                       match = re.match(r'###\s*(.*?)(?:\s*`\((.*?)\)`)?', line)
                       if match:
                            node_name = match.group(1).strip()
                            # Prefer backticked name if present
                            if match.group(2):
                                node_name = match.group(2).strip()
                       break # Found the header

             # Simple approach: metadata is everything after the first H4 or before it if no H4
             desc_lines = []
             metadata_lines = []
             found_h4 = False
             for line in lines:
                  if line.startswith("####"):
                      found_h4 = True
                  if found_h4:
                       metadata_lines.append(line)
                  else:
                       desc_lines.append(line)

             description = "\n".join(desc_lines).strip()
             metadata_text = "\n".join(metadata_lines).strip()

             # Re-parse metadata from the identified section or whole block
             metadata = self.parse_node_metadata(metadata_text if metadata_lines else block)
             nodes.append((node_name, block, metadata)) # Store the original full block text

        return nodes

    def format_filtered_markdown(self, scored_nodes: List[Dict], original_prompt: str, threshold: int) -> str:
        """Formats the filtered nodes into a markdown string."""
        output_lines = [
            f"# Filtered Nodes for Workflow Prompt:\n",
            f"> {original_prompt}\n",
            f"(Threshold: {threshold}+)\n",
            "---", "" # Separator
        ]

        if not scored_nodes:
            output_lines.append("*No nodes met the relevance threshold.*")
            return "\n".join(output_lines)

        # Sort by score descending
        sorted_nodes = sorted(scored_nodes, key=lambda x: x['score'], reverse=True)

        for node_info in sorted_nodes:
            output_lines.append(f"## Score: {node_info['score']}/100\n")
            output_lines.append(f"**Reason:** {node_info['reason']}\n")
            # Append the original node block
            output_lines.append(node_info['original_block'])
            output_lines.append("\n---\n") # Separator

        return "\n".join(output_lines)


    # --- Node Execution Method (Batch Processing) ---
    def filter_nodes_batch(self, trigger=None, node_markdown_content: str = "", workflow_prompt: str = "", relevance_threshold: int = 40, output_filename_prefix: str = "filtered_nodes", llm_batch_size: int = DEFAULT_BATCH_SIZE, batch_system_prompt: str = SYSTEM_PROMPT_FILTER_BATCH, api_url: str = DEFAULT_LLM_API_URL, model: str = DEFAULT_LLM_MODEL, temperature: float = DEFAULT_TEMPERATURE, max_retries: int = DEFAULT_MAX_RETRIES, timeout: int = DEFAULT_TIMEOUT):
        """Parses markdown, generates prompts, calls LLM batch static method, filters, and formats."""
        if not node_markdown_content:
            return ("Error: Input markdown content is empty.", "Error: No input content")
        if not workflow_prompt:
             return ("Error: Workflow prompt is empty.", "Error: No prompt")

        print(f"Filtering nodes based on prompt: '{workflow_prompt[:50]}...'")
        nodes_to_evaluate = self.parse_node_blocks(node_markdown_content)
        total_nodes = len(nodes_to_evaluate)
        print(f"Parsed {total_nodes} node blocks to evaluate.")

        if total_nodes == 0:
            return ("*No node blocks found in the input markdown.*", "Error: No nodes parsed")

        # Generate Prompts
        llm_prompts = []
        for node_name, node_block_text, _ in nodes_to_evaluate:
            # Inline the prompt generation logic here
            llm_prompt = f"""Workflow Goal: {workflow_prompt}

Node Name: {node_name}

Node Information Block:
--- START BLOCK ---
{node_block_text}
--- END BLOCK ---

Evaluate this node's relevance and utility for the specified workflow goal based *only* on the information provided in the block."""
            llm_prompts.append(llm_prompt)

        # Query LLM using imported static batch logic
        print(f"Querying LLM via LLMQueryAPIBatchNode static method...")
        llm_results = LLMQueryAPIBatchNode._static_query_llm_batch(
            prompts_list=llm_prompts,
            system_prompt=batch_system_prompt,
            api_url=api_url, model=model, temperature=temperature,
            batch_size=llm_batch_size, max_retries=max_retries, timeout=timeout
        )

        # Process results
        filtered_nodes_info = []
        if len(llm_results) != total_nodes:
             print(f"Warning: Mismatch between prompts ({total_nodes}) and results ({len(llm_results)}). Padding.")
             while len(llm_results) < total_nodes: llm_results.append({"score": 0, "reason": "Missing LLM response"})

        for i, (node_name, block, metadata) in enumerate(nodes_to_evaluate):
            result = llm_results[i]
            # Check for error key from internal batch logic first
            if result.get("error"):
                 print(f"Skipping node '{node_name}' due to processing error: {result['error']}")
                 continue
            score = result.get("score", 0)
            reason = result.get("reason", "No reason provided.")

            # Ensure score is an integer
            try:
                 score = int(score)
            except (ValueError, TypeError):
                 print(f"Warning: Invalid score '{score}' for node '{node_name}'. Setting to 0.")
                 score = 0


            if score >= relevance_threshold:
                filtered_nodes_info.append({
                    "name": node_name,
                    "original_block": block, # Store original block text
                    "score": score,
                    "reason": reason,
                    **metadata # Include parsed metadata
                })

        print(f"Found {len(filtered_nodes_info)} nodes meeting threshold {relevance_threshold}.")

        # Format output markdown
        filtered_markdown_output = self.format_filtered_markdown(
             filtered_nodes_info, workflow_prompt, relevance_threshold
        )

        # Save to file
        safe_prefix = re.sub(r'[^\w\-_\. ]', '_', output_filename_prefix)
        # Create a more descriptive filename if possible
        prompt_slug = re.sub(r'[^\w\-]+', '_', workflow_prompt[:25]).strip('_')
        output_filename = f"{safe_prefix}_filtered_{prompt_slug}.md"
        output_filepath = self.output_dir / output_filename

        try:
            output_filepath.write_text(filtered_markdown_output, encoding="utf-8")
            print(f"Filtered nodes saved to: {output_filepath}")
        except Exception as e:
            print(f"Error saving filtered nodes file: {e}")
            return (f"Error saving file: {e}", f"Error: {e}")

        return (filtered_markdown_output, str(output_filepath.resolve()))


    # --- Standalone Execution Capability (Optional) ---
    # Keep if you still want to run this script independently

    @classmethod
    def execute_standalone(cls, input_file: Path, output_file: Path, prompt: str, threshold: int = 40, batch_size: int = 4):
        """Run the filtering process from the command line."""
        print(f"\n--- Standalone Execution ---")
        print(f"Input: {input_file}, Output: {output_file}, Prompt: '{prompt[:60]}...', Threshold: {threshold}, Batch: {batch_size}")

        if not input_file.exists():
            print(f"Error: Input file not found: {input_file}")
            return

        try:
            markdown_content = input_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading input file: {e}")
            return

        # Parse nodes directly using instance method (needs instantiation now)
        instance = cls() # Instantiate to use parse_node_blocks
        nodes_to_evaluate = instance.parse_node_blocks(markdown_content)
        total_nodes = len(nodes_to_evaluate)
        print(f"Parsed {total_nodes} node blocks.")
        if total_nodes == 0:
            print("No nodes found in input.")
            return

        # Generate Prompts (Inlined)
        llm_prompts = []
        for node_name, node_block_text, _ in nodes_to_evaluate:
            llm_prompt = f"""Workflow Goal: {prompt}

Node Name: {node_name}

Node Information Block:
--- START BLOCK ---
{node_block_text}
--- END BLOCK ---

Evaluate this node's relevance and utility for the specified workflow goal based *only* on the information provided in the block."""
            llm_prompts.append(llm_prompt)

        # Query LLM (using default params for simplicity in standalone)
        print(f"Querying LLM with batch size {batch_size}...")
        llm_results = LLMQueryAPIBatchNode._static_query_llm_batch(
            prompts_list=llm_prompts,
            system_prompt=SYSTEM_PROMPT_FILTER_BATCH,
            api_url=DEFAULT_LLM_API_URL,
            model=DEFAULT_LLM_MODEL,
            temperature=DEFAULT_TEMPERATURE,
            batch_size=batch_size,
            max_retries=DEFAULT_MAX_RETRIES,
            timeout=DEFAULT_TIMEOUT
        )

        # Process results
        filtered_nodes_info = []
        if len(llm_results) != total_nodes:
             print(f"Warning: Mismatch between prompts ({total_nodes}) and results ({len(llm_results)}). Padding.")
             while len(llm_results) < total_nodes: llm_results.append({"score": 0, "reason": "Missing LLM response"})

        for i, (node_name, block, metadata) in enumerate(nodes_to_evaluate):
            result = llm_results[i]
            # Check for error key from internal batch logic first
            if result.get("error"):
                 print(f"Skipping node '{node_name}' due to processing error: {result['error']}")
                 continue
            score = result.get("score", 0)
            reason = result.get("reason", "No reason provided.")

            # Ensure score is an integer
            try:
                 score = int(score)
            except (ValueError, TypeError):
                 print(f"Warning: Invalid score '{score}' for node '{node_name}'. Setting to 0.")
                 score = 0


            if score >= threshold:
                filtered_nodes_info.append({
                    "name": node_name,
                    "original_block": block, # Store original block text
                    "score": score,
                    "reason": reason,
                    **metadata # Include parsed metadata
                })

        print(f"Found {len(filtered_nodes_info)} nodes meeting threshold {threshold}.")

        # Format output markdown
        filtered_markdown_output = self.format_filtered_markdown(
             filtered_nodes_info, prompt, threshold
        )

        # Save to file
        safe_prefix = re.sub(r'[^\w\-_\. ]', '_', output_file.stem)
        # Create a more descriptive filename if possible
        prompt_slug = re.sub(r'[^\w\-]+', '_', prompt[:25]).strip('_')
        output_filename = f"{safe_prefix}_filtered_{prompt_slug}.md"
        output_filepath = output_file

        try:
            output_filepath.write_text(filtered_markdown_output, encoding="utf-8")
            print(f"Standalone output written to: {output_filepath}")
        except Exception as e:
            print(f"Error writing standalone output file: {e}")


# --- Main block for standalone execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='(Standalone) Filter ComfyUI node markdown using LLM.')
    parser.add_argument('--input', required=True, help='Input markdown file path.')
    parser.add_argument('--output', required=True, help='Output markdown file path.')
    parser.add_argument('--prompt', required=True, help='Workflow goal prompt.')
    parser.add_argument('--threshold', type=int, default=40, help='Relevance score threshold.')
    parser.add_argument('--batch-size', type=int, default=4, help='LLM batch size.')
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    FilterNodesNode.execute_standalone(
        input_file=input_path,
        output_file=output_path,
        prompt=args.prompt,
        threshold=args.threshold,
        batch_size=args.batch_size
    ) 