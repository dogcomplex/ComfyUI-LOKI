import os
import folder_paths
# Updated import relative to the current file's directory
from .glamour_utils import GlamourImageManager

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        # Add a boolean widget to control the overall feature
        return {
            "required": {
                "enable_controls": ("BOOLEAN", {"default": True}),
                "glamour_state": (["All Glamoured", "Mixed", "All Veiled"],),
                "transparency": ("BOOLEAN", {"default": True, "label_on": "Transparent Overlay", "label_off": "Opaque Overlay"})
            }
        }

    RETURN_TYPES = () # This node primarily affects the UI, doesn't return workflow data
    FUNCTION = "do_nothing" # Needs a function, even if it does nothing in the backend flow
    CATEGORY = "UI"
    OUTPUT_NODE = True # Crucial: Allows it to interact with the UI framework
    NODE_NAME = "Glamour 🦊" # Keep the original internal name for JS matching if needed

    def __init__(self):
        # Utils might handle path creation now, but keep reference if needed
        self.glamour_dir = GlamourImageManager.BASE_OUTPUT_DIR
        os.makedirs(self.glamour_dir, exist_ok=True)

    def do_nothing(self, **kwargs):
        # This node's primary function is handled by its JavaScript counterpart
        # and the class methods registered as routes.
        return ()

    # --- Server Routes ---
    # These methods are called via HTTP requests from the JS frontend

    @classmethod
    def get_glamour_path(cls, image_id=None, node_type=None):
        """API endpoint to get the path for a glamour image."""
        if not image_id:
            # Use Flask or similar for proper HTTP responses if available,
            # otherwise return dicts which ComfyUI might handle.
            # For now, stick to dicts for simplicity.
            return {"success": False, "error": "No image_id provided"}

        try:
            path = GlamourImageManager.get_image_path(image_id, node_type)
            # Ensure path is absolute before making it relative
            abs_path = os.path.abspath(path)
            output_dir_abs = os.path.abspath(folder_paths.get_output_directory())

            if abs_path.startswith(output_dir_abs):
                 relative_path = os.path.relpath(abs_path, output_dir_abs)
                 # Normalize path separators for web
                 relative_path = relative_path.replace(os.sep, '/')
            else:
                 # Handle cases where the image might be outside the standard output dir (if applicable)
                 # This might indicate an issue or require different handling.
                 print(f"Warning: Glamour image path {abs_path} is outside output directory {output_dir_abs}")
                 # Fallback or error as appropriate for your setup
                 # For now, let's report success but maybe an empty path or flag this?
                 # Returning the absolute might be a security risk. Let's signal non-standard location.
                 return {
                     "success": True,
                     "path": None, # Indicate it's not relative to output
                     "absolute_path_warning": True, # Flag for frontend awareness
                     "exists": os.path.exists(abs_path)
                 }


            return {
                "success": True,
                "path": relative_path,
                "exists": os.path.exists(abs_path)
            }
        except Exception as e:
            print(f"Error in get_glamour_path: {e}")
            return {"success": False, "error": str(e)}


    @classmethod
    def check_glamour_timestamp(cls, image_id=None, node_type=None):
        """API endpoint to check the timestamp of a glamour image."""
        if not image_id:
            return {"success": False, "error": "No image_id provided"}

        try:
            path = GlamourImageManager.get_image_path(image_id, node_type)
            abs_path = os.path.abspath(path)
            output_dir_abs = os.path.abspath(folder_paths.get_output_directory())

            if os.path.exists(abs_path):
                timestamp = os.path.getmtime(abs_path)
                relative_path = None
                abs_warning = False
                if abs_path.startswith(output_dir_abs):
                     relative_path = os.path.relpath(abs_path, output_dir_abs).replace(os.sep, '/')
                else:
                    print(f"Warning: Timestamp check for non-output path: {abs_path}")
                    abs_warning = True


                return {
                    "success": True,
                    "timestamp": timestamp,
                    "path": relative_path, # Can be None if outside output dir
                    "absolute_path_warning": abs_warning,
                }
            else:
                return {"success": False, "error": "File not found"}
        except Exception as e:
            print(f"Error in check_glamour_timestamp: {e}")
            return {"success": False, "error": str(e)} 