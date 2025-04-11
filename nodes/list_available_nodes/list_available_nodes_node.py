import json
import os
import sys
from pathlib import Path
import requests
from collections import defaultdict
import re # For filename sanitization
from typing import List, Dict, Optional

# --- Node Definition ---

class ListAvailableNodesNode:
    """
    Lists available ComfyUI custom node packages from ComfyUI-Manager's list.
    Outputs the data as a JSON string and saves a Markdown file.
    Requires ComfyUI-Manager to be installed or manually provide the cache path.
    """

    NODE_OUTPUT_DIR = Path(__file__).parent / "output"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("*", {}), # Trigger execution
                "output_format": (["json_string", "markdown_file"], {"default": "markdown_file"}),
                "filename_prefix": ("STRING", {"default": "available_nodes"}),
            },
            "optional": {
                # Allow overriding the cache path if needed
                 "manager_cache_path_override": ("STRING", {"default": "", "multiline": False}),
                 "fallback_github_url": ("STRING", {"default": "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json"})
            }
        }

    RETURN_TYPES = ("STRING", "STRING") # JSON data, Markdown filepath
    RETURN_NAMES = ("extensions_json", "markdown_filepath")
    FUNCTION = "list_available_nodes"
    CATEGORY = "utils/docs"
    OUTPUT_NODE = True

    def __init__(self):
        # Ensure the output directory exists
        self.output_dir = ListAvailableNodesNode.NODE_OUTPUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # --- Helper Functions (Adapted from original script) ---

    @staticmethod
    def get_manager_path(override_path: str = None) -> Optional[str]:
        """Find ComfyUI-Manager directory"""
        if override_path and os.path.isdir(override_path):
             print(f"Using provided manager path: {override_path}")
             return override_path

        # Try to find it relative to this node's location (common structure)
        loki_dir = Path(__file__).parent.parent # Now inside nodes/, so go up twice
        custom_nodes_dir = loki_dir.parent
        manager_path = custom_nodes_dir / "ComfyUI-Manager"

        if manager_path.is_dir():
             print(f"Found manager path: {manager_path}")
             return str(manager_path)
        else:
             print(f"Warning: Could not automatically find ComfyUI-Manager directory near {custom_nodes_dir}")
             return None # Indicate not found


    def load_extension_list(self, manager_path_override: str = None, fallback_url: str = None) -> List[Dict]:
        """Load extension list from ComfyUI Manager's cache or fetch from GitHub"""
        manager_dir = self.get_manager_path(manager_path_override)
        cache_file = None
        data = None

        if manager_dir:
            cache_file = Path(manager_dir) / "cache" / "custom-node-list.json"
            if cache_file.exists():
                print(f"Loading extensions from cache: {cache_file}")
                try:
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        data = json.loads(content)
                        # Check structure (can be list or dict with 'custom_nodes')
                        if isinstance(data, dict) and 'custom_nodes' in data:
                            return data['custom_nodes']
                        elif isinstance(data, list):
                            return data # Already a list
                        else:
                             print(f"Warning: Unexpected JSON structure in cache file: {type(data)}")
                             data = None # Reset data to trigger fallback
                except json.JSONDecodeError as e:
                    print(f"JSON Parse Error in cache file {cache_file}: {e}")
                    print("Content causing error:", content[:100], "...")
                    # Fall through to GitHub fetch
                except Exception as e:
                    print(f"Error reading cache file {cache_file}: {e}")
                    # Fall through to GitHub fetch
            else:
                print(f"Manager cache file not found at: {cache_file}")

        # Fallback to direct GitHub fetch if cache failed or not found
        if data is None and fallback_url:
            print(f"Attempting to fetch extension list from: {fallback_url}")
            try:
                response = requests.get(fallback_url, timeout=15)
                response.raise_for_status()
                data = response.json()
                 # Check structure again
                if isinstance(data, dict) and 'custom_nodes' in data:
                    return data['custom_nodes']
                elif isinstance(data, list):
                    return data
                else:
                     print(f"Error: Unexpected JSON structure from GitHub URL: {type(data)}")
                     raise ValueError("Invalid data structure from fallback URL")

            except requests.exceptions.RequestException as e:
                print(f"Error fetching extension list from {fallback_url}: {e}")
                raise # Re-raise network errors
            except json.JSONDecodeError as e:
                 print(f"JSON Parse Error from {fallback_url}: {e}")
                 raise # Re-raise parse errors
            except Exception as e:
                 print(f"Unexpected error fetching from {fallback_url}: {e}")
                 raise # Re-raise other errors
        elif data is None:
             raise FileNotFoundError("Could not load extension list from cache or fallback URL.")


    def write_markdown(self, extensions: List[Dict], output_filepath: Path):
        """Write extension information to markdown file"""
        print(f"Writing available nodes markdown to: {output_filepath}")
        with output_filepath.open('w', encoding='utf-8') as f:
            f.write("# Available ComfyUI Custom Node Packages (from ComfyUI-Manager list)\n\n")

            # Group by category if available
            by_category = defaultdict(list)
            uncategorized = []

            for ext in extensions:
                # Normalize keys: 'reference' might be 'files'[0] in some versions
                if 'reference' not in ext and 'files' in ext and ext['files']:
                     ext['reference'] = ext['files'][0]

                category = ext.get('category')
                if category and isinstance(category, str): # Ensure category is a string
                    by_category[category].append(ext)
                else:
                    uncategorized.append(ext)

            # Write categorized extensions
            for category in sorted(by_category.keys()):
                f.write(f"## {category}\n\n")
                # Sort by title (case-insensitive)
                sorted_extensions = sorted(by_category[category], key=lambda x: x.get('title', x.get('name', '')).lower())
                for ext in sorted_extensions:
                    self.write_extension_info(f, ext)

            # Write uncategorized extensions
            if uncategorized:
                f.write("## Uncategorized\n\n")
                sorted_extensions = sorted(uncategorized, key=lambda x: x.get('title', x.get('name', '')).lower())
                for ext in sorted_extensions:
                    self.write_extension_info(f, ext)


    def write_extension_info(self, f, ext: Dict):
        """Write individual extension information to the file handle"""
        title = ext.get('title', ext.get('name', 'Unknown'))
        f.write(f"### {title}\n\n")

        if ext.get('description'):
            f.write(f"{ext['description']}\n\n")

        f.write(f"- **Author:** {ext.get('author', 'Unknown')}\n")

        reference = ext.get('reference') # Use normalized key
        if reference:
             # Attempt to make it a clickable link if it looks like a URL
             if reference.startswith('http://') or reference.startswith('https://'):
                 f.write(f"- **Repository/Reference:** [{reference}]({reference})\n")
             else:
                 f.write(f"- **Repository/Reference:** {reference}\n")


        if ext.get('install_type'):
            f.write(f"- **Install Type:** {ext['install_type']}\n")

        # Use 'nodes' key if 'nodeTypes' isn't present (older format?)
        node_types = ext.get('nodeTypes', ext.get('nodes'))
        if node_types and isinstance(node_types, list):
            f.write("\n**Included Node Types:**\n")
            for node_type in sorted(node_types): # Sort node types alphabetically
                f.write(f"- `{node_type}`\n")

        f.write("\n---\n\n") # Separator


    # --- Node Execution Method ---

    def list_available_nodes(self, trigger=None, output_format="markdown_file", filename_prefix="available_nodes", manager_cache_path_override=None, fallback_github_url=None):
        print("Listing available nodes...")
        extensions_json = "{}"
        md_filepath = "Error: Could not generate file path" # Default error path

        try:
            extensions = self.load_extension_list(manager_cache_path_override, fallback_github_url)
            extensions_json = json.dumps(extensions, indent=2)

            if output_format == "markdown_file":
                 # Sanitize prefix
                 safe_prefix = re.sub(r'[^\w\-_\. ]', '_', filename_prefix)
                 md_filename = f"{safe_prefix}.md"
                 md_filepath = self.output_dir / md_filename
                 self.write_markdown(extensions, md_filepath)
                 print("Markdown file generated.")
                 return (extensions_json, str(md_filepath.resolve()))
            else: # json_string
                 print("Outputting JSON string only.")
                 return (extensions_json, "Not generated (JSON output)")

        except FileNotFoundError as e:
             print(f"Error: {e}")
             error_json = json.dumps({"error": str(e)})
             return (error_json, f"Error: {e}")
        except Exception as e:
            print(f"Error listing available nodes: {e}")
            error_json = json.dumps({"error": f"Failed to list available nodes: {e}"})
            # Provide a meaningful error message for the filepath
            md_filepath = f"Error: {e}"
            return (error_json, md_filepath) 