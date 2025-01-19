import os
import json
import requests
from urllib.parse import quote
import folder_paths
from typing import Dict, List, Any, Optional

class ScribeNode:
    """
    Scribe node that documents the current workflow state and node information
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "include_docs": ("BOOLEAN", {"default": True}),
                "output_format": (["json", "markdown"], {"default": "markdown"}),
            },
            "optional": {
                "docs_base_url": ("STRING", {
                    "default": "https://docs.getsalt.ai/md/Comfy/Nodes/",
                    "multiline": False
                })
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "scribe"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def __init__(self):
        self.output_dir = os.path.join(folder_paths.get_output_directory(), "scribe")
        os.makedirs(self.output_dir, exist_ok=True)
        
    def fetch_node_docs(self, node_type: str, base_url: str) -> Optional[str]:
        """Fetch documentation for a node type from the docs site"""
        try:
            url = f"{base_url.rstrip('/')}/{quote(node_type)}/"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return None
        except Exception as e:
            print(f"Error fetching docs for {node_type}: {e}")
            return None

    def get_node_info(self, node: Any) -> Dict[str, Any]:
        """Gather comprehensive information about a node"""
        info = {
            "id": getattr(node, "id", None),
            "type": node.type if hasattr(node, "type") else type(node).__name__,
            "name": getattr(node, "name", None),
            "description": getattr(node, "__doc__", None),
            "category": getattr(node, "CATEGORY", None),
            "inputs": {},
            "outputs": {},
            "connections": {
                "inputs": {},
                "outputs": {}
            }
        }

        # Get input types and values
        if hasattr(node, "INPUT_TYPES"):
            input_types = node.INPUT_TYPES()
            for input_category in ["required", "optional"]:
                if input_category in input_types:
                    for input_name, input_config in input_types[input_category].items():
                        info["inputs"][input_name] = {
                            "type": input_config[0],
                            "config": input_config[1] if len(input_config) > 1 else None,
                            "value": getattr(node, input_name, None)
                        }

        # Get output types
        if hasattr(node, "RETURN_TYPES"):
            for idx, output_type in enumerate(node.RETURN_TYPES):
                output_name = node.RETURN_NAMES[idx] if hasattr(node, "RETURN_NAMES") else f"output_{idx}"
                info["outputs"][output_name] = {"type": output_type}

        # Get connections
        if hasattr(node, "inputs"):
            for input_name, input_data in node.inputs.items():
                if input_data and hasattr(input_data, "links"):
                    info["connections"]["inputs"][input_name] = [
                        {"node": link.origin_node.name, "slot": link.origin_slot}
                        for link in input_data.links
                    ]

        if hasattr(node, "outputs"):
            for output_idx, output_data in enumerate(node.outputs):
                if output_data and hasattr(output_data, "links"):
                    info["connections"]["outputs"][f"output_{output_idx}"] = [
                        {"node": link.target_node.name, "slot": link.target_slot}
                        for link in output_data.links
                    ]

        return info

    def format_output(self, workflow_info: Dict[str, Any], format: str) -> str:
        """Format the workflow information in the specified format"""
        if format == "json":
            return json.dumps(workflow_info, indent=2)
        
        # Markdown format
        md_output = ["# Workflow Documentation\n"]
        
        for node_id, node_info in workflow_info["nodes"].items():
            md_output.append(f"## {node_info['name']} ({node_info['type']})\n")
            
            if node_info["description"]:
                md_output.append(f"{node_info['description']}\n")
            
            md_output.append("### Inputs\n")
            for input_name, input_info in node_info["inputs"].items():
                md_output.append(f"- **{input_name}** ({input_info['type']})")
                if input_info["value"] is not None:
                    md_output.append(f": `{input_info['value']}`")
                md_output.append("\n")
            
            if node_info["connections"]["inputs"]:
                md_output.append("\n#### Input Connections\n")
                for input_name, connections in node_info["connections"]["inputs"].items():
                    for conn in connections:
                        md_output.append(f"- {input_name} <- {conn['node']}.{conn['slot']}\n")
            
            if node_info["docs"]:
                md_output.append("\n### Documentation\n")
                md_output.append(node_info["docs"])
            
            md_output.append("\n---\n")
        
        return "\n".join(md_output)

    def scribe(self, include_docs: bool, output_format: str, docs_base_url: str = None) -> tuple[str]:
        """Main function to document the workflow"""
        workflow_info = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "include_docs": include_docs
            },
            "nodes": {}
        }

        # Get all nodes in the current workflow
        for node in self.get_workflow_nodes():
            node_info = self.get_node_info(node)
            
            # Fetch documentation if requested
            if include_docs and docs_base_url:
                node_info["docs"] = self.fetch_node_docs(node_info["type"], docs_base_url)
            else:
                node_info["docs"] = None
                
            workflow_info["nodes"][node_info["id"]] = node_info

        # Format output
        output = self.format_output(workflow_info, output_format)
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"workflow_doc_{timestamp}.{output_format}"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(output)
            
        return (output,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        """Always return True to generate fresh documentation"""
        return float("nan")
