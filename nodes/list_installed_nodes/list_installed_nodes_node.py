import os
import sys
from pathlib import Path
import json
from collections import defaultdict
import importlib
import inspect
from typing import Dict, Any, List, Tuple
import re
import nodes

# Add ComfyUI root directory to Python path if running standalone,
# but usually not needed when run as a node.
# COMFY_ROOT = str(Path(__file__).parent.parent.parent.parent) # Adjust path depth
# sys.path.append(COMFY_ROOT)
# Instead, rely on ComfyUI's environment providing access to 'nodes'

# --- Node Definition ---

class ListInstalledNodesNode:
    """
    Lists installed ComfyUI nodes (built-in and custom) and outputs
    their information as a JSON string and saves detailed/short Markdown files.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                 "trigger": ("*", {}), # Trigger execution
                 "output_format": (["json_string", "markdown_files"], {"default": "markdown_files"}),
                 "filename_prefix": ("STRING", {"default": "installed_nodes"}),
            },
             "optional": {
                  "include_custom_nodes": ("BOOLEAN", {"default": True}),
             }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING") # JSON data, Markdown path, Short Markdown path
    RETURN_NAMES = ("nodes_json", "markdown_filepath", "short_markdown_filepath")
    FUNCTION = "list_nodes"
    CATEGORY = "utils/docs"
    OUTPUT_NODE = True # Indicate it produces output files/data

    # Define output dir relative to this node's file
    NODE_OUTPUT_DIR = Path(__file__).parent / "output"

    def __init__(self):
        self.output_dir = ListInstalledNodesNode.NODE_OUTPUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # --- Helper Functions (Adapted from original script) ---

    @staticmethod
    def get_node_io_info(node_class) -> Dict[str, Any]:
        """Extract comprehensive input/output information from a node class"""
        info = {
            'inputs': {}, 'input_tooltips': {},
            'outputs': [], 'output_tooltips': [], 'output_is_list': [], 'output_names': [],
            'description': getattr(node_class, 'DESCRIPTION', getattr(node_class, '__doc__', '') or '').strip(), # Add description fallback
            'category': getattr(node_class, 'CATEGORY', 'unknown')
        }
        try:
            # Get inputs and their tooltips
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
                                'options': options # Keep options, might be useful
                            }
                            if tooltip:
                                info['input_tooltips'][input_name] = tooltip

            # Get outputs
            if hasattr(node_class, 'RETURN_TYPES'):
                 ret_types = node_class.RETURN_TYPES
                 # Ensure it's a tuple or list for consistency
                 info['outputs'] = list(ret_types) if isinstance(ret_types, (list, tuple)) else [ret_types]


            # Get output tooltips
            if hasattr(node_class, 'OUTPUT_TOOLTIPS'):
                info['output_tooltips'] = list(node_class.OUTPUT_TOOLTIPS)

            # Get output list flags
            if hasattr(node_class, 'OUTPUT_IS_LIST'):
                info['output_is_list'] = list(node_class.OUTPUT_IS_LIST)
            else:
                info['output_is_list'] = [False] * len(info.get('outputs', []))

            # Get output names
            if hasattr(node_class, 'RETURN_NAMES'):
                 ret_names = node_class.RETURN_NAMES
                 info['output_names'] = list(ret_names) if isinstance(ret_names, (list, tuple)) else [ret_names]

            # Ensure output names match output count, fallback if needed
            if len(info.get('output_names', [])) != len(info.get('outputs',[])):
                 info['output_names'] = [str(t) for t in info.get('outputs', [])] # Fallback to type names

        except Exception as e:
             print(f"Warning: Error processing IO for {node_class.__name__}: {e}")
             # Set defaults to avoid errors later
             info['outputs'] = info.get('outputs', [])
             info['output_names'] = info.get('output_names', [])
             info['output_is_list'] = info.get('output_is_list', [False] * len(info.get('outputs', [])))
             if len(info.get('output_names',[])) != len(info.get('outputs',[])):
                  info['output_names'] = [f"output_{i}" for i in range(len(info.get('outputs', [])))]


        return info


    @staticmethod
    def get_all_node_info(include_custom=True) -> Dict[str, Dict[str, Any]]:
        """Gather comprehensive information about all nodes"""
        node_info_dict = {}

        # --- Process built-in nodes ---
        print("Processing built-in nodes...")
        for node_name, node_class in nodes.NODE_CLASS_MAPPINGS.items():
            try:
                display_name = nodes.NODE_DISPLAY_NAME_MAPPINGS.get(node_name, node_name)
                io_info = ListInstalledNodesNode.get_node_io_info(node_class)
                node_info_dict[node_name] = {
                    'class_name': node_class.__name__,
                    'display_name': display_name,
                    'is_output_node': getattr(node_class, 'OUTPUT_NODE', False),
                    'module': 'ComfyUI', # Mark as built-in
                    'file_path': inspect.getfile(node_class) if hasattr(node_class, '__module__') else 'unknown',
                    **io_info
                }
            except Exception as e:
                print(f"Error processing built-in node {node_name}: {e}")
                node_info_dict[node_name] = {'error': str(e), 'display_name': node_name, 'module': 'ComfyUI'}


        # --- Process custom nodes if requested ---
        if include_custom:
            print("Processing custom nodes...")
            # Custom nodes are usually loaded into these mappings by ComfyUI already
            # We need to identify which ones are custom.
            # Custom nodes often reside in modules within the 'custom_nodes' folder.
            custom_node_path_indicator = os.path.sep + 'custom_nodes' + os.path.sep

            for node_name, node_class in nodes.NODE_CLASS_MAPPINGS.items():
                 if node_name in node_info_dict:
                     continue # Already processed as built-in (shouldn't happen if mappings are distinct)

                 try:
                     # Determine if it's likely a custom node
                     module_name = getattr(node_class, '__module__', 'unknown')
                     file_path = 'unknown'
                     is_custom = False
                     if module_name != 'unknown':
                         try:
                             file_path = inspect.getfile(node_class)
                             if custom_node_path_indicator in file_path:
                                 is_custom = True
                                 # Extract the custom node directory name
                                 parts = file_path.split(custom_node_path_indicator)
                                 if len(parts) > 1:
                                     module_name = parts[1].split(os.path.sep)[0] # Get the top-level custom node folder
                         except TypeError: # Handle built-in types or weird cases
                             file_path = 'built-in or unknown source'
                         except Exception as inspect_e:
                              print(f"Could not inspect file for {node_name}: {inspect_e}")


                     # Heuristic: if module name looks like a custom node identifier
                     if not is_custom and module_name != 'nodes' and module_name != '__main__' and '.' not in module_name:
                          is_custom = True # Assume it's a custom node if module name is simple

                     if is_custom:
                         display_name = nodes.NODE_DISPLAY_NAME_MAPPINGS.get(node_name, node_name)
                         io_info = ListInstalledNodesNode.get_node_io_info(node_class)
                         node_info_dict[node_name] = {
                             'class_name': node_class.__name__,
                             'display_name': display_name,
                             'is_output_node': getattr(node_class, 'OUTPUT_NODE', False),
                             'module': module_name, # Custom node folder/module
                             'file_path': file_path,
                             **io_info
                         }

                 except Exception as e:
                     print(f"Error processing custom node candidate {node_name}: {e}")
                     node_info_dict[node_name] = {'error': str(e), 'display_name': node_name, 'module': 'custom?'}


        print(f"Found {len(node_info_dict)} total installed nodes.")
        return node_info_dict

    @staticmethod
    def write_markdown_to_file(node_info: Dict[str, Dict[str, Any]], output_filepath: Path):
        """Write node information as markdown to a file"""
        print(f"Writing full markdown to: {output_filepath}")
        with output_filepath.open('w', encoding='utf-8') as f:
            f.write("# Installed ComfyUI Node Documentation\n\n")

            # Group by category
            by_category = defaultdict(list)
            for node_name, info in node_info.items():
                 # Handle potential errors during info gathering
                 if 'error' in info:
                      category = 'Errored Nodes'
                 else:
                      category = info.get('category', 'uncategorized')
                 by_category[category].append((node_name, info))


            # Write each category
            for category in sorted(by_category.keys()):
                f.write(f"## {category.upper()}\n\n")

                # Sort nodes by display name within category
                sorted_nodes = sorted(by_category[category], key=lambda item: item[1].get('display_name', item[0]))

                for node_name, info in sorted_nodes:
                    if 'error' in info:
                         f.write(f"### {info.get('display_name', node_name)} (`{node_name}`)\n\n")
                         f.write(f"**Error processing this node:** {info['error']}\n\n")
                         f.write("---\n\n")
                         continue

                    # Node header
                    f.write(f"### {info.get('display_name', node_name)} (`{node_name}`)\n\n")

                    # Description
                    if info.get('description'):
                        f.write(f"{info['description']}\n\n")
                    else:
                        f.write("*No description provided.*\n\n")

                    # Module info
                    module_info = info.get('module', 'unknown')
                    f.write(f"**Source:** `{module_info}`")
                    if info.get('is_output_node'):
                         f.write(" (Output Node)")
                    f.write("\n\n")
                    # Optional: Add file path if desired
                    # f.write(f"**File Path:** `{info.get('file_path', 'unknown')}`\n\n")


                    # Inputs
                    if info.get('inputs'):
                        f.write("#### Inputs\n\n")
                        # Sort inputs alphabetically
                        sorted_inputs = sorted(info['inputs'].items())
                        for input_name, input_data in sorted_inputs:
                            req_status = "**(required)**" if input_data.get('required') else "(optional)"
                            input_type = input_data.get('type', '*')
                            line = f"- `{input_name}` {req_status}: `{input_type}`"

                            tooltip = info.get('input_tooltips', {}).get(input_name)
                            if tooltip:
                                line += f"\n  - Tooltip: *{tooltip}*"

                            options = input_data.get('options')
                            if options:
                                try:
                                    # Limit length of options display
                                    opt_str = json.dumps(options)
                                    if len(opt_str) > 150:
                                        opt_str = opt_str[:150] + "...}"
                                    line += f"\n  - Options: `{opt_str}`"
                                except TypeError:
                                     line += f"\n  - Options: *Non-serializable options*"


                            f.write(line + "\n")
                        f.write("\n")
                    else:
                         f.write("#### Inputs\n\n*No defined inputs.*\n\n")

                    # Outputs
                    if info.get('outputs'):
                        f.write("#### Outputs\n\n")
                        num_outputs = len(info['outputs'])
                        output_names = info.get('output_names', [f"output_{i}" for i in range(num_outputs)])
                        output_is_list = info.get('output_is_list', [False] * num_outputs)
                        output_tooltips = info.get('output_tooltips', [])

                        # Ensure lists have correct length
                        if len(output_names) != num_outputs: output_names = [f"output_{i}" for i in range(num_outputs)]
                        if len(output_is_list) != num_outputs: output_is_list = [False] * num_outputs

                        for i, output_type in enumerate(info['outputs']):
                            output_name = output_names[i]
                            is_list = output_is_list[i]

                            line = f"- `{output_name}`: `{output_type}`"
                            if is_list:
                                line += " (LIST)"

                            # Add tooltip if available
                            if i < len(output_tooltips) and output_tooltips[i]:
                                line += f"\n  - Tooltip: *{output_tooltips[i]}*"

                            f.write(line + "\n")
                        f.write("\n")
                    else:
                         f.write("#### Outputs\n\n*No defined outputs.*\n\n")

                    f.write("---\n\n") # Separator between nodes


    @staticmethod
    def write_short_markdown(node_info: Dict[str, Dict[str, Any]], output_filepath: Path):
        """Write a simplified markdown with just module names, node names, inputs and outputs"""
        print(f"Writing short markdown to: {output_filepath}")
        modules = defaultdict(list)

        # Group nodes by module
        for node_name, node_data in node_info.items():
             if 'error' in node_data:
                 continue # Skip errored nodes for short version

             module_name = node_data.get('module', 'Unknown')
             display_name = node_data.get('display_name', node_name)

             inputs = list(node_data.get('inputs', {}).keys())
             # Use RETURN_NAMES for outputs if available
             outputs = node_data.get('output_names', [str(t) for t in node_data.get('outputs', [])])


             node_entry = {
                 'name': node_name,
                 'display_name': display_name,
                 'inputs': sorted(inputs),
                 'outputs': outputs # Keep original order
             }
             modules[module_name].append(node_entry)

        # Write to file
        with output_filepath.open('w', encoding='utf-8') as f:
            f.write("# Installed Nodes Summary (Module -> Node [Inputs] => [Outputs])\n\n")
            for module_name in sorted(modules.keys()):
                f.write(f"## {module_name}\n\n")

                # Sort nodes alphabetically by display name within each module
                sorted_nodes = sorted(modules[module_name], key=lambda x: x['display_name'].lower())

                for node in sorted_nodes:
                    inputs_str = ", ".join(f"`{inp}`" for inp in node['inputs']) if node['inputs'] else " "
                    outputs_str = ", ".join(f"`{out}`" for out in node['outputs']) if node['outputs'] else " "
                    f.write(f"- **{node['display_name']}** (`{node['name']}`): [{inputs_str}] => [{outputs_str}]\n")
                f.write("\n")

    # --- Node Execution Method ---

    def list_nodes(self, trigger=None, output_format="markdown_files", include_custom_nodes=True, filename_prefix="installed_nodes"):
        print("Listing installed nodes...")
        node_info_dict = ListInstalledNodesNode.get_all_node_info(include_custom=include_custom_nodes)

        # Sanitize filename prefix
        safe_prefix = re.sub(r'[^\w\-_\. ]', '_', filename_prefix)

        # Prepare output paths
        md_filename = f"{safe_prefix}_detailed.md"
        short_md_filename = f"{safe_prefix}_summary.md"
        md_filepath = self.output_dir / md_filename
        short_md_filepath = self.output_dir / short_md_filename

        nodes_json = "{}"
        try:
            # Need to handle potential non-serializable data (like type objects) before dumping
            # A simple approach is to convert types to strings, but a more robust way might be needed.
            def serialize_item(item): # Nested helper for serialization
                 if isinstance(item, type): return str(item)
                 if isinstance(item, (list, tuple)): return [serialize_item(i) for i in item]
                 if isinstance(item, dict): return {k: serialize_item(v) for k, v in item.items()}
                 return item
            serializable_dict = serialize_item(node_info_dict)
            nodes_json = json.dumps(serializable_dict, indent=2)
        except Exception as e:
            print(f"Error serializing node info to JSON: {e}")
            nodes_json = json.dumps({"error": "Failed serialize", "details": str(e)})


        if output_format == "markdown_files":
            try:
                # Call static methods
                ListInstalledNodesNode.write_markdown_to_file(node_info_dict, md_filepath)
                ListInstalledNodesNode.write_short_markdown(node_info_dict, short_md_filepath)
                print("Markdown files generated.")
                # Return absolute paths as strings for potential use elsewhere
                return (nodes_json, str(md_filepath.resolve()), str(short_md_filepath.resolve()))
            except Exception as e:
                print(f"Error writing markdown files: {e}")
                return (nodes_json, f"Error: {e}", f"Error: {e}")
        else: # json_string
             print("Outputting JSON string only.")
             return (nodes_json, "Not generated (JSON output)", "Not generated (JSON output)") 