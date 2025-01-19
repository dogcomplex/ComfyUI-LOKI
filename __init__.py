from .Glamour import GlamourNode

# Register the custom node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "Glamour 🦊": GlamourNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Glamour 🦊": "Glamour 🦊"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
__version__ = "1.0.0"
__author__ = "LOKI🦊"



# AUTO-IMPORTING VARIOUS PIP PACKAGES: ====================

import importlib
import subprocess
import sys

REQUIRED_PACKAGES = [
    "git+https://github.com/THUDM/ImageReward.git",
    "mistralai",
    "sageattention",
    "modelscope",
    "moviepy"
]

for pkg in REQUIRED_PACKAGES:
    # Check if package name is installed (a quick & dirty approach):
    pkg_name = pkg.split("==")[0].split("/")[-1] if "@" not in pkg else pkg
    try:
        importlib.import_module(pkg_name)
    except ModuleNotFoundError:
        # Attempt to install:
        subprocess.run([sys.executable, "-m", "pip", "install", pkg])
