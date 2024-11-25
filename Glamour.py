import os
from .glamour_utils import GlamourImageManager

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "glamour_on": ("BOOLEAN", {"default": True})
            },
            "optional": {}   # Empty but needs to be defined
        }

    RETURN_TYPES = ("BOOLEAN",)  # Return a string (node ID)
    RETURN_NAMES = ("glamour_on",)
    FUNCTION = "process"
    CATEGORY = "UI"
    OUTPUT_NODE = True      # Mark as output node
    NODE_NAME = "Glamour 🦊"

    def __init__(self):
        GlamourImageManager.ensure_output_directory()

    def process(self, **kwargs):
        # Return the node's ID for tracking
        return ("glamour_active",)  # Return as tuple

    @classmethod
    def WEB_DIRECTORY(cls):
        return os.path.join(os.path.dirname(__file__), "js")
