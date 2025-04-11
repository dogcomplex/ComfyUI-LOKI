import os
import hashlib
import json
import re
import folder_paths # Need this for BASE_OUTPUT_DIR resolution

class GlamourImageManager:
    # Resolve path relative to ComfyUI's output directory
    BASE_OUTPUT_DIR = os.path.abspath(os.path.join(folder_paths.get_output_directory(), "Glamour"))
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True) # Ensure directory exists on module load

    @staticmethod
    def to_snake_case(text: str) -> str:
        if not isinstance(text, str):
             text = str(text) # Attempt to convert non-strings
        return re.sub(r'[-\s]+', '_', re.sub(r'[^\w\s-]', '', text)).strip().lower()

    @staticmethod
    def generate_image_id(node_id: str, node_type: str, node_hash: str) -> str:
         """Generates an image ID using node type, ID, and a hash."""
         # Using the hash passed from JS ensures consistency with frontend state
         return f"{GlamourImageManager.to_snake_case(node_type)}_{node_id}_{node_hash}"

    @staticmethod
    def get_image_path(image_id: str, node_type: str = None) -> str:
        """
        Finds the most specific existing image path.
        Checks for specific ID (webp/png), then default type (webp/png).
        Returns the expected path for the specific ID png if none exist.
        """
        base_name_specific = os.path.join(GlamourImageManager.BASE_OUTPUT_DIR, image_id)
        paths_to_check = [
            f"{base_name_specific}.webp",
            f"{base_name_specific}.png",
        ]

        if node_type:
            base_name_default = os.path.join(
                GlamourImageManager.BASE_OUTPUT_DIR,
                GlamourImageManager.to_snake_case(node_type)
            )
            paths_to_check.extend([
                f"{base_name_default}.webp",
                f"{base_name_default}.png",
            ])

        for path in paths_to_check:
            if os.path.exists(path):
                return path

        # If none exist, return the path where the specific PNG *should* be
        # (this is the path JS will try first if generating an image)
        return f"{base_name_specific}.png" 