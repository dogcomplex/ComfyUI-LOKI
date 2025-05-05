import os
import sys
from pathlib import Path
import importlib
import inspect
from typing import Dict, Any, List, Tuple
import argparse
import traceback
import json

# Global variables to hold the loaded mappings
# We populate these once during standalone loading
LOADED_NODE_CLASS_MAPPINGS = {}
LOADED_NODE_DISPLAY_NAME_MAPPINGS = {}
COMFY_ROOT_PATH = None

def get_node_io_info(node_class) -> Dict[str, Any]:
    """Extract comprehensive input/output information from a node class"""
    info = {
        'inputs': {}, 'input_tooltips': {},
        'outputs': [], 'output_tooltips': [], 'output_is_list': [], 'output_names': [],
        'description': getattr(node_class, 'DESCRIPTION', getattr(node_class, '__doc__', '') or '').strip(),
        'category': getattr(node_class, 'CATEGORY', 'unknown')
    }
    try:
        if hasattr(node_class, 'INPUT_TYPES') and callable(node_class.INPUT_TYPES):
            input_types = node_class.INPUT_TYPES()
            for section in ['required', 'optional']:
                if section in input_types:
                    for input_name, input_config in input_types[section].items():
                        input_type_info = input_config[0] if isinstance(input_config, (list, tuple)) else input_config
                        options = input_config[1] if isinstance(input_config, (list, tuple)) and len(input_config) > 1 else None
                        tooltip = options.get('tooltip') if isinstance(options, dict) else None
                        info['inputs'][input_name] = {
                            'type': input_type_info,
                            'required': section == 'required',
                            'options': options
                        }
                        if tooltip:
                            info['input_tooltips'][input_name] = tooltip

        if hasattr(node_class, 'RETURN_TYPES'):
            ret_types = node_class.RETURN_TYPES
            info['outputs'] = list(ret_types) if isinstance(ret_types, (list, tuple)) else [ret_types]

        if hasattr(node_class, 'OUTPUT_TOOLTIPS'):
            info['output_tooltips'] = list(node_class.OUTPUT_TOOLTIPS)

        if hasattr(node_class, 'OUTPUT_IS_LIST'):
            info['output_is_list'] = list(node_class.OUTPUT_IS_LIST)
        else:
            info['output_is_list'] = [False] * len(info.get('outputs', []))

        if hasattr(node_class, 'RETURN_NAMES'):
            ret_names = node_class.RETURN_NAMES
            info['output_names'] = list(ret_names) if isinstance(ret_names, (list, tuple)) else [ret_names]

        if len(info.get('output_names', [])) != len(info.get('outputs', [])):
            info['output_names'] = [str(t) for t in info.get('outputs', [])]

    except Exception as e:
        print(f"Warning: Error processing IO for {node_class.__name__}: {e}")
        # Ensure lists are initialized even on error
        info['outputs'] = info.get('outputs', [])
        info['output_names'] = info.get('output_names', [])
        info['output_is_list'] = info.get('output_is_list', [False] * len(info.get('outputs', [])))
        if len(info.get('output_names', [])) != len(info.get('outputs', [])):
            info['output_names'] = [f"output_{i}" for i in range(len(info.get('outputs', [])))]

    return info

def get_all_node_info(include_custom=True, class_mappings=None, display_mappings=None) -> Dict[str, Dict[str, Any]]:
    """Gather comprehensive information about all nodes.

    Args:
        include_custom: Whether to include custom nodes.
        class_mappings: Pre-loaded NODE_CLASS_MAPPINGS (used in standalone mode).
        display_mappings: Pre-loaded NODE_DISPLAY_NAME_MAPPINGS (used in standalone mode).

    Returns:
        A dictionary containing information about each discovered node.
    """
    # Determine which mappings to use
    active_class_mappings = class_mappings
    active_display_mappings = display_mappings

    # If mappings weren't provided (i.e., running inside ComfyUI),
    # try to import and use the live `nodes` module.
    if active_class_mappings is None or active_display_mappings is None:
        print("Mapping arguments not provided, attempting to import live ComfyUI 'nodes' module...")
        try:
            import nodes # Try importing the live module
            active_class_mappings = nodes.NODE_CLASS_MAPPINGS
            active_display_mappings = nodes.NODE_DISPLAY_NAME_MAPPINGS
            print("Successfully imported live 'nodes' module.")
        except ImportError:
            print("Error: Could not import live 'nodes' module. Node mappings are unavailable.")
            return {}
        except Exception as e:
             print(f"Error importing or accessing live 'nodes' module mappings: {e}")
             return {}

    if not active_class_mappings:
        print("Error: Node class mappings are empty or unavailable.")
        return {}

    node_info_dict = {}
    processed_classes = set()

    print("Processing nodes...")
    # Iterate using the active mappings
    for node_name, node_class in active_class_mappings.items():
        if node_class in processed_classes:
            continue
        try:
            display_name = active_display_mappings.get(node_name, node_name)
            io_info = get_node_io_info(node_class)

            module_name = getattr(node_class, '__module__', 'unknown')
            file_path = 'unknown'
            is_custom = False

            if module_name != 'unknown':
                try:
                    file_path = inspect.getfile(node_class)
                    normalized_file_path = os.path.normpath(file_path)
                    # Assume COMFY_ROOT_PATH is set correctly by load_comfyui_nodes *if running standalone*
                    # In ComfyUI mode, COMFY_ROOT_PATH might be None, rely on path structure.
                    custom_node_dir_part = os.path.normpath('custom_nodes')
                    comfy_nodes_dir_part = os.path.normpath('comfy') # Check within comfy too

                    # More robust check
                    path_parts = Path(normalized_file_path).parts
                    if custom_node_dir_part in path_parts:
                        is_custom = True
                        # Find the custom node root directory name
                        try:
                             custom_nodes_index = path_parts.index(custom_node_dir_part)
                             if custom_nodes_index + 1 < len(path_parts):
                                 module_name = path_parts[custom_nodes_index + 1]
                             else:
                                 module_name = "custom_nodes_root"
                        except ValueError: # Should not happen if check passed, but safeguard
                              module_name = "custom_node_unknown_structure"

                    elif comfy_nodes_dir_part in path_parts and 'nodes.py' not in path_parts[-1]: # Check if it's inside comfy/, but not the base nodes.py
                        # Could be a built-in node within a subfolder of comfy/
                        module_name = 'ComfyUI'
                    elif 'nodes.py' in path_parts[-1]: # Base comfy/nodes.py
                         module_name = 'ComfyUI'
                    else:
                        # Could be a built-in type or from another library added to path
                        if not COMFY_ROOT_PATH or not normalized_file_path.startswith(os.path.normpath(COMFY_ROOT_PATH)):
                            # Likely not part of comfy install path, treat as external/built-in
                            pass # Keep original module_name
                        else: # Inside comfy root, but not nodes/ or custom_nodes/
                             module_name = module_name # Keep original module name

                except TypeError:
                    file_path = 'built-in or unknown source'
                    module_name = 'built-in'
                except Exception as inspect_e:
                    print(f"Warning: Could not inspect file for {node_name} ({node_class.__name__}): {inspect_e}")

            if not include_custom and is_custom:
                continue

            class_key = f"{module_name}.{node_class.__name__}"
            node_info_dict[class_key] = {
                'class_name': node_class.__name__,
                'node_name': node_name,
                'display_name': display_name,
                'is_output_node': getattr(node_class, 'OUTPUT_NODE', False),
                'module': module_name,
                'file_path': file_path,
                'is_custom': is_custom,
                **io_info
            }
            processed_classes.add(node_class)

        except Exception as e:
            print(f"Error processing node {node_name} ({getattr(node_class, '__name__', 'UnknownClass')}): {e}")
            error_key = f"error.{node_name}.{getattr(node_class, '__name__', 'UnknownClass')}"
            node_info_dict[error_key] = {'error': str(e), 'display_name': node_name, 'node_name': node_name, 'module': 'error'}
            if 'node_class' in locals() and isinstance(node_class, type):
                 processed_classes.add(node_class)

    print(f"Processed {len(node_info_dict)} total nodes ({len(processed_classes)} unique classes).")
    return node_info_dict

def load_comfyui_nodes(comfyui_path: str):
    """Loads node mappings by simulating ComfyUI's loading process."""
    global LOADED_NODE_CLASS_MAPPINGS, LOADED_NODE_DISPLAY_NAME_MAPPINGS, COMFY_ROOT_PATH

    comfy_path = Path(comfyui_path).resolve()
    COMFY_ROOT_PATH = str(comfy_path)

    if not comfy_path.is_dir():
        print(f"Error: ComfyUI path not found or not a directory: {comfyui_path}")
        return False

    # Add ComfyUI path to sys.path to allow imports
    if str(comfy_path) not in sys.path:
        sys.path.insert(0, str(comfy_path))
        print(f"Added {comfy_path} to sys.path")

    # 1. Import base nodes
    try:
        import nodes # Import ComfyUI's base nodes.py
        LOADED_NODE_CLASS_MAPPINGS = nodes.NODE_CLASS_MAPPINGS.copy()
        LOADED_NODE_DISPLAY_NAME_MAPPINGS = nodes.NODE_DISPLAY_NAME_MAPPINGS.copy()
        print(f"Loaded {len(LOADED_NODE_CLASS_MAPPINGS)} built-in nodes.")
    except ImportError as e:
        print(f"Error: Could not import base 'nodes' module from {comfy_path}: {e}")
        return False
    except Exception as e:
         print(f"Error loading base nodes: {e}")
         traceback.print_exc()
         return False

    # 2. Scan and import custom nodes
    custom_nodes_path = comfy_path / "custom_nodes"
    if not custom_nodes_path.is_dir():
        print("No custom_nodes directory found. Skipping custom nodes.")
        return True

    print(f"Scanning custom nodes in: {custom_nodes_path}")
    for item in custom_nodes_path.iterdir():
        if item.is_dir():
            init_path = item / "__init__.py"
            module_name = f"custom_nodes.{item.name}"
            if init_path.is_file():
                try:
                    print(f"  -> Importing module: {module_name}")
                    module = importlib.import_module(module_name)

                    if hasattr(module, "NODE_CLASS_MAPPINGS") and isinstance(module.NODE_CLASS_MAPPINGS, dict):
                        LOADED_NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
                        print(f"     - Added {len(module.NODE_CLASS_MAPPINGS)} class mappings from {item.name}")

                    if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS") and isinstance(module.NODE_DISPLAY_NAME_MAPPINGS, dict):
                        LOADED_NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
                        print(f"     - Added {len(module.NODE_DISPLAY_NAME_MAPPINGS)} display name mappings from {item.name}")

                except Exception as e:
                    print(f"  -> Failed to import or process module {module_name}: {e}")
                    # Optionally print traceback:
                    # traceback.print_exc()
        # Optionally handle single-file custom nodes directly in custom_nodes? (Less common)

    print(f"Finished loading. Total unique node classes: {len(set(LOADED_NODE_CLASS_MAPPINGS.values()))}")
    return True

# Example usage if run standalone
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List installed ComfyUI nodes.")
    parser.add_argument("comfyui_path", help="Path to the root ComfyUI directory.")
    parser.add_argument("--include-custom", action=argparse.BooleanOptionalAction, default=True, help="Include custom nodes in the listing.")
    # Output defaults to the script's output directory
    script_dir = Path(__file__).parent
    default_output_dir = script_dir / "output"
    default_output_file = default_output_dir / "standalone_installed_nodes.json"
    parser.add_argument("-o", "--output", default=str(default_output_file), help=f"Output JSON file path. Defaults to {default_output_file}")
    args = parser.parse_args()

    print("Running node lister standalone...")

    # Ensure output directory exists
    output_file = Path(args.output)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Load node information first
    if load_comfyui_nodes(args.comfyui_path):
        # Then get the detailed info using the loaded mappings
        # Pass the loaded mappings explicitly to the function
        all_nodes = get_all_node_info(include_custom=args.include_custom, class_mappings=LOADED_NODE_CLASS_MAPPINGS, display_mappings=LOADED_NODE_DISPLAY_NAME_MAPPINGS)

        if all_nodes:
            print(f"Writing results to {output_file.resolve()}...")
            with output_file.open('w', encoding='utf-8') as f:
                def serialize_item(item):
                    if isinstance(item, Path):
                        return str(item)
                    try:
                        json.dumps(item)
                        return item
                    except TypeError:
                        return repr(item)

                import json # Import here as it's only needed for output
                json.dump(all_nodes, f, indent=4, default=serialize_item)
            print("Done.")
        else:
            print("No nodes found or error occurred during info gathering.")
    else:
        print("Failed to load ComfyUI node mappings.") 