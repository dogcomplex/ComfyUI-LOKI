import os
import hashlib
import json
import re

class GlamourImageManager:
    BASE_OUTPUT_DIR = "output/Glamour"
    
    @staticmethod
    def ensure_output_directory():
        os.makedirs(GlamourImageManager.BASE_OUTPUT_DIR, exist_ok=True)
    
    @staticmethod
    def to_snake_case(text: str) -> str:
        # Remove emojis and special characters
        text = re.sub(r'[^\w\s-]', '', text)
        # Replace spaces and hyphens with underscores
        text = re.sub(r'[-\s]+', '_', text)
        # Convert to lowercase
        return text.strip().lower()
    
    @staticmethod
    def generate_image_id(node_id: str, node_type: str, input_values: dict) -> str:
        # Create a deterministic hash from node info and inputs
        content = {
            "node_id": node_id,
            "inputs": input_values
        }
        content_str = json.dumps(content, sort_keys=True)
        hash_value = hashlib.sha256(content_str.encode()).hexdigest()[:8]
        
        # Create prefix from node type
        prefix = GlamourImageManager.to_snake_case(node_type)
        
        # Return full identifier
        return f"{prefix}_{node_id}_{hash_value}"
    
    @staticmethod
    def get_image_path(image_id: str, node_type: str = None) -> str:
        """
        Returns the first available image path in order of preference:
        1. {prefix}_{hash}.png (specific configuration)
        2. {prefix}.png (default for node type)
        """
        specific_path = os.path.join(GlamourImageManager.BASE_OUTPUT_DIR, f"{image_id}.png")
        
        if os.path.exists(specific_path):
            return specific_path
            
        # Try fallback to node type default if provided
        if node_type:
            default_path = os.path.join(
                GlamourImageManager.BASE_OUTPUT_DIR,
                f"{GlamourImageManager.to_snake_case(node_type)}.png"
            )
            if os.path.exists(default_path):
                return default_path
                
        return specific_path  # Return specific path even if it doesn't exist 