import json
import os
import sys
from pathlib import Path
import requests
from collections import defaultdict
import re
from typing import List, Dict, Optional
import uuid
from io import StringIO

# Import the core logic
from .list_available_nodes import load_extension_list

# --- Node Definition ---

class ListAvailableNodes:
    """
    Lists available ComfyUI custom node packages from ComfyUI-Manager's list or a fallback URL.
    Outputs the data in various formats (JSON string, Markdown string, list of JSON, list of Markdown).
    """
    _class_last_node_info_hash = None # Class variable for IS_CHANGED

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                 "manager_cache_path_override": ("STRING", {"default": "", "multiline": False}),
                 "fallback_github_url": ("STRING", {"default": "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json"})
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING") # Match list_installed_nodes
    RETURN_NAMES = ("all_nodes_json", "summary_markdown", "node_json_list", "node_markdown_list")
    FUNCTION = "list_available"
    CATEGORY = "LOKI 🦊/System"
    OUTPUT_NODE = False # Not writing files

    def __init__(self):
        pass # No output dir needed

    # --- Helper: Generate Markdown for a single available node --- (Adapted from original write_extension_info)
    @staticmethod
    def generate_single_node_markdown(ext: Dict) -> str:
        """Generates detailed markdown documentation string for a single available node/extension."""
        md_stream = StringIO()

        # Normalize keys: 'reference' might be 'files'[0]
        if 'reference' not in ext and 'files' in ext and ext.get('files'):
             ext['reference'] = ext['files'][0]

        title = ext.get('title', ext.get('name', 'Unknown Extension'))
        md_stream.write(f"### {title}\n\n")

        if ext.get('description'):
            md_stream.write(f"{ext['description']}\n\n")

        md_stream.write(f"- **Author:** {ext.get('author', 'Unknown')}\n")

        reference = ext.get('reference')
        if reference:
             if reference.startswith('http://') or reference.startswith('https://'):
                 md_stream.write(f"- **Repository/Reference:** [{reference}]({reference})\n")
             else:
                 md_stream.write(f"- **Repository/Reference:** {reference}\n")

        if ext.get('install_type'):
            md_stream.write(f"- **Install Type:** {ext['install_type']}\n")

        node_types = ext.get('nodeTypes', ext.get('nodes')) # Handle alias
        if node_types and isinstance(node_types, list):
            md_stream.write("\n**Included Node Types:**\n")
            for node_type in sorted(node_types):
                md_stream.write(f"- `{node_type}`\n")

        md_stream.write("\n---\n") # Separator
        return md_stream.getvalue()

    # --- Helper: Generate Summary Markdown String --- (Adapted from original write_markdown)
    @staticmethod
    def generate_summary_markdown(extensions: List[Dict]) -> str:
        """Generates a condensed markdown summary string of available nodes/extensions."""
        md_stream = StringIO()
        md_stream.write("# Available ComfyUI Custom Nodes (Summary)\n\n")

        # Group by category if available
        by_category = defaultdict(list)
        uncategorized = []
        for ext in extensions:
            category = ext.get('category')
            if category and isinstance(category, str):
                by_category[category].append(ext)
            else:
                uncategorized.append(ext)

        # Write categorized extensions
        for category in sorted(by_category.keys()):
            md_stream.write(f"## {category}\n\n")
            sorted_extensions = sorted(by_category[category], key=lambda x: x.get('title', x.get('name', '')).lower())
            for ext in sorted_extensions:
                 title = ext.get('title', ext.get('name', 'Unknown Extension'))
                 desc = ext.get('description', '').split('\n')[0]
                 if len(desc) > 120: desc = desc[:117] + '...'
                 author = ext.get('author', '?')
                 md_stream.write(f"- **{title}** (by {author}): {desc}\n")
            md_stream.write("\n")

        # Write uncategorized extensions
        if uncategorized:
            md_stream.write("## Uncategorized\n\n")
            sorted_extensions = sorted(uncategorized, key=lambda x: x.get('title', x.get('name', '')).lower())
            for ext in sorted_extensions:
                 title = ext.get('title', ext.get('name', 'Unknown Extension'))
                 desc = ext.get('description', '').split('\n')[0]
                 if len(desc) > 120: desc = desc[:117] + '...'
                 author = ext.get('author', '?')
                 md_stream.write(f"- **{title}** (by {author}): {desc}\n")
            md_stream.write("\n")

        return md_stream.getvalue()

    # --- JSON Serialization Helper ---
    @staticmethod
    def _serialize_item(item):
        # Basic serialization, extend if needed for complex types
        try:
            json.dumps(item)
            return item
        except TypeError:
            return repr(item)

    # --- Main Execution Logic ---
    def list_available(self, manager_cache_path_override=None, fallback_github_url=None):
        print("LOKI List Available Nodes: Executing...")
        extensions = []
        error_str = None
        try:
            extensions = load_extension_list(manager_cache_path_override, fallback_github_url)
        except Exception as e:
            print(f"Error loading available node list: {e}")
            error_str = f"Failed to load available nodes: {e}"

        # Calculate hash of current results (even if errored, hash the error state)
        current_hash = None
        try:
            data_to_hash = extensions if error_str is None else {"error": error_str}
            serialized_info = json.dumps(data_to_hash, sort_keys=True, default=repr)
            current_hash = hash(serialized_info)
            print(f"Calculated current available nodes hash: {current_hash}")
        except Exception as e:
            print(f"Warning: Could not calculate hash for available nodes: {e}")
            current_hash = hash(str(data_to_hash)) # Fallback hash

        # Update the class hash *after* successful execution/hashing
        ListAvailableNodes._class_last_node_info_hash = current_hash

        # --- Output Generation ---
        all_nodes_json_string = "{}"
        summary_markdown_string = ""
        node_json_list = []
        node_markdown_list = []

        if error_str:
             all_nodes_json_string = json.dumps({"error": error_str})
             summary_markdown_string = f"# Error\n\n{error_str}"
             # node_json_list and node_markdown_list remain empty
        else:
            # 1. Generate Full JSON String
            try:
                 all_nodes_json_string = json.dumps(extensions, indent=4, default=self._serialize_item)
            except Exception as json_err:
                 print(f"Error serializing available node info to JSON: {json_err}")
                 all_nodes_json_string = json.dumps({"error": "Failed to serialize available node info", "details": str(json_err)})

            # 2. Generate Summary Markdown String
            try:
                summary_markdown_string = self.generate_summary_markdown(extensions)
            except Exception as e:
                print(f"Error generating summary markdown: {e}")
                summary_markdown_string = f"# Error Generating Summary\n\n{e}"

            # 3. & 4. Generate Lists
            for ext_info in extensions:
                ext_key = ext_info.get('name', ext_info.get('reference', str(uuid.uuid4())))
                # JSON List Item
                try:
                    node_json_str = json.dumps({ext_key: ext_info}, indent=4, default=self._serialize_item)
                    node_json_list.append(node_json_str)
                except Exception as e:
                    print(f"Error serializing single available node JSON ({ext_key}): {e}")
                    node_json_list.append(json.dumps({"error": f"Failed to serialize node {ext_key}", "details": str(e)}))
                # Markdown List Item
                try:
                    node_md_str = self.generate_single_node_markdown(ext_info)
                    node_markdown_list.append(node_md_str)
                except Exception as e:
                     print(f"Error generating single available node markdown ({ext_key}): {e}")
                     node_markdown_list.append(f"### Error: Node {ext_key}\n\n{e}\n---")

        # Return the four outputs
        return (all_nodes_json_string, summary_markdown_string, node_json_list, node_markdown_list)

    @classmethod
    def IS_CHANGED(cls, manager_cache_path_override=None, fallback_github_url=None):
        """Check if the available node list has actually changed since the last run."""
        print("LOKI List Available Nodes: IS_CHANGED check")
        current_extensions = []
        error_str = None
        try:
            current_extensions = load_extension_list(manager_cache_path_override, fallback_github_url)
        except Exception as e:
            print(f"  IS_CHANGED: Error loading list: {e}")
            error_str = f"Failed to load list: {e}"

        current_hash = None
        try:
            data_to_hash = current_extensions if error_str is None else {"error": error_str}
            serialized_info = json.dumps(data_to_hash, sort_keys=True, default=repr)
            current_hash = hash(serialized_info)
            print(f"  IS_CHANGED current hash: {current_hash}")
            print(f"  IS_CHANGED last class hash: {cls._class_last_node_info_hash}")
        except Exception as e:
            print(f"  Warning: Could not calculate hash for IS_CHANGED check: {e}")
            return str(uuid.uuid4()) # Assume change if hashing fails

        if current_hash != cls._class_last_node_info_hash:
            print("  IS_CHANGED detected changes.")
            return str(uuid.uuid4())
        else:
            print("  IS_CHANGED detected no changes.")
            return cls._class_last_node_info_hash 