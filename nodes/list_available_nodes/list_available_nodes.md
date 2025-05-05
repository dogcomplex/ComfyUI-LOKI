# Requirements: list_available_nodes

## DESCRIPTION

Lists available ComfyUI custom node packages, primarily by fetching the list used by ComfyUI-Manager.

## INTENT

To provide a dynamic list of known available custom nodes for discovery, installation planning, or analysis.

## NODE_STRATEGY

This node attempts to load the `custom-node-list.json` file cached by an existing ComfyUI-Manager installation. If the manager is not found or the cache is missing/invalid, it falls back to fetching the list directly from a specified GitHub URL (defaulting to the ComfyUI-Manager repository's list).

## INPUTS

- `manager_cache_path_override` (optional, STRING): Manually specify the path to the ComfyUI-Manager directory if automatic detection fails.
- `fallback_github_url` (optional, STRING): The URL to fetch the `custom-node-list.json` from if the local cache cannot be used.

## OUTPUTS

- `all_nodes_json` (STRING): A JSON string representing the entire list of available extensions/nodes.
- `summary_markdown` (STRING): A Markdown string summarizing the available extensions, grouped by category.
- `node_json_list` (LIST): A list where each item is a JSON string representing a single available extension.
- `node_markdown_list` (LIST): A list where each item is a Markdown string detailing a single available extension. 