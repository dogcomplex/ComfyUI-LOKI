import os
import sys
from pathlib import Path
import json
from collections import defaultdict
import importlib
import inspect
from typing import Dict, Any, List, Tuple
import re
import uuid
from io import StringIO # For generating strings

# Import the core logic from the separate file
from .list_installed_nodes import get_all_node_info

# Add ComfyUI root directory to Python path if running standalone,
# but usually not needed when run as a node.
# COMFY_ROOT = str(Path(__file__).parent.parent.parent.parent) # Adjust path depth
# sys.path.append(COMFY_ROOT)
# Instead, rely on ComfyUI's environment providing access to 'nodes'

# --- Node Definition ---

class ListInstalledNodes:
    """
    Lists installed ComfyUI nodes (built-in and custom) and outputs
    their information in various formats (JSON string, Markdown string, list of JSON, list of Markdown).
    """
    _class_last_node_info_hash = None # Class variable to store the hash

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
             "optional": {
                  "include_custom_nodes": ("BOOLEAN", {"default": True}),
             }
        }

    # Updated RETURN types and names
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("all_nodes_json", "summary_markdown", "node_json_list", "node_markdown_list")
    FUNCTION = "list_nodes"
    CATEGORY = "LOKI 🦊/System"
    OUTPUT_NODE = False # Not primarily writing files anymore

    # NODE_OUTPUT_DIR = Path(__file__).parent / "output" # Removed

    def __init__(self):
        # self.output_dir = ListInstalledNodes.NODE_OUTPUT_DIR # Removed
        # self.output_dir.mkdir(parents=True, exist_ok=True) # Removed
        pass # No instance setup needed now

    # --- Helper: Generate Markdown for a single node --- (Adapted from write_markdown_to_file)
    @staticmethod
    def generate_single_node_markdown(class_key: str, info: Dict[str, Any]) -> str:
        """Generates detailed markdown documentation string for a single node."""
        # Use StringIO to capture the markdown string
        md_stream = StringIO()

        node_name = info.get('node_name', class_key)
        display_name = info.get('display_name', node_name)

        if 'error' in info:
             md_stream.write(f"### {display_name} (`{node_name}` / `{class_key}`)\n\n")
             md_stream.write(f"**Error processing this node:** {info['error']}\n\n")
             md_stream.write("---\n")
             return md_stream.getvalue()

        # Node header
        md_stream.write(f"### {display_name} (`{node_name}`)\n\n")

        # Class Name and Module
        md_stream.write(f"**Class:** `{info.get('class_name', 'N/A')}`\n")
        md_stream.write(f"**Source Module:** `{info.get('module', 'unknown')}`")
        if info.get('is_custom'):
             md_stream.write(" (Custom)")
        if info.get('is_output_node'):
             md_stream.write(" (Output Node)")
        md_stream.write("\n")
        md_stream.write(f"**File Path:** `{info.get('file_path', 'unknown')}`\n\n")

        # Description
        if info.get('description'):
            md_stream.write(f"{info['description']}\n\n")
        else:
            md_stream.write("*No description provided.*\n\n")

        # Inputs
        inputs = info.get('inputs', {})
        if inputs:
            md_stream.write("**Inputs:**\n\n")
            md_stream.write("| Name | Type | Required | Tooltip |\n")
            md_stream.write("|---|---|---|---|\n")
            for input_name, input_details in inputs.items():
                req = 'Yes' if input_details.get('required') else 'No'
                tooltip = info.get('input_tooltips', {}).get(input_name, '')
                # Truncate long tooltips
                if len(tooltip) > 100:
                    tooltip = tooltip[:97] + '...'
                # Escape pipes in tooltips
                tooltip = tooltip.replace('|', '\\|')
                md_stream.write(f"| `{input_name}` | `{input_details.get('type', '')}` | {req} | {tooltip} |\n")
            md_stream.write("\n")
        else:
            md_stream.write("**Inputs:** *None*\n\n")

        # Outputs
        outputs = info.get('outputs', [])
        if outputs:
            md_stream.write("**Outputs:**\n\n")
            md_stream.write("| Index | Name | Type | Tooltip |\n")
            md_stream.write("|---|---|---|---|\n")
            output_names = info.get('output_names', [])
            output_tooltips = info.get('output_tooltips', [])
            # Ensure lists have correct length for zip
            if len(output_names) < len(outputs):
                 output_names.extend([f'output_{i}' for i in range(len(output_names), len(outputs))])
            if len(output_tooltips) < len(outputs):
                 output_tooltips.extend(['' for _ in range(len(output_tooltips), len(outputs))])

            for i, (out_type, out_name, out_tooltip) in enumerate(zip(outputs, output_names, output_tooltips)):
                tooltip = out_tooltip or ''
                if len(tooltip) > 100:
                    tooltip = tooltip[:97] + '...'
                tooltip = tooltip.replace('|', '\\|')
                md_stream.write(f"| {i} | `{out_name}` | `{out_type}` | {tooltip} |\n")
            md_stream.write("\n")
        else:
            md_stream.write("**Outputs:** *None*\n\n")

        md_stream.write("---\n") # Separator between nodes
        return md_stream.getvalue()


    # --- Helper: Generate Summary Markdown String --- (Adapted from write_short_markdown)
    @staticmethod
    def generate_summary_markdown(node_info: Dict[str, Dict[str, Any]]) -> str:
        """Generates a condensed markdown summary string of all nodes."""
        md_stream = StringIO()
        md_stream.write("# Installed ComfyUI Nodes (Summary)\n\n")

        # Group by category
        by_category = defaultdict(list)
        for class_key, info in node_info.items():
            category = info.get('category', 'uncategorized') if 'error' not in info else 'Errored Nodes'
            by_category[category].append((class_key, info))

        # Write each category
        for category in sorted(by_category.keys()):
            md_stream.write(f"## {category.upper()}\n\n")
            sorted_nodes = sorted(by_category[category], key=lambda item: item[1].get('display_name', item[0]))
            for class_key, info in sorted_nodes:
                node_name = info.get('node_name', class_key)
                display_name = info.get('display_name', node_name)
                if 'error' in info:
                    md_stream.write(f"- **{display_name} (`{node_name}`)** - ERROR: {info['error']}\n")
                else:
                    desc = info.get('description', '').split('\n')[0] # First line of description
                    if len(desc) > 120:
                        desc = desc[:117] + '...'
                    module_info = f" (Source: `{info.get('module', '?')}`)" if info.get('is_custom') else ''
                    md_stream.write(f"- **{display_name} (`{node_name}`)**{module_info}: {desc}\n")
            md_stream.write("\n")

        return md_stream.getvalue()

    # --- JSON Serialization Helper ---
    @staticmethod
    def _serialize_item(item):
        if isinstance(item, Path):
            return str(item)
        try:
            json.dumps(item)
            return item
        except TypeError:
            return repr(item)

    # --- Main Node Execution Logic ---
    def list_nodes(self, include_custom_nodes=True):
        print(f"LOKI List Installed Nodes: Executing (Include Custom: {include_custom_nodes})")
        node_info = get_all_node_info(include_custom=include_custom_nodes)

        # Calculate hash of current results
        current_hash = None
        try:
             serialized_info = json.dumps(node_info, sort_keys=True, default=repr)
             current_hash = hash(serialized_info)
             print(f"Calculated current node info hash: {current_hash}")
        except Exception as e:
             print(f"Warning: Could not calculate hash for node info: {e}")
             current_hash = hash(str(node_info)) # Fallback hash

        # Update the class hash *after* successful execution and hashing
        ListInstalledNodes._class_last_node_info_hash = current_hash

        # --- Output Generation ---
        all_nodes_json_string = "{}"
        summary_markdown_string = ""
        node_json_list = []
        node_markdown_list = []

        # 1. Generate Full JSON String
        try:
             all_nodes_json_string = json.dumps(node_info, indent=4, default=self._serialize_item)
        except Exception as json_err:
             print(f"Error serializing node info to JSON: {json_err}")
             all_nodes_json_string = json.dumps({"error": "Failed to serialize node info", "details": str(json_err)})

        # 2. Generate Summary Markdown String
        try:
            summary_markdown_string = self.generate_summary_markdown(node_info)
        except Exception as e:
            print(f"Error generating summary markdown: {e}")
            summary_markdown_string = f"# Error Generating Summary\n\n{e}"

        # 3. Generate List of Node JSON Strings
        # 4. Generate List of Node Markdown Strings
        for class_key, info in node_info.items():
            # JSON List Item
            try:
                node_json_str = json.dumps({class_key: info}, indent=4, default=self._serialize_item)
                node_json_list.append(node_json_str)
            except Exception as e:
                print(f"Error serializing single node JSON ({class_key}): {e}")
                node_json_list.append(json.dumps({"error": f"Failed to serialize node {class_key}", "details": str(e)}))

            # Markdown List Item
            try:
                node_md_str = self.generate_single_node_markdown(class_key, info)
                node_markdown_list.append(node_md_str)
            except Exception as e:
                 print(f"Error generating single node markdown ({class_key}): {e}")
                 node_markdown_list.append(f"### Error: Node {class_key}\n\n{e}\n---")


        # Return the four outputs
        return (all_nodes_json_string, summary_markdown_string, node_json_list, node_markdown_list)

    @classmethod
    def IS_CHANGED(cls, include_custom_nodes=True):
        """Check if the node list has actually changed since the last run."""
        print("LOKI List Installed Nodes: IS_CHANGED check")
        # Get current node info
        # Note: This incurs the cost of scanning nodes during the check phase.
        # Consider optimizations if this becomes a bottleneck (e.g., caching results briefly).
        current_node_info = get_all_node_info(include_custom=include_custom_nodes)
        current_hash = None
        try:
            serialized_info = json.dumps(current_node_info, sort_keys=True, default=repr)
            current_hash = hash(serialized_info)
            print(f"  IS_CHANGED current hash: {current_hash}")
            print(f"  IS_CHANGED last class hash: {cls._class_last_node_info_hash}")
        except Exception as e:
            print(f"  Warning: Could not calculate hash for IS_CHANGED check: {e}")
            # If hashing fails, assume it changed to be safe
            return str(uuid.uuid4())

        # Compare with the stored hash from the last successful execution
        if current_hash != cls._class_last_node_info_hash:
            print("  IS_CHANGED detected changes.")
            # Return a new unique ID to signal change
            # (Don't update the class hash here, only in list_nodes after success)
            return str(uuid.uuid4())
        else:
            print("  IS_CHANGED detected no changes.")
            # Return the *same* hash to signal no change
            return cls._class_last_node_info_hash

# --- ComfyUI Registration --- (Moved to __init__.py in the parent nodes directory)
# NODE_CLASS_MAPPINGS = {
#     "ListInstalledNodes_Loki": ListInstalledNodesNode
# }
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "ListInstalledNodes_Loki": "List Installed Nodes 📜 (LOKI)"
# } 