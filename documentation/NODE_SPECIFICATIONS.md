# Node Specifications

This document describes the preferred standardized requirements for a "node" in the `ComfyUI-LOKI` project.

## Conceptual Overview

We want to create nodes as standalone modular components that perform a single task, and which conceptually align with ComfyUI's node-based interface design philosophy. This can range from very simple to somewhat complex tasks. Nodes are designed to be standalone importable modules, but may be implemented using other nodes as sub-processes, or use common python libraries.

`LOKI` nodes are special compared to standard ComfyUI nodes in that they are designed to cover a wider range of use cases. These don't all need to be implemented, but each of them must be possible to implement in the node's fully-built-out form. We refer to these as "layers" of a node, and are basically just implementations in different languages/mediums.

## Layers

Layers must match each other in functionality as closely as possible in *intent*, but may have different implementation details. There is no hard limit on the number of layers a node may have, but it should be possible to use all of them in conjunction with each other and expect the same result (subject to the limitations of the medium they operate in). Nodes are thus primarily identified by their distinct intent, not by their particular implementations.

### Layer Types:

#### ID LAYER: `<node_name>` parent folder
- AKA `<node_folder>`
- Simply having a folder with a unique name in the `ComfyUI-LOKI/nodes` directory designates it as a node. All other layers are optional from there, and should be added as needed.
- This project folder is the unique identifier for the node in all other contexts, and should be located in `ComfyUI-LOKI/nodes/<node_name>`. This folder should contain all these other layer files directly inside it.
- `<node_name>` must be in lowercase `snake_case`. All files within should use this same `<node_name>` naming convention.

#### REQUIREMENTS LAYER: `<node_name>.md`
- AKA "MANTLE LAYER"
- The master document for the node. This describes the node's intent, purpose, naming, and functionality in a high-level technical overview. This should be agnostic to the implementation details, and generally should shape other layers, but *may* be reciprocally impacted by them when common limitations are encountered.
- This should be treated as the source of truth for the node's functionality and behavior, and should be kept up to date as the node is developed.
- This is a technical requirements engineering document, and should use precise language to describe the node's functionality and behavior.
- This document should describe all `INPUTS` and `OUTPUTS` for the node (or specify if there are none), as well as describe any other relevant behavior or functionality which should be consistent across all layers.
- It is recommended that each node have a short `DESCRIPTION`, which should be a single sentence that captures the node's purpose and intent. A node that cannot be described in a single sentence should be considered as a candidate for a split into multiple nodes, if they do not exist already.
- A node *may* be the complex amalgamation of multiple nodes, in which case it should be described as such in this documentation under `NODE_STRATEGY`.
- A node *may* temporarily be a complex standalone node without sub-nodes, but this should be considered as a likely temporary state barring particular circumstances under `NODE_STRATEGY`.
- A node *may* be just a wrapper of 3rd party nodes or functions from other libraries or ComfyUI beyond LOKI. If so, this should be described under `NODE_STRATEGY`.

#### NAME LAYER: `<node_name>_name.md`
- A markdown file that contains the official full name of the node (English string with spaces), as well as any other naming information.
- Additional naming, e.g. using other cases and formats, if any, should be described in this document as well.
- It is recommended that each node have:
  - `TOKEN`: which is a unique identifier among all nodes, intended to be short and memorable to users. It is highly recommended that it start with (or entirely consist of) one or more EMOJIS which intuitively describe it. The `TOKEN` *may* be the emoji(s) with additional short text, e.g. `"🔍✋Detect"` for a node that searches for hands in an image. `TOKEN` should not include whitespace (use underscores sparingly instead).
  - `EMOJI_ICON`: which is a single emoji that visually represents the node's functionality but is non-unique (unlike the `TOKEN`). This is used as a default/fallback for the node's icon in the UI.
  - `RECIPE`: which takes the form of `<input tokens> => <output tokens>` and describes the node's functionality in a concise manner. Note pass-through tokens are just included on both sides. Try to use the canonical `TOKEN` form of inputs/outputs to describe this where applicable.
  - `X2Y_FORMAT`: which describes the node's functionality in simple terms as if it were a workflow, using the `X2Y_FORMAT.txt` format.
  - `ALIASES`: which are alternative names for the node that are not the official name.
  - `TAGS`: which are additional keywords that can be used to find the node in the UIs and searches.
  - `METAPHORS`: which are creative alternative ways to envision the node's functionality from an artistic or conceptual perspective. They need not be precise, but should be intuitive to a non-technical audience.

#### CONFIG LAYER: `<node_name>.json`
- A JSON file that describes the node's inputs, outputs, naming, constants, and any other relevant information which is used across multiple layers and is not solely relevant to the particular layer's implementation. This the config file for the node.

#### FUNCTIONALITY LAYER (PYTHON): `<node_name>.py`
- A python file that contains the core implementation logic for the node. Should be system agnostic and designed to be consumed by python projects in general as an importable library. May have a `__main__` block for direct calling via command line with sensible arguments/behavior matching the input/output intent of the node in general. ComfyUI-specific implementation details may be included here, or optionally split out to `<node_name>_node.py`.

#### INITIALIZATION LAYER: `__init__.py`
- A ComfyUI-compatible python `__init__` wrapper file which ensures that the node is properly imported and registered within ComfyUI systems. It should specify `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`, exported with ``__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']``. These mappings should preferably pull from a `<node_name>.json` file, but may be specified directly within the `__init__.py` file if necessary.
- Optionally: a node may have its own `requirements.txt` file, which should be used to describe this `<node_folder>`'s python package dependencies, and will be amalgamated by the `requirements.txt` file in the root of the project.


#### FUNCTIONALITY LAYER (COMFY-NODE): `<node_name>_node.py`
- A python file that contains the ComfyUI-specific implementation details for the node. This should be a thin wrapper around the core implementation logic, and should not include any additional functionality or behavior.

---

### OPTIONAL Layer Types:
These are not strictly necessary for functionality, and are generally not needed until the node is particularly highly complex or specialized and we need additional organization.

#### CACHE LAYER: `<node_folder>/output/` subfolder
- A subfolder caching the output of the node for various inputs. This behavior is OPTIONAL, disabled by default, and if it's implemented at all it should be described in the `REQUIREMENTS LAYER`. ComfyUI naturally caches outputs of nodes, so we do not prioritize this. However, it can be useful for nodes that perform expensive operations, such as model inference, with a large number of possible inputs.
- If used, file naming must be consistent with the input file naming, and might be a hash of the input file content if it cant be uniquely identified just by the input strings/numbers.
- Recommended for things like image/text generation, but not for simple operations or cheap intermediate steps.
- Note that the node cache might also simply use the ComfyUI folder's official output folder directly - i.e. `folder_paths.get_output_directory()`. This is generally recommended if the cached output should be user-facing, though you may want to output it to a `<official_comfy>/output/LOKI/<node_name>/output` subfolder for organization, and remember that there might be multiple instances of this same node running so output file names better be unique or handle collisions.

#### FUNCTIONALITY LAYER (COMFY-WORKFLOW): `<node_name>_workflow.json`
- An alternative implementation of the node's functionality as a ComfyUI workflow composed of even more primitive nodes than itself. This workflow should NOT use the node itself (`<node_name>_node.py`), but should be entirely composed of *other* ComfyUI nodes or *other* LOKI nodes. Conceptually, this is using the ComfyUI framework to implement the node's functionality rather than using raw python (`<node_name>.py`).
- These are rarely more efficient than the python implementation, but can be useful for testing the node's functionality and behavior in a real ComfyUI environment, or for demonstrating the node's functionality in a more intuitive way.
- This illustrates the recursive nature of nodes, and the fact that nodes can be used as building blocks for more complex workflows.
- Some nodes may be primarily implemented as a workflow (i.e. workflow-first), and may not have a python implementation at all, or may use ComfyScript (https://github.com/Chaoses-Ib/ComfyScript) or similar (https://github.com/atmaranto/ComfyUI-SaveAsScript) workflow-to-python translation techniques to use the workflow as a python script.
- This is actually the eventual recommended implementation strategy for nodes, and should be used whenever possible once our ecosystem has matured enough to represent everything easily as nodes.

#### TEST LAYER: `<node_name>_test.py`
- A python file that coordinates any related tests for the node. This should be in the root node folder (`<node_folder>/<node_name>_test.py`). If verbose or requiring additional files/data/etc, those should be placed in the `./tests` subfolder, with `<node_name>_test.py` used as the main entrypoint. Note that simply by having so many different layered implementations of a node we naturally have a lot of test coverage, so create these additional ones sparingly.
- `<node_folder>/tests/` subfolder: A subfolder containing any additional testing files for the node. Coordinated by `<node_folder>/<node_name>_test.py`
- `<node_name>_test_workflow.json`: A JSON file that contains a ComfyUI-compatible workflow which implements the node's functionality. This is used to test the node's functionality and behavior in a real ComfyUI environment, and should be as comprehensive as possible in testing all aspects of the node's functionality. Where possible it should use standard/official/stable ComfyUI input and output nodes to facilitate testing, so the emphasis should be on the node's functionality and behavior rather than the ComfyUI environment in general.
- Example implementations and executions would go in the `/tests/` subfolder, and would be named like `<node_name>_test_<example_name>.py` or `<node_name>_test_<example_name>.json` etc. Coordinated by `<node_name>_test.py`.
- Tests should primarily focus on ensuring that the node's functionality and behavior is correct, and that it is consistent with the `REQUIREMENTS`. Tests that target specific implementation details (e.g. python specifics, rather than general requirements) should be marked separately.

#### DOCUMENTATION LAYER: `<node_folder>/docs/` subfolder
- A subfolder containing any additional documentation for the node. It should contain a `README.md` file with information about the node, as well as any other relevant documentation. It may contain images, diagrams, and other assets that help illustrate the node's functionality and behavior.

#### VISUAL LAYER: `<node_folder>/glamour/` subfolder
- The visual representation of the node

##### ICON LAYER:
- `<node_folder>/glamour/icon.png` as the official icon for the node.
- `<node_folder>/glamour/icon_prompt.txt` as generator text for the icon prompt, if applicable.
- `<node_folder>/glamour/icon_workflow.json` as the comfyui workflow used to generate the icon, if applicable. Ideally with its prompt and seed fixed for reproducibility.
- This may be a static image or an animated icon (if so, use a `.gif` file).
- It should be a square icon, and should be `512x512px` at least. It will be converted into other sizes and formats as needed.
- It should represent the node's functionality and intent in a visual way, conducive with the `REQUIREMENTS` and `NAME` layers, especially the `TOKEN` and `EMOJI_ICON`.
- But it may be a sophisticated or complex image potentially.
- Upon implementation (running an external icon-making script. Do not manually create these files), these files will be generated in the `<node_folder>` folder:
  - `<node_folder>/folder.ani`
  - `<node_folder>/desktop.ini`
  - `<node_folder>/folder.ico`
- The icon will also be used for additional glamour assets.
- `ICON` should be considered as an optional override to the node's fallback `EMOJI_ICON` (specified in `NAME` layer).

##### GLAMOUR UI LAYER:
- `<node_folder>/glamour/glamour.json` Describes the UI behavior of this node to be implemented with the `ComfyUI-LOKI/nodes/glamour` UI-generating node.
- `<node_folder>/glamour/glamour.png` The default look of the UI, if applicable.
- `<node_folder>/glamour/glamour_alt1.png` (etc) Used to describe alternative states of the UI, if applicable. Defined in the `glamour.json`
- NOTE: Glamour overrides may also be auto-generated and located in the `<official_comfy>/output/LOKI/<node_name>/glamour` subfolder, if applicable. This nuance will be handled by the glamour node itself, and is not required scope of a node's layer self-definitions. Just be aware your node may be visually overridden dynamically by the glamour node UI in practice.
- Example `glamour.json`:
```json
{
  "version": "1.0",
  "default_state": "default",
  "states": {
    "default": {
      "image": "glamour.png", // Default. Relative path within the glamour folder
      "widgets": { // Optional basic widgets overlayed on the image
        "seed_input": {
          "type": "NumberInput", // Could be 'NumberInput', 'TextInput', 'Dropdown', 'Checkbox', etc.
          "widget_ref": "seed",    // Name of the corresponding ComfyUI widget
          "position": [10, 50],   // [x, y] top-left corner relative to image top-left
          "size": [80, 20]        // [width, height]
        },
        "model_dropdown": {
            "type": "Dropdown",
            "widget_ref": "model_name",
            "position": [10, 80],
            "size": [150, 25]
        }
      }
    },
    "alt1": {
      "image": "glamour_alt1.png"
      // No widgets defined for this state, just the image
    },
    "alt2": {
        "image": "glamour_alt2.webp", // An animated state
        "play_mode": "loop" // "once", "loop", "ping-pong"
    }
  },
  "interactions": [ // Define clickable regions and their actions
    {
      "region": [10, 10, 40, 40], // [x, y, width, height] relative to image top-left
      "on_click": {
        "action": "cycle_states", // Action type
        "states": ["default", "alt1"], // States to cycle through
        "widget_ref": "mode_selector" // Optional: Update a hidden widget's value
      }
    },
    {
      "region": [50, 10, 90, 40],
      "on_click": {
        "action": "set_state",
        "state": "alt2"
      },
       "on_hover": { // Optional hover effect
           "tooltip": "Show animation"
       }
    },
    {
      "region": [100, 10, 140, 40],
      "on_click": {
        "action": "set_widget_value",
        "widget_ref": "seed",
        "value": 12345 // Set a specific value
      }
    }
  ]
}
```

###### CARD LAYER: `<node_folder>/glamour/card/`
- A subfolder containing the specific glamour representation of the node as a card. Use Tarot card proportions and symbolism by default.
- `<node_folder>/glamour/card/card.png` The default look of the card.
- `<node_folder>/glamour/card/card_workflow.json` A ComfyUI workflow used to generate the card.
- This is just going to be a particularly useful universal visual format for all nodes, so I'm specifying it explicitly here. As we come up with other common glamours we'll follow a similar subfolder structure.

#### CONTEXT LAYER: `CONTEXT.md`, `<node_folder>/context/`
- Holographic Principle.
- A markdown file that describes the node's relationship to other nodes within `ComfyUI-LOKI` and ComfyUI node ecosystem in general.
- This should be used to describe the node's dependencies, and any other relevant information about the node's place in the ecosystem.
- Use this to describe similar nodes, and how they might be related to each other or interact.
- Be very clear about direct connections/dependencies vs just speculative/potential ones. This should be used to evaluate potential ways to implement the node, outsource the node, or describe similar nodes this amalgamates/replaces, as well as to justify and contextualize its relative place in the ecosystem as a whole. It should not be comprehensive either.
- You may want to include context in relation to other python, or other programming languages, or github repositories performing similar functionality, if relevant.
- Do not fill this out if your node is just another recreation of the wheel for the ComfyUI ecosystem, like in every language (it's fine if we just recreate from scratch). This should primarily be used for nodes that are somewhat ambitious, where it's worth considering the tradeoffs between outsourcing and implementing it from scratch - or where other projects might benefit from this node's functionality.
- This is also a great place to pre-plan the node when it's need is not justified yet, and you need to do a sweep of the current ecosystem to see if it's worth implementing your own.
- Favor just using tags or linking to lists if you want to reference programming domains generally, and reserve individual project-specific callouts for particularly relevant details.

#### JAVASCRIPT LAYER: `<node_name>.js`
- If the node has JS elements or behavior where it needs to do input/output logic in the JS (other than the glamour stuff, which is largely implemented in a standalone node), the base node functionality (e.g. the python layer) probably should be re-implemented in JS too, so the node's functionality is identical in both languages. This might just be redundant, but it also probably beats having to pass data back and forth between the two layers.

#### `<LANGUAGE>` LAYER: `<node_name>.<other_programming_language_extension>`
- A node may very-well have equivalent implementations in multiple programming languages.
- This is just a reminder that if you do implement it in others (or if it's initial implementation is in another language/library and we're just wrapping it), it should still follow the same general guidelines and structure as the python layer (if possible) and should have its `REQUIREMENTS`, `CONFIG` and `NAME` layers specified.

#### LOCALIZATION LAYER: `<node_name>/localization/`
- Subfolder to throw alternative translations of the node's documentation, name, etc.

#### RESOURCES LAYER: `<node_name>/src/`
- A subfolder containing any additional resources for the node. This should be used for additional python files, or other resources that are not part of the core functionality of the node, but are still relevant to the node's implementation.
- Try to avoid using these if possible and keep nodes small. But you may likely need to download additional files etc so store them here.

#### SECURITY LAYER: `<node_name>/security/`
- More just aspirational than anything else for now: it would be cool to be able to zk-proof sign node implementations. This would be the security layer for the node, storing proofs of implementation and allowing users to verify that the node is implemented correctly and without malicious intent, and/or sign particular inputs/output instances. Then this node could be hosted anywhere and still trusted.
- Node hashes, signatures, etc throw in here.

# COMPATIBILITY

- All nodes in the `ComfyUI-LOKI` project must be compatible with each other. This means using a common `requirements.txt` file, and ensuring that all nodes are compatible with each other's dependencies. If a node really requires a unique dependency, it should be considered a highly breaking change and require either custom `requirements.txt` options or a new subclass of the project for a new subset of nodes. Avoid at all costs.
- Similarly, specific versions in `requirements.txt` in general should be treated very cautiously, and should be evaluated against all existing nodes in the repository to ensure compatibility.
- If a node needs an AI model or similar large-scale resource, it should make every attempt to try to be compatible with the official ComfyUI model directory access procedures, and should read from and be stored in the `<official_comfy>/models/` directories (note: ComfyUI lets users specify multiple model directories). Avoid anything like an auto-downloader unless it's explicitly specified in the `REQUIREMENTS` layer. If you absolutely cannot do this and still need the model, you should use the `<node_folder>/models/` directory, and consider this a strong code smell.

# NODE STRATEGY

- Nodes should be designed to be as small and focused as possible. They should do exactly one thing well, and should be designed to be used in conjunction with other nodes to create more complex workflows.
- The one thing a node does well might be the amalgamation of multiple other nodes, but you should limit the unique behavior being added by the node itself to a single thing, and try to keep the node's behavior as simple as possible.
- If a node is doing something that is not obviously a single thing, you should consider splitting it into multiple nodes if possible.

## NODE GROWTH

What follows is a likely timeline for the growth of a node, from lazy start to most refined:
- Level -1: A loose list somewhere pondering potential nodes to create.
- Level 0: **ID:** You make the unique folder name.
- Level 1: **CONTEXT:** Amalgamating loose notes about what the node might do and what other nodes out there do that's similar, figuring out if we even need this node at all. Skip this if you're already confident it's needed. (optional)
- Level 2: **REQUIREMENTS:** Write out the requirements for the node. Could be skipped straight to implementation and done later.
- Level 3: **FUNCTIONALITY:** (pick one)
  - Level 3A (Node Route): `COMFY-NODE` - Implement the ComfyUI node in python. Just aim to have something you can throw into comfy. Add the `INITIALIZATION` stuff and you're good to go.
  - Level 3B (Workflow Route): `COMFY-WORKFLOW` - Implement what you need as a ComfyUI workflow using other existing nodes. Ignore the rest of this list, you already have a workflow.
  - Level 3C (Python): `PYTHON` - You just need a python script for cmd line or other python stuff quickly. Just write it up and throw it in here. Likely naively throw outputs to `CACHE` (`./output/` folder).
  - Level 3D (...Other): `CONTEXT` - You got weird and creative and are just wrapping some other node or library, or even using another language. Sounds good, whatever, nodes are just modularity blueprints.
- Level 4: **TEST:** Probably just literally run it, either in python or comfy, and make sure it works. Add automated tests if you need to.
--- **GOOD-ENOUGH DEV POINT** ---
- Level 5: **CONFIG:** You're probably extending implementation to work for both regular python and ComfyUI nodes, so move shared data to a config file.
- Level 6: **NAME** (and **REQUIREMENTS** if you haven't already): Polish the purpose of this node a bit and give it a solid identity and requirements engineering document. Make sure it's distinct from other nodes and think about if there's other functionality you want to add or if that should be a new node.
- Level 7: **FUNCTIONALITY (Complete):** Polish any remaining functionality you wanted from it, or spawn off new nodes to do other stuff. Implement the other 2 routes from Level 3 (so, should work equally well as python cmd, comfy node, or comfy workflow).
--- **BACKEND DONE** ---
- Level 7: **VISUAL:** Visual polish. Make it nice. At least a single picture/icon, or a `CARD`.
- Level 8: **GLAMOUR:** Give it a polished UI, multiple metaphors, or animations. Perhaps custom `JS`. `ComfyUI-LOKI` should be able to now drill-down into your node with pretty non-techy representations of it.
--- **FRONTEND DONE** ---
- Level 9: **CONSISTENCY:** Make sure everything is complete and consistent, or delete superfluous information. Streamline. Don't forget to test everything again.
- Level 10: **PERFORMANCE:** Make sure it's fast. Throw the mess in `RESOURCES` (`./src/`) or `CACHE` (`./output/`) folders.
- Level 11: **DOCUMENTATION** and **ICON:** Now you're just being a keener. You know only other devs will see this part, right? More likely just their AIs, too.
--- **FULL RELEASE** ---
- Level 12: **LANGUAGES:** Implement in other programming languages / systems and go and conquer the world. Probably `LOCALIZATION` too.
- Level 13: **SECURITY:** ZK-proof sign your node. Oh god, now it's on a blockchain?
- Level 14: **CALCIFY:** Make it a cryptographically-proven private operation with no entropy leakage, or split that into a rock-hard sub-node with a softer governance/trust wrapper. Are we even programming any more or creating new Laws?
--- **READY FOR POST-CENTRALIZED WORLD** ---


