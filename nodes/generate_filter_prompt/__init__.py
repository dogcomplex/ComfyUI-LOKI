from .generate_filter_prompt_node import GenerateFilterPromptNode

NODE_CLASS_MAPPINGS = {
    "GenerateFilterPromptLLM": GenerateFilterPromptNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "GenerateFilterPromptLLM": "Generate Node Filter Prompt (LLM)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 