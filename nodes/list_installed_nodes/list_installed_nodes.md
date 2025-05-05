# Requirements: list_installed_nodes

## DESCRIPTION

Lists all detected custom nodes installed in the ComfyUI environment.

## INTENT

To provide a dynamic list of installed custom nodes for inspection or use in other nodes.

## NODE_STRATEGY

This node scans the ComfyUI `custom_nodes` directory (and potentially other configured node directories) to identify installed nodes. It likely relies on ComfyUI's internal node loading mechanisms or directory scanning.

## INPUTS

- `trigger` (optional, any type `*`): An optional input that can be used to trigger re-execution of the node when the input changes.

## OUTPUTS

- `NODE_LIST` (LIST): A list of strings, where each string represents an identified installed custom node (e.g., by class name, display name, or module path). 