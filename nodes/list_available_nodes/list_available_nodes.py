import json
import os
import sys
from pathlib import Path
import requests
from typing import List, Dict, Optional

# --- Core Logic for Fetching Available Nodes ---

def get_manager_path(override_path: str = None) -> Optional[str]:
    """Find ComfyUI-Manager directory"""
    if override_path and os.path.isdir(override_path):
         print(f"Using provided manager path: {override_path}")
         return override_path

    # Try to find it relative to a potential ComfyUI root
    # Heuristic: Go up several levels from this script's location
    # Assumes standard ComfyUI/custom_nodes/ComfyUI-LOKI structure
    try:
        current_dir = Path(__file__).resolve().parent # nodes/list_available_nodes
        loki_dir = current_dir.parent # nodes
        custom_nodes_dir = loki_dir.parent # custom_nodes
        comfy_root_dir = custom_nodes_dir.parent # Potential ComfyUI root

        # Search known possible locations for ComfyUI-Manager
        possible_paths = [
            custom_nodes_dir / "ComfyUI-Manager",
            comfy_root_dir / "custom_nodes" / "ComfyUI-Manager"
        ]

        for manager_path in possible_paths:
            if manager_path.is_dir():
                 print(f"Found manager path: {manager_path}")
                 return str(manager_path)

    except Exception as e:
         print(f"Warning: Error determining relative paths: {e}")

    print(f"Warning: Could not automatically find ComfyUI-Manager directory.")
    return None # Indicate not found

def load_extension_list(manager_path_override: str = None, fallback_url: str = None) -> List[Dict]:
    """Load extension list from ComfyUI Manager's cache or fetch from GitHub"""
    manager_dir = get_manager_path(manager_path_override)
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

    # This line should theoretically not be reached if logic is correct,
    # but added for safety. It implies data was loaded but wasn't the right type.
    if data is None:
        raise ValueError("Failed to load or parse extension list data.")
    # If data was loaded from cache but wasn't list/dict, return empty or error?
    # Returning empty list for now if structure was wrong but file existed.
    return []


# --- Standalone Execution Example --- (Optional)
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch available ComfyUI nodes list.")
    parser.add_argument("--manager-path", help="Optional path to override ComfyUI-Manager directory.")
    parser.add_argument("--url", default="https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json", help="Fallback URL to fetch the list.")
    parser.add_argument("-o", "--output", default="standalone_available_nodes.json", help="Output JSON file name.")

    args = parser.parse_args()

    try:
        print("Running available node lister standalone...")
        extensions = load_extension_list(args.manager_path, args.url)

        output_file = Path(args.output)
        # Ensure output directory exists (create if necessary)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"Writing results to {output_file.resolve()}...")
        with output_file.open('w', encoding='utf-8') as f:
            json.dump(extensions, f, indent=4)
        print("Done.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1) 