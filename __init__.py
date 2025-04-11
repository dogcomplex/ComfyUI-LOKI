from .nodes.glamour import GlamourNode

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

# Import mappings from all node submodules within the 'nodes' directory
from .nodes.glamour import NODE_CLASS_MAPPINGS as glamour_mappings, NODE_DISPLAY_NAME_MAPPINGS as glamour_display_mappings
from .nodes.scribe import NODE_CLASS_MAPPINGS as scribe_mappings, NODE_DISPLAY_NAME_MAPPINGS as scribe_display_mappings
from .nodes.list_installed_nodes import NODE_CLASS_MAPPINGS as list_installed_mappings, NODE_DISPLAY_NAME_MAPPINGS as list_installed_display_mappings
from .nodes.list_available_nodes import NODE_CLASS_MAPPINGS as list_available_mappings, NODE_DISPLAY_NAME_MAPPINGS as list_available_display_mappings
from .nodes.filter_nodes import NODE_CLASS_MAPPINGS as filter_nodes_mappings, NODE_DISPLAY_NAME_MAPPINGS as filter_nodes_display_mappings
from .nodes.generate_filter_prompt import NODE_CLASS_MAPPINGS as generate_prompt_mappings, NODE_DISPLAY_NAME_MAPPINGS as generate_prompt_display_mappings
from .nodes.evaluate_relevance_llm import NODE_CLASS_MAPPINGS as evaluate_llm_mappings, NODE_DISPLAY_NAME_MAPPINGS as evaluate_llm_display_mappings
from .nodes.llm_query_api import NODE_CLASS_MAPPINGS as llm_query_api_mappings, NODE_DISPLAY_NAME_MAPPINGS as llm_query_api_display_mappings
from .nodes.llm_query_api_batch import NODE_CLASS_MAPPINGS as llm_query_api_batch_mappings, NODE_DISPLAY_NAME_MAPPINGS as llm_query_api_batch_display_mappings


# Combine all mappings
NODE_CLASS_MAPPINGS = {
    **glamour_mappings,
    **scribe_mappings,
    **list_installed_mappings,
    **list_available_mappings,
    **filter_nodes_mappings,
    **generate_prompt_mappings,
    **evaluate_llm_mappings,
    **llm_query_api_mappings,
    **llm_query_api_batch_mappings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **glamour_display_mappings,
    **scribe_display_mappings,
    **list_installed_display_mappings,
    **list_available_display_mappings,
    **filter_nodes_display_mappings,
    **generate_prompt_display_mappings,
    **evaluate_llm_display_mappings,
    **llm_query_api_display_mappings,
    **llm_query_api_batch_display_mappings,
}

# WEB_DIRECTORY remains relative to the root package directory
WEB_DIRECTORY = "js"

print(f"✅ Loaded ComfyUI-LOKI nodes ({len(NODE_CLASS_MAPPINGS)} total) from 'nodes' subdirectory.")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']


# --- PIP Requirements (Keep existing logic) ---
import importlib
import subprocess
import sys
import os

if "pytest" not in sys.modules and os.environ.get("SKIP_PIP_INSTALL") != "1":
    print("🐍 Checking LOKI PIP requirements...")
    REQUIRED_PACKAGES = [
        {"pip_package": "mistralai", "import_name": "mistralai"},
        {"pip_package": "modelscope", "import_name": "modelscope"},
        {"pip_package": "moviepy", "import_name": "moviepy"},
        {"pip_package": "git+https://github.com/THUDM/ImageReward.git", "import_name": "ImageReward"},
        {"pip_package": "requests", "import_name": "requests"},
    ]
    for pkg_info in REQUIRED_PACKAGES:
        pip_package = pkg_info["pip_package"]
        import_name = pkg_info["import_name"]
        try: importlib.import_module(import_name)
        except ModuleNotFoundError:
            print(f"Installing {import_name} ({pip_package})...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", pip_package], check=True, capture_output=True, text=True)
                print(f"  + {import_name} installed successfully.")
            except subprocess.CalledProcessError as e: print(f"Error installing {import_name}:\n{e.stderr}\nPlease install '{pip_package}' manually.")
            except Exception as e: print(f"Unexpected error during pip install for {import_name}: {e}")
# --- End PIP Requirements ---
