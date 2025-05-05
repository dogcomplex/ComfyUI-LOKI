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

#### STATUS LAYER: `STATUS.md`
- A description of the current status of the node, including any known limitations or issues.
- This should be updated as the node is developed to reflect the current state of the node
- This is where we include lists of TODOs, tasks, planning, future work speculation, etc.

#### NAME LAYER: `<node_name>_name.md`
- A markdown file that contains the official full name of the node (English string with spaces), as well as any other naming information.
- Additional naming, e.g. using other cases and formats, if any, should be described in this document as well.
- It is recommended that each node have:
  - `TOKEN`: which is a unique identifier among all nodes, intended to be short and memorable to users. It is highly recommended that it start with (or entirely consist of) one or more EMOJIS which intuitively describe it. The `TOKEN` *may* be the emoji(s) with additional short text, e.g. `"🔍✋Detect"` for a node that searches for hands in an image. `TOKEN` should not include whitespace (use underscores sparingly instead).
  - `EMOJI_ICON`: which is a single emoji that visually represents the node's functionality but is non-unique (unlike the `TOKEN`). This is used as a default/fallback for the node's icon in the UI.
  - `RECIPE`: which takes the form of `<input tokens> => <output tokens>` and describes the node's functionality in a concise manner. Note pass-through tokens are just included on both sides. Try to use the canonical `TOKEN` form of inputs/outputs to describe this where applicable.
  - `X2Y_FORMAT`: which describes the node's functionality in simple terms as if it were a workflow, using the `X2Y_FORMAT.txt` format. e.g. T2I_Flux might be used for text-to-image Flux model generation.  It is suggested (but not required) that this format be used for `<node_name>` to begin with, though `X2Y_FORMAT` might be the capitalized or longer form of it.
  - `ALIASES`: which are alternative names for the node that are not the official name.
  - `TAGS`: which are additional keywords that can be used to find the node in the UIs and searches.
  - `METAPHORS`: which are creative alternative ways to envision the node's functionality from an artistic or conceptual perspective. They need not be precise, but should be intuitive to a non-technical audience.

#### CONFIG LAYER: `<node_name>.json`
- A JSON file that describes the node's inputs, outputs, naming, constants, and any other relevant information which is used across multiple layers and is not solely relevant to the particular layer's implementation. This the config file for the node.

#### FUNCTIONALITY LAYER (PYTHON): `<node_name>.py`
- AKA "LOKI SCRIPT" or "LOKI PYTHON"
- A python file that contains the core implementation logic for the node. Should be system agnostic and designed to be consumed by python projects in general as an importable library. May have a `__main__` block for direct calling via command line with sensible arguments/behavior matching the input/output intent of the node in general. ComfyUI-specific implementation details may be included here, or optionally split out to `<node_name>_node.py`.

#### INITIALIZATION LAYER: `__init__.py`
- A ComfyUI-compatible python `__init__` wrapper file which ensures that the node is properly imported and registered within ComfyUI systems. It should specify `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`, exported with ``__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']``. These mappings should preferably pull from a `<node_name>.json` file, but may be specified directly within the `__init__.py` file if necessary.
- Optionally: a node may have its own `requirements.txt` file, which should be used to describe this `<node_folder>`'s python package dependencies, and will be amalgamated by the `requirements.txt` file in the root of the project.

#### FUNCTIONALITY LAYER (COMFY-NODE): `<node_name>_node.py`
- AKA "LOKI NODE"
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
- AKA "LOKI FLOW" or "LOKI WORKFLOW"
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

#### DOCUMENTATION LAYER: 
- `README.md` main handler
- `<node_folder>/docs/` subfolder for additional documentation / formats / analysis / etc
- A subfolder containing any additional documentation for the node. It may contain images, diagrams, and other assets that help illustrate the node's functionality and behavior.

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
- If we have a workflow, it should have a visual representation where the workflow is embedded in the metadata.  This could trivially be the icon, or could be more complex like the visual node representation (glamour) of the workflow itself.  Specify the filename for this in CONFIG but likely <node_folder>/<node_name>_workflow.png or similar.

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
- Level 2: **REQUIREMENTS:** Write out the requirements for the node. Could be skipped straight to implementation and done later.  But keep in mind this is essentially the LLM prompt which everything else spins out of.
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




# FUNCTIONAL FORMATS:

### Python Script: 
- just any python script, could be imported or a github repo or our own script.  No guarantees on format/usability (e.g. might not be easily importable or callable). Might not even be working!

### LOKI Python Script (LOKI Script / LOKI Python): 
- our own python wrapper around 3rd party Python code, or written from scratch.  Either way, guarantees it's callable via __main__ cmd line with all inputs specified and outputs to reasonable places (default <node_folder>/output/).  
- Probably reserve --output as specifying output folder.  May have other standard reserved arguments.
- Is expected to be treated as a standalone modular directly-callable script, though may have dependencies (requirements.txt etc).  
-Must also be importable as a python module locally.  (Might extend this to make it available as a python LOKI package later. Not a current requirement.)  
- May have dependencies on ComfyUI framework and custom_nodes e.g. if it's wrapping a custom node and converting it to a python script, or using ComfyScript.  Either way it needs to give the same python functionality guarantees.

### ComfyUI Node: 
- a regular comfyui node from a custom_nodes folder, which is likely a github repo with a bunch of nodes all interconnected and possibly nontrivial to extract individually.    

### LOKI ComfyUI Node (LOKI Node): 
- May be a wrapper around python or even a wrapper around another comfy node or workflow.  Regardless, intended to work as a standalone modular directly-usable node.  
- Will have the same node compatibilities within the ComfyUI space as other LOKI nodes - e.g. Glamour, caching controls, etc.  These are not well defined yet as of this writing, but we'll likely have to set a stronger standard than most nodes, and will definitely have to store our own extra data/wrappers for nodes.
- Likeliest complexity will be Glamour compatibility and metaphorical representation of the node, which we need to store in our caches.  It *is possible* to do that dynamically though and store in e.g. the <comfyui_root>/output/LOKI/<node_name>/glamour folder, but expect that will be a mirror of the cached defaults we store in LOKI for each other node.  Likelier we just go through the lists and make our own default glamours.  Basically expect that even if we're merely wrapping someone else's node, we're doing so much meta-analysis and visualization that it's its own thing.  Which is a damn good argument for just automating reverse-engineering of those and making our own standalone copy of every function out there... 

### ComfyUI Workflow:
- a regular comfyui workflow, typically a json file that might be in API format or not, might have messy execution flow or superfluous nodes, might have adult content, might have notes etc, might have a very particular visual arrangement, and likely has a big list of custom nodes it relies upon.  Might itself just be an image (or a video?) with the workflow embedded in it.

### LOKI ComfyUI Workflow (LOKI Flow):
- *Level 1:* A LOKI-style workflow should do one thing and do it well, with little other mess.  If it's a complex workflow, it's likely to be a wrapper around other nodes or workflows which do the (reusable, useful, modular) sub-tasks and has very little unique complexity to itself.
- But the challenge to that is usually those sub-nodes or sub-workflows don't exist yet, so:
- *Level 2:* We basically want to be able to represent any standard workflow as a single comfyui node which just recurses into those workflow steps (behind the scenes at least).  This was proven doable by the https://github.com/vivax3794/ComfyUI-Sub-Nodes project (now discontinued) so we have to reverse-engineer that into our own `workflow_node` node, probably, which just takes a workflow file and runs it as if it were a comfyui node.
- We'll have to make sure that the workflow node can handle all the inputs and outputs of the nodes it recurses into, which may be a challenge - and Sub-Nodes didn't do that automatically, instead requiring people to manually insert Input / Output nodes that catch those.
- We can likely get an LLM to do the Input/Output mapping easily (but requiring an LLM), or we can probably even use a default rule-of-thumb script to do it (e.g. look for every loose input field, every SaveAs output), but it's not entirely trivial on arbitrary workflows.  Might need to require minor conversion of the workflow .json to add those nodes (so users gotta do it themselves, or have an LLM do it).
- But if we can at least just get Sub-Nodes functionality reliably working, we can split workflows into only small non-complex modular pieces that are easier to work with. (or easy to just write into python nodes/scripts that might implement the workflow faster).
- Likely implementation path:  get ComfyScript (or that Save-as-script) thing to just convert workflows to python scripts and have that be what executes with our simulated workflow-node wrapper.  That should work fairly easily.  
- *Level 3:* Now, more ambitious:  in all likelihood we're being opinionated on workflows already.  We might just want to be even *more* opinionated and do our own auto-rearranging or chopping up of them in practice.  So, input a standard comfyui workflow and we split them into a whole recursive structure of sub-workflows corresponding to our modular workflows (or creating new nodes/workflows if we notice some sub-steps are useful/interesting).  This should be doable with an LLM, but probably requires some custom code to do it.  So now we have a modular workflow standard.
- *Level 4:* Main thing we're trying to eventually achieve though is the ability to use a workflow as if it were a node or a workflow interchangeably, and in the near future, be able to represent *any* node or python function as a workflow too, so that non-technical users can just follow the pretty graph along to see how it does things.  This means going back the other way: node => Workflow conversions.  But first just being able to visualize sub-workflows at all instead of just running them behind-the-scenes is more important.
- We'll want our workflow node to be able to be expandable into the sub-workflow to show what's going on, which means new headaches of compatibility with the way comfyui views workflows.  
- *Level 5:* Ideally we should be able to see live program flow as queues process through that sub-workflow, and then be able to minimize it back to the parent graph and continue seeing the execution.  
- This should be recursive - drilling down as far as you can til you hit the most trivial nodes.  
- This all doesn't even have to be how the node / workflow is implemented, these could be *virtual* workflows that just simulate what's happening possibly, but probably better to just genuinely break stuff down into workflows.
- *Level 6:*  Now we have sub-workflows visualizable and have a full standard modular system for representing workflows.  Lets now start converting nodes to workflows too - have an LLM read through what the node does and recreate it as a series of primitive nodes in a new workflow.  That way any time we want to analyze what a node is doing we can just "drill down" into it and see the workflow code flow instead.  Then zoom back out to see the simplified parent graph.  All just different fidelities of the same thing.
- *Level 7:*  Add in Glamours, which we should already have on a per-node basis by now fairly easily (see Node Glamours), but since any node can itself be represented as a workflow of nodes each with *their own* glamours, we can probably use some compounding metaphor for the different zoom levels so it feels like you're looking at the micro-world of a node.  This would probably just be another glamour metaphor, minorly influenced by its parent and the potential additional zoom-ins of its nodes.  Basically just trying to make a single all-encompassing metaphor for the entire macro/micro system of a workflow.
- *Level 8:* Annnnd because the LOKI system as a whole is just a big bunch of workflows which can all be connected together to a single resource dispatcher, the entire system can all be represented as one super-macro workflow and that's the LOKI OS as a whole. 🦊  All one giant-ass metaphoric world that corresponds to actual program flows.  Actually, we can probably get this macro-system itself as early as Level 2.  It's just a long chain of workflows calling workflows.  But it takes the pretty visual navigation (and the ability to continue recursing down past the node level into workflow metaphors of nodes) to give it full breadth.
- And of course, because we're stylish, we'll need to make this entire thing simply be a single image file of the LOKI "World" metaphor, which you can then drag into comfyui as a workflow, which installs the custom_nodes dependency of ComfyUI-LOKI, and thus bootloads the sub-workflows as well.  Our OS is a single image file! 🦊



# FUNCTIONAL CONVERSIONS:

### LOKI Script => LOKI Node:
- Generally just trivially wrap the script in a comfy node class.  Should suffice for most cases.
- We will add Glamour visuals etc later, but for just functionality it's a simple wrapper.

### LOKI Script => LOKI Flow:
- Convert to LOKI Script first (much easier).  Then we analyze them both to make this one
- Much more complex, and we'll probably not do these for a while.  Requires a node library mimicking most of the python functionality, so we can recreate the same effect of the original script as a ComfyUI workflow (with LOKI standardization).
- Probably pre-requisite would be to create nodes for each distinct python function in the script.  But we also dont want to be too micro (i.e. ideally the workflow should really just decompose into only a few sub-workflows, not a bunch of tiny nodes), so we actually want to split the script into its component pieces as macro as possible, focusing on what *this script* really adds to it that the subcomponents don't already cover.  Each of those subcomponents should be their own LOKI Node or LOKI Flow, and then we can use the workflow node to recursively expand them.
- So likely our converter needs to be a smart introspection basically asking "how could we break this script down into its largest component pieces?"  And then we can just recursively apply that to each sub-piece, while being pragmatic about creating genuinely-useful subcomponents.  This will also cause massive node bloat.
- Note that if the LOKI Script / LOKI Node is a wrapper around an external package we need the dependency of, then there's not much the LOKI Flow can do.  We can't actually recurse down into it - it's just a standalone single-node workflow.  Build it anyway though as there are bonus format things we probably want to do with it (e.g. put a Glamour node in it, forcing a ComfyUI-LOKI dependency to install the rest of the framework).

### LOKI Node => LOKI Script:
- Extract the functionality into the python script. Unlikely anything flows this direction though.
- If the node is a wrapper around another ComfyUI node, then the script probably has to be a wrapper too.  We might be able to recreate/reverse-engineer it though and just make a hardcoded standalone script.
- Consider dynamic vs hardcoded.  Might want separate nodes for the wrapper vs just our own version.

### LOKI Node => LOKI Flow:
- Convert to LOKI Script as well first (easy).  Then we analyze them both to make this one

### LOKI Flow => LOKI Script:
- MUCH easier than the other way around.  Just analyze the workflow and recreate it as a python script.  
- If component parts are needed as dependencies, then use ComfyScript (https://github.com/Chaoses-Ib/ComfyScript) or similar (https://github.com/atmaranto/ComfyUI-SaveAsScript) to extract them as python-callable script.
- Still need to wrap that and make sure it's callable via standard python and cmd line stuff.  This might be doable as a dynamic script/node (i.e. not using any LLM to do live conversions).
- Probably do both: hardcoded conversions (easier, but if there are dependencies you're still doing most of the dynamic linking work anyway) and then dynamic linking (more flexible but harder to get right)


### LOKI Flow => LOKI Node:
- Similar to LOKI Script.  Do that first, then just wrap it back into a node probably.
- We *could* just have a dynamic node that runs the workflow as if it were a node using the ComfyUI-Sub-Nodes project style.  It would allow any workflow to be run that way without an LLM doing this conversion.  But generally if we already own the whole workflow, we can just hardcode it down to a node.


---


### Python => LOKI Script: 
- Easy.  Just needs to ensure LOKI guarantees of capability are met.  Simple scripts are doable with just LLM + testing loop.  
- Complex scripts are just wrapped.  If wrapping a whole repo of dependencies store in `<node_folder>/src` and add a `<node_folder>/requirements.txt`.  Or just find a way to do it all as just a python import instead of needing the repo.
- Ideally though (i.e. once we're in massive-framework-mode) break the complexity down into multiple smaller LOKI Scripts
- Note that LOKI Scripts might often just use the same backend package to do *one thing* with some subset of the inputs / outputs.  So feel free to slice it into a single conceptual piece or many pieces.


### Comfy Node => LOKI Node:
- Probably want to just figure out what it's doing first and recreate as a LOKI Script first.  Then wrap it in a node.
- challenge is basically reverse engineering someone's node.  Somewhat automateable but legal concerns possibly, and generally not needed (loses whatever their updates are).  Might be handy though for keeping things modular and reliable...  If we do this, we'll have to assess licensing/copyright and do it carefully.
- Could also just *wrap* their nodes but maintain the wrapper here legally fine which keeps functional compatibility, but then there's still a dependency, and still iffy if we want to re-implement for e.g. python cmd
- Easy enough with ComfyScript / Save-as-script path.
- If we reverse engineer it or extract it directly (e.g. if it's totally open source), then should still expect to need to analyze the whole node's repo to make sure the node itself can be extracted cleanly.  Not trivial.
- Probably:  if the node is something we can just recreate in python without dependencies or legal issues, just do that.  Unless the node author is really good and we want to rely on their updates.  Else it's better to just have it stable and reliable.
- Else:  just wrap their node.  Probably using ComfyScript / Save-as-script, and having a dependency.
- If the wrapper itself is generic, we probably dont even have to do wrapping - we'll just use their node directly.  Buuuut - we probably need to reserve the namespace in our list of nodes, as we'll probably be adding a glamour for it still.  Whiiich - might be best packaged and shared as just a wrapper node anyway.
- I'm leaning towards recreating whenever possible, else wrapping. 
- The nice thing about nodes though is they're at least already scoped about right, so we likely dont have to split them into multiple simpler nodes.
- The easiest way to wrap a node *might be* to just make it a single-node workflow and then just start building out our recursive workflow stuff to use that.


### Comfy Workflow => LOKI Flow:
- This one might actually be easy.  We dont *have* to convert it to a script or node at all.  We can just store the workflow .json locally and turn it into a node later if we want to.
- We might want to standardize it to have a limited set of inputs/outputs explicitly defined, but again - we dont *have* to do that.  We can just use the workflow as-is.
- Its interesting...  ultimately the format we want everything in is ideally just gonna be LOKI Flows of every process into simpler sub-processes.  We don't actually even need LOKI Node or LOKI Script - those are just hardcoded versions which might make transition periods easier, or might be more efficient to actually run than the flows.  
- I think it's still important to have all 3 usually, but we should be moving towards flows as the primary format.
- Flows are also *far* more open and remixable than nodes or scripts if you have ComfyUI already.




