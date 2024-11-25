import os
import hashlib
import json
import re

class GlamourImageManager:
    BASE_OUTPUT_DIR = "output/Glamour"
    
    @staticmethod
    def to_snake_case(text: str) -> str:
        return re.sub(r'[-\s]+', '_', re.sub(r'[^\w\s-]', '', text)).strip().lower()
    
    @staticmethod
    def generate_image_id(node_id: str, node_type: str, input_values: dict) -> str:
        content_str = json.dumps({"node_id": node_id, "inputs": input_values}, sort_keys=True)
        hash_value = hashlib.sha256(content_str.encode()).hexdigest()[:8]
        return f"{GlamourImageManager.to_snake_case(node_type)}_{node_id}_{hash_value}"
    
    @staticmethod
    def get_image_path(image_id: str, node_type: str = None) -> str:
        specific_path = os.path.join(GlamourImageManager.BASE_OUTPUT_DIR, f"{image_id}.png")
        if os.path.exists(specific_path):
            return specific_path
            
        if node_type:
            default_path = os.path.join(
                GlamourImageManager.BASE_OUTPUT_DIR,
                f"{GlamourImageManager.to_snake_case(node_type)}.png"
            )
            if os.path.exists(default_path):
                return default_path
                
        return specific_path