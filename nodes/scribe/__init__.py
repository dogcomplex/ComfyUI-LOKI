from .scribe_node import ScribeNode

NODE_CLASS_MAPPINGS = {
    "Scribe": ScribeNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Scribe": "Workflow Scribe"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 