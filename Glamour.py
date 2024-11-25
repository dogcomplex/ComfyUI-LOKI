import os
from .glamour_utils import GlamourImageManager

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}  # No inputs needed

    RETURN_TYPES = tuple()  # No outputs needed
    FUNCTION = 'process'
    CATEGORY = 'UI'
    NODE_NAME = 'Glamour 🦊'

    def __init__(self):
        GlamourImageManager.ensure_output_directory()

    def process(self):
        # This node doesn't need to process anything
        return tuple()

    @classmethod
    def WEB_DIRECTORY(cls):
        return os.path.join(os.path.dirname(__file__), "js")
