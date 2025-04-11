from .filter_nodes_node import FilterNodesNode

NODE_CLASS_MAPPINGS = {
    "FilterNodesLLM": FilterNodesNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "FilterNodesLLM": "Filter Nodes (LLM)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 