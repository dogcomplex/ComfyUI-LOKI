import os
import folder_paths
from .glamour_utils import GlamourImageManager

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"glamour_on": ("BOOLEAN", {"default": True})}}

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("glamour_on",)
    FUNCTION = "process"
    CATEGORY = "UI"
    OUTPUT_NODE = True
    NODE_NAME = "Glamour 🦊"

    def __init__(self):
        self.glamour_dir = os.path.join(folder_paths.get_output_directory(), "Glamour")
        os.makedirs(self.glamour_dir, exist_ok=True)

    def process(self, **kwargs):
        return ("glamour_active",)

    @classmethod
    def ROUTES(cls):
        return {"get_glamour_path": cls.get_glamour_path}

    @classmethod
    def get_glamour_path(cls, image_id=None, node_type=None):
        if not image_id:
            return {"success": False, "error": "No image_id provided"}
        
        path = GlamourImageManager.get_image_path(image_id, node_type)
        relative_path = os.path.relpath(path, folder_paths.get_output_directory())
        
        return {
            "success": True,
            "path": relative_path,
            "exists": os.path.exists(path)
        }
