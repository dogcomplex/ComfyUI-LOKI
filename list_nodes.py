import os
import sys
from pathlib import Path

# Add ComfyUI root directory to Python path
COMFY_ROOT = str(Path(__file__).parent.parent.parent)
sys.path.append(COMFY_ROOT)

import nodes
import json
from collections import defaultdict
import importlib
import inspect
from typing import Dict, Any, List, Tuple

def get_node_io_info(node_class) -> Dict[str, Any]:
    """Extract comprehensive input/output information from a node class"""
    info = {
        'inputs': {},
        'input_tooltips': {},
        'outputs': [],
        'output_tooltips': [],
        'output_is_list': [],
        'output_names': [],
        'description': getattr(node_class, 'DESCRIPTION', ''),  # Add this line
        'category': getattr(node_class, 'CATEGORY', 'unknown')  # Add this line
    }
    
    # Get inputs and their tooltips
    if hasattr(node_class, 'INPUT_TYPES'):
        input_types = node_class.INPUT_TYPES()
        for section in ['required', 'optional']:
            if section in input_types:
                for input_name, input_info in input_types[section].items():
                    # Store input type
                    info['inputs'][input_name] = {
                        'type': input_info[0] if isinstance(input_info, tuple) else input_info,
                        'required': section == 'required',
                        'options': input_info[1] if isinstance(input_info, tuple) and len(input_info) > 1 else None
                    }
                    
                    # Extract tooltip if available
                    if isinstance(input_info, tuple) and len(input_info) > 1:
                        if isinstance(input_info[1], dict) and 'tooltip' in input_info[1]:
                            info['input_tooltips'][input_name] = input_info[1]['tooltip']
            
    # Get outputs
    if hasattr(node_class, 'RETURN_TYPES'):
        info['outputs'] = node_class.RETURN_TYPES
        
    # Get output tooltips
    if hasattr(node_class, 'OUTPUT_TOOLTIPS'):
        info['output_tooltips'] = list(node_class.OUTPUT_TOOLTIPS)  # Convert to list to ensure it's serializable
        
    # Get output list flags
    if hasattr(node_class, 'OUTPUT_IS_LIST'):
        info['output_is_list'] = node_class.OUTPUT_IS_LIST
    else:
        info['output_is_list'] = [False] * len(info['outputs'])
        
    # Get output names
    if hasattr(node_class, 'RETURN_NAMES'):
        info['output_names'] = node_class.RETURN_NAMES
    else:
        info['output_names'] = info['outputs']
        
    return info

def get_all_node_info(include_custom=True) -> Dict[str, Dict[str, Any]]:
    """Gather comprehensive information about all nodes"""
    node_info = {}
    
    # Process built-in nodes
    for node_name, node_class in nodes.NODE_CLASS_MAPPINGS.items():
        display_name = nodes.NODE_DISPLAY_NAME_MAPPINGS.get(node_name, node_name)
        
        node_info[node_name] = {
            'display_name': display_name,
            'description': getattr(node_class, 'DESCRIPTION', ''),
            'category': getattr(node_class, 'CATEGORY', 'uncategorized'),
            'module': getattr(node_class, 'RELATIVE_PYTHON_MODULE', 'nodes'),
            **get_node_io_info(node_class)
        }
    
    # Process custom nodes if requested
    if include_custom:
        custom_nodes_path = os.path.join(os.path.dirname(nodes.__file__), 'custom_nodes')
        if os.path.exists(custom_nodes_path):
            sys.path.insert(0, custom_nodes_path)
            
            for item in os.listdir(custom_nodes_path):
                if os.path.isdir(os.path.join(custom_nodes_path, item)):
                    try:
                        module = importlib.import_module(item)
                        if hasattr(module, 'NODE_CLASS_MAPPINGS'):
                            for node_name, node_class in module.NODE_CLASS_MAPPINGS.items():
                                display_name = getattr(module, 'NODE_DISPLAY_NAME_MAPPINGS', {}).get(node_name, node_name)
                                node_info[node_name] = {
                                    'display_name': display_name,
                                    'description': getattr(node_class, 'DESCRIPTION', ''),
                                    'category': getattr(node_class, 'CATEGORY', 'uncategorized'),
                                    'module': item,
                                    **get_node_io_info(node_class)
                                }
                    except:
                        continue
    
    return node_info

def write_markdown_to_file(node_info: Dict[str, Dict[str, Any]], output_file: str):
    """Write node information as markdown to a file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# ComfyUI Node Documentation\n\n")
        
        # Group by category
        by_category = defaultdict(list)
        for node_name, info in node_info.items():
            by_category[info['category']].append((node_name, info))
        
        # Write each category
        for category in sorted(by_category.keys()):
            f.write(f"## {category.upper()}\n\n")
            
            for node_name, info in sorted(by_category[category]):
                # Node header
                f.write(f"### {info['display_name']} (`{node_name}`)\n\n")
                
                # Description
                if info['description']:
                    f.write(f"{info['description']}\n\n")
                
                # Module info for custom nodes
                if info['module'] != 'nodes':
                    f.write(f"**Module:** `{info['module']}`\n\n")
                
                # Inputs
                if info['inputs']:
                    f.write("#### Inputs\n\n")
                    for input_name, input_info in info['inputs'].items():
                        req_status = "(required)" if input_info['required'] else "(optional)"
                        input_type = input_info['type']
                        
                        line = f"- `{input_name}` {req_status}: `{input_type}`"
                        
                        # Add tooltip if available
                        if input_name in info['input_tooltips']:
                            line += f"\n  - {info['input_tooltips'][input_name]}"
                        
                        # Add options if available
                        if input_info['options']:
                            opt_str = str(input_info['options']).replace('{', '{{').replace('}', '}}')
                            line += f"\n  - Options: `{opt_str}`"
                        
                        f.write(line + "\n")
                    f.write("\n")
                
                # Outputs
                if info['outputs']:
                    f.write("#### Outputs\n\n")
                    for i, (output_type, is_list, output_name) in enumerate(zip(
                        info['outputs'],
                        info['output_is_list'],
                        info['output_names']
                    )):
                        line = f"- `{output_name}`: `{output_type}`"
                        if is_list:
                            line += " (LIST)"
                        
                        # Add tooltip if available
                        if i < len(info['output_tooltips']):
                            line += f"\n  - {info['output_tooltips'][i]}"
                        
                        f.write(line + "\n")
                    f.write("\n")

def write_short_markdown(node_info, output_path):
    """Write a simplified markdown with just module names, node names, inputs and outputs"""
    modules = {}
    
    # Group nodes by module
    for node_name, node_data in node_info.items():
        try:
            module_name = node_data.get('module', 'Unknown')
            if module_name not in modules:
                modules[module_name] = []
                
            # Get inputs - handle both string and dict inputs
            inputs = []
            if 'inputs' in node_data:
                inputs = list(node_data['inputs'].keys())
            elif 'input' in node_data:  # Fallback for older format
                inputs = [str(inp) for inp in node_data['input']]
                    
            # Get outputs - handle both string and list outputs
            outputs = []
            if 'outputs' in node_data:
                outputs = node_data['outputs']
            elif 'output' in node_data:  # Fallback for older format
                outputs = node_data['output']
            
            # Ensure outputs are strings
            outputs = [str(out) if isinstance(out, (str, int, float)) 
                      else out[0] if isinstance(out, (list, tuple)) 
                      else str(out) for out in outputs]
                    
            # Create node entry
            node_entry = {
                'name': node_name,
                'inputs': inputs,
                'outputs': outputs
            }
            modules[module_name].append(node_entry)
        except Exception as e:
            print(f"Warning: Error processing node {node_name}: {str(e)}")
            continue

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        for module_name in sorted(modules.keys()):
            f.write(f"# {module_name}\n")
            
            # Sort nodes alphabetically within each module
            for node in sorted(modules[module_name], key=lambda x: x['name'].lower()):
                try:
                    inputs_str = ", ".join(str(inp) for inp in node['inputs']) if node['inputs'] else ""
                    outputs_str = ", ".join(str(out) for out in node['outputs']) if node['outputs'] else ""
                    f.write(f"- {node['name']} ({inputs_str}) => ({outputs_str})\n")
                except Exception as e:
                    print(f"Warning: Error writing node {node['name']}: {str(e)}")
                    continue
            f.write("\n")

if __name__ == '__main__':
    node_info = get_all_node_info()
    output_path = Path(__file__).parent / "INSTALLED_NODES.md"
    write_markdown_to_file(node_info, output_path)
    
    # Add short version
    short_output_path = Path(__file__).parent / "INSTALLED_NODES_SHORT.md"
    write_short_markdown(node_info, short_output_path) 