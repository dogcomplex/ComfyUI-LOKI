# Glamour Node Requirements (`glamour.md`)

## DESCRIPTION

Provides a dynamic, visually customizable UI overlay framework for other ComfyUI nodes within the LOKI ecosystem.

## PURPOSE

To allow nodes to define custom visual appearances and interactive behaviors directly within the ComfyUI graph interface, overriding the standard node presentation. This enhances user experience by providing richer visual feedback and node-specific controls integrated into their visual representation.

## INPUTS

*   **Implicit (Configuration):** Relies on target nodes having a `glamour/` subfolder containing:
    *   `glamour.json`: Defines UI states, images, widget mappings, and interactions.
    *   Image Assets (e.g., `glamour.png`, `glamour_alt1.png`): Visuals for different states.
*   **Implicit (API Calls):** Receives requests from its JavaScript counterpart (`js/glamour-*.js`) via internal ComfyUI server routes to:
    *   Get glamour image paths (`get_glamour_path`).
    *   Check image timestamps (`check_glamour_timestamp`).

## OUTPUTS

*   **Implicit (UI Modification):** Modifies the visual appearance and behavior of target ComfyUI nodes in the frontend graph. Does not output data directly into the workflow graph connections.

## NODE_STRATEGY

This is a core UI infrastructure node for the LOKI project. Its implementation is split:
*   **Backend (Python):** `glamour_node.py` defines the ComfyUI node structure and registers server API endpoints. `glamour_utils.py` handles file path logic and image management.
*   **Frontend (JavaScript):** Files in the `js/` directory (`glamour-ui.js`, `glamour.js`, `glamour-images.js`) handle the rendering of overlays, interaction logic (clicks, hovers), state management, and communication with the Python backend via API calls.

It acts as a central service that other LOKI nodes utilize by providing the necessary configuration files in their respective `glamour/` subdirectories. 