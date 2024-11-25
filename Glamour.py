import os
from .glamour_utils import GlamourImageManager

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "node_id": ("STRING", {"default": ""}),  # ComfyUI will populate this
                "text": ("STRING", {"default": "Overlay Active"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = 'process'
    CATEGORY = 'UI'
    NODE_NAME = 'Glamour 🦊'

    def __init__(self):
        GlamourImageManager.ensure_output_directory()

    def process(self, node_id, text):
        # Generate unique ID for this node's configuration
        image_id = GlamourImageManager.generate_image_id(
            node_id=node_id,
            node_type=self.NODE_NAME,
            input_values={"text": text}
        )
        
        # Get the path where the image should be, with fallback support
        image_path = GlamourImageManager.get_image_path(image_id, self.NODE_NAME)
        
        return (image_id,)

    @classmethod
    def WEB_DIRECTORY(cls):
        return os.path.join(os.path.dirname(__file__), "js")
