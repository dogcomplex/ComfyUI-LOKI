from .Glamour import GlamourNode

# Register the custom node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "Glamour 🦊": GlamourNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Glamour 🦊": "Glamour 🦊"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
__version__ = "1.0.0"
__author__ = "LOKI🦊"