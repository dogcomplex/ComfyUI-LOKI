import os
import json
import requests
from urllib.parse import quote
from pathlib import Path # Use pathlib
from typing import Dict, List, Any, Optional
from datetime import datetime # Need to import datetime
import server # Need server instance to access graph
import re

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
                 # Add trigger mechanism if needed, otherwise it runs on every change
                "trigger": ("*", {}) # Accepts any input to trigger execution
            },
            "optional": {
                "docs_base_url": ("STRING", {
                    "default": "https://docs.getsalt.ai/md/Comfy/Nodes/",
                    "multiline": False
                }),
                "filename_prefix": ("STRING", {"default": "workflow_doc"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "scribe"
    CATEGORY = "utils/docs" # Slightly more specific category
    OUTPUT_NODE = True # Output is saved to file and returned as string

    # Store output dir relative to this node's file
    NODE_OUTPUT_DIR = Path(__file__).parent / "output"

    def __init__(self):
        # Ensure the node-specific output directory exists
        self.output_dir = ScribeNode.NODE_OUTPUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # Need access to the graph - typically via the server instance
        self.server = server.PromptServer.instance

    def fetch_node_docs(self, node_type: str, base_url: str) -> Optional[str]:
        """Fetch documentation for a node type from the docs site"""
        if not base_url or not node_type:
            return None
        try:
            # Ensure base_url ends with a slash
            if not base_url.endswith('/'):
                base_url += '/'
            # URL encode the node type
            url = f"{base_url}{quote(node_type)}.md" # Assuming .md extension
            print(f"Fetching docs from: {url}")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Maybe strip frontmatter if present? For now, return raw text.
                 return response.text
            else:
                print(f"Docs fetch failed for {node_type} (Status: {response.status_code})")
                return f"Failed to fetch documentation (Status: {response.status_code})"
        except requests.exceptions.RequestException as e:
            print(f"Error fetching docs for {node_type}: {e}")
            return f"Error fetching documentation: {e}"
        except Exception as e:
            print(f"Unexpected error fetching docs for {node_type}: {e}")
            return f"Unexpected error fetching documentation: {e}"


    def get_node_info(self, node_data: Dict[str, Any], all_nodes_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gather comprehensive information about a node from its graph data"""
        node_id = str(node_data.get("id", "unknown"))
        node_type = node_data.get("type", "unknown")

        info = {
            "id": node_id,
            "type": node_type,
            "title": node_data.get("title", node_type), # Use title if available
            "properties": node_data.get("properties", {}),
            "widgets_values": node_data.get("widgets_values", []),
            "inputs": {},
            "outputs": {},
            "connections": {"inputs": {}, "outputs": {}},
            "position": node_data.get("pos", [0, 0]),
            "size": node_data.get("size", [0, 0]),
            # Placeholder for fetched docs
            "description": f"Node Type: {node_type}", # Basic description
            "docs": None
        }

        # --- Inputs ---
        if "inputs" in node_data:
            for input_info in node_data["inputs"]:
                input_name = input_info.get("name", "unknown")
                input_type = input_info.get("type", "*")
                link_id = input_info.get("link", None)

                info["inputs"][input_name] = {
                    "type": input_type,
                    "link": link_id,
                    "origin_node": None, # Will be filled later if linked
                    "origin_slot": None,
                }

                # Find connection source
                if link_id is not None:
                    for other_node_id, other_node_data in all_nodes_data.items():
                        if "outputs" in other_node_data:
                            for output_idx, output_info in enumerate(other_node_data["outputs"]):
                                if "links" in output_info and link_id in output_info["links"]:
                                    info["inputs"][input_name]["origin_node"] = str(other_node_id)
                                    info["inputs"][input_name]["origin_slot"] = output_idx
                                    # Add to connections structure
                                    if node_id not in info["connections"]["inputs"]:
                                        info["connections"]["inputs"][node_id] = []
                                    info["connections"]["inputs"][node_id].append({
                                        "input_name": input_name,
                                        "origin_node_id": str(other_node_id),
                                        "origin_slot_index": output_idx,
                                        # Optionally add origin node title here if needed later
                                    })
                                    break # Found the source link
                            if info["inputs"][input_name]["origin_node"]:
                                break # Found the source node

        # --- Outputs ---
        if "outputs" in node_data:
            for output_idx, output_info in enumerate(node_data["outputs"]):
                output_name = output_info.get("name", f"output_{output_idx}")
                output_type = output_info.get("type", "*")
                links = output_info.get("links", [])
                slot_index = output_info.get("slot_index", output_idx) # Use provided index if available

                info["outputs"][output_name] = {
                    "type": output_type,
                    "links": links,
                    "slot_index": slot_index,
                    "targets": [] # Will be filled later
                }

                # Find connection targets
                if links:
                     if node_id not in info["connections"]["outputs"]:
                          info["connections"]["outputs"][node_id] = []

                     for link_id in links:
                          for target_node_id, target_node_data in all_nodes_data.items():
                               if "inputs" in target_node_data:
                                    for input_idx, input_info in enumerate(target_node_data["inputs"]):
                                         if input_info.get("link") == link_id:
                                             target_input_name = input_info.get("name", f"input_{input_idx}")
                                             info["outputs"][output_name]["targets"].append({
                                                 "target_node_id": str(target_node_id),
                                                 "target_input_name": target_input_name,
                                             })
                                             # Add to connections structure
                                             info["connections"]["outputs"][node_id].append({
                                                 "output_name": output_name,
                                                 "output_slot_index": slot_index,
                                                 "target_node_id": str(target_node_id),
                                                 "target_input_name": target_input_name,
                                                  # Optionally add target node title here if needed later
                                             })
                                             # Note: A single output can link to multiple inputs
                                             # Don't break here, find all targets for the link_id

        # --- Widget Values ---
        # Try to map widget values back to inputs if possible (requires node definition knowledge)
        # This is complex without loading the actual node class definition.
        # For now, just list them.
        # TODO: Enhance this by potentially looking up NODE_CLASS_MAPPINGS if feasible

        return info

    def format_output(self, workflow_info: Dict[str, Any], output_format: str) -> str:
        """Format the workflow information in the specified format"""
        if output_format == "json":
            # Use default=str to handle potential non-serializable types like datetime
            return json.dumps(workflow_info, indent=2, default=str)

        # Markdown format
        md_output = ["# Workflow Documentation\n"]
        md_output.append(f"Generated: {workflow_info['metadata']['timestamp']}\n")
        md_output.append(f"Includes External Docs: {workflow_info['metadata']['include_docs']}\n")
        md_output.append("---\n")

        # Sort nodes by ID for consistent output
        sorted_node_ids = sorted(workflow_info["nodes"].keys(), key=lambda x: int(x))

        for node_id in sorted_node_ids:
            node_info = workflow_info["nodes"][node_id]
            node_title = node_info.get('title', node_info['type'])
            md_output.append(f"## Node {node_id}: {node_title} (`{node_info['type']}`)\n")

            md_output.append(f"- Position: `{node_info.get('position')}`")
            md_output.append(f"- Size: `{node_info.get('size')}`\n")

            if node_info.get("properties"):
                md_output.append("### Properties\n")
                for key, value in node_info["properties"].items():
                     md_output.append(f"- `{key}`: `{value}`")
                md_output.append("\n")

            if node_info.get("widgets_values"):
                md_output.append("### Widget Values\n")
                # Try to provide more context if widget names exist (not guaranteed in basic graph data)
                widget_values = node_info["widgets_values"]
                if isinstance(widget_values, list):
                    for idx, value in enumerate(widget_values):
                        md_output.append(f"- Widget {idx}: `{value}`")
                elif isinstance(widget_values, dict): # Some nodes might store widgets differently
                    for name, value in widget_values.items():
                        md_output.append(f"- {name}: `{value}`")
                md_output.append("\n")


            md_output.append("### Inputs\n")
            if node_info["inputs"]:
                for input_name, input_data in node_info["inputs"].items():
                    connection_info = ""
                    if input_data["link"] is not None and input_data["origin_node"]:
                        # Find the title of the origin node
                        origin_node_title = workflow_info["nodes"].get(input_data["origin_node"], {}).get('title', f"Node {input_data['origin_node']}")
                        origin_node_type = workflow_info["nodes"].get(input_data["origin_node"], {}).get('type', 'unknown')
                         # Find the name of the origin output slot
                        origin_output_name = f"output_{input_data['origin_slot']}" # Default name
                        origin_node_outputs = workflow_info["nodes"].get(input_data["origin_node"], {}).get("outputs", {})
                        for name, out_data in origin_node_outputs.items():
                            if out_data.get("slot_index") == input_data['origin_slot']:
                                origin_output_name = name
                                break

                        connection_info = f" <- `{origin_node_title}`.`{origin_output_name}` (Node {input_data['origin_node']}, Slot {input_data['origin_slot']})"
                    md_output.append(f"- **{input_name}** (`{input_data['type']}`){connection_info}")
            else:
                 md_output.append("*No inputs defined.*\n")
            md_output.append("\n")


            md_output.append("### Outputs\n")
            if node_info["outputs"]:
                 for output_name, output_data in node_info["outputs"].items():
                     md_output.append(f"- **{output_name}** (`{output_data['type']}`, Slot {output_data['slot_index']})")
                     if output_data["targets"]:
                         for target in output_data["targets"]:
                             target_node_title = workflow_info["nodes"].get(target['target_node_id'], {}).get('title', f"Node {target['target_node_id']}")
                             md_output.append(f"  - -> `{target_node_title}`.`{target['target_input_name']}` (Node {target['target_node_id']})")
            else:
                md_output.append("*No outputs defined.*\n")
            md_output.append("\n")

            # Include fetched documentation
            if node_info.get("docs"):
                md_output.append("### Documentation\n")
                md_output.append("```markdown") # Use code block for potentially raw markdown docs
                md_output.append(node_info["docs"])
                md_output.append("```\n")

            md_output.append("\n---\n")

        return "\n".join(md_output)

    def scribe(self, trigger=None, include_docs: bool = True, output_format: str = "markdown", docs_base_url: str = None, filename_prefix: str = "workflow_doc") -> tuple[str]:
        """Main function to document the workflow"""

        # Access the graph data from the server instance
        # The exact way to get the *current* graph might vary slightly
        # depending on ComfyUI version or context. PromptServer usually holds it.
        if not hasattr(self.server, 'prompt_queue') or not hasattr(self.server.prompt_queue, 'get_latest_prompt'):
             print("Error: Cannot access prompt queue or latest prompt.")
             return ("Error: Cannot access workflow data.",)

        # This might get the last *executed* prompt's workflow,
        # which might differ from the current state in the UI if changes were made.
        # Getting the live UI state is much harder from the backend.
        latest_prompt = self.server.prompt_queue.get_latest_prompt()
        if latest_prompt is None:
            print("Error: No prompt executed yet in this session.")
            return ("Error: No workflow executed yet.",)

        # The prompt data usually contains the workflow structure under 'workflow' or 'prompt'
        # Adjust key based on inspection of `latest_prompt` structure
        prompt_data = latest_prompt.prompt # Or latest_prompt.workflow, etc.

        if not isinstance(prompt_data, dict) or 'nodes' not in prompt_data:
            print(f"Error: Unexpected prompt data structure: {type(prompt_data)}")
            # Attempt to access graph directly (might be less reliable)
            if hasattr(self.server, 'graph'):
                 prompt_data = self.server.graph.serialize() # Or similar method if available
                 if 'nodes' not in prompt_data:
                     print("Error: Could not find nodes in direct graph access either.")
                     return ("Error: Could not find workflow nodes data.",)
            else:
                 return ("Error: Cannot access workflow nodes data.",)


        raw_nodes_data = {str(n['id']): n for n in prompt_data['nodes']} # Use dict indexed by ID

        workflow_info = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "include_docs": include_docs,
                "output_format": output_format,
                "docs_base_url": docs_base_url,
                 "prompt_id": getattr(latest_prompt, 'id', 'unknown') # Add prompt ID if available
            },
            "nodes": {}
        }


        # Process each node found in the prompt data
        for node_id, node_data in raw_nodes_data.items():
            node_info = self.get_node_info(node_data, raw_nodes_data) # Pass all nodes for connection lookup

            # Fetch documentation if requested
            if include_docs and docs_base_url:
                node_info["docs"] = self.fetch_node_docs(node_info["type"], docs_base_url)

            workflow_info["nodes"][node_id] = node_info # Store by ID


        # Format output
        output_string = self.format_output(workflow_info, output_format)

        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prefix = re.sub(r'[^\w\-_\. ]', '_', filename_prefix) # Sanitize prefix
        filename = f"{safe_prefix}_{timestamp}.{output_format}"
        filepath = self.output_dir / filename # Use pathlib Path object

        try:
            filepath.write_text(output_string, encoding="utf-8") # Use write_text
            print(f"Workflow documentation saved to: {filepath}")
        except Exception as e:
            print(f"Error saving workflow documentation: {e}")
            return (f"Error saving file: {e}",) # Return error message

        # Return the formatted string as output
        return (output_string,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Make it run every time its inputs change or it's triggered
        return float("nan") 