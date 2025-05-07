# REQUIREMENTS: Scribe Node

## DESCRIPTION

A node that generates documentation for the current ComfyUI workflow, including node details, connections, and optionally fetching external documentation for individual node types.

## INPUTS

-   **`include_docs`** (BOOLEAN, default: `True`): If enabled, the node attempts to fetch external documentation for each node type from the specified `docs_base_url`.
-   **`output_format`** (STRING: "json" | "markdown", default: "markdown"): Specifies the format of the generated documentation file and the output string.
-   **`trigger`** (*, optional): Connect an output from a later node here to delay the Scribe node's execution until that node finishes. This helps ensure the workflow data is available when Scribe runs.
-   **`docs_base_url`** (STRING, optional, default: "https://docs.getsalt.ai/md/Comfy/Nodes/"): The base URL used for fetching external node documentation.
-   **`filename_prefix`** (STRING, optional, default: "workflow_doc"): Prefix for the output documentation file name.

*(Hidden Input)*: The node implicitly receives the current workflow definition (prompt data) via a hidden `PROMPT` input provided by the ComfyUI execution system.

## OUTPUTS

-   **`documentation`** (STRING): The generated workflow documentation as a single string, formatted according to the `output_format` input. The content includes workflow structure, node details (ID, type, title, properties, widgets, connections), and fetched external documentation if `include_docs` is enabled.

## NODE_STRATEGY

This node is implemented as a standalone ComfyUI Python node (`scribe_node.py`). It relies on the ComfyUI execution system identifying the need for workflow data via the hidden `PROMPT` input and passing this data as a keyword argument (`prompt=...`) to the node's execution function. To ensure this data is available when the function is called, connect the optional `trigger` input to a node that executes late in the workflow. It parses the node and connection data, optionally makes external HTTP requests to fetch documentation, formats the information, saves it to a file in the main ComfyUI output directory (`<output>/LOKI/Scribe/output/`), and returns the documentation as a string. It uses standard Python libraries (`requests`, `json`, `pathlib`). 