import re

class GenerateFilterPromptNode:
    """
    Generates a formatted text prompt suitable for an LLM
    to evaluate a node's relevance to a workflow goal.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "workflow_prompt": ("STRING", {"multiline": True, "default": "Describe the desired workflow..."}),
                "node_name": ("STRING", {"default": "Unknown Node"}),
                # Takes the full block text parsed previously
                "node_block_text": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("llm_prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "utils/llm"
    OUTPUT_NODE = False # This is an intermediate processing node

    def generate_prompt(self, workflow_prompt: str, node_name: str, node_block_text: str) -> tuple[str]:
        """Creates the specific prompt for the LLM."""
        # Basic validation
        if not workflow_prompt:
            print("Warning: Workflow prompt is empty.")
        if not node_block_text:
            print(f"Warning: Node block text for '{node_name}' is empty.")

        # Construct the prompt (similar to the one previously in FilterNodesNode)
        llm_prompt = f"""Workflow Goal: {workflow_prompt}

Node Name: {node_name}

Node Information Block:
--- START BLOCK ---
{node_block_text}
--- END BLOCK ---

Evaluate this node's relevance and utility for the specified workflow goal based *only* on the information provided in the block."""

        return (llm_prompt,) 