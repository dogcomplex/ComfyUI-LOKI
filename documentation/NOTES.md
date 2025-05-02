Some rough planning notes that may be outdated:

# FORMATS:

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



# CONVERSIONS:

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


