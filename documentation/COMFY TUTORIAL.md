
# COMFYUI GUIDE
This is a WIP guide to Open Source AI Image/Video/Text/Code Generation, centered around the ComfyUI Platform and all its possibilities.

## Table of Contents
- [Level 0: Total Beginner](#level-0-total-beginner)
- [Level 0.5: Casual GenAI](#level-05-casual-genai)
- [Level 1: Easy Local Official ComfyUI](#level-1-easy-local-official-comfyui)
- [Level 2: Portable ComfyUI](#level-2-portable-comfyui)
- [Level 3: Dockerized ComfyUI](#level-3-dockerized-comfyui)
- [The State of AI](#state-of-ai)
- [Misc Resources](#misc-resources)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)

It's my hope to continue updating this with advice for people at different skill/commitment levels, from total beginner to power user, while building a ComfyUI-based useful platform that targets a similar scope.  Open source AI tools should be accessible to everyone - we're not quite there yet, but those days are coming.  Those of us who are technical enough to wade through the current mess can help make that happen.

---

## LEVEL 0:  Total Beginner  {#level-0-total-beginner}
Real advice: Just use <a href="https://chatgpt.com/">ChatGPT</a>

###### Image Gen: {#image-gen}
- <a href="https://openai.com/index/introducing-4o-image-generation/">ChatGPT Guide</a>:  This will honestly probably outperform most local image generation stuff for a while and for any one-off task it's the first place to go.  It's also the most user friendly.  Only start down the rest of this rabbit hole when you're getting into bulk generations, chaining into a larger system, seeking privacy/security, or need specific abilities that ChatGPT can't handle.  We do local AI generation because of open source principles, control, security, and cheap price if you have the hardware already.   If you just want to generate an image (or keyframes for an animation, or consistent characters, or etc etc) just go with ChatGPT off the bat.
- <a href="https://tensor.art/">Tensor.art</a> also decent for simple one-off workflows that are just a bit more specific than chatgpt.  Free for non-bulk use
- I do think a chatbot wrapper for very beginner-friendly open source ComfyUI etc services will happen soon, mimicking the versatility of ChatGPT, but we need more organized systems and to train a model for tool use.  Should just be a url portal you talk to and "does the thing" though soon enough.

###### Video Gen: {#video-gen}
- Likewise, paid AI video gen services are probably always going to be easier and higher quality than local generation.  If you're just looking to generate a single video without much control, go with one of these.
(In rough recommended order.  Tbh I haven't really delved into any of these beyond cursory attempts and I'm not sure which is most beginner-friendly, but all are just web interfaces)
- <a href="https://minimaxaivideogenerator.org/">Minimax</a>
- <a href="https://www.klingai.com/global/">Kling</a>
- <a href="https://runwayml.com/">Runway</a>
- <a href="https://ltx.studio/">LTX Studio</a>
- <a href="https://pika.art/">Pika</a>
- <a href="https://www.krea.ai/">Krea</a>
- <a href="https://lumalabs.ai/">LumaLabs</a>
- <a href="https://haiper.ai/home">Haiper AI</a>
- <a href="https://openai.com/sora/">Sora</a>
Note: while still 1/1000th the price of a film studio to generate videos, these do add up if you're paying credits each time.  Locally-generated videos on your own hardware are the cheap option if you already have a decent video card

###### Text/Code/3D/Audio/etc TODO



---

## LEVEL 0.5:  Casual GenAI:  Cloud-hosted ComfyUI  {#level-05-casual-genai}
- These still aren't local open source, as you're just feeding your data to some computer on the internet to do the work, but they sure are convenient - and they let you understand what ComfyUI is without any installation.   Many applications can be built with this style of ComfyUI stuff as a background engine
https://comfyai.run/
- modify green-box prompt, click Queue, observe it flow through the steps, image comes out
https://comfy.icu/workflows/_8ydGT-ekfLY3dXwddfZE/edit
- same deal.  sign up, create workflow, click Queue, and off it goes
- many other demo workflows to choose from, hit Run Workflow to run the code yourself

###### Honourable mentions:
- <a href="https://github.com/ComfyWorkflows/ComfyUI-Launcher">ComfyUI-Launcher</a>
- <a href="https://runpod.io/">your own runpod instance</a>




---
## LEVEL 1: Easy Local Official ComfyUI  {#level-1-easy-local-official-comfyui}
- https://www.comfy.org/
- official ComfyUI .exe application installer (with Windows, Mac and Linux versions!)
- https://docs.comfy.org/installation/desktop/windows
- Install this first before you mess around with anything else.  It is likely all deeper stuff isn't going to be needed eventually, and this is the most official and easy way to get a working setup

---
<div style="background-color: #ff000015; padding: 1em; border-left: 4px solid #ff0000;">

#### ⚠️ WARNING: HERE THERE BE MONSTERS. ⚠️

- Past this point you are likely going to deal with non-user-friendly incredibly annoying bugs related to the bane of my existence that is the python package manager.  If you're a programmer or just competent enough with vibe coding to copy-paste error logs from comfy into an LLM and follow directions, you'll likely fare okay, but this stuff is nowhere near user friendly yet and needs serious stability polishing.
- I also generally assume you have at least 24GB VRAM going forward (aka a 3090rtx or 4090rtx or beyond).  Many workflows are still doable with e.g. 12 or 16GB VRAM, but most will become a lot trickier to run without a high VRAM card.  (Personally I am running mine on a 5090rtx 32GB VRAM beast now and upgrading my workstation further in preparation for video/game production) 
- Apple Mac Studios / M4 processors and similar are also going to create additional challenges.  Mac has limited support, but still works in various workflows.  In general though expect far slower speeds - but hopefully more efficient overall throughput if we run multiple instances of ComfyUI on its large VRAM or run higher-quality models.  Still, not an easy machine for fast tinkering with workflows.  I'd guess they're good for production once you have everything built already, not dev.
- I will gear specific advice towards a Windows setup, but the general principles should apply to any OS.  Linux may be easier in some ways.  Macs will be harder than either due to the unique graphics hardware.
</div>

---




## LEVEL 2: Portable ComfyUI  {#level-2-portable-comfyui}
- Build ComfyUI slightly more versatile, on bare metal but portable enough you can move it and replicate multiple copies for different builds.  
- Highly recommend putting it on an NTFS drive if running Windows so you can make virtual links to your model folders between each copy of comfy because you do *not* want to have to copy 500+GB of models.  And you will need at least that much storage space.
- I did not do this, so now I'm into considerably more annoying Dockerized Comfyui instances which use virtual volumes.  At least that ups the security though, which is honestly a major concern on bare metal if you're downloading too many comfy extensions/custom_nodes.
- TODO guide here but it's the same as the official comfyui portable install 
- https://docs.comfy.org/installation/comfyui_portable_windows
- this is probably my main recommended path for anyone who isn't too concerned with security yet and/or isnt doing doing devwork with various non-compatible workflows which require different system builds.  Good multi-purpose single build for tinkering that will last you a while.


---

## LEVEL 3: Dockerized ComfyUI  {#level-3-dockerized-comfyui}

- This is where you end up if you care about security, reconfigurable builds that can just be spun up for any particular dependency chain, and control.  I personally am really not a fan of Docker in general, and find this all impossible to deal with unless you're an experienced programmer, but it does the trick for now. Ultimately we probably need to wrap a better interface around all this for a more user-friendly version, or bake individual ComfyUI builds in secure containers.  I don't see easy paths to getting normal non-technical people using Docker reliably though.
- That said, <a href="https://comfydock.com/">Comfydock</a> at least tries to walk this path.  See the Pinokio section below
- But if you're already technical and you're more comfortable managing Dockerfile and docker-compose.yml yourself then just do that.   Will look similar to these, except you may want an older cuda version depending on your gpu and current cuda version, e.g. `FROM mmartial/comfyui-nvidia-docker:ubuntu24_cuda12.6.3-latest`  for 12.6.3 cuda:

```
# Base image with CUDA 12.8 and ComfyUI logic (for a 5090rtx card)
FROM mmartial/comfyui-nvidia-docker:ubuntu24_cuda12.8-latest

# Set default environment variables
ENV WANTED_UID=1000
ENV WANTED_GID=1000
ENV SECURITY_LEVEL=normal
ENV COMFY_CMDLINE_EXTRA="--fast"
ENV FORCE_CHOWN=yes

# Avoid overriding CMD or ENTRYPOINT — let base image init.bash handle startup

# Set the environment variable
ENV TORCH_CUDA_ARCH_LIST="9.0"
ENV BASE_DIRECTORY=/app/ComfyUI

# Add these lines before the VOLUME declarations
USER root
RUN mkdir -p /app/ComfyUI && chown -R 1000:1000 /app/ComfyUI

# Set back to non-root user
USER 1000:1000

# Required volume mount points
VOLUME ["/app/ComfyUI/input"]
VOLUME ["/app/ComfyUI/output"]
VOLUME ["/app/ComfyUI/user"]
VOLUME ["/app/ComfyUI/custom_nodes"]
VOLUME ["/app/ComfyUI/models"]

# Expose the default UI port
EXPOSE 8188
```

```
version: "3.9"

services:
  comfyui:
    image: comfydock-loki
    container_name: comfydock5090
    runtime: nvidia
    ports:
      - "8188:8188"
    environment:
      WANTED_UID: 1000
      WANTED_GID: 1000
      BASE_DIRECTORY: /app/ComfyUI
      SECURITY_LEVEL: normal
      COMFY_CMDLINE_EXTRA: "--fast"
      FORCE_CHOWN: yes
      TORCH_CUDA_ARCH_LIST: "9.0"
    volumes:
      # Main ComfyUI installation directory in WSL
      - /home/w/comfy-run:/comfy/mnt:rw
      # Your data mounts
      - /mnt/n/COMFY/wan_custom_nodes:/app/ComfyUI/custom_nodes:rw,z
      - /home/w/COMFY/models:/app/ComfyUI/models:rw,z
      # note: I am storing models on the WSL drive for faster model loading
      - /mnt/n/COMFY/COMFYPORT/ComfyUI/user:/app/ComfyUI/user:rw,z
      - /mnt/n/COMFY/COMFYPORT/ComfyUI/input:/app/ComfyUI/input:rw,z
      - /mnt/n/COMFY/COMFYPORT/ComfyUI/output:/app/ComfyUI/output:rw,z
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    user: "1000:1000"
```

#### Install:
- similar to:
```
sudo chown -R $(id -u):$(id -g) /home/w/comfy-run
sudo chown -R $(id -u):$(id -g) /mnt/n/COMFY/wan_custom_nodes
sudo chown -R $(id -u):$(id -g) /home/w/COMFY/models
sudo chown -R $(id -u):$(id -g) /mnt/n/COMFY/COMFYPORT/ComfyUI/user
sudo chown -R $(id -u):$(id -g) /mnt/n/COMFY/COMFYPORT/ComfyUI/input
sudo chown -R $(id -u):$(id -g) /mnt/n/COMFY/COMFYPORT/ComfyUI/output


docker build --no-cache -t comfydock-loki . 
docker compose up --force-recreate
```

- Note: I personally have only resorted to this crude self-configured docker stuff after wrestling with a 5090rtx's unique requirements.  An easier but still sometimes annoying option is to use:


### Pinokio - Comfydock  {#pinokio-comfydock}
- https://github.com/ComfyDock/ComfyDock-Pinokio
- I somewhat-like this method and would endorse it for most people if I didn't occasionally still encounter bugs which are hard to diagnose.  It is *almost* a click-only no-code solution to setting up ComfyUI in dockerized containers though, which I admire the ambition of
##### Steps:  
- basically just follow install instructions in https://github.com/ComfyDock/ComfyDock-Pinokio
- install Pinokio platform (which is kinda cool, as it's all a bunch of no-code installers for various AI apps.  Though I expect every one is still temporarily a buggy mess that doesnt *quite* live up to the promise yet)
- hit the Install & Update tab in the ComfyDock Pinokio extension, then Start, then Show Environments (each one churns its installs)
- essentially this is just a docker wrapper, but it lets you spin up multiple copies of comfyui for each particular application (if e.g. you're battling various compatibility issues across workflows)
- choose your docker image (12.4 cuda at least recommended for most cards, python 3.12), Environment Type: Default+Both, and then map to your shared folders for custom_nodes, user, models, output, input.  Note, newer gpus need cuda 12.8 which isnt supported yet in here
- Currently there is a narrow window in which I recommend this app... you have to be both a programmer and too lazy/unconfident to want to manage docker containers directly, and have hardware that doesn't push the limits.  The no-code feeling is nice though, and spinning up multiple docker containers is nice encapsulation.
- lol if you do end up using this, I found this hard reset to be the main solution to 90% of the bugs I encountered:
```
tasklist | findstr Pinokio
taskkill /IM Pinokio.exe /F
net stop winnat
net start winnat
```



---

## STATE OF AI (04/2025):  {#state-of-ai}
- Capabilities I'm keeping an eye on:

#### Animation is suddenly cheap and easy now:
- https://www.reddit.com/r/singularity/s/6BU3I8Xcfm
- this in particular looks like a genius new way to maintain consistency, and will probably have deeper implications for AI training outside this domain
- https://www.reddit.com/r/aivideo/comments/1jky598/what_if_studio_ghibli_directed_lord_of_the_rings/
- https://x.com/techhalla/status/1906433147211768140
	- animated stylized remakes are very doable for cheap now, especially with (but not requiring) chatgpt.
	- naive process is essentially: get each scene starting (and optionally end) frame, convert to your new style, put through video generator until you're happy, repeat (prompt each one)
	- https://github.com/dogcomplex/flow_animator is a crude version I made to do this splitting and prompt annotating automatically from source video (hit me up to fix it into working version if actually using it)
	- doable with Wan in ComfyUI too for free

#### Camera control is quite doable (along with any other visual effect) too:
- https://jianhongbai.github.io/ReCamMaster/
- https://github.com/TrajectoryCrafter
	- camera movements, open source version

#### Steerable Motion *in general* is quite doable:
- https://github.com/Eyeline-Research/Go-with-the-Flow
- These guys somewhat solved steerable motion for video generations.  You can now just input a very crude sliding puppet animation into it and get out a much more lifelike motion.  More importantly, this works for keeping *multiple clips* consistent with each other, thus avoiding the awkward feeling between clips where the AI suddenly reverses direction or changes the way it handles motion.  Much less hiccuping = possible indefinitely-extendable video clips.
- Problem is they only suppose CogXVideo which is the lowest-quality open source model atm.  If and when they make a LoRA for Wan video then expect infinite-length consistent videos
- Even so, they're already useful for making guidable motions, and e.g. converting a video-game-like crude left/right/up/down control to a realistic video.  Important overlooked tool imo
- I converted a meme video with their work:  https://www.youtube.com/watch?v=Gh-ImbICkeI  one-shot no-interference conversion from 2D crude animation to AI video
- keep in mind this is all just using the first frame + the general motion of the video.  Modify the first frame to any style you want (Ghibli?) and get the motion for free

#### Steerable Motion is especially doable with human poses:
- https://www.reddit.com/r/comfyui/comments/1jpcpfe/wan_21_fun_13b_control_16gb_vram_comfyui_native/
- https://www.reddit.com/r/StableDiffusion/comments/1jortj7/tropical_joker_my_wan21_vid2vid_test_on_a_local/
- AKA "ControlNet".   This does impose enough motion steering between extended clips too so a long dance will actually work!

#### In general, long clips beyond 5-10s are still difficult to stitch
- <a href="https://www.youtube.com/watch?v=V1vNV5YPyIk">Opassa Beach - my tech demo</a> of what we *can* do so far (in a one-shot blind generation)
- the above Go-with-the-Flow controls enable *almost*-consistent motion between clips but there are still hiccups and backsliding between clips as the AI guesses differently.
- Not sure if it's a CogXVideo limitation which would improve with Wan video or not.
- Still on the lookout for someone to get continuous infinite clips working
- You can fudge this by just generating several options for each next extended clip and picking the most consistent, then repeating.  This is more than good enough for most use cases.  It's just not *automatic* yet.

 
---

## MISC RESOURCES:  {#misc-resources}
https://www.reddit.com/r/comfyui/
https://www.youtube.com/@pixaroma/videos
https://www.youtube.com/@latentvision/videos
- I'm a reader more than a listener, but I hear these are good video guides

#### N8N  {#n8n}
- Starting to look into this node editor too.  Looks very useful, and integrated with Comfyui.  Will report back.
- https://www.reddit.com/r/n8n/comments/1jbvt0a/i_built_a_free_browser_extension_that_creates/


---

## FAQ  {#faq}

#### Q: Can comfyui workflows just be run in plain python without the interface?
- A: Yep.  https://github.com/Chaoses-Ib/ComfyScript  Translates any workflow to a python script format.  Vice-versa is trickier but likely doable with an LLM to convert it back to a JSON workflow (on the TODO list)
- https://github.com/atmaranto/ComfyUI-SaveAsScript  Too.  Haven't used either extensively yet though.

#### Q: Wait, can any arbitrary program be represented as a ComfyUI workflow?  Is this a complete programming language?
- A: Yeah pretty much, though we need to build the mapper still and the current state of comfyui node libraries are a bit of a mess.  Basically though any program or function can be easily wrapped up as a Comfy node at least and run like that, but we can drill down into them too and represent the whole program with nodes if you want to.  Takes conversion from iterative to functional programming styles though - but doable.  Should be possible for other languages too, but faces the same challenges as any language conversion.  All getting a lot easier as AIs improve though.  Expecting to be able to do this dynamically mostly reliably with e.g. Claude.

#### Q: Can we modularly/recursively call workflows from other workflows?
- A: Yes but the 3rd party implementation is janky, old and needs dev work.  
- https://github.com/vivax3794/ComfyUI-Sub-Nodes
- I am pretty-much expecting to need to rewrite this nodepack into an updated one.  But the proof of concept is there and works.  Use a caller node to modularly go through another workflow, which needs to have its inputs/outputs explicitly set.  My plan is to have an LLM auto-wrap each workflow and determine those inputs/outputs.

### Q: Can we call workflows from other computers or other instances of ComfyUI?
- A: Yes.... but it's also super janky and needs work.
- https://github.com/city96/ComfyUI_NetDist
- Limited success last I tried those nodes.  Would probably have to get Claude to spruce them up a bit before I can rely on them.
- https://github.com/ComfyPlus/ComfyPlus_Anywhere


### Q: Can we run multiple instances of ComfyUI on the same machine?
- A: Yes....? but it will be tricky.  Docker containers with different ports recommended, and then we deal with sharing the same gpu.  One model could in theory be shared between multiple instances though - each doing their own passthroughs.

### Q: Can we call LLMs from ComfyUI?  Locally?  Remotely?
- A: Yes to all.  But again - somewhat janky implementations...
- TODO will upload my workflows for this.  Many implementations are hit or miss and break frequently from updates.

### Q: ...Do I have to wait for ComfyUI to fully rebuild every time I edit a custom node's code?
- A:  No!  Janky hack ftw:  https://github.com/logtd/ComfyUI-HotReloadHack 
- Does the trick for most use cases.  You still need to refresh the page in browser.  I recommend lightweight dockerized environments with only the custom_nodes you actually need for a given workflow though for fast reloads.

### Q:  Can AI sort and score images for me?  This is generating more than I can even view.
- A:  Yes!  And this is probably where most development will go soon imo.  But image analysis is far weaker than generation imo for local models.  DeepSeek's Janus is the best I've used so far.  (Ping me to get me to go through the archived experiments for suggestions on nodes)
- TODO workflow links

### Q:  Can ComfyUI auto-load image/json/prompt/etc files from a folder automatically for batch processing?
- A:  Yes! BUT.  God, is even this annoying to do sometimes.
- TODO will upload my custom workflow just to do this reliably 

### Q:  Can it do if/else logic and XYZ basic-ass quality of life functionality?
- A:  Yes usually.... but you have to find the damn working nodes to do it.  We are still in stupidly early days it seems.  Also if/then branching works weirdly in ComfyUI as a declarative functional language than you might be used to
- TODO workflow links

### Q:  Can ComfyUI do 3d object generation?  AI speech?  Audio-video syncing?  XYZ?
- A: Yes, yes, yes, probably.  Just search the dang thing in the Comfy Manager and try out the nodes yourself.  Good luck bug hunting.
- 3D Vision: https://github.com/IsItDanOrAi/ComfyUI-Stereopsis
- 3D models: https://github.com/kijai/ComfyUI-Hunyuan3DWrapper
- ...more

### Q:  Why are you using ComfyUI when you could be using LangChain / OmniChain / n8n / Flowise  (LLM-oriented graph visual computing) ?
- A:  Mostly just buzzword bloat filling my brain.  I haven't tried them.  But also I want multimodal as a baseline guarantee, so I don't see why we should use anything but Comfy when it's already quite popular.
- But I do entirely endorse graph-based programming solutions as I thin they have a good chance of being what non-technical people "program" with in the coming years as this all becomes much more accessible
- https://github.com/numz/Comfyui-FlowChain
- https://github.com/mason276752/n8n-nodes-comfyui
- a lot of cross-compatibility.
- N8N might be a good idea as the host program, calling comfyui. Investigating this.

### Q:  This is too complicated, can I just type a prompt of what I want and have it just work?
- A:  Soon.   We're not at gpt4o levels just yet but some tools come close.
- https://github.com/1038lab/ComfyUI-OmniGen
- https://github.com/lks-ai/anynode


## TROUBLESHOOTING:  {#troubleshooting}
- oh god, this would be a nearly endless section if I actually tried to be authoritative here.  I will start with just the main techniques that you'll be repeating endlessly til someone automates these:

#### Q:  My ComfyUI has broken!  It says Missing Nodes.
- A:  This is normal for any workflow beyond the defaults.  Go to Manager => Install Missing Custom Nodes.  Click the top-left box to select all.  Click "Fix" and/or "Update".  Wait for each to process.  Click "Restart".  Wait.  Repeat if there are still any.  

#### Q:  It still says it's broken!  Missing Nodes or other error.
- A:  You're probably boned.  Try Uninstalling / Reinstalling the bad node in Install Missing Custom Nodes.  If that doesn't do it, then examine the ComfyUI main logs, copy-paste it into a good LLM, and follow directions - usually you need to install a missing python module which wasn't included.   Depending on your build style, that probably means activating the venv (god help you if you dont know what that is - you're in too deep.  Ask the LLM though if you're still feeling brave) and then running pip install on the missing package.  If you got to this point and it still doesn't work I hope you have a degree.  More likely:  just restart comfyui a couple times, then just give up on that particular workflow and try one that's easier to get going.  Many are simply out of date.

#### Q:  My ComfyUI has broken!  Different error, or doesnt even startup!
- A: Oh god.  You're on your own.  If you can see the log paste it into a good LLM and follow directions.  Very likely the culprit is something in ComfyUI/custom_nodes folder, so try emptying everything in there except "comfyui-manager".  Otherwise consider reinstalling your computer (jk just comfyui).

#### Q:  Okay I'm reinstalling...
- A:  WAIT.  Save the ComfyUI/input, output, user, custom_nodes and models folders first.   And try just renaming the old custom_nodes and making a fresh custom_nodes folder with just "comfyui-manager" in it first.

#### Q:  Fresh ComfyUI works but one of my custom nodes is breaking things.  The logs don't seem to point to the cause.
- Worst case scenario, try just binary-search:  cut and paste half the custom_nodes contents somewhere else, rerun and see if it boots okay, and repeatedly divide what's left til you've isolated the offending node and removed it.

#### Q:  Some other issue unrelated to all the above!
- I'm gonna try to keep a longer term focus on making a general system with the rough edges filed off, but I may be able to help with little things like this too in the interim, and will try and adjust this guide to catch common pain points.  Hit me up in the Signal chat group or similar as this evolves.



