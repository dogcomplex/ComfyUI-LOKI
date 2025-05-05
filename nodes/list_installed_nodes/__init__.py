from .list_installed_nodes_node import ListInstalledNodes

NODE_CLASS_MAPPINGS = {
    "LokiListInstalledNodes": ListInstalledNodes
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LokiListInstalledNodes": "📜🔍 List Installed Nodes (LOKI)"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 