import argparse
import json
import re
import requests
from pathlib import Path
from typing import List, Dict, Tuple

SYSTEM_PROMPT = """You are an expert at analyzing ComfyUI nodes and determining their relevance to specific workflow tasks. 
Your job is to evaluate each node's description and determine how useful it would be for a given workflow goal.

Please analyze the node based on:
1. Direct relevance to the workflow goal
2. Utility as a supporting node for the workflow
3. Specific features that would help achieve the goal

Rate the node's applicability from 0-100 where:
0-20: Not relevant
21-40: Marginally relevant
41-60: Moderately useful
61-80: Very useful
81-100: Essential for this workflow

Return only a JSON response in this format:
{
    "score": <0-100>,
    "reason": "<brief 1-2 sentence explanation>"
}"""

def create_llm_prompt(node_text: str, user_prompt: str) -> str:
    return f"""Workflow Goal: {user_prompt}

Node Information:
{node_text}

Evaluate this node's relevance and utility for the specified workflow goal."""

def query_llm(prompt: str, system_prompt: str) -> Dict:
    url = "http://localhost:12345/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "meta-llama2-3.1-8b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            try:
                # Attempt to parse the JSON response
                parsed_result = json.loads(content)
                if "score" in parsed_result and "reason" in parsed_result:
                    return parsed_result
                raise ValueError("Invalid JSON format")
            except (json.JSONDecodeError, ValueError):
                print(f"Attempt {retry_count + 1}: Invalid JSON response")
                retry_count += 1
                continue
                
        except Exception as e:
            print(f"Attempt {retry_count + 1}: Error querying LLM: {e}")
            retry_count += 1
            if retry_count == max_retries:
                return {"score": 0, "reason": "Error processing node after maximum retries"}
            continue
            
    return {"score": 0, "reason": "Error processing node after maximum retries"}

def query_llm_batch(prompts: List[str], system_prompt: str, batch_size: int = 4) -> List[Dict]:
    url = "http://localhost:12345/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    results = []
    
    for i in range(0, len(prompts), batch_size):
        batch_prompts = prompts[i:i + batch_size]
        
        # Create a more structured prompt format that explicitly requests JSON
        combined_prompt = "Analyze these nodes and return a JSON array. Each element should be a JSON object with 'score' (0-100) and 'reason' (string):\n\n"
        combined_prompt += "\n\n".join([
            f"Node {j+1}:\n```\n{p}\n```"
            for j, p in enumerate(batch_prompts)
        ])
        
        system_message = f"{system_prompt}\nYou must respond with only a valid JSON array in this format: [{{'score': number, 'reason': 'string'}}, ...]"
        
        data = {
            "model": "meta-llama2-3.1-8b-instruct",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": combined_prompt}
            ],
            "temperature": 0.3
        }
        
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                content = response.json()["choices"][0]["message"]["content"]
                
                # Clean up the response
                content = content.strip()
                
                # Find the first [ and last ]
                start_idx = content.find('[')
                end_idx = content.rfind(']')
                
                if start_idx != -1 and end_idx != -1:
                    content = content[start_idx:end_idx + 1]
                    content = content.replace("'", '"')
                    content = re.sub(r'(\w+):', r'"\1":', content)
                    
                    try:
                        parsed_results = json.loads(content)
                        if isinstance(parsed_results, list):
                            # Validate and fix each result
                            validated_results = []
                            for result in parsed_results:
                                if not isinstance(result, dict):
                                    result = {"score": 0, "reason": "Invalid response format"}
                                if "score" not in result:
                                    result["score"] = 0
                                if "reason" not in result:
                                    result["reason"] = "No reason provided"
                                validated_results.append(result)
                                
                            # Pad results if needed
                            while len(validated_results) < len(batch_prompts):
                                validated_results.append({"score": 0, "reason": "Missing response"})
                                
                            results.extend(validated_results[:len(batch_prompts)])
                            break
                    except json.JSONDecodeError as e:
                        print(f"Attempt {retry_count + 1}: JSON parsing error - {str(e)}")
                        retry_count += 1
                else:
                    print(f"Attempt {retry_count + 1}: No valid JSON array found in response")
                    retry_count += 1
                    
            except Exception as e:
                print(f"Attempt {retry_count + 1}: Error querying LLM - {str(e)}")
                retry_count += 1
                if retry_count == max_retries:
                    # Add placeholder results for failed batch
                    results.extend([{"score": 0, "reason": "Failed to process node"} for _ in batch_prompts])
                continue
    
    return results

def parse_node_metadata(text: str) -> dict:
    """Extract metadata from node description"""
    metadata = {}
    lines = text.split('\n')
    
    for line in lines:
        if '**Author:**' in line:
            metadata['author'] = line.split('**Author:**')[1].strip()
        elif '**Repository:**' in line:
            metadata['repository'] = line.split('**Repository:**')[1].strip()
        elif '**Install Type:**' in line:
            metadata['install_type'] = line.split('**Install Type:**')[1].strip()
    
    return metadata

def parse_node_block(text: str) -> List[Tuple[str, str, dict]]:
    """Parse markdown text into list of (node_name, description, metadata) tuples"""
    nodes = []
    current_node = ""
    current_desc = []
    
    for line in text.split('\n'):
        if line.startswith('### '):
            if current_node:
                desc_text = '\n'.join(current_desc)
                metadata = parse_node_metadata(desc_text)
                nodes.append((current_node, desc_text, metadata))
            current_node = line[4:].strip()
            current_desc = []
        elif current_node:
            current_desc.append(line)
            
    if current_node:
        desc_text = '\n'.join(current_desc)
        metadata = parse_node_metadata(desc_text)
        nodes.append((current_node, desc_text, metadata))
        
    return nodes

def count_nodes(text: str) -> int:
    """Count total number of nodes in markdown file"""
    return len([line for line in text.split('\n') if line.startswith('### ')])

def write_header(output_file: Path, total_nodes: int, prompt: str):
    """Write header information to output file"""
    batch_size = 4  # Processing multiple nodes at a time to improve speed
    est_time_per_query = 5  # seconds
    total_est_time = ((total_nodes / batch_size) * est_time_per_query) / 60  # minutes
    
    if not output_file.exists():
        header = f"""# Filtered Nodes for: {prompt}

Total Available Nodes: {total_nodes}
Batch Size: {batch_size}
Estimated Processing Time: {total_est_time:.1f} minutes

## Results
"""
        output_file.write_text(header)

def append_node_result(output_file: Path, node_info: dict):
    """Append a single node result to the output file with applicability section"""
    with output_file.open('a', encoding='utf-8') as f:
        node_text = f"""
### {node_info['name']}

**Description:**
{node_info['description']}

### Applicability

**Score:** {node_info['score']}/100

**Reason:** {node_info['reason']}

### Metadata
"""
        if 'author' in node_info:
            node_text += f"**Author:** {node_info['author']}\n"
        if 'repository' in node_info:
            node_text += f"**Repository:** {node_info['repository']}\n"
        if 'install_type' in node_info:
            node_text += f"**Install Type:** {node_info['install_type']}\n"
        
        node_text += "\n---\n"
        f.write(node_text)

def filter_nodes(input_file: Path, output_file: Path, prompt: str, threshold: int = 40, batch_size: int = 4):
    """Filter nodes based on relevance to prompt with incremental saving"""
    text = input_file.read_text(encoding='utf-8')
    nodes = parse_node_block(text)
    total_nodes = len(nodes)
    
    print(f"\nProcessing {input_file.name}")
    print(f"Total nodes to evaluate: {total_nodes}")
    
    # Initialize output file with header if it doesn't exist
    write_header(output_file, total_nodes, prompt)
    
    # Process in batches
    for i in range(0, len(nodes), batch_size):
        batch_nodes = nodes[i:i + batch_size]
        batch_prompts = [create_llm_prompt(f"{name}\n{desc}", prompt) for name, desc, _ in batch_nodes]
        
        print(f"Batch {i//batch_size + 1}/{(total_nodes + batch_size - 1)//batch_size}: ", end="", flush=True)
        results = query_llm_batch(batch_prompts, SYSTEM_PROMPT, batch_size)
        
        # Process results for this batch
        matched = 0
        for (node_name, desc, metadata), result in zip(batch_nodes, results):
            if result["score"] >= threshold:
                matched += 1
                node_info = {
                    "name": node_name,
                    "description": desc,
                    "score": result["score"],
                    "reason": result["reason"],
                    **metadata
                }
                append_node_result(output_file, node_info)
        print(f"{matched} matches")

def main():
    parser = argparse.ArgumentParser(description='Filter ComfyUI nodes based on workflow requirements')
    parser.add_argument('--prompt', required=True, help='Workflow goal/requirement')
    parser.add_argument('--batch-size', type=int, default=4, help='Number of nodes to process in each batch')
    parser.add_argument('--output-folder', required=True, help='Output folder for filtered node files')
    args = parser.parse_args()

    # Update base path to use current script location
    base_path = Path(__file__).parent
    output_path = Path(args.output_folder)
    
    # Process installed nodes
    filter_nodes(
        base_path / "INSTALLED_NODES.md",
        output_path / "installed_nodes_filtered.md",
        args.prompt,
        batch_size=args.batch_size
    )
    
    # Process available nodes
    filter_nodes(
        base_path / "AVAILABLE_NODES.md",
        output_path / "available_nodes_filtered.md",
        args.prompt,
        batch_size=args.batch_size
    )

if __name__ == "__main__":
    main() 