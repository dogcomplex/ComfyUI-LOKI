import json
import os
import sys
from pathlib import Path
import requests
from collections import defaultdict

def get_manager_path():
    """Find ComfyUI-Manager directory"""
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    manager_path = os.path.join(base_path, "ComfyUI-Manager")
    return manager_path

def load_extension_list():
    """Load extension list from ComfyUI Manager's cache or fetch from GitHub"""
    cache_path = os.path.join(get_manager_path(), "cache", "custom-node-list.json")
    
    try:
        if os.path.exists(cache_path):
            with open(cache_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                data = json.loads(content)
                return data['custom_nodes'] if isinstance(data, dict) and 'custom_nodes' in data else data
        else:
            # Fallback to direct GitHub fetch
            url = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['custom_nodes'] if isinstance(data, dict) and 'custom_nodes' in data else data
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {str(e)}")
        print("Content causing error:", content[:100], "...")
        raise
    except Exception as e:
        print(f"Error loading extension list: {str(e)}")
        raise

def write_markdown(extensions, output_file):
    """Write extension information to markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Available ComfyUI Custom Node Packages\n\n")
        
        # Group by category if available
        by_category = defaultdict(list)
        uncategorized = []
        
        for ext in extensions:
            if 'category' in ext and ext['category']:
                by_category[ext['category']].append(ext)
            else:
                uncategorized.append(ext)
        
        # Write categorized extensions
        for category in sorted(by_category.keys()):
            f.write(f"## {category}\n\n")
            for ext in sorted(by_category[category], key=lambda x: x['title'].lower()):
                write_extension_info(f, ext)
        
        # Write uncategorized extensions
        if uncategorized:
            f.write("## Uncategorized\n\n")
            for ext in sorted(uncategorized, key=lambda x: x['title'].lower()):
                write_extension_info(f, ext)

def write_extension_info(f, ext):
    """Write individual extension information"""
    title = ext.get('title', ext.get('name', 'Unknown'))  # Fallback to 'name' if 'title' not present
    f.write(f"### {title}\n\n")
    
    if ext.get('description'):
        f.write(f"{ext['description']}\n\n")
    
    f.write(f"- **Author:** {ext.get('author', 'Unknown')}\n")
    if 'reference' in ext:  # Changed from 'repository' to 'reference'
        f.write(f"- **Repository:** [{ext['reference']}]({ext['reference']})\n")
    
    if ext.get('install_type'):
        f.write(f"- **Install Type:** {ext['install_type']}\n")
    
    if ext.get('nodeTypes'):  # Changed from 'nodes' to 'nodeTypes'
        f.write("\n**Included Nodes:**\n")
        for node in ext['nodeTypes']:
            f.write(f"- {node}\n")
    
    f.write("\n")

if __name__ == "__main__":
    try:
        extensions = load_extension_list()
        write_markdown(extensions, "AVAILABLE_NODES.md")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1) 