# Filtered Nodes for: Inpainting workflow with mask input

Total Available Nodes: 1865
Batch Size: 4
Estimated Processing Time: 38.9 minutes

## Results

### a-person-mask-generator

**Description:**

Extension for Automatic1111 and ComfyUI to automatically create masks for Background/Hair/Body/Face/Clothes in Img2Img

- **Author:** djbielejeski
- **Repository:** [https://github.com/djbielejeski/a-person-mask-generator](https://github.com/djbielejeski/a-person-mask-generator)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly generates masks for Background/Hair/Body/Face/Clothes in Img2Img which is crucial for inpainting workflows.

### Metadata
**Author:** djbielejeski
**Repository:** [https://github.com/djbielejeski/a-person-mask-generator](https://github.com/djbielejeski/a-person-mask-generator)
**Install Type:** git-clone

---

### A8R8 ComfyUI Nodes

**Description:**

Nodes: Base64Image Input Node, Base64Image Output Node. [a/A8R8](https://github.com/ramyma/a8r8) supporting nodes to integrate with ComfyUI

- **Author:** ramyma
- **Repository:** [https://github.com/ramyma/A8R8_ComfyUI_nodes](https://github.com/ramyma/A8R8_ComfyUI_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While these nodes provide supporting functionality, they are more related to input/output handling rather than the core inpainting process with mask input.

### Metadata
**Author:** ramyma
**Repository:** [https://github.com/ramyma/A8R8_ComfyUI_nodes](https://github.com/ramyma/A8R8_ComfyUI_nodes)
**Install Type:** git-clone

---

### abg-comfyui

**Description:**

Nodes: Remove Image Background (abg). A Anime Background Remover node for comfyui, based on this hf space, works same as AGB extention in automatic1111.

- **Author:** kwaroran
- **Repository:** [https://github.com/kwaroran/abg-comfyui](https://github.com/kwaroran/abg-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node can be useful in removing image backgrounds which might be necessary for some inpainting workflows but is not directly relevant to using a mask as input.

### Metadata
**Author:** kwaroran
**Repository:** [https://github.com/kwaroran/abg-comfyui](https://github.com/kwaroran/abg-comfyui)
**Install Type:** git-clone

---

### add_text_2_img

**Description:**

Support adding custom text to the generated images.

- **Author:** fanfanfan
- **Repository:** [https://github.com/yuan199696/add_text_2_img](https://github.com/yuan199696/add_text_2_img)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node supports adding custom text to generated images, which can be useful for labeling or annotating inpainted results.

### Metadata
**Author:** fanfanfan
**Repository:** [https://github.com/yuan199696/add_text_2_img](https://github.com/yuan199696/add_text_2_img)
**Install Type:** git-clone

---

### AegisFlow Utility Nodes

**Description:**

These nodes will be placed in comfyui/custom_nodes/aegisflow and contains the image passer (accepts an image as either wired or wirelessly, input and passes it through. Latent passer does the same for latents, and the Preprocessor chooser allows a passthrough image and 10 controlnets to be passed in AegisFlow Shima. The inputs on the Preprocessor  chooser should not be renamed if you intend to accept image inputs wirelessly through UE nodes. It can be done, but the send node input regex for each controlnet preprocessor column must also be changed.

- **Author:** Aegis72
- **Repository:** [https://github.com/aegis72/aegisflow_utility_nodes](https://github.com/aegis72/aegisflow_utility_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** These nodes provide utility functions for passing images and latents in AegisFlow Shima, which could be useful as supporting nodes in an inpainting workflow with a mask input.

### Metadata
**Author:** Aegis72
**Repository:** [https://github.com/aegis72/aegisflow_utility_nodes](https://github.com/aegis72/aegisflow_utility_nodes)
**Install Type:** git-clone

---

### AIRedoon

**Description:**

NODES:AIRedoon Qwen Model Loader, AIRedoon Translator, AIRedoon Image Caption, AIRedoon LoRA Stack, AIRedoon Image RGBA2RGB, AIRedoon Preview Text, AIRedoon Save Text, ...
RedoonAi Tool Kit

- **Author:** purpen
- **Repository:** [https://github.com/purpen/ComfyUI-AIRedoon](https://github.com/purpen/ComfyUI-AIRedoon)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node contains a variety of tools that can be used in an inpainting workflow, including model loaders, translators, and image processing nodes.

### Metadata
**Author:** purpen
**Repository:** [https://github.com/purpen/ComfyUI-AIRedoon](https://github.com/purpen/ComfyUI-AIRedoon)
**Install Type:** git-clone

---

### Amazon Bedrock nodes for ComfyUI

**Description:**

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies. This repo is the ComfyUI nodes for Bedrock service. You could invoke the foundation model in your ComfyUI pipeline.

- **Author:** yytdfc
- **Repository:** [https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock](https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Amazon Bedrock nodes can invoke foundation models that could potentially aid in inpainting tasks with mask input.

### Metadata
**Author:** yytdfc
**Repository:** [https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock](https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock)
**Install Type:** git-clone

---

### AnimateDiff

**Description:**

AnimateDiff integration for ComfyUI, adapts from sd-webui-animatediff.
[w/You only need to download one of [a/mm_sd_v14.ckpt](https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v14.ckpt) | [a/mm_sd_v15.ckpt](https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15.ckpt). Put the model weights under %%ComfyUI/custom_nodes/comfyui-animatediff/models%%. DO NOT change model filename.]

- **Author:** ArtVentureX
- **Repository:** [https://github.com/ArtVentureX/comfyui-animatediff](https://github.com/ArtVentureX/comfyui-animatediff)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** AnimateDiff is a direct integration for ComfyUI and adapts from sd-webui-animatediff which can be used for inpainting tasks with mask input.

### Metadata
**Author:** ArtVentureX
**Repository:** [https://github.com/ArtVentureX/comfyui-animatediff](https://github.com/ArtVentureX/comfyui-animatediff)
**Install Type:** git-clone

---

### AnimateDiff Evolved

**Description:**

A forked repository that actively maintains [a/AnimateDiff](https://github.com/ArtVentureX/comfyui-animatediff), created by ArtVentureX.

Improved AnimateDiff integration for ComfyUI, adapts from sd-webui-animatediff.
[w/Download one or more motion models from [a/Original Models](https://huggingface.co/guoyww/animatediff/tree/main) | [a/Finetuned Models](https://huggingface.co/manshoety/AD_Stabilized_Motion/tree/main). See README for additional model links and usage. Put the model weights under %%ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/models%%. You are free to rename the models, but keeping original names will ease use when sharing your workflow.]

- **Author:** Kosinkadink
- **Repository:** [https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** AnimateDiff Evolved is an improved version of AnimateDiff that actively maintains the original codebase and includes additional models specifically designed for inpainting tasks with mask input.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
**Install Type:** git-clone

---

### Anime Character Segmentation node for comfyui

**Description:**

A Anime Character Segmentation node for comfyui, based on [this hf space](https://huggingface.co/spaces/skytnt/anime-remove-background).

- **Author:** LyazS
- **Repository:** [https://github.com/LyazS/comfyui-anime-seg](https://github.com/LyazS/comfyui-anime-seg)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for anime character segmentation, which can be used as a pre-processing step in an inpainting workflow with mask input.

### Metadata
**Author:** LyazS
**Repository:** [https://github.com/LyazS/comfyui-anime-seg](https://github.com/LyazS/comfyui-anime-seg)
**Install Type:** git-clone

---

### antrobots ComfyUI Nodepack

**Description:**

A small node pack containing various things I felt like ought to be in base comfy-UI. Currently includes Some image handling nodes to help with inpainting, a version of KSampler (advanced) that allows for denoise, and a node that can swap it's inputs. Remember to make an issue if you experience any bugs or errors!

- **Author:** antrobot
- **Repository:** [https://github.com/antrobot1234/antrobots-comfyUI-nodepack](https://github.com/antrobot1234/antrobots-comfyUI-nodepack)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node pack includes various image handling nodes that can be useful for inpainting, making it moderately to very useful for the specified workflow goal.

### Metadata
**Author:** antrobot
**Repository:** [https://github.com/antrobot1234/antrobots-comfyUI-nodepack](https://github.com/antrobot1234/antrobots-comfyUI-nodepack)
**Install Type:** git-clone

---

### APISR IN COMFYUI

**Description:**

Unofficial implementation of APISR for ComfyUI, both image and video

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** APISR can be used for image and video inpainting with mask input, making it very useful for this workflow goal.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR](https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR)
**Install Type:** git-clone

---

### Arc2Face ComfyUI Node Library

**Description:**

This ComfyUI node library builds upon the work done to train the [a/Arc2Face](https://github.com/foivospar/Arc2Face) model by foivospar. It provides a set of nodes for ComfyUI that allow users to extract face embeddings, generate images based on these embeddings, and perform image-to-image transformations.

- **Author:** caleboleary
- **Repository:** [https://github.com/caleboleary/ComfyUI-Arc2Face](https://github.com/caleboleary/ComfyUI-Arc2Face)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node library provides a set of nodes that can be used for various tasks including image-to-image transformations which could be useful for an inpainting workflow.

### Metadata
**Author:** caleboleary
**Repository:** [https://github.com/caleboleary/ComfyUI-Arc2Face](https://github.com/caleboleary/ComfyUI-Arc2Face)
**Install Type:** git-clone

---

### asyncdiff_comfyui

**Description:**

AsyncDiff node for ComfyUI

- **Author:** SlackinJack
- **Repository:** [https://github.com/SlackinJack/asyncdiff_comfyui](https://github.com/SlackinJack/asyncdiff_comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This AsyncDiff node can be useful in handling differences between images and supporting the inpainting workflow.

### Metadata
**Author:** SlackinJack
**Repository:** [https://github.com/SlackinJack/asyncdiff_comfyui](https://github.com/SlackinJack/asyncdiff_comfyui)
**Install Type:** git-clone

---

### Auto-MBW

**Description:**

Auto-MBW for ComfyUI loosely based on sdweb-auto-MBW. Nodes: auto merge block weighted

- **Author:** szhublox
- **Repository:** [https://github.com/szhublox/ambw_comfyui](https://github.com/szhublox/ambw_comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can merge block weighted images which could be useful for inpainting tasks that involve merging multiple image blocks.

### Metadata
**Author:** szhublox
**Repository:** [https://github.com/szhublox/ambw_comfyui](https://github.com/szhublox/ambw_comfyui)
**Install Type:** git-clone

---

### Batch Rembg for ComfyUI

**Description:**

Remove background of plural images.

- **Author:** Mamaaaamooooo
- **Repository:** [https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes](https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for the specified workflow goal as it can remove backgrounds of plural images.

### Metadata
**Author:** Mamaaaamooooo
**Repository:** [https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes](https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes)
**Install Type:** git-clone

---

### Bjornulf_custom_nodes

**Description:**

Nodes: Ollama, Green Screen to Transparency, Save image for Bjornulf LobeChat, Text with random Seed, Random line from input, Combine images (Background+Overlay alpha), Image to grayscale (black & white), Remove image Transparency (alpha), Resize Image, ...

- **Author:** justUmen
- **Repository:** [https://github.com/justUmen/Bjornulf_custom_nodes](https://github.com/justUmen/Bjornulf_custom_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node collection includes several useful nodes such as Green Screen to Transparency, Remove image Transparency (alpha), and Resize Image that can support the inpainting workflow with mask input.

### Metadata
**Author:** justUmen
**Repository:** [https://github.com/justUmen/Bjornulf_custom_nodes](https://github.com/justUmen/Bjornulf_custom_nodes)
**Install Type:** git-clone

---

### Bobs_Latent_Optimizer

**Description:**

This custom node for ComfyUI is designed to optimize latent generation for use with FLUX, SDXL and SD3. It provides flexible control over aspect ratios, megapixel sizes, and upscale factors, allowing users to dynamically create latents that fit specific tiling and resolution needs.

- **Author:** bobsblazed
- **Repository:** [https://github.com/BobsBlazed/Bobs_Latent_Optimizer](https://github.com/BobsBlazed/Bobs_Latent_Optimizer)
- **Install Type:** copy


### Applicability

**Score:** 90/100

**Reason:** This custom optimizer provides flexible control over latent generation and can help create latents that fit specific tiling and resolution needs for the inpainting workflow.

### Metadata
**Author:** bobsblazed
**Repository:** [https://github.com/BobsBlazed/Bobs_Latent_Optimizer](https://github.com/BobsBlazed/Bobs_Latent_Optimizer)
**Install Type:** copy

---

### braintacles-nodes

**Description:**

Nodes: CLIPTextEncodeSDXL-Multi-IO, CLIPTextEncodeSDXL-Pipe, Empty Latent Image from Aspect-Ratio, Random Find and Replace.

- **Author:** braintacles
- **Repository:** [https://github.com/braintacles/braintacles-comfyui-nodes](https://github.com/braintacles/braintacles-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Some of these nodes (e.g., Empty Latent Image from Aspect-Ratio) might be marginally useful in an inpainting context, but their relevance is limited compared to other options.

### Metadata
**Author:** braintacles
**Repository:** [https://github.com/braintacles/braintacles-comfyui-nodes](https://github.com/braintacles/braintacles-comfyui-nodes)
**Install Type:** git-clone

---

### BrushNet

**Description:**

These are custom nodes for ComfyUI native implementation of [a/BrushNet](https://arxiv.org/abs/2403.06976) (inpaint), PowerPaint (inpaint, object removal) and HiDiffusion (higher resolution for SD15 and SDXL)

- **Author:** nullquant
- **Repository:** [https://github.com/nullquant/ComfyUI-BrushNet](https://github.com/nullquant/ComfyUI-BrushNet)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** BrushNet provides a native implementation of an inpainting model, making it very useful for this specific workflow goal.

### Metadata
**Author:** nullquant
**Repository:** [https://github.com/nullquant/ComfyUI-BrushNet](https://github.com/nullquant/ComfyUI-BrushNet)
**Install Type:** git-clone

---

### bsz-cui-extras

**Description:**

This contains all-in-one 'principled' nodes for T2I, I2I, refining, and scaling. Additionally it has many tools for directly manipulating the color of latents, high res fix math, and scripted image post-processing.

- **Author:** Beinsezii
- **Repository:** [https://github.com/Beinsezii/bsz-cui-extras](https://github.com/Beinsezii/bsz-cui-extras)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** bsz-cui-extras contains nodes specifically designed for image manipulation and post-processing, including tools that can be used in an inpainting workflow with mask input.

### Metadata
**Author:** Beinsezii
**Repository:** [https://github.com/Beinsezii/bsz-cui-extras](https://github.com/Beinsezii/bsz-cui-extras)
**Install Type:** git-clone

---

### Canvas Tab

**Description:**

This extension provides a full page image editor with mask support. There are two nodes, one to receive images from the editor and one to send images to the editor.

- **Author:** Lerc
- **Repository:** [https://github.com/Lerc/canvas_tab](https://github.com/Lerc/canvas_tab)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a full-page image editor with mask support, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** Lerc
**Repository:** [https://github.com/Lerc/canvas_tab](https://github.com/Lerc/canvas_tab)
**Install Type:** git-clone

---

### Chaosaiart-Nodes

**Description:**

LowVRAM Animation : txt2video - img2video - video2video , Frame by Frame, compatible with LowVRAM GPUs
Included : Prompt Switch, Checkpoint Switch, Cache, Number Count by Frame, Ksampler txt2img & img2img ...

- **Author:** chaosaiart
- **Repository:** [https://github.com/chaosaiart/Chaosaiart-Nodes](https://github.com/chaosaiart/Chaosaiart-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides various animation features that can be useful as supporting nodes in an inpainting workflow with mask input.

### Metadata
**Author:** chaosaiart
**Repository:** [https://github.com/chaosaiart/Chaosaiart-Nodes](https://github.com/chaosaiart/Chaosaiart-Nodes)
**Install Type:** git-clone

---

### Chatbox Overlay node for ComfyUI

**Description:**

Nodes: Chatbox Overlay. Custom node for ComfyUI to add a text box over a processed image before save node.

- **Author:** Smuzzies
- **Repository:** [https://github.com/Smuzzies/comfyui_chatbox_overlay](https://github.com/Smuzzies/comfyui_chatbox_overlay)
- **Install Type:** copy


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant as it allows for text overlays on processed images, but does not directly contribute to the inpainting process.

### Metadata
**Author:** Smuzzies
**Repository:** [https://github.com/Smuzzies/comfyui_chatbox_overlay](https://github.com/Smuzzies/comfyui_chatbox_overlay)
**Install Type:** copy

---

### chris-comfyui-nodes

**Description:**

This repository contains a custom node for ComfyUI that pads an image to be square, filling the new pixels black.

- **Author:** chrissy0
- **Repository:** [https://github.com/chrissy0/chris-comfyui-nodes](https://github.com/chrissy0/chris-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node can pad an image to be square, filling new pixels black, which could be useful for preparing the input image for inpainting.

### Metadata
**Author:** chrissy0
**Repository:** [https://github.com/chrissy0/chris-comfyui-nodes](https://github.com/chrissy0/chris-comfyui-nodes)
**Install Type:** git-clone

---

### Civitai Comfy Nodes

**Description:**

Tired of manually downloading and moving models, LoRAs, and more to the right places?
Sick of scouring Civitai for that one mystical LoRA someone was using to make that cool image?
Want to be share a fully reproducable workflow?

- **Author:** civitai
- **Repository:** [https://github.com/civitai/civitai_comfy_nodes](https://github.com/civitai/civitai_comfy_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a collection of custom nodes that can help with various tasks in the workflow, including downloading and managing models, making it essential for this workflow.

### Metadata
**Author:** civitai
**Repository:** [https://github.com/civitai/civitai_comfy_nodes](https://github.com/civitai/civitai_comfy_nodes)
**Install Type:** git-clone

---

### Clh Tool for ComfyUI

**Description:**

Some mathematical calculation nodes，freedom And omnipotent, string calculation nodes, can customize the number of parameters and calculation formulas（expression）. The calculation content can also be displayed in places such as the label title of Comfy Node，String to Image Title Label

- **Author:** clhui
- **Repository:** [https://github.com/clhui/ComfyUi-clh-Tool](https://github.com/clhui/ComfyUi-clh-Tool)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for the Inpainting workflow with mask input as it provides mathematical calculation nodes that can be customized and used in various parts of the workflow.

### Metadata
**Author:** clhui
**Repository:** [https://github.com/clhui/ComfyUi-clh-Tool](https://github.com/clhui/ComfyUi-clh-Tool)
**Install Type:** git-clone

---

### CLIP with BREAK syntax

**Description:**

Clip text encoder with BREAK formatting like A1111 (uses conditioning concat)

- **Author:** dfl
- **Repository:** [https://github.com/dfl/comfyui-clip-with-break](https://github.com/dfl/comfyui-clip-with-break)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for the Inpainting workflow with mask input as it provides a Clip text encoder that can be used to process and format text inputs, potentially aiding in the creation of masks or other workflow tasks.

### Metadata
**Author:** dfl
**Repository:** [https://github.com/dfl/comfyui-clip-with-break](https://github.com/dfl/comfyui-clip-with-break)
**Install Type:** git-clone

---

### CLIPSeg

**Description:**

The CLIPSeg node generates a binary mask for a given input image and text prompt.
NOTE:This custom node is a forked custom node with hotfixes applied from the [a/original repository](https://github.com/biegert/ComfyUI-CLIPSeg), which is no longer maintained.

- **Author:** time-river
- **Repository:** [https://github.com/time-river/ComfyUI-CLIPSeg](https://github.com/time-river/ComfyUI-CLIPSeg)
- **Install Type:** copy


### Applicability

**Score:** 100/100

**Reason:** This node directly generates a binary mask from an image and text prompt, which is essential for inpainting workflows.

### Metadata
**Author:** time-river
**Repository:** [https://github.com/time-river/ComfyUI-CLIPSeg](https://github.com/time-river/ComfyUI-CLIPSeg)
**Install Type:** copy

---

### Comfy Controller

**Description:**

Quickly and easily build a GUI on top of your workflow. Gather just the nodes that you want to see, with no spaghetti, onto controller panels, leaving your workflow untouched in the background.

- **Author:** chrisgoringe
- **Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for organizing and customizing the GUI of the inpainting workflow with mask input.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
**Install Type:** git-clone

---

### Comfy UI Online Loaders

**Description:**

Nodes: Submit Image (Parameters), Submit Image. A collection of loaders that use a shared common online data source rather than relying on the files to be present locally.

- **Author:** yolanother
- **Repository:** [https://github.com/yolanother/DTAIComfyLoaders](https://github.com/yolanother/DTAIComfyLoaders)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it allows loading images from an online data source, which may be necessary if the images are not present locally.

### Metadata
**Author:** yolanother
**Repository:** [https://github.com/yolanother/DTAIComfyLoaders](https://github.com/yolanother/DTAIComfyLoaders)
**Install Type:** git-clone

---

### comfy-easy-grids

**Description:**

A set of custom nodes for creating image grids, sequences, and batches in ComfyUI.

- **Author:** shockz0rz
- **Repository:** [https://github.com/shockz0rz/comfy-easy-grids](https://github.com/shockz0rz/comfy-easy-grids)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful in supporting the inpainting workflow as it allows creating image grids, sequences, and batches which are essential for processing multiple mask inputs.

### Metadata
**Author:** shockz0rz
**Repository:** [https://github.com/shockz0rz/comfy-easy-grids](https://github.com/shockz0rz/comfy-easy-grids)
**Install Type:** git-clone

---

### Comfy-Photoshop-SD

**Description:**

Nodes: load Image with metadata, get config data, load image from base64 string, Load Loras From Prompt, Generate Latent Noise, Combine Two Latents Into Batch, General Purpose Controlnet Unit, ControlNet Script, Content Mask Latent, Auto-Photoshop-SD Seed, Expand and Blur the Mask

- **Author:** AbdullahAlfaraj
- **Repository:** [https://github.com/AbdullahAlfaraj/Comfy-Photoshop-SD](https://github.com/AbdullahAlfaraj/Comfy-Photoshop-SD)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains multiple nodes specifically designed for image processing tasks, including loading images, generating latents, and combining them, which are essential for the inpainting workflow with mask input.

### Metadata
**Author:** AbdullahAlfaraj
**Repository:** [https://github.com/AbdullahAlfaraj/Comfy-Photoshop-SD](https://github.com/AbdullahAlfaraj/Comfy-Photoshop-SD)
**Install Type:** git-clone

---

### Comfy-Topaz

**Description:**

Comfy-Topaz is a custom node for ComfyUI, which integrates with Topaz Photo AI to enhance (upscale, sharpen, denoise, etc.) images, allowing this traditionally asynchronous step to become a part of ComfyUI workflows.
NOTE:Licensed installation of Topaz Photo AI

- **Author:** choey
- **Repository:** [https://github.com/choey/Comfy-Topaz](https://github.com/choey/Comfy-Topaz)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node can upscale and enhance images using Topaz Photo AI, which is directly useful for improving image quality in an inpainting workflow.

### Metadata
**Author:** choey
**Repository:** [https://github.com/choey/Comfy-Topaz](https://github.com/choey/Comfy-Topaz)
**Install Type:** git-clone

---

### comfy_clip_blip_node

**Description:**

CLIPTextEncodeBLIP: This custom node provides a CLIP Encoder that is capable of receiving images as input.

- **Author:** paulo-coronado
- **Repository:** [https://github.com/paulo-coronado/comfy_clip_blip_node](https://github.com/paulo-coronado/comfy_clip_blip_node)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node can encode images using CLIP and might be useful as a supporting node for tasks that require text-encoding of images in the inpainting workflow.

### Metadata
**Author:** paulo-coronado
**Repository:** [https://github.com/paulo-coronado/comfy_clip_blip_node](https://github.com/paulo-coronado/comfy_clip_blip_node)
**Install Type:** git-clone

---

### Comfy_KepMatteAnything

**Description:**

This extension provides a custom node that allows the use of [a/Matte Anything](https://github.com/hustvl/Matte-Anything) in ComfyUI.

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/Comfy_KepMatteAnything](https://github.com/M1kep/Comfy_KepMatteAnything)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for the inpainting workflow as it allows using Matte Anything, a tool specifically designed for image matting and inpainting.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/Comfy_KepMatteAnything](https://github.com/M1kep/Comfy_KepMatteAnything)
**Install Type:** git-clone

---

### comfy_PoP

**Description:**

A collection of custom nodes for ComfyUI. Includes a quick canny edge detection node with unconventional settings, simple LoRA stack nodes for workflow efficiency, and a customizable aspect ratio node.

- **Author:** picturesonpictures
- **Repository:** [https://github.com/picturesonpictures/comfy_PoP](https://github.com/picturesonpictures/comfy_PoP)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node offers a quick canny edge detection node and customizable aspect ratio node which could be useful in the inpainting workflow.

### Metadata
**Author:** picturesonpictures
**Repository:** [https://github.com/picturesonpictures/comfy_PoP](https://github.com/picturesonpictures/comfy_PoP)
**Install Type:** git-clone

---

### ComfyBreakAnim

**Description:**

Nodes:BreakFrames, GetKeyFrames, MakeGrid.

- **Author:** LonicaMewinsky
- **Repository:** [https://github.com/LonicaMewinsky/ComfyUI-MakeFrame](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides functionality for breaking and making frames but lacks direct relevance to inpainting with mask input.

### Metadata
**Author:** LonicaMewinsky
**Repository:** [https://github.com/LonicaMewinsky/ComfyUI-MakeFrame](https://github.com/LonicaMewinsky/ComfyUI-MakeFrame)
**Install Type:** git-clone

---

### ComfyI2I

**Description:**

A set of custom nodes to perform image 2 image functions in ComfyUI.

- **Author:** ManglerFTW
- **Repository:** [https://github.com/ManglerFTW/ComfyI2I](https://github.com/ManglerFTW/ComfyI2I)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node contains custom nodes for image-to-image functions which can be useful in an inpainting workflow with mask input.

### Metadata
**Author:** ManglerFTW
**Repository:** [https://github.com/ManglerFTW/ComfyI2I](https://github.com/ManglerFTW/ComfyI2I)
**Install Type:** git-clone

---

### ComfyKit Custom Nodes

**Description:**

Nodes:LoraWithMetadata, TypecasterImage.

- **Author:** bobmagicii
- **Repository:** [https://github.com/bobmagicii/comfykit-custom-nodes](https://github.com/bobmagicii/comfykit-custom-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides some custom nodes but they do not seem to be directly related to the inpainting workflow with mask input.

### Metadata
**Author:** bobmagicii
**Repository:** [https://github.com/bobmagicii/comfykit-custom-nodes](https://github.com/bobmagicii/comfykit-custom-nodes)
**Install Type:** git-clone

---

### ComfyMath

**Description:**

Provides Math Nodes for ComfyUI. Boolean Logic, Integer Arithmetic, Floating Point Arithmetic and Functions, Vec2, Vec3, and Vec4 Arithmetic and Functions

- **Author:** evanspearman
- **Repository:** [https://github.com/evanspearman/ComfyMath](https://github.com/evanspearman/ComfyMath)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyMath offers arithmetic and logic operations that could be useful for processing mask inputs in the inpainting workflow.

### Metadata
**Author:** evanspearman
**Repository:** [https://github.com/evanspearman/ComfyMath](https://github.com/evanspearman/ComfyMath)
**Install Type:** git-clone

---

### ComfyQR

**Description:**

QR generation within ComfyUI. Contains nodes suitable for workflows from generating basic QR images to techniques with advanced QR masking.

- **Author:** coreyryanhanson
- **Repository:** [https://github.com/coreyryanhanson/ComfyQR](https://github.com/coreyryanhanson/ComfyQR)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** ComfyQR provides QR generation nodes but lacks functionality directly related to inpainting workflows with mask inputs.

### Metadata
**Author:** coreyryanhanson
**Repository:** [https://github.com/coreyryanhanson/ComfyQR](https://github.com/coreyryanhanson/ComfyQR)
**Install Type:** git-clone

---

### ComfyS3

**Description:**

ComfyS3 seamlessly integrates with [a/Amazon S3](https://aws.amazon.com/en/s3/) in ComfyUI. This open-source project provides custom nodes for effortless loading and saving of images, videos, and checkpoint models directly from S3 buckets within the ComfyUI graph interface.

- **Author:** TemryL
- **Repository:** [https://github.com/TemryL/ComfyS3](https://github.com/TemryL/ComfyS3)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyS3 seamlessly integrates with Amazon S3 for effortless loading and saving of images, videos, and checkpoint models, which is essential for an inpainting workflow with mask input.

### Metadata
**Author:** TemryL
**Repository:** [https://github.com/TemryL/ComfyS3](https://github.com/TemryL/ComfyS3)
**Install Type:** git-clone

---

### ComfyUI - Mask Bounding Box

**Description:**

The ComfyUI Mask Bounding Box Plugin provides functionalities for selecting a specific size mask from an image. Can be combined with ClipSEG to replace any aspect of an SDXL image with an SD1.5 output.

- **Author:** mikkel
- **Repository:** [https://github.com/mikkel/comfyui-mask-boundingbox](https://github.com/mikkel/comfyui-mask-boundingbox)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly provides a mask bounding box selection feature that is essential for inpainting with a mask input.

### Metadata
**Author:** mikkel
**Repository:** [https://github.com/mikkel/comfyui-mask-boundingbox](https://github.com/mikkel/comfyui-mask-boundingbox)
**Install Type:** git-clone

---

### ComfyUI - Native DynamiCrafter

**Description:**

DynamiCrafter that works natively with ComfyUI's nodes, optimizations, ControlNet, and more.

- **Author:** ExponentialML
- **Repository:** [https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Native DynamiCrafter node can be used to optimize and fine-tune the inpainting process, making it an essential component of this workflow.

### Metadata
**Author:** ExponentialML
**Repository:** [https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter)
**Install Type:** git-clone

---

### ComfyUI - P2LDGAN Node

**Description:**

Nodes: P2LDGAN. This integrates P2LDGAN into ComfyUI. P2LDGAN extracts lineart from input images.
[w/To use this extension, you need to download the [a/p2ldgan model](https://drive.google.com/file/d/1To4V_Btc3QhCLBWZ0PdSNgC1cbm3isHP) and save it in the %%ComfyUI/custom_nodes/comfyui-p2ldgan/checkpoints%% directory.]

- **Author:** jamesWalker55
- **Repository:** [https://github.com/jamesWalker55/comfyui-p2ldgan](https://github.com/jamesWalker55/comfyui-p2ldgan)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** P2LDGAN Node can be used for extracting lineart from images, but its relevance to inpainting with a mask input is limited and indirect.

### Metadata
**Author:** jamesWalker55
**Repository:** [https://github.com/jamesWalker55/comfyui-p2ldgan](https://github.com/jamesWalker55/comfyui-p2ldgan)
**Install Type:** git-clone

---

### ComfyUI AnyNode: Any Node you ask for

**Description:**

Nodes: AnyNode. Nodes that can be anything you ask. Auto-Generate functional nodes using LLMs. Create impossible workflows. API Compatibility: (OpenAI, LocalLLMs, Gemini).

- **Author:** lks-ai
- **Repository:** [https://github.com/lks-ai/anynode](https://github.com/lks-ai/anynode)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can auto-generate functional nodes using LLMs, making it highly relevant and useful for creating impossible workflows like inpainting with mask input.

### Metadata
**Author:** lks-ai
**Repository:** [https://github.com/lks-ai/anynode](https://github.com/lks-ai/anynode)
**Install Type:** git-clone

---

### ComfyUI BEN - Background Erase Network

**Description:**

Remove backgrounds from images with [a/BEN](https://huggingface.co/PramaLLC/BEN) in ComfyUI

- **Author:** Doctor Diffusion
- **Repository:** [https://github.com/DoctorDiffusion/ComfyUI-BEN](https://github.com/DoctorDiffusion/ComfyUI-BEN)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to the inpainting workflow with mask input as it provides a background erasure network.

### Metadata
**Author:** Doctor Diffusion
**Repository:** [https://github.com/DoctorDiffusion/ComfyUI-BEN](https://github.com/DoctorDiffusion/ComfyUI-BEN)
**Install Type:** git-clone

---

### ComfyUI Bringing Old Photos Back to Life

**Description:**

Enhance old or low-quality images in ComfyUI. Optional features include automatic scratch removal and face enhancement. Based on Microsoft's Bringing-Old-Photos-Back-to-Life. Requires installing models, so see instructions here: https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life.

- **Author:** cdb-boop
- **Repository:** [https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life](https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to the inpainting workflow with mask input as it enhances old or low-quality images which can be used in conjunction with a mask for inpainting.

### Metadata
**Author:** cdb-boop
**Repository:** [https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life](https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life)
**Install Type:** git-clone

---

### ComfyUI Checkpoint Automatic Config

**Description:**

This node was designed to help with checkpoint configuration. Fee free to add new checkpoint configurations!

- **Author:** DarKDinDoN
- **Repository:** [https://github.com/mech-tools/comfyui-checkpoint-automatic-config](https://github.com/mech-tools/comfyui-checkpoint-automatic-config)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential for the inpainting workflow with mask input as it helps configure checkpoints which are crucial for training and inference processes.

### Metadata
**Author:** DarKDinDoN
**Repository:** [https://github.com/mech-tools/comfyui-checkpoint-automatic-config](https://github.com/mech-tools/comfyui-checkpoint-automatic-config)
**Install Type:** git-clone

---

### ComfyUI Checkpoint Loader Config

**Description:**

Provides a custom node to load config for sampler nodes from a yaml file.

- **Author:** Cyberschorsch
- **Repository:** [https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader](https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for the inpainting workflow with mask input as it provides a custom config loader from a yaml file, supporting checkpoint configuration.

### Metadata
**Author:** Cyberschorsch
**Repository:** [https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader](https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader)
**Install Type:** git-clone

---

### ComfyUI Coherent Video Sampler Node

**Description:**

A custom node for ComfyUI that enables coherent video generation while maintaining efficient memory usage, specifically optimized for heavy models like Flux.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler](https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node enables coherent video generation which can be useful in inpainting workflows that require efficient memory usage.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler](https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler)
**Install Type:** git-clone

---

### ComfyUI CustomScheduler

**Description:**

Simple node for setting the sigma values directly. Note, for a full denoise the last sigma should be zero.

- **Author:** BlakeOne
- **Repository:** [https://github.com/BlakeOne/ComfyUI-CustomScheduler](https://github.com/BlakeOne/ComfyUI-CustomScheduler)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node allows for direct control over sigma values in the inpainting workflow, which can significantly impact the quality of the output.

### Metadata
**Author:** BlakeOne
**Repository:** [https://github.com/BlakeOne/ComfyUI-CustomScheduler](https://github.com/BlakeOne/ComfyUI-CustomScheduler)
**Install Type:** git-clone

---

### ComfyUI DataBeast

**Description:**

This extension provides convenience nodes for batch processing.

- **Author:** hanoixan
- **Repository:** [https://github.com/hanoixan/ComfyUI-DataBeast](https://github.com/hanoixan/ComfyUI-DataBeast)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node offers batch processing convenience nodes, its direct relevance to inpainting with a mask input is limited.

### Metadata
**Author:** hanoixan
**Repository:** [https://github.com/hanoixan/ComfyUI-DataBeast](https://github.com/hanoixan/ComfyUI-DataBeast)
**Install Type:** git-clone

---

### ComfyUI Deepface

**Description:**

ComfyUI nodes wrapping the [a/deepface](https://github.com/serengil/deepface) library.

- **Author:** jordoh
- **Repository:** [https://github.com/jordoh/ComfyUI-Deepface](https://github.com/jordoh/ComfyUI-Deepface)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it provides face recognition functionality that can be used in conjunction with mask inputs.

### Metadata
**Author:** jordoh
**Repository:** [https://github.com/jordoh/ComfyUI-Deepface](https://github.com/jordoh/ComfyUI-Deepface)
**Install Type:** git-clone

---

### ComfyUI DenseDiffusion

**Description:**

[a/DenseDiffusion](https://github.com/naver-ai/DenseDiffusion) custom node for ComfyUI.

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI_densediffusion](https://github.com/huchenlei/ComfyUI_densediffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it implements a custom DenseDiffusion model that can be used for image restoration and inpainting tasks.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI_densediffusion](https://github.com/huchenlei/ComfyUI_densediffusion)
**Install Type:** git-clone

---

### ComfyUI Dreamtalk

**Description:**

Unofficial implementation of [a/dreamtalk](https://github.com/ali-vilab/dreamtalk) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_Dreamtalk](https://github.com/hay86/ComfyUI_Dreamtalk)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used for image manipulation and could potentially support inpainting tasks.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_Dreamtalk](https://github.com/hay86/ComfyUI_Dreamtalk)
**Install Type:** git-clone

---

### ComfyUI Easy Civitai (XTNodes)

**Description:**

Load your model with image previews, or directly download and import Civitai models via URL. This custom ComfyUI node supports Checkpoint, LoRA, and LoRA Stack models, offering features like bypass options.

- **Author:** X-T-E-R
- **Repository:** [https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes](https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node allows loading and importing models from Civitai, which can be useful for inpainting tasks if the model is suitable.

### Metadata
**Author:** X-T-E-R
**Repository:** [https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes](https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes)
**Install Type:** git-clone

---

### ComfyUI Easy Use

**Description:**

To enhance the usability of ComfyUI, optimizations and integrations have been implemented for several commonly used nodes.

- **Author:** yolain
- **Repository:** [https://github.com/yolain/ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node enhances usability of ComfyUI and can make the inpainting workflow more efficient by optimizing commonly used nodes.

### Metadata
**Author:** yolain
**Repository:** [https://github.com/yolain/ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
**Install Type:** git-clone

---

### ComfyUI Essentials

**Description:**

Essential nodes that are weirdly missing from ComfyUI core. With few exceptions they are new features and not commodities. I hope this will be just a temporary repository until the nodes get included into ComfyUI.

- **Author:** cubiq
- **Repository:** [https://github.com/cubiq/ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI Essentials includes essential nodes that might be missing from the core, potentially including functionality relevant to an inpainting workflow with mask input.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
**Install Type:** git-clone

---

### ComfyUI fabric

**Description:**

ComfyUI nodes based on the paper [a/FABRIC: Personalizing Diffusion Models with Iterative Feedback](https://arxiv.org/abs/2307.10159) (Feedback via Attention-Based Reference Image Conditioning)

- **Author:** ssitu
- **Repository:** [https://github.com/ssitu/ComfyUI_fabric](https://github.com/ssitu/ComfyUI_fabric)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI fabric is highly relevant as it allows for iterative feedback via attention-based reference image conditioning, which can be useful for refining the inpainted result.

### Metadata
**Author:** ssitu
**Repository:** [https://github.com/ssitu/ComfyUI_fabric](https://github.com/ssitu/ComfyUI_fabric)
**Install Type:** git-clone

---

### ComfyUI Flux 1.1 Ultra & Raw Node

**Description:**

A ComfyUI custom node for Black Forest Labs' FLUX 1.1 [pro] API, supporting both regular and Ultra modes with optional Raw mode.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_Flux_1.1_RAW_API](https://github.com/ShmuelRonen/ComfyUI_Flux_1.1_RAW_API)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This Flux API node supports Ultra mode which could be useful for inpainting tasks that require high-quality image generation.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_Flux_1.1_RAW_API](https://github.com/ShmuelRonen/ComfyUI_Flux_1.1_RAW_API)
**Install Type:** git-clone

---

### ComfyUI Flux Accelerator

**Description:**

ComfyUI Flux Accelerator is a custom node for ComfyUI that accelerates Flux.1 image generation, just by using this node.

- **Author:** discus0434
- **Repository:** [https://github.com/discus0434/comfyui-flux-accelerator](https://github.com/discus0434/comfyui-flux-accelerator)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** The Flux Accelerator node might provide some performance benefits but its direct relevance to inpainting with a mask input is unclear.

### Metadata
**Author:** discus0434
**Repository:** [https://github.com/discus0434/comfyui-flux-accelerator](https://github.com/discus0434/comfyui-flux-accelerator)
**Install Type:** git-clone

---

### ComfyUI Flux Trainer

**Description:**

Currently supports LoRA training, and untested full finetune with code from kohya's scripts: [a/https://github.com/kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-FluxTrainer](https://github.com/kijai/ComfyUI-FluxTrainer)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** The Flux Trainer has some relevance due to its ability to support LoRA training, but its full finetune capabilities are untested and may not be directly applicable to the inpainting workflow.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-FluxTrainer](https://github.com/kijai/ComfyUI-FluxTrainer)
**Install Type:** git-clone

---

### ComfyUI for InstructIR

**Description:**

Enhancing Image Restoration. (ref:[a/InstructIR](https://github.com/mv-lab/InstructIR))

- **Author:** zhongpei
- **Repository:** [https://github.com/zhongpei/ComfyUI-InstructIR](https://github.com/zhongpei/ComfyUI-InstructIR)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** The ComfyUI for InstructIR node appears very useful for the inpainting workflow with mask input as it enhances Image Restoration, a task closely related to inpainting.

### Metadata
**Author:** zhongpei
**Repository:** [https://github.com/zhongpei/ComfyUI-InstructIR](https://github.com/zhongpei/ComfyUI-InstructIR)
**Install Type:** git-clone

---

### ComfyUI Frame Maker

**Description:**

This node creates a sequence of frames by moving and scaling a subject image over a background image.

- **Author:** diSty
- **Repository:** [https://github.com/diStyApps/ComfyUI_FrameMaker](https://github.com/diStyApps/ComfyUI_FrameMaker)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node can be moderately useful in creating a sequence of frames that may be used as input or reference for the inpainting process.

### Metadata
**Author:** diSty
**Repository:** [https://github.com/diStyApps/ComfyUI_FrameMaker](https://github.com/diStyApps/ComfyUI_FrameMaker)
**Install Type:** git-clone

---

### ComfyUI Hallo

**Description:**

Unofficial implementation of [a/hallo](https://github.com/fudan-generative-vision/hallo) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_Hallo](https://github.com/hay86/ComfyUI_Hallo)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is an unofficial implementation of Hallo, which can be used for inpainting tasks and has direct relevance to the workflow goal.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_Hallo](https://github.com/hay86/ComfyUI_Hallo)
**Install Type:** git-clone

---

### ComfyUI HiDiffusion

**Description:**

Simple custom nodes for testing and use HiDiffusion technology: https://github.com/megvii-research/HiDiffusion/

- **Author:** florestefano1975
- **Repository:** [https://github.com/florestefano1975/ComfyUI-HiDiffusion](https://github.com/florestefano1975/ComfyUI-HiDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is related to HiDiffusion technology but its simplicity might limit its utility in a complex inpainting workflow with mask input.

### Metadata
**Author:** florestefano1975
**Repository:** [https://github.com/florestefano1975/ComfyUI-HiDiffusion](https://github.com/florestefano1975/ComfyUI-HiDiffusion)
**Install Type:** git-clone

---

### Comfyui HiFORCE Plugin

**Description:**

Custom nodes pack provided by [a/HiFORCE](https://www.hiforce.net/) for ComfyUI. This custom node helps to conveniently enhance images through Sampler, Upscaler, Mask, and more.
NOTE:You should install [a/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack). Many optimizations are built upon the foundation of ComfyUI-Impact-Pack.

- **Author:** hiforce
- **Repository:** [https://github.com/hiforce/comfyui-hiforce-plugin](https://github.com/hiforce/comfyui-hiforce-plugin)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node provides custom nodes for enhancing images through various operations like Sampler and Upscaler, which can be useful in an inpainting workflow with mask input.

### Metadata
**Author:** hiforce
**Repository:** [https://github.com/hiforce/comfyui-hiforce-plugin](https://github.com/hiforce/comfyui-hiforce-plugin)
**Install Type:** git-clone

---

### ComfyUI Impact Pack

**Description:**

This node pack offers various detector nodes and detailer nodes that allow you to configure a workflow that automatically enhances facial details. And provide iterative upscaler.
NOTE: To use the UltralyticsDetectorProvider, you must install the 'ComfyUI Impact Subpack' separately.

- **Author:** Dr.Lt.Data
- **Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Essential for enhancing facial details and iterative upscaling in the inpainting workflow

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
**Install Type:** git-clone

---

### ComfyUI Impact Subpack

**Description:**

This node pack provides nodes that complement the Impact Pack, such as the UltralyticsDetectorProvider.

- **Author:** Dr.Lt.Data
- **Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Very useful as a complementary pack for the Impact Pack, providing key nodes like UltralyticsDetectorProvider

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
**Install Type:** git-clone

---

### ComfyUI Inpaint Nodes

**Description:**

Nodes for better inpainting with ComfyUI. Adds various ways to pre-process inpaint areas. Supports the Fooocus inpaint model, a small and flexible patch which can be applied to any SDXL checkpoint and will improve consistency when generating masked areas.

- **Author:** Acly
- **Repository:** [https://github.com/Acly/comfyui-inpaint-nodes](https://github.com/Acly/comfyui-inpaint-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly supports inpainting with mask input using Fooocus model.

### Metadata
**Author:** Acly
**Repository:** [https://github.com/Acly/comfyui-inpaint-nodes](https://github.com/Acly/comfyui-inpaint-nodes)
**Install Type:** git-clone

---

### ComfyUI InstantID Faceswapper

**Description:**

Implementation of [a/faceswap](https://github.com/nosiu/InstantID-faceswap/tree/main) based on [a/InstantID](https://github.com/InstantID/InstantID) for ComfyUI. Allows usage of [a/LCM Lora](https://huggingface.co/latent-consistency/lcm-lora-sdxl) which can produce good results in only a few generation steps.
NOTE:Works ONLY with SDXL checkpoints.

- **Author:** nosiu
- **Repository:** [https://github.com/nosiu/comfyui-instantId-faceswap](https://github.com/nosiu/comfyui-instantId-faceswap)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Directly supports inpainting with mask input using LCM Lora and faceswapping, making it highly useful for this workflow goal.

### Metadata
**Author:** nosiu
**Repository:** [https://github.com/nosiu/comfyui-instantId-faceswap](https://github.com/nosiu/comfyui-instantId-faceswap)
**Install Type:** git-clone

---

### ComfyUI Iterative Mixing Nodes

**Description:**

Nodes to use Florence2 VLM for image vision tasks: object detection, captioning, segmentation and ocr

- **Author:** ttulttul
- **Repository:** [https://github.com/ttulttul/ComfyUI-Iterative-Mixer](https://github.com/ttulttul/ComfyUI-Iterative-Mixer)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides iterative mixing nodes that can be useful in image vision tasks such as inpainting, making it very useful for the specified workflow goal.

### Metadata
**Author:** ttulttul
**Repository:** [https://github.com/ttulttul/ComfyUI-Iterative-Mixer](https://github.com/ttulttul/ComfyUI-Iterative-Mixer)
**Install Type:** git-clone

---

### ComfyUI LatentSync

**Description:**

Unofficial implementation of [a/LatentSync](https://github.com/bytedance/LatentSync) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_LatentSync](https://github.com/hay86/ComfyUI_LatentSync)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node may be useful in certain situations but its relevance to the inpainting workflow goal is marginal.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_LatentSync](https://github.com/hay86/ComfyUI_LatentSync)
**Install Type:** git-clone

---

### ComfyUI Load and Save file to S3

**Description:**

Nodes:Load From S3, Save To S3.

- **Author:** kealiu
- **Repository:** [https://github.com/kealiu/ComfyUI-S3-Tools](https://github.com/kealiu/ComfyUI-S3-Tools)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used to load and save files from/to S3, which is essential for storing and retrieving data in an inpainting workflow with mask input.

### Metadata
**Author:** kealiu
**Repository:** [https://github.com/kealiu/ComfyUI-S3-Tools](https://github.com/kealiu/ComfyUI-S3-Tools)
**Install Type:** git-clone

---

### ComfyUI Mask Contour Processor

**Description:**

A ComfyUI node that improves inpainting results by extending mask boundaries with geometric patterns, helping create smoother transitions and better context for AI-driven image completion.

- **Author:** codeprimate
- **Repository:** [https://github.com/codeprimate/ComfyUI-MaskContourProcessor](https://github.com/codeprimate/ComfyUI-MaskContourProcessor)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node improves inpainting results by extending mask boundaries, making it very useful for this specific workflow goal.

### Metadata
**Author:** codeprimate
**Repository:** [https://github.com/codeprimate/ComfyUI-MaskContourProcessor](https://github.com/codeprimate/ComfyUI-MaskContourProcessor)
**Install Type:** git-clone

---

### ComfyUI Minimap

**Description:**

A simple minimap in the bottom-right of the window showing the full workflow, left click to navigate

- **Author:** OliverCrosby
- **Repository:** [https://github.com/OliverCrosby/Comfyui-Minimap](https://github.com/OliverCrosby/Comfyui-Minimap)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a useful minimap feature that can aid in navigation and visualization during the inpainting process.

### Metadata
**Author:** OliverCrosby
**Repository:** [https://github.com/OliverCrosby/Comfyui-Minimap](https://github.com/OliverCrosby/Comfyui-Minimap)
**Install Type:** git-clone

---

### ComfyUI Model Downloader

**Description:**

This node allows downloading models directly within ComfyUI for easier use and integration.

- **Author:** ciri
- **Repository:** [https://github.com/ciri/comfyui-model-downloader](https://github.com/ciri/comfyui-model-downloader)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the inpainting workflow by allowing users to download models within ComfyUI, which is essential for this specific task.

### Metadata
**Author:** ciri
**Repository:** [https://github.com/ciri/comfyui-model-downloader](https://github.com/ciri/comfyui-model-downloader)
**Install Type:** git-clone

---

### ComfyUI NAI Prompt Converter

**Description:**

A custom node extension for ComfyUI that enables conversion between NovelAI and ComfyUI prompt formats, along with extraction of NovelAI metadata from PNG images.

- **Author:** raspie10032
- **Repository:** [https://github.com/raspie10032/ComfyUI_RS_NAI_Local_Prompt_converter](https://github.com/raspie10032/ComfyUI_RS_NAI_Local_Prompt_converter)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This custom prompt converter can be useful for handling NovelAI prompts which might be used in conjunction with inpainting workflows.

### Metadata
**Author:** raspie10032
**Repository:** [https://github.com/raspie10032/ComfyUI_RS_NAI_Local_Prompt_converter](https://github.com/raspie10032/ComfyUI_RS_NAI_Local_Prompt_converter)
**Install Type:** git-clone

---

### ComfyUI Neural Network Toolkit NNT

**Description:**

Neural Network Toolkit (NNT) for ComfyUI is an extensive set of custom ComfyUI nodes for designing, training, and fine-tuning neural networks. This toolkit allows defining models, layers, training workflows, transformers, and tensor operations in a visual manner using nodes.

- **Author:** inventorado
- **Repository:** [https://github.com/inventorado/ComfyUI_NNT](https://github.com/inventorado/ComfyUI_NNT)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** As a comprehensive toolkit for designing and training neural networks, this node can be very useful in creating models for inpainting tasks.

### Metadata
**Author:** inventorado
**Repository:** [https://github.com/inventorado/ComfyUI_NNT](https://github.com/inventorado/ComfyUI_NNT)
**Install Type:** git-clone

---

### ComfyUI NodeReset

**Description:**

An extension for ComyUI to allow resetting a node's inputs to their default values.
NOTE:Right click any node and choose 'Reset' from the context menu.

- **Author:** BlakeOne
- **Repository:** [https://github.com/BlakeOne/ComfyUI-NodeReset](https://github.com/BlakeOne/ComfyUI-NodeReset)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be very useful for resetting nodes in the inpainting workflow to their default values, which could help troubleshoot or restart the process.

### Metadata
**Author:** BlakeOne
**Repository:** [https://github.com/BlakeOne/ComfyUI-NodeReset](https://github.com/BlakeOne/ComfyUI-NodeReset)
**Install Type:** git-clone

---

### ComfyUI Nodes for External Tooling

**Description:**

Provides nodes and server API extensions geared towards using ComfyUI as a backend for external tools.

- **Author:** Acly
- **Repository:** [https://github.com/Acly/comfyui-tooling-nodes](https://github.com/Acly/comfyui-tooling-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node might be marginally useful for integrating external tools into the inpainting workflow, but its relevance depends on the specific requirements of the workflow and the capabilities of the external tools.

### Metadata
**Author:** Acly
**Repository:** [https://github.com/Acly/comfyui-tooling-nodes](https://github.com/Acly/comfyui-tooling-nodes)
**Install Type:** git-clone

---

### ComfyUI nodes to use Style-Aligned

**Description:**

ComfyUI for [a/style-aligned](https://github.com/google/style-aligned)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_Style_Aligned](https://github.com/leeguandong/ComfyUI_Style_Aligned)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Style-Aligned is highly relevant and very useful for the inpainting workflow with mask input, as it can help align styles in images.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_Style_Aligned](https://github.com/leeguandong/ComfyUI_Style_Aligned)
**Install Type:** git-clone

---

### ComfyUI NPNet (Golden Noise)

**Description:**

A very barebones mostly-copypaste implementation of [a/https://github.com/xie-lab-ml/Golden-Noise-for-Diffusion-Models](https://github.com/xie-lab-ml/Golden-Noise-for-Diffusion-Models)

- **Author:** asagi4
- **Repository:** [https://github.com/asagi4/ComfyUI-NPNet](https://github.com/asagi4/ComfyUI-NPNet)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node might be useful as a supporting node due to its noise generation capabilities, but it"s not directly related to inpainting.

### Metadata
**Author:** asagi4
**Repository:** [https://github.com/asagi4/ComfyUI-NPNet](https://github.com/asagi4/ComfyUI-NPNet)
**Install Type:** git-clone

---

### ComfyUI Ollama

**Description:**

Custom ComfyUI Nodes for interacting with [a/Ollama](https://ollama.com/) using the [a/ollama python client](https://github.com/ollama/ollama-python).
Integrate the power of LLMs into CompfyUI workflows easily.

- **Author:** stavsap
- **Repository:** [https://github.com/stavsap/comfyui-ollama](https://github.com/stavsap/comfyui-ollama)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as a supporting node for the inpainting workflow since it allows integration of LLMs like Ollama to enhance or assist in the inpainting process.

### Metadata
**Author:** stavsap
**Repository:** [https://github.com/stavsap/comfyui-ollama](https://github.com/stavsap/comfyui-ollama)
**Install Type:** git-clone

---

### ComfyUI OpenVoice

**Description:**

Unofficial implementation of [a/OpenVoice](https://github.com/myshell-ai/OpenVoice) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_OpenVoice](https://github.com/hay86/ComfyUI_OpenVoice)
- **Install Type:** git-clone


### Applicability

**Score:** 50/100

**Reason:** While not directly relevant, it could be used as a supporting node for audio processing in an inpainting workflow.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_OpenVoice](https://github.com/hay86/ComfyUI_OpenVoice)
**Install Type:** git-clone

---

### ComfyUI Optical Flow

**Description:**

This package contains three nodes to help you compute optical flow between pairs of images, usually adjacent frames in a video, visualize the flow, and apply the flow to another image of the same dimensions. Most of the code is from Deforum, so this is released under the same license (MIT).

- **Author:** seanlynch
- **Repository:** [https://github.com/seanlynch/comfyui-optical-flow](https://github.com/seanlynch/comfyui-optical-flow)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides functionality that can help compute and apply optical flow between images, which is useful for inpainting with a mask input.

### Metadata
**Author:** seanlynch
**Repository:** [https://github.com/seanlynch/comfyui-optical-flow](https://github.com/seanlynch/comfyui-optical-flow)
**Install Type:** git-clone

---

### ComfyUI Overlay Media Node

**Description:**

This repository contains a custom ComfyUI node for overlaying media using ffmpeg.

- **Author:** Elaine-chennn
- **Repository:** [https://github.com/Elaine-chennn/comfyui-overlay-media](https://github.com/Elaine-chennn/comfyui-overlay-media)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node could potentially be used as a supporting node for media processing in an inpainting workflow, but its direct relevance is limited.

### Metadata
**Author:** Elaine-chennn
**Repository:** [https://github.com/Elaine-chennn/comfyui-overlay-media](https://github.com/Elaine-chennn/comfyui-overlay-media)
**Install Type:** git-clone

---

### ComfyUI PhotoMaker Plus

**Description:**

ComfyUI reference implementation for [a/PhotoMaker](https://github.com/TencentARC/PhotoMaker) models.
NOTE: PhotoMaker V2 is supported.

- **Author:** shiimizu
- **Repository:** [https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus](https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it provides a PhotoMaker model implementation that can be used for inpainting with mask input.

### Metadata
**Author:** shiimizu
**Repository:** [https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus](https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus)
**Install Type:** git-clone

---

### ComfyUI PixelArt Detector

**Description:**

This node manipulates the pixel art image in ways that it should look pixel perfect (downscales, changes palette, upscales etc.).

- **Author:** dimtoneff
- **Repository:** [https://github.com/dimtoneff/ComfyUI-PixelArt-Detector](https://github.com/dimtoneff/ComfyUI-PixelArt-Detector)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can manipulate pixel art images which could potentially be useful in an inpainting workflow with mask input.

### Metadata
**Author:** dimtoneff
**Repository:** [https://github.com/dimtoneff/ComfyUI-PixelArt-Detector](https://github.com/dimtoneff/ComfyUI-PixelArt-Detector)
**Install Type:** git-clone

---

### ComfyUI Pixtral Large Extension

**Description:**

A ComfyUI custom node that integrates Mistral AI's Pixtral Large vision model, enabling powerful multimodal AI capabilities within ComfyUI. Pixtral Large is a 124B parameter model (123B decoder + 1B visual encoder)

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_large](https://github.com/ShmuelRonen/ComfyUI_pixtral_large)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node integrates Pixtral Large vision model which is a powerful multimodal AI capability that can directly contribute to the inpainting process.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_large](https://github.com/ShmuelRonen/ComfyUI_pixtral_large)
**Install Type:** git-clone

---

### ComfyUI Preset Merger

**Description:**

Nodes: ModelMergeByPreset. Merge checkpoint models by preset

- **Author:** WASasquatch
- **Repository:** [https://github.com/WASasquatch/ComfyUI_Preset_Merger](https://github.com/WASasquatch/ComfyUI_Preset_Merger)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for merging checkpoint models by preset which could be a crucial step in fine-tuning an inpainting model.

### Metadata
**Author:** WASasquatch
**Repository:** [https://github.com/WASasquatch/ComfyUI_Preset_Merger](https://github.com/WASasquatch/ComfyUI_Preset_Merger)
**Install Type:** git-clone

---

### ComfyUI Prompt ExtraNetworks

**Description:**

Instead of LoraLoader or HypernetworkLoader, it receives a prompt and loads and applies LoRA or HN based on the specifications within the prompt. The main purpose of this custom node is to allow changes without reconnecting the LoraLoader node when the prompt is randomly altered, etc.

- **Author:** Taremin
- **Repository:** [https://github.com/Taremin/comfyui-prompt-extranetworks](https://github.com/Taremin/comfyui-prompt-extranetworks)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows changes to LoRA or HN specifications within a prompt without reconnecting nodes, which can be useful in an inpainting workflow where prompts are frequently altered.

### Metadata
**Author:** Taremin
**Repository:** [https://github.com/Taremin/comfyui-prompt-extranetworks](https://github.com/Taremin/comfyui-prompt-extranetworks)
**Install Type:** git-clone

---

### ComfyUI ProPainter Nodes

**Description:**

ComfyUI custom node implementation of [a/ProPainter](https://github.com/sczhou/ProPainter) framework for video inpainting.

- **Author:** daniabib
- **Repository:** [https://github.com/daniabib/ComfyUI_ProPainter_Nodes](https://github.com/daniabib/ComfyUI_ProPainter_Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements a video inpainting framework with mask input.

### Metadata
**Author:** daniabib
**Repository:** [https://github.com/daniabib/ComfyUI_ProPainter_Nodes](https://github.com/daniabib/ComfyUI_ProPainter_Nodes)
**Install Type:** git-clone

---

### ComfyUI PyramidFlow Wrapper

**Description:**

Wrapper for PyramidFlow -models: [a/https://github.com/jy0205/Pyramid-Flow](https://github.com/jy0205/Pyramid-Flow)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-PyramidFlowWrapper](https://github.com/kijai/ComfyUI-PyramidFlowWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Wraps a Pyramidal Flow model for video inpainting, which is highly relevant to the specified workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-PyramidFlowWrapper](https://github.com/kijai/ComfyUI-PyramidFlowWrapper)
**Install Type:** git-clone

---

### ComfyUI Resynthesizer

**Description:**

This repository is a quick port of [a/Resynthesizer](https://github.com/bootchk/resynthesizer) to ComfyUI.
Resynthesizer is the open-source implementation of a texture generation technique proposed by Paul Harrison in 2005, especially useful for removing an object from an image (inpainting), which is most likely close to what Photoshop uses to for the content aware fill feature. Note that this is not using a diffusion model to inpaint, as opposed to many techniques of today, which makes it very fast and predictable, but sometimes yields worse results.

- **Author:** brayevalerien
- **Repository:** [https://github.com/brayevalerien/ComfyUI-resynthesizer](https://github.com/brayevalerien/ComfyUI-resynthesizer)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a texture generation technique specifically useful for removing objects from images (inpainting) and is fast and predictable.

### Metadata
**Author:** brayevalerien
**Repository:** [https://github.com/brayevalerien/ComfyUI-resynthesizer](https://github.com/brayevalerien/ComfyUI-resynthesizer)
**Install Type:** git-clone

---

### ComfyUI Rife TensorRT

**Description:**

This project provides a TensorRT implementation of [a/RIFE](https://github.com/hzwer/ECCV2022-RIFE) for ultra fast frame interpolation inside ComfyUI

- **Author:** yuvraj108c
- **Repository:** [https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides an ultra-fast frame interpolation technique specifically useful for video editing tasks like inpainting and mask input.

### Metadata
**Author:** yuvraj108c
**Repository:** [https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt)
**Install Type:** git-clone

---

### ComfyUI SAM2(Segment Anything 2)

**Description:**

This project adapts the SAM2 to incorporate functionalities from [a/comfyui_segment_anything](https://github.com/storyicon/comfyui_segment_anything). Many thanks to continue-revolution for their foundational work.

- **Author:** neverbiasu
- **Repository:** [https://github.com/neverbiasu/ComfyUI-SAM2](https://github.com/neverbiasu/ComfyUI-SAM2)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is specifically designed for segmenting anything with mask input, making it highly relevant to the inpainting workflow goal.

### Metadata
**Author:** neverbiasu
**Repository:** [https://github.com/neverbiasu/ComfyUI-SAM2](https://github.com/neverbiasu/ComfyUI-SAM2)
**Install Type:** git-clone

---

### ComfyUI SaveAS

**Description:**

This custom node for ComfyUI allows you to save images in multiple formats, including PNG, JPG, WebP, and ICO.
[w/ComfyUI-Save-Multi-Format is renamed to SaveAs. Remove previous one and reinstall to this.]

- **Author:** SEkINVR
- **Repository:** [https://github.com/SEkINVR/ComfyUI-SaveAs](https://github.com/SEkINVR/ComfyUI-SaveAs)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node allows saving images in multiple formats, which could be useful for outputting the inpainted results.

### Metadata
**Author:** SEkINVR
**Repository:** [https://github.com/SEkINVR/ComfyUI-SaveAs](https://github.com/SEkINVR/ComfyUI-SaveAs)
**Install Type:** git-clone

---

### ComfyUI SchedulerMixer

**Description:**

Create a custom scheduler from a weighted average of the built-in schedulers

- **Author:** BlakeOne
- **Repository:** [https://github.com/BlakeOne/ComfyUI-SchedulerMixer](https://github.com/BlakeOne/ComfyUI-SchedulerMixer)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can create custom schedulers which might be useful for fine-tuning the inpainting process.

### Metadata
**Author:** BlakeOne
**Repository:** [https://github.com/BlakeOne/ComfyUI-SchedulerMixer](https://github.com/BlakeOne/ComfyUI-SchedulerMixer)
**Install Type:** git-clone

---

### ComfyUI Segment Anything

**Description:**

This project is a ComfyUI version of [a/sd-webui-segment-anything](https://github.com/continue-revolution/sd-webui-segment-anything). At present, only the most core functionalities have been implemented. I would like to express my gratitude to [a/continue-revolution](https://github.com/continue-revolution) for their preceding work on which this is based.

- **Author:** un-seen
- **Repository:** [https://github.com/un-seen/comfyui_segment_anything_plus](https://github.com/un-seen/comfyui_segment_anything_plus)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides functionality similar to Segment Anything, a popular model for image segmentation and inpainting.

### Metadata
**Author:** un-seen
**Repository:** [https://github.com/un-seen/comfyui_segment_anything_plus](https://github.com/un-seen/comfyui_segment_anything_plus)
**Install Type:** git-clone

---

### ComfyUI SegMoE

**Description:**

Unofficial implementation of [a/SegMoE: Segmind Mixture of Diffusion Experts](https://github.com/segmind/segmoe) for ComfyUI

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node is an unofficial implementation of SegMoE, which can be used for inpainting tasks with mask input.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE)
**Install Type:** git-clone

---

### ComfyUI Simple Feed

**Description:**

A lightweight image tray forked from Comfy-UI-CustomScripts with simple sorting, positioning and filtering options.

- **Author:** tachyon-beep
- **Repository:** [https://github.com/tachyon-beep/comfyui-simplefeed](https://github.com/tachyon-beep/comfyui-simplefeed)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can be used to display and manage images in a simple feed but does not directly contribute to the inpainting process.

### Metadata
**Author:** tachyon-beep
**Repository:** [https://github.com/tachyon-beep/comfyui-simplefeed](https://github.com/tachyon-beep/comfyui-simplefeed)
**Install Type:** git-clone

---

### ComfyUI Slothful Attention

**Description:**

This custom node allow controlling output without training. The reducing method is similar to [a/Spatial-Reduction Attention](https://paperswithcode.com/method/spatial-reduction-attention), but generating speed may not be increased on typical image sizes due to overheads. (In some cases, slightly slower)

- **Author:** MitoshiroPJ
- **Repository:** [https://github.com/MitoshiroPJ/comfyui_slothful_attention](https://github.com/MitoshiroPJ/comfyui_slothful_attention)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** The Slothful Attention node seems to be relevant to the workflow goal as it allows controlling output without training and has a reducing method similar to Spatial-Reduction Attention which could potentially be useful in an inpainting workflow with a mask input.

### Metadata
**Author:** MitoshiroPJ
**Repository:** [https://github.com/MitoshiroPJ/comfyui_slothful_attention](https://github.com/MitoshiroPJ/comfyui_slothful_attention)
**Install Type:** git-clone

---

### ComfyUI StabilityAI Suite

**Description:**

This fork of the official StabilityAI repository contains a number of enhancements and implementations.

- **Author:** florestefano1975
- **Repository:** [https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite](https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a suite of StabilityAI models which can be used for inpainting tasks, making it very useful for the specified workflow goal.

### Metadata
**Author:** florestefano1975
**Repository:** [https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite](https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite)
**Install Type:** git-clone

---

### ComfyUI Stable Video Diffusion

**Description:**

Easily use Stable Video Diffusion inside ComfyUI!

- **Author:** thecooltechguy
- **Repository:** [https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides direct access to Stable Video Diffusion which can be used for inpainting tasks, making it very useful and almost essential for the specified workflow goal.

### Metadata
**Author:** thecooltechguy
**Repository:** [https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion)
**Install Type:** git-clone

---

### ComfyUI template matching

**Description:**

This project is a ComfyUI version of [a/https://github.com/cozheyuanzhangde/Invariant-TemplateMatching](https://github.com/cozheyuanzhangde/Invariant-TemplateMatching).

- **Author:** wentao-uw
- **Repository:** [https://github.com/wentao-uw/ComfyUI-template-matching](https://github.com/wentao-uw/ComfyUI-template-matching)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used for template matching which could potentially be useful in inpainting workflows.

### Metadata
**Author:** wentao-uw
**Repository:** [https://github.com/wentao-uw/ComfyUI-template-matching](https://github.com/wentao-uw/ComfyUI-template-matching)
**Install Type:** git-clone

---

### ComfyUI Timer Nodes

**Description:**

This project provides a set of custom timer nodes for ComfyUI. These nodes allow you to measure and append runtime information to strings or other data during your workflow.

- **Author:** shannooty
- **Repository:** [https://github.com/Shannooty/ComfyUI-Timer-Nodes](https://github.com/Shannooty/ComfyUI-Timer-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is moderately useful as it provides timer nodes that can measure and append runtime information to strings or other data during the workflow, but it does not directly contribute to inpainting with a mask input.

### Metadata
**Author:** shannooty
**Repository:** [https://github.com/Shannooty/ComfyUI-Timer-Nodes](https://github.com/Shannooty/ComfyUI-Timer-Nodes)
**Install Type:** git-clone

---

### ComfyUI Upscaler TensorRT

**Description:**

This project provides a Tensorrt implementation for fast image upscaling inside ComfyUI (3-4x faster)

- **Author:** yuvraj108c
- **Repository:** [https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a fast image upscaling capability using TensorRT, which can be useful for preprocessing images in an inpainting workflow.

### Metadata
**Author:** yuvraj108c
**Repository:** [https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt)
**Install Type:** git-clone

---

### ComfyUI Vectorscope CC

**Description:**

ComfyUI port of Vectorscope CC and Diffusion Color Grading by Haoming02. Makes it possible to adjust Brightness/Contrast/Saturation/Hue during image generation.

- **Author:** pamparamm
- **Repository:** [https://github.com/pamparamm/ComfyUI-vectorscope-cc](https://github.com/pamparamm/ComfyUI-vectorscope-cc)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** It allows adjusting Brightness/Contrast/Saturation/Hue during image generation which can be useful for fine-tuning the inpainted result.

### Metadata
**Author:** pamparamm
**Repository:** [https://github.com/pamparamm/ComfyUI-vectorscope-cc](https://github.com/pamparamm/ComfyUI-vectorscope-cc)
**Install Type:** git-clone

---

### ComfyUI VIDU

**Description:**

This is a ComfyUI node package that integrates with VIDU API, supporting features such as text-to-video, image-to-video, character-to-video generation, and video super-resolution.

- **Author:** 1zhangyy1
- **Repository:** [https://github.com/1zhangyy1/comfyui-vidu-nodes](https://github.com/1zhangyy1/comfyui-vidu-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** It supports features like text-to-video and image-to-video generation but none of these are directly related to inpainting with a mask input.

### Metadata
**Author:** 1zhangyy1
**Repository:** [https://github.com/1zhangyy1/comfyui-vidu-nodes](https://github.com/1zhangyy1/comfyui-vidu-nodes)
**Install Type:** git-clone

---

### ComfyUI Web Viewer

**Description:**

The ComfyUI Web Viewer by [a/vrch.ai](https://vrch.ai) is a custom node collection offering a real-time AI-generated interactive art framework. This utility integrates realtime streaming into ComfyUI workflows, supporting keyboard control nodes, OSC control nodes, sound input nodes, and more. Accessible from any device with a web browser, it enables real time interaction with AI-generated content, making it ideal for interactive visual projects and enhancing ComfyUI workflows with efficient content management and display.

- **Author:** Vrch Studio (vrch.ai)
- **Repository:** [https://github.com/VrchStudio/comfyui-web-viewer](https://github.com/VrchStudio/comfyui-web-viewer)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for the specified workflow goal as it provides real-time AI-generated interactive art framework and supports keyboard control nodes, OSC control nodes, sound input nodes, and more.

### Metadata
**Author:** Vrch Studio (vrch.ai)
**Repository:** [https://github.com/VrchStudio/comfyui-web-viewer](https://github.com/VrchStudio/comfyui-web-viewer)
**Install Type:** git-clone

---

### Comfyui Webcam capture node

**Description:**

This node captures images one at a time from your webcam when you click generate.
This is particular useful for img2img or controlnet workflows.
NOTE:This node will take over your webcam, so if you have another program using it, you may need to close that program first. Likewise, you may need to close Comfyui or close the workflow to release the webcam.

- **Author:** victorchall
- **Repository:** [https://github.com/victorchall/comfyui_webcamcapture](https://github.com/victorchall/comfyui_webcamcapture)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for the specified workflow goal as it can capture images from a webcam one at a time, which may be useful in certain inpainting scenarios.

### Metadata
**Author:** victorchall
**Repository:** [https://github.com/victorchall/comfyui_webcamcapture](https://github.com/victorchall/comfyui_webcamcapture)
**Install Type:** git-clone

---

### ComfyUI Workspace Manager - Comfyspace

**Description:**

A ComfyUI custom node for project management to centralize the management of all your workflows in one place. Seamlessly switch between workflows, create and update them within a single workspace, like Google Docs.

- **Author:** 11cafe
- **Repository:** [https://github.com/11cafe/comfyui-workspace-manager](https://github.com/11cafe/comfyui-workspace-manager)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a workspace manager that can centralize and manage workflows, making it very useful for organizing an inpainting workflow.

### Metadata
**Author:** 11cafe
**Repository:** [https://github.com/11cafe/comfyui-workspace-manager](https://github.com/11cafe/comfyui-workspace-manager)
**Install Type:** git-clone

---

### ComfyUI YetAnotherSafetyChecker

**Description:**

Just a simple node to filter out NSFW outputs. This node utilizes [a/AdamCodd/vit-base-nsfw-detector](https://huggingface.co/AdamCodd/vit-base-nsfw-detector) to score the outputs. I chose this model because it's small, fast, and performed very well in my testing. Nudity tends to be scored in the 0.95+ range, but I've set the default to 0.8 as a safe baseline.

- **Author:** BetaDoggo
- **Repository:** [https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker](https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node filters out NSFW outputs, which could be useful for an inpainting workflow that requires safe and appropriate content, but its relevance is not directly related to the mask input.

### Metadata
**Author:** BetaDoggo
**Repository:** [https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker](https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker)
**Install Type:** git-clone

---

### ComfyUI Yolov8

**Description:**

Nodes: Yolov8Detection, Yolov8Segmentation. Deadly simple yolov8 comfyui plugin

- **Author:** zcfrank1st
- **Repository:** [https://github.com/zcfrank1st/Comfyui-Yolov8](https://github.com/zcfrank1st/Comfyui-Yolov8)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node provides object detection and segmentation capabilities which could support the inpainting workflow by providing necessary information for inpainting.

### Metadata
**Author:** zcfrank1st
**Repository:** [https://github.com/zcfrank1st/Comfyui-Yolov8](https://github.com/zcfrank1st/Comfyui-Yolov8)
**Install Type:** git-clone

---

### ComfyUI-3D-Pack

**Description:**

Make 3D assets generation in ComfyUI good and convenient as it generates image/video!
This is an extensive node suite that enables ComfyUI to process 3D inputs (Mesh & UV Texture, etc.) using cutting edge algorithms (3DGS, NeRF, etc.) and models (InstantMesh, CRM, TripoSR, etc.)
NOTE: Pre-built python wheels can manually download from [a/https://github.com/MrForExample/Comfy3D_Pre_Builds](https://github.com/MrForExample/Comfy3D_Pre_Builds) if automatic install failed

- **Author:** MrForExample
- **Repository:** [https://github.com/MrForExample/ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node suite provides extensive support for 3D inputs and cutting-edge algorithms, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** MrForExample
**Repository:** [https://github.com/MrForExample/ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack)
**Install Type:** git-clone

---

### ComfyUI-3d-photo-inpainting

**Description:**

a comfyui custom node for [a/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting),then you can render one image to zoom-in/dolly zoom/swing motion/circle motion video

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-3d-photo-inpainting](https://github.com/AIFSH/ComfyUI-3d-photo-inpainting)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This custom node is specifically designed for 3D photo inpainting, which aligns perfectly with the workflow goal of inpainting with mask input.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-3d-photo-inpainting](https://github.com/AIFSH/ComfyUI-3d-photo-inpainting)
**Install Type:** git-clone

---

### ComfyUI-Advanced-ControlNet

**Description:**

Nodes for scheduling ControlNet strength across timesteps and batched latents, as well as applying custom weights and attention masks.

- **Author:** Kosinkadink
- **Repository:** [https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides advanced control over ControlNet strength and attention masks which can be useful for fine-tuning inpainting results with mask input.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
**Install Type:** git-clone

---

### ComfyUI-AdvancedTiling

**Description:**

Advanced tiling of various shapes for ComfyUI

- **Author:** JosefKuchar
- **Repository:** [https://github.com/JosefKuchar/ComfyUI-AdvancedTiling](https://github.com/JosefKuchar/ComfyUI-AdvancedTiling)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides advanced tiling capabilities which may be useful for organizing and processing multiple images in the inpainting workflow, but it is not directly related to the task of inpainting with a mask.

### Metadata
**Author:** JosefKuchar
**Repository:** [https://github.com/JosefKuchar/ComfyUI-AdvancedTiling](https://github.com/JosefKuchar/ComfyUI-AdvancedTiling)
**Install Type:** git-clone

---

### ComfyUI-AharaNodes

**Description:**

NODES:Frame Segmenter, Get Frame at Index, Repeat Sampler Config, Patch Repeat Sampler Config (Model), Patch Repeat Sampler Config (Latent), KSampler (Simple Input)

- **Author:** chris-arsenault
- **Repository:** [https://github.com/chris-arsenault/ComfyUI-AharaNodes](https://github.com/chris-arsenault/ComfyUI-AharaNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** The Frame Segmenter is directly relevant to the inpainting workflow with mask input, helping segment frames which can be used as input for inpainting.

### Metadata
**Author:** chris-arsenault
**Repository:** [https://github.com/chris-arsenault/ComfyUI-AharaNodes](https://github.com/chris-arsenault/ComfyUI-AharaNodes)
**Install Type:** git-clone

---

### ComfyUI-AIT

**Description:**

A ComfyUI implementation of Facebook Meta's [a/AITemplate](https://github.com/facebookincubator/AITemplate) repo for faster inference using cpp/cuda. This new repo is behind the old version but is a much more stable foundation to keep AIT online. Please be patient as the repo will eventually include the same features as before.
NOTE: You can find the old AIT extension in the legacy channel.

- **Author:** FizzleDorf
- **Repository:** [https://github.com/FizzleDorf/ComfyUI-AIT](https://github.com/FizzleDorf/ComfyUI-AIT)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI-AIT is specifically designed for faster inference using cpp/cuda and can be used as a key component of an inpainting workflow with mask input.

### Metadata
**Author:** FizzleDorf
**Repository:** [https://github.com/FizzleDorf/ComfyUI-AIT](https://github.com/FizzleDorf/ComfyUI-AIT)
**Install Type:** git-clone

---

### ComfyUI-Allegro

**Description:**

ComfyUI supports over [a/rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro), which uses text prompt to generate short video in relatively high quality, especially comparing to other open source solutions available for now.

- **Author:** bombax-xiaoice
- **Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Allegro](https://github.com/bombax-xiaoice/ComfyUI-Allegro)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node uses text prompts to generate high-quality video and can be used as a supporting tool for the inpainting workflow by generating background images.

### Metadata
**Author:** bombax-xiaoice
**Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Allegro](https://github.com/bombax-xiaoice/ComfyUI-Allegro)
**Install Type:** git-clone

---

### ComfyUI-AnimateAnyone-reproduction

**Description:**

A ComfyUI custom node that simply integrates the [a/animate-anyone-reproduction](https://github.com/bendanzzc/AnimateAnyone-reproduction) functionality.

- **Author:** AuroBit
- **Repository:** [https://github.com/AuroBit/ComfyUI-AnimateAnyone-reproduction](https://github.com/AuroBit/ComfyUI-AnimateAnyone-reproduction)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node integrates the AnimateAnyone-reproduction functionality, which might be useful for certain animation tasks, but its direct relevance to inpainting workflows is limited.

### Metadata
**Author:** AuroBit
**Repository:** [https://github.com/AuroBit/ComfyUI-AnimateAnyone-reproduction](https://github.com/AuroBit/ComfyUI-AnimateAnyone-reproduction)
**Install Type:** git-clone

---

### ComfyUI-Animation_Nodes_and_Workflows

**Description:**

These are nodes and workflows that can facilitate the creation of animations and video compilations.

- **Author:** Isi-dev
- **Repository:** [https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows](https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node contains animation nodes and workflows, which could be useful for creating animations that involve inpainting or masking techniques.

### Metadata
**Author:** Isi-dev
**Repository:** [https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows](https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows)
**Install Type:** git-clone

---

### ComfyUI-APGScaling

**Description:**

ComfyUI nodes to use [a/APG scaling](https://huggingface.co/papers/2410.02416) for CFG, allowing for better image quality with higher CFG.

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-APGScaling](https://github.com/logtd/ComfyUI-APGScaling)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a method for scaling images using APG, which can be useful in improving image quality for inpainting.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-APGScaling](https://github.com/logtd/ComfyUI-APGScaling)
**Install Type:** git-clone

---

### ComfyUI-Arrow-Key-Canvas-Navigation

**Description:**

A ComfyUI Custom Node that enables arrow key canvas navigation with a pan speed setting.

- **Author:** codecringebinge
- **Repository:** [https://github.com/codecringebinge/ComfyUI-Arrow-Key-Canvas-Navigation](https://github.com/codecringebinge/ComfyUI-Arrow-Key-Canvas-Navigation)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node provides navigation functionality, which can be useful in adjusting the canvas for inpainting tasks.

### Metadata
**Author:** codecringebinge
**Repository:** [https://github.com/codecringebinge/ComfyUI-Arrow-Key-Canvas-Navigation](https://github.com/codecringebinge/ComfyUI-Arrow-Key-Canvas-Navigation)
**Install Type:** git-clone

---

### comfyui-art-venture

**Description:**

A comprehensive set of custom nodes for ComfyUI, focusing on utilities for image processing, JSON manipulation, model operations and working with object via URLs

- **Author:** sipherxyz
- **Repository:** [https://github.com/sipherxyz/comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture)
- **Install Type:** git-clone


### Applicability

**Score:** 85/100

**Reason:** This node offers a comprehensive set of utilities for image processing and model operations, making it moderately to very useful for inpainting workflows.

### Metadata
**Author:** sipherxyz
**Repository:** [https://github.com/sipherxyz/comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture)
**Install Type:** git-clone

---

### ComfyUI-AstralAnimator

**Description:**

A custom node for ComfyUI that enables smooth, keyframe-based animations for image generation. Create dynamic sequences with control over motion, zoom, rotation, and easing effects. Ideal for AI-assisted animation and video content creation.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-AstralAnimator](https://github.com/ShmuelRonen/ComfyUI-AstralAnimator)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has some marginally relevant features such as animation control but does not directly support the inpainting workflow with mask input.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-AstralAnimator](https://github.com/ShmuelRonen/ComfyUI-AstralAnimator)
**Install Type:** git-clone

---

### ComfyUI-AudioLDM

**Description:**

ComfyUI Workflow to run audioldm-l-full pipeline
[a/https://huggingface.co/cvssp/audioldm-l-full](https://huggingface.co/cvssp/audioldm-l-full)

- **Author:** sanbuphy
- **Repository:** [https://github.com/sanbuphy/ComfyUI-AudioLDM](https://github.com/sanbuphy/ComfyUI-AudioLDM)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it directly supports the specified workflow goal of inpainting with a mask input by providing an audioldm-l-full pipeline.

### Metadata
**Author:** sanbuphy
**Repository:** [https://github.com/sanbuphy/ComfyUI-AudioLDM](https://github.com/sanbuphy/ComfyUI-AudioLDM)
**Install Type:** git-clone

---

### ComfyUI-AutoCropFaces

**Description:**

Use RetinaFace to detect and automatically crop faces.

- **Author:** Sida Liu
- **Repository:** [https://github.com/liusida/ComfyUI-AutoCropFaces](https://github.com/liusida/ComfyUI-AutoCropFaces)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can automatically detect and crop faces from images, which might be necessary for inpainting tasks.

### Metadata
**Author:** Sida Liu
**Repository:** [https://github.com/liusida/ComfyUI-AutoCropFaces](https://github.com/liusida/ComfyUI-AutoCropFaces)
**Install Type:** git-clone

---

### ComfyUI-AutomaticCFG

**Description:**

My own version 'from scratch' of a self-rescaling CFG. It isn't much but it's honest work.
TLDR: set your CFG at 8 to try it. No burned images and artifacts anymore. CFG is also a bit more sensitive because it's a proportion around 8. Low scale like 4 also gives really nice results since your CFG is not the CFG anymore. Also in general even with relatively low settings it seems to improve the quality.

- **Author:** Extraltodeus
- **Repository:** [https://github.com/Extraltodeus/ComfyUI-AutomaticCFG](https://github.com/Extraltodeus/ComfyUI-AutomaticCFG)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node optimizes CFG settings for high-quality results in inpainting workflows.

### Metadata
**Author:** Extraltodeus
**Repository:** [https://github.com/Extraltodeus/ComfyUI-AutomaticCFG](https://github.com/Extraltodeus/ComfyUI-AutomaticCFG)
**Install Type:** git-clone

---

### ComfyUI-AutoSplitGridImage

**Description:**

ComfyUI-AutoSplitGridImage is a custom node for ComfyUI that provides intelligent image splitting functionality. It combines edge detection for column splits and uniform division for row splits, offering a balanced approach to grid-based image segmentation.

- **Author:** stormcenter
- **Repository:** [https://github.com/stormcenter/ComfyUI-AutoSplitGridImage](https://github.com/stormcenter/ComfyUI-AutoSplitGridImage)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node splits images into grids based on edge detection and uniform division, aiding in mask input preparation.

### Metadata
**Author:** stormcenter
**Repository:** [https://github.com/stormcenter/ComfyUI-AutoSplitGridImage](https://github.com/stormcenter/ComfyUI-AutoSplitGridImage)
**Install Type:** git-clone

---

### ComfyUI-Azure-Blob-Storage

**Description:**

ComfyUI-Azure-Blob-Storage seamlessly integrates with [a/Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/) in ComfyUI. This open-source project provides custom nodes for effortless loading and saving of images, videos, and checkpoint models directly from Azure blob containers within the ComfyUI graph interface.

- **Author:** l20richo
- **Repository:** [https://github.com/l20richo/ComfyUI-Azure-Blob-Storage](https://github.com/l20richo/ComfyUI-Azure-Blob-Storage)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Essential for storing and loading images from Azure blob containers in the inpainting workflow.

### Metadata
**Author:** l20richo
**Repository:** [https://github.com/l20richo/ComfyUI-Azure-Blob-Storage](https://github.com/l20richo/ComfyUI-Azure-Blob-Storage)
**Install Type:** git-clone

---

### ComfyUI-Background-Edit

**Description:**

ComfyUI nodes for editing background of images/videos with CUDA acceleration support.

- **Author:** yondonfu
- **Repository:** [https://github.com/yondonfu/ComfyUI-Background-Edit](https://github.com/yondonfu/ComfyUI-Background-Edit)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Very useful for editing backgrounds of images and videos in the inpainting workflow, especially considering its CUDA acceleration support.

### Metadata
**Author:** yondonfu
**Repository:** [https://github.com/yondonfu/ComfyUI-Background-Edit](https://github.com/yondonfu/ComfyUI-Background-Edit)
**Install Type:** git-clone

---

### ComfyUI-Benripack

**Description:**

ComfyUI-Benripack is an extension for ComfyUI that provides a CharacterPipe node. This node allows for managing various elements such as images, prompts, and models in a single structure, simplifying the workflow for character-based image generation.

- **Author:** blackcodetavern
- **Repository:** [https://github.com/blackcodetavern/ComfyUI-Benripack](https://github.com/blackcodetavern/ComfyUI-Benripack)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node simplifies character-based image generation workflows by managing various elements in a single structure, making it very useful for this workflow goal.

### Metadata
**Author:** blackcodetavern
**Repository:** [https://github.com/blackcodetavern/ComfyUI-Benripack](https://github.com/blackcodetavern/ComfyUI-Benripack)
**Install Type:** git-clone

---

### ComfyUI-BiRefNet-Fix utils

**Description:**

Bilateral Reference Network achieves SOTA result in multi Salient Object Segmentation dataset, this repo pack BiRefNet as ComfyUI nodes, and make this SOTA model easier use for everyone.
NOTE: The original node was replaced with a version maintained by hieuck because it is no longer maintained.

- **Author:** viperyl
- **Repository:** [https://github.com/hieuck/ComfyUI-BiRefNet](https://github.com/hieuck/ComfyUI-BiRefNet)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a high-performance BiRefNet model that achieves SOTA results in multi Salient Object Segmentation dataset, making it very useful for inpainting with mask input.

### Metadata
**Author:** viperyl
**Repository:** [https://github.com/hieuck/ComfyUI-BiRefNet](https://github.com/hieuck/ComfyUI-BiRefNet)
**Install Type:** git-clone

---

### ComfyUI-BiRefNet-Hugo

**Description:**

This repository wraps the latest BiRefNet model as ComfyUI nodes. Compared to the previous model, the latest model offers higher and better matting accuracy.

- **Author:** Hugo
- **Repository:** [https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo](https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node wraps the latest BiRefNet model offering higher and better matting accuracy, which is essential for achieving high-quality inpainting results with mask input.

### Metadata
**Author:** Hugo
**Repository:** [https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo](https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo)
**Install Type:** git-clone

---

### ComfyUI-BiRefNet-lite

**Description:**

This repository packages the latest BiRefNet model as a ComfyUI node for use, supporting chunked loading on both CPU and GPU, as well as model caching features.

- **Author:** duhaifeng
- **Repository:** [https://github.com/rubi-du/ComfyUI-BiRefNet-Super](https://github.com/rubi-du/ComfyUI-BiRefNet-Super)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node packages the latest BiRefNet model supporting chunked loading on both CPU and GPU, as well as model caching features, making it very useful for large-scale inpainting tasks with mask input.

### Metadata
**Author:** duhaifeng
**Repository:** [https://github.com/rubi-du/ComfyUI-BiRefNet-Super](https://github.com/rubi-du/ComfyUI-BiRefNet-Super)
**Install Type:** git-clone

---

### ComfyUI-Bongsang

**Description:**

The 'ComfyUI-Bongsang' is very useful tools for a diffusion model developer.

- **Author:** bongsang
- **Repository:** [https://github.com/bongsang/ComfyUI-Bongsang](https://github.com/bongsang/ComfyUI-Bongsang)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is a general-purpose tool for diffusion model developers and could be useful in various aspects of the inpainting workflow with mask input.

### Metadata
**Author:** bongsang
**Repository:** [https://github.com/bongsang/ComfyUI-Bongsang](https://github.com/bongsang/ComfyUI-Bongsang)
**Install Type:** git-clone

---

### ComfyUI-BRIA_AI-RMBG

**Description:**

Unofficial implementation of BRIA RMBG Model for ComfyUI.

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG](https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides an implementation of the BRIA RMBG Model for ComfyUI and could be essential for achieving the inpainting workflow with mask input goal.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG](https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG)
**Install Type:** git-clone

---

### comfyui-bunny-cdn-storage

**Description:**

Save Your Image to BunnyStorage

- **Author:** k-komarov
- **Repository:** [https://github.com/k-komarov/comfyui-bunny-cdn-storage](https://github.com/k-komarov/comfyui-bunny-cdn-storage)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node allows saving images to BunnyStorage, which can be useful for storing the inpainted image.

### Metadata
**Author:** k-komarov
**Repository:** [https://github.com/k-komarov/comfyui-bunny-cdn-storage](https://github.com/k-komarov/comfyui-bunny-cdn-storage)
**Install Type:** git-clone

---

### ComfyUI-CADS

**Description:**

Attempts to implement [a/CADS](https://arxiv.org/abs/2310.17347) for ComfyUI. Credit also to the [a/A1111 implementation](https://github.com/v0xie/sd-webui-cads/tree/main) that I used as a reference.

- **Author:** asagi4
- **Repository:** [https://github.com/asagi4/ComfyUI-CADS](https://github.com/asagi4/ComfyUI-CADS)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node implements CADS, which can be useful for inpainting tasks, especially those involving complex shapes or objects.

### Metadata
**Author:** asagi4
**Repository:** [https://github.com/asagi4/ComfyUI-CADS](https://github.com/asagi4/ComfyUI-CADS)
**Install Type:** git-clone

---

### ComfyUI-Calculation

**Description:**

Nodes: Center Calculation. Improved Numerical Calculation for ComfyUI

- **Author:** Limitex
- **Repository:** [https://github.com/Limitex/ComfyUI-Calculation](https://github.com/Limitex/ComfyUI-Calculation)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Center Calculation is a numerical calculation node that could be useful for adjusting the position of the inpainted region based on the mask input.

### Metadata
**Author:** Limitex
**Repository:** [https://github.com/Limitex/ComfyUI-Calculation](https://github.com/Limitex/ComfyUI-Calculation)
**Install Type:** git-clone

---

### ComfyUI-CascadeResolutions

**Description:**

Nodes:Cascade Resolutions

- **Author:** al-swaiti
- **Repository:** [https://github.com/al-swaiti/ComfyUI-CascadeResolutions](https://github.com/al-swaiti/ComfyUI-CascadeResolutions)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Cascade Resolutions could potentially be useful for adjusting the resolution of the inpainted region based on the mask input, but its direct relevance is limited.

### Metadata
**Author:** al-swaiti
**Repository:** [https://github.com/al-swaiti/ComfyUI-CascadeResolutions](https://github.com/al-swaiti/ComfyUI-CascadeResolutions)
**Install Type:** git-clone

---

### Comfyui-CatVTON

**Description:**

Comfyui-CatVTON This repository is the modified official Comfyui node of CatVTON, which is a simple and efficient virtual try-on diffusion model with 1) Lightweight Network (899.06M parameters totally), 2) Parameter-Efficient Training (49.57M parameters trainable) 3) Simplified Inference (< 8G VRAM for 1024X768 resolution).
The original GitHub project is [a/https://github.com/Zheng-Chong/CatVTON](https://github.com/Zheng-Chong/CatVTON)

- **Author:** pzc163
- **Repository:** [https://github.com/pzc163/Comfyui-CatVTON](https://github.com/pzc163/Comfyui-CatVTON)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a virtual try-on diffusion model that can be used for inpainting tasks with mask input.

### Metadata
**Author:** pzc163
**Repository:** [https://github.com/pzc163/Comfyui-CatVTON](https://github.com/pzc163/Comfyui-CatVTON)
**Install Type:** git-clone

---

### ComfyUI-CatvtonFluxWrapper

**Description:**

ComfyUI-CatvtonFluxWrapper provides ComfyUI nodes for diffusers implementation of Catvton-Flux.

- **Author:** lujiazho
- **Repository:** [https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper](https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides ComfyUI nodes for diffusers implementation of Catvton-Flux, which is relevant to the inpainting workflow with mask input.

### Metadata
**Author:** lujiazho
**Repository:** [https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper](https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper)
**Install Type:** git-clone

---

### ComfyUI-ClipScore-Nodes

**Description:**

Nodes:ImageScore, Loader, Image Processor, Real Image Processor, Fake Image Processor, Text Processor. ComfyUI Nodes for ClipScore

- **Author:** azure-dragon-ai
- **Repository:** [https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes](https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** ImageScore and other nodes in ComfyUI-ClipScore-Nodes may be useful for evaluating or processing images but are not directly related to the inpainting task.

### Metadata
**Author:** azure-dragon-ai
**Repository:** [https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes](https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes)
**Install Type:** git-clone

---

### ComfyUI-CLIPSlider

**Description:**

A node to replicate [a/https://huggingface.co/spaces/latentexplorers/latentnavigation-flux](A node to replicate https://huggingface.co/spaces/latentexplorers/latentnavigation-flux)

- **Author:** RhizoNymph
- **Repository:** [https://github.com/RhizoNymph/ComfyUI-CLIPSlider](https://github.com/RhizoNymph/ComfyUI-CLIPSlider)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI-CLIPSlider is highly relevant as it allows users to interactively navigate a latent space which can be used in inpainting workflows with mask input.

### Metadata
**Author:** RhizoNymph
**Repository:** [https://github.com/RhizoNymph/ComfyUI-CLIPSlider](https://github.com/RhizoNymph/ComfyUI-CLIPSlider)
**Install Type:** git-clone

---

### ComfyUI-CogVideoX-MZ

**Description:**

Nodes:MZ_CogVideoXLoader

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ](https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant as it provides a pre-trained model specifically designed for video inpainting tasks.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ](https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ)
**Install Type:** git-clone

---

### ComfyUI-ColorWheel

**Description:**

NODES:Color Wheel Generator

- **Author:** RhizoNymph
- **Repository:** [https://github.com/RhizoNymph/ComfyUI-ColorWheel](https://github.com/RhizoNymph/ComfyUI-ColorWheel)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node generates a color wheel which can be useful for selecting colors in the inpainting process.

### Metadata
**Author:** RhizoNymph
**Repository:** [https://github.com/RhizoNymph/ComfyUI-ColorWheel](https://github.com/RhizoNymph/ComfyUI-ColorWheel)
**Install Type:** git-clone

---

### ComfyUI-ComfyWorkflows

**Description:**

The best way to run, share, & discover thousands of ComfyUI workflows.

- **Author:** thecooltechguy
- **Repository:** [https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows](https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides access to thousands of ComfyUI workflows but does not directly support the specific goal of an inpainting workflow with mask input.

### Metadata
**Author:** thecooltechguy
**Repository:** [https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows](https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows)
**Install Type:** git-clone

---

### ComfyUI-ConditionalInterrupt

**Description:**

A node for ComfyUI that terminates the workflow processing if 'proceed' is set to False. More convenient than manually bypassing a bunch of nodes.
This is a restructured version of the 'SRL Conditional Interrupt' node from the [a/srl-nodes](https://github.com/seanlynch/srl-nodes) pack.

- **Author:** SparknightLLC
- **Repository:** [https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt](https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can terminate the workflow if a condition is met, which could be useful in certain scenarios of the inpainting workflow.

### Metadata
**Author:** SparknightLLC
**Repository:** [https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt](https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt)
**Install Type:** git-clone

---

### ComfyUI-Coziness

**Description:**

Nodes:MultiLora Loader, Lora Text Extractor. Provides a node for assisting in loading loras through text.

- **Author:** skfoo
- **Repository:** [https://github.com/skfoo/ComfyUI-Coziness](https://github.com/skfoo/ComfyUI-Coziness)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** ComfyUI-Coziness provides some utility as a supporting node by assisting in loading loras through text, but it"s not directly related to the inpainting workflow.

### Metadata
**Author:** skfoo
**Repository:** [https://github.com/skfoo/ComfyUI-Coziness](https://github.com/skfoo/ComfyUI-Coziness)
**Install Type:** git-clone

---

### ComfyUI-CreaPrompt

**Description:**

Generate random prompts easily.

- **Author:** Tritant
- **Repository:** [https://github.com/tritant/ComfyUI_CreaPrompt](https://github.com/tritant/ComfyUI_CreaPrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI-CreaPrompt is very useful for generating random prompts which could be helpful in an inpainting workflow with mask input.

### Metadata
**Author:** Tritant
**Repository:** [https://github.com/tritant/ComfyUI_CreaPrompt](https://github.com/tritant/ComfyUI_CreaPrompt)
**Install Type:** git-clone

---

### ComfyUI-CSV-Loader

**Description:**

CSV Loader for prompt building within ComfyUI interface. Allows access to positive/negative prompts associated with a name. Selections are being pulled from CSV files.

- **Author:** PCMonsterx
- **Repository:** [https://github.com/PCMonsterx/ComfyUI-CSV-Loader](https://github.com/PCMonsterx/ComfyUI-CSV-Loader)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI-CSV-Loader is essential for this workflow as it allows access to positive/negative prompts associated with a name from CSV files, which can be used to build and customize the inpainting process.

### Metadata
**Author:** PCMonsterx
**Repository:** [https://github.com/PCMonsterx/ComfyUI-CSV-Loader](https://github.com/PCMonsterx/ComfyUI-CSV-Loader)
**Install Type:** git-clone

---

### ComfyUI-CUP

**Description:**

Bridge between ComfyUI and blender's ComfyUI-BlenderAI-node addon.

- **Author:** AIGODLIKE
- **Repository:** [https://github.com/AIGODLIKE/ComfyUI-CUP](https://github.com/AIGODLIKE/ComfyUI-CUP)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is essential for bridging ComfyUI and blender"s ComfyUI-BlenderAI-node addon, which is crucial for an inpainting workflow with mask input.

### Metadata
**Author:** AIGODLIKE
**Repository:** [https://github.com/AIGODLIKE/ComfyUI-CUP](https://github.com/AIGODLIKE/ComfyUI-CUP)
**Install Type:** git-clone

---

### ComfyUI-CustomNodes

**Description:**

Nodes:Image Blending Mode Mask, Load Image With Bool, IPAdapter Mad Scientist Weight_Type, IPAdapter FaceID With Bool

- **Author:** wTechArtist
- **Repository:** [https://github.com/wTechArtist/ComfyUI-CustomNodes](https://github.com/wTechArtist/ComfyUI-CustomNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node contains custom nodes that might be useful in an inpainting workflow, but their relevance depends on the specific requirements of the task.

### Metadata
**Author:** wTechArtist
**Repository:** [https://github.com/wTechArtist/ComfyUI-CustomNodes](https://github.com/wTechArtist/ComfyUI-CustomNodes)
**Install Type:** git-clone

---

### ComfyUI-DataSet

**Description:**

Data research, preparation, and manipulation nodes for model trainers and artists.

- **Author:** daxcay
- **Repository:** [https://github.com/daxcay/ComfyUI-DataSet](https://github.com/daxcay/ComfyUI-DataSet)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides data research and manipulation capabilities which are essential for preparing and working with masks in an inpainting workflow.

### Metadata
**Author:** daxcay
**Repository:** [https://github.com/daxcay/ComfyUI-DataSet](https://github.com/daxcay/ComfyUI-DataSet)
**Install Type:** git-clone

---

### ComfyUI-DDUF

**Description:**

Run DDUF in ComfyUI - powered by Diffusers.

- **Author:** Vaibhavs10
- **Repository:** [https://github.com/Vaibhavs10/ComfyUI-DDUF](https://github.com/Vaibhavs10/ComfyUI-DDUF)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as DDUF can be used for image restoration and inpainting tasks.

### Metadata
**Author:** Vaibhavs10
**Repository:** [https://github.com/Vaibhavs10/ComfyUI-DDUF](https://github.com/Vaibhavs10/ComfyUI-DDUF)
**Install Type:** git-clone

---

### ComfyUI-deepcache

**Description:**

This extension provides nodes for [a/DeepCache: Accelerating Diffusion Models for Free](https://arxiv.org/abs/2312.00858)
NOTE:Original code can be found [a/here](https://gist.github.com/laksjdjf/435c512bc19636e9c9af4ee7bea9eb86). Full credit to laksjdjf for sharing the code. 

- **Author:** styler00dollar
- **Repository:** [https://github.com/styler00dollar/ComfyUI-deepcache](https://github.com/styler00dollar/ComfyUI-deepcache)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for accelerating diffusion models and can be used in conjunction with inpainting workflows, making it highly relevant.

### Metadata
**Author:** styler00dollar
**Repository:** [https://github.com/styler00dollar/ComfyUI-deepcache](https://github.com/styler00dollar/ComfyUI-deepcache)
**Install Type:** git-clone

---

### ComfyUI-DeepCache-Fix

**Description:**

Accelerate ComfyUI Nodes for Faster Image Generation, Ensuring Consistency Pre and Post-Acceleration, Ideal for Bulk Image Production.

- **Author:** SoftMeng
- **Repository:** [https://github.com/SoftMeng/ComfyUI-DeepCache-Fix](https://github.com/SoftMeng/ComfyUI-DeepCache-Fix)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is an extension of DeepCache that accelerates ComfyUI nodes for faster image generation, which aligns well with the inpainting workflow goal.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI-DeepCache-Fix](https://github.com/SoftMeng/ComfyUI-DeepCache-Fix)
**Install Type:** git-clone

---

### ComfyUI-denoise-mask-scheduler

**Description:**

ComfyUI-denoise-mask-scheduler experimental approach involves selectively applying a denoise mask at each step during the inpainting inference process in diffusion models.

- **Author:** MiddleKD
- **Repository:** [https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler](https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node selectively applies a denoise mask at each step during inpainting inference process making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** MiddleKD
**Repository:** [https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler](https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler)
**Install Type:** git-clone

---

### ComfyUI-Depth-Visualization

**Description:**

Works with any Depth Map and visualizes the applied version it inside ComfyUI

- **Author:** gokayfem
- **Repository:** [https://github.com/gokayfem/ComfyUI-Depth-Visualization](https://github.com/gokayfem/ComfyUI-Depth-Visualization)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Directly supports visualization of depth maps which is crucial for inpainting with mask input.

### Metadata
**Author:** gokayfem
**Repository:** [https://github.com/gokayfem/ComfyUI-Depth-Visualization](https://github.com/gokayfem/ComfyUI-Depth-Visualization)
**Install Type:** git-clone

---

### ComfyUI-DepthAnythingV2

**Description:**

ComfyUI nodes to use [a/DepthAnythingV2](https://depth-anything-v2.github.io/)
NOTE:Models autodownload to ComfyUI/models/depthanything from [a/https://huggingface.co/Kijai/DepthAnythingV2-safetensors/tree/main](https://huggingface.co/Kijai/DepthAnythingV2-safetensors/tree/main)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** Offers a pre-trained model for estimating depth from images, directly applicable to inpainting workflows with mask input.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2)
**Install Type:** git-clone

---

### ComfyUI-Detail-Daemon

**Description:**

A port of muerrilla's [a/sd-webui-Detail-Daemon](https://github.com/muerrilla/sd-webui-detail-daemon) as a node for ComfyUI, to adjust sigmas that control detail.

- **Author:** Jonseed
- **Repository:** [https://github.com/Jonseed/ComfyUI-Detail-Daemon](https://github.com/Jonseed/ComfyUI-Detail-Daemon)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node adjusts sigmas for detail control, its primary purpose seems unrelated to the specified inpainting workflow goal.

### Metadata
**Author:** Jonseed
**Repository:** [https://github.com/Jonseed/ComfyUI-Detail-Daemon](https://github.com/Jonseed/ComfyUI-Detail-Daemon)
**Install Type:** git-clone

---

### ComfyUI-Diffusers

**Description:**

This extension enables the use of the diffuser pipeline in ComfyUI. It also includes nodes related to Stream Diffusion.

- **Author:** Limitex
- **Repository:** [https://github.com/Limitex/ComfyUI-Diffusers](https://github.com/Limitex/ComfyUI-Diffusers)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides diffuser pipeline nodes and Stream Diffusion-related nodes, which are highly relevant for an inpainting workflow with mask input.

### Metadata
**Author:** Limitex
**Repository:** [https://github.com/Limitex/ComfyUI-Diffusers](https://github.com/Limitex/ComfyUI-Diffusers)
**Install Type:** git-clone

---

### ComfyUI-DiffusersImageOutpaint

**Description:**

ComfyUI nodes for outpainting images with diffusers, based on [a/diffusers-image-outpaint](https://huggingface.co/spaces/fffiloni/diffusers-image-outpaint/tree/main) by fffiloni.

- **Author:** GiusTex
- **Repository:** [https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint](https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for outpainting images with diffusers, making it very useful for the specified workflow goal.

### Metadata
**Author:** GiusTex
**Repository:** [https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint](https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint)
**Install Type:** git-clone

---

### ComfyUI-Documents

**Description:**

ComfyUI-Documents is a powerful extension for ComfyUI that enhances workflows with advanced document processing capabilities. It includes nodes for loading and parsing various document types (PDF, TXT, DOC, DOCX), converting PDF pages to images, splitting PDFs into individual pages, and selecting specific images from batches. Features include text extraction, image conversion, and seamless integration with existing ComfyUI projects.

- **Author:** Indra's Mirror
- **Repository:** [https://github.com/Excidos/ComfyUI-Documents](https://github.com/Excidos/ComfyUI-Documents)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides advanced document processing capabilities that can be used to load and parse various document types, including those that may contain masks or other relevant information for the inpainting workflow.

### Metadata
**Author:** Indra's Mirror
**Repository:** [https://github.com/Excidos/ComfyUI-Documents](https://github.com/Excidos/ComfyUI-Documents)
**Install Type:** git-clone

---

### ComfyUI-DrawThingsWrapper

**Description:**

These nodes provide a wrapper for calling Draw Things image generations from ComfyUI.
Wait, why? The Draw Things app has been optimized for Apple hardware and runs roughly x3 faster than ComfyUI generations. But ComfyUI is a flexible and powerful tools, and has some features - like queuing and face swapping - that haven't been implemented in Draw Things.

- **Author:** JosephThomasParker
- **Repository:** [https://github.com/JosephThomasParker/ComfyUI-DrawThingsWrapper](https://github.com/JosephThomasParker/ComfyUI-DrawThingsWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a wrapper for calling Draw Things image generations which can be used in conjunction with inpainting workflows.

### Metadata
**Author:** JosephThomasParker
**Repository:** [https://github.com/JosephThomasParker/ComfyUI-DrawThingsWrapper](https://github.com/JosephThomasParker/ComfyUI-DrawThingsWrapper)
**Install Type:** git-clone

---

### ComfyUI-dust3r

**Description:**

ComfyUI dust3r

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-dust3r](https://github.com/chaojie/ComfyUI-dust3r)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the inpainting workflow with mask input and can be used as a utility node to achieve the goal.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-dust3r](https://github.com/chaojie/ComfyUI-dust3r)
**Install Type:** git-clone

---

### ComfyUI-DynamiCrafterWrapper

**Description:**

Wrapper nodes to use DynamiCrafter image2video and frame interpolation models in ComfyUI
And this extension supports ToonCrafter as well

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-DynamiCrafterWrapper](https://github.com/kijai/ComfyUI-DynamiCrafterWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the inpainting workflow with mask input and provides a wrapper around DynamiCrafter models that can be used in the workflow.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-DynamiCrafterWrapper](https://github.com/kijai/ComfyUI-DynamiCrafterWrapper)
**Install Type:** git-clone

---

### comfyui-edit-mask

**Description:**

Nodes:Edit Mask

- **Author:** shadowcz007
- **Repository:** [https://github.com/shadowcz007/comfyui-edit-mask](https://github.com/shadowcz007/comfyui-edit-mask)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly provides functionality to edit masks which is essential for the specified workflow goal.

### Metadata
**Author:** shadowcz007
**Repository:** [https://github.com/shadowcz007/comfyui-edit-mask](https://github.com/shadowcz007/comfyui-edit-mask)
**Install Type:** git-clone

---

### ComfyUI-EfficientTAM

**Description:**

A ComfyUI implementation of [a/EfficientTAM](https://github.com/yformer/EfficientTAM)

- **Author:** RyanOnTheInside
- **Repository:** [https://github.com/ryanontheinside/ComfyUI_EfficientTAM](https://github.com/ryanontheinside/ComfyUI_EfficientTAM)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node implements EfficientTAM which can be used for inpainting tasks and is highly relevant to the specified workflow goal.

### Metadata
**Author:** RyanOnTheInside
**Repository:** [https://github.com/ryanontheinside/ComfyUI_EfficientTAM](https://github.com/ryanontheinside/ComfyUI_EfficientTAM)
**Install Type:** git-clone

---

### ComfyUI-ELLA-wrapper

**Description:**

ComfyUI wrapper nodes to use the Diffusers implementation of ELLA

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-ELLA-wrapper](https://github.com/kijai/ComfyUI-ELLA-wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is a wrapper for the Diffusers implementation of ELLA and seems directly relevant to the inpainting workflow with mask input, as it provides a way to use ELLA in ComfyUI.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-ELLA-wrapper](https://github.com/kijai/ComfyUI-ELLA-wrapper)
**Install Type:** git-clone

---

### comfyui-enhanced-save-node

**Description:**

Nodes:Enhanced Save Node

- **Author:** HebelHuber
- **Repository:** [https://github.com/HebelHuber/comfyui-enhanced-save-node](https://github.com/HebelHuber/comfyui-enhanced-save-node)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This enhanced save node can be useful for saving the inpainted image after processing it through other nodes in the workflow.

### Metadata
**Author:** HebelHuber
**Repository:** [https://github.com/HebelHuber/comfyui-enhanced-save-node](https://github.com/HebelHuber/comfyui-enhanced-save-node)
**Install Type:** git-clone

---

### Comfyui-ergouzi-samplers

**Description:**

Partial redraw sampler and variant seed sampler

- **Author:** 11dogzi
- **Repository:** [https://github.com/11dogzi/Comfyui-ergouzi-samplers](https://github.com/11dogzi/Comfyui-ergouzi-samplers)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides samplers which are useful in inpainting workflows for generating diverse results.

### Metadata
**Author:** 11dogzi
**Repository:** [https://github.com/11dogzi/Comfyui-ergouzi-samplers](https://github.com/11dogzi/Comfyui-ergouzi-samplers)
**Install Type:** git-clone

---

### ComfyUI-FaceChain

**Description:**

The official ComfyUI version of facechain greatly improves the speed of reasoning and has great custom process controls.

- **Author:** THtianhao
- **Repository:** [https://github.com/THtianhao/ComfyUI-FaceChain](https://github.com/THtianhao/ComfyUI-FaceChain)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it provides a face chain reasoning process that can be used in conjunction with inpainting techniques.

### Metadata
**Author:** THtianhao
**Repository:** [https://github.com/THtianhao/ComfyUI-FaceChain](https://github.com/THtianhao/ComfyUI-FaceChain)
**Install Type:** git-clone

---

### ComfyUI-FastSDCPU

**Description:**

A set of nodes for interfacing with the FastSDCPU webserver.

- **Author:** BetaDoggo
- **Repository:** [https://github.com/BetaDoggo/ComfyUI-FastSDCPU](https://github.com/BetaDoggo/ComfyUI-FastSDCPU)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a set of nodes for interfacing with the FastSDCPU webserver which could be useful in conjunction with the inpainting workflow.

### Metadata
**Author:** BetaDoggo
**Repository:** [https://github.com/BetaDoggo/ComfyUI-FastSDCPU](https://github.com/BetaDoggo/ComfyUI-FastSDCPU)
**Install Type:** git-clone

---

### comfyui-fb-utils

**Description:**

Nodes:FBStringJoin, FBStringSplit, FBMultilineStringList, FBMultilineString

- **Author:** FredBill1
- **Repository:** [https://github.com/FredBill1/comfyui-fb-utils](https://github.com/FredBill1/comfyui-fb-utils)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** These string manipulation nodes are marginally relevant to the inpainting workflow as they can be used to process input or output data but do not directly contribute to the inpainting task.

### Metadata
**Author:** FredBill1
**Repository:** [https://github.com/FredBill1/comfyui-fb-utils](https://github.com/FredBill1/comfyui-fb-utils)
**Install Type:** git-clone

---

### ComfyUI-FBCNN

**Description:**

A node for JPEG de-artifacting using [a/FBCNN](https://github.com/jiaxi-jiang/FBCNN).

- **Author:** miosp
- **Repository:** [https://github.com/Miosp/ComfyUI-FBCNN](https://github.com/Miosp/ComfyUI-FBCNN)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a JPEG de-artifacting function which is very useful for preprocessing images before inpainting and could significantly improve the quality of the final result.

### Metadata
**Author:** miosp
**Repository:** [https://github.com/Miosp/ComfyUI-FBCNN](https://github.com/Miosp/ComfyUI-FBCNN)
**Install Type:** git-clone

---

### ComfyUI-FilePathCreator

**Description:**

The ComfyUI-FilePathCreator is a custom node extension for ComfyUI designed to generate dynamic filenames based on user-defined parameters. This node helps streamline the process of creating organized and timestamped filenames, ideal for saving output files in a structured manner.

- **Author:** HECer
- **Repository:** [https://github.com/HECer/ComfyUI-FilePathCreator](https://github.com/HECer/ComfyUI-FilePathCreator)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for organizing and timestamping filenames in the inpainting workflow with mask input.

### Metadata
**Author:** HECer
**Repository:** [https://github.com/HECer/ComfyUI-FilePathCreator](https://github.com/HECer/ComfyUI-FilePathCreator)
**Install Type:** git-clone

---

### ComfyUI-Fill-Image-for-Outpainting

**Description:**

This node is to fill image for outpainting(inpainting)
Fill image using cv2 methods(cv2_ns, cv2_telea and edge_pad)

- **Author:** hyejinlee12
- **Repository:** [https://github.com/Lhyejin/ComfyUI-Fill-Image-for-Outpainting](https://github.com/Lhyejin/ComfyUI-Fill-Image-for-Outpainting)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for filling images in outpainting (inpainting) tasks within the specified workflow goal.

### Metadata
**Author:** hyejinlee12
**Repository:** [https://github.com/Lhyejin/ComfyUI-Fill-Image-for-Outpainting](https://github.com/Lhyejin/ComfyUI-Fill-Image-for-Outpainting)
**Install Type:** git-clone

---

### comfyui-fitsize

**Description:**

Nodes:Fit Size From Int/Image/Resize, Load Image And Resize To Fit, Pick Image From Batch/List, Crop Image Into Even Pieces, Image Region To Mask... A simple set of nodes for making an image fit within a bounding box

- **Author:** bronkula
- **Repository:** [https://github.com/bronkula/comfyui-fitsize](https://github.com/bronkula/comfyui-fitsize)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides functionality for resizing images which could be useful in preparing the mask input for the inpainting workflow.

### Metadata
**Author:** bronkula
**Repository:** [https://github.com/bronkula/comfyui-fitsize](https://github.com/bronkula/comfyui-fitsize)
**Install Type:** git-clone

---

### ComfyUI-FJDH

**Description:**

bbox tools, image tools, mask generators, point tools

- **Author:** riverolls
- **Repository:** [https://github.com/riverolls/ComfyUI-FJDH](https://github.com/riverolls/ComfyUI-FJDH)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has a broad set of tools but none specifically related to image inpainting or mask input, making it marginally relevant at best.

### Metadata
**Author:** riverolls
**Repository:** [https://github.com/riverolls/ComfyUI-FJDH](https://github.com/riverolls/ComfyUI-FJDH)
**Install Type:** git-clone

---

### ComfyUI-Florence-2

**Description:**

[a/https://huggingface.co/microsoft/Florence-2-large-ft](https://huggingface.co/microsoft/Florence-2-large-ft)
Large or base model, support for captioning and bbox task modes, more coming soon.

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a Vision-Language Model (VLM) specifically designed for image vision tasks including inpainting with mask input.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2)
**Install Type:** git-clone

---

### ComfyUI-Florence2

**Description:**

Nodes to use Florence2 VLM for image vision tasks: object detection, captioning, segmentation and ocr

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a VLM that supports object detection, captioning, segmentation and ocr which are all relevant to the inpainting workflow with mask input.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)
**Install Type:** git-clone

---

### ComfyUI-FlowChain

**Description:**

Convert your workflows into node and chain them.

- **Author:** NumZ
- **Repository:** [https://github.com/numz/Comfyui-FlowChain](https://github.com/numz/Comfyui-FlowChain)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node can convert workflows into nodes and chains, it is not directly relevant to the specific task of inpainting with mask input.

### Metadata
**Author:** NumZ
**Repository:** [https://github.com/numz/Comfyui-FlowChain](https://github.com/numz/Comfyui-FlowChain)
**Install Type:** git-clone

---

### ComfyUI-Flowty-CRM

**Description:**

This is a custom node that lets you use Convolutional Reconstruction Models right from ComfyUI.
[a/CRM](https://ml.cs.tsinghua.edu.cn/~zhengyi/CRM/) is a high-fidelity feed-forward single image-to-3D generative model.

- **Author:** flowtyone
- **Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-CRM](https://github.com/flowtyone/ComfyUI-Flowty-CRM)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a high-fidelity feed-forward single image-to-3D generative model that can be used directly in ComfyUI, making it very useful for inpainting with mask input.

### Metadata
**Author:** flowtyone
**Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-CRM](https://github.com/flowtyone/ComfyUI-Flowty-CRM)
**Install Type:** git-clone

---

### ComfyUI-Flowty-LDSR

**Description:**

This is a custom node that lets you take advantage of Latent Diffusion Super Resolution (LDSR) models inside ComfyUI.

- **Author:** flowtyone
- **Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-LDSR](https://github.com/flowtyone/ComfyUI-Flowty-LDSR)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node uses Latent Diffusion Super Resolution models inside ComfyUI, which can be moderately useful for inpainting with mask input, but might not produce the best results compared to other options.

### Metadata
**Author:** flowtyone
**Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-LDSR](https://github.com/flowtyone/ComfyUI-Flowty-LDSR)
**Install Type:** git-clone

---

### ComfyUI-Flowty-TripoSR

**Description:**

This is a custom node that lets you use TripoSR right from ComfyUI.
[a/TripoSR](https://github.com/VAST-AI-Research/TripoSR) is a state-of-the-art open-source model for fast feedforward 3D reconstruction from a single image, collaboratively developed by Tripo AI and Stability AI. (TL;DR it creates a 3d model from an image.)

- **Author:** flowtyone
- **Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-TripoSR](https://github.com/flowtyone/ComfyUI-Flowty-TripoSR)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node is a state-of-the-art open-source model for fast feedforward 3D reconstruction from a single image, but its primary use case is creating 3D models from images, making it marginally relevant for inpainting with mask input.

### Metadata
**Author:** flowtyone
**Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-TripoSR](https://github.com/flowtyone/ComfyUI-Flowty-TripoSR)
**Install Type:** git-clone

---

### ComfyUI-Flux-Inpainting

**Description:**

This node wraps the flux fill model as ComfyUI nodes. Use NF4 flux fill model, support for inpainting and outpainting image. Compared to the flux fill dev model, these nodes can use the flux fill model to perform inpainting and outpainting work under lower VRM conditions.

- **Author:** duhaifeng
- **Repository:** [https://github.com/rubi-du/ComfyUI-Flux-Inpainting](https://github.com/rubi-du/ComfyUI-Flux-Inpainting)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports inpainting work under lower VRM conditions using the NF4 flux fill model.

### Metadata
**Author:** duhaifeng
**Repository:** [https://github.com/rubi-du/ComfyUI-Flux-Inpainting](https://github.com/rubi-du/ComfyUI-Flux-Inpainting)
**Install Type:** git-clone

---

### ComfyUI-FluxExt-MZ

**Description:**

Nodes:MZ_Flux1PartialLoad_Patch. Tool nodes related to flux1

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ](https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node appears to be related to Flux and has tool nodes that could support the inpainting workflow.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ](https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ)
**Install Type:** git-clone

---

### ComfyUI-Fluxtapoz

**Description:**

ComfyUI nodes for image editing with Flux, such as RF-Inversion and more

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-Fluxtapoz](https://github.com/logtd/ComfyUI-Fluxtapoz)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a collection of image editing nodes but its description does not specifically mention inpainting or mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-Fluxtapoz](https://github.com/logtd/ComfyUI-Fluxtapoz)
**Install Type:** git-clone

---

### comfyui-fofr-toolkit

**Description:**

Nodes:Incrementer, Width and height from aspect ratio, Width and height for scaling image to ideal resolutio. A simple set of tooling nodes.

- **Author:** fofr
- **Repository:** [https://github.com/fofr/comfyui-fofr-toolkit](https://github.com/fofr/comfyui-fofr-toolkit)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides utility nodes such as incrementer and aspect ratio calculator which could be useful in preparing the mask for inpainting.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/fofr/comfyui-fofr-toolkit](https://github.com/fofr/comfyui-fofr-toolkit)
**Install Type:** git-clone

---

### ComfyUI-FrameFX

**Description:**

A set of custom nodes for frame interpolation and video processing in ComfyUI.

- **Author:** mgfxer
- **Repository:** [https://github.com/mgfxer/ComfyUI-FrameFX](https://github.com/mgfxer/ComfyUI-FrameFX)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** A set of custom nodes for frame interpolation and video processing in ComfyUI makes it very useful for the specified workflow goal.

### Metadata
**Author:** mgfxer
**Repository:** [https://github.com/mgfxer/ComfyUI-FrameFX](https://github.com/mgfxer/ComfyUI-FrameFX)
**Install Type:** git-clone

---

### ComfyUI-FreeMemory

**Description:**

ComfyUI-FreeMemory is a custom node extension for ComfyUI that provides advanced memory management capabilities within your image generation workflows. It aims to help prevent out-of-memory errors and optimize resource usage during complex operations.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-FreeMemory](https://github.com/ShmuelRonen/ComfyUI-FreeMemory)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** ComfyUI-FreeMemory provides advanced memory management capabilities, but its direct utility for the specified workflow goal is moderate.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-FreeMemory](https://github.com/ShmuelRonen/ComfyUI-FreeMemory)
**Install Type:** git-clone

---

### ComfyUI-GCP-Storage

**Description:**

Node:GCP Storage Node. Support google-cloud-storage.

- **Author:** Fantaxico
- **Repository:** [https://github.com/Fantaxico/ComfyUI-GCP-Storage](https://github.com/Fantaxico/ComfyUI-GCP-Storage)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node supports Google Cloud Storage, which could potentially store and retrieve images for inpainting, but it is not directly related to the task.

### Metadata
**Author:** Fantaxico
**Repository:** [https://github.com/Fantaxico/ComfyUI-GCP-Storage](https://github.com/Fantaxico/ComfyUI-GCP-Storage)
**Install Type:** git-clone

---

### ComfyUI-GCP_Storage_tools

**Description:**

A set of ComfyUI nodes for GPC Storage access

- **Author:** ahernandezmiro
- **Repository:** [https://github.com/ahernandezmiro/ComfyUI-GCP_Storage_tools](https://github.com/ahernandezmiro/ComfyUI-GCP_Storage_tools)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides a set of tools for GCP Storage access, which could be useful for storing and retrieving images for inpainting, but its direct relevance to the task is still limited.

### Metadata
**Author:** ahernandezmiro
**Repository:** [https://github.com/ahernandezmiro/ComfyUI-GCP_Storage_tools](https://github.com/ahernandezmiro/ComfyUI-GCP_Storage_tools)
**Install Type:** git-clone

---

### ComfyUI-GeekyRemB

**Description:**

GeekyRemB is a powerful and versatile image processing node for ComfyUI, designed to remove backgrounds from images with advanced customization options. This node leverages the rembg library and offers a wide range of features for fine-tuning the background removal process and enhancing the resulting images.

- **Author:** GeekyGhost
- **Repository:** [https://github.com/GeekyGhost/ComfyUI-GeekyRemB](https://github.com/GeekyGhost/ComfyUI-GeekyRemB)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to the inpainting workflow with mask input as it can remove backgrounds from images.

### Metadata
**Author:** GeekyGhost
**Repository:** [https://github.com/GeekyGhost/ComfyUI-GeekyRemB](https://github.com/GeekyGhost/ComfyUI-GeekyRemB)
**Install Type:** git-clone

---

### ComfyUI-GG

**Description:**

ComfyUI-GG is a collection of ComfyUI nodes designed to enhance productivity in image processing workflows. This plugin provides a set of custom nodes that perform various image manipulations and metadata extractions to streamline your tasks.

- **Author:** leestuartx
- **Repository:** [https://github.com/leestuartx/ComfyUI-GG](https://github.com/leestuartx/ComfyUI-GG)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is a collection of image processing nodes and provides metadata extractions, which are directly relevant to an inpainting workflow with mask input.

### Metadata
**Author:** leestuartx
**Repository:** [https://github.com/leestuartx/ComfyUI-GG](https://github.com/leestuartx/ComfyUI-GG)
**Install Type:** git-clone

---

### ComfyUI-GIMM-VFI

**Description:**

ComfyUI nodes to use GIMM-VFI frame interpolation

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-GIMM-VFI](https://github.com/kijai/ComfyUI-GIMM-VFI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports frame interpolation for video inpainting, making it very useful and essential for this workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-GIMM-VFI](https://github.com/kijai/ComfyUI-GIMM-VFI)
**Install Type:** git-clone

---

### ComfyUI-Golden-Noise

**Description:**

ComfyUI Custom Node for 'Golden Noise for Diffusion Models: A Learning Framework'. This node refines the initial latent noise in the diffusion process, enhancing both image quality and semantic coherence.

- **Author:** LucipherDev
- **Repository:** [https://github.com/LucipherDev/ComfyUI-Golden-Noise](https://github.com/LucipherDev/ComfyUI-Golden-Noise)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node refines initial latent noise in the diffusion process, which can enhance image quality and coherence in inpainting workflows with mask input.

### Metadata
**Author:** LucipherDev
**Repository:** [https://github.com/LucipherDev/ComfyUI-Golden-Noise](https://github.com/LucipherDev/ComfyUI-Golden-Noise)
**Install Type:** git-clone

---

### ComfyUI-graphToPrompt

**Description:**

workflow.json -> workflow_api.json

- **Author:** nat-chan
- **Repository:** [https://github.com/nat-chan/ComfyUI-graphToPrompt](https://github.com/nat-chan/ComfyUI-graphToPrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node converts a workflow graph into a prompt, which could be useful for generating the inpainting mask input.

### Metadata
**Author:** nat-chan
**Repository:** [https://github.com/nat-chan/ComfyUI-graphToPrompt](https://github.com/nat-chan/ComfyUI-graphToPrompt)
**Install Type:** git-clone

---

### ComfyUI-HaiperAI-API

**Description:**

Haiper API official ComfyUI custom node.

- **Author:** tuohe
- **Repository:** [https://github.com/Haiper-ai/ComfyUI-HaiperAI-API](https://github.com/Haiper-ai/ComfyUI-HaiperAI-API)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it provides an official API integration.

### Metadata
**Author:** tuohe
**Repository:** [https://github.com/Haiper-ai/ComfyUI-HaiperAI-API](https://github.com/Haiper-ai/ComfyUI-HaiperAI-API)
**Install Type:** git-clone

---

### ComfyUI-HakuImg

**Description:**

Image processing tool for ComfyUI

- **Author:** licyk
- **Repository:** [https://github.com/licyk/ComfyUI-HakuImg](https://github.com/licyk/ComfyUI-HakuImg)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is essential for the inpainting workflow with mask input as it offers image processing capabilities.

### Metadata
**Author:** licyk
**Repository:** [https://github.com/licyk/ComfyUI-HakuImg](https://github.com/licyk/ComfyUI-HakuImg)
**Install Type:** git-clone

---

### ComfyUI-Hangover-Nodes

**Description:**

Nodes: MS kosmos-2 Interrogator, Save Image w/o Metadata, Image Scale Bounding Box. An implementation of Microsoft [a/kosmos-2](https://huggingface.co/microsoft/kosmos-2-patch14-224) image to text transformer.

- **Author:** Hangover3832
- **Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Nodes](https://github.com/Hangover3832/ComfyUI-Hangover-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains various image processing nodes but none of them are specifically designed for inpainting with a mask input.

### Metadata
**Author:** Hangover3832
**Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Nodes](https://github.com/Hangover3832/ComfyUI-Hangover-Nodes)
**Install Type:** git-clone

---

### ComfyUI-HfLoader

**Description:**

Nodes:Lora Loader From HF

- **Author:** olduvai-jp
- **Repository:** [https://github.com/olduvai-jp/ComfyUI-HfLoader](https://github.com/olduvai-jp/ComfyUI-HfLoader)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can load models from Hugging Face repositories, which could be useful for loading pre-trained models for inpainting tasks.

### Metadata
**Author:** olduvai-jp
**Repository:** [https://github.com/olduvai-jp/ComfyUI-HfLoader](https://github.com/olduvai-jp/ComfyUI-HfLoader)
**Install Type:** git-clone

---

### ComfyUI-HH-Image-Selector

**Description:**

comfy ui custom node that returns an image from a batch based on selected criteria such as RGB value, brightness, etc (credits to chris goringe's custom nodes tutorial ).

- **Author:** haohaocreates
- **Repository:** [https://github.com/haohaocreates/ComfyUI-HH-Image-Selector](https://github.com/haohaocreates/ComfyUI-HH-Image-Selector)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node is not directly related to inpainting, it could potentially be used as a supporting node to select images based on certain criteria, but its relevance is marginal.

### Metadata
**Author:** haohaocreates
**Repository:** [https://github.com/haohaocreates/ComfyUI-HH-Image-Selector](https://github.com/haohaocreates/ComfyUI-HH-Image-Selector)
**Install Type:** git-clone

---

### ComfyUI-HunyuanImageLatentToVideoLatent

**Description:**

A ComfyUI node which copies a given latent's samples tensor along the time axis ((length - 1) // 4) + 1 times to form a longer latent (see EmptyHunyuanLatentVideo's implementation for why this specific number of copies is used) and then prepares a noise_mask tensor of the same shape such that the value of the mask for a given time step is given by the function at https://www.desmos.com/calculator/vhw74mr1vh.

- **Author:** philiprodriguez
- **Repository:** [https://github.com/philiprodriguez/ComfyUI-HunyuanImageLatentToVideoLatent](https://github.com/philiprodriguez/ComfyUI-HunyuanImageLatentToVideoLatent)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node modifies latent tensors but its purpose seems unrelated to the direct goal of inpainting with a mask. It may be useful in other parts of the workflow.

### Metadata
**Author:** philiprodriguez
**Repository:** [https://github.com/philiprodriguez/ComfyUI-HunyuanImageLatentToVideoLatent](https://github.com/philiprodriguez/ComfyUI-HunyuanImageLatentToVideoLatent)
**Install Type:** git-clone

---

### ComfyUI-HunyuanVideoMultiLora

**Description:**

A custom LoRA-loading node designed to prevent issues such as blurriness and other artifacts when loading multiple LoRAs in HunYuan Video.
Usage Instructions: The connection method remains unchanged from the original. The only difference is the additional blocks_type option. Please select double_blocks.

- **Author:** facok
- **Repository:** [https://github.com/facok/ComfyUI-HunyuanVideoMultiLora](https://github.com/facok/ComfyUI-HunyuanVideoMultiLora)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node addresses a common issue in loading multiple LoRAs, which could be relevant when working with complex video inputs for inpainting.

### Metadata
**Author:** facok
**Repository:** [https://github.com/facok/ComfyUI-HunyuanVideoMultiLora](https://github.com/facok/ComfyUI-HunyuanVideoMultiLora)
**Install Type:** git-clone

---

### ComfyUI-HyperSDXL1StepUnetScheduler (ByteDance)

**Description:**

Original author is ByteDance.
ComfyUI sampler for HyperSDXL UNet
Ported from: [a/https://huggingface.co/ByteDance/Hyper-SD](https://huggingface.co/ByteDance/Hyper-SD)

- **Author:** fofr
- **Repository:** [https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler](https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a scheduler specifically designed for HyperSDXL UNet, which can be used in an inpainting workflow with mask input.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler](https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler)
**Install Type:** git-clone

---

### ComfyUI-I2VGEN-XL

**Description:**

This is an implementation of [a/i2vgen-xl](https://github.com/ali-vilab/i2vgen-xl)

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-I2VGEN-XL](https://github.com/chaojie/ComfyUI-I2VGEN-XL)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node implements i2vgen-xl, which can be used in image-to-video tasks and may have applications in inpainting workflows, especially when dealing with video inputs or outputs.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-I2VGEN-XL](https://github.com/chaojie/ComfyUI-I2VGEN-XL)
**Install Type:** git-clone

---

### ComfyUI-IC-Light-Native

**Description:**

ComfyUI native implementation of [a/IC-Light](https://github.com/lllyasviel/IC-Light).

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI-IC-Light-Native](https://github.com/huchenlei/ComfyUI-IC-Light-Native)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a direct implementation of IC-Light which can be used for inpainting tasks with mask input.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI-IC-Light-Native](https://github.com/huchenlei/ComfyUI-IC-Light-Native)
**Install Type:** git-clone

---

### ComfyUI-IF_MemoAvatar

**Description:**

ComfyUI MemoAvatar is a talking head avatar generator using Memory-Guided Diffusion for Expressive Talking Video Generation

- **Author:** if-ai
- **Repository:** [https://github.com/if-ai/ComfyUI-IF_MemoAvatar](https://github.com/if-ai/ComfyUI-IF_MemoAvatar)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node generates talking head avatars but its primary focus is on expressive video generation rather than inpainting with mask input.

### Metadata
**Author:** if-ai
**Repository:** [https://github.com/if-ai/ComfyUI-IF_MemoAvatar](https://github.com/if-ai/ComfyUI-IF_MemoAvatar)
**Install Type:** git-clone

---

### ComfyUI-IG-Motion-I2V

**Description:**

ComfyUI adaptation of https://github.com/G-U-N/Motion-I2V

- **Author:** IDGallagher
- **Repository:** [https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V](https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can decode images from SLAT representation and supports Rectified Flow Transformers.

### Metadata
**Author:** IDGallagher
**Repository:** [https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V](https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V)
**Install Type:** git-clone

---

### ComfyUI-Image-Evaluation

**Description:**

An extension to ComfyUI that evaluates images using multiple models.

- **Author:** wu12023
- **Repository:** [https://github.com/wu12023/ComfyUI-Image-Evaluation](https://github.com/wu12023/ComfyUI-Image-Evaluation)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can be marginally useful in evaluating the quality of inpainted images but may require additional processing steps.

### Metadata
**Author:** wu12023
**Repository:** [https://github.com/wu12023/ComfyUI-Image-Evaluation](https://github.com/wu12023/ComfyUI-Image-Evaluation)
**Install Type:** git-clone

---

### ComfyUI-Image-Filters

**Description:**

Image and matte filtering nodes for ComfyUI `image/filters/*`

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for applying filters to inpainted images and adjusting their appearance as needed.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)
**Install Type:** git-clone

---

### ComfyUI-Image-Inpainting

**Description:**

Nodes:VAE Encode Inpaint, VAE Decode Inpaint, ColorCorrection Inpaint, ImagePreprocess Inpaint, ImagePostprocess Inpaint, Load Model Inpaint, Inpainting (using Model)

- **Author:** SherryXieYuchen
- **Repository:** [https://github.com/SherryXieYuchen/ComfyUI-Image-Inpainting](https://github.com/SherryXieYuchen/ComfyUI-Image-Inpainting)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to the inpainting workflow with mask input.

### Metadata
**Author:** SherryXieYuchen
**Repository:** [https://github.com/SherryXieYuchen/ComfyUI-Image-Inpainting](https://github.com/SherryXieYuchen/ComfyUI-Image-Inpainting)
**Install Type:** git-clone

---

### ComfyUI-Image-Matting

**Description:**

This node improves the quality of the image mask. more suitable for image composite matting

- **Author:** hackkhai
- **Repository:** [https://github.com/hackkhai/ComfyUI-Image-Matting](https://github.com/hackkhai/ComfyUI-Image-Matting)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not specifically designed for inpainting, this node can improve the quality of image masks which are crucial for inpainting workflows.

### Metadata
**Author:** hackkhai
**Repository:** [https://github.com/hackkhai/ComfyUI-Image-Matting](https://github.com/hackkhai/ComfyUI-Image-Matting)
**Install Type:** git-clone

---

### ComfyUI-Image-Tools

**Description:**

Nodes:BatchImageResizeProcessor, SingleImagePathLoader, SingleImageUrlLoader

- **Author:** knuknX
- **Repository:** [https://github.com/knuknX/ComfyUI-Image-Tools](https://github.com/knuknX/ComfyUI-Image-Tools)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains multiple tools that can be useful in preparing images for inpainting, such as resizing and loading.

### Metadata
**Author:** knuknX
**Repository:** [https://github.com/knuknX/ComfyUI-Image-Tools](https://github.com/knuknX/ComfyUI-Image-Tools)
**Install Type:** git-clone

---

### ComfyUI-ImageCropper

**Description:**

Nodes:Image cropping tool

- **Author:** Auttasak-L
- **Repository:** [https://github.com/Auttasak-L/ComfyUI-ImageCropper](https://github.com/Auttasak-L/ComfyUI-ImageCropper)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node may be marginally relevant if the image needs to be cropped before inpainting, but it is not directly related to the workflow goal.

### Metadata
**Author:** Auttasak-L
**Repository:** [https://github.com/Auttasak-L/ComfyUI-ImageCropper](https://github.com/Auttasak-L/ComfyUI-ImageCropper)
**Install Type:** git-clone

---

### ComfyUI-Img2DrawingAssistants

**Description:**

These are ComfyUI nodes to assist in converting an image to sketches or lineArts.

- **Author:** Isi-dev
- **Repository:** [https://github.com/Isi-dev/ComfyUI-Img2DrawingAssistants](https://github.com/Isi-dev/ComfyUI-Img2DrawingAssistants)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can assist in converting an image to sketches or lineArts but does not directly contribute to inpainting with a mask.

### Metadata
**Author:** Isi-dev
**Repository:** [https://github.com/Isi-dev/ComfyUI-Img2DrawingAssistants](https://github.com/Isi-dev/ComfyUI-Img2DrawingAssistants)
**Install Type:** git-clone

---

### ComfyUI-Img2Img-Turbo

**Description:**

ComfyUI Img2Img-Turbo

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-Img2Img-Turbo](https://github.com/chaojie/ComfyUI-Img2Img-Turbo)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly supports inpainting with mask input.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Img2Img-Turbo](https://github.com/chaojie/ComfyUI-Img2Img-Turbo)
**Install Type:** git-clone

---

### ComfyUI-ImgMask2PNG

**Description:**

NODES:ImageMask2PNG

- **Author:** freelifehacker
- **Repository:** [https://github.com/freelifehacker/ComfyUI-ImgMask2PNG](https://github.com/freelifehacker/ComfyUI-ImgMask2PNG)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Directly supports converting an image mask to PNG format, useful for inpainting workflows.

### Metadata
**Author:** freelifehacker
**Repository:** [https://github.com/freelifehacker/ComfyUI-ImgMask2PNG](https://github.com/freelifehacker/ComfyUI-ImgMask2PNG)
**Install Type:** git-clone

---

### Comfyui-In-Context-Lora-Utils

**Description:**

NODES: Add Mask For IC Lora, Create Context Window, Concatenate Context Window, Auto Patch

- **Author:** lrzjason
- **Repository:** [https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils](https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a set of utilities that can be used to prepare the mask input for the inpainting workflow.

### Metadata
**Author:** lrzjason
**Repository:** [https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils](https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils)
**Install Type:** git-clone

---

### ComfyUI-Inpaint-CropAndStitch

**Description:**

'✂️ Inpaint Crop' is a node that crops an image before sampling. The context area can be specified via the mask, expand pixels and expand factor or via a separate (optional) mask.
'✂️ Inpaint Stitch' is a node that stitches the inpainted image back into the original image without altering unmasked areas.

- **Author:** lquesada
- **Repository:** [https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for inpainting workflows with mask input and offers both cropping and stitching functionality.

### Metadata
**Author:** lquesada
**Repository:** [https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch)
**Install Type:** git-clone

---

### ComfyUI-InpaintEasy

**Description:**

InpaintEasy is a set of optimized local repainting (Inpaint) nodes that provide a simpler and more powerful local repainting workflow. It makes local repainting work easier and more efficient with intelligent cropping and merging functions.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-InpaintEasy](https://github.com/CY-CHENYUE/ComfyUI-InpaintEasy)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node provides optimized local repainting nodes that can be used to simplify and improve the efficiency of the inpainting workflow.

### Metadata
**Author:** CY-CHENYUE
**Repository:** [https://github.com/CY-CHENYUE/ComfyUI-InpaintEasy](https://github.com/CY-CHENYUE/ComfyUI-InpaintEasy)
**Install Type:** git-clone

---

### ComfyUI-InstantIDUtils

**Description:**

Nodes:Multi-ControlNet Converter, List of Images, Convert PIL to Tensor (NHWC), Convert Tensor (NHWC) to (NCHW), Convert Tensor (NHWC) to PIL

- **Author:** BXYMartin
- **Repository:** [https://github.com/BXYMartin/ComfyUI-InstantIDUtils](https://github.com/BXYMartin/ComfyUI-InstantIDUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node offers several utility functions that can be used to prepare images for the inpainting workflow, such as tensor conversions and PIL handling.

### Metadata
**Author:** BXYMartin
**Repository:** [https://github.com/BXYMartin/ComfyUI-InstantIDUtils](https://github.com/BXYMartin/ComfyUI-InstantIDUtils)
**Install Type:** git-clone

---

### ComfyUI-Interactive

**Description:**

Nodes that allow making the UI interactive, with selectors and switches. Enables selecting across multiple options with the click of a button to move a workflow forward.

- **Author:** lquesada
- **Repository:** [https://github.com/lquesada/ComfyUI-Interactive](https://github.com/lquesada/ComfyUI-Interactive)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows making the UI interactive, which can be useful for selecting options and moving the workflow forward in an inpainting task.

### Metadata
**Author:** lquesada
**Repository:** [https://github.com/lquesada/ComfyUI-Interactive](https://github.com/lquesada/ComfyUI-Interactive)
**Install Type:** git-clone

---

### ComfyUI-IP_LAP

**Description:**

Nodes:IP_LAP Node, Video Loader, PreView Video, Combine Audio Video. the comfyui custom node of [a/IP_LAP](https://github.com/Weizhi-Zhong/IP_LAP) to make audio driven videos!

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-IP_LAP](https://github.com/AIFSH/ComfyUI-IP_LAP)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node seems to be a custom implementation of the IP_LAP model for video editing, which could be useful for inpainting tasks that involve audio-driven videos.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-IP_LAP](https://github.com/AIFSH/ComfyUI-IP_LAP)
**Install Type:** git-clone

---

### ComfyUI-IPAdapter-Flux

**Description:**

NODES:Load IPAdapter Flux Model, Apply IPAdapter Flux Model

- **Author:** Shakker-Labs
- **Repository:** [https://github.com/Shakker-Labs/ComfyUI-IPAdapter-Flux](https://github.com/Shakker-Labs/ComfyUI-IPAdapter-Flux)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly loads and applies IPAdapter Flux Model, making it essential for the inpainting workflow with mask input.

### Metadata
**Author:** Shakker-Labs
**Repository:** [https://github.com/Shakker-Labs/ComfyUI-IPAdapter-Flux](https://github.com/Shakker-Labs/ComfyUI-IPAdapter-Flux)
**Install Type:** git-clone

---

### ComfyUI-IPAnimate

**Description:**

This is a project that generates videos frame by frame based on IPAdapter+ControlNet. Unlike [a/Steerable-motion](https://github.com/banodoco/Steerable-Motion), we do not rely on AnimateDiff. This decision is primarily due to the fact that the videos generated by AnimateDiff are often blurry. Through frame-by-frame control using IPAdapter+ControlNet, we can produce higher definition and more controllable videos.

- **Author:** Chan-0312
- **Repository:** [https://github.com/Chan-0312/ComfyUI-IPAnimate](https://github.com/Chan-0312/ComfyUI-IPAnimate)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Generates videos frame by frame based on IPAdapter+ControlNet, but its primary focus is video generation rather than inpainting.

### Metadata
**Author:** Chan-0312
**Repository:** [https://github.com/Chan-0312/ComfyUI-IPAnimate](https://github.com/Chan-0312/ComfyUI-IPAnimate)
**Install Type:** git-clone

---

### ComfyUI-J

**Description:**

This is a completely different set of nodes than Comfy's own KSampler series. This set of nodes is based on Diffusers, which makes it easier to import models, apply prompts with weights, inpaint, reference only, controlnet, etc.

- **Author:** Jannchie
- **Repository:** [https://github.com/Jannchie/ComfyUI-J](https://github.com/Jannchie/ComfyUI-J)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for Diffusers-based workflows, making it highly relevant to the inpainting task with mask input.

### Metadata
**Author:** Jannchie
**Repository:** [https://github.com/Jannchie/ComfyUI-J](https://github.com/Jannchie/ComfyUI-J)
**Install Type:** git-clone

---

### ComfyUI-JakeUpgrade

**Description:**

A ComfyUI workflow customization by Jake.

- **Author:** jakechai
- **Repository:** [https://github.com/jakechai/ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not as directly related to inpainting as ComfyUI-J, this customization offers various workflow enhancements that could be useful in supporting the inpainting goal.

### Metadata
**Author:** jakechai
**Repository:** [https://github.com/jakechai/ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade)
**Install Type:** git-clone

---

### ComfyUI-JDCN

**Description:**

Jerry Davos Custom Nodes for Saving Latents in Directory (BatchLatentSave) , Importing Latent from directory (BatchLatentLoadFromDir) , List to string, string to list, get any file list from directory which give filepath, filename, move any files from any directory to any other directory, VHS Video combine file mover, rebatch list of strings, batch image load from any dir, load image batch from any directory and other custom nodes.

- **Author:** daxcay
- **Repository:** [https://github.com/daxcay/ComfyUI-JDCN](https://github.com/daxcay/ComfyUI-JDCN)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** While this collection of nodes offers various utility functions, its primary purpose seems to be focused on automation and directory management rather than inpainting or image processing tasks.

### Metadata
**Author:** daxcay
**Repository:** [https://github.com/daxcay/ComfyUI-JDCN](https://github.com/daxcay/ComfyUI-JDCN)
**Install Type:** git-clone

---

### comfyui-jk-easy-nodes

**Description:**

NODES: EasyHRFix, EasyHRFix_Context, JKAnythingToString, JKBigContext, JKDynamicThresholdingMultiModel, JKEasyCheckpointLoader, JKEasyDetailer, JKEasyDetailer_Context, JKEasyKSampler_Context, JKEasyWatermark, JKInspireSchedulerAdapter, JKLilContext, JKMultiModelSamplerUnpatch, JKStringEmpty, JKStringEquals, JKStringNotEmpty, JKStringNotEquals, JKStringToSamplerAdapter

- **Author:** kostenickj
- **Repository:** [https://github.com/kostenickj/jk-comfyui-helpers](https://github.com/kostenickj/jk-comfyui-helpers)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a set of easy-to-use nodes that can be useful for various tasks in the inpainting workflow, such as fixing HR issues and dynamic thresholding.

### Metadata
**Author:** kostenickj
**Repository:** [https://github.com/kostenickj/jk-comfyui-helpers](https://github.com/kostenickj/jk-comfyui-helpers)
**Install Type:** git-clone

---

### ComfyUI-JMESPath

**Description:**

A ComfyUI node that runs a [a/JMESPath](https://jmespath.org/) query against input JSON and outputs the result.

- **Author:** gremlation
- **Repository:** [https://github.com/gremlation/ComfyUI-JMESPath](https://github.com/gremlation/ComfyUI-JMESPath)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed to run JMESPath queries against input JSON, which could be used to manipulate or extract data from the mask input.

### Metadata
**Author:** gremlation
**Repository:** [https://github.com/gremlation/ComfyUI-JMESPath](https://github.com/gremlation/ComfyUI-JMESPath)
**Install Type:** git-clone

---

### ComfyUI-jq

**Description:**

A ComfyUI node that runs a [a/jq](https://jqlang.github.io/jq/) query against input JSON and outputs the result.

- **Author:** gremlation
- **Repository:** [https://github.com/gremlation/ComfyUI-jq](https://github.com/gremlation/ComfyUI-jq)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can parse JSON data and run queries against it, which could be useful for manipulating the mask input in the inpainting workflow.

### Metadata
**Author:** gremlation
**Repository:** [https://github.com/gremlation/ComfyUI-jq](https://github.com/gremlation/ComfyUI-jq)
**Install Type:** git-clone

---

### ComfyUI-KepOpenAI

**Description:**

ComfyUI-KepOpenAI is a user-friendly node that serves as an interface to the GPT-4 with Vision (GPT-4V) API. This integration facilitates the processing of images coupled with text prompts, leveraging the capabilities of the OpenAI API to generate text completions that are contextually relevant to the provided inputs.

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/ComfyUI-KepOpenAI](https://github.com/M1kep/ComfyUI-KepOpenAI)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node integrates with the OpenAI API and can process images coupled with text prompts, making it highly relevant and useful for generating contextual completions in an inpainting workflow with a mask input.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/ComfyUI-KepOpenAI](https://github.com/M1kep/ComfyUI-KepOpenAI)
**Install Type:** git-clone

---

### ComfyUI-KGnodes

**Description:**

NODES:Custom Resolution Latent Node, Style Selector
This Custom node offers various experimental nodes to make it easier to use ComfyUI.

- **Author:** shahkoorosh
- **Repository:** [https://github.com/shahkoorosh/ComfyUI-KGnodes](https://github.com/shahkoorosh/ComfyUI-KGnodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some experimental nodes that might be tangentially related to inpainting, but its relevance is limited and mostly supporting.

### Metadata
**Author:** shahkoorosh
**Repository:** [https://github.com/shahkoorosh/ComfyUI-KGnodes](https://github.com/shahkoorosh/ComfyUI-KGnodes)
**Install Type:** git-clone

---

### ComfyUI-KLingAI-API

**Description:**

Provide high-quality video and image generation capabilities, meeting creators' needs for creative content production and management through more convenient operations, richer functionalities, professional parameters, and stunning effects.

- **Author:** Kling AI
- **Repository:** [https://github.com/KwaiVGI/ComfyUI-KLingAI-API](https://github.com/KwaiVGI/ComfyUI-KLingAI-API)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides high-quality video and image generation capabilities specifically designed for creative content production and management, which aligns well with the inpainting workflow goal.

### Metadata
**Author:** Kling AI
**Repository:** [https://github.com/KwaiVGI/ComfyUI-KLingAI-API](https://github.com/KwaiVGI/ComfyUI-KLingAI-API)
**Install Type:** git-clone

---

### ComfyUI-KwaiKolorsWrapper

**Description:**

Rudimentary wrapper that runs [a/Kwai-Kolors](https://huggingface.co/Kwai-Kolors/Kolors) text2image pipeline using diffusers.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node provides a text-to-image pipeline using diffusers which can be used as a supporting tool for the inpainting workflow goal, although it may require additional processing steps.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper)
**Install Type:** git-clone

---

### comfyui-labs-google

**Description:**

NODES: ComfyUI-ImageFx, ComfyUI-Whisk

- **Author:** ainewsto
- **Repository:** [https://github.com/ainewsto/comfyui-labs-google](https://github.com/ainewsto/comfyui-labs-google)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI-ImageFx could be used for image processing tasks related to inpainting.

### Metadata
**Author:** ainewsto
**Repository:** [https://github.com/ainewsto/comfyui-labs-google](https://github.com/ainewsto/comfyui-labs-google)
**Install Type:** git-clone

---

### Comfyui-Lama

**Description:**

Nodes: LamaaModelLoad, LamaApply, YamlConfigLoader. a costumer node is realized to remove anything/inpainting anything from a picture by mask inpainting.[w/WARN:This extension includes the entire model, which can result in a very long initial installation time, and there may be some compatibility issues with older dependencies and ComfyUI.]

- **Author:** hhhzzyang
- **Repository:** [https://github.com/hhhzzyang/Comfyui_Lama](https://github.com/hhhzzyang/Comfyui_Lama)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** LamaApply is directly related to the workflow goal of inpainting with a mask input.

### Metadata
**Author:** hhhzzyang
**Repository:** [https://github.com/hhhzzyang/Comfyui_Lama](https://github.com/hhhzzyang/Comfyui_Lama)
**Install Type:** git-clone

---

### ComfyUI-LatentSyncWrapper

**Description:**

This node provides lip-sync capabilities in ComfyUI using ByteDance's LatentSync model. It allows you to synchronize video lips with audio input.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper](https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides lip-sync capabilities which can be useful for video editing but may not directly contribute to inpainting with mask input.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper](https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper)
**Install Type:** git-clone

---

### ComfyUI-layerdiffuse (layerdiffusion)

**Description:**

ComfyUI implementation of [a/LayerDiffusion](https://github.com/layerdiffusion/LayerDiffusion).

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node implements layer diffusion, a key component in many inpainting workflows with mask input.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse)
**Install Type:** git-clone

---

### ComfyUI-LightGlue

**Description:**

This is an ComfyUI implementation of LightGlue to generate motion brush

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-LightGlue](https://github.com/chaojie/ComfyUI-LightGlue)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** LightGlue is directly relevant to generating motion brushes which can be useful in an inpainting workflow with mask input.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-LightGlue](https://github.com/chaojie/ComfyUI-LightGlue)
**Install Type:** git-clone

---

### comfyui-liveportrait

**Description:**

The ComfyUI version of [a/LivePortrait](https://github.com/KwaiVGI/LivePortrait).

- **Author:** shadowcz007
- **Repository:** [https://github.com/shadowcz007/comfyui-liveportrait](https://github.com/shadowcz007/comfyui-liveportrait)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node is related to generating animal image-based emoji from videos but can be used as a supporting tool for inpainting workflows.

### Metadata
**Author:** shadowcz007
**Repository:** [https://github.com/shadowcz007/comfyui-liveportrait](https://github.com/shadowcz007/comfyui-liveportrait)
**Install Type:** git-clone

---

### ComfyUI-LivePortrait_v2

**Description:**

We developed a custom_node for Liveportrait_v2 that enables flexible use on Comfyui to drive animal image-based emoji generation from videos.

- **Author:** VangengLab
- **Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v2](https://github.com/VangengLab/ComfyUI-LivePortrait_v2)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This custom node enables flexible use of LivePortrait_v2 on Comfyui and directly supports the generation of images with mask input.

### Metadata
**Author:** VangengLab
**Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v2](https://github.com/VangengLab/ComfyUI-LivePortrait_v2)
**Install Type:** git-clone

---

### ComfyUI-LivePortraitKJ

**Description:**

Nodes for [a/LivePortrait](https://github.com/KwaiVGI/LivePortrait)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-LivePortraitKJ](https://github.com/kijai/ComfyUI-LivePortraitKJ)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node seems to be a custom implementation of Live Portrait, which could be useful for the specified workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-LivePortraitKJ](https://github.com/kijai/ComfyUI-LivePortraitKJ)
**Install Type:** git-clone

---

### ComfyUI-LivePortraitNode (Replicate API)

**Description:**

Two simple to install nodes to get Live Portrait working in ComfyUI without the need for a fancy GPU (Replicate account needed).

- **Author:** LightSketch-ai
- **Repository:** [https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode](https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for replicating the Live Portrait API in ComfyUI, making it highly relevant and useful for the inpainting workflow with mask input.

### Metadata
**Author:** LightSketch-ai
**Repository:** [https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode](https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode)
**Install Type:** git-clone

---

### ComfyUI-LLaMA-Mesh

**Description:**

ComfyUI nodes for LLaMA-Mesh model.

- **Author:** Yuan-ManX
- **Repository:** [https://github.com/Yuan-ManX/ComfyUI-LLaMA-Mesh](https://github.com/Yuan-ManX/ComfyUI-LLaMA-Mesh)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI-LLaMA-Mesh model seems directly relevant for the inpainting workflow with mask input.

### Metadata
**Author:** Yuan-ManX
**Repository:** [https://github.com/Yuan-ManX/ComfyUI-LLaMA-Mesh](https://github.com/Yuan-ManX/ComfyUI-LLaMA-Mesh)
**Install Type:** git-clone

---

### ComfyUI-LLMs

**Description:**

A minimalist node that calls LLMs, combined with one API, can call all language models, including local models.

- **Author:** leoleelxh
- **Repository:** [https://github.com/leoleelxh/ComfyUI-LLMs](https://github.com/leoleelxh/ComfyUI-LLMs)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** ComfyUI-LLMs can call all language models, including local models, but its direct relevance to the inpainting workflow with mask input is unclear.

### Metadata
**Author:** leoleelxh
**Repository:** [https://github.com/leoleelxh/ComfyUI-LLMs](https://github.com/leoleelxh/ComfyUI-LLMs)
**Install Type:** git-clone

---

### ComfyUI-Load-DirectoryFiles

**Description:**

This node loads prompts (txt) and images (png) from a specified directory. By specifying an index, it outputs the selected file.

- **Author:** educator-art
- **Repository:** [https://github.com/educator-art/ComfyUI-Load-DirectoryFiles](https://github.com/educator-art/ComfyUI-Load-DirectoryFiles)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can load images from a directory, which could be useful for providing input images for the inpainting workflow.

### Metadata
**Author:** educator-art
**Repository:** [https://github.com/educator-art/ComfyUI-Load-DirectoryFiles](https://github.com/educator-art/ComfyUI-Load-DirectoryFiles)
**Install Type:** git-clone

---

### ComfyUI-load-image-from-url

**Description:**

A simple node to load image from local path or http url.
You can find this node from 'image' category.

- **Author:** tsogzark
- **Repository:** [https://github.com/tsogzark/ComfyUI-load-image-from-url](https://github.com/tsogzark/ComfyUI-load-image-from-url)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can load an image from a URL or local path, making it suitable for fetching input images for the inpainting workflow.

### Metadata
**Author:** tsogzark
**Repository:** [https://github.com/tsogzark/ComfyUI-load-image-from-url](https://github.com/tsogzark/ComfyUI-load-image-from-url)
**Install Type:** git-clone

---

### ComfyUI-LoadImage-Advanced

**Description:**

This is a node that simply integrates LoadImage, Vae Encode, Upscale, Resolution factor correction, and Color Adjustment.

- **Author:** souki202
- **Repository:** [https://github.com/souki202/ComfyUI-LoadImage-Advanced](https://github.com/souki202/ComfyUI-LoadImage-Advanced)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node seems very useful as it integrates multiple image processing tasks that are likely necessary for an inpainting workflow with mask input.

### Metadata
**Author:** souki202
**Repository:** [https://github.com/souki202/ComfyUI-LoadImage-Advanced](https://github.com/souki202/ComfyUI-LoadImage-Advanced)
**Install Type:** git-clone

---

### comfyui-loadimagewithsubfolder

**Description:**

Extend LoadImage node with subfolder support

- **Author:** liangt
- **Repository:** [https://github.com/liangt/comfyui-loadimagewithsubfolder](https://github.com/liangt/comfyui-loadimagewithsubfolder)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant to the workflow goal, as it extends the LoadImage node to support subfolders, which could be necessary for loading mask inputs or other images required by the inpainting workflow.

### Metadata
**Author:** liangt
**Repository:** [https://github.com/liangt/comfyui-loadimagewithsubfolder](https://github.com/liangt/comfyui-loadimagewithsubfolder)
**Install Type:** git-clone

---

### ComfyUI-Long-CLIP

**Description:**

This project implements the comfyui for long-clip, currently supporting the replacement of clip-l. For SD1.5, the SeaArtLongClip module can be used to replace the original clip in the model, expanding the token length from 77 to 248.

- **Author:** SeaArtLab
- **Repository:** [https://github.com/SeaArtLab/ComfyUI-Long-CLIP](https://github.com/SeaArtLab/ComfyUI-Long-CLIP)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node specifically extends ComfyUI for long-clip support and replacement of clip-l, which aligns closely with the inpainting workflow goal involving mask input.

### Metadata
**Author:** SeaArtLab
**Repository:** [https://github.com/SeaArtLab/ComfyUI-Long-CLIP](https://github.com/SeaArtLab/ComfyUI-Long-CLIP)
**Install Type:** git-clone

---

### ComfyUI-Loop-image

**Description:**

ComfyUI Loop Image is a node package specifically designed for image loop processing. It provides two main processing modes: Batch Image Processing and Single Image Processing, along with supporting image segmentation and merging functions.

- **Author:** WainWong
- **Repository:** [https://github.com/WainWong/ComfyUI-Loop-image](https://github.com/WainWong/ComfyUI-Loop-image)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI-Loop-image is specifically designed for image loop processing and can handle batch or single image processing, making it very useful for the specified workflow goal.

### Metadata
**Author:** WainWong
**Repository:** [https://github.com/WainWong/ComfyUI-Loop-image](https://github.com/WainWong/ComfyUI-Loop-image)
**Install Type:** git-clone

---

### ComfyUI-LoRA-Tuner

**Description:**

Nodes: LoRA-Tuner. For using multiple LoRA easily.

- **Author:** AonekoSS
- **Repository:** [https://github.com/AonekoSS/ComfyUI-LoRA-Tuner](https://github.com/AonekoSS/ComfyUI-LoRA-Tuner)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node provides a LoRA tuner, its relevance to an inpainting workflow with mask input is marginal as it seems to focus on LoRA functionality rather than image processing or inpainting.

### Metadata
**Author:** AonekoSS
**Repository:** [https://github.com/AonekoSS/ComfyUI-LoRA-Tuner](https://github.com/AonekoSS/ComfyUI-LoRA-Tuner)
**Install Type:** git-clone

---

### ComfyUI-LTXTricks

**Description:**

A set of nodes that provide additional controls for the LTX Video model

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-LTXTricks](https://github.com/logtd/ComfyUI-LTXTricks)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides additional controls that can be useful in an inpainting workflow with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-LTXTricks](https://github.com/logtd/ComfyUI-LTXTricks)
**Install Type:** git-clone

---

### ComfyUI-LTXVideo

**Description:**

ComfyUI nodes for LTXVideo model.

- **Author:** lightricks
- **Repository:** [https://github.com/Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for the LTX Video model, which is likely used in an inpainting workflow with mask input.

### Metadata
**Author:** lightricks
**Repository:** [https://github.com/Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo)
**Install Type:** git-clone

---

### ComfyUI-Lumina-Next-SFT-DiffusersWrapper

**Description:**

ComfyUI-Lumina-Next-SFT-DiffusersWrapper is a custom node for ComfyUI that integrates the advanced Lumina-Next-SFT model. It offers high-quality image generation with features like time-aware scaling, optional ODE sampling, and support for high-resolution outputs. This node brings the power of the Lumina text-to-image pipeline directly into ComfyUI workflows, allowing for flexible and powerful image generation capabilities.

- **Author:** Indra's Mirror
- **Repository:** [https://github.com/Excidos/ComfyUI-Lumina-Next-SFT-DiffusersWrapper](https://github.com/Excidos/ComfyUI-Lumina-Next-SFT-DiffusersWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential for the inpainting workflow as it integrates a high-quality image generation model with advanced features.

### Metadata
**Author:** Indra's Mirror
**Repository:** [https://github.com/Excidos/ComfyUI-Lumina-Next-SFT-DiffusersWrapper](https://github.com/Excidos/ComfyUI-Lumina-Next-SFT-DiffusersWrapper)
**Install Type:** git-clone

---

### ComfyUI-LuminaWrapper

**Description:**

ComfyUI wrapper nodes for Lumina models

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-LuminaWrapper](https://github.com/kijai/ComfyUI-LuminaWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node provides basic integration with Lumina models but lacks specific features mentioned in other nodes.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-LuminaWrapper](https://github.com/kijai/ComfyUI-LuminaWrapper)
**Install Type:** git-clone

---

### ComfyUI-MagickWand

**Description:**

Proper implementation of ImageMagick - the famous software suite for editing and manipulating digital images to ComfyUI using [a/wandpy](https://github.com/emcconville/wand).
NOTE: You need to install ImageMagick, manually.

- **Author:** Fannovel16
- **Repository:** [https://github.com/Fannovel16/ComfyUI-MagickWand](https://github.com/Fannovel16/ComfyUI-MagickWand)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a direct interface for ImageMagick which is useful for image manipulation and editing tasks in the inpainting workflow.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/ComfyUI-MagickWand](https://github.com/Fannovel16/ComfyUI-MagickWand)
**Install Type:** git-clone

---

### ComfyUI-Manager

**Description:**

ComfyUI-Manager itself is also a custom node.

- **Author:** Dr.Lt.Data
- **Repository:** [https://github.com/ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI-Manager can manage other nodes, including those used in an inpainting workflow, making it essential for this task.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
**Install Type:** git-clone

---

### comfyui-mask-util

**Description:**

Nodes:Split Masks, Mask Selection Of Masks, Mask Region Info

- **Author:** longgui0318
- **Repository:** [https://github.com/longgui0318/comfyui-mask-util](https://github.com/longgui0318/comfyui-mask-util)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** The node provides utilities related to masks but doesn"t directly contribute to the inpainting process.

### Metadata
**Author:** longgui0318
**Repository:** [https://github.com/longgui0318/comfyui-mask-util](https://github.com/longgui0318/comfyui-mask-util)
**Install Type:** git-clone

---

### ComfyUI-MaskArbiter

**Description:**

A node for ComfyUI that takes a list of masks and returns a single mask based on your criteria.

- **Author:** SparknightLLC
- **Repository:** [https://github.com/SparknightLLC/ComfyUI-MaskArbiter](https://github.com/SparknightLLC/ComfyUI-MaskArbiter)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential as it takes a list of masks and returns a single mask based on criteria, which can be used for inpainting.

### Metadata
**Author:** SparknightLLC
**Repository:** [https://github.com/SparknightLLC/ComfyUI-MaskArbiter](https://github.com/SparknightLLC/ComfyUI-MaskArbiter)
**Install Type:** git-clone

---

### ComfyUI-MaskBatchPermutations

**Description:**

Permutes a mask batch to present possible additive combinations. Passing a mask batch (e.g. out of [a/SEGS to Mask Batch](https://github.com/ltdrdata/ComfyUI-Impact-Pack)) will return a new mask batch representing all the possible combinations of the included masks. So, a mask batch with two mask sections, 'A' and 'B', will return a batch containing an empty mask, an empty mask & A, an empty mask & B, and an empty mask & A & B.

- **Author:** curiousjp
- **Repository:** [https://github.com/curiousjp/ComfyUI-MaskBatchPermutations](https://github.com/curiousjp/ComfyUI-MaskBatchPermutations)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** The node generates all possible combinations of additive masks, supporting the inpainting process by providing multiple options.

### Metadata
**Author:** curiousjp
**Repository:** [https://github.com/curiousjp/ComfyUI-MaskBatchPermutations](https://github.com/curiousjp/ComfyUI-MaskBatchPermutations)
**Install Type:** git-clone

---

### ComfyUI-Merlin: Magic Photo Prompter

**Description:**

ComfyUI-Merlin is a custom node extension for ComfyUI, introducing the Magic Photo Prompter. This powerful tool enhances your prompt engineering process by allowing users to easily construct detailed, high-quality prompts for photo-realistic image generation.

- **Author:** Xclbr7
- **Repository:** [https://github.com/Xclbr7/ComfyUI-Merlin](https://github.com/Xclbr7/ComfyUI-Merlin)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it enhances prompt engineering and allows users to construct detailed, high-quality prompts for photo-realistic image generation.

### Metadata
**Author:** Xclbr7
**Repository:** [https://github.com/Xclbr7/ComfyUI-Merlin](https://github.com/Xclbr7/ComfyUI-Merlin)
**Install Type:** git-clone

---

### ComfyUI-MidjourneyHub

**Description:**

A ComfyUI custom node for integrating with Midjourney API.

- **Author:** jiaqianjing
- **Repository:** [https://github.com/jiaqianjing/ComfyUI-MidjourneyHub](https://github.com/jiaqianjing/ComfyUI-MidjourneyHub)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for integrating with Midjourney API, which can be used in the inpainting workflow.

### Metadata
**Author:** jiaqianjing
**Repository:** [https://github.com/jiaqianjing/ComfyUI-MidjourneyHub](https://github.com/jiaqianjing/ComfyUI-MidjourneyHub)
**Install Type:** git-clone

---

### ComfyUI-MimicBrush

**Description:**

a comfyui custom node for [a/MimicBrush](https://github.com/ali-vilab/MimicBrush),then inpainting with reference image.

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-MimicBrush](https://github.com/AIFSH/ComfyUI-MimicBrush)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it provides a MimicBrush functionality that can aid in the inpainting process with reference images.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-MimicBrush](https://github.com/AIFSH/ComfyUI-MimicBrush)
**Install Type:** git-clone

---

### ComfyUI-MimicMotionWrapper

**Description:**

Optimized wrapper nodes for MimicMotion: [a/https://github.com/tencent/MimicMotion](https://github.com/tencent/MimicMotion)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-MimicMotionWrapper](https://github.com/kijai/ComfyUI-MimicMotionWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as a wrapper for MimicMotion, which can be used in the inpainting workflow with mask input.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-MimicMotionWrapper](https://github.com/kijai/ComfyUI-MimicMotionWrapper)
**Install Type:** git-clone

---

### ComfyUI-MingNodes

**Description:**

Nodes: ConvertGrayChannelNode, AdjustBrightnessContrastSaturationNode, BaiduTranslateNode.

- **Author:** mingsky
- **Repository:** [https://github.com/mingsky-ai/ComfyUI-MingNodes](https://github.com/mingsky-ai/ComfyUI-MingNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Provides nodes that can be used in the inpainting workflow but their relevance is unclear

### Metadata
**Author:** mingsky
**Repository:** [https://github.com/mingsky-ai/ComfyUI-MingNodes](https://github.com/mingsky-ai/ComfyUI-MingNodes)
**Install Type:** git-clone

---

### ComfyUI-MistralAI-API

**Description:**

Mistral AI API's chat completion endpoint in ComfyUI

- **Author:** randomnoner11
- **Repository:** [https://github.com/randomnoner11/ComfyUI-MistralAI-API](https://github.com/randomnoner11/ComfyUI-MistralAI-API)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides direct access to Mistral AI API"s chat completion endpoint which can be used for generating inpainted content based on user input and a provided mask.

### Metadata
**Author:** randomnoner11
**Repository:** [https://github.com/randomnoner11/ComfyUI-MistralAI-API](https://github.com/randomnoner11/ComfyUI-MistralAI-API)
**Install Type:** git-clone

---

### ComfyUI-MochiEdit

**Description:**

ComfyUI nodes to edit videos using Genmo Mochi

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-MochiEdit](https://github.com/logtd/ComfyUI-MochiEdit)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports video editing using Genmo Mochi, which can be used for inpainting workflows with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-MochiEdit](https://github.com/logtd/ComfyUI-MochiEdit)
**Install Type:** git-clone

---

### ComfyUI-ModelDownloader

**Description:**

A ComfyUI node to download models(Checkpoints and LoRA) from external links and act as an output standalone node.

- **Author:** holchan
- **Repository:** [https://github.com/holchan/ComfyUI-ModelDownloader](https://github.com/holchan/ComfyUI-ModelDownloader)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can download pre-trained models which are essential for an inpainting workflow, making it very useful.

### Metadata
**Author:** holchan
**Repository:** [https://github.com/holchan/ComfyUI-ModelDownloader](https://github.com/holchan/ComfyUI-ModelDownloader)
**Install Type:** git-clone

---

### ComfyUI-MoGe

**Description:**

NODES:(Down)load MoGe Model, MoGe Process

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-MoGe](https://github.com/kijai/ComfyUI-MoGe)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node has some relevance to the inpainting workflow with mask input, its primary function is not directly related. It may be marginally useful as a supporting node.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-MoGe](https://github.com/kijai/ComfyUI-MoGe)
**Install Type:** git-clone

---

### ComfyUI-Moore-AnimateAnyone

**Description:**

Nodes: Run python tools/download_weights.py first to download weights automatically

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-Moore-AnimateAnyone](https://github.com/chaojie/ComfyUI-Moore-AnimateAnyone)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has a Moondream feature but its primary function is animation which may not be directly useful for inpainting with mask input.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Moore-AnimateAnyone](https://github.com/chaojie/ComfyUI-Moore-AnimateAnyone)
**Install Type:** git-clone

---

### ComfyUI-Mosaic-Mask

**Description:**

ComfyUI-Mosaic-Mask is an automatic tool designed to detect and mask mosaic areas in input images.

- **Author:** okgo4
- **Repository:** [https://github.com/okgo4/ComfyUI-Mosaic-Mask](https://github.com/okgo4/ComfyUI-Mosaic-Mask)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed to detect and mask mosaic areas in input images, which can be useful for preprocessing before inpainting.

### Metadata
**Author:** okgo4
**Repository:** [https://github.com/okgo4/ComfyUI-Mosaic-Mask](https://github.com/okgo4/ComfyUI-Mosaic-Mask)
**Install Type:** git-clone

---

### ComfyUI-MotionCtrl

**Description:**

Nodes: Download the weights of MotionCtrl [a/motionctrl.pth](https://huggingface.co/TencentARC/MotionCtrl/blob/main/motionctrl.pth) and put it to ComfyUI/models/checkpoints

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-MotionCtrl](https://github.com/chaojie/ComfyUI-MotionCtrl)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node controls motion in videos but the weights need to be downloaded separately and it may not be directly applicable for inpainting with mask input.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-MotionCtrl](https://github.com/chaojie/ComfyUI-MotionCtrl)
**Install Type:** git-clone

---

### ComfyUI-MultiGPU

**Description:**

This extension adds CUDA device selection to supported loader nodes in ComfyUI. By monkey-patching ComfyUI’s memory management, each model component (like UNet, Clip, or VAE) can be loaded on a specific GPU. Examples included are multi-GPU workflows for SDXL, FLUX, LTXVideo, and Hunyuan Video for both standard and GGUF loader nodes.

- **Author:** pollockjj
- **Repository:** [https://github.com/pollockjj/ComfyUI-MultiGPU](https://github.com/pollockjj/ComfyUI-MultiGPU)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it allows multi-GPU workflows which can significantly speed up processing time and improve performance.

### Metadata
**Author:** pollockjj
**Repository:** [https://github.com/pollockjj/ComfyUI-MultiGPU](https://github.com/pollockjj/ComfyUI-MultiGPU)
**Install Type:** git-clone

---

### ComfyUI-MusePose-Remaster

**Description:**

MusePose Remaster is a remaster version of ComfyUI MusePose node.
It supports auto weights download, remove most necessary dependencies, etc.

- **Author:** hoveychen
- **Repository:** [https://github.com/hoveychen/ComfyUI-MusePose-Remaster](https://github.com/hoveychen/ComfyUI-MusePose-Remaster)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This remastered version of MusePose supports auto weights download and has fewer dependencies, making it more suitable for the specified workflow goal.

### Metadata
**Author:** hoveychen
**Repository:** [https://github.com/hoveychen/ComfyUI-MusePose-Remaster](https://github.com/hoveychen/ComfyUI-MusePose-Remaster)
**Install Type:** git-clone

---

### ComfyUI-MVAdapter

**Description:**

This extension integrates [a/MV-Adapter](https://github.com/huanngzh/MV-Adapter) into ComfyUI, allowing users to generate multi-view consistent images from text prompts or single images directly within the ComfyUI interface.

- **Author:** huanngzh
- **Repository:** [https://github.com/huanngzh/ComfyUI-MVAdapter](https://github.com/huanngzh/ComfyUI-MVAdapter)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node integrates MV-Adapter into ComfyUI and allows users to generate multi-view consistent images from text prompts or single images directly within the ComfyUI interface. This feature would be very useful for an inpainting workflow with mask input.

### Metadata
**Author:** huanngzh
**Repository:** [https://github.com/huanngzh/ComfyUI-MVAdapter](https://github.com/huanngzh/ComfyUI-MVAdapter)
**Install Type:** git-clone

---

### ComfyUI-My-Mask

**Description:**

Some nodes for processing masks, currently including nodes that fill in the concave parts of existing masks with convex hulls.

- **Author:** jerrylongyan
- **Repository:** [https://github.com/jerrylongyan/ComfyUI-My-Mask](https://github.com/jerrylongyan/ComfyUI-My-Mask)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains mask processing nodes, specifically designed for filling in concave parts of existing masks with convex hulls, making it very useful for this workflow goal.

### Metadata
**Author:** jerrylongyan
**Repository:** [https://github.com/jerrylongyan/ComfyUI-My-Mask](https://github.com/jerrylongyan/ComfyUI-My-Mask)
**Install Type:** git-clone

---

### ComfyUI-N-Nodes

**Description:**

A suite of custom nodes for ConfyUI that includes GPT text-prompt generation, LoadVideo,SaveVideo,LoadFramesFromFolder and FrameInterpolator

- **Author:** Nuked
- **Repository:** [https://github.com/Nuked88/ComfyUI-N-Nodes](https://github.com/Nuked88/ComfyUI-N-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains various video processing nodes that may indirectly support this workflow goal, but are not directly related to inpainting or mask inputs.

### Metadata
**Author:** Nuked
**Repository:** [https://github.com/Nuked88/ComfyUI-N-Nodes](https://github.com/Nuked88/ComfyUI-N-Nodes)
**Install Type:** git-clone

---

### comfyui-NDI

**Description:**

Real-time input output node for ComfyUI by NDI. Leveraging the powerful linking capabilities of NDI, you can access NDI video stream frames and send images generated by the model to NDI video streams.

- **Author:** ningxiaoxiao
- **Repository:** [https://github.com/ningxiaoxiao/comfyui-NDI](https://github.com/ningxiaoxiao/comfyui-NDI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides real-time input/output capabilities using NDI, which could be useful for receiving or sending video streams in the inpainting workflow.

### Metadata
**Author:** ningxiaoxiao
**Repository:** [https://github.com/ningxiaoxiao/comfyui-NDI](https://github.com/ningxiaoxiao/comfyui-NDI)
**Install Type:** git-clone

---

### ComfyUI-NegiTools

**Description:**

Nodes:OpenAI DALLe3, OpenAI Translate to English, String Function, Seed Generator

- **Author:** natto-maki
- **Repository:** [https://github.com/natto-maki/ComfyUI-NegiTools](https://github.com/natto-maki/ComfyUI-NegiTools)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node contains a variety of tools that can support the inpainting workflow, including OpenAI models and string manipulation functions.

### Metadata
**Author:** natto-maki
**Repository:** [https://github.com/natto-maki/ComfyUI-NegiTools](https://github.com/natto-maki/ComfyUI-NegiTools)
**Install Type:** git-clone

---

### ComfyUI-NeuralMedia

**Description:**

A set of custom nodes modified to achieve things I felt were missing.

- **Author:** YarvixPA
- **Repository:** [https://github.com/YarvixPA/ComfyUI-NeuralMedia](https://github.com/YarvixPA/ComfyUI-NeuralMedia)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a collection of custom nodes, but its specific features are not clearly described in relation to the inpainting workflow goal.

### Metadata
**Author:** YarvixPA
**Repository:** [https://github.com/YarvixPA/ComfyUI-NeuralMedia](https://github.com/YarvixPA/ComfyUI-NeuralMedia)
**Install Type:** git-clone

---

### ComfyUI-NodeAligner

**Description:**

ComfyUI-NodeAligner is a lightweight ComfyUI layout plugin that includes features such as node alignment, distribution, and resizing. This plugin is designed to simplify layout adjustments in visual node editors or custom UI components, making node arrangement more convenient and efficient.

- **Author:** Tenney95
- **Repository:** [https://github.com/Tenney95/ComfyUI-NodeAligner](https://github.com/Tenney95/ComfyUI-NodeAligner)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can simplify layout adjustments and make node arrangement more convenient and efficient.

### Metadata
**Author:** Tenney95
**Repository:** [https://github.com/Tenney95/ComfyUI-NodeAligner](https://github.com/Tenney95/ComfyUI-NodeAligner)
**Install Type:** git-clone

---

### ComfyUI-nodes-hnmr

**Description:**

Provide various custom nodes for Latent, Sampling, Model, Loader, Image, Text. This is the fixed version of the original [a/ComfyUI-nodes-hnmr](https://github.com/hnmr293/ComfyUI-nodes-hnmr) by hnmr293.

- **Author:** CYBERLOOM-INC
- **Repository:** [https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr](https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides custom nodes that could be useful in an Inpainting workflow with mask input, particularly those related to image processing.

### Metadata
**Author:** CYBERLOOM-INC
**Repository:** [https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr](https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr)
**Install Type:** git-clone

---

### ComfyUI-NS-ManySliders

**Description:**

ComfyUI-NS-ManySliders is a custom node developed for ComfyUI that allows you to manipulate values using multiple sliders. With this node, you can easily adjust numerous numerical parameters intuitively, making it useful for various purposes.

- **Author:** Assistant
- **Repository:** [https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for adjusting numerical parameters in the inpainting workflow with mask input, making it a valuable addition to this task.

### Metadata
**Author:** Assistant
**Repository:** [https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
**Install Type:** git-clone

---

### ComfyUI-ntfy

**Description:**

NODES:Save Image and ntfy

- **Author:** boredofnames
- **Repository:** [https://github.com/boredofnames/ComfyUI-ntfy](https://github.com/boredofnames/ComfyUI-ntfy)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can save images and notify users, which could be useful in the inpainting workflow for saving results or notifying when a task is complete.

### Metadata
**Author:** boredofnames
**Repository:** [https://github.com/boredofnames/ComfyUI-ntfy](https://github.com/boredofnames/ComfyUI-ntfy)
**Install Type:** git-clone

---

### ComfyUI-NuA-BIRD

**Description:**

ComfyUI implementation of '[a/Blind Image Restoration via Fast Diffusion Inversion](https://github.com/hamadichihaoui/BIRD)' Original [a/article](https://arxiv.org/abs/2405.19572)

- **Author:** nuanarchy
- **Repository:** [https://github.com/nuanarchy/ComfyUI-NuA-BIRD](https://github.com/nuanarchy/ComfyUI-NuA-BIRD)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node implements Blind Image Restoration via Fast Diffusion Inversion, which is relevant to inpainting with mask input as it involves restoring damaged areas of an image.

### Metadata
**Author:** nuanarchy
**Repository:** [https://github.com/nuanarchy/ComfyUI-NuA-BIRD](https://github.com/nuanarchy/ComfyUI-NuA-BIRD)
**Install Type:** git-clone

---

### ComfyUI-NuA-FlashFace

**Description:**

ComfyUI implementation of [a/FlashFace: Human Image Personalization with High-fidelity Identity Preservation](https://github.com/ali-vilab/FlashFace)
NOTE: You need to downalod models manually.

- **Author:** nuanarchy
- **Repository:** [https://github.com/nuanarchy/ComfyUI-NuA-FlashFace](https://github.com/nuanarchy/ComfyUI-NuA-FlashFace)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is not directly related to inpainting with mask input but could be useful for human image personalization, potentially supporting the inpainting workflow in certain scenarios.

### Metadata
**Author:** nuanarchy
**Repository:** [https://github.com/nuanarchy/ComfyUI-NuA-FlashFace](https://github.com/nuanarchy/ComfyUI-NuA-FlashFace)
**Install Type:** git-clone

---

### ComfyUI-Ollama-Describer

**Description:**

This is an extension for ComfyUI that makes it possible to use some LLM models provided by Ollama, such as Gemma, Llava (multimodal), Llama2, Llama3 or Mistral. Speaking specifically of the LLaVa - Large Language and Vision Assistant model, although trained on a relatively small dataset, it demonstrates exceptional capabilities in understanding images and answering questions about them. This model presents similar behaviors to multimodal models such as GPT-4, even when presented with invisible images and instructions.

- **Author:** alisson-anjos
- **Repository:** [https://github.com/alisson-anjos/ComfyUI-Ollama-Describer](https://github.com/alisson-anjos/ComfyUI-Ollama-Describer)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides direct access to LLaVa - Large Language and Vision Assistant model which can be used for understanding images and answering questions about them, making it essential for this workflow.

### Metadata
**Author:** alisson-anjos
**Repository:** [https://github.com/alisson-anjos/ComfyUI-Ollama-Describer](https://github.com/alisson-anjos/ComfyUI-Ollama-Describer)
**Install Type:** git-clone

---

### comfyui-ollama-nodes

**Description:**

ComfyUI custom nodes for working with [a/Ollama](https://github.com/ollama/ollama).
NOTE:Assumes that an Ollama server is running at http://127.0.0.1:11434 and accessible by the ComfyUI backend.

- **Author:** slyt
- **Repository:** [https://github.com/slyt/comfyui-ollama-nodes](https://github.com/slyt/comfyui-ollama-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides custom nodes for working with Ollama server, which can be useful for tasks like image generation or description, but might require additional setup to integrate with the inpainting workflow.

### Metadata
**Author:** slyt
**Repository:** [https://github.com/slyt/comfyui-ollama-nodes](https://github.com/slyt/comfyui-ollama-nodes)
**Install Type:** git-clone

---

### ComfyUI-OllamaPromptsGeneratorTlant

**Description:**

Use ollama to generate prompts based on reference text in comfyui.

- **Author:** Tlant
- **Repository:** [https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant](https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node generates prompts based on reference text using Ollama, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** Tlant
**Repository:** [https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant](https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant)
**Install Type:** git-clone

---

### ComfyUI-OmniGen

**Description:**

ComfyUI custom node implementation of OmniGen

- **Author:** 1038lab
- **Repository:** [https://github.com/1038lab/ComfyUI-OmniGen](https://github.com/1038lab/ComfyUI-OmniGen)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node implements OmniGen which could potentially be useful in generating prompts or images, but its direct relevance to the specified workflow goal is unclear.

### Metadata
**Author:** 1038lab
**Repository:** [https://github.com/1038lab/ComfyUI-OmniGen](https://github.com/1038lab/ComfyUI-OmniGen)
**Install Type:** git-clone

---

### ComfyUI-OneForOne

**Description:**

Node:Image Fit Calculator

- **Author:** Meettya
- **Repository:** [https://github.com/Meettya/ComfyUI-OneForOne](https://github.com/Meettya/ComfyUI-OneForOne)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides an Image Fit Calculator which can be useful for adjusting the mask to fit the input image in the inpainting workflow.

### Metadata
**Author:** Meettya
**Repository:** [https://github.com/Meettya/ComfyUI-OneForOne](https://github.com/Meettya/ComfyUI-OneForOne)
**Install Type:** git-clone

---

### ComfyUI-Open-Sora-I2V

**Description:**

Another comfy implementation for the short video generation project hpcaitech/Open-Sora, supporting latest V2 and V3 models as well as image to video functions, etc.

- **Author:** bombax-xiaoice
- **Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Open-Sora-I2V](https://github.com/bombax-xiaoice/ComfyUI-Open-Sora-I2V)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node supports image-to-video functions, it may have some features that could be useful for the inpainting workflow but its direct relevance to the goal is limited.

### Metadata
**Author:** bombax-xiaoice
**Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Open-Sora-I2V](https://github.com/bombax-xiaoice/ComfyUI-Open-Sora-I2V)
**Install Type:** git-clone

---

### ComfyUI-OpenDiTWrapper

**Description:**

Wrapper nodes for OpenDiT: [a/OpenDiT](https://github.com/NUS-HPC-AI-Lab/OpenDiT/), supports Open-Sora t2i and i2i

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-OpenDiTWrapper](https://github.com/kijai/ComfyUI-OpenDiTWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is a wrapper for OpenDiT, which supports inpainting tasks and can be used with mask inputs.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-OpenDiTWrapper](https://github.com/kijai/ComfyUI-OpenDiTWrapper)
**Install Type:** git-clone

---

### ComfyUI-Paint3D-Nodes

**Description:**

Paint3D Nodes is a custom ComfyUI node for 3D model texture inpainting based on [a/Paint3D](https://arxiv.org/pdf/2312.13913).

- **Author:** N3rd00d
- **Repository:** [https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is specifically designed for 3D model texture inpainting using Paint3D, making it highly relevant to the workflow goal.

### Metadata
**Author:** N3rd00d
**Repository:** [https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes)
**Install Type:** git-clone

---

### ComfyUI-PhandoNodes

**Description:**

A collection of nodes to help streamline your ComfyUI workflows

- **Author:** Phando
- **Repository:** [https://github.com/Phando/ComfyUI-PhandoNodes](https://github.com/Phando/ComfyUI-PhandoNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this collection of nodes may provide some utility in a ComfyUI workflow, its relevance and specific features for an inpainting workflow with mask input are not clearly defined and would require further investigation.

### Metadata
**Author:** Phando
**Repository:** [https://github.com/Phando/ComfyUI-PhandoNodes](https://github.com/Phando/ComfyUI-PhandoNodes)
**Install Type:** git-clone

---

### ComfyUI-Photopea

**Description:**

Edit images in the Photopea editor directly within ComfyUI.

- **Author:** Jin Liu
- **Repository:** [https://github.com/coolzilj/ComfyUI-Photopea](https://github.com/coolzilj/ComfyUI-Photopea)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides direct image editing capabilities within ComfyUI using Photopea, which can be used for inpainting with mask input.

### Metadata
**Author:** Jin Liu
**Repository:** [https://github.com/coolzilj/ComfyUI-Photopea](https://github.com/coolzilj/ComfyUI-Photopea)
**Install Type:** git-clone

---

### comfyui-photoshop

**Description:**

Powerfull bridge to Photoshop by NimaNzrii

- **Author:** NimaNzrii
- **Repository:** [https://github.com/NimaNzrii/comfyui-photoshop](https://github.com/NimaNzrii/comfyui-photoshop)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node acts as a bridge to Photoshop, allowing users to leverage its capabilities for inpainting with mask input, making it very useful for this workflow goal.

### Metadata
**Author:** NimaNzrii
**Repository:** [https://github.com/NimaNzrii/comfyui-photoshop](https://github.com/NimaNzrii/comfyui-photoshop)
**Install Type:** git-clone

---

### ComfyUI-PIL

**Description:**

ComfyUI is proud to present a new plugin designed to enhance user experience through seamless integration with Pillow, the powerful fork of Python Imaging Library (PIL). This plugin offers a suite of basic image manipulation tools that are easy to use and integrate directly into the ComfyUI framework.

- **Author:** SoftMeng
- **Repository:** [https://github.com/SoftMeng/ComfyUI-PIL](https://github.com/SoftMeng/ComfyUI-PIL)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node offers basic image manipulation tools that could be useful for preprocessing or post-processing in an inpainting workflow.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI-PIL](https://github.com/SoftMeng/ComfyUI-PIL)
**Install Type:** git-clone

---

### ComfyUI-PixelResolutionCalculator

**Description:**

Simple resuluition calculator to convert pixel resolution and aspect ratio to laten friendlt pixel width and height size.

- **Author:** LING-APE
- **Repository:** [https://github.com/Ling-APE/ComfyUI-PixelResolutionCalculator](https://github.com/Ling-APE/ComfyUI-PixelResolutionCalculator)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly calculates resolution and aspect ratio, which is essential for inpainting with mask input to ensure accurate pixel width and height sizing.

### Metadata
**Author:** LING-APE
**Repository:** [https://github.com/Ling-APE/ComfyUI-PixelResolutionCalculator](https://github.com/Ling-APE/ComfyUI-PixelResolutionCalculator)
**Install Type:** git-clone

---

### ComfyUI-Portrait-Maker

**Description:**

Nodes:RetainFace, FaceFusion, RatioMerge2Image, MaskMerge2Image, ReplaceBoxImg, ExpandMaskBox, FaceSkin, SkinRetouching, PortraitEnhancement, ...

- **Author:** THtianhao
- **Repository:** [https://github.com/THtianhao/ComfyUI-Portrait-Maker](https://github.com/THtianhao/ComfyUI-Portrait-Maker)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for portrait making with a mask input, directly relevant to the inpainting workflow.

### Metadata
**Author:** THtianhao
**Repository:** [https://github.com/THtianhao/ComfyUI-Portrait-Maker](https://github.com/THtianhao/ComfyUI-Portrait-Maker)
**Install Type:** git-clone

---

### ComfyUI-post-processing-nodes

**Description:**

A collection of post processing nodes for ComfyUI, simply download this repo and drag.

- **Author:** EllangoK
- **Repository:** [https://github.com/EllangoK/ComfyUI-post-processing-nodes](https://github.com/EllangoK/ComfyUI-post-processing-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not specifically designed for inpainting, this collection of post-processing nodes could provide useful utilities that support the workflow goal.

### Metadata
**Author:** EllangoK
**Repository:** [https://github.com/EllangoK/ComfyUI-post-processing-nodes](https://github.com/EllangoK/ComfyUI-post-processing-nodes)
**Install Type:** git-clone

---

### ComfyUI-Prediction

**Description:**

Fully customizable Classifier Free Guidance for ComfyUI.

- **Author:** redhottensors
- **Repository:** [https://github.com/redhottensors/ComfyUI-Prediction](https://github.com/redhottensors/ComfyUI-Prediction)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides fully customizable Classifier Free Guidance for ComfyUI, which would be very useful for the specified workflow goal of inpainting with mask input.

### Metadata
**Author:** redhottensors
**Repository:** [https://github.com/redhottensors/ComfyUI-Prediction](https://github.com/redhottensors/ComfyUI-Prediction)
**Install Type:** git-clone

---

### ComfyUI-Prediction-Boost

**Description:**

prediction boost custom node for ComfyUI

- **Author:** tmagara
- **Repository:** [https://github.com/tmagara/ComfyUI-Prediction-Boost](https://github.com/tmagara/ComfyUI-Prediction-Boost)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant to inpainting with mask input as it could potentially provide a prediction boost, but its direct relevance and utility are unclear.

### Metadata
**Author:** tmagara
**Repository:** [https://github.com/tmagara/ComfyUI-Prediction-Boost](https://github.com/tmagara/ComfyUI-Prediction-Boost)
**Install Type:** git-clone

---

### comfyui-previewlatent

**Description:**

a ComfyUI plugin for previewing latents without vae decoding. Useful for showing intermediate results and can be used a faster 'preview image' if you don't wan't to use vae decode.

- **Author:** martijnat
- **Repository:** [https://github.com/martijnat/comfyui-previewlatent](https://github.com/martijnat/comfyui-previewlatent)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows for previewing latents without VAE decoding, which would be very useful for showing intermediate results during the inpainting process with mask input.

### Metadata
**Author:** martijnat
**Repository:** [https://github.com/martijnat/comfyui-previewlatent](https://github.com/martijnat/comfyui-previewlatent)
**Install Type:** git-clone

---

### comfyui-prompt-composer

**Description:**

A suite of tools for prompt management. Combining nodes helps the user sequence strings for prompts, also creating logical groupings if necessary. Individual nodes can be chained together in any order.

- **Author:** florestefano1975
- **Repository:** [https://github.com/florestefano1975/comfyui-prompt-composer](https://github.com/florestefano1975/comfyui-prompt-composer)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is moderately useful for managing prompts but may not provide direct benefits to an inpainting workflow with a mask input.

### Metadata
**Author:** florestefano1975
**Repository:** [https://github.com/florestefano1975/comfyui-prompt-composer](https://github.com/florestefano1975/comfyui-prompt-composer)
**Install Type:** git-clone

---

### ComfyUI-Prompt-MZ

**Description:**

Use llama.cpp to help generate some nodes for prompt word related work

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ](https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Node uses llama.cpp to generate nodes related to prompts, which may be marginally useful for generating related tasks in the inpainting workflow.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ](https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ)
**Install Type:** git-clone

---

### ComfyUI-Prompter-fofrAI

**Description:**

A prompt helper for ComfyUI, based on [a/prompter.fofr.ai](https://prompter.fofr.ai)

- **Author:** fofr
- **Repository:** [https://github.com/fofr/ComfyUI-Prompter-fofrAI](https://github.com/fofr/ComfyUI-Prompter-fofrAI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This prompt helper can generate and refine prompts for the inpainting task, making it very useful in this workflow.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/fofr/ComfyUI-Prompter-fofrAI](https://github.com/fofr/ComfyUI-Prompter-fofrAI)
**Install Type:** git-clone

---

### ComfyUI-promptLAB

**Description:**

connection nodes for api requests, fully supports promptLAB

- **Author:** Makeezi
- **Repository:** [https://github.com/Makeezi/ComfyUI-promptLAB](https://github.com/Makeezi/ComfyUI-promptLAB)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node supports promptLAB which might be related to inpainting, its primary function is connecting nodes for API requests, making it marginally relevant to the specified workflow goal.

### Metadata
**Author:** Makeezi
**Repository:** [https://github.com/Makeezi/ComfyUI-promptLAB](https://github.com/Makeezi/ComfyUI-promptLAB)
**Install Type:** git-clone

---

### ComfyUI-PromptUtilities

**Description:**

Nodes: Format String, Join String List, Load Preset, Load Preset (Advanced), Const String, Const String (multi line). Add useful nodes related to prompt.

- **Author:** nkchocoai
- **Repository:** [https://github.com/nkchocoai/ComfyUI-PromptUtilities](https://github.com/nkchocoai/ComfyUI-PromptUtilities)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides various prompt utilities that can be useful for generating or manipulating masks in the inpainting workflow.

### Metadata
**Author:** nkchocoai
**Repository:** [https://github.com/nkchocoai/ComfyUI-PromptUtilities](https://github.com/nkchocoai/ComfyUI-PromptUtilities)
**Install Type:** git-clone

---

### ComfyUI-PromptUtils

**Description:**

A set of ComfyUI nodes designed to enhance your workflow with realistic filename generation and keyword generation.

- **Author:** Black-Lioness
- **Repository:** [https://github.com/Black-Lioness/ComfyUI-PromptUtils](https://github.com/Black-Lioness/ComfyUI-PromptUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node offers filename and keyword generation features which could support the inpainting workflow by providing relevant metadata.

### Metadata
**Author:** Black-Lioness
**Repository:** [https://github.com/Black-Lioness/ComfyUI-PromptUtils](https://github.com/Black-Lioness/ComfyUI-PromptUtils)
**Install Type:** git-clone

---

### ComfyUI-PuLID-Flux-Enhanced

**Description:**

adapted from [a/https://github.com/balazik/ComfyUI-PuLID-Flux](https://github.com/balazik/ComfyUI-PuLID-Flux).
common fusion methods for multi-image input, some further experimental fusion methods, switch between using gray image (official) and rgb.,

- **Author:** sipie800
- **Repository:** [https://github.com/sipie800/ComfyUI-PuLID-Flux-Enhanced](https://github.com/sipie800/ComfyUI-PuLID-Flux-Enhanced)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a PuLID fusion method specifically designed for multi-image input and can be used in an inpainting workflow with mask input.

### Metadata
**Author:** sipie800
**Repository:** [https://github.com/sipie800/ComfyUI-PuLID-Flux-Enhanced](https://github.com/sipie800/ComfyUI-PuLID-Flux-Enhanced)
**Install Type:** git-clone

---

### ComfyUI-PuLID-Flux-GR

**Description:**

This is a PuLID node that has been extended with new features.

- **Author:** GraftingRayman
- **Repository:** [https://github.com/GraftingRayman/ComfyUI-PuLID-Flux-GR](https://github.com/GraftingRayman/ComfyUI-PuLID-Flux-GR)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node extends the PuLID fusion method with new features suitable for use in an inpainting workflow with mask input.

### Metadata
**Author:** GraftingRayman
**Repository:** [https://github.com/GraftingRayman/ComfyUI-PuLID-Flux-GR](https://github.com/GraftingRayman/ComfyUI-PuLID-Flux-GR)
**Install Type:** git-clone

---

### comfyui-put-image

**Description:**

Load image from directory.

- **Author:** shinich39
- **Repository:** [https://github.com/shinich39/comfyui-put-image](https://github.com/shinich39/comfyui-put-image)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Loads an image from a directory but does not directly contribute to inpainting with mask input.

### Metadata
**Author:** shinich39
**Repository:** [https://github.com/shinich39/comfyui-put-image](https://github.com/shinich39/comfyui-put-image)
**Install Type:** git-clone

---

### ComfyUI-Qais-Helper

**Description:**

This Extension adds a few custom QOL nodes that ComfyUI lacks by default.

- **Author:** Qais Malkawi
- **Repository:** [https://github.com/QaisMalkawi/ComfyUI-QaisHelper](https://github.com/QaisMalkawi/ComfyUI-QaisHelper)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** ComfyUI-Qais-Helper may contain custom nodes that could support the inpainting workflow, but its primary purpose is QOL improvements.

### Metadata
**Author:** Qais Malkawi
**Repository:** [https://github.com/QaisMalkawi/ComfyUI-QaisHelper](https://github.com/QaisMalkawi/ComfyUI-QaisHelper)
**Install Type:** git-clone

---

### ComfyUI-Qwen2

**Description:**

Qwen2 Nodes for ComfyUI.
I needed to run Qwen2 on ComfyUI to use it in my workflow for batching images and captioning and none of the implementations I found on the web worked the way I wanted.[w/May contain bugs.]

- **Author:** ARZUMATA
- **Repository:** [https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2](https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node collection might offer some utility in supporting tasks like batching images and captioning, but its relevance to inpainting workflows with mask input is limited.

### Metadata
**Author:** ARZUMATA
**Repository:** [https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2](https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2)
**Install Type:** git-clone

---

### ComfyUI-RAFT

**Description:**

This is an ComfyUI implementation of RAFT to generate motion brush

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-RAFT](https://github.com/chaojie/ComfyUI-RAFT)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** RAFT can generate motion brush which could be useful in inpainting workflows.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-RAFT](https://github.com/chaojie/ComfyUI-RAFT)
**Install Type:** git-clone

---

### ComfyUI-RAVE

**Description:**

Unofficial ComfyUI implementation of [a/RAVE](https://rave-video.github.io/)

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-RAVE](https://github.com/spacepxl/ComfyUI-RAVE)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node can be useful for generating images that may need inpainting, but its primary purpose is to implement RAVE video synthesis.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-RAVE](https://github.com/spacepxl/ComfyUI-RAVE)
**Install Type:** git-clone

---

### ComfyUI-RAVE Attention

**Description:**

ComfyUI nodes to use RAVE attention as a temporal attention mechanism.
This differs from other implementations in that it does not concatenate the images together, but within the UNet's Self-Attention mechanism performs the RAVE technique. By not altering the images/latents throughout the UNet, this method does not affect other temporal techniques, style mechanisms, or other UNet modifications.
For example, it can be combined with AnimateDiff, ModelScope/ZeroScope, or FLATTEN.

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-RAVE_ATTN](https://github.com/logtd/ComfyUI-RAVE_ATTN)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly implements the RAVE attention mechanism as a temporal attention mechanism, which could be very useful in an inpainting workflow with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RAVE_ATTN](https://github.com/logtd/ComfyUI-RAVE_ATTN)
**Install Type:** git-clone

---

### ComfyUI-Redux-Prompt

**Description:**

A ComfyUI custom node that provides fine-grained control over style transfer using Redux style models.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt](https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides fine-grained control over style transfer which can be useful for inpainting with mask input.

### Metadata
**Author:** CY-CHENYUE
**Repository:** [https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt](https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt)
**Install Type:** git-clone

---

### ComfyUI-RefSampling

**Description:**

Nodes:Apply Ref UNet, Ref Sampler, Ref Sampler Custom

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-RefSampling](https://github.com/logtd/ComfyUI-RefSampling)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node offers various nodes (Ref UNet, Ref Sampler, Ref Sampler Custom) that are directly related to inpainting with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RefSampling](https://github.com/logtd/ComfyUI-RefSampling)
**Install Type:** git-clone

---

### ComfyUI-RefUNet

**Description:**

A set of nodes to use Reference UNets

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-RefUNet](https://github.com/logtd/ComfyUI-RefUNet)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node provides a set of Reference UNets which is highly relevant and useful for inpainting with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RefUNet](https://github.com/logtd/ComfyUI-RefUNet)
**Install Type:** git-clone

---

### ComfyUI-Remover

**Description:**

Custom node for ComfyUI that makes parts of the image transparent (face, background...)

- **Author:** Shraknard
- **Repository:** [https://github.com/Shraknard/ComfyUI-Remover](https://github.com/Shraknard/ComfyUI-Remover)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This custom node can make parts of the image transparent, which could be useful in an inpainting workflow.

### Metadata
**Author:** Shraknard
**Repository:** [https://github.com/Shraknard/ComfyUI-Remover](https://github.com/Shraknard/ComfyUI-Remover)
**Install Type:** git-clone

---

### ComfyUI-Replicate

**Description:**

Run [a/Replicate models](https://replicate.com/explore) in ComfyUI.

- **Author:** fofr
- **Repository:** [https://github.com/replicate/comfyui-replicate](https://github.com/replicate/comfyui-replicate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it allows running Replicate models in ComfyUI.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/replicate/comfyui-replicate](https://github.com/replicate/comfyui-replicate)
**Install Type:** git-clone

---

### ComfyUI-RGT

**Description:**

This repo cast Recursive Generalization Transformer for Image Super-Resolution to ComfyUI, the original [a/paper link](https://arxiv.org/abs/2303.06373) and [a/github link](https://github.com/zhengchen1999/RGT)

- **Author:** viperyl
- **Repository:** [https://github.com/viperyl/ComfyUI-RGT](https://github.com/viperyl/ComfyUI-RGT)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is highly relevant as it provides Recursive Generalization Transformer for Image Super-Resolution, which can be used in conjunction with a mask for inpainting.

### Metadata
**Author:** viperyl
**Repository:** [https://github.com/viperyl/ComfyUI-RGT](https://github.com/viperyl/ComfyUI-RGT)
**Install Type:** git-clone

---

### comfyui-ricklove

**Description:**

Nodes: Image Crop and Resize by Mask, Image Uncrop, Image Shadow, Optical Flow (Dip), Warp Image with Flow, Image Threshold (Channels), Finetune Variable, Finetune Analyze, Finetune Analyze Batch, ... Misc ComfyUI nodes by Rick Love

- **Author:** ricklove
- **Repository:** [https://github.com/ricklove/comfyui-ricklove](https://github.com/ricklove/comfyui-ricklove)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node has multiple nodes that are directly related to the workflow goal, including Image Crop and Resize by Mask, making it very useful for inpainting.

### Metadata
**Author:** ricklove
**Repository:** [https://github.com/ricklove/comfyui-ricklove](https://github.com/ricklove/comfyui-ricklove)
**Install Type:** git-clone

---

### ComfyUI-RMBG

**Description:**

A ComfyUI node for removing image backgrounds using RMBG-2.0

- **Author:** 1038lab
- **Repository:** [https://github.com/1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly addresses the workflow goal by removing image backgrounds using RMBG-2.0.

### Metadata
**Author:** 1038lab
**Repository:** [https://github.com/1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)
**Install Type:** git-clone

---

### ComfyUI-Ruyi

**Description:**

ComfyUI wrapper nodes for Ruyi, an image-to-video model by CreateAI.

- **Author:** IamCreateAI
- **Repository:** [https://github.com/IamCreateAI/Ruyi-Models](https://github.com/IamCreateAI/Ruyi-Models)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is a wrapper for an image-to-video model that can be used in conjunction with inpainting and mask input.

### Metadata
**Author:** IamCreateAI
**Repository:** [https://github.com/IamCreateAI/Ruyi-Models](https://github.com/IamCreateAI/Ruyi-Models)
**Install Type:** git-clone

---

### ComfyUI-SAM2-Realtime

**Description:**

NODES:(Down)Load SAM2-Realtime Model, Sam2RealtimeSegmentation

- **Author:** pschroedl
- **Repository:** [https://github.com/pschroedl/ComfyUI-SAM2-Realtime](https://github.com/pschroedl/ComfyUI-SAM2-Realtime)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node loads a segmentation model, but its relevance to inpainting with mask input is unclear without more information about its capabilities.

### Metadata
**Author:** pschroedl
**Repository:** [https://github.com/pschroedl/ComfyUI-SAM2-Realtime](https://github.com/pschroedl/ComfyUI-SAM2-Realtime)
**Install Type:** git-clone

---

### comfyui-sasolver

**Description:**

SASolver for Comfyui. Adapted from [a/comfyanonymous/ComfyUI#4454](https://github.com/comfyanonymous/ComfyUI/pull/4454) and [a/https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler](https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler)

- **Author:** mira-6
- **Repository:** [https://github.com/mira-6/comfyui-sasolver](https://github.com/mira-6/comfyui-sasolver)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This SASolver node can be used to optimize and solve the inpainting problem with a mask input, making it moderately useful for this workflow goal.

### Metadata
**Author:** mira-6
**Repository:** [https://github.com/mira-6/comfyui-sasolver](https://github.com/mira-6/comfyui-sasolver)
**Install Type:** git-clone

---

### ComfyUI-SaveImageWithMetaData

**Description:**

Add a node to save images with metadata (PNGInfo) extracted from the input values of each node.
Since the values are extracted dynamically, values output by various extension nodes can be added to metadata.

- **Author:** nkchocoai
- **Repository:** [https://github.com/nkchocoai/ComfyUI-SaveImageWithMetaData](https://github.com/nkchocoai/ComfyUI-SaveImageWithMetaData)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows saving images with metadata extracted from the input values of each node, which could be useful for preserving information about the inpainting process and its parameters.

### Metadata
**Author:** nkchocoai
**Repository:** [https://github.com/nkchocoai/ComfyUI-SaveImageWithMetaData](https://github.com/nkchocoai/ComfyUI-SaveImageWithMetaData)
**Install Type:** git-clone

---

### ComfyUI-ScaleToTargetMegapixels

**Description:**

NODES:ScaleToTargetMegapixels.

- **Author:** troyxmccall
- **Repository:** [https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels](https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly scales images to target megapixels, which is essential for adjusting image sizes in the inpainting workflow.

### Metadata
**Author:** troyxmccall
**Repository:** [https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels](https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels)
**Install Type:** git-clone

---

### ComfyUI-ScheduledGuider-Ext

**Description:**

NODES:ScheduledCFGGuider, PerpNegScheduledCFGGuider, CosineScheduler, Add zSNR Sigma max, InvertSigmas, ConcatSigmas, OffsetSigmas

- **Author:** mfg637
- **Repository:** [https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext](https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides various scheduled CFG guider nodes that can be used to optimize the inpainting process with mask input.

### Metadata
**Author:** mfg637
**Repository:** [https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext](https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext)
**Install Type:** git-clone

---

### ComfyUI-SD3-nodes

**Description:**

Nodes that support Stable Diffusion 3 Medium better.

- **Author:** Sida Liu
- **Repository:** [https://github.com/liusida/ComfyUI-SD3-nodes](https://github.com/liusida/ComfyUI-SD3-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node provides nodes that support Stable Diffusion 3 Medium, which can be used as a supporting tool for the inpainting workflow with mask input.

### Metadata
**Author:** Sida Liu
**Repository:** [https://github.com/liusida/ComfyUI-SD3-nodes](https://github.com/liusida/ComfyUI-SD3-nodes)
**Install Type:** git-clone

---

### ComfyUI-SD3-Powerlab

**Description:**

Nodes:Render SD3 Attention, SD3 Attention To Image, SD3 Image Into Attention.

- **Author:** G-370
- **Repository:** [https://github.com/G-370/ComfyUI-SD3-Powerlab](https://github.com/G-370/ComfyUI-SD3-Powerlab)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly supports inpainting with mask input through SD3 Attention nodes.

### Metadata
**Author:** G-370
**Repository:** [https://github.com/G-370/ComfyUI-SD3-Powerlab](https://github.com/G-370/ComfyUI-SD3-Powerlab)
**Install Type:** git-clone

---

### ComfyUI-SD3LatentSelectRes

**Description:**

You'll get a new node called SD3 Latent Select Resolution, you can pick the x and y sizes from a list.

- **Author:** GavChap
- **Repository:** [https://github.com/GavChap/ComfyUI-SD3LatentSelectRes](https://github.com/GavChap/ComfyUI-SD3LatentSelectRes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Provides a crucial feature of selecting resolution sizes for inpainting workflows.

### Metadata
**Author:** GavChap
**Repository:** [https://github.com/GavChap/ComfyUI-SD3LatentSelectRes](https://github.com/GavChap/ComfyUI-SD3LatentSelectRes)
**Install Type:** git-clone

---

### ComfyUI-SDXL-EmptyLatentImage

**Description:**

Nodes:SDXL Empty Latent Image. An extension node for ComfyUI that allows you to select a resolution from the pre-defined json files and output a Latent Image.

- **Author:** shingo1228
- **Repository:** [https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage](https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Supports the creation of latent images but may not directly contribute to inpainting with mask input.

### Metadata
**Author:** shingo1228
**Repository:** [https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage](https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage)
**Install Type:** git-clone

---

### ComfyUI-seam-carving

**Description:**

Nodes: Image Resize (seam carving). Seam carving (image resize) for ComfyUI. Based on [a/https://github.com/li-plus/seam-carving](https://github.com/li-plus/seam-carving). With seam carving algorithm, the image could be intelligently resized while keeping the important contents undistorted. The carving process could be further guided, so that an object could be removed from the image without apparent artifacts.

- **Author:** spinagon
- **Repository:** [https://github.com/spinagon/ComfyUI-seam-carving](https://github.com/spinagon/ComfyUI-seam-carving)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Offers an alternative resizing method (seam carving) that could be useful in certain inpainting scenarios.

### Metadata
**Author:** spinagon
**Repository:** [https://github.com/spinagon/ComfyUI-seam-carving](https://github.com/spinagon/ComfyUI-seam-carving)
**Install Type:** git-clone

---

### ComfyUI-SeeCoder

**Description:**

ComfyUI nodes to use the SeeCoder from [a/Prompt-Free-Diffusion](https://github.com/SHI-Labs/Prompt-Free-Diffusion)

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-SeeCoder](https://github.com/logtd/ComfyUI-SeeCoder)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides ComfyUI nodes to use SeeCoder from Prompt-Free-Diffusion, which can be used for inpainting tasks with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-SeeCoder](https://github.com/logtd/ComfyUI-SeeCoder)
**Install Type:** git-clone

---

### ComfyUI-SEGAttention

**Description:**

Nodes to use [a/Smoothed Energy Guidance](https://github.com/SusungHong/SEG-SDXL) for ComfyUI.

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-SEGAttention](https://github.com/logtd/ComfyUI-SEGAttention)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides nodes to use Smoothed Energy Guidance for ComfyUI, which can be used for inpainting tasks with mask input.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-SEGAttention](https://github.com/logtd/ComfyUI-SEGAttention)
**Install Type:** git-clone

---

### comfyui-SegGPT

**Description:**

SegGPT model for comfyui,segmentation everything with mask prompt. Download (https://huggingface.co/BAAI/SegGPT/blob/main/seggpt_vit_large.pth) in this node path.

- **Author:** nicehero
- **Repository:** [https://github.com/nicehero/comfyui-SegGPT](https://github.com/nicehero/comfyui-SegGPT)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** SegGPT model is specifically designed for segmentation tasks with mask prompts, making it highly relevant to the inpainting workflow.

### Metadata
**Author:** nicehero
**Repository:** [https://github.com/nicehero/comfyui-SegGPT](https://github.com/nicehero/comfyui-SegGPT)
**Install Type:** git-clone

---

### ComfyUI-segment-anything-2

**Description:**

Nodes to use [a/segment-anything-2](https://github.com/facebookresearch/segment-anything-2) for image or video segmentation.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI-segment-anything-2 node uses a state-of-the-art segmentation model and can handle both image and video inputs, making it essential for this workflow.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2)
**Install Type:** git-clone

---

### comfyui-selector

**Description:**

Nodes:Selector. Quick and dirty parameter generator node for ComfyUI.

- **Author:** exdysa
- **Repository:** [https://github.com/exdysa/comfyui-selector](https://github.com/exdysa/comfyui-selector)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Comfyui-selector node can generate parameters quickly but does not have a direct connection to the inpainting workflow with mask input.

### Metadata
**Author:** exdysa
**Repository:** [https://github.com/exdysa/comfyui-selector](https://github.com/exdysa/comfyui-selector)
**Install Type:** git-clone

---

### ComfyUI-ShadertoyGL

**Description:**

Nodes:Shadertoy, Shader, ColorChannelOffset.

- **Author:** quadme7macoon
- **Repository:** [https://github.com/e7mac/ComfyUI-ShadertoyGL](https://github.com/e7mac/ComfyUI-ShadertoyGL)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be very useful for the inpainting workflow with mask input as it allows for Shadertoy integration, potentially enabling complex shader-based processing of the image and its mask.

### Metadata
**Author:** quadme7macoon
**Repository:** [https://github.com/e7mac/ComfyUI-ShadertoyGL](https://github.com/e7mac/ComfyUI-ShadertoyGL)
**Install Type:** git-clone

---

### ComfyUI-SimDA

**Description:**

Nodes:SimDATrain, SimDALoader, SimDARun, VHS_FILENAMES_STRING_SimDA

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-SimDA](https://github.com/chaojie/ComfyUI-SimDA)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a set of nodes specifically designed for SimDA, which can be used in conjunction with the inpainting workflow with mask input.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-SimDA](https://github.com/chaojie/ComfyUI-SimDA)
**Install Type:** git-clone

---

### ComfyUI-SimpleLogger

**Description:**

A simple node to save your history in html file. I saves the WorkFlow with all it's input values so you can duplicate it later.

- **Author:** moustafa-nasr
- **Repository:** [https://github.com/moustafa-nasr/ComfyUI-SimpleLogger](https://github.com/moustafa-nasr/ComfyUI-SimpleLogger)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for logging and tracking the workflow history, which can be helpful for debugging and duplicating successful runs.

### Metadata
**Author:** moustafa-nasr
**Repository:** [https://github.com/moustafa-nasr/ComfyUI-SimpleLogger](https://github.com/moustafa-nasr/ComfyUI-SimpleLogger)
**Install Type:** git-clone

---

### ComfyUI-Small-Utility

**Description:**

Context menu extension for CLIPTextEncode (sort prompt), EmptyLatentImage (sdxl size selector).

- **Author:** changwook987
- **Repository:** [https://github.com/changwook987/ComfyUI-Small-Utility](https://github.com/changwook987/ComfyUI-Small-Utility)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant as it extends context menu functionality but does not directly contribute to the inpainting process.

### Metadata
**Author:** changwook987
**Repository:** [https://github.com/changwook987/ComfyUI-Small-Utility](https://github.com/changwook987/ComfyUI-Small-Utility)
**Install Type:** git-clone

---

### ComfyUI-SmartCrop

**Description:**

a ComfyUI Custom Node for [a/smartcrop.py](https://github.com/smartcrop/smartcrop.py)

- **Author:** turkyden
- **Repository:** [https://github.com/turkyden/ComfyUI-SmartCrop](https://github.com/turkyden/ComfyUI-SmartCrop)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can help crop and align the image with the mask.

### Metadata
**Author:** turkyden
**Repository:** [https://github.com/turkyden/ComfyUI-SmartCrop](https://github.com/turkyden/ComfyUI-SmartCrop)
**Install Type:** git-clone

---

### ComfyUI-SnakeOil

**Description:**

Use [a/Doctor Diffusion's snake oil nLoRAs](https://civitai.com/models/987843) as well as [a/other negative LoRAs](https://civitai.com/models/186617/doctor-diffusions-negative-xl-lora) easily within ComfyUI.

- **Author:** Doctor Diffusion
- **Repository:** [https://github.com/DoctorDiffusion/ComfyUI-SnakeOil](https://github.com/DoctorDiffusion/ComfyUI-SnakeOil)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides access to snake oil nLoRAs and negative LoRAs specifically designed for inpainting tasks with mask input.

### Metadata
**Author:** Doctor Diffusion
**Repository:** [https://github.com/DoctorDiffusion/ComfyUI-SnakeOil](https://github.com/DoctorDiffusion/ComfyUI-SnakeOil)
**Install Type:** git-clone

---

### comfyui-snek-nodes

**Description:**

NODES:Aesthetics, Aesthetics V2, Load AI Toolkit Latent Flux, Send_to_Eagle

- **Author:** sneccc
- **Repository:** [https://github.com/sneccc/comfyui-snek-nodes](https://github.com/sneccc/comfyui-snek-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some nodes that may be useful for image processing, but it does not explicitly mention inpainting functionality.

### Metadata
**Author:** sneccc
**Repository:** [https://github.com/sneccc/comfyui-snek-nodes](https://github.com/sneccc/comfyui-snek-nodes)
**Install Type:** git-clone

---

### comfyui-some-image-processing-stuff

**Description:**

Some ComfyUI nodes that provide some image-processing functionality. Resampling, Color Grading, Inpainting, ...

- **Author:** wmpmiles
- **Repository:** [https://github.com/wmpmiles/comfyui-some-image-processing-stuff](https://github.com/wmpmiles/comfyui-some-image-processing-stuff)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node is a collection of ComfyUI nodes specifically designed for image-processing tasks, including inpainting with mask input.

### Metadata
**Author:** wmpmiles
**Repository:** [https://github.com/wmpmiles/comfyui-some-image-processing-stuff](https://github.com/wmpmiles/comfyui-some-image-processing-stuff)
**Install Type:** git-clone

---

### ComfyUI-SoundHub

**Description:**

ComfyUI-SoundHub is a collection of audio processing nodes designed for ComfyUI, enabling seamless audio processing and generation within your ComfyUI workflows.

- **Author:** Yuan-ManX
- **Repository:** [https://github.com/Yuan-ManX/ComfyUI-SoundHub](https://github.com/Yuan-ManX/ComfyUI-SoundHub)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI-SoundHub is a collection of audio processing nodes designed for ComfyUI, which can be useful for an inpainting workflow with mask input.

### Metadata
**Author:** Yuan-ManX
**Repository:** [https://github.com/Yuan-ManX/ComfyUI-SoundHub](https://github.com/Yuan-ManX/ComfyUI-SoundHub)
**Install Type:** git-clone

---

### ComfyUI-Stereopsis

**Description:**

This initiative represents a solo venture dedicated to integrating a stereopsis effect within ComfyUI (Stable Diffusion). Presently, the project is focused on the refinement of node categorization within a unified framework, as it is in the early stages of development. However, it has achieved functionality in a fundamental capacity. By processing a video through the Side-by-Side (SBS) node and applying Frame Delay to one of the inputs, it facilitates the creation of a stereopsis effect. This effect is compatible with any Virtual Reality headset that supports SBS video playback, offering a practical application in immersive media experiences.

- **Author:** IsItDanOrAi
- **Repository:** [https://github.com/IsItDanOrAi/ComfyUI-Stereopsis](https://github.com/IsItDanOrAi/ComfyUI-Stereopsis)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a stereopsis effect that can be used in immersive media experiences and is compatible with Virtual Reality headsets supporting SBS video playback.

### Metadata
**Author:** IsItDanOrAi
**Repository:** [https://github.com/IsItDanOrAi/ComfyUI-Stereopsis](https://github.com/IsItDanOrAi/ComfyUI-Stereopsis)
**Install Type:** git-clone

---

### ComfyUI-StringsAndThings

**Description:**

EA collection of ComfyUI custom nodes for formatting and debugging string data with the intention of collecting generation data to be processed by a custom node pack like comfy-image-saver, as well as miscellaneous extra nodes to experiment with.

- **Author:** PressWagon
- **Repository:** [https://github.com/PressWagon/ComfyUI-StringsAndThings](https://github.com/PressWagon/ComfyUI-StringsAndThings)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this collection of nodes includes some string formatting and debugging tools, it may have limited relevance to the specific task of inpainting with mask input.

### Metadata
**Author:** PressWagon
**Repository:** [https://github.com/PressWagon/ComfyUI-StringsAndThings](https://github.com/PressWagon/ComfyUI-StringsAndThings)
**Install Type:** git-clone

---

### ComfyUI-StyleTransferPlus

**Description:**

Nodes:Neural Neighbor, CAST, EFDM, MicroAST, Coral Color Transfer.

- **Author:** Fuou Marinas
- **Repository:** [https://github.com/FuouM/ComfyUI-StyleTransferPlus](https://github.com/FuouM/ComfyUI-StyleTransferPlus)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides StyleShot functionality which can be used for inpainting tasks and supports mask input.

### Metadata
**Author:** Fuou Marinas
**Repository:** [https://github.com/FuouM/ComfyUI-StyleTransferPlus](https://github.com/FuouM/ComfyUI-StyleTransferPlus)
**Install Type:** git-clone

---

### ComfyUI-sudo-latent-upscale

**Description:**

Directly upscaling inside the latent space. Model was trained for SD1.5 and drawn content. Might add new architectures or update models at some point. This took heavy inspriration from [city96/SD-Latent-Upscaler](https://github.com/city96/SD-Latent-Upscaler) and [Ttl/ComfyUi_NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale). 

- **Author:** styler00dollar
- **Repository:** [https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale](https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly upscaling inside the latent space which is essential for the inpainting workflow with mask input.

### Metadata
**Author:** styler00dollar
**Repository:** [https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale](https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale)
**Install Type:** git-clone

---

### ComfyUI-SUPIR

**Description:**

Wrapper nodes to use SUPIR upscaling process in ComfyUI

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-SUPIR](https://github.com/kijai/ComfyUI-SUPIR)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly uses SUPIR upscaling process which is relevant to inpainting with mask input.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-SUPIR](https://github.com/kijai/ComfyUI-SUPIR)
**Install Type:** git-clone

---

### ComfyUI-SVDResizer

**Description:**

SVDResizer is a helper for resizing the source image, according to the sizes enabled in Stable Video Diffusion. The rationale behind the possibility of changing the size of the image in steps between the ranges of 576 and 1024, is the use of the greatest common denominator of these two numbers which is 64. SVD is lenient with resizing that adheres to this rule, so the chance of coherent video that is not the standard size of 576X1024 is greater. It is advisable to keep the value 1024 constant and play with the second size to maintain the stability of the result.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-SVDResizer](https://github.com/ShmuelRonen/ComfyUI-SVDResizer)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Helps with resizing images according to SVD requirements which is useful for maintaining stability in the inpainting process.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-SVDResizer](https://github.com/ShmuelRonen/ComfyUI-SVDResizer)
**Install Type:** git-clone

---

### ComfyUI-SVGview

**Description:**

Nodes:Preview SVG

- **Author:** Parameshvadivel
- **Repository:** [https://github.com/Parameshvadivel/ComfyUI-SVGview](https://github.com/Parameshvadivel/ComfyUI-SVGview)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can preview SVG files which could be useful in an inpainting workflow.

### Metadata
**Author:** Parameshvadivel
**Repository:** [https://github.com/Parameshvadivel/ComfyUI-SVGview](https://github.com/Parameshvadivel/ComfyUI-SVGview)
**Install Type:** git-clone

---

### ComfyUI-tagger

**Description:**

Nodes to use Florence2 VLM for image vision tasks: object detection, captioning, segmentation and ocr

- **Author:** jsonL
- **Repository:** [https://github.com/StarMagicAI/comfyui_tagger](https://github.com/StarMagicAI/comfyui_tagger)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node has a broad range of applications, its primary use case is object detection and captioning, making it marginally relevant for an inpainting workflow.

### Metadata
**Author:** jsonL
**Repository:** [https://github.com/StarMagicAI/comfyui_tagger](https://github.com/StarMagicAI/comfyui_tagger)
**Install Type:** git-clone

---

### ComfyUI-tbox

**Description:**

Nodes:ImageLoader, ImageSaver, ImagesSaver, ImageResize, ImageSize, GFPGANNode, MaskAddNode, Video Load, ...

- **Author:** ai-shizuka
- **Repository:** [https://github.com/ai-shizuka/ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI-tbox contains various image processing nodes including MaskAddNode which is directly relevant to the inpainting workflow goal.

### Metadata
**Author:** ai-shizuka
**Repository:** [https://github.com/ai-shizuka/ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox)
**Install Type:** git-clone

---

### ComfyUI-TCD-scheduler

**Description:**

ComfyUI Custom Sampler nodes that implement Zheng et al.'s Trajectory Consistency Distillation based on [a/https://mhh0318.github.io/tcd](https://mhh0318.github.io/tcd)

- **Author:** dfl
- **Repository:** [https://github.com/dfl/comfyui-tcd-scheduler](https://github.com/dfl/comfyui-tcd-scheduler)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it implements Trajectory Consistency Distillation.

### Metadata
**Author:** dfl
**Repository:** [https://github.com/dfl/comfyui-tcd-scheduler](https://github.com/dfl/comfyui-tcd-scheduler)
**Install Type:** git-clone

---

### Comfyui-Template-Loader

**Description:**

Easily Load Your Frequently Used Prompts in ComfyUI
With ComfyUI Template Loader, managing and reusing your favorite prompts has never been simpler. Save time and streamline your workflow by loading your go-to templates with just a few clicks!

- **Author:** r3dsd
- **Repository:** [https://github.com/r3dsd/comfyui-template-loader](https://github.com/r3dsd/comfyui-template-loader)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node allows loading frequently used prompts in ComfyUI, which can be useful for managing and reusing templates in the inpainting workflow.

### Metadata
**Author:** r3dsd
**Repository:** [https://github.com/r3dsd/comfyui-template-loader](https://github.com/r3dsd/comfyui-template-loader)
**Install Type:** git-clone

---

### ComfyUI-TextOverlay

**Description:**

This extension provides a node that allows you to overlay text on an image or a batch of images with support for custom fonts and styles.

- **Author:** munkyfoot
- **Repository:** [https://github.com/Munkyfoot/ComfyUI-TextOverlay](https://github.com/Munkyfoot/ComfyUI-TextOverlay)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for overlaying text on images or batches of images in an inpainting workflow.

### Metadata
**Author:** munkyfoot
**Repository:** [https://github.com/Munkyfoot/ComfyUI-TextOverlay](https://github.com/Munkyfoot/ComfyUI-TextOverlay)
**Install Type:** git-clone

---

### ComfyUI-Thumbnails

**Description:**

Load Image thumbnails, delete images, browse input subfolders.

- **Author:** audioscavenger
- **Repository:** [https://github.com/audioscavenger/ComfyUI-Thumbnails](https://github.com/audioscavenger/ComfyUI-Thumbnails)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant as it loads image thumbnails but does not directly contribute to inpainting with mask input.

### Metadata
**Author:** audioscavenger
**Repository:** [https://github.com/audioscavenger/ComfyUI-Thumbnails](https://github.com/audioscavenger/ComfyUI-Thumbnails)
**Install Type:** git-clone

---

### ComfyUI-TimestepShiftModel

**Description:**

This is a ComfyUI implementation of the timestep shift technique used in [a/NitroFusion: High-Fidelity Single-Step Diffusion through Dynamic Adversarial Training.](https://arxiv.org/abs/2412.02030)
For more details, visit the official [a/NitroFusion GitHub repository](https://github.com/ChenDarYen/NitroFusion).

- **Author:** ChenDarYen
- **Repository:** [https://github.com/ChenDarYen/ComfyUI-TimestepShiftModel](https://github.com/ChenDarYen/ComfyUI-TimestepShiftModel)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node seems highly relevant and useful for the inpainting workflow with mask input. It implements a timestep shift technique used in high-fidelity single-step diffusion models.

### Metadata
**Author:** ChenDarYen
**Repository:** [https://github.com/ChenDarYen/ComfyUI-TimestepShiftModel](https://github.com/ChenDarYen/ComfyUI-TimestepShiftModel)
**Install Type:** git-clone

---

### comfyui-toml-prompt

**Description:**

Encode Prompt in TOML for ComfyUI.

- **Author:** morino-kumasan
- **Repository:** [https://github.com/morino-kumasan/comfyui-toml-prompt](https://github.com/morino-kumasan/comfyui-toml-prompt)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can encode prompts in TOML format which could be useful for configuring ComfyUI nodes for inpainting with mask input.

### Metadata
**Author:** morino-kumasan
**Repository:** [https://github.com/morino-kumasan/comfyui-toml-prompt](https://github.com/morino-kumasan/comfyui-toml-prompt)
**Install Type:** git-clone

---

### Comfyui-Toolbox

**Description:**

Nodes:Preview Json, Save Json, Test Json Preview, ... preview and save nodes

- **Author:** zcfrank1st
- **Repository:** [https://github.com/zcfrank1st/Comfyui-Toolbox](https://github.com/zcfrank1st/Comfyui-Toolbox)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** This node provides preview and save functionality which could be useful for testing and refining inpainting with mask input workflows.

### Metadata
**Author:** zcfrank1st
**Repository:** [https://github.com/zcfrank1st/Comfyui-Toolbox](https://github.com/zcfrank1st/Comfyui-Toolbox)
**Install Type:** git-clone

---

### ComfyUI-ToonCrafter

**Description:**

This project is used to enable [a/ToonCrafter](https://github.com/ToonCrafter/ToonCrafter) to be used in ComfyUI.
You can use it to achieve generative keyframe animation
And use it in Blender for animation rendering and prediction

- **Author:** AIGODLIKE
- **Repository:** [https://github.com/AIGODLIKE/ComfyUI-ToonCrafter](https://github.com/AIGODLIKE/ComfyUI-ToonCrafter)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly enables generative keyframe animation which can be used in inpainting workflows.

### Metadata
**Author:** AIGODLIKE
**Repository:** [https://github.com/AIGODLIKE/ComfyUI-ToonCrafter](https://github.com/AIGODLIKE/ComfyUI-ToonCrafter)
**Install Type:** git-clone

---

### ComfyUI-ToSVG

**Description:**

This project converts raster images into SVG format using the [a/VTracer](https://github.com/visioncortex/vtracer) library. It's a handy tool for designers and developers who need to work with vector graphics programmatically.

- **Author:** Yanick112
- **Repository:** [https://github.com/Yanick112/ComfyUI-ToSVG](https://github.com/Yanick112/ComfyUI-ToSVG)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the inpainting workflow by converting raster images into SVG format which can be used as a mask for inpainting.

### Metadata
**Author:** Yanick112
**Repository:** [https://github.com/Yanick112/ComfyUI-ToSVG](https://github.com/Yanick112/ComfyUI-ToSVG)
**Install Type:** git-clone

---

### ComfyUI-Transceiver📡

**Description:**

Transceiver is a python library that swiftly exchanges fundamental data structures, specifically numpy arrays, between processes, optimizing AI inference tasks that utilize ComfyUI.

- **Author:** nat-chan
- **Repository:** [https://github.com/nat-chan/comfyui-transceiver](https://github.com/nat-chan/comfyui-transceiver)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Transceiver can efficiently exchange numpy arrays between processes, which is crucial for optimizing AI inference tasks in the inpainting workflow with mask input.

### Metadata
**Author:** nat-chan
**Repository:** [https://github.com/nat-chan/comfyui-transceiver](https://github.com/nat-chan/comfyui-transceiver)
**Install Type:** git-clone

---

### ComfyUI-TrollSuite

**Description:**

Nodes: BinaryImageMask, ImagePadding, LoadLastCreatedImage, RandomMask, TransparentImage.

- **Author:** oyvindg
- **Repository:** [https://github.com/oyvindg/ComfyUI-TrollSuite](https://github.com/oyvindg/ComfyUI-TrollSuite)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it contains several nodes that can be used to create or manipulate masks, which are essential components of the inpainting workflow.

### Metadata
**Author:** oyvindg
**Repository:** [https://github.com/oyvindg/ComfyUI-TrollSuite](https://github.com/oyvindg/ComfyUI-TrollSuite)
**Install Type:** git-clone

---

### ComfyUI-ultimate-openpose-estimator

**Description:**

Super fast tensorrt performance with accuate pose estimation of dwpose model, giving the detecting threshold control, plus pose image render and pose json format output. Fine control for pose plotting.

- **Author:** westNeighbor
- **Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides pose estimation capabilities that can be used in conjunction with a mask input for inpainting workflows.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator)
**Install Type:** git-clone

---

### ComfyUI-ultimate-openpose-render

**Description:**

The ultimate openpose render node for ComfyUI with flexible input, output and adjustment.

- **Author:** westNeighbor
- **Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node offers flexible rendering options and adjustment controls, making it useful for post-processing in an inpainting workflow with mask input.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render)
**Install Type:** git-clone

---

### ComfyUI-UltraPixel

**Description:**

Implementation of UltraPixel on ComfyUI

- **Author:** 2kpr
- **Repository:** [https://github.com/2kpr/ComfyUI-UltraPixel](https://github.com/2kpr/ComfyUI-UltraPixel)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is an implementation of UltraPixel which supports image inpainting and could be useful for the specified workflow goal.

### Metadata
**Author:** 2kpr
**Repository:** [https://github.com/2kpr/ComfyUI-UltraPixel](https://github.com/2kpr/ComfyUI-UltraPixel)
**Install Type:** git-clone

---

### ComfyUI-Unload-Model

**Description:**

For unloading a model or all models, using the memory management that is already present in ComfyUI. Copied from [a/https://github.com/willblaschko/ComfyUI-Unload-Models](https://github.com/willblaschko/ComfyUI-Unload-Models) but without the unnecessary extra stuff.

- **Author:** SeanScripts
- **Repository:** [https://github.com/SeanScripts/ComfyUI-Unload-Model](https://github.com/SeanScripts/ComfyUI-Unload-Model)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for unloading models after use in the inpainting workflow with mask input.

### Metadata
**Author:** SeanScripts
**Repository:** [https://github.com/SeanScripts/ComfyUI-Unload-Model](https://github.com/SeanScripts/ComfyUI-Unload-Model)
**Install Type:** git-clone

---

### comfyui-upscale-by-model

**Description:**

This custom node allow upscaling an image by a factor using a model.

- **Author:** TheBill2001
- **Repository:** [https://github.com/TheBill2001/comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This custom node allows upscaling an image by a factor using a model which could be useful in conjunction with inpainting for achieving higher resolution outputs.

### Metadata
**Author:** TheBill2001
**Repository:** [https://github.com/TheBill2001/comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model)
**Install Type:** git-clone

---

### ComfyUI-Vextra-Nodes

**Description:**

Nodes: Pixel Sort, Swap Color Mode, Solid Color, Glitch This, Add Text To Image, Play Sound, Prettify Prompt, Generate Noise, Flatten Colors

- **Author:** diontimmer
- **Repository:** [https://github.com/diontimmer/ComfyUI-Vextra-Nodes](https://github.com/diontimmer/ComfyUI-Vextra-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Some of these nodes (e.g., Add Text To Image) could be useful in an inpainting workflow but the majority are not directly relevant to the goal.

### Metadata
**Author:** diontimmer
**Repository:** [https://github.com/diontimmer/ComfyUI-Vextra-Nodes](https://github.com/diontimmer/ComfyUI-Vextra-Nodes)
**Install Type:** git-clone

---

### ComfyUI-Video-Matting

**Description:**

A minimalistic implementation of [a/Robust Video Matting (RVM)](https://github.com/PeterL1n/RobustVideoMatting/) in ComfyUI

- **Author:** Fannovel16
- **Repository:** [https://github.com/Fannovel16/ComfyUI-Video-Matting](https://github.com/Fannovel16/ComfyUI-Video-Matting)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a minimalistic implementation of robust video matting, which can be used for inpainting with mask input.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/ComfyUI-Video-Matting](https://github.com/Fannovel16/ComfyUI-Video-Matting)
**Install Type:** git-clone

---

### ComfyUI-ViewData

**Description:**

A ComfyUI node that displays the type and contents of whatever is connected to the input. In the case of a Tensor object, it shows the shape instead of its value.

- **Author:** gremlation
- **Repository:** [https://github.com/gremlation/ComfyUI-ViewData](https://github.com/gremlation/ComfyUI-ViewData)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it displays the type and contents of whatever is connected to the input, which can be helpful in understanding the mask input.

### Metadata
**Author:** gremlation
**Repository:** [https://github.com/gremlation/ComfyUI-ViewData](https://github.com/gremlation/ComfyUI-ViewData)
**Install Type:** git-clone

---

### ComfyUI-Vivax-Nodes

**Description:**

Nodes:Inspect, Any String, Model From URL

- **Author:** vivax3794
- **Repository:** [https://github.com/vivax3794/ComfyUI-Vivax-Nodes](https://github.com/vivax3794/ComfyUI-Vivax-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some potentially useful nodes like Inspect or Model From URL, but they are not directly related to the inpainting workflow goal.

### Metadata
**Author:** vivax3794
**Repository:** [https://github.com/vivax3794/ComfyUI-Vivax-Nodes](https://github.com/vivax3794/ComfyUI-Vivax-Nodes)
**Install Type:** git-clone

---

### ComfyUI-VLM_Captions

**Description:**

A simple ComfyUI node that let's you use Claude or ChatGPT 4o's VLM capabilities to generate captions/tags for images.

- **Author:** 5x00
- **Repository:** [https://github.com/5x00/ComfyUI-VLM-Captions](https://github.com/5x00/ComfyUI-VLM-Captions)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is highly relevant for generating captions/tags for images using VLM capabilities, which could be useful in an inpainting workflow with mask input.

### Metadata
**Author:** 5x00
**Repository:** [https://github.com/5x00/ComfyUI-VLM-Captions](https://github.com/5x00/ComfyUI-VLM-Captions)
**Install Type:** git-clone

---

### ComfyUI-Vsgan

**Description:**

Nodes:Upscale Video Tensorrt

- **Author:** yuvraj108c
- **Repository:** [https://github.com/yuvraj108c/ComfyUI-Vsgan](https://github.com/yuvraj108c/ComfyUI-Vsgan)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is highly relevant and essential for the inpainting workflow with mask input as it provides a TensorRT-based upscale video functionality.

### Metadata
**Author:** yuvraj108c
**Repository:** [https://github.com/yuvraj108c/ComfyUI-Vsgan](https://github.com/yuvraj108c/ComfyUI-Vsgan)
**Install Type:** git-clone

---

### ComfyUI-WildPromptor

**Description:**

Create dynamic prompts with wildcard list.

- **Author:** 1038lab
- **Repository:** [https://github.com/1038lab/ComfyUI-WildPromptor](https://github.com/1038lab/ComfyUI-WildPromptor)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate dynamic prompts which could be useful in creating a custom inpainting prompt.

### Metadata
**Author:** 1038lab
**Repository:** [https://github.com/1038lab/ComfyUI-WildPromptor](https://github.com/1038lab/ComfyUI-WildPromptor)
**Install Type:** git-clone

---

### ComfyUI-X-Portrait-Nodes

**Description:**

Implementation of X-Portrait nodes for ComfyUI, animate portraits with an input video and a reference image.

- **Author:** akatz-ai
- **Repository:** [https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes](https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node can be used as a supporting tool for debugging or resuming the workflow in case of issues.

### Metadata
**Author:** akatz-ai
**Repository:** [https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes](https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes)
**Install Type:** git-clone

---

### Comfyui-Ycanvas

**Description:**

NODES:Canvas View

- **Author:** yichengup
- **Repository:** [https://github.com/yichengup/Comfyui-Ycanvas](https://github.com/yichengup/Comfyui-Ycanvas)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows visualization of the canvas, which can be useful for inspecting the inpainted result or providing user feedback during the workflow.

### Metadata
**Author:** yichengup
**Repository:** [https://github.com/yichengup/Comfyui-Ycanvas](https://github.com/yichengup/Comfyui-Ycanvas)
**Install Type:** git-clone

---

### ComfyUI-YOLO

**Description:**

Ultralytics-Powered Object Recognition for ComfyUI

- **Author:** kadirnar
- **Repository:** [https://github.com/kadirnar/ComfyUI-YOLO](https://github.com/kadirnar/ComfyUI-YOLO)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node enables object recognition, which can be used as a pre-processing step or in conjunction with inpainting to achieve more complex tasks.

### Metadata
**Author:** kadirnar
**Repository:** [https://github.com/kadirnar/ComfyUI-YOLO](https://github.com/kadirnar/ComfyUI-YOLO)
**Install Type:** git-clone

---

### comfyui_ab_sampler

**Description:**

Experimental sampler node. Sampling alternates between A and B inputs until only one remains, starting with A. B steps run over a 2x2 grid, where 3/4's of the grid are copies of the original input latent. When the optional mask is used, the region outside the defined roi is copied from the original latent at the end of every step.

- **Author:** bmad4ever
- **Repository:** [https://github.com/bmad4ever/comfyui_ab_samplercustom](https://github.com/bmad4ever/comfyui_ab_samplercustom)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This experimental sampler alternates between two inputs and uses a mask for region of interest (ROI) definition, making it very useful for the specified workflow goal.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_ab_samplercustom](https://github.com/bmad4ever/comfyui_ab_samplercustom)
**Install Type:** git-clone

---

### ComfyUI_Accessories

**Description:**

Get Mask Dimensions

- **Author:** var1ableX
- **Repository:** [https://github.com/var1ableX/ComfyUI_Accessories](https://github.com/var1ableX/ComfyUI_Accessories)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly retrieves mask dimensions, which is essential information required for inpainting with mask input.

### Metadata
**Author:** var1ableX
**Repository:** [https://github.com/var1ableX/ComfyUI_Accessories](https://github.com/var1ableX/ComfyUI_Accessories)
**Install Type:** git-clone

---

### ComfyUI_Aniportrait

**Description:**

implementation of [a/AniPortrait](https://github.com/Zejun-Yang/AniPortrait) generating of videos, includes self driven, face reenacment and audio driven with a reference image

- **Author:** FrankChieng
- **Repository:** [https://github.com/frankchieng/ComfyUI_Aniportrait](https://github.com/frankchieng/ComfyUI_Aniportrait)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can generate videos including face reenactment and audio-driven animations, making it highly useful for an inpainting workflow that requires dynamic content generation.

### Metadata
**Author:** FrankChieng
**Repository:** [https://github.com/frankchieng/ComfyUI_Aniportrait](https://github.com/frankchieng/ComfyUI_Aniportrait)
**Install Type:** git-clone

---

### ComfyUI_Anytext

**Description:**

Unofficial Simple And Rough Implementation Of [a/AnyText](https://github.com/tyxsspa/AnyText) and [a/Glyph-ByT5] (https://github.com/AIGText/Glyph-ByT5) and [a/JoyType](https://github.com/jdh-algo/JoyType)

- **Author:** zmwv823
- **Repository:** [https://github.com/zmwv823/ComfyUI_Anytext](https://github.com/zmwv823/ComfyUI_Anytext)
- **Install Type:** git-clone


### Applicability

**Score:** 50/100

**Reason:** This node can generate text from images and is moderately useful for an inpainting workflow that requires text insertion or manipulation.

### Metadata
**Author:** zmwv823
**Repository:** [https://github.com/zmwv823/ComfyUI_Anytext](https://github.com/zmwv823/ComfyUI_Anytext)
**Install Type:** git-clone

---

### ComfyUI_Auto_Caption

**Description:**

This report contains a 'load many images' node which is going to load the image set by the number of file names from smallest to largest, and the images will no longer be loaded in the wrong order! Setting index=0 makes it load from the first small value (image flie name) image, and index=2 will load them from the second image. Another node 'load images & resize' can resize the image by the first loaded image.

- **Author:** Cyber-BCat
- **Repository:** [https://github.com/Cyber-BCat/ComfyUI_Auto_Caption](https://github.com/Cyber-BCat/ComfyUI_Auto_Caption)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can be used to load multiple images but it does not directly contribute to the inpainting workflow with mask input. It might be useful as a supporting node for image processing tasks.

### Metadata
**Author:** Cyber-BCat
**Repository:** [https://github.com/Cyber-BCat/ComfyUI_Auto_Caption](https://github.com/Cyber-BCat/ComfyUI_Auto_Caption)
**Install Type:** git-clone

---

### ComfyUI_BadgerTools

**Description:**

Nodes:ImageOverlap-badger, FloatToInt-badger, IntToString-badger, FloatToString-badger, ImageNormalization-badger, ImageScaleToSide-badger, NovelToFizz-badger.

- **Author:** AbyssBadger0
- **Repository:** [https://github.com/AbyssBadger0/ComfyUI_BadgerTools](https://github.com/AbyssBadger0/ComfyUI_BadgerTools)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains several image processing tools that could be useful for inpainting with a mask input.

### Metadata
**Author:** AbyssBadger0
**Repository:** [https://github.com/AbyssBadger0/ComfyUI_BadgerTools](https://github.com/AbyssBadger0/ComfyUI_BadgerTools)
**Install Type:** git-clone

---

### ComfyUI_BiRefNet_ll

**Description:**

Sync with version of BiRefNet. NODES:AutoDownloadBiRefNetModel, LoadRembgByBiRefNetModel, RembgByBiRefNet.

- **Author:** lldacing
- **Repository:** [https://github.com/lldacing/ComfyUI_BiRefNet_ll](https://github.com/lldacing/ComfyUI_BiRefNet_ll)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for BiRefNet-based inpainting tasks, which aligns closely with the specified workflow goal.

### Metadata
**Author:** lldacing
**Repository:** [https://github.com/lldacing/ComfyUI_BiRefNet_ll](https://github.com/lldacing/ComfyUI_BiRefNet_ll)
**Install Type:** git-clone

---

### comfyui_bmab

**Description:**

BMAB for ComfyUI. BMAB is an custom nodes of ComfyUI and has the function of post-processing the generated image according to settings. If necessary, you can find and redraw people, faces, and hands, or perform functions such as resize, resample, and add noise. You can composite two images or perform the Upscale function.

- **Author:** portu-sim
- **Repository:** [https://github.com/portu-sim/comfyui_bmab](https://github.com/portu-sim/comfyui_bmab)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node has post-processing functions that can enhance the quality of the inpainted image.

### Metadata
**Author:** portu-sim
**Repository:** [https://github.com/portu-sim/comfyui_bmab](https://github.com/portu-sim/comfyui_bmab)
**Install Type:** git-clone

---

### ComfyUI_CAS

**Description:**

This extension provides nodes that allow experimentation with various elements (samplers, latent, activators, attenuator, scheulders, ...) of Stable Diffusion.

- **Author:** BenNarum
- **Repository:** [https://github.com/BenNarum/ComfyUI_CAS](https://github.com/BenNarum/ComfyUI_CAS)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides various elements of Stable Diffusion that can be used in an inpainting workflow with mask input.

### Metadata
**Author:** BenNarum
**Repository:** [https://github.com/BenNarum/ComfyUI_CAS](https://github.com/BenNarum/ComfyUI_CAS)
**Install Type:** git-clone

---

### ComfyUI_ColorMod

**Description:**

This extension currently has two sets of nodes - one set for editing the contrast/color of images and another set for saving images as 16 bit PNG files.

- **Author:** city96
- **Repository:** [https://github.com/city96/ComfyUI_ColorMod](https://github.com/city96/ComfyUI_ColorMod)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a way to use Cohere AI for text-based tasks, but its relevance to inpainting or mask input is limited.

### Metadata
**Author:** city96
**Repository:** [https://github.com/city96/ComfyUI_ColorMod](https://github.com/city96/ComfyUI_ColorMod)
**Install Type:** git-clone

---

### comfyui_custom_node_image

**Description:**

Nodes:ImageCropCircle.

- **Author:** jstit
- **Repository:** [https://github.com/jstit/comfyui_custom_node_image](https://github.com/jstit/comfyui_custom_node_image)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows image cropping and circular cropping, which could be useful as a supporting node for creating or manipulating the mask used in inpainting.

### Metadata
**Author:** jstit
**Repository:** [https://github.com/jstit/comfyui_custom_node_image](https://github.com/jstit/comfyui_custom_node_image)
**Install Type:** git-clone

---

### Comfyui_CXH_DeepLX

**Description:**

NODES:CXH_DeepLX_Free, CXH_DeepLX_translate

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/Comfyui_CXH_DeepLX](https://github.com/StartHua/Comfyui_CXH_DeepLX)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** This node provides access to CXH_DeepLX models, which are deep learning-based image processing tools that could be useful for inpainting tasks.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_CXH_DeepLX](https://github.com/StartHua/Comfyui_CXH_DeepLX)
**Install Type:** git-clone

---

### ComfyUI_Dados_Nodes

**Description:**

ComfyUI_Dados_Nodes is a collection of custom nodes for ComfyUI, designed to enhance functionality and provide integration with various services, including Pinterest. This privacy policy explains how these nodes handle user data.
NOTE: [a/privacy_policy](https://github.com/dadoirie/ComfyUI_Dados_Nodes/blob/master/privacy_policy.md)

- **Author:** dadoirie
- **Repository:** [https://github.com/dadoirie/ComfyUI_Dados_Nodes](https://github.com/dadoirie/ComfyUI_Dados_Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node collection may have some supporting nodes for the inpainting workflow, but its primary focus is on enhancing ComfyUI functionality and integrating with services like Pinterest.

### Metadata
**Author:** dadoirie
**Repository:** [https://github.com/dadoirie/ComfyUI_Dados_Nodes](https://github.com/dadoirie/ComfyUI_Dados_Nodes)
**Install Type:** git-clone

---

### comfyui_davcha

**Description:**

Nodes:SmartMask, ResizeCropFit, Percent Padding, SoftErosion, StringScheduleHelper, DStack, DavchaConditioningConcat, DavchaModelMergeSimple, DavchaCLIPMergeSimple, DavchaModelMergeSD1, DavchaModelMergeSDXL, ConditioningCompress... Some personal QoL and experimental nodes

- **Author:** dchatel
- **Repository:** [https://github.com/dchatel/comfyui_davcha](https://github.com/dchatel/comfyui_davcha)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a wide range of nodes that can be used in an inpainting workflow, including SmartMask and DavchaConditioningConcat.

### Metadata
**Author:** dchatel
**Repository:** [https://github.com/dchatel/comfyui_davcha](https://github.com/dchatel/comfyui_davcha)
**Install Type:** git-clone

---

### ComfyUI_Demucs

**Description:**

Using Demucs in comfyUI, make Music Source Separation

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Demucs](https://github.com/smthemex/ComfyUI_Demucs)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can separate music sources from an audio file.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Demucs](https://github.com/smthemex/ComfyUI_Demucs)
**Install Type:** git-clone

---

### ComfyUI_DepthFlow

**Description:**

comfyui custom node for depthflow
original depthflow website: [a/https://github.com/BrokenSource/DepthFlow](https://github.com/BrokenSource/DepthFlow)
check this for installation: [a/https://brokensrc.dev/get/](https://brokensrc.dev/get/)

- **Author:** cr7Por
- **Repository:** [https://github.com/cr7Por/ComfyUI_DepthFlow](https://github.com/cr7Por/ComfyUI_DepthFlow)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly implements DepthFlow, a relevant inpainting algorithm with mask input.

### Metadata
**Author:** cr7Por
**Repository:** [https://github.com/cr7Por/ComfyUI_DepthFlow](https://github.com/cr7Por/ComfyUI_DepthFlow)
**Install Type:** git-clone

---

### ComfyUI_Diffree

**Description:**

using diffree: Text-Guided Shape Free Object Inpainting with Diffusion Model

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Diffree](https://github.com/smthemex/ComfyUI_Diffree)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for text-guided shape-free object inpainting with diffusion model, making it highly relevant to the workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Diffree](https://github.com/smthemex/ComfyUI_Diffree)
**Install Type:** git-clone

---

### ComfyUI_DiffusionModel_fp8_converter

**Description:**

This is a custom node to convert only the Diffusion model part or CLIP model part to fp8 in ComfyUI.
VAE fp8 conversion is not supported.
The advantage of this node is that you do not need to separate unet/clip/vae in advance when converting to fp8, but can use the safetenros files that ComfyUI provides.

- **Author:** Shiba-2-shiba
- **Repository:** [https://github.com/Shiba-2-shiba/ComfyUI_DiffusionModel_fp8_converter](https://github.com/Shiba-2-shiba/ComfyUI_DiffusionModel_fp8_converter)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** While this node can convert parts of a Diffusion model to fp8 format, its direct relevance to the inpainting workflow with mask input is limited.

### Metadata
**Author:** Shiba-2-shiba
**Repository:** [https://github.com/Shiba-2-shiba/ComfyUI_DiffusionModel_fp8_converter](https://github.com/Shiba-2-shiba/ComfyUI_DiffusionModel_fp8_converter)
**Install Type:** git-clone

---

### comfyui_DSP_imagehelpers

**Description:**

Nodes: DSP Image Concat

- **Author:** dave-palt
- **Repository:** [https://github.com/dave-palt/comfyui_DSP_imagehelpers](https://github.com/dave-palt/comfyui_DSP_imagehelpers)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** DSP Image Concat is highly relevant as it can concatenate images which could be useful for combining the masked area and the inpainted image.

### Metadata
**Author:** dave-palt
**Repository:** [https://github.com/dave-palt/comfyui_DSP_imagehelpers](https://github.com/dave-palt/comfyui_DSP_imagehelpers)
**Install Type:** git-clone

---

### comfyui_dygen

**Description:**

NODES: DY Image Quantize, DY Image Cluster, DY Image Palette, DY Image Masks, Image List to Grid, DY Image Scaler, DY Random Lines, DY Adaptive Color Lines, DY Adaptive Color Circles, DY Adaptive Color Rectangles, DY Binary Pattern Stamper

- **Author:** dymokomi
- **Repository:** [https://github.com/dymokomi/comfyui_dygen](https://github.com/dymokomi/comfyui_dygen)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** DY Image Masks is moderately useful as it can generate masks which could be used for inpainting, but the other nodes in this repository do not seem directly relevant to the workflow goal.

### Metadata
**Author:** dymokomi
**Repository:** [https://github.com/dymokomi/comfyui_dygen](https://github.com/dymokomi/comfyui_dygen)
**Install Type:** git-clone

---

### comfyui_extra_api

**Description:**

Add more endpoints to make easy for utilizing ComfyUI API.

- **Author:** injet-zhou
- **Repository:** [https://github.com/injet-zhou/comfyui_extra_api](https://github.com/injet-zhou/comfyui_extra_api)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node adds more endpoints for utilizing ComfyUI API, it does not directly relate to the inpainting workflow or mask input.

### Metadata
**Author:** injet-zhou
**Repository:** [https://github.com/injet-zhou/comfyui_extra_api](https://github.com/injet-zhou/comfyui_extra_api)
**Install Type:** git-clone

---

### comfyui_face_parsing

**Description:**

This is a set of custom nodes for ComfyUI. The nodes utilize the [a/face parsing model](https://huggingface.co/jonathandinu/face-parsing) to provide detailed segmantation of face. To improve face segmantation accuracy, [a/yolov8 face model](https://huggingface.co/Bingsu/adetailer/) is used to first extract face from an image. There are also auxiliary nodes for image and mask processing. A guided filter is also provided for skin smoothing.

- **Author:** Ryuukeisyou
- **Repository:** [https://github.com/Ryuukeisyou/comfyui_face_parsing](https://github.com/Ryuukeisyou/comfyui_face_parsing)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides face parsing functionality which is directly relevant to inpainting with mask input.

### Metadata
**Author:** Ryuukeisyou
**Repository:** [https://github.com/Ryuukeisyou/comfyui_face_parsing](https://github.com/Ryuukeisyou/comfyui_face_parsing)
**Install Type:** git-clone

---

### ComfyUI_FaceShaper

**Description:**

Match two faces' shape before using other face swap nodes
Face-swapping tools typically only replace facial features during the swap, without altering the facial shape. When there is a significant difference in facial shape between the target person and the person in the original photo, the result of the face swap is less satisfactory.
This project is a small script that can first liquefy and stretch the face in the original photo according to the horizontal and vertical proportions of the target person's facial contour. The resulting image can be used as input for other face-swapping nodes.

- **Author:** fssorc
- **Repository:** [https://github.com/fssorc/ComfyUI_FaceShaper](https://github.com/fssorc/ComfyUI_FaceShaper)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node matches two faces" shape before using other face swap nodes, making it very useful for the specified workflow goal.

### Metadata
**Author:** fssorc
**Repository:** [https://github.com/fssorc/ComfyUI_FaceShaper](https://github.com/fssorc/ComfyUI_FaceShaper)
**Install Type:** git-clone

---

### comfyui_facetools

**Description:**

These custom nodes provide a rotation aware face extraction, paste back, and various face related masking options.

- **Author:** dchatel
- **Repository:** [https://github.com/dchatel/comfyui_facetools](https://github.com/dchatel/comfyui_facetools)
- **Install Type:** git-clone


### Applicability

**Score:** 88/100

**Reason:** These custom nodes provide a rotation aware face extraction and paste back which is moderately to very useful for inpainting with mask input.

### Metadata
**Author:** dchatel
**Repository:** [https://github.com/dchatel/comfyui_facetools](https://github.com/dchatel/comfyui_facetools)
**Install Type:** git-clone

---

### ComfyUI_FFT

**Description:**

Perform a Fast Fourier Transform on the image, and then users can freely select the filtering range to filter the image. The main function is to remove the grid patterns on the image, and it can also perform high-pass filtering and low-pass filtering. The detailed workflow is shown in the figure below. The PNG file contains the ComfyUI workflow.The working principle is similar to the FFT filter in Photoshop.

- **Author:** fssorc
- **Repository:** [https://github.com/fssorc/ComfyUI_FFT](https://github.com/fssorc/ComfyUI_FFT)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can perform Fast Fourier Transform and filtering operations which could be useful in removing grid patterns or noise from images before inpainting.

### Metadata
**Author:** fssorc
**Repository:** [https://github.com/fssorc/ComfyUI_FFT](https://github.com/fssorc/ComfyUI_FFT)
**Install Type:** git-clone

---

### comfyui_fk_server

**Description:**

🤗🤗🤗Comfyui Universal Translation Plugin (no longer requires adding various nodes, directly add translation function on the existing nodes), allowing Comfyui to support Chinese input and automatic translation for any long text input box, while adding error translation function (calling Baidu Translate), achieving translation freedom!

- **Author:** juehackr
- **Repository:** [https://github.com/juehackr/comfyui_fk_server](https://github.com/juehackr/comfyui_fk_server)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a universal translation function that can be used with long text input boxes in the inpainting workflow, making it essential for this goal.

### Metadata
**Author:** juehackr
**Repository:** [https://github.com/juehackr/comfyui_fk_server](https://github.com/juehackr/comfyui_fk_server)
**Install Type:** git-clone

---

### ComfyUI_FlipStreamViewer

**Description:**

ComfyUI_FlipStreamViewer is a tool that provides a viewer interface for flipping images with frame interpolation, allowing you to watch high-fidelity pseudo-videos without needing AnimateDiff.

- **Author:** sakura1bgx
- **Repository:** [https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer](https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a viewer interface for flipping images with frame interpolation, which can be used in the inpainting workflow to create high-fidelity pseudo-videos from mask inputs.

### Metadata
**Author:** sakura1bgx
**Repository:** [https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer](https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer)
**Install Type:** git-clone

---

### ComfyUI_Florence2SAM2

**Description:**

ComfyUI custom node implementing Florence 2 + Segment Anything Model 2, based on [a/SkalskiP's HuggingFace space](https://huggingface.co/spaces/SkalskiP/florence-sam)

- **Author:** rdancer
- **Repository:** [https://github.com/rdancer/ComfyUI_Florence2SAM2](https://github.com/rdancer/ComfyUI_Florence2SAM2)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly implements Florence 2 + Segment Anything Model 2, which is suitable for inpainting with mask input.

### Metadata
**Author:** rdancer
**Repository:** [https://github.com/rdancer/ComfyUI_Florence2SAM2](https://github.com/rdancer/ComfyUI_Florence2SAM2)
**Install Type:** git-clone

---

### ComfyUI_FluxMod

**Description:**

A modulation layer addon for Flux that reduces model size to 8.8B parameters without significant quality loss.

- **Author:** Horizon Team
- **Repository:** [https://github.com/lodestone-rock/ComfyUI_FluxMod](https://github.com/lodestone-rock/ComfyUI_FluxMod)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node reduces model size for Flux, it does not seem directly relevant to the inpainting workflow goal.

### Metadata
**Author:** Horizon Team
**Repository:** [https://github.com/lodestone-rock/ComfyUI_FluxMod](https://github.com/lodestone-rock/ComfyUI_FluxMod)
**Install Type:** git-clone

---

### ComfyUI_fnodes

**Description:**

ComfyUI_fnodes is a collection of custom nodes designed for ComfyUI. These nodes provide additional functionality that can enhance your ComfyUI workflows.
File manipulation tools, Image resizing tools, IPAdapter tools, Image processing tools, Mask tools, Face analysis tools, Sampler tools, Miscellaneous tools

- **Author:** syaofox
- **Repository:** [https://github.com/syaofox/ComfyUI_fnodes](https://github.com/syaofox/ComfyUI_fnodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a collection of tools that can be useful for various tasks in the inpainting workflow, including mask manipulation.

### Metadata
**Author:** syaofox
**Repository:** [https://github.com/syaofox/ComfyUI_fnodes](https://github.com/syaofox/ComfyUI_fnodes)
**Install Type:** git-clone

---

### comfyUI_FrequencySeparation_RGB-HSV

**Description:**

A collection of simple nodes for Frequency Separation / Frequency Recombine with RGB and HSV methods

- **Author:** risunobushi
- **Repository:** [https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV](https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides Frequency Separation and Recombine methods in RGB and HSV, directly supporting the inpainting workflow goal.

### Metadata
**Author:** risunobushi
**Repository:** [https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV](https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV)
**Install Type:** git-clone

---

### Comfyui_Get_promptId

**Description:**

NODES: Get Prompt_Id, Success Callback
get comfyui task id and Callback for successful image generation, in conjunction with the back-end

- **Author:** xs315431
- **Repository:** [https://github.com/xs315431/Comfyui_Get_promptId](https://github.com/xs315431/Comfyui_Get_promptId)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it retrieves the task ID and callback for successful image generation, which is essential for tracking progress in an inpainting workflow.

### Metadata
**Author:** xs315431
**Repository:** [https://github.com/xs315431/Comfyui_Get_promptId](https://github.com/xs315431/Comfyui_Get_promptId)
**Install Type:** git-clone

---

### ComfyUI_GradientDeepShrink

**Description:**

Nodes:GradientPatchModelAddDownscale (Kohya Deep Shrink).

- **Author:** kinfolk0117
- **Repository:** [https://github.com/kinfolk0117/ComfyUI_GradientDeepShrink](https://github.com/kinfolk0117/ComfyUI_GradientDeepShrink)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is specifically designed for gradient-based deep shrink models and could be useful for inpainting tasks that involve shrinking or downscaling images.

### Metadata
**Author:** kinfolk0117
**Repository:** [https://github.com/kinfolk0117/ComfyUI_GradientDeepShrink](https://github.com/kinfolk0117/ComfyUI_GradientDeepShrink)
**Install Type:** git-clone

---

### ComfyUI_HF_Inference

**Description:**

Unofficial support for Hugging Face's hosted inference.

- **Author:** bitaffinity
- **Repository:** [https://github.com/bitaffinity/ComfyUI_HF_Inference](https://github.com/bitaffinity/ComfyUI_HF_Inference)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides support for Hugging Face"s hosted inference, which could be useful in an inpainting workflow that relies on Hugging Face models.

### Metadata
**Author:** bitaffinity
**Repository:** [https://github.com/bitaffinity/ComfyUI_HF_Inference](https://github.com/bitaffinity/ComfyUI_HF_Inference)
**Install Type:** git-clone

---

### ComfyUI_HiDiffusion_Pro

**Description:**

A HiDiffusion node for ComfyUI.

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_HiDiffusion_Pro](https://github.com/smthemex/ComfyUI_HiDiffusion_Pro)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a HiDiffusion interface, but its specific features and capabilities are unclear; it may or may not be relevant to the inpainting workflow.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_HiDiffusion_Pro](https://github.com/smthemex/ComfyUI_HiDiffusion_Pro)
**Install Type:** git-clone

---

### ComfyUI_HuggingFace_Downloader

**Description:**

The ComfyUI HuggingFace Downloader is a custom node extension for ComfyUI, designed to streamline the process of downloading models, checkpoints, and other resources from the Hugging Face Hub directly into your models directory. This tool simplifies workflow integration by providing a seamless interface to select and download required resources.

- **Author:** jnxmx
- **Repository:** [https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader](https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows for seamless downloading of Hugging Face models and resources, which would be essential in an inpainting workflow that relies on these models.

### Metadata
**Author:** jnxmx
**Repository:** [https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader](https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader)
**Install Type:** git-clone

---

### Comfyui_Hunyuan3D

**Description:**

NODES:TTP_Hunyuan3DNode, TTP_SquareImage, TTP_GIFViewer

- **Author:** TTPlanetPig
- **Repository:** [https://github.com/TTPlanetPig/Comfyui_Hunyuan3D](https://github.com/TTPlanetPig/Comfyui_Hunyuan3D)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly related to Hunyuan3D inpainting with mask input.

### Metadata
**Author:** TTPlanetPig
**Repository:** [https://github.com/TTPlanetPig/Comfyui_Hunyuan3D](https://github.com/TTPlanetPig/Comfyui_Hunyuan3D)
**Install Type:** git-clone

---

### Comfyui_Hunyuan3D_EX

**Description:**

This is a custom node designed to simplify the use of Hunyuan3D in ComfyUI

- **Author:** BIMer-99
- **Repository:** [https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX](https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Customized node designed specifically for simplifying Hunyuan3D usage in ComfyUI for inpainting workflows.

### Metadata
**Author:** BIMer-99
**Repository:** [https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX](https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX)
**Install Type:** git-clone

---

### ComfyUI_IndustrialMagick

**Description:**

[a/ImageMagick](https://imagemagick.org/index.php) nodes for ComfyUI. Adds nodes to call ImageMagick subprocesses from ComfyUI.
Requirements: [a/ImagMagick7](https://imagemagick.org/script/download.php), 'magick' command in your CLI environment.

- **Author:** my-opencode
- **Repository:** [https://github.com/my-opencode/ComfyUI_IndustrialMagick](https://github.com/my-opencode/ComfyUI_IndustrialMagick)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides ImageMagick functionality which can be useful for image processing tasks in the inpainting workflow.

### Metadata
**Author:** my-opencode
**Repository:** [https://github.com/my-opencode/ComfyUI_IndustrialMagick](https://github.com/my-opencode/ComfyUI_IndustrialMagick)
**Install Type:** git-clone

---

### ComfyUI_InstantIR_Wrapper

**Description:**

You can InstantIR to Fix blurry photos in ComfyUI ，[a/InstantIR](https://github.com/instantX-research/InstantIR):Blind Image Restoration with Instant Generative Reference

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_InstantIR_Wrapper](https://github.com/smthemex/ComfyUI_InstantIR_Wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node uses InstantIR for blind image restoration, making it highly relevant and useful for fixing blurry photos in the inpainting workflow.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_InstantIR_Wrapper](https://github.com/smthemex/ComfyUI_InstantIR_Wrapper)
**Install Type:** git-clone

---

### ComfyUI_IPAdapter_plus

**Description:**

ComfyUI reference implementation for IPAdapter models. The code is mostly taken from the original IPAdapter repository and laksjdjf's implementation, all credit goes to them. I just made the extension closer to ComfyUI philosophy.

- **Author:** cubiq
- **Repository:** [https://github.com/cubiq/ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a reference implementation for IPAdapter models, which are likely used in inpainting workflows with mask input.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
**Install Type:** git-clone

---

### comfyui_jankhidiffusion

**Description:**

Janky implementation of [a/HiDiffusion](https://github.com/megvii-research/HiDiffusion) for ComfyUI. Enables generating at resolutions higher than what the model was trained for. Only supports SD 1.x (maybe 2.x) and SDXL.

- **Author:** blepping
- **Repository:** [https://github.com/blepping/comfyui_jankhidiffusion](https://github.com/blepping/comfyui_jankhidiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node supports generating at resolutions higher than what the model was trained for without requiring model patches, making it very useful for the specified workflow goal.

### Metadata
**Author:** blepping
**Repository:** [https://github.com/blepping/comfyui_jankhidiffusion](https://github.com/blepping/comfyui_jankhidiffusion)
**Install Type:** git-clone

---

### comfyui_kmeans_filter

**Description:**

Nodes:Apply Kmeans Filter

- **Author:** githubYiheng
- **Repository:** [https://github.com/githubYiheng/comfyui_kmeans_filter](https://github.com/githubYiheng/comfyui_kmeans_filter)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node applies a Kmeans filter which could potentially be used in image processing but its direct relevance to inpainting or mask processing is limited.

### Metadata
**Author:** githubYiheng
**Repository:** [https://github.com/githubYiheng/comfyui_kmeans_filter](https://github.com/githubYiheng/comfyui_kmeans_filter)
**Install Type:** git-clone

---

### ComfyUI_LG_FFT

**Description:**

Implementation of Fast Fourier Transform in COMFYUI

- **Author:** laogou666
- **Repository:** [https://github.com/LAOGOU-666/ComfyUI_LG_FFT](https://github.com/LAOGOU-666/ComfyUI_LG_FFT)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node implements Fast Fourier Transform which can be useful for various image processing tasks including inpainting with a mask input.

### Metadata
**Author:** laogou666
**Repository:** [https://github.com/LAOGOU-666/ComfyUI_LG_FFT](https://github.com/LAOGOU-666/ComfyUI_LG_FFT)
**Install Type:** git-clone

---

### ComfyUI_LiteLLM

**Description:**

Nodes for calling LLMs, enabled by LiteLLM

- **Author:** TashaSkyUp
- **Repository:** [https://github.com/Hopping-Mad-Games/ComfyUI_LiteLLM](https://github.com/Hopping-Mad-Games/ComfyUI_LiteLLM)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node enables calling LLMs but its direct relevance to inpainting with a mask input is limited.

### Metadata
**Author:** TashaSkyUp
**Repository:** [https://github.com/Hopping-Mad-Games/ComfyUI_LiteLLM](https://github.com/Hopping-Mad-Games/ComfyUI_LiteLLM)
**Install Type:** git-clone

---

### ComfyUI_Llama3_8B

**Description:**

Llama3_8B for comfyUI， using pipeline workflow.

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Llama3_8B](https://github.com/smthemex/ComfyUI_Llama3_8B)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** ComfyUI_Llama3_8B is a direct implementation of Llama3_8B for comfyUI, making it highly relevant to the inpainting workflow with mask input.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Llama3_8B](https://github.com/smthemex/ComfyUI_Llama3_8B)
**Install Type:** git-clone

---

### ComfyUI_LLaSM

**Description:**

ComfyUI for [a/LLaSM](https://huggingface.co/spaces/LinkSoul/LLaSM)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_LLaSM](https://github.com/leeguandong/ComfyUI_LLaSM)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI_LLaSM is specifically designed for [a/LLaSM], which seems to be related to inpainting, making it essential for this workflow goal.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_LLaSM](https://github.com/leeguandong/ComfyUI_LLaSM)
**Install Type:** git-clone

---

### comfyui_LLM_party

**Description:**

A set of block-based LLM agent node libraries designed for ComfyUI.This project aims to develop a complete set of nodes for LLM workflow construction based on comfyui. It allows users to quickly and conveniently build their own LLM workflows and easily integrate them into their existing SD workflows.

- **Author:** heshengtao
- **Repository:** [https://github.com/heshengtao/comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** comfyui_LLM_party is a set of block-based LLM agent node libraries for ComfyUI, which might be useful in building workflows, but its direct relevance to the inpainting workflow with mask input is limited.

### Metadata
**Author:** heshengtao
**Repository:** [https://github.com/heshengtao/comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)
**Install Type:** git-clone

---

### comfyui_lumaAPI

**Description:**

Unofficial Luma API-ComfyUI version.[w/WARN: This project is for learning purpose only!]

- **Author:** superyoman
- **Repository:** [https://github.com/superyoman/comfyui_lumaAPI](https://github.com/superyoman/comfyui_lumaAPI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides an unofficial Luma API-ComfyUI version, but its learning purpose and limited functionality make it marginally relevant to the specified workflow goal.

### Metadata
**Author:** superyoman
**Repository:** [https://github.com/superyoman/comfyui_lumaAPI](https://github.com/superyoman/comfyui_lumaAPI)
**Install Type:** git-clone

---

### ComfyUI_M3Net

**Description:**

ComfyUI for [a/M3Net](https://github.com/I2-Multimedia-Lab/M3Net)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_M3Net](https://github.com/leeguandong/ComfyUI_M3Net)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements inpainting with mask input, making it essential for this workflow.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_M3Net](https://github.com/leeguandong/ComfyUI_M3Net)
**Install Type:** git-clone

---

### ComfyUI_MagicClothing

**Description:**

implementation of MagicClothing with garment and prompt in ComfyUI

- **Author:** FrankChieng
- **Repository:** [https://github.com/frankchieng/ComfyUI_MagicClothing](https://github.com/frankchieng/ComfyUI_MagicClothing)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Provides a MagicClothing implementation that can be used in conjunction with inpainting and mask inputs, making it very useful for this workflow.

### Metadata
**Author:** FrankChieng
**Repository:** [https://github.com/frankchieng/ComfyUI_MagicClothing](https://github.com/frankchieng/ComfyUI_MagicClothing)
**Install Type:** git-clone

---

### ComfyUI_MaskGCT

**Description:**

Suitable for Windows - MaskGCT ComfyUI Node Wrapping

- **Author:** 807502278
- **Repository:** [https://github.com/807502278/ComfyUI_MaskGCT](https://github.com/807502278/ComfyUI_MaskGCT)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Directly provides a ComfyUI node for MaskGCT, which can be used in inpainting workflows with mask inputs, making it very useful for this workflow.

### Metadata
**Author:** 807502278
**Repository:** [https://github.com/807502278/ComfyUI_MaskGCT](https://github.com/807502278/ComfyUI_MaskGCT)
**Install Type:** git-clone

---

### ComfyUI_merge_ASVL

**Description:**

This is a simple node for connecting images. For pictures of the same size, users can choose to fill in vertical in the parameter to connect the pictures vertically or fill in horizontal to connect the pictures horizontally.

- **Author:** aisabervisionlab
- **Repository:** [https://github.com/aisabervisionlab/ComfyUI_merge_ASVL](https://github.com/aisabervisionlab/ComfyUI_merge_ASVL)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Directly relevant to combining images with a mask input

### Metadata
**Author:** aisabervisionlab
**Repository:** [https://github.com/aisabervisionlab/ComfyUI_merge_ASVL](https://github.com/aisabervisionlab/ComfyUI_merge_ASVL)
**Install Type:** git-clone

---

### ComfyUI_Mexx_Poster

**Description:**

Nodes: ComfyUI_Mexx_Poster

- **Author:** SoftMeng
- **Repository:** [https://github.com/SoftMeng/ComfyUI_Mexx_Poster](https://github.com/SoftMeng/ComfyUI_Mexx_Poster)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a poster generation tool which could be useful in creating visual aids for an inpainting workflow.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI_Mexx_Poster](https://github.com/SoftMeng/ComfyUI_Mexx_Poster)
**Install Type:** git-clone

---

### Comfyui_MiniCPMv2_6-prompt-generator

**Description:**

This is an implementation of [MiniCPMv2_6-prompt-generator](https://huggingface.co/pzc163/MiniCPMv2_6-prompt-generator) by [ComfyUI](https://github.com/comfyanonymous/ComfyUI), including support for single-image caption, generate prompt by upload image and batch-images Prompt generation.

- **Author:** pzc163
- **Repository:** [https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator](https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate prompts based on image inputs which could be useful for the inpainting workflow.

### Metadata
**Author:** pzc163
**Repository:** [https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator](https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator)
**Install Type:** git-clone

---

### ComfyUI_Mira

**Description:**

Slice regions of the canvas and convert them to masks for regional conditions widh PNG preview output. And a few support nodes.

- **Author:** mirabarukaso
- **Repository:** [https://github.com/mirabarukaso/ComfyUI_Mira](https://github.com/mirabarukaso/ComfyUI_Mira)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly supports regional masking and output preview which is highly relevant to the inpainting workflow with mask input.

### Metadata
**Author:** mirabarukaso
**Repository:** [https://github.com/mirabarukaso/ComfyUI_Mira](https://github.com/mirabarukaso/ComfyUI_Mira)
**Install Type:** git-clone

---

### ComfyUI_mittimiWidthHeight

**Description:**

This node can easily switch between vertical and horizontal values with a single button.

- **Author:** mittimi
- **Repository:** [https://github.com/mittimi/ComfyUI_mittimiWidthHeight](https://github.com/mittimi/ComfyUI_mittimiWidthHeight)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows easy switching between vertical and horizontal values which is useful for defining the mask in an inpainting workflow.

### Metadata
**Author:** mittimi
**Repository:** [https://github.com/mittimi/ComfyUI_mittimiWidthHeight](https://github.com/mittimi/ComfyUI_mittimiWidthHeight)
**Install Type:** git-clone

---

### ComfyUI_MS_Diffusion

**Description:**

you can make story in comfyUI using MS-diffusion

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for MS-Diffusion, which can be used for image inpainting tasks, making it very useful for this workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)
**Install Type:** git-clone

---

### comfyui_nai_api

**Description:**

A node that can use Nai in Comfyui

- **Author:** creeper
- **Repository:** [https://github.com/Creeper-MZ/comfyui_nai_api](https://github.com/Creeper-MZ/comfyui_nai_api)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can use Nai in Comfyui which could be useful for generating images through NAI, a common technique used in inpainting workflows.

### Metadata
**Author:** creeper
**Repository:** [https://github.com/Creeper-MZ/comfyui_nai_api](https://github.com/Creeper-MZ/comfyui_nai_api)
**Install Type:** git-clone

---

### ComfyUI_NAIDGenerator

**Description:**

This extension helps generate images through NAI.

- **Author:** bedovyy
- **Repository:** [https://github.com/bedovyy/ComfyUI_NAIDGenerator](https://github.com/bedovyy/ComfyUI_NAIDGenerator)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is directly related to the workflow goal as it helps generate images through NAI, making it essential for this Inpainting workflow with mask input.

### Metadata
**Author:** bedovyy
**Repository:** [https://github.com/bedovyy/ComfyUI_NAIDGenerator](https://github.com/bedovyy/ComfyUI_NAIDGenerator)
**Install Type:** git-clone

---

### ComfyUI_Nimbus-Pack

**Description:**

Nodes:Image Square Adapter Node, Image Resize And Crop Node

- **Author:** sergekatzmann
- **Repository:** [https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack](https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains image processing nodes (Image Square Adapter Node and Image Resize And Crop Node) that could support the inpainting workflow by preparing or manipulating the input images.

### Metadata
**Author:** sergekatzmann
**Repository:** [https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack](https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack)
**Install Type:** git-clone

---

### ComfyUI_NoxinNodes

**Description:**

Nodes: Noxin Complete Chime, Noxin Scaled Resolutions, Load from Noxin Prompt Library, Save to Noxin Prompt Library

- **Author:** noxinias
- **Repository:** [https://github.com/noxinias/ComfyUI_NoxinNodes](https://github.com/noxinias/ComfyUI_NoxinNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some image-related nodes (Load from Noxin Prompt Library and Save to Noxin Prompt Library) that could potentially support the inpainting workflow by loading or saving necessary data.

### Metadata
**Author:** noxinias
**Repository:** [https://github.com/noxinias/ComfyUI_NoxinNodes](https://github.com/noxinias/ComfyUI_NoxinNodes)
**Install Type:** git-clone

---

### ComfyUI_OmniGen_Wrapper

**Description:**

ComfyUI custom node of OmniGen project.

- **Author:** chflame163
- **Repository:** [https://github.com/chflame163/ComfyUI_OmniGen_Wrapper](https://github.com/chflame163/ComfyUI_OmniGen_Wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant and useful for the specified workflow goal as it provides a custom implementation of OmniGen project which can be used for inpainting with mask input.

### Metadata
**Author:** chflame163
**Repository:** [https://github.com/chflame163/ComfyUI_OmniGen_Wrapper](https://github.com/chflame163/ComfyUI_OmniGen_Wrapper)
**Install Type:** git-clone

---

### ComfyUI_OmniParser

**Description:**

Try [a/OmniParser](https://github.com/microsoft/OmniParser) in ComfyUI which a simple screen parsing tool towards pure vision based GUI agent.

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_OmniParser](https://github.com/smthemex/ComfyUI_OmniParser)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal as it provides a simple screen parsing tool that can be used in conjunction with other nodes to achieve inpainting with mask input.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_OmniParser](https://github.com/smthemex/ComfyUI_OmniParser)
**Install Type:** git-clone

---

### ComfyUI_omost

**Description:**

ComfyUI implementation of [a/Omost](https://github.com/lllyasviel/Omost), and everything about regional prompt.
NOTE: You need to install ComfyUI_densediffusion to use this node.

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI_omost](https://github.com/huchenlei/ComfyUI_omost)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** This node is moderately useful for the specified workflow goal as it provides an implementation of Omost which can be used for regional prompt and potentially inpainting with mask input, but requires additional installation of ComfyUI_densediffusion.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI_omost](https://github.com/huchenlei/ComfyUI_omost)
**Install Type:** git-clone

---

### ComfyUI_OOTDiffusion_CXH

**Description:**

Nodes:Ood_hd_CXH, Ood_hd_CXH. [a/OOTDiffusion](https://github.com/levihsu/OOTDiffusion)

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH](https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides OOT Diffusion functionality which can be used for inpainting tasks with mask input.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH](https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH)
**Install Type:** git-clone

---

### ComfyUI_PBR_Maker

**Description:**

you can make PBR in comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_PBR_Maker](https://github.com/smthemex/ComfyUI_PBR_Maker)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports PBR (Physically Based Rendering), which could be a crucial step in creating realistic textures for inpainting; it is essential for this workflow.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_PBR_Maker](https://github.com/smthemex/ComfyUI_PBR_Maker)
**Install Type:** git-clone

---

### ComfyUI_PerpCFG

**Description:**

Perpendicular CFG for reducing oversaturation issues with high guidance scale values.

- **Author:** bvhari
- **Repository:** [https://github.com/bvhari/ComfyUI_PerpCFG](https://github.com/bvhari/ComfyUI_PerpCFG)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node addresses oversaturation issues with high guidance scale values, which can be beneficial for inpainting workflows.

### Metadata
**Author:** bvhari
**Repository:** [https://github.com/bvhari/ComfyUI_PerpCFG](https://github.com/bvhari/ComfyUI_PerpCFG)
**Install Type:** git-clone

---

### ComfyUI_PerpWeight

**Description:**

A novel weighting scheme for token vectors from CLIP. Allows a wider range of values for the weight. Inspired by Perp-Neg.

- **Author:** bvhari
- **Repository:** [https://github.com/bvhari/ComfyUI_PerpWeight](https://github.com/bvhari/ComfyUI_PerpWeight)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides a novel weighting scheme that may improve performance in certain inpainting scenarios.

### Metadata
**Author:** bvhari
**Repository:** [https://github.com/bvhari/ComfyUI_PerpWeight](https://github.com/bvhari/ComfyUI_PerpWeight)
**Install Type:** git-clone

---

### ComfyUI_Pic2Story

**Description:**

you can using pic2story in comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** ComfyUI_Pic2Story seems to be a relevant tool for image processing and could potentially be used in an inpainting workflow with mask input.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)
**Install Type:** git-clone

---

### ComfyUI_Pops

**Description:**

You can use [a/Popspaper](https://popspaper.github.io/pOps/) method in comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can be used in conjunction with other nodes to perform inpainting tasks, utilizing the Popspaper method from POPS.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)
**Install Type:** git-clone

---

### ComfyUI_Prompt-Quill

**Description:**

Nodes:Use Prompt Quill in Comfyui

- **Author:** osiworx
- **Repository:** [https://github.com/osi1880vr/prompt_quill_comfyui](https://github.com/osi1880vr/prompt_quill_comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a custom prompt quill interface for ComfyUI, which could be useful in generating prompts for the inpainting workflow.

### Metadata
**Author:** osiworx
**Repository:** [https://github.com/osi1880vr/prompt_quill_comfyui](https://github.com/osi1880vr/prompt_quill_comfyui)
**Install Type:** git-clone

---

### ComfyUI_PS_Blend_Node

**Description:**

This repository contains a simple custom node for ComfyUI that implements familiar PS-style blend modes using PyTorch. The PSBlendNode allows you to blend two images together using a variety of blend modes and an opacity parameter.

- **Author:** bluevisor
- **Repository:** [https://github.com/bluevisor/ComfyUI_PS_Blend_Node](https://github.com/bluevisor/ComfyUI_PS_Blend_Node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows blending of two images using various blend modes and opacity parameters, which can be useful in post-processing or combining multiple inpainted regions.

### Metadata
**Author:** bluevisor
**Repository:** [https://github.com/bluevisor/ComfyUI_PS_Blend_Node](https://github.com/bluevisor/ComfyUI_PS_Blend_Node)
**Install Type:** git-clone

---

### comfyui_quilting

**Description:**

image and latent quilting nodes for comfyui

- **Author:** bmad4ever
- **Repository:** [https://github.com/bmad4ever/comfyui_quilting](https://github.com/bmad4ever/comfyui_quilting)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant and useful for the inpainting workflow with mask input as it involves image quilting techniques.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_quilting](https://github.com/bmad4ever/comfyui_quilting)
**Install Type:** git-clone

---

### Comfyui_Redux_Advanced

**Description:**

Redux style adds more controls

- **Author:** yichengup
- **Repository:** [https://github.com/yichengup/Comfyui_Redux_Advanced](https://github.com/yichengup/Comfyui_Redux_Advanced)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides additional controls for the inpainting workflow, which could be useful for fine-tuning the process.

### Metadata
**Author:** yichengup
**Repository:** [https://github.com/yichengup/Comfyui_Redux_Advanced](https://github.com/yichengup/Comfyui_Redux_Advanced)
**Install Type:** git-clone

---

### comfyui_reimgsize

**Description:**

a simple reimgsize node(s) in comfyui.

- **Author:** Makki_Shizu
- **Repository:** [https://github.com/MakkiShizu/comfyui_reimgsize](https://github.com/MakkiShizu/comfyui_reimgsize)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows resizing images, but its relevance to the inpainting workflow with mask input is limited.

### Metadata
**Author:** Makki_Shizu
**Repository:** [https://github.com/MakkiShizu/comfyui_reimgsize](https://github.com/MakkiShizu/comfyui_reimgsize)
**Install Type:** git-clone

---

### ComfyUI_RH_OminiControl

**Description:**

ComfyUI_RH_OminiControl is a ComfyUI plugin based on OminiControl By splitting the pipeline load, the plugin efficiently runs on NVIDIA RTX 4090 GPUs. Additionally, the spatial and fill functionalities are generated using the schnell model, reducing the number of sampling steps and improving overall efficiency.

- **Author:** HM-RunningHub
- **Repository:** [https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl](https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node efficiently runs on NVIDIA RTX 4090 GPUs and utilizes the schnell model for spatial and fill functionalities, making it highly useful for the inpainting workflow with mask input.

### Metadata
**Author:** HM-RunningHub
**Repository:** [https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl](https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl)
**Install Type:** git-clone

---

### ComfyUI_S3_direct

**Description:**

ComfyUI custom_node that load and save file directly from S3
Simplified version of [a/https://github.com/kealiu/ComfyUI-S3-Tools](https://github.com/kealiu/ComfyUI-S3-Tools)

- **Author:** KunmyonChoi
- **Repository:** [https://github.com/KunmyonChoi/ComfyUI_S3_direct](https://github.com/KunmyonChoi/ComfyUI_S3_direct)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows loading and saving files directly from S3, which might be useful as a supporting node but is not essential for the specified workflow goal.

### Metadata
**Author:** KunmyonChoi
**Repository:** [https://github.com/KunmyonChoi/ComfyUI_S3_direct](https://github.com/KunmyonChoi/ComfyUI_S3_direct)
**Install Type:** git-clone

---

### ComfyUI_Sapiens

**Description:**

You can call Using Sapiens to get seg,normal,pose,depth,mask maps. Sapiens From: [a/facebookresearch/sapiens](https://github.com/facebookresearch/sapiens)

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Sapiens](https://github.com/smthemex/ComfyUI_Sapiens)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides access to Sapiens, which can generate various maps including masks, making it very useful for image inpainting with a mask input.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Sapiens](https://github.com/smthemex/ComfyUI_Sapiens)
**Install Type:** git-clone

---

### ComfyUI_Seg_VITON

**Description:**

Nodes:segformer_clothes, segformer_agnostic, segformer_remove_bg, stabel_vition. Nodes for model dress up.

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/ComfyUI_Seg_VITON](https://github.com/StartHua/ComfyUI_Seg_VITON)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a segmentation model specifically designed for clothes and human segmentation, making it highly relevant to the inpainting workflow with mask input.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/ComfyUI_Seg_VITON](https://github.com/StartHua/ComfyUI_Seg_VITON)
**Install Type:** git-clone

---

### comfyui_segformer_b2_clothes

**Description:**

SegFormer model fine-tuned on ATR dataset for clothes segmentation but can also be used for human segmentation!
Download the weight and put it under checkpoints: [a/https://huggingface.co/mattmdjaga/segformer_b2_clothes](https://huggingface.co/mattmdjaga/segformer_b2_clothes)

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/Comfyui_segformer_b2_clothes](https://github.com/StartHua/Comfyui_segformer_b2_clothes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to the inpainting workflow with mask input as it provides a fine-tuned SegFormer model for clothes segmentation which can be used for inpainting.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_segformer_b2_clothes](https://github.com/StartHua/Comfyui_segformer_b2_clothes)
**Install Type:** git-clone

---

### ComfyUI_Segment_Mask

**Description:**

Mask cutout based on Segment Anything.

- **Author:** MarkoCa1
- **Repository:** [https://github.com/MarkoCa1/ComfyUI_Segment_Mask](https://github.com/MarkoCa1/ComfyUI_Segment_Mask)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Although this node is not specifically designed for inpainting, its ability to perform segment anything and cut out masks makes it moderately useful for the specified workflow goal.

### Metadata
**Author:** MarkoCa1
**Repository:** [https://github.com/MarkoCa1/ComfyUI_Segment_Mask](https://github.com/MarkoCa1/ComfyUI_Segment_Mask)
**Install Type:** git-clone

---

### ComfyUI_Slider_Sidebar

**Description:**

A custom node that adds a UI element to the sidebar allowing easy access, navigation, and use of a massive collection (100+) of LECO (Slider) LoRAs. LECOs are an amazing tool to generate variance in your output with a minimal impact to consistency, i.e. deviating form your prompt. They can also allow you access to control parts of your image without taking up CLIP space, saving your token weights for more valuable keywords. If you haven't used them, there's never been a better time to try!

- **Author:** Kinglord
- **Repository:** [https://github.com/Kinglord/ComfyUI_Slider_Sidebar](https://github.com/Kinglord/ComfyUI_Slider_Sidebar)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a UI element for easy access and navigation of LECO LoRAs which can be used to generate variance in the output without deviating from consistency. It is very useful for this workflow goal.

### Metadata
**Author:** Kinglord
**Repository:** [https://github.com/Kinglord/ComfyUI_Slider_Sidebar](https://github.com/Kinglord/ComfyUI_Slider_Sidebar)
**Install Type:** git-clone

---

### ComfyUI_Stable_Makeup

**Description:**

you can using stable makeup when use comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Stable_Makeup](https://github.com/smthemex/ComfyUI_Stable_Makeup)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides stable makeup functionality, which can be useful in creating realistic inpainted results by filling in missing areas with consistent textures and colors.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Stable_Makeup](https://github.com/smthemex/ComfyUI_Stable_Makeup)
**Install Type:** git-clone

---

### ComfyUI_StableCascadeLatentRatio

**Description:**

A custom node to create empty latents for Stable Cascade.
features: width and height incrementation of 64 by default, possibility to lock the aspect ratio, switch width/height at execution

- **Author:** Guillaume-Fgt
- **Repository:** [https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio](https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node creates empty latents for Stable Cascade, which can be useful in inpainting workflows by providing a starting point for the model to fill in missing areas based on the provided mask.

### Metadata
**Author:** Guillaume-Fgt
**Repository:** [https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio](https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio)
**Install Type:** git-clone

---

### ComfyUI_StoryDiffusion

**Description:**

you can using sotry-diffusion in comfyui

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is highly relevant to the inpainting workflow as it utilizes story diffusion for image generation.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)
**Install Type:** git-clone

---

### ComfyUI_StreamDiffusion

**Description:**

This is a simple implementation StreamDiffusion(A Pipeline-Level Solution for Real-Time Interactive Generation) for ComfyUI

- **Author:** jesenzhang
- **Repository:** [https://github.com/jesenzhang/ComfyUI_StreamDiffusion](https://github.com/jesenzhang/ComfyUI_StreamDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it implements StreamDiffusion for real-time interactive generation.

### Metadata
**Author:** jesenzhang
**Repository:** [https://github.com/jesenzhang/ComfyUI_StreamDiffusion](https://github.com/jesenzhang/ComfyUI_StreamDiffusion)
**Install Type:** git-clone

---

### ComfyUi_String_Function_Tree

**Description:**

This custom node provides the capability to manipulate multiple string inputs.

- **Author:** wolfden
- **Repository:** [https://github.com/wolfden/ComfyUi_String_Function_Tree](https://github.com/wolfden/ComfyUi_String_Function_Tree)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node manipulates string inputs but has no direct relevance to inpainting with a mask.

### Metadata
**Author:** wolfden
**Repository:** [https://github.com/wolfden/ComfyUi_String_Function_Tree](https://github.com/wolfden/ComfyUi_String_Function_Tree)
**Install Type:** git-clone

---

### ComfyUI_SVFR

**Description:**

SVFR is a unified framework for face video restoration that supports tasks such as BFR, Colorization, Inpainting，you can use it in ComfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_SVFR](https://github.com/smthemex/ComfyUI_SVFR)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node supports face video restoration tasks including inpainting, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_SVFR](https://github.com/smthemex/ComfyUI_SVFR)
**Install Type:** git-clone

---

### ComfyUI_tinyterraNodes

**Description:**

This extension offers various pipe nodes, extensive XYZ plotting, fullscreen image viewer based on node history, dynamic widgets, interface customization, and more.

- **Author:** TinyTerra
- **Repository:** [https://github.com/TinyTerra/ComfyUI_tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node offers various features that could be useful in a workflow, but its direct relevance to inpainting with mask input is unclear without more context.

### Metadata
**Author:** TinyTerra
**Repository:** [https://github.com/TinyTerra/ComfyUI_tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)
**Install Type:** git-clone

---

### comfyui_wfc_like

**Description:**

An 'opinionated' Wave Function Collapse implementation with a set of nodes for comfyui

- **Author:** bmad4ever
- **Repository:** [https://github.com/bmad4ever/comfyui_wfc_like](https://github.com/bmad4ever/comfyui_wfc_like)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node implements Wave Function Collapse which can be used for inpainting tasks and supports mask input.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_wfc_like](https://github.com/bmad4ever/comfyui_wfc_like)
**Install Type:** git-clone

---

### ComfyUI_YoloSegment_Mask

**Description:**

NODES:Object Mask.
NOTE:push [a/yolov8x-seg.pt](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x-seg.pt) in models/yolo

- **Author:** Trgtuan10
- **Repository:** [https://github.com/Trgtuan10/ComfyUI_YoloSegment_Mask](https://github.com/Trgtuan10/ComfyUI_YoloSegment_Mask)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node specifically supports object segmentation and mask generation using YOLOv8x-seg.pt model.

### Metadata
**Author:** Trgtuan10
**Repository:** [https://github.com/Trgtuan10/ComfyUI_YoloSegment_Mask](https://github.com/Trgtuan10/ComfyUI_YoloSegment_Mask)
**Install Type:** git-clone

---

### ComfyUI_ZenID

**Description:**

Inspired by [a/InstantID](https://github.com/instantX-research/InstantID) and [a/InstantID Comfy](https://github.com/cubiq/ComfyUI_InstantID)
This ZenID Node has been refactored for specialized tasks like Face Swap

- **Author:** vuongminh1907
- **Repository:** [https://github.com/vuongminh1907/ComfyUI_ZenID](https://github.com/vuongminh1907/ComfyUI_ZenID)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate unique IDs which could be useful in various tasks including inpainting workflow.

### Metadata
**Author:** vuongminh1907
**Repository:** [https://github.com/vuongminh1907/ComfyUI_ZenID](https://github.com/vuongminh1907/ComfyUI_ZenID)
**Install Type:** git-clone

---

### ComfyUI_Zwng_Nodes

**Description:**

Simple nodes for loading image files.Nodes that include a simple remote connection to Photoshop, a node that can overlay and preview an image with a mask, and a node that can load images directly from a file path.

- **Author:** zwng
- **Repository:** [https://github.com/za-wa-n-go/ComfyUI_Zwng_Nodes](https://github.com/za-wa-n-go/ComfyUI_Zwng_Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node includes nodes that can load images and overlay them with masks which is highly relevant to the inpainting workflow.

### Metadata
**Author:** zwng
**Repository:** [https://github.com/za-wa-n-go/ComfyUI_Zwng_Nodes](https://github.com/za-wa-n-go/ComfyUI_Zwng_Nodes)
**Install Type:** git-clone

---

### ComfyUIFlexiLoRALoader

**Description:**

FlexiLoRALoader - A ComfyUI custom node for dynamic LoRA weight management. Apply multiple LoRAs with flexible weight patterns and randomization features for creative AI image generation.
Features: • Multiple LoRA handling (up to 3) • Weight pattern presets • Random/Sequential mode • Debug logging support

- **Author:** ronsantash
- **Repository:** [https://github.com/ronsantash/Comfyui-flexi-lora-loader](https://github.com/ronsantash/Comfyui-flexi-lora-loader)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** FlexiLoRALoader can be used to manage LoRA weights which might be useful in some AI image generation tasks but its direct relevance to inpainting with mask input is moderate.

### Metadata
**Author:** ronsantash
**Repository:** [https://github.com/ronsantash/Comfyui-flexi-lora-loader](https://github.com/ronsantash/Comfyui-flexi-lora-loader)
**Install Type:** git-clone

---

### ComfyWarp

**Description:**

WarpFusion workflow wrapper for ComfyUI

- **Author:** Sxela
- **Repository:** [https://github.com/Sxela/ComfyWarp](https://github.com/Sxela/ComfyWarp)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyWarp provides a wrapper for WarpFusion, which can be useful in an inpainting workflow with mask input.

### Metadata
**Author:** Sxela
**Repository:** [https://github.com/Sxela/ComfyWarp](https://github.com/Sxela/ComfyWarp)
**Install Type:** git-clone

---

### Compositor Node

**Description:**

pass up to 8 images and visually place, rotate and scale them to build the perfect composition. group move and group rescale. remember their position and scaling value across generations to easy swap images. use the buffer zone to to park an asset you don't want to use or easily reach transformations controls

- **Author:** erosDiffusion
- **Repository:** [https://github.com/erosDiffusion/ComfyUI-enricos-nodes](https://github.com/erosDiffusion/ComfyUI-enricos-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** The Compositor Node allows for image composition and manipulation, making it essential for an inpainting workflow that involves combining multiple images or layers.

### Metadata
**Author:** erosDiffusion
**Repository:** [https://github.com/erosDiffusion/ComfyUI-enricos-nodes](https://github.com/erosDiffusion/ComfyUI-enricos-nodes)
**Install Type:** git-clone

---

### Consistency Decoder

**Description:**

[a/openai Consistency Decoder](https://github.com/openai/consistencydecoder). After downloading the [a/OpenAI VAE model](https://openaipublic.azureedge.net/diff-vae/c9cebd3132dd9c42936d803e33424145a748843c8f716c0814838bdc8a2fe7cb/decoder.pt), place it in the `model/vae` directory for use.

- **Author:** shadowcz007
- **Repository:** [https://github.com/shadowcz007/comfyui-consistency-decoder](https://github.com/shadowcz007/comfyui-consistency-decoder)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This Consistency Decoder node can help refine the inpainted image by ensuring consistency across different parts of the output.

### Metadata
**Author:** shadowcz007
**Repository:** [https://github.com/shadowcz007/comfyui-consistency-decoder](https://github.com/shadowcz007/comfyui-consistency-decoder)
**Install Type:** git-clone

---

### ControlAltAI Nodes

**Description:**

Quality of Life ComfyUI nodes starting with Flux Resolution Calculator and Flux Sampler.

- **Author:** ControlAltAI
- **Repository:** [https://github.com/gseth/ControlAltAI-Nodes](https://github.com/gseth/ControlAltAI-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While ControlAltAI Nodes may offer some quality-of-life improvements, they are not directly relevant to the inpainting workflow with mask input.

### Metadata
**Author:** ControlAltAI
**Repository:** [https://github.com/gseth/ControlAltAI-Nodes](https://github.com/gseth/ControlAltAI-Nodes)
**Install Type:** git-clone

---

### ControlNet-LLLite-ComfyUI

**Description:**

Nodes: LLLiteLoader

- **Author:** kohya-ss
- **Repository:** [https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is designed specifically for ControlNet-LLLite and can be used as a supporting node in the inpainting workflow.

### Metadata
**Author:** kohya-ss
**Repository:** [https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)
**Install Type:** git-clone

---

### Cozy Human Parser

**Description:**

A ComfyUI node to automatically extract masks for body regions and clothing/fashion items. Made with 💚 by the CozyMantis squad.

- **Author:** CozyMantis
- **Repository:** [https://github.com/cozymantis/human-parser-comfyui-node](https://github.com/cozymantis/human-parser-comfyui-node)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can automatically extract masks for body regions and clothing/fashion items, making it essential for the inpainting workflow with mask input.

### Metadata
**Author:** CozyMantis
**Repository:** [https://github.com/cozymantis/human-parser-comfyui-node](https://github.com/cozymantis/human-parser-comfyui-node)
**Install Type:** git-clone

---

### CrasH Utils

**Description:**

A mixture of effects and quality of life nodes. Nodes: ImageGlitcher (gives an image a cool glitchy effect), ColorStylizer (highlights a single color in an image), QueryLocalLLM (queries a local LLM API though oobabooga), SDXLReslution (resolution picker for the standard SDXL resolutions, the complete list), SDXLResolutionSplit (splits the SDXL resolution into width and height). 

- **Author:** chrish-slingshot
- **Repository:** [https://github.com/chrish-slingshot/CrasHUtils](https://github.com/chrish-slingshot/CrasHUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains ImageGlitcher which is marginally relevant and ColorStylizer which could be useful for image processing, making it very useful for the specified workflow goal.

### Metadata
**Author:** chrish-slingshot
**Repository:** [https://github.com/chrish-slingshot/CrasHUtils](https://github.com/chrish-slingshot/CrasHUtils)
**Install Type:** git-clone

---

### Crystools

**Description:**

With this suit, you can see the resources monitor, progress bar & time elapsed, metadata and compare between two images, compare between two JSONs, show any value to console/display, pipes, and more!
This provides better nodes to load/save images, previews, etc, and see "hidden" data without loading a new workflow.

- **Author:** Crystian
- **Repository:** [https://github.com/crystian/ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node contains various utility nodes such as resources monitor, progress bar & time elapsed, metadata comparison, and more which could be useful for workflow management making it moderately useful for the specified workflow goal.

### Metadata
**Author:** Crystian
**Repository:** [https://github.com/crystian/ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)
**Install Type:** git-clone

---

### CS Transform Node for ComfyUI

**Description:**

The CS Transform node is a custom node for ComfyUI that applies a series of transformations to an input image and mask. The transformations include scaling, rotation, and translation, all centered around a specified pivot point. The node ensures that the transformed image is properly accommodated within a canvas, which can be expanded if needed.

- **Author:** claussteinmassl
- **Repository:** [https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes](https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node applies transformations to an image and mask, which could be essential in preparing or processing the input data for the inpainting workflow.

### Metadata
**Author:** claussteinmassl
**Repository:** [https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes](https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes)
**Install Type:** git-clone

---

### CSV Search Node

**Description:**

This repository contains a custom node for ComfyUI that allows searching for a keyword in the first column of a CSV file and returning a value from a specified column in that row. The node is designed to be modular and fit within the node-based workflow of ComfyUI.

- **Author:** folkghost
- **Repository:** [https://github.com/folkghost/comfyui_search_csv](https://github.com/folkghost/comfyui_search_csv)
- **Install Type:** copy


### Applicability

**Score:** 40/100

**Reason:** This node can be useful as a supporting tool in the workflow by allowing searching for specific values within CSV files, but it is not essential for the inpainting process itself.

### Metadata
**Author:** folkghost
**Repository:** [https://github.com/folkghost/comfyui_search_csv](https://github.com/folkghost/comfyui_search_csv)
**Install Type:** copy

---

### Customizable API Call Nodes by BillBum

**Description:**

API call node for Third-party platforms both official and local. Support VLMs LLMs Dalle3 Flux-Pro SD3 etc. And some little tools: img to b64 url, b64 url to img, b64 url to b64 data, reg text to word and ',' only, etc.

- **Author:** AhBumm
- **Repository:** [https://github.com/AhBumm/ComfyUI_BillBum_Nodes](https://github.com/AhBumm/ComfyUI_BillBum_Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This API call node could potentially support the inpainting workflow by allowing integration with third-party platforms or services that may offer inpainting capabilities.

### Metadata
**Author:** AhBumm
**Repository:** [https://github.com/AhBumm/ComfyUI_BillBum_Nodes](https://github.com/AhBumm/ComfyUI_BillBum_Nodes)
**Install Type:** git-clone

---

### D2 Size Selector

**Description:**

This is a custom node that allows you to easily call up and set image size presets. Settings can be made by editing the included config.yaml. It is almost identical to Comfyroll Studio's CR AspectRatio. I created it because I wanted to easily edit the presets.

- **Author:** da2el-ai
- **Repository:** [https://github.com/da2el-ai/ComfyUI-d2-size-selector](https://github.com/da2el-ai/ComfyUI-d2-size-selector)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows you to easily set and select image size presets which can be useful for preparing input images for inpainting with mask input.

### Metadata
**Author:** da2el-ai
**Repository:** [https://github.com/da2el-ai/ComfyUI-d2-size-selector](https://github.com/da2el-ai/ComfyUI-d2-size-selector)
**Install Type:** git-clone

---

### D2 Steps

**Description:**

A handy custom node for using Refiner (switching to a different checkpoint midway) When you specify the end of the base checkpoint, you can extract refiner_start which is end + 1. The output is fixed as an INT, so it can be passed to the handy custom node, Anything Everywhere? Since it only outputs a numerical value, it can also be used for other purposes.

- **Author:** da2el-ai
- **Repository:** [https://github.com/da2el-ai/ComfyUI-d2-steps](https://github.com/da2el-ai/ComfyUI-d2-steps)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a way to switch to a different checkpoint in the Refiner but its direct relevance to inpainting with mask input is limited.

### Metadata
**Author:** da2el-ai
**Repository:** [https://github.com/da2el-ai/ComfyUI-d2-steps](https://github.com/da2el-ai/ComfyUI-d2-steps)
**Install Type:** git-clone

---

### DarkPrompts

**Description:**

Slightly better random prompt generation tools that allow combining and picking prompts from both file and text input sources.

- **Author:** darkpixel
- **Repository:** [https://github.com/darkpixel/darkprompts](https://github.com/darkpixel/darkprompts)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** DarkPrompts offers improved random prompt generation tools that can be used in conjunction with a mask input, making it very useful for this workflow goal.

### Metadata
**Author:** darkpixel
**Repository:** [https://github.com/darkpixel/darkprompts](https://github.com/darkpixel/darkprompts)
**Install Type:** git-clone

---

### Dashscope FLUX API for ComfyUI

**Description:**

The FLUX model API from DashScope, developed by Black Forest Labs, offers superior image generation capabilities with optimized support for Chinese prompts, achieving a commendable tradeoff between performance and the quality of generated images compared to other open-source models.

- **Author:** Artiprocher
- **Repository:** [https://github.com/modelscope/comfyscope](https://github.com/modelscope/comfyscope)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** The FLUX model API from DashScope is highly relevant and essential for achieving high-quality image generation capabilities, especially when working with Chinese prompts, making it a crucial component of the inpainting workflow.

### Metadata
**Author:** Artiprocher
**Repository:** [https://github.com/modelscope/comfyscope](https://github.com/modelscope/comfyscope)
**Install Type:** git-clone

---

### Deforum Nodes

**Description:**

Official Deforum animation pipeline tools that provide a unique way to create frame-by-frame generative motion art.

- **Author:** deforum
- **Repository:** [https://github.com/XmYx/deforum-comfy-nodes](https://github.com/XmYx/deforum-comfy-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Deforum Nodes are relevant to animation and motion art creation, which can be useful for the inpainting workflow goal, especially if the goal involves creating generative or artistic content.

### Metadata
**Author:** deforum
**Repository:** [https://github.com/XmYx/deforum-comfy-nodes](https://github.com/XmYx/deforum-comfy-nodes)
**Install Type:** git-clone

---

### demofusion-comfyui

**Description:**

The Demofusion Custom Node is a wrapper that adapts the work and implementation of the [a/DemoFusion](https://ruoyidu.github.io/demofusion/demofusion.html) technique created and implemented by Ruoyi Du to the Comfyui environment.

- **Author:** deroberon
- **Repository:** [https://github.com/deroberon/demofusion-comfyui](https://github.com/deroberon/demofusion-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Demofusion-comfyui is a wrapper of the Demofusion technique, but its direct relevance to inpainting with mask input is unclear; further investigation may be needed to determine its utility in this workflow.

### Metadata
**Author:** deroberon
**Repository:** [https://github.com/deroberon/demofusion-comfyui](https://github.com/deroberon/demofusion-comfyui)
**Install Type:** git-clone

---

### Den_ComfyUI_Workflows

**Description:**

Custom nodes make easy Advanced Workflows. Focus on Image/Video and ControlNet efficiency and performances. Manipulation of Latent Space, Automatic pipeline with a bit efforts.

- **Author:** denfrost
- **Repository:** [https://github.com/denfrost/Den_ComfyUI_Workflow](https://github.com/denfrost/Den_ComfyUI_Workflow)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Den_ComfyUI_Workflows seems highly relevant and useful for the inpainting workflow goal, as it focuses on image/video manipulation, latent space control, and automatic pipeline creation, which are all essential aspects of inpainting with mask input.

### Metadata
**Author:** denfrost
**Repository:** [https://github.com/denfrost/Den_ComfyUI_Workflow](https://github.com/denfrost/Den_ComfyUI_Workflow)
**Install Type:** git-clone

---

### DepthFM IN COMFYUI

**Description:**

Unofficial implementation of [a/DepthFM](https://github.com/CompVis/depth-fm) for ComfyUI

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node can be useful in supporting the inpainting workflow by providing a method for estimating depth maps from images.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM)
**Install Type:** git-clone

---

### DiffMorpher-ComfyUI

**Description:**

a custom node for [a/DiffMorpher](https://github.com/Kevin-thu/DiffMorpher),you can find base workflow in [a/doc](https://github.com/AIFSH/DiffMorpher-ComfyUI/blob/main/doc)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/DiffMorpher-ComfyUI](https://github.com/AIFSH/DiffMorpher-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a custom implementation of DiffMorpher specifically designed for ComfyUI, making it highly relevant to the inpainting workflow with mask input.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/DiffMorpher-ComfyUI](https://github.com/AIFSH/DiffMorpher-ComfyUI)
**Install Type:** git-clone

---

### DiffSynth-ComfyUI

**Description:**

a custom node for [a/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/DiffSynth-ComfyUI](https://github.com/AIFSH/DiffSynth-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node provides a custom interface for DiffSynth-Studio, which can be useful in an inpainting workflow with mask input, but its direct relevance is lower compared to other nodes.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/DiffSynth-ComfyUI](https://github.com/AIFSH/DiffSynth-ComfyUI)
**Install Type:** git-clone

---

### Diffusers-in-ComfyUI

**Description:**

A collection of ComfyUI custom nodes that allow to use most Diffusers pipelines and components in Comfy(Txt2Img, Img2Img, Inpainting, LoRAS, B-LoRAS, ControlNet...)

- **Author:** Dr.Jusseaux
- **Repository:** [https://github.com/maepopi/Diffusers-in-ComfyUI](https://github.com/maepopi/Diffusers-in-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node collection includes a wide range of Diffusers pipelines and components specifically designed for ComfyUI, including inpainting, making it essential for this workflow goal.

### Metadata
**Author:** Dr.Jusseaux
**Repository:** [https://github.com/maepopi/Diffusers-in-ComfyUI](https://github.com/maepopi/Diffusers-in-ComfyUI)
**Install Type:** git-clone

---

### Diffusion360_ComfyUI

**Description:**

ComfyUI plugin of [a/SD-T2I-360PanoImage](https://github.com/ArcherFMY/SD-T2I-360PanoImage).
base t2i-pipeline for generating 512*1024 panorama image from text input

- **Author:** ArcherFMY
- **Repository:** [https://github.com/ArcherFMY/Diffusion360_ComfyUI](https://github.com/ArcherFMY/Diffusion360_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides a plugin for generating panorama images from text input but could potentially be used as a supporting node in an inpainting workflow with some creative adaptation.

### Metadata
**Author:** ArcherFMY
**Repository:** [https://github.com/ArcherFMY/Diffusion360_ComfyUI](https://github.com/ArcherFMY/Diffusion360_ComfyUI)
**Install Type:** git-clone

---

### Dimensional Latent Perlin for ComfyUI

**Description:**

Dimensional Latent Perlin is a custom node for ComfyUI that generates Perlin noise in the latent space. This node is designed to work seamlessly with various diffusion models and can be used as an alternative or complement to standard random noise generators in image generation pipelines.

- **Author:** NeuralSamurAI
- **Repository:** [https://github.com/NeuralSamurAI/ComfyUI-Dimensional-Latent-Perlin](https://github.com/NeuralSamurAI/ComfyUI-Dimensional-Latent-Perlin)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node generates Perlin noise in the latent space and could be useful as a supporting node in an inpainting workflow to introduce additional texture or structure into generated images.

### Metadata
**Author:** NeuralSamurAI
**Repository:** [https://github.com/NeuralSamurAI/ComfyUI-Dimensional-Latent-Perlin](https://github.com/NeuralSamurAI/ComfyUI-Dimensional-Latent-Perlin)
**Install Type:** git-clone

---

### Disco Diffusion

**Description:**

Modularized version of Disco Diffusion for use with ComfyUI.

- **Author:** space-nuko
- **Repository:** [https://github.com/space-nuko/ComfyUI-Disco-Diffusion](https://github.com/space-nuko/ComfyUI-Disco-Diffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node is highly relevant and useful for the inpainting workflow with mask input, being a modularized version of Disco Diffusion specifically designed for ComfyUI.

### Metadata
**Author:** space-nuko
**Repository:** [https://github.com/space-nuko/ComfyUI-Disco-Diffusion](https://github.com/space-nuko/ComfyUI-Disco-Diffusion)
**Install Type:** git-clone

---

### Dynamic Prompts

**Description:**

Nodes that implement functionality similar to the Dynamic Prompts extension for A1111.

- **Author:** exectails
- **Repository:** [https://github.com/exectails/comfyui-et_dynamicprompts](https://github.com/exectails/comfyui-et_dynamicprompts)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Node implements functionality similar to Dynamic Prompts which can be useful in generating dynamic prompts for inpainting tasks.

### Metadata
**Author:** exectails
**Repository:** [https://github.com/exectails/comfyui-et_dynamicprompts](https://github.com/exectails/comfyui-et_dynamicprompts)
**Install Type:** git-clone

---

### Dynamic Thresholding

**Description:**

Adds nodes for Dynamic Thresholding, CFG scheduling, and related techniques.

- **Author:** mcmonkeyprojects
- **Repository:** [https://github.com/mcmonkeyprojects/sd-dynamic-thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Node adds nodes for Dynamic Thresholding and CFG scheduling that are directly relevant to optimizing inpainting results with a mask input.

### Metadata
**Author:** mcmonkeyprojects
**Repository:** [https://github.com/mcmonkeyprojects/sd-dynamic-thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)
**Install Type:** git-clone

---

### DynamicPose-ComfyUI

**Description:**

NODES:pose_extraction, Load_reference_unet, Load_denoising_unet, Load_Pose_Guider, Pose_Guider_Encode, DynamicPose_Sampler, load_pose_model, align

- **Author:** Bin-sam
- **Repository:** [https://github.com/Bin-sam/DynamicPose-ComfyUI](https://github.com/Bin-sam/DynamicPose-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node has a high relevance and utility for the specified workflow goal as it involves pose extraction and dynamic sampling which can aid in inpainting with mask input.

### Metadata
**Author:** Bin-sam
**Repository:** [https://github.com/Bin-sam/DynamicPose-ComfyUI](https://github.com/Bin-sam/DynamicPose-ComfyUI)
**Install Type:** git-clone

---

### DynamicPrompts Custom Nodes

**Description:**

Nodes: Random Prompts, Combinatorial Prompts, I'm Feeling Lucky, Magic Prompt, Jinja2 Templates. ComfyUI-DynamicPrompts is a custom nodes library that integrates into your existing ComfyUI Library. It provides nodes that enable the use of Dynamic Prompts in your ComfyUI.

- **Author:** adieyal
- **Repository:** [https://github.com/adieyal/comfyui-dynamicprompts](https://github.com/adieyal/comfyui-dynamicprompts)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant and useful for the specified workflow goal as it provides custom nodes for dynamic prompts that can be used to generate masks or guide the inpainting process.

### Metadata
**Author:** adieyal
**Repository:** [https://github.com/adieyal/comfyui-dynamicprompts](https://github.com/adieyal/comfyui-dynamicprompts)
**Install Type:** git-clone

---

### DZ-FaceDetailer

**Description:**

Face Detailer is a custom node for the 'ComfyUI' framework inspired by !After Detailer extension from auto1111, it allows you to detect faces using Mediapipe and YOLOv8n to create masks for the detected faces.

- **Author:** daxthin
- **Repository:** [https://github.com/nicofdga/DZ-FaceDetailer](https://github.com/nicofdga/DZ-FaceDetailer)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node has a very high relevance and utility for the specified workflow goal as it specifically deals with face detection using Mediapipe and YOLOv8n to create masks which is directly applicable to inpainting workflows.

### Metadata
**Author:** daxthin
**Repository:** [https://github.com/nicofdga/DZ-FaceDetailer](https://github.com/nicofdga/DZ-FaceDetailer)
**Install Type:** git-clone

---

### Easy automatic (square) image cropper using Yolo

**Description:**

A very simple and easy to use node to automaticaaly create (square) image crops and masks using YoloV8. This can be very useful when using controlnet and ip adapters

- **Author:** Tool Of North america
- **Repository:** [https://github.com/tooldigital/ComfyUI-Yolo-Cropper](https://github.com/tooldigital/ComfyUI-Yolo-Cropper)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node can automatically create square image crops and masks using YoloV8, which would be very useful for creating masks in the inpainting workflow.

### Metadata
**Author:** Tool Of North america
**Repository:** [https://github.com/tooldigital/ComfyUI-Yolo-Cropper](https://github.com/tooldigital/ComfyUI-Yolo-Cropper)
**Install Type:** git-clone

---

### EasyCaptureNode for ComfyUI

**Description:**

Capture window content from other programs, easyway combined with LCM for real-time painting

- **Author:** zhuanqianfish
- **Repository:** [https://github.com/zhuanqianfish/ComfyUI-EasyNode](https://github.com/zhuanqianfish/ComfyUI-EasyNode)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node can capture window content from other programs and could potentially be used for real-time painting in the inpainting workflow, making it moderately useful.

### Metadata
**Author:** zhuanqianfish
**Repository:** [https://github.com/zhuanqianfish/ComfyUI-EasyNode](https://github.com/zhuanqianfish/ComfyUI-EasyNode)
**Install Type:** git-clone

---

### Eden.art LoRa Trainer

**Description:**

Maintained by Eden.art, this is a very fast, well tuned trainer for SDXL and SD15

- **Author:** aiXander
- **Repository:** [https://github.com/edenartlab/sd-lora-trainer](https://github.com/edenartlab/sd-lora-trainer)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for LoRa training and can likely be used as part of an inpainting workflow with mask input.

### Metadata
**Author:** aiXander
**Repository:** [https://github.com/edenartlab/sd-lora-trainer](https://github.com/edenartlab/sd-lora-trainer)
**Install Type:** git-clone

---

### Eden.art nodesuite

**Description:**

Maintained by Eden.art, this is a growing suite of custom nodes for building advanced pipelines.

- **Author:** aiXander
- **Repository:** [https://github.com/edenartlab/eden_comfy_pipelines](https://github.com/edenartlab/eden_comfy_pipelines)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** As part of the Eden.art nodesuite, this node may contain custom nodes that could be useful for building advanced inpainting pipelines.

### Metadata
**Author:** aiXander
**Repository:** [https://github.com/edenartlab/eden_comfy_pipelines](https://github.com/edenartlab/eden_comfy_pipelines)
**Install Type:** git-clone

---

### Embedding Merge for ComfyUI

**Description:**

Extremely inspired and forked from: [a/https://github.com/klimaleksus/stable-diffusion-webui-embedding-merge](https://github.com/klimaleksus/stable-diffusion-webui-embedding-merge)

- **Author:** duskfallcrew
- **Repository:** [https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node](https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node)
- **Install Type:** copy


### Applicability

**Score:** 90/100

**Reason:** The Embedding Merge node is highly relevant and useful for the specified workflow goal as it can help merge embeddings which are crucial for inpainting with a mask input.

### Metadata
**Author:** duskfallcrew
**Repository:** [https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node](https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node)
**Install Type:** copy

---

### Embedding Picker

**Description:**

Tired of forgetting and misspelling often weird names of embeddings you use? Or perhaps you use only one, cause you forgot you have tens of them installed?

- **Author:** Tropfchen
- **Repository:** [https://github.com/Tropfchen/ComfyUI-Embedding_Picker](https://github.com/Tropfchen/ComfyUI-Embedding_Picker)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** The Embedding Picker node might be marginally useful for the specified workflow goal as it can help manage and select embeddings, which could indirectly aid in inpainting with a mask input.

### Metadata
**Author:** Tropfchen
**Repository:** [https://github.com/Tropfchen/ComfyUI-Embedding_Picker](https://github.com/Tropfchen/ComfyUI-Embedding_Picker)
**Install Type:** git-clone

---

### Endless ️🌊✨ Nodes

**Description:**

A small set of nodes I created for various numerical and text inputs.  Features image saver with ability to have JSON saved to separate folder, parameter collection nodes, two aesthetic scoring models, switches for text and numbers, and conversion of string to numeric and vice versa.

- **Author:** BiffMunky
- **Repository:** [https://github.com/tusharbhutt/Endless-Nodes](https://github.com/tusharbhutt/Endless-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node pack includes various nodes that could support an inpainting workflow, such as image saver and parameter collection nodes.

### Metadata
**Author:** BiffMunky
**Repository:** [https://github.com/tusharbhutt/Endless-Nodes](https://github.com/tusharbhutt/Endless-Nodes)
**Install Type:** git-clone

---

### Euler-Smea-Dyn-Sampler

**Description:**

СomfyUI version of [a/Euler Smea Dyn Sampler](https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler). It adds samplers directly to KSampler nodes.

- **Author:** Koishi-Star
- **Repository:** [https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler](https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node adds samplers to KSampler nodes but does not directly contribute to the inpainting process with a mask input.

### Metadata
**Author:** Koishi-Star
**Repository:** [https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler](https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler)
**Install Type:** git-clone

---

### F5-TTS-ComfyUI

**Description:**

a custom node for [a/F5-TTS](https://github.com/SWivid/F5-TTS)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/F5-TTS-ComfyUI](https://github.com/AIFSH/F5-TTS-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This custom node is directly related to the F5-TTS model and can be used in conjunction with the inpainting workflow.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/F5-TTS-ComfyUI](https://github.com/AIFSH/F5-TTS-ComfyUI)
**Install Type:** git-clone

---

### Face Compare

**Description:**

Nodes:FaceCompare

- **Author:** czcz1024
- **Repository:** [https://github.com/czcz1024/Comfyui-FaceCompare](https://github.com/czcz1024/Comfyui-FaceCompare)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to comparing faces and can be used in conjunction with the inpainting workflow for tasks like facial inpainting or object removal.

### Metadata
**Author:** czcz1024
**Repository:** [https://github.com/czcz1024/Comfyui-FaceCompare](https://github.com/czcz1024/Comfyui-FaceCompare)
**Install Type:** git-clone

---

### Face Restorer for ComfyUI

**Description:**

The face restore node for ComfyUI, based on RestoreFormer

- **Author:** tungdop2
- **Repository:** [https://github.com/tungdop2/Comfyui_face_restorer](https://github.com/tungdop2/Comfyui_face_restorer)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** The Face Restorer is directly relevant to restoring faces in images which aligns with the inpainting workflow goal.

### Metadata
**Author:** tungdop2
**Repository:** [https://github.com/tungdop2/Comfyui_face_restorer](https://github.com/tungdop2/Comfyui_face_restorer)
**Install Type:** git-clone

---

### Faceless Node for ComfyUI

**Description:**

A facefusion custom node for ComfyUI. Swap or restore faces for image or video

- **Author:** jeffy5
- **Repository:** [https://github.com/jeffy5/comfyui-faceless-node](https://github.com/jeffy5/comfyui-faceless-node)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** The Faceless Node can be used as a supporting node for face manipulation tasks but may not directly contribute to inpainting.

### Metadata
**Author:** jeffy5
**Repository:** [https://github.com/jeffy5/comfyui-faceless-node](https://github.com/jeffy5/comfyui-faceless-node)
**Install Type:** git-clone

---

### Facerestore CF (Code Former)

**Description:**

This is a copy of [a/facerestore custom node](https://civitai.com/models/24690/comfyui-facerestore-node) with a bit of a change to support CodeFormer Fidelity parameter. These ComfyUI nodes can be used to restore faces in images similar to the face restore option in AUTOMATIC1111 webui.
NOTE: To use this node, you need to download the face restoration model and face detection model from the 'Install models' menu.

- **Author:** mav-rik
- **Repository:** [https://github.com/mav-rik/facerestore_cf](https://github.com/mav-rik/facerestore_cf)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Facerestore CF is highly relevant and useful for restoring faces in images with support for CodeFormer Fidelity parameter.

### Metadata
**Author:** mav-rik
**Repository:** [https://github.com/mav-rik/facerestore_cf](https://github.com/mav-rik/facerestore_cf)
**Install Type:** git-clone

---

### FAI-Node

**Description:**

Various custom nodes for ComfyUI

- **Author:** Fantasy AI Studio
- **Repository:** [https://github.com/alanhuang67/ComfyUI-FAI-Node](https://github.com/alanhuang67/ComfyUI-FAI-Node)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** FAI-Node seems to be a collection of custom nodes, but one of them might be related to inpainting or image manipulation, making it very useful for the specified workflow goal.

### Metadata
**Author:** Fantasy AI Studio
**Repository:** [https://github.com/alanhuang67/ComfyUI-FAI-Node](https://github.com/alanhuang67/ComfyUI-FAI-Node)
**Install Type:** git-clone

---

### fcSuite

**Description:**

fcFloatMatic is a custom module, that when configured correctly will increment through the lines generating you loras at different strengths. The JSON file will load the config.

- **Author:** fitCorder
- **Repository:** [https://github.com/fitCorder/fcSuite](https://github.com/fitCorder/fcSuite)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** This custom module seems highly relevant for the specified workflow goal as it can generate different strengths of output based on configuration.

### Metadata
**Author:** fitCorder
**Repository:** [https://github.com/fitCorder/fcSuite](https://github.com/fitCorder/fcSuite)
**Install Type:** copy

---

### FitDiT

**Description:**

[a/FitDiT](https://arxiv.org/abs/2411.10499): Advancing the Authentic Garment Details for High-fidelity Virtual Try-onon

- **Author:** Jash-Vora
- **Repository:** [https://github.com/Jash-Vora/ComfyUI-GarmentDiT](https://github.com/Jash-Vora/ComfyUI-GarmentDiT)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node is for garment details and virtual try-on, it might have some utility as a supporting node due to its image processing capabilities.

### Metadata
**Author:** Jash-Vora
**Repository:** [https://github.com/Jash-Vora/ComfyUI-GarmentDiT](https://github.com/Jash-Vora/ComfyUI-GarmentDiT)
**Install Type:** git-clone

---

### FizzNodes

**Description:**

Scheduled prompts, scheduled float/int values and wave function nodes for animations and utility. compatable with [a/framesync](https://www.framesync.xyz/) and [a/keyframe-string-generator](https://www.chigozie.co.uk/keyframe-string-generator/) for audio synced animations in Comfyui.

- **Author:** FizzleDorf
- **Repository:** [https://github.com/FizzleDorf/ComfyUI_FizzNodes](https://github.com/FizzleDorf/ComfyUI_FizzNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides scheduled prompts and float/int values which can be useful in animations and utility tasks that may support or aid the inpainting workflow with mask input.

### Metadata
**Author:** FizzleDorf
**Repository:** [https://github.com/FizzleDorf/ComfyUI_FizzNodes](https://github.com/FizzleDorf/ComfyUI_FizzNodes)
**Install Type:** git-clone

---

### florence_dw

**Description:**

Based on the original repository [a/https://github.com/spacepxl/ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2), the model loading and storage methods have been improved, and sd3 has been newly added with enhanced speed and accuracy.

- **Author:** yiwangsimple
- **Repository:** [https://github.com/yiwangsimple/florence_dw](https://github.com/yiwangsimple/florence_dw)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** florence_dw is a model loading and storage method that can be used for inpainting tasks, making it highly relevant to the workflow goal.

### Metadata
**Author:** yiwangsimple
**Repository:** [https://github.com/yiwangsimple/florence_dw](https://github.com/yiwangsimple/florence_dw)
**Install Type:** git-clone

---

### Flux Prompt Generator for ComfyUI

**Description:**

A flexible and customizable prompt generator for generating detailed and creative prompts for image generation models for ComfyUI

- **Author:** fairy-root
- **Repository:** [https://github.com/fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Very useful as a supporting node for generating detailed prompts for inpainting.

### Metadata
**Author:** fairy-root
**Repository:** [https://github.com/fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator)
**Install Type:** git-clone

---

### FluxPseudoNegative

**Description:**

FluxPseudoNegative is an advanced custom node for ComfyUI that converts negative prompts into positive ones. It's designed to enhance prompt engineering for image generation models that don't natively support negative prompts or where using negative prompts significantly increases generation time. So instead of hacking CFG we simply invert your negative words and find their antonyms!

- **Author:** NeuralSamurAI
- **Repository:** [https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt](https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Essential for this workflow; converting negative prompts into positive ones can significantly enhance inpainting results.

### Metadata
**Author:** NeuralSamurAI
**Repository:** [https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt](https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt)
**Install Type:** git-clone

---

### FM_nodes

**Description:**

A collection of ComfyUI nodes. Including: WFEN, RealViFormer, ProPIH

- **Author:** Fuou Marinas
- **Repository:** [https://github.com/FuouM/FM_nodes](https://github.com/FuouM/FM_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** FM_nodes includes WFEN and RealViFormer which are directly relevant to inpainting with mask input.

### Metadata
**Author:** Fuou Marinas
**Repository:** [https://github.com/FuouM/FM_nodes](https://github.com/FuouM/FM_nodes)
**Install Type:** git-clone

---

### foxpack

**Description:**

Collection of nodes for the automation of workflows

- **Author:** gisu
- **Repository:** [https://github.com/gisu/comfyui-foxpack](https://github.com/gisu/comfyui-foxpack)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** foxpack is a collection of automation nodes but does not specifically mention inpainting or mask inputs.

### Metadata
**Author:** gisu
**Repository:** [https://github.com/gisu/comfyui-foxpack](https://github.com/gisu/comfyui-foxpack)
**Install Type:** git-clone

---

### FreeU_Advanced

**Description:**

This custom node provides advanced settings for FreeU.

- **Author:** WASasquatch
- **Repository:** [https://github.com/WASasquatch/FreeU_Advanced](https://github.com/WASasquatch/FreeU_Advanced)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** FreeU_Advanced provides advanced settings which might be useful in an inpainting workflow, but its direct relevance to the goal is moderate.

### Metadata
**Author:** WASasquatch
**Repository:** [https://github.com/WASasquatch/FreeU_Advanced](https://github.com/WASasquatch/FreeU_Advanced)
**Install Type:** git-clone

---

### Gallery&Tabs

**Description:**

Adds a gallery to the Load Image node and tabs for Load Checkpoint/Lora/etc nodes

- **Author:** OgreLemonSoup
- **Repository:** [https://github.com/OgreLemonSoup/ComfyUI-Load-Image-Gallery](https://github.com/OgreLemonSoup/ComfyUI-Load-Image-Gallery)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node adds a gallery and tabs for loading images/checkpoints, which could be moderately useful as a supporting feature in the workflow, but it doesn"t directly contribute to inpainting or mask input.

### Metadata
**Author:** OgreLemonSoup
**Repository:** [https://github.com/OgreLemonSoup/ComfyUI-Load-Image-Gallery](https://github.com/OgreLemonSoup/ComfyUI-Load-Image-Gallery)
**Install Type:** git-clone

---

### GeminiOllama ComfyUI Extension

**Description:**

This extension integrates Google's Gemini API and Ollama into ComfyUI, allowing users to leverage these powerful language models directly within their ComfyUI workflows.

- **Author:** al-swaiti
- **Repository:** [https://github.com/al-swaiti/ComfyUI-OllamaGemini](https://github.com/al-swaiti/ComfyUI-OllamaGemini)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node integrates Gemini API and Ollama into ComfyUI, making it essential for leveraging powerful language models in the inpainting workflow.

### Metadata
**Author:** al-swaiti
**Repository:** [https://github.com/al-swaiti/ComfyUI-OllamaGemini](https://github.com/al-swaiti/ComfyUI-OllamaGemini)
**Install Type:** git-clone

---

### GFrbmg2

**Description:**

This custom node for ComfyUI provides advanced background removal capabilities using the briaai/RMBG-2.0 model. It is designed to seamlessly integrate into the ComfyUI environment, offering users a powerful tool for image processing tasks.

- **Author:** GorillaFrame
- **Repository:** [https://github.com/gorillaframeai/GF_nodes](https://github.com/gorillaframeai/GF_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This custom node provides advanced background removal capabilities using the briaai/RMBG-2.0 model, making it very useful for the specified workflow goal.

### Metadata
**Author:** GorillaFrame
**Repository:** [https://github.com/gorillaframeai/GF_nodes](https://github.com/gorillaframeai/GF_nodes)
**Install Type:** git-clone

---

### GLSL Nodes

**Description:**

A collections of nodes to support GLSL shaders inside a workflow.

- **Author:** Patricio Gonzalez Vivo
- **Repository:** [https://github.com/patriciogonzalezvivo/comfyui_glslnodes](https://github.com/patriciogonzalezvivo/comfyui_glslnodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This collection of nodes supports GLSL shaders, which might be useful for image processing tasks in general, but is only marginally relevant to the specified workflow goal.

### Metadata
**Author:** Patricio Gonzalez Vivo
**Repository:** [https://github.com/patriciogonzalezvivo/comfyui_glslnodes](https://github.com/patriciogonzalezvivo/comfyui_glslnodes)
**Install Type:** git-clone

---

### GPU temperature protection

**Description:**

Pause image generation when GPU temperature exceeds threshold.

- **Author:** meap158
- **Repository:** [https://github.com/meap158/ComfyUI-GPU-temperature-protection](https://github.com/meap158/ComfyUI-GPU-temperature-protection)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it pauses image generation when GPU temperature exceeds threshold, preventing potential damage or slowdowns during the inpainting process.

### Metadata
**Author:** meap158
**Repository:** [https://github.com/meap158/ComfyUI-GPU-temperature-protection](https://github.com/meap158/ComfyUI-GPU-temperature-protection)
**Install Type:** git-clone

---

### GSTTS-ComfyUI

**Description:**

a comfyui custom node for [a/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/GSTTS-ComfyUI](https://github.com/AIFSH/GSTTS-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** GSTTS-ComfyUI seems highly relevant and potentially essential for the specified workflow goal given its custom design for inpainting tasks.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/GSTTS-ComfyUI](https://github.com/AIFSH/GSTTS-ComfyUI)
**Install Type:** git-clone

---

### Hakkun-ComfyUI-nodes

**Description:**

Nodes: Prompt parser. ComfyUI extra nodes. Mostly prompt parsing.

- **Author:** tudal
- **Repository:** [https://github.com/tudal/Hakkun-ComfyUI-nodes](https://github.com/tudal/Hakkun-ComfyUI-nodes)
- **Install Type:** copy


### Applicability

**Score:** 40/100

**Reason:** Hakkun-ComfyUI-nodes contains some potentially useful prompt parsing functionality but its overall utility is uncertain without more information about its specific features and capabilities.

### Metadata
**Author:** tudal
**Repository:** [https://github.com/tudal/Hakkun-ComfyUI-nodes](https://github.com/tudal/Hakkun-ComfyUI-nodes)
**Install Type:** copy

---

### Hayo comfyui nodes

**Description:**

Nodes:tensor_trans_pil, Make Transparent mask, MergeImages, words_generatee, load_PIL image

- **Author:** LZC
- **Repository:** [https://github.com/1shadow1/hayo_comfyui_nodes](https://github.com/1shadow1/hayo_comfyui_nodes)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** This pack contains several nodes (Make Transparent mask, MergeImages) that are directly relevant to working with masks in an inpainting workflow.

### Metadata
**Author:** LZC
**Repository:** [https://github.com/1shadow1/hayo_comfyui_nodes](https://github.com/1shadow1/hayo_comfyui_nodes)
**Install Type:** copy

---

### hd-nodes-comfyui

**Description:**

Nodes:Combine HDMasks, Cover HDMasks, HD FaceIndex, HD SmoothEdge, HD GetMaskArea, HD Image Levels, HD Ultimate SD Upscale

- **Author:** xiaoxiaodesha
- **Repository:** [https://github.com/xiaoxiaodesha/hd_node](https://github.com/xiaoxiaodesha/hd_node)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node pack includes several high-quality nodes specifically designed for handling HD masks and images, making it very useful for the specified workflow goal.

### Metadata
**Author:** xiaoxiaodesha
**Repository:** [https://github.com/xiaoxiaodesha/hd_node](https://github.com/xiaoxiaodesha/hd_node)
**Install Type:** git-clone

---

### HFDownLoad Node for ComfyUI

**Description:**

Download the model from huggingface and put it in any directory.

- **Author:** icesun963
- **Repository:** [https://github.com/icesun963/ComfyUI_HFDownLoad](https://github.com/icesun963/ComfyUI_HFDownLoad)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for downloading models from huggingface which can be used in the inpainting workflow with mask input.

### Metadata
**Author:** icesun963
**Repository:** [https://github.com/icesun963/ComfyUI_HFDownLoad](https://github.com/icesun963/ComfyUI_HFDownLoad)
**Install Type:** git-clone

---

### Human Parts Detector

**Description:**

Detect human parts using the DeepLabV3+ ResNet50 model from Keras-io. You can extract hair, arms, legs, and other parts with ease and with small memory usage.

- **Author:** Metal3d
- **Repository:** [https://github.com/metal3d/ComfyUI_Human_Parts](https://github.com/metal3d/ComfyUI_Human_Parts)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is directly related to detecting human parts which can be useful for inpainting workflows that involve human subjects.

### Metadata
**Author:** Metal3d
**Repository:** [https://github.com/metal3d/ComfyUI_Human_Parts](https://github.com/metal3d/ComfyUI_Human_Parts)
**Install Type:** git-clone

---

### IC-Light-ComfyUI-Node

**Description:**

Original repo: [a/https://github.com/lllyasviel/IC-Light](https://github.com/lllyasviel/IC-Light)
Models: [a/https://huggingface.co/lllyasviel/ic-light/tree/main](https://huggingface.co/lllyasviel/ic-light/tree/main), [a/https://huggingface.co/digiplay/Photon_v1/tree/main](https://huggingface.co/digiplay/Photon_v1/tree/main)
models go into ComfyUI/models/unet

- **Author:** Fihade
- **Repository:** [https://github.com/Fihade/IC-Light-ComfyUI-Node](https://github.com/Fihade/IC-Light-ComfyUI-Node)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides IC-Light models specifically designed for inpainting tasks and can be easily integrated into ComfyUI, making it essential for this workflow.

### Metadata
**Author:** Fihade
**Repository:** [https://github.com/Fihade/IC-Light-ComfyUI-Node](https://github.com/Fihade/IC-Light-ComfyUI-Node)
**Install Type:** git-clone

---

### Image chooser

**Description:**

A custom node that pauses the flow while you choose which image (or latent) to pass on to the rest of the workflow.

- **Author:** chrisgoringe
- **Repository:** [https://github.com/chrisgoringe/cg-image-picker](https://github.com/chrisgoringe/cg-image-picker)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is highly relevant and useful for allowing users to choose an image or latent in the inpainting workflow.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-image-picker](https://github.com/chrisgoringe/cg-image-picker)
**Install Type:** git-clone

---

### Image Metadata Nodes

**Description:**

Nodes for loading and saving images with metadata in ComfyUI.

- **Author:** Light-x02
- **Repository:** [https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes](https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides metadata loading and saving capabilities which can be useful for storing information about the input images used in the inpainting workflow.

### Metadata
**Author:** Light-x02
**Repository:** [https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes](https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes)
**Install Type:** git-clone

---

### Image Processing Suite for ComfyUI

**Description:**

A collection of specialized image processing nodes for ComfyUI, focused on dataset preparation and pixel art manipulation.

- **Author:** marcoc2
- **Repository:** [https://github.com/marcoc2/ComfyUI-AnotherUtils](https://github.com/marcoc2/ComfyUI-AnotherUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this suite of image processing nodes is not directly related to inpainting with a mask, it may contain some utility functions that could support the workflow. However, its primary focus on dataset preparation and pixel art manipulation makes it only marginally relevant.

### Metadata
**Author:** marcoc2
**Repository:** [https://github.com/marcoc2/ComfyUI-AnotherUtils](https://github.com/marcoc2/ComfyUI-AnotherUtils)
**Install Type:** git-clone

---

### Image Resize for ComfyUI

**Description:**

This custom node provides various tools for resizing images. The goal is resizing without distorting proportions, yet without having to perform any calculations with the size of the original image. If a mask is present, it is resized and modified along with the image.

- **Author:** palant
- **Repository:** [https://github.com/palant/image-resize-comfyui](https://github.com/palant/image-resize-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides resizing functionality which can be useful for preparing input images for the inpainting workflow. It also supports resizing masks along with the image, making it a very useful tool for this specific goal.

### Metadata
**Author:** palant
**Repository:** [https://github.com/palant/image-resize-comfyui](https://github.com/palant/image-resize-comfyui)
**Install Type:** git-clone

---

### Image to Painting and Inspyrenet Assistant Nodes

**Description:**

These are ComfyUI nodes to assist in converting images to paintings and to assist the Inspyrenet Rembg node to totally remove, or replace with a color, the original background from images so that the background does not reappear in videos or in nodes that do not retain the alpha channel in rgba images.

- **Author:** Isi-dev
- **Repository:** [https://github.com/Isi-dev/ComfyUI-Img2PaintingAssistant](https://github.com/Isi-dev/ComfyUI-Img2PaintingAssistant)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it directly assists in converting images to paintings.

### Metadata
**Author:** Isi-dev
**Repository:** [https://github.com/Isi-dev/ComfyUI-Img2PaintingAssistant](https://github.com/Isi-dev/ComfyUI-Img2PaintingAssistant)
**Install Type:** git-clone

---

### image_control

**Description:**

Nodes:abyz22_Padding Image, abyz22_ImpactWildcardEncode, abyz22_setimageinfo, abyz22_SaveImage, abyz22_ImpactWildcardEncode_GetPrompt, abyz22_SetQueue, abyz22_drawmask, abyz22_FirstNonNull, abyz22_blendimages, abyz22_blend_onecolor. Please check workflow in [a/https://github.com/abyz22/image_control](https://github.com/abyz22/image_control)

- **Author:** abyz22
- **Repository:** [https://github.com/abyz22/image_control](https://github.com/abyz22/image_control)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node has multiple nodes that can be useful for the inpainting workflow with mask input, such as drawing masks and blending images.

### Metadata
**Author:** abyz22
**Repository:** [https://github.com/abyz22/image_control](https://github.com/abyz22/image_control)
**Install Type:** git-clone

---

### ImageProcessing

**Description:**

ComfyUI custom nodes to apply various image processing techniques.

- **Author:** bvhari
- **Repository:** [https://github.com/bvhari/ComfyUI_ImageProcessing](https://github.com/bvhari/ComfyUI_ImageProcessing)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides various image processing techniques that could be useful for pre-processing or post-processing the inpainted image.

### Metadata
**Author:** bvhari
**Repository:** [https://github.com/bvhari/ComfyUI_ImageProcessing](https://github.com/bvhari/ComfyUI_ImageProcessing)
**Install Type:** git-clone

---

### ImagesGrid

**Description:**

This tool provides a viewer node that allows for checking multiple outputs in a grid, similar to the X/Y Plot extension.

- **Author:** LEv145
- **Repository:** [https://github.com/LEv145/images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a viewer for multiple outputs but does not directly contribute to the inpainting process with a mask input.

### Metadata
**Author:** LEv145
**Repository:** [https://github.com/LEv145/images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
**Install Type:** git-clone

---

### Img2color - Extract Colors from Image

**Description:**

Extract the most common colors from an image, up to any number. Convert colors to plain English names using various color naming systems.

- **Author:** christian-byrne
- **Repository:** [https://github.com/christian-byrne/img2colors-comfyui-node](https://github.com/christian-byrne/img2colors-comfyui-node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node extracts colors from an image which can be useful for inpainting by providing color information that can help guide the inpainting process.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/img2colors-comfyui-node](https://github.com/christian-byrne/img2colors-comfyui-node)
**Install Type:** git-clone

---

### Info Utils

**Description:**

Nodes that facilitate simpler information providing and gathering, such as Text Box, Show Data and Token Counter nodes.

- **Author:** exectails
- **Repository:** [https://github.com/exectails/comfyui-et_infoutils](https://github.com/exectails/comfyui-et_infoutils)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a set of utility functions that can help with information gathering and display, which is essential for understanding the inpainting process and mask inputs.

### Metadata
**Author:** exectails
**Repository:** [https://github.com/exectails/comfyui-et_infoutils](https://github.com/exectails/comfyui-et_infoutils)
**Install Type:** git-clone

---

### InstanceDiffusion Nodes

**Description:**

A set of nodes to perform multi-object prompting with InstanceDiffusion

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-InstanceDiffusion](https://github.com/logtd/ComfyUI-InstanceDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node offers InstanceDiffusion nodes specifically designed for multi-object prompting, making it highly relevant to the inpainting workflow goal.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-InstanceDiffusion](https://github.com/logtd/ComfyUI-InstanceDiffusion)
**Install Type:** git-clone

---

### JH Misc. Nodes

**Description:**

NODES: Daisy-Chainable String Constant, Two-Way Switch, Three-Way Switch, Preview Imag
Miscellaneous custom nodes for ComfyUI

- **Author:** jefferyharrell
- **Repository:** [https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes](https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Node contains miscellaneous custom nodes that may have some utility in a broader context but are not directly relevant to the specified workflow goal.

### Metadata
**Author:** jefferyharrell
**Repository:** [https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes](https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes)
**Install Type:** git-clone

---

### Jovi_Measure

**Description:**

Image metrics nodes for ComfyUI

- **Author:** amorano
- **Repository:** [https://github.com/Amorano/Jovi_Measure](https://github.com/Amorano/Jovi_Measure)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides image metrics nodes that can help evaluate the quality of the inpainted result or provide feedback during the inpainting process.

### Metadata
**Author:** amorano
**Repository:** [https://github.com/Amorano/Jovi_Measure](https://github.com/Amorano/Jovi_Measure)
**Install Type:** git-clone

---

### Joy Caption Alpha Two for ComfyUI

**Description:**

The Joy Caption Alpha Two node for ComfyUI, based on https://huggingface.co/spaces/fancyfeast/joy-caption-alpha-two

- **Author:** tungdop2
- **Repository:** [https://github.com/tungdop2/Comfyui_joy-caption-alpha-two](https://github.com/tungdop2/Comfyui_joy-caption-alpha-two)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for text captioning and has the potential to be used in conjunction with inpainting workflows.

### Metadata
**Author:** tungdop2
**Repository:** [https://github.com/tungdop2/Comfyui_joy-caption-alpha-two](https://github.com/tungdop2/Comfyui_joy-caption-alpha-two)
**Install Type:** git-clone

---

### Jurdns Groq API Node

**Description:**

This node utilizes the Groq.com API to enhance prompts. (Place API key and main system prompt in the groq_config.json)

- **Author:** Jurdn
- **Repository:** [https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node](https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides access to the Groq.com API which can be used to enhance prompts for inpainting tasks.

### Metadata
**Author:** Jurdn
**Repository:** [https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node](https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node)
**Install Type:** git-clone

---

### Knodes

**Description:**

Nodes: Image(s) To Websocket (Base64), Load Image (Base64),Load Images (Base64)

- **Author:** kft334
- **Repository:** [https://github.com/kft334/Knodes](https://github.com/kft334/Knodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node includes nodes that can load images from base64 strings, which could be useful for loading mask inputs in an inpainting workflow.

### Metadata
**Author:** kft334
**Repository:** [https://github.com/kft334/Knodes](https://github.com/kft334/Knodes)
**Install Type:** git-clone

---

### LAizypainter-Exporter-ComfyUI

**Description:**

This exporter is a plugin for ComfyUI, which can export tasks for [a/LAizypainter](https://github.com/DimaChaichan/LAizypainter).
LAizypainter is a Photoshop plugin with which you can send tasks directly to a Stable Diffusion server. More information about a [a/Task](https://github.com/DimaChaichan/LAizypainter?tab=readme-ov-file#task)

- **Author:** DimaChaichan
- **Repository:** [https://github.com/DimaChaichan/LAizypainter-Exporter-ComfyUI](https://github.com/DimaChaichan/LAizypainter-Exporter-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node exports tasks for LAizypainter, a Photoshop plugin that can send tasks directly to a Stable Diffusion server, making it essential for this inpainting workflow with mask input.

### Metadata
**Author:** DimaChaichan
**Repository:** [https://github.com/DimaChaichan/LAizypainter-Exporter-ComfyUI](https://github.com/DimaChaichan/LAizypainter-Exporter-ComfyUI)
**Install Type:** git-clone

---

### Latent Mirror node for ComfyUI

**Description:**

Nodes: Latent Mirror. Node to mirror a latent along the Y (vertical / left to right) or X (horizontal / top to bottom) axis.

- **Author:** spro
- **Repository:** [https://github.com/spro/comfyui-mirror](https://github.com/spro/comfyui-mirror)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input because mirroring latents can help in generating more diverse and realistic results by creating symmetrical patterns or structures.

### Metadata
**Author:** spro
**Repository:** [https://github.com/spro/comfyui-mirror](https://github.com/spro/comfyui-mirror)
**Install Type:** git-clone

---

### Latent-Interposer

**Description:**

Custom node to convert the lantents between SDXL and SD v1.5 directly without the VAE decoding/encoding step.

- **Author:** city96
- **Repository:** [https://github.com/city96/SD-Latent-Interposer](https://github.com/city96/SD-Latent-Interposer)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is essential for the inpainting workflow with mask input because converting latents between SDXL and SD v1.5 formats can be a crucial step in integrating different models or workflows for more complex image editing tasks.

### Metadata
**Author:** city96
**Repository:** [https://github.com/city96/SD-Latent-Interposer](https://github.com/city96/SD-Latent-Interposer)
**Install Type:** git-clone

---

### Lazy Pony Prompter

**Description:**

A booru API powered prompt generator for A1111 and ComfyUI with flexible tag filtering system and customizable prompt templates.

- **Author:** Siberpone
- **Repository:** [https://github.com/Siberpone/lazy-pony-prompter](https://github.com/Siberpone/lazy-pony-prompter)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate prompts for inpainting tasks using flexible tag filtering and customizable templates.

### Metadata
**Author:** Siberpone
**Repository:** [https://github.com/Siberpone/lazy-pony-prompter](https://github.com/Siberpone/lazy-pony-prompter)
**Install Type:** git-clone

---

### LCM_Inpaint-Outpaint_Comfy

**Description:**

ComfyUI custom nodes for inpainting/outpainting using the new latent consistency model (LCM)

- **Author:** taabata
- **Repository:** [https://github.com/taabata/LCM_Inpaint_Outpaint_Comfy](https://github.com/taabata/LCM_Inpaint_Outpaint_Comfy)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides custom nodes specifically designed for inpainting/outpainting tasks with the latent consistency model (LCM).

### Metadata
**Author:** taabata
**Repository:** [https://github.com/taabata/LCM_Inpaint_Outpaint_Comfy](https://github.com/taabata/LCM_Inpaint_Outpaint_Comfy)
**Install Type:** git-clone

---

### LF Nodes

**Description:**

Custom nodes with a touch of extra UX, including: history for primitives, JSON manipulation, logic switches with visual feedback, LLM chat... and more!

- **Author:** lucafoscili
- **Repository:** [https://github.com/lucafoscili/comfyui-lf](https://github.com/lucafoscili/comfyui-lf)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node offers various features including history for primitives and logic switches which could be useful in an inpainting workflow.

### Metadata
**Author:** lucafoscili
**Repository:** [https://github.com/lucafoscili/comfyui-lf](https://github.com/lucafoscili/comfyui-lf)
**Install Type:** git-clone

---

### LiamUtil

**Description:**

Nodes: LiamLibLoadImage, LiamLibImageToGray, LiamLibSaveImg, LiamLibFillImage, PreviewReliefImage, GetBetterDepthImage, LiamLibSaveText

- **Author:** ai-liam
- **Repository:** [https://github.com/ai-liam/comfyui-liam](https://github.com/ai-liam/comfyui-liam)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides a set of image processing nodes that could support the inpainting workflow but may not directly address the goal.

### Metadata
**Author:** ai-liam
**Repository:** [https://github.com/ai-liam/comfyui-liam](https://github.com/ai-liam/comfyui-liam)
**Install Type:** git-clone

---

### LiamUtil (single node)

**Description:**

Nodes: LiamLoadImage. This node provides the capability to load images from a URL.

- **Author:** ai-liam
- **Repository:** [https://github.com/ai-liam/comfyui_liam_util](https://github.com/ai-liam/comfyui_liam_util)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows loading images from a URL which is a supporting task for an inpainting workflow with mask input.

### Metadata
**Author:** ai-liam
**Repository:** [https://github.com/ai-liam/comfyui_liam_util](https://github.com/ai-liam/comfyui_liam_util)
**Install Type:** git-clone

---

### Lists Cartesian Product

**Description:**

Given a set of lists, the node adjusts them so that when used as input to another node all the possible argument permutations are computed.

- **Author:** bmad4ever
- **Repository:** [https://github.com/bmad4ever/comfyui_lists_cartesian_product](https://github.com/bmad4ever/comfyui_lists_cartesian_product)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node computes all possible argument permutations from lists but does not have any direct relevance to the specified workflow goal of inpainting with a mask.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_lists_cartesian_product](https://github.com/bmad4ever/comfyui_lists_cartesian_product)
**Install Type:** git-clone

---

### Load Image From Base64 URI

**Description:**

Nodes: LoadImageFromBase64. Loads an image and its transparency mask from a base64-encoded data URI for easy API connection.

- **Author:** glowcone
- **Repository:** [https://github.com/glowcone/comfyui-base64-to-image](https://github.com/glowcone/comfyui-base64-to-image)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node loads an image and its transparency mask from a base64-encoded data URI, which can be useful for providing the necessary input for the inpainting workflow.

### Metadata
**Author:** glowcone
**Repository:** [https://github.com/glowcone/comfyui-base64-to-image](https://github.com/glowcone/comfyui-base64-to-image)
**Install Type:** git-clone

---

### Logo Generator Node for ComfyUI

**Description:**

This custom node allows you to generate logo images using Google Fonts.

- **Author:** cherninlab
- **Repository:** [https://github.com/cherninlab/logo-generator-comfyui](https://github.com/cherninlab/logo-generator-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can generate logo images using Google Fonts which could be useful for branding or adding text overlays in an inpainting workflow.

### Metadata
**Author:** cherninlab
**Repository:** [https://github.com/cherninlab/logo-generator-comfyui](https://github.com/cherninlab/logo-generator-comfyui)
**Install Type:** git-clone

---

### lollms_nodes_suite

**Description:**

lollms_nodes_suite is a set of nodes for comfyui that harnesses the power of lollms, a state-of-the-art AI text generation tool, to improve the quality of image generation.

- **Author:** ParisNeo
- **Repository:** [https://github.com/ParisNeo/lollms_nodes_suite](https://github.com/ParisNeo/lollms_nodes_suite)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node harnesses the power of lollms AI text generation tool but its relevance to image inpainting is unclear without more context.

### Metadata
**Author:** ParisNeo
**Repository:** [https://github.com/ParisNeo/lollms_nodes_suite](https://github.com/ParisNeo/lollms_nodes_suite)
**Install Type:** git-clone

---

### LoRA Power-Merger ComfyUI

**Description:**

An extension for merging LoRAs. Offers a wide range of LoRA merge techniques (including dare) and XY plots. XY plots require efficiency nodes.

- **Author:** larsupb
- **Repository:** [https://github.com/larsupb/LoRA-Merger-ComfyUI](https://github.com/larsupb/LoRA-Merger-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** This node offers a range of LoRA merge techniques which could be useful for combining different models in an inpainting workflow.

### Metadata
**Author:** larsupb
**Repository:** [https://github.com/larsupb/LoRA-Merger-ComfyUI](https://github.com/larsupb/LoRA-Merger-ComfyUI)
**Install Type:** git-clone

---

### MaskGCT-ComfyUI

**Description:**

a custom node for [a/MaskGCT](https://github.com/open-mmlab/Amphion/blob/main/models/tts/maskgct/README.md) to Zero-Shot Text-to-Speech

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/MaskGCT-ComfyUI](https://github.com/AIFSH/MaskGCT-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the inpainting workflow by providing a custom implementation of MaskGCT for Zero-Shot Text-to-Speech.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/MaskGCT-ComfyUI](https://github.com/AIFSH/MaskGCT-ComfyUI)
**Install Type:** git-clone

---

### MergeBlockWeighted_fo_ComfyUI

**Description:**

Nodes: MergeBlockWeighted

- **Author:** YinBailiang
- **Repository:** [https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI](https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has some marginally relevant features such as merging blocks, but none directly applicable to the inpainting workflow with mask input.

### Metadata
**Author:** YinBailiang
**Repository:** [https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI](https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI)
**Install Type:** git-clone

---

### mihaiiancu/Inpaint

**Description:**

Nodes: InpaintMediapipe. This node provides a simple interface to inpaint.

- **Author:** mihaiiancu
- **Repository:** [https://github.com/mihaiiancu/ComfyUI_Inpaint](https://github.com/mihaiiancu/ComfyUI_Inpaint)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for inpainting tasks and can be used as a key component in the workflow.

### Metadata
**Author:** mihaiiancu
**Repository:** [https://github.com/mihaiiancu/ComfyUI_Inpaint](https://github.com/mihaiiancu/ComfyUI_Inpaint)
**Install Type:** git-clone

---

### MilitantHitchhiker-SwitchbladePack

**Description:**

Militant Hitchhiker's Switchblade Pack is a collection of custom nodes for ComfyUI that provide various multi-function capabilities.

- **Author:** MilitantHitchhiker
- **Repository:** [https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack](https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this pack contains various nodes with different functionalities, none of them seem directly related to inpainting tasks.

### Metadata
**Author:** MilitantHitchhiker
**Repository:** [https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack](https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack)
**Install Type:** git-clone

---

### MLTask_ComfyUI

**Description:**

a set of nodes to help u run ai code using MLTask

- **Author:** mltask
- **Repository:** [https://github.com/misterjoessef/MLTask_ComfyUI](https://github.com/misterjoessef/MLTask_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** The MLTask_ComfyUI node is very useful for running AI code using MLTask and can likely be used as a supporting node in an inpainting workflow with mask input.

### Metadata
**Author:** mltask
**Repository:** [https://github.com/misterjoessef/MLTask_ComfyUI](https://github.com/misterjoessef/MLTask_ComfyUI)
**Install Type:** git-clone

---

### mm-comfyui-megamask

**Description:**

Nodes:ColorListMaskToImage, FlattenAndCombineMaskImages

- **Author:** meshmesh-io
- **Repository:** [https://github.com/meshmesh-io/mm-comfyui-megamask](https://github.com/meshmesh-io/mm-comfyui-megamask)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** The mm-comfyui-megamask node has specific features such as ColorListMaskToImage and FlattenAndCombineMaskImages that would be very useful in an inpainting workflow with mask input.

### Metadata
**Author:** meshmesh-io
**Repository:** [https://github.com/meshmesh-io/mm-comfyui-megamask](https://github.com/meshmesh-io/mm-comfyui-megamask)
**Install Type:** git-clone

---

### Model and Checkpoint Loaders for NF4 and FP4

**Description:**

Nodes for loading both Checkpoints and UNET/Diffussion models quantized to bitsandbytes NF4 or FP4 format.
Still under development and some limitations such as using LoRA might apply still.

- **Author:** silveroxides
- **Repository:** [https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders](https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Essential for loading checkpoints and models in NF4 or FP4 format, which is crucial for the specified workflow goal.

### Metadata
**Author:** silveroxides
**Repository:** [https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders](https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders)
**Install Type:** git-clone

---

### MTB Nodes

**Description:**

NODES: Face Swap, Film Interpolation, Latent Lerp, Int To Number, Bounding Box, Crop, Uncrop, ImageBlur, Denoise, ImageCompare, RGV to HSV, HSV to RGB, Color Correct, Modulo, Deglaze Image, Smart Step, ...

- **Author:** melMass
- **Repository:** [https://github.com/melMass/comfy_mtb](https://github.com/melMass/comfy_mtb)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Moderately useful as a collection of nodes that could potentially support the workflow goal, but none are directly related to inpainting or mask inputs.

### Metadata
**Author:** melMass
**Repository:** [https://github.com/melMass/comfy_mtb](https://github.com/melMass/comfy_mtb)
**Install Type:** git-clone

---

### net tool node for comfyui

**Description:**

A net tool node for comfyui, rewrite from [comfyui-tooling-nodes](https://github.com/Acly/comfyui-tooling-nodes) but support more big data sending.

- **Author:** LyazS
- **Repository:** [https://github.com/LyazS/comfyui-nettools](https://github.com/LyazS/comfyui-nettools)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node supports big data sending and rewriting of net tool nodes, but its direct relevance to the inpainting workflow is unclear.

### Metadata
**Author:** LyazS
**Repository:** [https://github.com/LyazS/comfyui-nettools](https://github.com/LyazS/comfyui-nettools)
**Install Type:** git-clone

---

### Node - Size Matcher

**Description:**

Match image/mask sizes

- **Author:** christian-byrne
- **Repository:** [https://github.com/christian-byrne/size-match-compositing-nodes](https://github.com/christian-byrne/size-match-compositing-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is essential for matching image/mask sizes which is a crucial step in the inpainting workflow.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/size-match-compositing-nodes](https://github.com/christian-byrne/size-match-compositing-nodes)
**Install Type:** git-clone

---

### noise latent perlinpinpin

**Description:**

Nodes: NoisyLatentPerlin. This allows to create latent spaces filled with perlin-based noise that can actually be used by the samplers.

- **Author:** Extraltodeus
- **Repository:** [https://github.com/Extraltodeus/noise_latent_perlinpinpin](https://github.com/Extraltodeus/noise_latent_perlinpinpin)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** NoisyLatentPerlin node can generate latent spaces with perlin-based noise, which could be useful for generating diverse inpainting results or creating realistic textures.

### Metadata
**Author:** Extraltodeus
**Repository:** [https://github.com/Extraltodeus/noise_latent_perlinpinpin](https://github.com/Extraltodeus/noise_latent_perlinpinpin)
**Install Type:** git-clone

---

### NX_HuggingFace_Flux

**Description:**

Nodes:Hugging Face Flux

- **Author:** Franck-Demongin
- **Repository:** [https://github.com/Franck-Demongin/NX_HuggingFace_Flux](https://github.com/Franck-Demongin/NX_HuggingFace_Flux)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides access to Hugging Face Flux which can be used in the inpainting workflow with mask input, especially when working with models from the Hugging Face model hub.

### Metadata
**Author:** Franck-Demongin
**Repository:** [https://github.com/Franck-Demongin/NX_HuggingFace_Flux](https://github.com/Franck-Demongin/NX_HuggingFace_Flux)
**Install Type:** git-clone

---

### ObjectFusion_ComfyUI_nodes

**Description:**

This is a node to generate new image that combine 2 objects from different scene.

- **Author:** ducido
- **Repository:** [https://github.com/ducido/ObjectFusion_ComfyUI_nodes](https://github.com/ducido/ObjectFusion_ComfyUI_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can combine objects from different scenes which could be useful for generating masks or combining inpainted regions.

### Metadata
**Author:** ducido
**Repository:** [https://github.com/ducido/ObjectFusion_ComfyUI_nodes](https://github.com/ducido/ObjectFusion_ComfyUI_nodes)
**Install Type:** git-clone

---

### Ollama and Llava Vision integration for ComfyUI

**Description:**

Ollama and Llava vision integration for ComfyUI

- **Author:** fairy-root
- **Repository:** [https://github.com/fairy-root/comfyui-ollama-llms](https://github.com/fairy-root/comfyui-ollama-llms)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node integrates Ollama and Llava vision but its direct relevance to inpainting with a mask input is unclear.

### Metadata
**Author:** fairy-root
**Repository:** [https://github.com/fairy-root/comfyui-ollama-llms](https://github.com/fairy-root/comfyui-ollama-llms)
**Install Type:** git-clone

---

### Ollama Prompt Encode

**Description:**

A prompt generator and CLIP encoder using AI provided by Ollama.

- **Author:** Michael Standen
- **Repository:** [https://github.com/ScreamingHawk/comfyui-ollama-prompt-encode](https://github.com/ScreamingHawk/comfyui-ollama-prompt-encode)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node generates prompts and encodes them using CLIP which could be useful for guiding the inpainting process with a mask input.

### Metadata
**Author:** Michael Standen
**Repository:** [https://github.com/ScreamingHawk/comfyui-ollama-prompt-encode](https://github.com/ScreamingHawk/comfyui-ollama-prompt-encode)
**Install Type:** git-clone

---

### OmniGen-ComfyUI

**Description:**

a custom node for [a/OmniGen](https://github.com/VectorSpaceLab/OmniGen)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/OmniGen-ComfyUI](https://github.com/AIFSH/OmniGen-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has some potential utility as a supporting node for the workflow, but its relevance to inpainting is unclear.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/OmniGen-ComfyUI](https://github.com/AIFSH/OmniGen-ComfyUI)
**Install Type:** git-clone

---

### OmniGen-ComfyUI

**Description:**

A custom node for [a/OmniGen](https://github.com/VectorSpaceLab/OmniGen).

- **Author:** hzane
- **Repository:** [https://github.com/hzane/OmniGen-ComfyUI](https://github.com/hzane/OmniGen-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node appears to be identical to Node 2 and has some potential utility as a supporting node for the workflow, but its relevance to inpainting is unclear.

### Metadata
**Author:** hzane
**Repository:** [https://github.com/hzane/OmniGen-ComfyUI](https://github.com/hzane/OmniGen-ComfyUI)
**Install Type:** git-clone

---
