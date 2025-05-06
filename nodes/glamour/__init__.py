import json
import os

from .glamour_node import GlamourNode

# Load config to get names
config_path = os.path.join(os.path.dirname(__file__), 'glamour.json')
try:
    with open(config_path, 'r') as f:
        config = json.load(f)
    NODE_NAME_INTERNAL = config.get('node_name_internal', 'GlamourNode_Fallback')
    NODE_DISPLAY_NAME = config.get('node_display_name', 'Glamour_Fallback (LOKI)')
except Exception as e:
    print(f"[LOKI Glamour Init Error] Could not load or parse glamour.json: {e}")
    NODE_NAME_INTERNAL = 'GlamourNode_Error'
    NODE_DISPLAY_NAME = 'Glamour_Error (LOKI)'

NODE_CLASS_MAPPINGS = {
    NODE_NAME_INTERNAL: GlamourNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME_INTERNAL: NODE_DISPLAY_NAME
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 