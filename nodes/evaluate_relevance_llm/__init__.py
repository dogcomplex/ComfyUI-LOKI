from .evaluate_relevance_llm_node import EvaluateRelevanceLLMNode

NODE_CLASS_MAPPINGS = {
    "EvaluateRelevanceLLM": EvaluateRelevanceLLMNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "EvaluateRelevanceLLM": "Evaluate Node Relevance (LLM)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 