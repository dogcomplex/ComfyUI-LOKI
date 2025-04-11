from .llm_query_api_node import LLMQueryAPINode

NODE_CLASS_MAPPINGS = {
    "LLMQueryAPI": LLMQueryAPINode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMQueryAPI": "LLM Query API (Single)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 