import gradio as gr
import os
import folder_paths

class GlamourNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "Overlay Active"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = 'process'
    CATEGORY = 'UI'
    NODE_NAME = 'Glamour 🦊'

    def process(self, text):
        print("Glamour is running!")
        return (text,)

    @classmethod
    def WEB_DIRECTORY(cls):
        return os.path.join(os.path.dirname(__file__), "js")
