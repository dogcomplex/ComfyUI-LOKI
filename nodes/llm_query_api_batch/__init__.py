from .llm_query_api_batch_node import LLMQueryAPIBatchNode

NODE_CLASS_MAPPINGS = {
    "LLMQueryAPIBatch": LLMQueryAPIBatchNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMQueryAPIBatch": "LLM Query API (Batch)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 