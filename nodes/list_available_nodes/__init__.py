from .list_available_nodes_node import ListAvailableNodes

NODE_CLASS_MAPPINGS = {
    "LokiListAvailableNodes": ListAvailableNodes
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LokiListAvailableNodes": "🌐🔍 List Available Nodes (LOKI)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 