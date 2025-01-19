# Filtered Nodes for: Generate an image from text and upscale it with a 2-pass highres fix

Total Available Nodes: 1865
Batch Size: 4
Estimated Processing Time: 38.9 minutes

## Results

### A8R8 ComfyUI Nodes

**Description:**

Nodes: Base64Image Input Node, Base64Image Output Node. [a/A8R8](https://github.com/ramyma/a8r8) supporting nodes to integrate with ComfyUI

- **Author:** ramyma
- **Repository:** [https://github.com/ramyma/A8R8_ComfyUI_nodes](https://github.com/ramyma/A8R8_ComfyUI_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** These nodes provide input and output functionality for base64 encoded images which can be useful for integrating with other ComfyUI nodes.

### Metadata
**Author:** ramyma
**Repository:** [https://github.com/ramyma/A8R8_ComfyUI_nodes](https://github.com/ramyma/A8R8_ComfyUI_nodes)
**Install Type:** git-clone

---

### add_text_2_img

**Description:**

Support adding custom text to the generated images.

- **Author:** fanfanfan
- **Repository:** [https://github.com/yuan199696/add_text_2_img](https://github.com/yuan199696/add_text_2_img)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node allows adding custom text to generated images, which can be useful but not essential for the specified workflow goal.

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

**Score:** 40/100

**Reason:** These nodes are marginally useful as they provide utility functions like passing images and latents, but their primary purpose seems to be for AegisFlow Shima rather than high-resolution image upscaling or generation from text.

### Metadata
**Author:** Aegis72
**Repository:** [https://github.com/aegis72/aegisflow_utility_nodes](https://github.com/aegis72/aegisflow_utility_nodes)
**Install Type:** git-clone

---

### AIFSH/ComfyUI-AuraSR

**Description:**

a node for [a/AuraSR](https://github.com/fal-ai/aura-sr)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-AuraSR](https://github.com/AIFSH/ComfyUI-AuraSR)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a direct implementation of AuraSR, which is necessary for generating an image from text.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-AuraSR](https://github.com/AIFSH/ComfyUI-AuraSR)
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

**Score:** 100/100

**Reason:** This node contains multiple nodes that can be used for tasks such as model loading, translation, and image processing, which are essential for achieving the workflow goal.

### Metadata
**Author:** purpen
**Repository:** [https://github.com/purpen/ComfyUI-AIRedoon](https://github.com/purpen/ComfyUI-AIRedoon)
**Install Type:** git-clone

---

### AlekPet/ComfyUI_Custom_Nodes_AlekPet

**Description:**

Nodes: PoseNode, PainterNode, TranslateTextNode, TranslateCLIPTextEncodeNode, DeepTranslatorTextNode, DeepTranslatorCLIPTextEncodeNode, ArgosTranslateTextNode, ArgosTranslateCLIPTextEncodeNode, PreviewTextNode, HexToHueNode, ColorsCorrectNode, IDENode.

- **Author:** AlekPet
- **Repository:** [https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node pack contains multiple nodes that could be useful for generating an image from text and upscaling it, including CLIP-based translation nodes.

### Metadata
**Author:** AlekPet
**Repository:** [https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet)
**Install Type:** git-clone

---

### Amazon Bedrock nodes for ComfyUI

**Description:**

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies. This repo is the ComfyUI nodes for Bedrock service. You could invoke the foundation model in your ComfyUI pipeline.

- **Author:** yytdfc
- **Repository:** [https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock](https://github.com/aws-samples/comfyui-llm-node-for-amazon-bedrock)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a direct integration with Amazon Bedrock, which can be used to generate images from text and upscale them.

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

**Score:** 80/100

**Reason:** AnimateDiff is relevant for image upscaling, but it may require additional setup and model downloads.

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

**Score:** 90/100

**Reason:** This node provides an improved version of AnimateDiff with more features and a wider range of motion models.

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

**Reason:** This node can segment anime characters, which could be useful in removing backgrounds before upscaling the image.

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

**Score:** 40/100

**Reason:** This nodepack contains various utility nodes for image handling, but none are specifically designed for the task of generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** antrobot
**Repository:** [https://github.com/antrobot1234/antrobots-comfyUI-nodepack](https://github.com/antrobot1234/antrobots-comfyUI-nodepack)
**Install Type:** git-clone

---

### Apply Style Model Adjust for ComfyUI

**Description:**

A custom node that provides enhanced control over style transfer balance when using FLUX style models in ComfyUI. This node offers better control over the influence of text prompts versus style reference images.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-Apply_Style_Model_Adjust](https://github.com/ShmuelRonen/ComfyUI-Apply_Style_Model_Adjust)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides enhanced control over style transfer balance, which can be useful for fine-tuning image generation with FLUX style models.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-Apply_Style_Model_Adjust](https://github.com/ShmuelRonen/ComfyUI-Apply_Style_Model_Adjust)
**Install Type:** git-clone

---

### Arc2Face ComfyUI Node Library

**Description:**

This ComfyUI node library builds upon the work done to train the [a/Arc2Face](https://github.com/foivospar/Arc2Face) model by foivospar. It provides a set of nodes for ComfyUI that allow users to extract face embeddings, generate images based on these embeddings, and perform image-to-image transformations.

- **Author:** caleboleary
- **Repository:** [https://github.com/caleboleary/ComfyUI-Arc2Face](https://github.com/caleboleary/ComfyUI-Arc2Face)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This library provides nodes for image generation based on face embeddings, which aligns perfectly with the workflow goal of generating an image from text and upscaling it.

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

**Score:** 100/100

**Reason:** This AsyncDiff node can upscale images with a highres fix, making it essential for the specified workflow goal.

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

**Score:** 40/100

**Reason:** This node may help with merging blocks in the workflow, but its relevance to generating an image from text or upscaling it is limited.

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

**Score:** 80/100

**Reason:** This node can remove backgrounds from multiple images which is a necessary step in preparing images for upscaling.

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

**Score:** 90/100

**Reason:** This node includes several useful nodes for post-processing and image manipulation that could support the workflow goal.

### Metadata
**Author:** justUmen
**Repository:** [https://github.com/justUmen/Bjornulf_custom_nodes](https://github.com/justUmen/Bjornulf_custom_nodes)
**Install Type:** git-clone

---

### BLIP Vision-Language Model Integration

**Description:**

A Python implementation for integrating the BLIP (Bootstrapping Language-Image Pre-training) model for visual question answering.

- **Author:** muhammederem
- **Repository:** [https://github.com/muhammederem/blip-comfyui](https://github.com/muhammederem/blip-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly integrates the BLIP model for visual question answering, which can generate images from text.

### Metadata
**Author:** muhammederem
**Repository:** [https://github.com/muhammederem/blip-comfyui](https://github.com/muhammederem/blip-comfyui)
**Install Type:** git-clone

---

### Bobs_Latent_Optimizer

**Description:**

This custom node for ComfyUI is designed to optimize latent generation for use with FLUX, SDXL and SD3. It provides flexible control over aspect ratios, megapixel sizes, and upscale factors, allowing users to dynamically create latents that fit specific tiling and resolution needs.

- **Author:** bobsblazed
- **Repository:** [https://github.com/BobsBlazed/Bobs_Latent_Optimizer](https://github.com/BobsBlazed/Bobs_Latent_Optimizer)
- **Install Type:** copy


### Applicability

**Score:** 98/100

**Reason:** Optimizes latent generation for upscale tasks and provides flexible control over aspect ratios, megapixel sizes, and upscale factors.

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

**Reason:** Contains nodes that may be useful for preprocessing or generating latents, but none directly contribute to the specified workflow goal.

### Metadata
**Author:** braintacles
**Repository:** [https://github.com/braintacles/braintacles-comfyui-nodes](https://github.com/braintacles/braintacles-comfyui-nodes)
**Install Type:** git-clone

---

### BRIA AI API nodes

**Description:**

Custom nodes for ComfyUI using BRIA's API.

- **Author:** BRIA AI
- **Repository:** [https://github.com/Bria-AI/ComfyUI-BRIA-API](https://github.com/Bria-AI/ComfyUI-BRIA-API)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to the workflow goal as it provides a BRIA AI API that can generate an image from text.

### Metadata
**Author:** BRIA AI
**Repository:** [https://github.com/Bria-AI/ComfyUI-BRIA-API](https://github.com/Bria-AI/ComfyUI-BRIA-API)
**Install Type:** git-clone

---

### BrushNet

**Description:**

These are custom nodes for ComfyUI native implementation of [a/BrushNet](https://arxiv.org/abs/2403.06976) (inpaint), PowerPaint (inpaint, object removal) and HiDiffusion (higher resolution for SD15 and SDXL)

- **Author:** nullquant
- **Repository:** [https://github.com/nullquant/ComfyUI-BrushNet](https://github.com/nullquant/ComfyUI-BrushNet)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for upscaling images with a 2-pass highres fix using BrushNet, which matches the specified workflow goal.

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

**Reason:** This node is directly relevant to the workflow goal as it contains all-in-one nodes for T2I, I2I, refining, and scaling, including high res fix math.

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

**Score:** 100/100

**Reason:** This node provides a full page image editor with mask support, directly relevant to generating and editing images.

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

**Reason:** This node provides a range of features that can be used in conjunction with other nodes to achieve the workflow goal.

### Metadata
**Author:** chaosaiart
**Repository:** [https://github.com/chaosaiart/Chaosaiart-Nodes](https://github.com/chaosaiart/Chaosaiart-Nodes)
**Install Type:** git-clone

---

### chris-comfyui-nodes

**Description:**

This repository contains a custom node for ComfyUI that pads an image to be square, filling the new pixels black.

- **Author:** chrissy0
- **Repository:** [https://github.com/chrissy0/chris-comfyui-nodes](https://github.com/chrissy0/chris-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports the workflow goal by padding an image to be square, which could help upscale it.

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

**Score:** 80/100

**Reason:** This node indirectly supports the workflow goal by providing a collection of nodes that can aid in generating and processing images.

### Metadata
**Author:** civitai
**Repository:** [https://github.com/civitai/civitai_comfy_nodes](https://github.com/civitai/civitai_comfy_nodes)
**Install Type:** git-clone

---

### CLIP Directional Prompt Attention

**Description:**

Nodes: CLIP Directional Prompt Attention Encode. Direction prompt attention tries to solve the problem of contextual words (or parts of the prompt) having an effect on much later or irrelevant parts of the prompt.

- **Author:** andersxa
- **Repository:** [https://github.com/andersxa/comfyui-PromptAttention](https://github.com/andersxa/comfyui-PromptAttention)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly addresses the issue of contextual words affecting later parts of the prompt, which could improve image generation quality.

### Metadata
**Author:** andersxa
**Repository:** [https://github.com/andersxa/comfyui-PromptAttention](https://github.com/andersxa/comfyui-PromptAttention)
**Install Type:** git-clone

---

### CLIP with BREAK syntax

**Description:**

Clip text encoder with BREAK formatting like A1111 (uses conditioning concat)

- **Author:** dfl
- **Repository:** [https://github.com/dfl/comfyui-clip-with-break](https://github.com/dfl/comfyui-clip-with-break)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a text encoder with BREAK formatting, which can be useful for generating images from text and might help in upscaling.

### Metadata
**Author:** dfl
**Repository:** [https://github.com/dfl/comfyui-clip-with-break](https://github.com/dfl/comfyui-clip-with-break)
**Install Type:** git-clone

---

### Clothing Migration Kit

**Description:**

This is an experimental project focused on Stable Diffusion (SD) models. In a single generated image, the same object or character consistently maintains a very high level of consistency. I had already attempted to address this issue in the SDXL model.

- **Author:** TTPlanetPig
- **Repository:** [https://github.com/TTPlanetPig/Comfyui_Object_Migration](https://github.com/TTPlanetPig/Comfyui_Object_Migration)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node can help maintain object consistency in generated images, but its primary focus is on Stable Diffusion models. It may still be useful for the specified workflow goal with some modifications.

### Metadata
**Author:** TTPlanetPig
**Repository:** [https://github.com/TTPlanetPig/Comfyui_Object_Migration](https://github.com/TTPlanetPig/Comfyui_Object_Migration)
**Install Type:** git-clone

---

### Comflowy's Custom Nodes

**Description:**

Custom nodes for ComfyUI by Comflowy.

- **Author:** Comflowy
- **Repository:** [https://github.com/6174/comflowy-nodes](https://github.com/6174/comflowy-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides custom nodes for ComfyUI, which can include functionality for generating images from text and upscaling them.

### Metadata
**Author:** Comflowy
**Repository:** [https://github.com/6174/comflowy-nodes](https://github.com/6174/comflowy-nodes)
**Install Type:** git-clone

---

### Comfy Controller

**Description:**

Quickly and easily build a GUI on top of your workflow. Gather just the nodes that you want to see, with no spaghetti, onto controller panels, leaving your workflow untouched in the background.

- **Author:** chrisgoringe
- **Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a GUI builder that can be used to organize nodes and streamline the workflow for generating an image from text and upsampling it.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
**Install Type:** git-clone

---

### comfy-easy-grids

**Description:**

A set of custom nodes for creating image grids, sequences, and batches in ComfyUI.

- **Author:** shockz0rz
- **Repository:** [https://github.com/shockz0rz/comfy-easy-grids](https://github.com/shockz0rz/comfy-easy-grids)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides functionality for creating image grids and sequences, which could be useful in post-processing steps after generating and upscaling the image.

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

**Score:** 90/100

**Reason:** This node has multiple nodes that can be used in conjunction with other nodes to generate an image from text and upscale it with a 2-pass highres fix.

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

**Score:** 100/100

**Reason:** This node directly integrates with Topaz Photo AI, which can upscale images as part of the workflow.

### Metadata
**Author:** choey
**Repository:** [https://github.com/choey/Comfy-Topaz](https://github.com/choey/Comfy-Topaz)
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

**Reason:** This node allows for the use of Matte Anything, a tool that can help with image masking and editing, which could be useful in preparing or post-processing images generated from text.

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

**Reason:** This node offers a collection of custom nodes that can be used for workflow efficiency and might include features helpful for upscaling images.

### Metadata
**Author:** picturesonpictures
**Repository:** [https://github.com/picturesonpictures/comfy_PoP](https://github.com/picturesonpictures/comfy_PoP)
**Install Type:** git-clone

---

### ComfyCanvas

**Description:**

Canvas to use with ComfyUI

- **Author:** taabata
- **Repository:** [https://github.com/taabata/ComfyCanvas](https://github.com/taabata/ComfyCanvas)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyCanvas is directly related to generating images from text, making it essential for this workflow.

### Metadata
**Author:** taabata
**Repository:** [https://github.com/taabata/ComfyCanvas](https://github.com/taabata/ComfyCanvas)
**Install Type:** git-clone

---

### comfygen

**Description:**

Setting Up a Web Interface Using ComfyUI.
NOTE:When installed, you can access it via http://127.0.0.1:8188/comfygen.

- **Author:** wei30172
- **Repository:** [https://github.com/wei30172/comfygen](https://github.com/wei30172/comfygen)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** comfygen provides a web interface for image generation and can upscale images with its built-in features, making it very useful for this workflow.

### Metadata
**Author:** wei30172
**Repository:** [https://github.com/wei30172/comfygen](https://github.com/wei30172/comfygen)
**Install Type:** git-clone

---

### ComfyI2I

**Description:**

A set of custom nodes to perform image 2 image functions in ComfyUI.

- **Author:** ManglerFTW
- **Repository:** [https://github.com/ManglerFTW/ComfyI2I](https://github.com/ManglerFTW/ComfyI2I)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyI2I has custom nodes for performing image-to-image functions, including upscaling, which makes it moderately to very useful for this specific task.

### Metadata
**Author:** ManglerFTW
**Repository:** [https://github.com/ManglerFTW/ComfyI2I](https://github.com/ManglerFTW/ComfyI2I)
**Install Type:** git-clone

---

### ComfyMath

**Description:**

Provides Math Nodes for ComfyUI. Boolean Logic, Integer Arithmetic, Floating Point Arithmetic and Functions, Vec2, Vec3, and Vec4 Arithmetic and Functions

- **Author:** evanspearman
- **Repository:** [https://github.com/evanspearman/ComfyMath](https://github.com/evanspearman/ComfyMath)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides mathematical operations necessary for high-resolution image upscaling and manipulation.

### Metadata
**Author:** evanspearman
**Repository:** [https://github.com/evanspearman/ComfyMath](https://github.com/evanspearman/ComfyMath)
**Install Type:** git-clone

---

### ComfyS3

**Description:**

ComfyS3 seamlessly integrates with [a/Amazon S3](https://aws.amazon.com/en/s3/) in ComfyUI. This open-source project provides custom nodes for effortless loading and saving of images, videos, and checkpoint models directly from S3 buckets within the ComfyUI graph interface.

- **Author:** TemryL
- **Repository:** [https://github.com/TemryL/ComfyS3](https://github.com/TemryL/ComfyS3)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyS3 provides seamless integration with Amazon S3 for loading and saving images, which is essential for upscaling high-resolution images from text.

### Metadata
**Author:** TemryL
**Repository:** [https://github.com/TemryL/ComfyS3](https://github.com/TemryL/ComfyS3)
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

**Reason:** This node directly supports generating images from text with its native DynamiCrafter functionality, making it essential for this workflow.

### Metadata
**Author:** ExponentialML
**Repository:** [https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter)
**Install Type:** git-clone

---

### ComfyUI A1111-like Prompt Custom Node Solution

**Description:**

Nodes: CLIPTextEncodeA1111, RerouteTextForCLIPTextEncodeA1111.

- **Author:** SadaleNet
- **Repository:** [https://github.com/SadaleNet/CLIPTextEncodeA1111-ComfyUI](https://github.com/SadaleNet/CLIPTextEncodeA1111-ComfyUI)
- **Install Type:** copy


### Applicability

**Score:** 90/100

**Reason:** This node customizes A1111-like prompts which can be useful for generating high-quality images from text.

### Metadata
**Author:** SadaleNet
**Repository:** [https://github.com/SadaleNet/CLIPTextEncodeA1111-ComfyUI](https://github.com/SadaleNet/CLIPTextEncodeA1111-ComfyUI)
**Install Type:** copy

---

### ComfyUI AnyNode: Any Node you ask for

**Description:**

Nodes: AnyNode. Nodes that can be anything you ask. Auto-Generate functional nodes using LLMs. Create impossible workflows. API Compatibility: (OpenAI, LocalLLMs, Gemini).

- **Author:** lks-ai
- **Repository:** [https://github.com/lks-ai/anynode](https://github.com/lks-ai/anynode)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is designed to auto-generate functional nodes based on user requests, making it highly relevant and useful for generating an image from text and upscaling with a 2-pass highres fix.

### Metadata
**Author:** lks-ai
**Repository:** [https://github.com/lks-ai/anynode](https://github.com/lks-ai/anynode)
**Install Type:** git-clone

---

### ComfyUI Bringing Old Photos Back to Life

**Description:**

Enhance old or low-quality images in ComfyUI. Optional features include automatic scratch removal and face enhancement. Based on Microsoft's Bringing-Old-Photos-Back-to-Life. Requires installing models, so see instructions here: https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life.

- **Author:** cdb-boop
- **Repository:** [https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life](https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node enhances old images which can be useful for upscaling low-quality images as part of the workflow goal.

### Metadata
**Author:** cdb-boop
**Repository:** [https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life](https://github.com/cdb-boop/ComfyUI-Bringing-Old-Photos-Back-to-Life)
**Install Type:** git-clone

---

### ComfyUI Checkpoint Loader Config

**Description:**

Provides a custom node to load config for sampler nodes from a yaml file.

- **Author:** Cyberschorsch
- **Repository:** [https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader](https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a way to load config for sampler nodes from a yaml file, which might be useful in certain situations but is not essential for this specific workflow goal.

### Metadata
**Author:** Cyberschorsch
**Repository:** [https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader](https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader)
**Install Type:** git-clone

---

### ComfyUI CogVideoX Wrapper

**Description:**

Diffusers wrapper for CogVideoX -models: [a/https://github.com/THUDM/CogVideo](https://github.com/THUDM/CogVideo)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-CogVideoXWrapper](https://github.com/kijai/ComfyUI-CogVideoXWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates images from text with high-resolution upscaling capabilities.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-CogVideoXWrapper](https://github.com/kijai/ComfyUI-CogVideoXWrapper)
**Install Type:** git-clone

---

### ComfyUI Coherent Video Sampler Node

**Description:**

A custom node for ComfyUI that enables coherent video generation while maintaining efficient memory usage, specifically optimized for heavy models like Flux.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler](https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Enables coherent video generation while maintaining efficient memory usage, suitable for heavy models like Flux.

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

**Score:** 80/100

**Reason:** This node allows for setting sigma values directly, which is essential for controlling denoising in the highres fix step of the workflow.

### Metadata
**Author:** BlakeOne
**Repository:** [https://github.com/BlakeOne/ComfyUI-CustomScheduler](https://github.com/BlakeOne/ComfyUI-CustomScheduler)
**Install Type:** git-clone

---

### ComfyUI Cutoff

**Description:**

These custom nodes provides features that allow for better control over the effects of the text prompt.

- **Author:** BlenderNeko
- **Repository:** [https://github.com/BlenderNeko/ComfyUI_Cutoff](https://github.com/BlenderNeko/ComfyUI_Cutoff)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides features for better control over text prompt effects but does not directly contribute to image generation or upscaling.

### Metadata
**Author:** BlenderNeko
**Repository:** [https://github.com/BlenderNeko/ComfyUI_Cutoff](https://github.com/BlenderNeko/ComfyUI_Cutoff)
**Install Type:** git-clone

---

### ComfyUI DDColor

**Description:**

Unofficial implementation of [a/DDColor](https://github.com/piddnad/DDColor) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_DDColor](https://github.com/hay86/ComfyUI_DDColor)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for generating an image from text as it directly implements a DDColor model.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_DDColor](https://github.com/hay86/ComfyUI_DDColor)
**Install Type:** git-clone

---

### ComfyUI Deepface

**Description:**

ComfyUI nodes wrapping the [a/deepface](https://github.com/serengil/deepface) library.

- **Author:** jordoh
- **Repository:** [https://github.com/jordoh/ComfyUI-Deepface](https://github.com/jordoh/ComfyUI-Deepface)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for generating an image from text using the Deepface library and can be used in conjunction with other nodes to upscale the image.

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

**Score:** 95/100

**Reason:** This node is very useful for generating an image from text as it implements a DenseDiffusion model which can be used to upscale the image.

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

**Score:** 100/100

**Reason:** This node directly implements Dreamtalk, a model that can generate images from text, making it essential for the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node allows loading models with image previews or directly downloading Civitai models via URL, making it essential for the specified workflow goal.

### Metadata
**Author:** X-T-E-R
**Repository:** [https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes](https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes)
**Install Type:** git-clone

---

### ComfyUI Essentials

**Description:**

Essential nodes that are weirdly missing from ComfyUI core. With few exceptions they are new features and not commodities. I hope this will be just a temporary repository until the nodes get included into ComfyUI.

- **Author:** cubiq
- **Repository:** [https://github.com/cubiq/ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI Essentials likely includes nodes necessary for image generation and upscaling, making it very useful for this workflow.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
**Install Type:** git-clone

---

### ComfyUI ExLlamaV2 Nodes

**Description:**

A simple local text generator for ComfyUI utilizing [a/ExLlamaV2](https://github.com/turboderp/exllamav2).
[w/NOTE:Manual package installation is required.]

- **Author:** Zuellni
- **Repository:** [https://github.com/Zuellni/ComfyUI-ExLlama-Nodes](https://github.com/Zuellni/ComfyUI-ExLlama-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ExLlamaV2 Nodes is a direct contributor to generating text from input, which is essential for the specified workflow goal.

### Metadata
**Author:** Zuellni
**Repository:** [https://github.com/Zuellni/ComfyUI-ExLlama-Nodes](https://github.com/Zuellni/ComfyUI-ExLlama-Nodes)
**Install Type:** git-clone

---

### ComfyUI fabric

**Description:**

ComfyUI nodes based on the paper [a/FABRIC: Personalizing Diffusion Models with Iterative Feedback](https://arxiv.org/abs/2307.10159) (Feedback via Attention-Based Reference Image Conditioning)

- **Author:** ssitu
- **Repository:** [https://github.com/ssitu/ComfyUI_fabric](https://github.com/ssitu/ComfyUI_fabric)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is based on a paper that focuses on personalizing diffusion models with iterative feedback, which aligns well with the goal of refining generated images.

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

**Score:** 80/100

**Reason:** This node provides access to a high-resolution image API that can be used for generating and upsampling images.

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

**Score:** 90/100

**Reason:** This node accelerates the Flux.1 image generation process, which is directly relevant to the workflow goal.

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

**Score:** 80/100

**Reason:** The Flux Trainer can be used to fine-tune models for image generation and upscaling tasks, making it very useful for this workflow goal.

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

**Score:** 40/100

**Reason:** InstructIR is focused on image restoration, which may be tangentially related to upscaling tasks, but it"s not a direct fit for this workflow goal.

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

**Score:** 100/100

**Reason:** This node directly creates a sequence of frames by moving and scaling a subject image over a background image, which can be used as input for the workflow goal.

### Metadata
**Author:** diSty
**Repository:** [https://github.com/diStyApps/ComfyUI_FrameMaker](https://github.com/diStyApps/ComfyUI_FrameMaker)
**Install Type:** git-clone

---

### ComfyUI Griptape Nodes

**Description:**

This repo creates a series of nodes that enable you to utilize the [a/Griptape Python Framework](https://github.com/griptape-ai/griptape/) with ComfyUI, integrating AI into your workflow. This repo creates a series of nodes that enable you to utilize the Griptape Python Framework with ComfyUI, integrating AI into your workflow.

- **Author:** griptape-ai
- **Repository:** [https://github.com/griptape-ai/ComfyUI-Griptape](https://github.com/griptape-ai/ComfyUI-Griptape)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly integrates AI into the workflow with Griptape Python Framework.

### Metadata
**Author:** griptape-ai
**Repository:** [https://github.com/griptape-ai/ComfyUI-Griptape](https://github.com/griptape-ai/ComfyUI-Griptape)
**Install Type:** git-clone

---

### ComfyUI Hallo

**Description:**

Unofficial implementation of [a/hallo](https://github.com/fudan-generative-vision/hallo) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_Hallo](https://github.com/hay86/ComfyUI_Hallo)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Unofficial implementation of hallo for ComfyUI, but may require additional setup.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_Hallo](https://github.com/hay86/ComfyUI_Hallo)
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

**Score:** 91/100

**Reason:** Custom nodes pack provided by HiFORCE for image enhancement, including upscaling and sampler features.

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

**Score:** 80/100

**Reason:** This node pack offers various nodes that can enhance facial details and provide iterative upscaling, making it very useful for achieving the specified workflow goal.

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

**Score:** 90/100

**Reason:** This node provides a crucial component of the Impact Pack, which is essential for using the UltralyticsDetectorProvider to enhance facial details in the workflow.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
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

**Score:** 80/100

**Reason:** This node is very useful because it allows usage of LCM Lora which can produce good results in only a few generation steps, directly contributing to the main goal of generating an image from text and upsampling it.

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

**Score:** 80/100

**Reason:** This node provides iterative mixing nodes that can be used for image vision tasks such as object detection and captioning, which could support the workflow goal of generating an image from text.

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

**Score:** 80/100

**Reason:** This node can be used to improve image quality by synchronizing latent spaces, which would help upscale the generated image.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_LatentSync](https://github.com/hay86/ComfyUI_LatentSync)
**Install Type:** git-clone

---

### ComfyUI Layer Style

**Description:**

A set of nodes for ComfyUI it generate image like Adobe Photoshop's Layer Style. the Drop Shadow is first completed node, and follow-up work is in progress.

- **Author:** chflame163
- **Repository:** [https://github.com/chflame163/ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node could potentially be used for styling the generated image, its primary function is not directly related to upscaling or generating images from text.

### Metadata
**Author:** chflame163
**Repository:** [https://github.com/chflame163/ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle)
**Install Type:** git-clone

---

### ComfyUI LLaVA Captioner

**Description:**

A ComfyUI extension for chatting with your images. Runs on your own system, no external services used, no filter. Uses the [a/LLaVA multimodal LLM](https://llava-vl.github.io/) so you can give instructions or ask questions in natural language. It's maybe as smart as GPT3.5, and it can see.

- **Author:** ceruleandeep
- **Repository:** [https://github.com/ceruleandeep/ComfyUI-LLaVA-Captioner](https://github.com/ceruleandeep/ComfyUI-LLaVA-Captioner)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node can generate captions for images using natural language instructions, which could be used as input for the image generation process.

### Metadata
**Author:** ceruleandeep
**Repository:** [https://github.com/ceruleandeep/ComfyUI-LLaVA-Captioner](https://github.com/ceruleandeep/ComfyUI-LLaVA-Captioner)
**Install Type:** git-clone

---

### ComfyUI Mask Contour Processor

**Description:**

A ComfyUI node that improves inpainting results by extending mask boundaries with geometric patterns, helping create smoother transitions and better context for AI-driven image completion.

- **Author:** codeprimate
- **Repository:** [https://github.com/codeprimate/ComfyUI-MaskContourProcessor](https://github.com/codeprimate/ComfyUI-MaskContourProcessor)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node improves inpainting results by extending mask boundaries with geometric patterns, which could be useful for post-processing images generated by the workflow.

### Metadata
**Author:** codeprimate
**Repository:** [https://github.com/codeprimate/ComfyUI-MaskContourProcessor](https://github.com/codeprimate/ComfyUI-MaskContourProcessor)
**Install Type:** git-clone

---

### ComfyUI MiniCPM-V

**Description:**

Unofficial implementation of [a/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) for ComfyUI

- **Author:** hay86
- **Repository:** [https://github.com/hay86/ComfyUI_MiniCPM-V](https://github.com/hay86/ComfyUI_MiniCPM-V)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a model-based image generation tool that directly matches the workflow goal.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_MiniCPM-V](https://github.com/hay86/ComfyUI_MiniCPM-V)
**Install Type:** git-clone

---

### ComfyUI Model Downloader

**Description:**

This node allows downloading models directly within ComfyUI for easier use and integration.

- **Author:** ciri
- **Repository:** [https://github.com/ciri/comfyui-model-downloader](https://github.com/ciri/comfyui-model-downloader)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This model downloader can facilitate the use of necessary models for the image generation task, making it very useful for this workflow.

### Metadata
**Author:** ciri
**Repository:** [https://github.com/ciri/comfyui-model-downloader](https://github.com/ciri/comfyui-model-downloader)
**Install Type:** git-clone

---

### ComfyUI Multi-Workspace

**Description:**

A simple, quick, and dirty implementation of multiple workspaces within ComfyUI.

- **Author:** prozacgod
- **Repository:** [https://github.com/prozacgod/comfyui-pzc-multiworkspace](https://github.com/prozacgod/comfyui-pzc-multiworkspace)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node can provide multiple workspaces which could be useful for organizing tasks related to image generation and upscaling.

### Metadata
**Author:** prozacgod
**Repository:** [https://github.com/prozacgod/comfyui-pzc-multiworkspace](https://github.com/prozacgod/comfyui-pzc-multiworkspace)
**Install Type:** git-clone

---

### ComfyUI MuseV Evolved

**Description:**

Nodes:MuseVImg2Vid (comfyui_musev_evolved)
NOTE: Download [a/MuseV](https://huggingface.co/TMElyralab/MuseV) to ComfyUI/models/diffusers

- **Author:** storyicon
- **Repository:** [https://github.com/storyicon/comfyui_musev_evolved](https://github.com/storyicon/comfyui_musev_evolved)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly generates an image from text using MuseV, making it highly relevant to the workflow goal.

### Metadata
**Author:** storyicon
**Repository:** [https://github.com/storyicon/comfyui_musev_evolved](https://github.com/storyicon/comfyui_musev_evolved)
**Install Type:** git-clone

---

### ComfyUI Neural Network Latent Upscale

**Description:**

Nodes:NNLatentUpscale, A custom ComfyUI node designed for rapid latent upscaling using a compact neural network, eliminating the need for VAE-based decoding and encoding.

- **Author:** Ttl
- **Repository:** [https://github.com/Ttl/ComfyUi_NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Directly relevant to upscaling images, matching the workflow goal.

### Metadata
**Author:** Ttl
**Repository:** [https://github.com/Ttl/ComfyUi_NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
**Install Type:** git-clone

---

### ComfyUI Neural Network Toolkit NNT

**Description:**

Neural Network Toolkit (NNT) for ComfyUI is an extensive set of custom ComfyUI nodes for designing, training, and fine-tuning neural networks. This toolkit allows defining models, layers, training workflows, transformers, and tensor operations in a visual manner using nodes.

- **Author:** inventorado
- **Repository:** [https://github.com/inventorado/ComfyUI_NNT](https://github.com/inventorado/ComfyUI_NNT)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Extensive toolkit with nodes for designing and training neural networks, including those used in image upscaling, making it essential for this workflow.

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

**Score:** 40/100

**Reason:** This node can be useful as a supporting node by resetting nodes to their default values if the workflow fails or needs to be restarted.

### Metadata
**Author:** BlakeOne
**Repository:** [https://github.com/BlakeOne/ComfyUI-NodeReset](https://github.com/BlakeOne/ComfyUI-NodeReset)
**Install Type:** git-clone

---

### ComfyUI nodes for ControlNext-SVD v2

**Description:**

These nodes include my wrapper for the original diffusers pipeline, as well as work in progress native ComfyUI implementation.
For the diffusers wrapper models should be downloaded automatically, for the native version you can get the unet [a/here](https://huggingface.co/Kijai/ControlNeXt-SVD-V2-Comfy/blob/main/controlnext-svd_v2-unet-fp16_converted.safetensors).

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-ControlNeXt-SVD](https://github.com/kijai/ComfyUI-ControlNeXt-SVD)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** These nodes provide a high-quality image generation pipeline that matches the specified workflow goal, making them very useful for achieving this task.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-ControlNeXt-SVD](https://github.com/kijai/ComfyUI-ControlNeXt-SVD)
**Install Type:** git-clone

---

### ComfyUI nodes to use CrossImageAttention

**Description:**

ComfyUI for [a/CrossImageAttention](https://github.com/garibida/cross-image-attention)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_CrossImageAttention](https://github.com/leeguandong/ComfyUI_CrossImageAttention)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly relevant to generating an image from text with upscaling.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_CrossImageAttention](https://github.com/leeguandong/ComfyUI_CrossImageAttention)
**Install Type:** git-clone

---

### ComfyUI nodes to use Style-Aligned

**Description:**

ComfyUI for [a/style-aligned](https://github.com/google/style-aligned)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_Style_Aligned](https://github.com/leeguandong/ComfyUI_Style_Aligned)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Style-Aligned is a node that can generate images from text but may not directly support the 2-pass highres fix for upscaling.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_Style_Aligned](https://github.com/leeguandong/ComfyUI_Style_Aligned)
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

**Reason:** This node can integrate LLMs into ComfyUI workflows, which could be useful for generating images from text. However, its primary purpose is interacting with Ollama, so it"s not a direct solution to the workflow goal but has significant utility as a supporting node.

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

**Score:** 81/100

**Reason:** This node is a direct implementation of OpenVoice, which can be used for generating images from text, making it very useful for this workflow goal.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_OpenVoice](https://github.com/hay86/ComfyUI_OpenVoice)
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

**Reason:** This node directly supports generating an image from text and upscaling it using PhotoMaker V2, making it very useful for the specified workflow goal.

### Metadata
**Author:** shiimizu
**Repository:** [https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus](https://github.com/shiimizu/ComfyUI-PhotoMaker-Plus)
**Install Type:** git-clone

---

### ComfyUI Pixtral Large Extension

**Description:**

A ComfyUI custom node that integrates Mistral AI's Pixtral Large vision model, enabling powerful multimodal AI capabilities within ComfyUI. Pixtral Large is a 124B parameter model (123B decoder + 1B visual encoder)

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_large](https://github.com/ShmuelRonen/ComfyUI_pixtral_large)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it integrates a powerful multimodal AI model (Pixtral Large) that can be used for generating high-quality images and potentially upscaling them with advanced capabilities.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_large](https://github.com/ShmuelRonen/ComfyUI_pixtral_large)
**Install Type:** git-clone

---

### ComfyUI Pollinations

**Description:**

Generate images from text prompts using Pollinations' AI models for free.

- **Author:** ciga2011
- **Repository:** [https://github.com/ciga2011/ComfyUI-Pollinations](https://github.com/ciga2011/ComfyUI-Pollinations)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates images from text using Pollinations" AI models, which matches the workflow goal exactly.

### Metadata
**Author:** ciga2011
**Repository:** [https://github.com/ciga2011/ComfyUI-Pollinations](https://github.com/ciga2011/ComfyUI-Pollinations)
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

**Reason:** This node allows for dynamic loading and application of LoRA or HN models based on the input prompt, making it very useful for workflows that involve changing models during execution.

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

**Reason:** This node is a custom implementation of ProPainter framework which can generate an image from text and upscale it with highres fix.

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

**Score:** 100/100

**Reason:** This node provides a wrapper for PyramidFlow models that can be used to generate images from text and upscale them.

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

**Score:** 100/100

**Reason:** This node is a texture generation technique that can be used to upscale images and fill in missing details.

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

**Score:** 100/100

**Reason:** This node provides a TensorRT implementation of RIFE for ultra-fast frame interpolation, which can be used as part of the workflow goal.

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

**Score:** 100/100

**Reason:** This node is specifically designed for segmenting images and can be adapted to generate an image from text with highres fix functionality.

### Metadata
**Author:** neverbiasu
**Repository:** [https://github.com/neverbiasu/ComfyUI-SAM2](https://github.com/neverbiasu/ComfyUI-SAM2)
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

**Reason:** This node is designed for segmenting images, which could be useful in preparing the input image or separating objects within the generated image.

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

**Score:** 80/100

**Reason:** This node is an unofficial implementation of a segmentation model that can be used to separate objects or refine the output of other models.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE)
**Install Type:** git-clone

---

### ComfyUI SKBundle

**Description:**

Nodes: MultiText, TextBox, TitlePlus, SeamlessTexture, AspectRatioPlus, DisplayEverything, ComparerPlus, AnySwitch, Node Design Tools...

- **Author:** SKBv0
- **Repository:** [https://github.com/SKBv0/ComfyUI_SKBundle](https://github.com/SKBv0/ComfyUI_SKBundle)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node bundle includes several nodes that could support the workflow goal, such as SeamlessTexture and AspectRatioPlus, but their direct relevance is moderate.

### Metadata
**Author:** SKBv0
**Repository:** [https://github.com/SKBv0/ComfyUI_SKBundle](https://github.com/SKBv0/ComfyUI_SKBundle)
**Install Type:** git-clone

---

### ComfyUI StabilityAI Suite

**Description:**

This fork of the official StabilityAI repository contains a number of enhancements and implementations.

- **Author:** florestefano1975
- **Repository:** [https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite](https://github.com/florestefano1975/ComfyUI-StabilityAI-Suite)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a direct implementation of Stable Diffusion, which can generate high-resolution images from text inputs.

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

**Score:** 100/100

**Reason:** This node provides access to Stable Video Diffusion, a model that can upscale video frames and generate high-resolution images from text inputs.

### Metadata
**Author:** thecooltechguy
**Repository:** [https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion)
**Install Type:** git-clone

---

### ComfyUI Suno API

**Description:**

An unofficial Python library for [a/Suno AI](https://www.suno.ai/) API

- **Author:** GentlemanHu
- **Repository:** [https://github.com/GentlemanHu/ComfyUI-SunoAI](https://github.com/GentlemanHu/ComfyUI-SunoAI)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides access to a Suno AI API which can be used for generating images from text, making it very useful for the specified workflow goal.

### Metadata
**Author:** GentlemanHu
**Repository:** [https://github.com/GentlemanHu/ComfyUI-SunoAI](https://github.com/GentlemanHu/ComfyUI-SunoAI)
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

**Reason:** Although not directly related to image generation or upscaling, this template matching node could potentially be used as a supporting tool in the workflow by providing a way to match templates and possibly upscale them.

### Metadata
**Author:** wentao-uw
**Repository:** [https://github.com/wentao-uw/ComfyUI-template-matching](https://github.com/wentao-uw/ComfyUI-template-matching)
**Install Type:** git-clone

---

### ComfyUI Universal Styler

**Description:**

A research Node based project on Artificial Intelligence using ComfyUI visual editor with Stable diffusion Local processing focus in mind. This custom node is intended to serve the purpose to offer a large palette of prompting scenrarios, based on Public Checkpoint Models OR/AND Private custom Models and LoRas. It includes an integrated learning machine process as well as a set of workflows.

- **Author:** KoreTeknology
- **Repository:** [https://github.com/KoreTeknology/ComfyUI-Universal-Styler](https://github.com/KoreTeknology/ComfyUI-Universal-Styler)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node offers a wide range of prompting scenarios and can be used for generating images from text, making it very useful for the specified workflow goal.

### Metadata
**Author:** KoreTeknology
**Repository:** [https://github.com/KoreTeknology/ComfyUI-Universal-Styler](https://github.com/KoreTeknology/ComfyUI-Universal-Styler)
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

**Reason:** This node provides fast image upscaling capabilities using TensorRT, which is directly relevant to the workflow goal of upscaling an image with a 2-pass highres fix.

### Metadata
**Author:** yuvraj108c
**Repository:** [https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt)
**Install Type:** git-clone

---

### ComfyUI UX Nodes

**Description:**

Nodes: Easy Resolution Picker, Save Diffusion Model, Load Checkpoint BNB On the fly, Load UNET BNB On the fly

- **Author:** Anibaaal
- **Repository:** [https://github.com/Anibaaal/ComfyUI-UX-Nodes](https://github.com/Anibaaal/ComfyUI-UX-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides all necessary components to generate an image from text and upscale it with a 2-pass highres fix.

### Metadata
**Author:** Anibaaal
**Repository:** [https://github.com/Anibaaal/ComfyUI-UX-Nodes](https://github.com/Anibaaal/ComfyUI-UX-Nodes)
**Install Type:** git-clone

---

### ComfyUI VIDU

**Description:**

This is a ComfyUI node package that integrates with VIDU API, supporting features such as text-to-video, image-to-video, character-to-video generation, and video super-resolution.

- **Author:** 1zhangyy1
- **Repository:** [https://github.com/1zhangyy1/comfyui-vidu-nodes](https://github.com/1zhangyy1/comfyui-vidu-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides text-to-video, image-to-video, character-to-video generation, and video super-resolution features which align with the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node provides a real-time AI-generated interactive art framework that can be used for image generation and upscaling.

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

**Score:** 81/100

**Reason:** This node captures webcam images which could be used as input for the image generation process.

### Metadata
**Author:** victorchall
**Repository:** [https://github.com/victorchall/comfyui_webcamcapture](https://github.com/victorchall/comfyui_webcamcapture)
**Install Type:** git-clone

---

### ComfyUI Yolov8

**Description:**

Nodes: Yolov8Detection, Yolov8Segmentation. Deadly simple yolov8 comfyui plugin

- **Author:** zcfrank1st
- **Repository:** [https://github.com/zcfrank1st/Comfyui-Yolov8](https://github.com/zcfrank1st/Comfyui-Yolov8)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for the workflow goal as it provides a yolov8 detection and segmentation functionality that can be used to generate an image from text.

### Metadata
**Author:** zcfrank1st
**Repository:** [https://github.com/zcfrank1st/Comfyui-Yolov8](https://github.com/zcfrank1st/Comfyui-Yolov8)
**Install Type:** git-clone

---

### ComfyUI YoloWorld-EfficientSAM

**Description:**

Unofficial implementation of [a/YOLO-World + EfficientSAM](https://huggingface.co/spaces/SkalskiP/YOLO-World) & [a/YOLO-World](https://github.com/AILab-CVC/YOLO-World) for ComfyUI
NOTE: Install the efficient_sam model from the Install models menu.
[w/When installing or updating this custom node, many installation packages may be downgraded due to the installation of requirements.
!! python3.12 is incompatible.]

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for the workflow goal as it provides a yoloworld model with efficient SAM, but requires additional installation steps.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM)
**Install Type:** git-clone

---

### ComfyUI's ControlNet Auxiliary Preprocessors

**Description:**

Plug-and-play ComfyUI node sets for making ControlNet hint images.

- **Author:** Fannovel16
- **Repository:** [https://github.com/Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to generating ControlNet hint images which can be used as input for upscaling an image.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
**Install Type:** git-clone

---

### comfyui's gaffer(ComfyUI native implementation of IC-Light. )

**Description:**

Nodes:Load ICLight Model,Apply ICLight,Simple Light Source,Calculate Normal Map

- **Author:** ray
- **Repository:** [https://github.com/huagetai/ComfyUI-Gaffer](https://github.com/huagetai/ComfyUI-Gaffer)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not directly related, this node provides a way to apply lighting effects which could be useful in conjunction with other nodes for the specified workflow goal.

### Metadata
**Author:** ray
**Repository:** [https://github.com/huagetai/ComfyUI-Gaffer](https://github.com/huagetai/ComfyUI-Gaffer)
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

**Reason:** This node suite can process 3D inputs using cutting-edge algorithms and models, making it very useful for the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node is highly relevant to generating an image from text and upscaling it with a 2-pass highres fix, as it includes features like dolly zoom and swing motion video rendering.

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

**Score:** 81/100

**Reason:** This node allows scheduling ControlNet strength and applying custom weights and attention masks, which are essential for fine-tuning the generated image and preparing it for upscaling.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
**Install Type:** git-clone

---

### ComfyUI-AharaNodes

**Description:**

NODES:Frame Segmenter, Get Frame at Index, Repeat Sampler Config, Patch Repeat Sampler Config (Model), Patch Repeat Sampler Config (Latent), KSampler (Simple Input)

- **Author:** chris-arsenault
- **Repository:** [https://github.com/chris-arsenault/ComfyUI-AharaNodes](https://github.com/chris-arsenault/ComfyUI-AharaNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** The Frame Segmenter is essential for breaking down text into frames which can be used to generate an image.

### Metadata
**Author:** chris-arsenault
**Repository:** [https://github.com/chris-arsenault/ComfyUI-AharaNodes](https://github.com/chris-arsenault/ComfyUI-AharaNodes)
**Install Type:** git-clone

---

### ComfyUI-Allegro

**Description:**

ComfyUI supports over [a/rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro), which uses text prompt to generate short video in relatively high quality, especially comparing to other open source solutions available for now.

- **Author:** bombax-xiaoice
- **Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Allegro](https://github.com/bombax-xiaoice/ComfyUI-Allegro)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node supports generating images from text and can upscale them, aligning perfectly with the specified workflow goal.

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

**Score:** 81/100

**Reason:** This node integrates functionality specifically designed for generating images from text and can be used as a direct solution for the workflow goal.

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

**Reason:** Although this node contains animation-related nodes and workflows, it may not directly contribute to generating images from text or upscaling, but could be useful as a supporting tool for more complex animations.

### Metadata
**Author:** Isi-dev
**Repository:** [https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows](https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows)
**Install Type:** git-clone

---

### ComfyUI-AniPortrait

**Description:**

ComfyUI [a/AniPortrait](https://github.com/Zejun-Yang/AniPortrait)

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-AniPortrait](https://github.com/chaojie/ComfyUI-AniPortrait)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly related to generating an image from text with highres fix.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-AniPortrait](https://github.com/chaojie/ComfyUI-AniPortrait)
**Install Type:** git-clone

---

### ComfyUI-APGScaling

**Description:**

ComfyUI nodes to use [a/APG scaling](https://huggingface.co/papers/2410.02416) for CFG, allowing for better image quality with higher CFG.

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-APGScaling](https://github.com/logtd/ComfyUI-APGScaling)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Provides APG scaling for better image quality with higher CFG, which is essential for the specified workflow goal.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-APGScaling](https://github.com/logtd/ComfyUI-APGScaling)
**Install Type:** git-clone

---

### ComfyUI-APISR

**Description:**

Node to use [a/APISR](https://github.com/Kiteretsu77/APISR) upscale models in ComfyUI.[w/NOTE: repo name is changed from ComfyUI-APISR -> ComfyUI-APISR-KJ]

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-APISR-KJ](https://github.com/kijai/ComfyUI-APISR-KJ)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** Offers upscale models in ComfyUI but requires additional setup and configuration to achieve the desired highres fix.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-APISR-KJ](https://github.com/kijai/ComfyUI-APISR-KJ)
**Install Type:** git-clone

---

### comfyui-art-venture

**Description:**

A comprehensive set of custom nodes for ComfyUI, focusing on utilities for image processing, JSON manipulation, model operations and working with object via URLs

- **Author:** sipherxyz
- **Repository:** [https://github.com/sipherxyz/comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This comprehensive set of custom nodes includes utilities for image processing, making it highly relevant to the workflow goal.

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

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it enables smooth animations for image generation, which can be used to create dynamic sequences and upscale images with a 2-pass highres fix.

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

**Score:** 100/100

**Reason:** This node is essential for this workflow as it provides a direct pipeline for image generation and upscaling with a 2-pass highres fix.

### Metadata
**Author:** sanbuphy
**Repository:** [https://github.com/sanbuphy/ComfyUI-AudioLDM](https://github.com/sanbuphy/ComfyUI-AudioLDM)
**Install Type:** git-clone

---

### ComfyUI-AutoColorGimp

**Description:**

Shamelessly copied the code to auto color correct the image like in gimp from this answer: [a/https://stackoverflow.com/a/56365560/4561887](https://stackoverflow.com/a/56365560/4561887)

- **Author:** A4P7J1N7M05OT
- **Repository:** [https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp](https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node auto-color corrects images but does not upscale them and is not specifically designed for text-to-image generation.

### Metadata
**Author:** A4P7J1N7M05OT
**Repository:** [https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp](https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp)
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

**Reason:** This node detects faces and can be used to automatically crop the generated image, which could be useful in certain workflows.

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

**Score:** 90/100

**Reason:** This node can help with image quality improvement by adjusting CFG settings, which is essential for the specified workflow goal.

### Metadata
**Author:** Extraltodeus
**Repository:** [https://github.com/Extraltodeus/ComfyUI-AutomaticCFG](https://github.com/Extraltodeus/ComfyUI-AutomaticCFG)
**Install Type:** git-clone

---

### ComfyUI-autosize

**Description:**

A ComfyUI utility plugin designed to optimize the latent space for generating high-quality results. It approximates the closest size model for better generation results.

- **Author:** chakib-belgaid
- **Repository:** [https://github.com/chakib-belgaid/ComfyUI-autosize](https://github.com/chakib-belgaid/ComfyUI-autosize)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node optimizes latent space for high-quality results, making it very useful for generating images from text and upscaling them.

### Metadata
**Author:** chakib-belgaid
**Repository:** [https://github.com/chakib-belgaid/ComfyUI-autosize](https://github.com/chakib-belgaid/ComfyUI-autosize)
**Install Type:** git-clone

---

### ComfyUI-Background-Edit

**Description:**

ComfyUI nodes for editing background of images/videos with CUDA acceleration support.

- **Author:** yondonfu
- **Repository:** [https://github.com/yondonfu/ComfyUI-Background-Edit](https://github.com/yondonfu/ComfyUI-Background-Edit)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node edits backgrounds of images/videos which could be a supporting task for the specified workflow goal, but its direct relevance is limited.

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

**Reason:** This node provides a CharacterPipe that can manage elements relevant to character-based image generation, making it very useful for this workflow.

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

**Score:** 100/100

**Reason:** This node is a high-resolution image generation model specifically designed for two-pass highres fix upscales.

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

**Score:** 90/100

**Reason:** This node wraps the latest BiRefNet model with improved matting accuracy, making it suitable for generating high-quality images.

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

**Score:** 80/100

**Reason:** Although this node is a lightweight version of BiRefNet, its support for chunked loading and model caching makes it useful for large-scale image generation tasks.

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

**Score:** 100/100

**Reason:** This node is a diffusion model tool that can generate images from text, making it highly relevant for the specified workflow goal.

### Metadata
**Author:** bongsang
**Repository:** [https://github.com/bongsang/ComfyUI-Bongsang](https://github.com/bongsang/ComfyUI-Bongsang)
**Install Type:** git-clone

---

### ComfyUI-BrushNet-Wrapper

**Description:**

ComfyUI wrapper nodes to use the Diffusers implementation of BrushNet

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-BrushNet-Wrapper](https://github.com/kijai/ComfyUI-BrushNet-Wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements BrushNet model for image generation from text.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-BrushNet-Wrapper](https://github.com/kijai/ComfyUI-BrushNet-Wrapper)
**Install Type:** git-clone

---

### ComfyUI-CADS

**Description:**

Attempts to implement [a/CADS](https://arxiv.org/abs/2310.17347) for ComfyUI. Credit also to the [a/A1111 implementation](https://github.com/v0xie/sd-webui-cads/tree/main) that I used as a reference.

- **Author:** asagi4
- **Repository:** [https://github.com/asagi4/ComfyUI-CADS](https://github.com/asagi4/ComfyUI-CADS)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements CADS model for image generation from text which matches the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node provides improved numerical calculations which could aid in upscale processing.

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

**Reason:** This node handles resolutions but does not seem to be specifically designed for upscaling or image generation from text.

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

**Reason:** This node directly provides a virtual try-on diffusion model that can generate images from text and upscale them with high resolution.

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

**Reason:** This node is very useful as it provides ComfyUI nodes for the Catvton-Flux diffuser implementation, which is relevant to generating images from text and upscaling them.

### Metadata
**Author:** lujiazho
**Repository:** [https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper](https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper)
**Install Type:** git-clone

---

### ComfyUI-CCSR

**Description:**

ComfyUI- CCSR upscaler node

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-CCSR](https://github.com/kijai/ComfyUI-CCSR)
- **Install Type:** git-clone


### Applicability

**Score:** 50/100

**Reason:** This node has moderate utility as it provides an upscaler node, but its relevance to a 2-pass highres fix is unclear without further information.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-CCSR](https://github.com/kijai/ComfyUI-CCSR)
**Install Type:** git-clone

---

### ComfyUI-Champ

**Description:**

ComfyUI Champ

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-Champ](https://github.com/chaojie/ComfyUI-Champ)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can upscale an image with a 2-pass highres fix, directly aligning with the workflow goal.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Champ](https://github.com/chaojie/ComfyUI-Champ)
**Install Type:** git-clone

---

### ComfyUI-Chibi-Nodes

**Description:**

Nodes:Loader, Prompts, ImageTool, Wildcards, LoadEmbedding, ConditionText, SaveImages, ...

- **Author:** chibiace
- **Repository:** [https://github.com/chibiace/ComfyUI-Chibi-Nodes](https://github.com/chibiace/ComfyUI-Chibi-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates images from text with upscaling capabilities.

### Metadata
**Author:** chibiace
**Repository:** [https://github.com/chibiace/ComfyUI-Chibi-Nodes](https://github.com/chibiace/ComfyUI-Chibi-Nodes)
**Install Type:** git-clone

---

### ComfyUI-CLIPSlider

**Description:**

A node to replicate [a/https://huggingface.co/spaces/latentexplorers/latentnavigation-flux](A node to replicate https://huggingface.co/spaces/latentexplorers/latentnavigation-flux)

- **Author:** RhizoNymph
- **Repository:** [https://github.com/RhizoNymph/ComfyUI-CLIPSlider](https://github.com/RhizoNymph/ComfyUI-CLIPSlider)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Provides a slider interface for navigating CLIP embeddings which can aid in finding suitable images.

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

**Score:** 100/100

**Reason:** This node directly implements CogVideoX model which can generate images from text and upscale them with a 2-pass highres fix.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ](https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ)
**Install Type:** git-clone

---

### ComfyUI-ComfyWorkflows

**Description:**

The best way to run, share, & discover thousands of ComfyUI workflows.

- **Author:** thecooltechguy
- **Repository:** [https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows](https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** ComfyUI-ComfyWorkflows contains thousands of workflows that may include the specific task of generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** thecooltechguy
**Repository:** [https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows](https://github.com/thecooltechguy/ComfyUI-ComfyWorkflows)
**Install Type:** git-clone

---

### ComfyUI-ConDelta

**Description:**

This extension extends ComfyUI's capabilities with respect to manipulating conditionings.

- **Author:** envy-ai
- **Repository:** [https://github.com/envy-ai/ComfyUI-ConDelta](https://github.com/envy-ai/ComfyUI-ConDelta)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This extension is specifically designed to manipulate conditionings which could be useful in generating high-quality images from text.

### Metadata
**Author:** envy-ai
**Repository:** [https://github.com/envy-ai/ComfyUI-ConDelta](https://github.com/envy-ai/ComfyUI-ConDelta)
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

**Reason:** CreaPrompt can generate random prompts which could be useful for this workflow goal by providing alternative text inputs for image generation.

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

**Score:** 40/100

**Reason:** The CSV Loader is marginally relevant as it allows access to positive/negative prompts associated with a name, but its primary function is loading CSV files rather than contributing directly to the workflow goal of generating and upscaling images from text.

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

**Score:** 100/100

**Reason:** This node acts as a bridge between ComfyUI and Blender, which is necessary for the specified workflow goal.

### Metadata
**Author:** AIGODLIKE
**Repository:** [https://github.com/AIGODLIKE/ComfyUI-CUP](https://github.com/AIGODLIKE/ComfyUI-CUP)
**Install Type:** git-clone

---

### ComfyUI-Dashscope

**Description:**

This project adapts the dashscope([a/aliyun-bailian](https://bailian.console.aliyun.com)) api into ComfyUI.

- **Author:** neverbiasu
- **Repository:** [https://github.com/neverbiasu/ComfyUI-Dashscope](https://github.com/neverbiasu/ComfyUI-Dashscope)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node adapts an API into ComfyUI but its relevance to the workflow goal is unclear.

### Metadata
**Author:** neverbiasu
**Repository:** [https://github.com/neverbiasu/ComfyUI-Dashscope](https://github.com/neverbiasu/ComfyUI-Dashscope)
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

**Reason:** This node provides data research and manipulation capabilities that can support tasks related to generating images from text and upscaling them.

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

**Score:** 100/100

**Reason:** This node directly supports the workflow goal by providing a high-resolution image generation capability.

### Metadata
**Author:** Vaibhavs10
**Repository:** [https://github.com/Vaibhavs10/ComfyUI-DDUF](https://github.com/Vaibhavs10/ComfyUI-DDUF)
**Install Type:** git-clone

---

### ComfyUI-decadetw-auto-prompt-llm

**Description:**

Auto prompt by LLM and LLM-Vision. (Trigger more details hiding in model)

- **Author:** xlinx
- **Repository:** [https://github.com/xlinx/ComfyUI-decadetw-auto-prompt-llm](https://github.com/xlinx/ComfyUI-decadetw-auto-prompt-llm)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates images from text with highres fix functionality.

### Metadata
**Author:** xlinx
**Repository:** [https://github.com/xlinx/ComfyUI-decadetw-auto-prompt-llm](https://github.com/xlinx/ComfyUI-decadetw-auto-prompt-llm)
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

**Score:** 90/100

**Reason:** Provides acceleration for ComfyUI nodes, ideal for bulk image production.

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

**Score:** 100/100

**Reason:** Directly accelerates and fixes ComfyUI nodes for highres image generation.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI-DeepCache-Fix](https://github.com/SoftMeng/ComfyUI-DeepCache-Fix)
**Install Type:** git-clone

---

### comfyui-default-values-manager

**Description:**

comfyui-default-values-manager

- **Author:** christian-byrne
- **Repository:** [https://github.com/christian-byrne/comfyui-default-values-manager](https://github.com/christian-byrne/comfyui-default-values-manager)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides default values that can be used in conjunction with other nodes to generate and upscale images.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/comfyui-default-values-manager](https://github.com/christian-byrne/comfyui-default-values-manager)
**Install Type:** git-clone

---

### ComfyUI-Depth-Pro

**Description:**

Based on [a/https://github.com/apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-Depth-Pro](https://github.com/spacepxl/ComfyUI-Depth-Pro)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can estimate depth maps which are necessary for high-resolution upsampling in the specified workflow goal.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Depth-Pro](https://github.com/spacepxl/ComfyUI-Depth-Pro)
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

**Reason:** This node can generate depth maps which are essential for high-resolution upsampling in the specified workflow goal and also autodownloads models for convenience.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2)
**Install Type:** git-clone

---

### ComfyUI-Desert-Pixel-Nodes

**Description:**

A collection of custom nodes for ComfyUI focused on animation, image processing, and workflow optimization.

- **Author:** DesertPixelAi
- **Repository:** [https://github.com/DesertPixelAi/ComfyUI-Desert-Pixel-Nodes](https://github.com/DesertPixelAi/ComfyUI-Desert-Pixel-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node collection is specifically focused on animation and image processing, making it highly relevant to generating an image from text and upscaling it.

### Metadata
**Author:** DesertPixelAi
**Repository:** [https://github.com/DesertPixelAi/ComfyUI-Desert-Pixel-Nodes](https://github.com/DesertPixelAi/ComfyUI-Desert-Pixel-Nodes)
**Install Type:** git-clone

---

### ComfyUI-DiffSynth-Studio

**Description:**

make [a/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) available in ComfyUI

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-DiffSynth-Studio](https://github.com/AIFSH/ComfyUI-DiffSynth-Studio)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential as it provides a studio environment specifically designed for DiffSynth, which aligns perfectly with the workflow goal.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-DiffSynth-Studio](https://github.com/AIFSH/ComfyUI-DiffSynth-Studio)
**Install Type:** git-clone

---

### ComfyUI-Diffusers

**Description:**

This extension enables the use of the diffuser pipeline in ComfyUI. It also includes nodes related to Stream Diffusion.

- **Author:** Limitex
- **Repository:** [https://github.com/Limitex/ComfyUI-Diffusers](https://github.com/Limitex/ComfyUI-Diffusers)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it enables the use of the diffuser pipeline in ComfyUI, directly supporting the generation and upscaling of images from text.

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

**Score:** 60/100

**Reason:** This node is moderately useful for outpainting images with diffusers, but its relevance to the specific workflow goal (upscale with a 2-pass highres fix) is not as direct.

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

**Score:** 90/100

**Reason:** This node provides advanced document processing capabilities that can be used to load and parse text documents, which is essential for generating an image from text.

### Metadata
**Author:** Indra's Mirror
**Repository:** [https://github.com/Excidos/ComfyUI-Documents](https://github.com/Excidos/ComfyUI-Documents)
**Install Type:** git-clone

---

### ComfyUI-DragNUWA

**Description:**

Nodes: Download the weights of DragNUWA [a/drag_nuwa_svd.pth](https://drive.google.com/file/d/1Z4JOley0SJCb35kFF4PCc6N6P1ftfX4i/view) and put it to ComfyUI/models/checkpoints/drag_nuwa_svd.pth
[w/Due to changes in the torch package and versions of many other packages, it may disrupt your installation environment.]

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-DragNUWA](https://github.com/chaojie/ComfyUI-DragNUWA)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly provides the necessary weights for generating images from text and upscaling them.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-DragNUWA](https://github.com/chaojie/ComfyUI-DragNUWA)
**Install Type:** git-clone

---

### ComfyUI-DreamWaltz-G

**Description:**

This repository contains custom ComfyUI nodes designed to integrate with [a/DreamWaltz-G](https://github.com/Yukun-Huang/DreamWaltz-G), a cutting-edge model for generating expressive 3D Gaussian avatars using skeleton-guided 2D diffusion.

- **Author:** gt732
- **Repository:** [https://github.com/gt732/ComfyUI-DreamWaltz-G](https://github.com/gt732/ComfyUI-DreamWaltz-G)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a custom integration with DreamWaltz-G, which directly supports generating images from text.

### Metadata
**Author:** gt732
**Repository:** [https://github.com/gt732/ComfyUI-DreamWaltz-G](https://github.com/gt732/ComfyUI-DreamWaltz-G)
**Install Type:** git-clone

---

### ComfyUI-dust3r

**Description:**

ComfyUI dust3r

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-dust3r](https://github.com/chaojie/ComfyUI-dust3r)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node supports image generation from text but lacks specific information about high-resolution fixes or upscaling.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-dust3r](https://github.com/chaojie/ComfyUI-dust3r)
**Install Type:** git-clone

---

### ComfyUI-DynamiCrafter

**Description:**

Better Dynamic, Higher Resolution, and Stronger Coherence!

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-DynamiCrafter](https://github.com/chaojie/ComfyUI-DynamiCrafter)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node claims to generate higher resolution and stronger coherence, making it moderately useful for upscaling images.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-DynamiCrafter](https://github.com/chaojie/ComfyUI-DynamiCrafter)
**Install Type:** git-clone

---

### ComfyUI-EasyAnimate

**Description:**

ComfyUI-EasyAnimate

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-EasyAnimate](https://github.com/chaojie/ComfyUI-EasyAnimate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** ComfyUI-EasyAnimate provides animation features but also includes functionality for image processing and manipulation which can be used for upscaling images.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-EasyAnimate](https://github.com/chaojie/ComfyUI-EasyAnimate)
**Install Type:** git-clone

---

### ComfyUI-EasyOCR

**Description:**

This node is primarily based on Easy-OCR to implement OCR text recognition functionality.

- **Author:** prodogape
- **Repository:** [https://github.com/prodogape/ComfyUI-EasyOCR](https://github.com/prodogape/ComfyUI-EasyOCR)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides OCR text recognition functionality which can be useful in preprocessing the input text before generating an image.

### Metadata
**Author:** prodogape
**Repository:** [https://github.com/prodogape/ComfyUI-EasyOCR](https://github.com/prodogape/ComfyUI-EasyOCR)
**Install Type:** git-clone

---

### ComfyUI-EbSynth

**Description:**

Run EbSynth, Fast Example-based Image Synthesis and Style Transfer, in ComfyUI.

- **Author:** Fuou Marinas
- **Repository:** [https://github.com/FuouM/ComfyUI-EbSynth](https://github.com/FuouM/ComfyUI-EbSynth)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements EbSynth, a fast example-based image synthesis and style transfer model suitable for generating images from text.

### Metadata
**Author:** Fuou Marinas
**Repository:** [https://github.com/FuouM/ComfyUI-EbSynth](https://github.com/FuouM/ComfyUI-EbSynth)
**Install Type:** git-clone

---

### ComfyUI-EfficientTAM

**Description:**

A ComfyUI implementation of [a/EfficientTAM](https://github.com/yformer/EfficientTAM)

- **Author:** RyanOnTheInside
- **Repository:** [https://github.com/ryanontheinside/ComfyUI_EfficientTAM](https://github.com/ryanontheinside/ComfyUI_EfficientTAM)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node implements EfficientTAM, which can be used for image generation and upscaling tasks. However, it may not directly support a 2-pass highres fix, but it could still be useful with additional processing steps.

### Metadata
**Author:** RyanOnTheInside
**Repository:** [https://github.com/ryanontheinside/ComfyUI_EfficientTAM](https://github.com/ryanontheinside/ComfyUI_EfficientTAM)
**Install Type:** git-clone

---

### ComfyUI-ELLA

**Description:**

ComfyUI implementation for [a/ELLA](https://github.com/TencentQQGYLab/ELLA).

- **Author:** TencentQQGYLab
- **Repository:** [https://github.com/TencentQQGYLab/ComfyUI-ELLA](https://github.com/TencentQQGYLab/ComfyUI-ELLA)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly implements ELLA, which can generate high-quality images from text and upscale them with a 2-pass highres fix.

### Metadata
**Author:** TencentQQGYLab
**Repository:** [https://github.com/TencentQQGYLab/ComfyUI-ELLA](https://github.com/TencentQQGYLab/ComfyUI-ELLA)
**Install Type:** git-clone

---

### ComfyUI-ELLA-wrapper

**Description:**

ComfyUI wrapper nodes to use the Diffusers implementation of ELLA

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-ELLA-wrapper](https://github.com/kijai/ComfyUI-ELLA-wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** As a wrapper for the Diffusers implementation of ELLA, this node is very useful for generating images from text and upscaling them with a 2-pass highres fix.

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

**Score:** 81/100

**Reason:** This node can save enhanced images generated by other nodes in the workflow, making it very useful for this goal.

### Metadata
**Author:** HebelHuber
**Repository:** [https://github.com/HebelHuber/comfyui-enhanced-save-node](https://github.com/HebelHuber/comfyui-enhanced-save-node)
**Install Type:** git-clone

---

### ComfyUI-EvTexture

**Description:**

Wrapper for EvTexture Video Upscaler: [a/https://github.com/DachunKai/EvTexture](https://github.com/DachunKai/EvTexture)

- **Author:** tocubed
- **Repository:** [https://github.com/tocubed/ComfyUI-EvTexture](https://github.com/tocubed/ComfyUI-EvTexture)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a wrapper for EvTexture Video Upscaler which can upscale images, directly contributing to the specified workflow goal.

### Metadata
**Author:** tocubed
**Repository:** [https://github.com/tocubed/ComfyUI-EvTexture](https://github.com/tocubed/ComfyUI-EvTexture)
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

**Reason:** This node directly enables face chain functionality which can generate images from text.

### Metadata
**Author:** THtianhao
**Repository:** [https://github.com/THtianhao/ComfyUI-FaceChain](https://github.com/THtianhao/ComfyUI-FaceChain)
**Install Type:** git-clone

---

### ComfyUI-Fal-API-Flux

**Description:**

This repository contains custom nodes for ComfyUI that integrate the fal.ai FLUX.1 [dev] with LoRA API, specifically for text-to-image generation. These nodes allow you to use the FLUX.1 model directly within your ComfyUI workflows.

- **Author:** yhayano-ponotech
- **Repository:** [https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux](https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides direct integration of the FLUX.1 model for text-to-image generation.

### Metadata
**Author:** yhayano-ponotech
**Repository:** [https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux](https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux)
**Install Type:** git-clone

---

### ComfyUI-FapMixPlus

**Description:**

This is an audio processing script that applies soft limiting, optional loudness normalization, and optional slicing for transcription. It can also produce stereo-mixed outputs with optional audio appended to the end. The script organizes processed files into structured folders with sanitized filenames and retains original timestamps for continuity.

- **Author:** akspa0
- **Repository:** [https://github.com/akspa0/ComfyUI-FapMixPlus](https://github.com/akspa0/ComfyUI-FapMixPlus)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a basic neural style transfer function but lacks upscale functionality.

### Metadata
**Author:** akspa0
**Repository:** [https://github.com/akspa0/ComfyUI-FapMixPlus](https://github.com/akspa0/ComfyUI-FapMixPlus)
**Install Type:** git-clone

---

### ComfyUI-fastblend

**Description:**

fastblend for comfyui, and other nodes that I write for video2video. rebatch image, my openpose

- **Author:** AInseven
- **Repository:** [https://github.com/AInseven/ComfyUI-fastblend](https://github.com/AInseven/ComfyUI-fastblend)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a prompt styler that can replace {prompt} words in CSV files, which could be useful for generating text-based prompts for image generation.

### Metadata
**Author:** AInseven
**Repository:** [https://github.com/AInseven/ComfyUI-fastblend](https://github.com/AInseven/ComfyUI-fastblend)
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

**Reason:** This node is specifically designed for JPEG de-artifacting, which can improve the quality of images after upscaling.

### Metadata
**Author:** miosp
**Repository:** [https://github.com/Miosp/ComfyUI-FBCNN](https://github.com/Miosp/ComfyUI-FBCNN)
**Install Type:** git-clone

---

### ComfyUI-FFmpeg

**Description:**

Encapsulate the commonly used functions of FFmpeg into ComfyUI nodes, making it convenient for users to perform various video processing tasks within ComfyUI.

- **Author:** MoonHugo
- **Repository:** [https://github.com/MoonHugo/ComfyUI-FFmpeg](https://github.com/MoonHugo/ComfyUI-FFmpeg)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for generating an image from text using FFmpeg.

### Metadata
**Author:** MoonHugo
**Repository:** [https://github.com/MoonHugo/ComfyUI-FFmpeg](https://github.com/MoonHugo/ComfyUI-FFmpeg)
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

**Score:** 80/100

**Reason:** Although this node can fill images for outpainting, its primary purpose is not directly related to the specified workflow goal, but it could be used as a supporting node.

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

**Score:** 81/100

**Reason:** This node can be used to resize images, which could be a supporting step in the workflow goal of generating an image from text and upscaling it.

### Metadata
**Author:** bronkula
**Repository:** [https://github.com/bronkula/comfyui-fitsize](https://github.com/bronkula/comfyui-fitsize)
**Install Type:** git-clone

---

### ComfyUI-FLATTEN

**Description:**

ComfyUI nodes to use [a/FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing](https://github.com/yrcong/flatten).

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-FLATTEN](https://github.com/logtd/ComfyUI-FLATTEN)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node appears to be related to optical flow-guided attention for consistent text-to-video editing, which could be relevant to generating images from text and upscaling them.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-FLATTEN](https://github.com/logtd/ComfyUI-FLATTEN)
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

**Score:** 100/100

**Reason:** Directly supports generating images from text with upscale functionality.

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

**Score:** 90/100

**Reason:** Supports image vision tasks including captioning which can be used to generate an image from text.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)
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

**Reason:** Directly relevant to generating an image from text.

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

**Score:** 100/100

**Reason:** Essential for upscaling with a 2-pass highres fix.

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

**Score:** 100/100

**Reason:** Essential for upscaling with a 2-pass highres fix.

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

**Score:** 81/100

**Reason:** This node directly supports image inpainting and outpainting which is a crucial step in upscaling an image.

### Metadata
**Author:** duhaifeng
**Repository:** [https://github.com/rubi-du/ComfyUI-Flux-Inpainting](https://github.com/rubi-du/ComfyUI-Flux-Inpainting)
**Install Type:** git-clone

---

### ComfyUI-Flux-Replicate-API

**Description:**

Flux Pro via Replicate API
Create API key at [a/https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
Copy config.ini.example to config.ini and put the replicate key there.

- **Author:** smlbiobot
- **Repository:** [https://github.com/smlbiobot/ComfyUI-Flux-Replicate-API](https://github.com/smlbiobot/ComfyUI-Flux-Replicate-API)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node provides access to the Flux Pro model via Replicate API but does not directly contribute to the workflow goal of generating and upsampling an image.

### Metadata
**Author:** smlbiobot
**Repository:** [https://github.com/smlbiobot/ComfyUI-Flux-Replicate-API](https://github.com/smlbiobot/ComfyUI-Flux-Replicate-API)
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

**Reason:** This node seems to be related to the Flux model and has tool nodes for it, which could be useful in conjunction with other nodes for upscaling.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ](https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ)
**Install Type:** git-clone

---

### comfyui-fofr-toolkit

**Description:**

Nodes:Incrementer, Width and height from aspect ratio, Width and height for scaling image to ideal resolutio. A simple set of tooling nodes.

- **Author:** fofr
- **Repository:** [https://github.com/fofr/comfyui-fofr-toolkit](https://github.com/fofr/comfyui-fofr-toolkit)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some utility nodes like incrementer and width/height calculators that could support the workflow, but they are not directly related to text-to-image or upscaling.

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

**Score:** 100/100

**Reason:** This node provides features (frame interpolation) that can be used in conjunction with the workflow goal of generating an image and upscaling it.

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

**Score:** 80/100

**Reason:** This node provides advanced memory management capabilities that can help prevent out-of-memory errors during complex operations like upscaling images.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-FreeMemory](https://github.com/ShmuelRonen/ComfyUI-FreeMemory)
**Install Type:** git-clone

---

### ComfyUI-FutureWarningIgnore

**Description:**

This extension collapses 'future warning' messages in your Console

- **Author:** Gourieff
- **Repository:** [https://github.com/Gourieff/ComfyUI-FutureWarningIgnore](https://github.com/Gourieff/ComfyUI-FutureWarningIgnore)
- **Install Type:** copy


### Applicability

**Score:** 100/100

**Reason:** This node directly ignores future warning messages in the Console, which can be distracting during workflow execution.

### Metadata
**Author:** Gourieff
**Repository:** [https://github.com/Gourieff/ComfyUI-FutureWarningIgnore](https://github.com/Gourieff/ComfyUI-FutureWarningIgnore)
**Install Type:** copy

---

### Comfyui-Gelbooru

**Description:**

Get random images from gelbooru, support multiple tag searches, exclude tags, etc. user and api key are optional.

- **Author:** 1mckw
- **Repository:** [https://github.com/1mckw/Comfyui-Gelbooru](https://github.com/1mckw/Comfyui-Gelbooru)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node can be used to fetch random images from Gelbooru, which could potentially be used as a source for the image generation task.

### Metadata
**Author:** 1mckw
**Repository:** [https://github.com/1mckw/Comfyui-Gelbooru](https://github.com/1mckw/Comfyui-Gelbooru)
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

**Reason:** This node is highly relevant as it contains a collection of ComfyUI nodes designed for image processing workflows, including tasks related to text-to-image generation and upscaling.

### Metadata
**Author:** leestuartx
**Repository:** [https://github.com/leestuartx/ComfyUI-GG](https://github.com/leestuartx/ComfyUI-GG)
**Install Type:** git-clone

---

### ComfyUI-GigapixelAI

**Description:**

Custom nodes use gigapixelai in comfyui.

- **Author:** sh570655308
- **Repository:** [https://github.com/sh570655308/ComfyUI-GigapixelAI](https://github.com/sh570655308/ComfyUI-GigapixelAI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly provides high-resolution image upscaling with a 2-pass fix, aligning perfectly with the workflow goal.

### Metadata
**Author:** sh570655308
**Repository:** [https://github.com/sh570655308/ComfyUI-GigapixelAI](https://github.com/sh570655308/ComfyUI-GigapixelAI)
**Install Type:** git-clone

---

### ComfyUI-Golden-Noise

**Description:**

ComfyUI Custom Node for 'Golden Noise for Diffusion Models: A Learning Framework'. This node refines the initial latent noise in the diffusion process, enhancing both image quality and semantic coherence.

- **Author:** LucipherDev
- **Repository:** [https://github.com/LucipherDev/ComfyUI-Golden-Noise](https://github.com/LucipherDev/ComfyUI-Golden-Noise)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node refines latent noise in the diffusion process, enhancing image quality which could be useful for upscale tasks but may require additional processing steps.

### Metadata
**Author:** LucipherDev
**Repository:** [https://github.com/LucipherDev/ComfyUI-Golden-Noise](https://github.com/LucipherDev/ComfyUI-Golden-Noise)
**Install Type:** git-clone

---

### ComfyUI-GPT4V-Image-Captioner

**Description:**

Nodes:GPT4V-Image-Captioner

- **Author:** 438443467
- **Repository:** [https://github.com/438443467/ComfyUI-GPT4V-Image-Captioner](https://github.com/438443467/ComfyUI-GPT4V-Image-Captioner)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly responsible for generating an image from text.

### Metadata
**Author:** 438443467
**Repository:** [https://github.com/438443467/ComfyUI-GPT4V-Image-Captioner](https://github.com/438443467/ComfyUI-GPT4V-Image-Captioner)
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

**Reason:** This node provides direct access to Haiper AI API which can generate images from text and upscale them.

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

**Reason:** This node offers a range of image processing tools that can be used for upscaling and fixing generated images.

### Metadata
**Author:** licyk
**Repository:** [https://github.com/licyk/ComfyUI-HakuImg](https://github.com/licyk/ComfyUI-HakuImg)
**Install Type:** git-clone

---

### ComfyUI-Hangover-Moondream

**Description:**

Moondream is a lightweight multimodal large language model.
[w/WARN:Additional python code will be downloaded from huggingface and executed. You have to trust this creator if you want to use this node!]

- **Author:** Hangover3832
- **Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Moondream](https://github.com/Hangover3832/ComfyUI-Hangover-Moondream)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly generates images from text and has upscaling capabilities.

### Metadata
**Author:** Hangover3832
**Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Moondream](https://github.com/Hangover3832/ComfyUI-Hangover-Moondream)
**Install Type:** git-clone

---

### ComfyUI-Hangover-Nodes

**Description:**

Nodes: MS kosmos-2 Interrogator, Save Image w/o Metadata, Image Scale Bounding Box. An implementation of Microsoft [a/kosmos-2](https://huggingface.co/microsoft/kosmos-2-patch14-224) image to text transformer.

- **Author:** Hangover3832
- **Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Nodes](https://github.com/Hangover3832/ComfyUI-Hangover-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Provides multiple nodes that can be used to generate an image from text and upscale it with a 2-pass highres fix.

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

**Reason:** This node loads models from Hugging Face repositories, which could be used for text-to-image generation and upscaling.

### Metadata
**Author:** olduvai-jp
**Repository:** [https://github.com/olduvai-jp/ComfyUI-HfLoader](https://github.com/olduvai-jp/ComfyUI-HfLoader)
**Install Type:** git-clone

---

### ComfyUI-Html2Image

**Description:**

NODES: Webpage Screenshot, Camera Watermark, Template To Image

- **Author:** liuqianhonga
- **Repository:** [https://github.com/liuqianhonga/ComfyUI-Html2Image](https://github.com/liuqianhonga/ComfyUI-Html2Image)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate an image from HTML content which could be used as a starting point for the workflow goal.

### Metadata
**Author:** liuqianhonga
**Repository:** [https://github.com/liuqianhonga/ComfyUI-Html2Image](https://github.com/liuqianhonga/ComfyUI-Html2Image)
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

**Score:** 100/100

**Reason:** This node directly addresses issues with loading multiple LoRAs in HunYuan Video, which may be related to image generation and upscaling.

### Metadata
**Author:** facok
**Repository:** [https://github.com/facok/ComfyUI-HunyuanVideoMultiLora](https://github.com/facok/ComfyUI-HunyuanVideoMultiLora)
**Install Type:** git-clone

---

### ComfyUI-HunyuanVideoWrapper

**Description:**

ComfyUI diffusers wrapper nodes for [a/HunyuanVideo](https://github.com/Tencent/HunyuanVideo)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-HunyuanVideoWrapper](https://github.com/kijai/ComfyUI-HunyuanVideoWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is a wrapper for HunyuanVideo, which can generate images from text. It also supports upscaling with a highres fix, making it directly relevant to the workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-HunyuanVideoWrapper](https://github.com/kijai/ComfyUI-HunyuanVideoWrapper)
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

**Score:** 41/100

**Reason:** This node is a sampler for HyperSDXL UNet, but its relevance to the specific workflow goal of generating an image and upscaling with a 2-pass highres fix is unclear. It might be useful as a supporting node, but more information would be needed.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler](https://github.com/fofr/ComfyUI-HyperSDXL1StepUnetScheduler)
**Install Type:** git-clone

---

### ComfyUI-I2V-Adapter

**Description:**

a comfyui custom node for [a/I2V-Adapter](https://github.com/KwaiVGI/I2V-Adapter)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-I2V-Adapter](https://github.com/AIFSH/ComfyUI-I2V-Adapter)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is an adapter for I2V-Adapter, which can generate images from text. While it does not explicitly mention upscaling with a highres fix, it could potentially be used in conjunction with other nodes to achieve the desired outcome.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-I2V-Adapter](https://github.com/AIFSH/ComfyUI-I2V-Adapter)
**Install Type:** git-clone

---

### ComfyUI-I2VGEN-XL

**Description:**

This is an implementation of [a/i2vgen-xl](https://github.com/ali-vilab/i2vgen-xl)

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-I2VGEN-XL](https://github.com/chaojie/ComfyUI-I2VGEN-XL)
- **Install Type:** git-clone


### Applicability

**Score:** 91/100

**Reason:** This node implements i2vgen-xl, which is specifically designed for generating high-resolution images from text and supports upscaling. It seems like this node would be essential for achieving the workflow goal.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-I2VGEN-XL](https://github.com/chaojie/ComfyUI-I2VGEN-XL)
**Install Type:** git-clone

---

### ComfyUI-IC-Light

**Description:**

ComfyUI native nodes for IC-Light

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-IC-Light](https://github.com/kijai/ComfyUI-IC-Light)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Direct implementation of IC-Light, a key component in generating high-quality images from text.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-IC-Light](https://github.com/kijai/ComfyUI-IC-Light)
**Install Type:** git-clone

---

### ComfyUI-IC-Light-Native

**Description:**

ComfyUI native implementation of [a/IC-Light](https://github.com/lllyasviel/IC-Light).

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI-IC-Light-Native](https://github.com/huchenlei/ComfyUI-IC-Light-Native)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Native implementation of IC-Light, ensuring optimal performance and compatibility with the specified workflow goal.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI-IC-Light-Native](https://github.com/huchenlei/ComfyUI-IC-Light-Native)
**Install Type:** git-clone

---

### ComfyUI-IF_AI_tools

**Description:**

Various AI tools to use in Comfy UI. Starting with VL and prompt making tools using Ollma as backend will evolve as I find time.

- **Author:** if-ai
- **Repository:** [https://github.com/if-ai/ComfyUI-IF_AI_tools](https://github.com/if-ai/ComfyUI-IF_AI_tools)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains various AI tools that can be used in Comfy UI for tasks like image generation and upscaling.

### Metadata
**Author:** if-ai
**Repository:** [https://github.com/if-ai/ComfyUI-IF_AI_tools](https://github.com/if-ai/ComfyUI-IF_AI_tools)
**Install Type:** git-clone

---

### ComfyUI-IG-Motion-I2V

**Description:**

ComfyUI adaptation of https://github.com/G-U-N/Motion-I2V

- **Author:** IDGallagher
- **Repository:** [https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V](https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for image-to-video tasks and can likely upscale images with high-resolution fixes, making it highly relevant to the workflow goal.

### Metadata
**Author:** IDGallagher
**Repository:** [https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V](https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V)
**Install Type:** git-clone

---

### ComfyUI-Image-Filters

**Description:**

Image and matte filtering nodes for ComfyUI `image/filters/*`

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides image filters which could be used as a supporting tool for post-processing but is not essential for upscaling.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)
**Install Type:** git-clone

---

### comfyui-image-round

**Description:**

A simple node to round an input image up (pad) or down (crop) to the nearest integer multiple. Padding offset from left/bottom and the padding value are adjustable.

- **Author:** cdb-boop
- **Repository:** [https://github.com/cdb-boop/comfyui-image-round](https://github.com/cdb-boop/comfyui-image-round)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can be used to adjust image size but doesn"t directly contribute to generating an image from text or upscaling it with a 2-pass highres fix.

### Metadata
**Author:** cdb-boop
**Repository:** [https://github.com/cdb-boop/comfyui-image-round](https://github.com/cdb-boop/comfyui-image-round)
**Install Type:** git-clone

---

### ComfyUI-Image-Tools

**Description:**

Nodes:BatchImageResizeProcessor, SingleImagePathLoader, SingleImageUrlLoader

- **Author:** knuknX
- **Repository:** [https://github.com/knuknX/ComfyUI-Image-Tools](https://github.com/knuknX/ComfyUI-Image-Tools)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a batch of images that can be used as input for generating an image from text and upscaling it.

### Metadata
**Author:** knuknX
**Repository:** [https://github.com/knuknX/ComfyUI-Image-Tools](https://github.com/knuknX/ComfyUI-Image-Tools)
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

**Reason:** This node assists in converting images into sketches, which is marginally relevant to the workflow goal of generating and upsampling an image.

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

**Reason:** Directly generates an image from text with highres fix functionality

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Img2Img-Turbo](https://github.com/chaojie/ComfyUI-Img2Img-Turbo)
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

**Score:** 90/100

**Reason:** This node is highly relevant as it can be used for cropping and stitching images, which are crucial steps in the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node provides optimized local repainting functions that could aid in generating an image from text by simplifying the inpainting process.

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

**Score:** 80/100

**Reason:** This node provides several utility nodes that could be used in conjunction with other nodes to upscale the generated image.

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

**Score:** 80/100

**Reason:** This node can make the UI interactive, allowing users to select options and move the workflow forward, which could be useful for this goal.

### Metadata
**Author:** lquesada
**Repository:** [https://github.com/lquesada/ComfyUI-Interactive](https://github.com/lquesada/ComfyUI-Interactive)
**Install Type:** git-clone

---

### ComfyUI-IPAnimate

**Description:**

This is a project that generates videos frame by frame based on IPAdapter+ControlNet. Unlike [a/Steerable-motion](https://github.com/banodoco/Steerable-Motion), we do not rely on AnimateDiff. This decision is primarily due to the fact that the videos generated by AnimateDiff are often blurry. Through frame-by-frame control using IPAdapter+ControlNet, we can produce higher definition and more controllable videos.

- **Author:** Chan-0312
- **Repository:** [https://github.com/Chan-0312/ComfyUI-IPAnimate](https://github.com/Chan-0312/ComfyUI-IPAnimate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates videos frame by frame based on IPAdapter+ControlNet and can be used for high-definition video generation which aligns with the workflow goal of upscaling an image.

### Metadata
**Author:** Chan-0312
**Repository:** [https://github.com/Chan-0312/ComfyUI-IPAnimate](https://github.com/Chan-0312/ComfyUI-IPAnimate)
**Install Type:** git-clone

---

### ComfyUI-JakeUpgrade

**Description:**

A ComfyUI workflow customization by Jake.

- **Author:** jakechai
- **Repository:** [https://github.com/jakechai/ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a customization of ComfyUI and includes features like highres fix which directly relates to the workflow goal.

### Metadata
**Author:** jakechai
**Repository:** [https://github.com/jakechai/ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade)
**Install Type:** git-clone

---

### ComfyUI-Jjk-Nodes

**Description:**

Nodes: SDXLRecommendedImageSize, JjkText, JjkShowText, JjkConcat. A set of custom nodes for ComfyUI - focused on text and parameter utility

- **Author:** jjkramhoeft
- **Repository:** [https://github.com/jjkramhoeft/ComfyUI-Jjk-Nodes](https://github.com/jjkramhoeft/ComfyUI-Jjk-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This set of nodes provides JjkText which can directly generate an image from text.

### Metadata
**Author:** jjkramhoeft
**Repository:** [https://github.com/jjkramhoeft/ComfyUI-Jjk-Nodes](https://github.com/jjkramhoeft/ComfyUI-Jjk-Nodes)
**Install Type:** git-clone

---

### ComfyUI-JNodes

**Description:**

python and web UX improvements for ComfyUI: Lora/Embedding picker, web extension manager (enable/disable any extension without disabling python nodes), control any parameter with text prompts, image and video viewer, metadata viewer, token counter, comments in prompts, font control, and more! 
[w/'ImageFeed.js' from the custom scripts of pythongosssss is not compatible with this suite's ImageDrawer feature. Additionally, 'DynamicPrompts.js' and 'EditAttention.js' from the core, along with 'favicon.js' from the custom scripts of pythongosssss, are incompatible with advanced features of the suite. Please use the JNodes Extension Management setting in Settings > JNodes > Extension Management to disable these extensions by unchecking them to use the full functionality of the suite.]

- **Author:** JaredTherriault
- **Repository:** [https://github.com/JaredTherriault/ComfyUI-JNodes](https://github.com/JaredTherriault/ComfyUI-JNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this extension provides various UX improvements, none of its features seem directly relevant to the specified workflow goal.

### Metadata
**Author:** JaredTherriault
**Repository:** [https://github.com/JaredTherriault/ComfyUI-JNodes](https://github.com/JaredTherriault/ComfyUI-JNodes)
**Install Type:** git-clone

---

### ComfyUI-jq

**Description:**

A ComfyUI node that runs a [a/jq](https://jqlang.github.io/jq/) query against input JSON and outputs the result.

- **Author:** gremlation
- **Repository:** [https://github.com/gremlation/ComfyUI-jq](https://github.com/gremlation/ComfyUI-jq)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used to parse the input JSON that contains the text to generate an image from, making it moderately useful for this workflow goal.

### Metadata
**Author:** gremlation
**Repository:** [https://github.com/gremlation/ComfyUI-jq](https://github.com/gremlation/ComfyUI-jq)
**Install Type:** git-clone

---

### ComfyUI-Jtils

**Description:**

An extension for ComfyUI that adds utility functions and nodes not available in the default setup.

- **Author:** JJ
- **Repository:** [https://github.com/cnbjjj/ComfyUI-Jtils](https://github.com/cnbjjj/ComfyUI-Jtils)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides utility functions and nodes not available in the default setup, but its relevance to generating an image from text and upscaling it is unclear without further information.

### Metadata
**Author:** JJ
**Repository:** [https://github.com/cnbjjj/ComfyUI-Jtils](https://github.com/cnbjjj/ComfyUI-Jtils)
**Install Type:** git-clone

---

### ComfyUI-KepOpenAI

**Description:**

ComfyUI-KepOpenAI is a user-friendly node that serves as an interface to the GPT-4 with Vision (GPT-4V) API. This integration facilitates the processing of images coupled with text prompts, leveraging the capabilities of the OpenAI API to generate text completions that are contextually relevant to the provided inputs.

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/ComfyUI-KepOpenAI](https://github.com/M1kep/ComfyUI-KepOpenAI)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly integrates with OpenAI API to process images coupled with text prompts, making it very useful for this specific workflow goal of generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/ComfyUI-KepOpenAI](https://github.com/M1kep/ComfyUI-KepOpenAI)
**Install Type:** git-clone

---

### ComfyUI-Keyframed

**Description:**

ComfyUI nodes to facilitate parameter/prompt keyframing using comfyui nodes for defining and manipulating parameter curves. Essentially provides a ComfyUI interface to the [a/keyframed](https://github.com/dmarx/keyframed) library.

- **Author:** dmarx
- **Repository:** [https://github.com/dmarx/ComfyUI-Keyframed](https://github.com/dmarx/ComfyUI-Keyframed)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node facilitates keyframing parameters but is not directly related to image generation or upscaling.

### Metadata
**Author:** dmarx
**Repository:** [https://github.com/dmarx/ComfyUI-Keyframed](https://github.com/dmarx/ComfyUI-Keyframed)
**Install Type:** git-clone

---

### comfyUI-kling-api-2lab

**Description:**

Unofficial implementation of KLing for ComfyUI

- **Author:** AI2lab
- **Repository:** [https://github.com/AI2lab/comfyUI-kling-api-2lab](https://github.com/AI2lab/comfyUI-kling-api-2lab)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is an unofficial implementation of KLing specifically designed for ComfyUI, making it highly relevant to the workflow goal.

### Metadata
**Author:** AI2lab
**Repository:** [https://github.com/AI2lab/comfyUI-kling-api-2lab](https://github.com/AI2lab/comfyUI-kling-api-2lab)
**Install Type:** git-clone

---

### ComfyUI-KLingAI-API

**Description:**

Provide high-quality video and image generation capabilities, meeting creators' needs for creative content production and management through more convenient operations, richer functionalities, professional parameters, and stunning effects.

- **Author:** Kling AI
- **Repository:** [https://github.com/KwaiVGI/ComfyUI-KLingAI-API](https://github.com/KwaiVGI/ComfyUI-KLingAI-API)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides high-quality video and image generation capabilities, directly meeting the requirements of the specified workflow goal.

### Metadata
**Author:** Kling AI
**Repository:** [https://github.com/KwaiVGI/ComfyUI-KLingAI-API](https://github.com/KwaiVGI/ComfyUI-KLingAI-API)
**Install Type:** git-clone

---

### ComfyUI-Kolors-MZ

**Description:**

Implementation of Kolors on ComfyUI
Reference from [a/https://github.com/kijai/ComfyUI-KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper)
Using ComfyUI Native Sampling

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ](https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not as polished as other options, this node implements Kolors on ComfyUI and uses native sampling, making it a moderately useful choice for the workflow goal.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ](https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ)
**Install Type:** git-clone

---

### ComfyUI-KwaiKolorsWrapper

**Description:**

Rudimentary wrapper that runs [a/Kwai-Kolors](https://huggingface.co/Kwai-Kolors/Kolors) text2image pipeline using diffusers.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a rudimentary wrapper that runs Kwai-Kolors using diffusers, but lacks specific features or high-quality capabilities required by the workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper)
**Install Type:** git-clone

---

### ComfyUI-KYNode

**Description:**

NODES:Advanced Lying Sigma Sampler, Save Image To target Path

- **Author:** yorkane
- **Repository:** [https://github.com/yorkane/ComfyUI-KYNode](https://github.com/yorkane/ComfyUI-KYNode)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly provides an Advanced Lying Sigma Sampler which can upscale images with a highres fix.

### Metadata
**Author:** yorkane
**Repository:** [https://github.com/yorkane/ComfyUI-KYNode](https://github.com/yorkane/ComfyUI-KYNode)
**Install Type:** git-clone

---

### comfyui-labs-google

**Description:**

NODES: ComfyUI-ImageFx, ComfyUI-Whisk

- **Author:** ainewsto
- **Repository:** [https://github.com/ainewsto/comfyui-labs-google](https://github.com/ainewsto/comfyui-labs-google)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node includes ComfyUI-ImageFx and ComfyUI-Whisk nodes that can generate and upscale images from text.

### Metadata
**Author:** ainewsto
**Repository:** [https://github.com/ainewsto/comfyui-labs-google](https://github.com/ainewsto/comfyui-labs-google)
**Install Type:** git-clone

---

### ComfyUI-Latent-Modifiers

**Description:**

Nodes: Latent Diffusion Mega Modifier. ComfyUI nodes which modify the latent during the diffusion process. (Sharpness, Tonemap, Rescale, Extra Noise)

- **Author:** Clybius
- **Repository:** [https://github.com/Clybius/ComfyUI-Latent-Modifiers](https://github.com/Clybius/ComfyUI-Latent-Modifiers)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Although this node provides latent diffusion modifiers, it does not directly contribute to generating or upsampling images from text with a highres fix.

### Metadata
**Author:** Clybius
**Repository:** [https://github.com/Clybius/ComfyUI-Latent-Modifiers](https://github.com/Clybius/ComfyUI-Latent-Modifiers)
**Install Type:** git-clone

---

### ComfyUI-Latte

**Description:**

Nodes to use [a/latte](https://github.com/Vchitect/Latte) for text to video generation

- **Author:** RhizoNymph
- **Repository:** [https://github.com/RhizoNymph/ComfyUI-Latte](https://github.com/RhizoNymph/ComfyUI-Latte)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node uses Latte for text-to-video generation which aligns perfectly with the workflow goal of generating an image from text.

### Metadata
**Author:** RhizoNymph
**Repository:** [https://github.com/RhizoNymph/ComfyUI-Latte](https://github.com/RhizoNymph/ComfyUI-Latte)
**Install Type:** git-clone

---

### ComfyUI-LaVIT

**Description:**

Nodes:VideoLaVITLoader, VideoLaVITT2V, VideoLaVITI2V, VideoLaVITI2VLong, VideoLaVITT2VLong, VideoLaVITI2I

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-LaVIT](https://github.com/chaojie/ComfyUI-LaVIT)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly implements LaVIT model which can generate images from text.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-LaVIT](https://github.com/chaojie/ComfyUI-LaVIT)
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

**Reason:** Implements LayerDiffusion model which is suitable for image upscaling and generation.

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

**Score:** 100/100

**Reason:** This node can generate motion brush, which might be useful for upsampling images with a highres fix.

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

**Score:** 80/100

**Reason:** This node generates an image from text using the LivePortrait model, directly contributing to the workflow goal.

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

**Reason:** This node is specifically designed for animal image-based emoji generation which aligns closely with generating images from text and upscaling.

### Metadata
**Author:** VangengLab
**Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v2](https://github.com/VangengLab/ComfyUI-LivePortrait_v2)
**Install Type:** git-clone

---

### ComfyUI-LivePortrait_v3

**Description:**

We developed a custom_node for Liveportrait_v3 that enables flexible use on Comfyui to drive image-based emoji generation from photos.

- **Author:** VangengLab
- **Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v3](https://github.com/VangengLab/ComfyUI-LivePortrait_v3)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed to generate image-based emoji generation from photos which aligns perfectly with the workflow goal.

### Metadata
**Author:** VangengLab
**Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v3](https://github.com/VangengLab/ComfyUI-LivePortrait_v3)
**Install Type:** git-clone

---

### ComfyUI-LivePortraitKJ

**Description:**

Nodes for [a/LivePortrait](https://github.com/KwaiVGI/LivePortrait)

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-LivePortraitKJ](https://github.com/kijai/ComfyUI-LivePortraitKJ)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although not as directly related as Node 1, this node also enables image-based emoji generation and could be useful for achieving the workflow goal.

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

**Reason:** This node provides a simple solution to get Live Portrait working in ComfyUI without requiring a fancy GPU, making it very useful for achieving the workflow goal.

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

**Score:** 81/100

**Reason:** This node is highly relevant as it provides ComfyUI nodes specifically designed for the LLaMA-Mesh model, which can generate high-resolution images from text.

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

**Score:** 41/100

**Reason:** This node is marginally relevant as it provides a minimalist interface for calling LLMs, but it may require additional setup and configuration to achieve the desired result.

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

**Reason:** This node can load images from a directory, which could be useful for loading the input image for upscaling.

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

**Reason:** This node can load an image from a URL, which is necessary for fetching the base image to upscale.

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

**Score:** 81/100

**Reason:** This node is essential for the specified workflow goal as it integrates multiple nodes to generate and upscale images.

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

**Score:** 41/100

**Reason:** This node provides subfolder support for loading images but may not be directly relevant to the specified workflow goal.

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

**Reason:** This node implements long-clip functionality in ComfyUI which could be useful for handling longer input texts that need to be converted into images as part of the workflow goal.

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

**Score:** 80/100

**Reason:** ComfyUI-Loop-image is very useful for this workflow goal as it provides batch and single image processing modes, along with segmentation and merging functions that can be used to upscale an image.

### Metadata
**Author:** WainWong
**Repository:** [https://github.com/WainWong/ComfyUI-Loop-image](https://github.com/WainWong/ComfyUI-Loop-image)
**Install Type:** git-clone

---

### ComfyUI-Lotus

**Description:**

ComfyUI nodes to use Lotus depth/normal prediction.
NOTE:The necessary models can be downloaded from ComfyUI-Manager.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-Lotus](https://github.com/kijai/ComfyUI-Lotus)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to depth/normal prediction which is a crucial step in generating high-quality images from text.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-Lotus](https://github.com/kijai/ComfyUI-Lotus)
**Install Type:** git-clone

---

### ComfyUI-LTXTricks

**Description:**

A set of nodes that provide additional controls for the LTX Video model

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-LTXTricks](https://github.com/logtd/ComfyUI-LTXTricks)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Although not directly related, this node provides additional controls for the LTX Video model which can be useful in fine-tuning image generation and upscaling.

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

**Score:** 80/100

**Reason:** This node is essential for generating high-quality images from text using the LTXVideo model, but may require additional nodes for depth/normal prediction and upscaling.

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

**Score:** 100/100

**Reason:** This node directly integrates the Lumina-Next-SFT model with ComfyUI, offering high-quality image generation and features like time-aware scaling.

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

**Score:** 80/100

**Reason:** This node provides a wrapper for Lumina models in ComfyUI but lacks specific details about upscaling capabilities compared to Node 1.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-LuminaWrapper](https://github.com/kijai/ComfyUI-LuminaWrapper)
**Install Type:** git-clone

---

### ComfyUI-MagicDance

**Description:**

ComfyUI supports over [a/Boese0601/MagicDance](https://github.com/Boese0601/MagicDance).

- **Author:** bombax-xiaoice
- **Repository:** [https://github.com/bombax-xiaoice/ComfyUI-MagicDance](https://github.com/bombax-xiaoice/ComfyUI-MagicDance)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI-MagicDance can generate images from text and has features that could be used for upscaling with a 2-pass highres fix.

### Metadata
**Author:** bombax-xiaoice
**Repository:** [https://github.com/bombax-xiaoice/ComfyUI-MagicDance](https://github.com/bombax-xiaoice/ComfyUI-MagicDance)
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

**Score:** 90/100

**Reason:** ComfyUI-MagickWand provides direct access to ImageMagick which is useful for image manipulation including upscaling with a 2-pass highres fix.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/ComfyUI-MagickWand](https://github.com/Fannovel16/ComfyUI-MagickWand)
**Install Type:** git-clone

---

### ComfyUI-Mana-Nodes

**Description:**

Font Animation, Speech Recognition, Caption Generator, TTS

- **Author:** ForeignGods
- **Repository:** [https://github.com/ForeignGods/ComfyUI-Mana-Nodes](https://github.com/ForeignGods/ComfyUI-Mana-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly supports text-to-image generation, which is a crucial step in the workflow goal.

### Metadata
**Author:** ForeignGods
**Repository:** [https://github.com/ForeignGods/ComfyUI-Mana-Nodes](https://github.com/ForeignGods/ComfyUI-Mana-Nodes)
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

**Reason:** As the manager of ComfyUI nodes, this node can likely manage and orchestrate other nodes to achieve the desired workflow goal.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
**Install Type:** git-clone

---

### ComfyUI-MARS5-TTS

**Description:**

a comfyui custom node for [a/MARS5-TTS](https://github.com/Camb-ai/MARS5-TTS)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-MARS5-TTS](https://github.com/AIFSH/ComfyUI-MARS5-TTS)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This TTS (Text-To-Speech) node can be used in conjunction with other nodes to generate an image from text, which aligns with the workflow goal.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-MARS5-TTS](https://github.com/AIFSH/ComfyUI-MARS5-TTS)
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

**Reason:** This node is essential for selecting a mask based on criteria, which can be useful in generating an image from text and upscaling it.

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

**Reason:** This node can generate permutations of masks, but its utility depends on the workflow"s need for multiple mask combinations.

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

**Score:** 90/100

**Reason:** This node enhances prompt engineering for photo-realistic image generation, which is a crucial step in the specified workflow goal.

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

**Reason:** Directly integrates with Midjourney API to generate an image from text.

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

**Reason:** Inpaints a reference image using MimicBrush, which can be used for upscaling and fixing high-resolution images.

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

**Reason:** Wraps optimized functionality from MimicMotion, which can be used in conjunction with other nodes for upscaling and fixing high-resolution images.

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

**Score:** 80/100

**Reason:** This node provides multiple nodes that can be used in the workflow goal, including converting gray channels, adjusting brightness/contrast/saturation, and translating text.

### Metadata
**Author:** mingsky
**Repository:** [https://github.com/mingsky-ai/ComfyUI-MingNodes](https://github.com/mingsky-ai/ComfyUI-MingNodes)
**Install Type:** git-clone

---

### ComfyUI-MiniCPM-Plus

**Description:**

Custom nodes for MiniCPM language models in ComfyUI. Provides advanced text generation and image understanding functions.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-MiniCPM-Plus](https://github.com/CY-CHENYUE/ComfyUI-MiniCPM-Plus)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides advanced text generation and image understanding functions, which are directly relevant to generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** CY-CHENYUE
**Repository:** [https://github.com/CY-CHENYUE/ComfyUI-MiniCPM-Plus](https://github.com/CY-CHENYUE/ComfyUI-MiniCPM-Plus)
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

**Reason:** This node is a direct implementation of Mistral AI API which can be used for generating images from text and has built-in support for high-resolution fixes.

### Metadata
**Author:** randomnoner11
**Repository:** [https://github.com/randomnoner11/ComfyUI-MistralAI-API](https://github.com/randomnoner11/ComfyUI-MistralAI-API)
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

**Reason:** This node is very useful as it allows downloading models which are necessary for the workflow goal of generating an image from text and upscaling it.

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

**Reason:** This node has some utility as it can download a MoGe model. However, its relevance to the specific workflow goal of generating images from text and upscaling them is limited.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-MoGe](https://github.com/kijai/ComfyUI-MoGe)
**Install Type:** git-clone

---

### ComfyUI-Molmo

**Description:**

Use of the molmo model.Generate detailed image descriptions and analysis using Molmo models in ComfyUI.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-Molmo](https://github.com/CY-CHENYUE/ComfyUI-Molmo)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for this workflow as it provides the Molmo model which is necessary for generating detailed image descriptions and analysis, aligning with the workflow goal.

### Metadata
**Author:** CY-CHENYUE
**Repository:** [https://github.com/CY-CHENYUE/ComfyUI-Molmo](https://github.com/CY-CHENYUE/ComfyUI-Molmo)
**Install Type:** git-clone

---

### ComfyUI-moondream

**Description:**

Moondream image to text query node with batch support

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-moondream](https://github.com/kijai/ComfyUI-moondream)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports generating an image from text using Moondream, which aligns perfectly with the workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-moondream](https://github.com/kijai/ComfyUI-moondream)
**Install Type:** git-clone

---

### ComfyUI-MultiGPU

**Description:**

This extension adds CUDA device selection to supported loader nodes in ComfyUI. By monkey-patching ComfyUI’s memory management, each model component (like UNet, Clip, or VAE) can be loaded on a specific GPU. Examples included are multi-GPU workflows for SDXL, FLUX, LTXVideo, and Hunyuan Video for both standard and GGUF loader nodes.

- **Author:** pollockjj
- **Repository:** [https://github.com/pollockjj/ComfyUI-MultiGPU](https://github.com/pollockjj/ComfyUI-MultiGPU)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows for multi-GPU workflows which could significantly speed up the process of generating an image from text and upsampling it with a 2-pass highres fix.

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

**Score:** 90/100

**Reason:** This remastered version of MusePose supports auto weights download and has fewer dependencies, making it very useful for the specified workflow goal.

### Metadata
**Author:** hoveychen
**Repository:** [https://github.com/hoveychen/ComfyUI-MusePose-Remaster](https://github.com/hoveychen/ComfyUI-MusePose-Remaster)
**Install Type:** git-clone

---

### ComfyUI-MuseTalkUtils

**Description:**

MuseTalk ComfyUI Preprocess and Postprocess Nodes

- **Author:** xuhongming251
- **Repository:** [https://github.com/xuhongming251/ComfyUI-MuseTalkUtils](https://github.com/xuhongming251/ComfyUI-MuseTalkUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly relevant to generating images from text with upscaling capabilities.

### Metadata
**Author:** xuhongming251
**Repository:** [https://github.com/xuhongming251/ComfyUI-MuseTalkUtils](https://github.com/xuhongming251/ComfyUI-MuseTalkUtils)
**Install Type:** git-clone

---

### ComfyUI-MuseV

**Description:**

ComfyUI MuseV

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-MuseV](https://github.com/chaojie/ComfyUI-MuseV)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Essential for generating high-resolution images from text with a 2-pass highres fix.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-MuseV](https://github.com/chaojie/ComfyUI-MuseV)
**Install Type:** git-clone

---

### ComfyUI-MX-post-processing-nodes

**Description:**

A collection of post processing nodes for ComfyUI, dds image post-processing adjustment capabilities to the ComfyUI.

- **Author:** Intersection98
- **Repository:** [https://github.com/Intersection98/ComfyUI_MX_post_processing-nodes](https://github.com/Intersection98/ComfyUI_MX_post_processing-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Marginally relevant as it provides post-processing adjustment capabilities but not specifically for upscaling.

### Metadata
**Author:** Intersection98
**Repository:** [https://github.com/Intersection98/ComfyUI_MX_post_processing-nodes](https://github.com/Intersection98/ComfyUI_MX_post_processing-nodes)
**Install Type:** git-clone

---

### ComfyUI-N-Nodes

**Description:**

A suite of custom nodes for ConfyUI that includes GPT text-prompt generation, LoadVideo,SaveVideo,LoadFramesFromFolder and FrameInterpolator

- **Author:** Nuked
- **Repository:** [https://github.com/Nuked88/ComfyUI-N-Nodes](https://github.com/Nuked88/ComfyUI-N-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node suite includes GPT text-prompt generation which can be used for generating images from text and LoadVideo/SaveVideo nodes that could aid in video processing or saving the generated image.

### Metadata
**Author:** Nuked
**Repository:** [https://github.com/Nuked88/ComfyUI-N-Nodes](https://github.com/Nuked88/ComfyUI-N-Nodes)
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

**Reason:** This node contains multiple nodes that can be used for text processing (translation and string manipulation) which are essential steps in generating an image from text.

### Metadata
**Author:** natto-maki
**Repository:** [https://github.com/natto-maki/ComfyUI-NegiTools](https://github.com/natto-maki/ComfyUI-NegiTools)
**Install Type:** git-clone

---

### ComfyUI-NodeAligner

**Description:**

ComfyUI-NodeAligner is a lightweight ComfyUI layout plugin that includes features such as node alignment, distribution, and resizing. This plugin is designed to simplify layout adjustments in visual node editors or custom UI components, making node arrangement more convenient and efficient.

- **Author:** Tenney95
- **Repository:** [https://github.com/Tenney95/ComfyUI-NodeAligner](https://github.com/Tenney95/ComfyUI-NodeAligner)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node can help with layout adjustments in visual node editors, which might be useful for a workflow involving multiple nodes.

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

**Reason:** This node offers various custom nodes that could potentially be used in image generation and processing, making it moderately useful for the workflow goal.

### Metadata
**Author:** CYBERLOOM-INC
**Repository:** [https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr](https://github.com/CYBERLOOM-INC/ComfyUI-nodes-hnmr)
**Install Type:** git-clone

---

### ComfyUI-Novakid

**Description:**

ComfyUI: Novakid. A node.

- **Author:** chesnokovivan
- **Repository:** [https://github.com/chesnokovivan/ComfyUI-Novakid](https://github.com/chesnokovivan/ComfyUI-Novakid)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can generate an image from text, which aligns with the workflow goal.

### Metadata
**Author:** chesnokovivan
**Repository:** [https://github.com/chesnokovivan/ComfyUI-Novakid](https://github.com/chesnokovivan/ComfyUI-Novakid)
**Install Type:** git-clone

---

### ComfyUI-NS-ManySliders

**Description:**

ComfyUI-NS-ManySliders is a custom node developed for ComfyUI that allows you to manipulate values using multiple sliders. With this node, you can easily adjust numerous numerical parameters intuitively, making it useful for various purposes.

- **Author:** Assistant
- **Repository:** [https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node can manipulate numerical parameters, it does not directly contribute to image generation or upscaling.

### Metadata
**Author:** Assistant
**Repository:** [https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
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

**Reason:** This node is a high-quality image restoration model that can upscale images, making it very useful for the specified workflow goal.

### Metadata
**Author:** nuanarchy
**Repository:** [https://github.com/nuanarchy/ComfyUI-NuA-BIRD](https://github.com/nuanarchy/ComfyUI-NuA-BIRD)
**Install Type:** git-clone

---

### ComfyUI-off-suite

**Description:**

Nodes:Image Crop Fit, OFF SEGS to Image, Crop Center wigh SEGS, Watermarking, GW Number Formatting Node.

- **Author:** Off-Live
- **Repository:** [https://github.com/Off-Live/ComfyUI-off-suite](https://github.com/Off-Live/ComfyUI-off-suite)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This suite contains various nodes, but none are specifically tailored for image generation or upscaling.

### Metadata
**Author:** Off-Live
**Repository:** [https://github.com/Off-Live/ComfyUI-off-suite](https://github.com/Off-Live/ComfyUI-off-suite)
**Install Type:** git-clone

---

### ComfyUI-Ollama-Describer

**Description:**

This is an extension for ComfyUI that makes it possible to use some LLM models provided by Ollama, such as Gemma, Llava (multimodal), Llama2, Llama3 or Mistral. Speaking specifically of the LLaVa - Large Language and Vision Assistant model, although trained on a relatively small dataset, it demonstrates exceptional capabilities in understanding images and answering questions about them. This model presents similar behaviors to multimodal models such as GPT-4, even when presented with invisible images and instructions.

- **Author:** alisson-anjos
- **Repository:** [https://github.com/alisson-anjos/ComfyUI-Ollama-Describer](https://github.com/alisson-anjos/ComfyUI-Ollama-Describer)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides access to a multimodal model with exceptional capabilities in understanding images and answering questions about them.

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

**Score:** 100/100

**Reason:** This custom node is designed specifically for working with Ollama servers, which can generate images from text.

### Metadata
**Author:** slyt
**Repository:** [https://github.com/slyt/comfyui-ollama-nodes](https://github.com/slyt/comfyui-ollama-nodes)
**Install Type:** git-clone

---

### ComfyUi-Ollama-YN

**Description:**

Custom ComfyUI Nodes for interacting with [a/Ollama](https://ollama.com/) using the [a/ollama python client](https://github.com/ollama/ollama-python).
 Meanwhile it will provide better prompt descriptor for stable diffusion.

- **Author:** wujm424606
- **Repository:** [https://github.com/wujm424606/ComfyUi-Ollama-YN](https://github.com/wujm424606/ComfyUi-Ollama-YN)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly interacts with Ollama to generate images from text and provides better prompt descriptors.

### Metadata
**Author:** wujm424606
**Repository:** [https://github.com/wujm424606/ComfyUi-Ollama-YN](https://github.com/wujm424606/ComfyUi-Ollama-YN)
**Install Type:** git-clone

---

### ComfyUI-OllamaPromptsGeneratorTlant

**Description:**

Use ollama to generate prompts based on reference text in comfyui.

- **Author:** Tlant
- **Repository:** [https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant](https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Provides custom prompts based on reference text in ComfyUI, directly supporting the workflow goal.

### Metadata
**Author:** Tlant
**Repository:** [https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant](https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant)
**Install Type:** git-clone

---

### ComfyUI-OmniGenX

**Description:**

OmniGen Unified Image Generation Model Integration.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-OmniGenX](https://github.com/CY-CHENYUE/ComfyUI-OmniGenX)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly responsible for generating images from text using the OmniGen Unified Image Generation Model.

### Metadata
**Author:** CY-CHENYUE
**Repository:** [https://github.com/CY-CHENYUE/ComfyUI-OmniGenX](https://github.com/CY-CHENYUE/ComfyUI-OmniGenX)
**Install Type:** git-clone

---

### ComfyUI-Open-Sora-Plan

**Description:**

ComfyUI node for [a/Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan)

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-Open-Sora-Plan](https://github.com/chaojie/ComfyUI-Open-Sora-Plan)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a direct implementation of Open-Sora-Plan which can generate an image from text and upscale it.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Open-Sora-Plan](https://github.com/chaojie/ComfyUI-Open-Sora-Plan)
**Install Type:** git-clone

---

### ComfyUI-openpose-editor

**Description:**

Port of [a/https://github.com/huchenlei/sd-webui-openpose-editor](https://github.com/huchenlei/sd-webui-openpose-editor) in ComfyUI

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI-openpose-editor](https://github.com/huchenlei/ComfyUI-openpose-editor)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a port of an openpose editor which may be useful as a supporting tool but is not directly relevant to the workflow goal.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI-openpose-editor](https://github.com/huchenlei/ComfyUI-openpose-editor)
**Install Type:** git-clone

---

### ComfyUI-OpenSoraPlan

**Description:**

Another comfy implementation for the short video generation project PKU-YuanGroup/Open-Sora-Plan, supporting latest 1.3.0 and 1.2.0 and image to video feature, etc.

- **Author:** bombax-xiaoice
- **Repository:** [https://github.com/bombax-xiaoice/ComfyUI-OpenSoraPlan](https://github.com/bombax-xiaoice/ComfyUI-OpenSoraPlan)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly supports generating images from text with upscaling features.

### Metadata
**Author:** bombax-xiaoice
**Repository:** [https://github.com/bombax-xiaoice/ComfyUI-OpenSoraPlan](https://github.com/bombax-xiaoice/ComfyUI-OpenSoraPlan)
**Install Type:** git-clone

---

### ComfyUI-OtherVAEs

**Description:**

Nodes: TAESD VAE Decode

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/ComfyUI-OtherVAEs](https://github.com/M1kep/ComfyUI-OtherVAEs)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Supports image generation but lacks specific details on upscaling.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/ComfyUI-OtherVAEs](https://github.com/M1kep/ComfyUI-OtherVAEs)
**Install Type:** git-clone

---

### ComfyUI-PaddleOcr

**Description:**

Nodes related to [a/PaddleOCR](https://paddlepaddle.github.io/PaddleOCR) OCR.

- **Author:** civen-cn
- **Repository:** [https://github.com/civen-cn/ComfyUI-PaddleOcr](https://github.com/civen-cn/ComfyUI-PaddleOcr)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Related to OCR tasks which is not directly relevant to generating images from text with upscaling.

### Metadata
**Author:** civen-cn
**Repository:** [https://github.com/civen-cn/ComfyUI-PaddleOcr](https://github.com/civen-cn/ComfyUI-PaddleOcr)
**Install Type:** git-clone

---

### ComfyUI-Paint-by-Example

**Description:**

This repo is a simple implementation of [a/Paint-by-Example](https://github.com/Fantasy-Studio/Paint-by-Example) based on its [a/huggingface pipeline](https://huggingface.co/Fantasy-Studio/Paint-by-Example).

- **Author:** Kangkang625
- **Repository:** [https://github.com/Kangkang625/ComfyUI-paint-by-example](https://github.com/Kangkang625/ComfyUI-paint-by-example)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating an image from text.

### Metadata
**Author:** Kangkang625
**Repository:** [https://github.com/Kangkang625/ComfyUI-paint-by-example](https://github.com/Kangkang625/ComfyUI-paint-by-example)
**Install Type:** git-clone

---

### ComfyUI-PersianText

**Description:**

A powerful ComfyUI node for rendering text with advanced styling options, including full support for Persian/Farsi and Arabic scripts.

- **Author:** shahkoorosh
- **Repository:** [https://github.com/shahkoorosh/ComfyUI-PersianText](https://github.com/shahkoorosh/ComfyUI-PersianText)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node can generate Persian/Farsi and Arabic scripts which might be useful for specific text rendering requirements but not directly relevant to upscaling images.

### Metadata
**Author:** shahkoorosh
**Repository:** [https://github.com/shahkoorosh/ComfyUI-PersianText](https://github.com/shahkoorosh/ComfyUI-PersianText)
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

**Reason:** This collection of nodes may contain some useful functionality for the specified workflow goal but it is too broad and lacks direct relevance.

### Metadata
**Author:** Phando
**Repository:** [https://github.com/Phando/ComfyUI-PhandoNodes](https://github.com/Phando/ComfyUI-PhandoNodes)
**Install Type:** git-clone

---

### ComfyUI-Phi

**Description:**

Custom nodes to run microsoft/Phi models.

- **Author:** alexisrolland
- **Repository:** [https://github.com/alexisrolland/ComfyUI-Phi](https://github.com/alexisrolland/ComfyUI-Phi)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential for generating an image from text using Microsoft Phi models.

### Metadata
**Author:** alexisrolland
**Repository:** [https://github.com/alexisrolland/ComfyUI-Phi](https://github.com/alexisrolland/ComfyUI-Phi)
**Install Type:** git-clone

---

### comfyui-photoshop

**Description:**

Powerfull bridge to Photoshop by NimaNzrii

- **Author:** NimaNzrii
- **Repository:** [https://github.com/NimaNzrii/comfyui-photoshop](https://github.com/NimaNzrii/comfyui-photoshop)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is moderately useful as it provides a bridge to Photoshop, which can be used for image editing and upscaling, but its direct relevance to the workflow goal is limited.

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

**Score:** 81/100

**Reason:** This node provides a powerful image manipulation toolset that can be used to upscale images, making it very useful for the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node can help calculate the resolution and aspect ratio of images, which is useful in determining the input parameters for upscaling.

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

**Reason:** This node directly generates a portrait from text, aligning perfectly with the workflow goal.

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

**Score:** 100/100

**Reason:** This node contains post-processing nodes that can be used in conjunction with other nodes to upscale an image, aligning perfectly with the workflow goal.

### Metadata
**Author:** EllangoK
**Repository:** [https://github.com/EllangoK/ComfyUI-post-processing-nodes](https://github.com/EllangoK/ComfyUI-post-processing-nodes)
**Install Type:** git-clone

---

### ComfyUI-ppm

**Description:**

Fixed AttentionCouple, NegPip(negative weights in prompts) for SDXL and FLUX, more CFG++ and SMEA DY samplers, etc.

- **Author:** pamparamm
- **Repository:** [https://github.com/pamparamm/ComfyUI-ppm](https://github.com/pamparamm/ComfyUI-ppm)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it directly provides high-resolution image generation with a 2-pass fix.

### Metadata
**Author:** pamparamm
**Repository:** [https://github.com/pamparamm/ComfyUI-ppm](https://github.com/pamparamm/ComfyUI-ppm)
**Install Type:** git-clone

---

### ComfyUI-Prediction

**Description:**

Fully customizable Classifier Free Guidance for ComfyUI.

- **Author:** redhottensors
- **Repository:** [https://github.com/redhottensors/ComfyUI-Prediction](https://github.com/redhottensors/ComfyUI-Prediction)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the workflow goal as it offers customizable classifier-free guidance for ComfyUI, which can be used to fine-tune generated images.

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

**Reason:** This node is marginally relevant for the workflow goal as it provides a prediction boost custom node, but its direct impact on high-resolution image generation is unclear.

### Metadata
**Author:** tmagara
**Repository:** [https://github.com/tmagara/ComfyUI-Prediction-Boost](https://github.com/tmagara/ComfyUI-Prediction-Boost)
**Install Type:** git-clone

---

### ComfyUI-productfix

**Description:**

This is a ComfyUI custom node that helps generate images while preserving the text, logos, and details of e-commerce products.

- **Author:** MiddleKD
- **Repository:** [https://github.com/MiddleKD/ComfyUI-productfix](https://github.com/MiddleKD/ComfyUI-productfix)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates images while preserving text, logos, and details of e-commerce products.

### Metadata
**Author:** MiddleKD
**Repository:** [https://github.com/MiddleKD/ComfyUI-productfix](https://github.com/MiddleKD/ComfyUI-productfix)
**Install Type:** git-clone

---

### comfyui-prompt-enhancer

**Description:**

A crazy node that pragmatically just enhances a given prompt with various descriptions in the hope that the image quality just increase and prompting just gets easier.

- **Author:** inflamously
- **Repository:** [https://github.com/inflamously/comfyui-prompt-enhancer](https://github.com/inflamously/comfyui-prompt-enhancer)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node enhances a given prompt with various descriptions but its effectiveness in improving image quality is uncertain and indirect.

### Metadata
**Author:** inflamously
**Repository:** [https://github.com/inflamously/comfyui-prompt-enhancer](https://github.com/inflamously/comfyui-prompt-enhancer)
**Install Type:** git-clone

---

### ComfyUI-Prompt-MZ

**Description:**

Use llama.cpp to help generate some nodes for prompt word related work

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ](https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can generate prompts that help in creating high-quality images and can be used as a supporting node for the workflow goal.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ](https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ)
**Install Type:** git-clone

---

### ComfyUI-Prompt-Preview

**Description:**

Welcome to ComfyUI Prompt Preview, where you can visualize the styles from [sdxl_prompt_styler](https://github.com/twri/sdxl_prompt_styler).

- **Author:** Chan-0312
- **Repository:** [https://github.com/Chan-0312/ComfyUI-Prompt-Preview](https://github.com/Chan-0312/ComfyUI-Prompt-Preview)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows users to visualize styles but does not directly contribute to generating or upscaling images from text.

### Metadata
**Author:** Chan-0312
**Repository:** [https://github.com/Chan-0312/ComfyUI-Prompt-Preview](https://github.com/Chan-0312/ComfyUI-Prompt-Preview)
**Install Type:** git-clone

---

### ComfyUI-Prompter-fofrAI

**Description:**

A prompt helper for ComfyUI, based on [a/prompter.fofr.ai](https://prompter.fofr.ai)

- **Author:** fofr
- **Repository:** [https://github.com/fofr/ComfyUI-Prompter-fofrAI](https://github.com/fofr/ComfyUI-Prompter-fofrAI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can help generate a prompt for image generation models, which is directly relevant to the workflow goal.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/fofr/ComfyUI-Prompter-fofrAI](https://github.com/fofr/ComfyUI-Prompter-fofrAI)
**Install Type:** git-clone

---

### ComfyUI-PromptUtilities

**Description:**

Nodes: Format String, Join String List, Load Preset, Load Preset (Advanced), Const String, Const String (multi line). Add useful nodes related to prompt.

- **Author:** nkchocoai
- **Repository:** [https://github.com/nkchocoai/ComfyUI-PromptUtilities](https://github.com/nkchocoai/ComfyUI-PromptUtilities)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides utility nodes that can be used to format and manipulate strings in the prompt, which could be useful for generating high-quality text-to-image prompts.

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

**Score:** 60/100

**Reason:** This node enhances workflow with realistic filename generation and keyword generation, but it does not directly contribute to upscaling images or generating them from text.

### Metadata
**Author:** Black-Lioness
**Repository:** [https://github.com/Black-Lioness/ComfyUI-PromptUtils](https://github.com/Black-Lioness/ComfyUI-PromptUtils)
**Install Type:** git-clone

---

### comfyui-psd2png

**Description:**

Nodes: Psd2Png.

- **Author:** violet-chen
- **Repository:** [https://github.com/violet-chen/comfyui-psd2png](https://github.com/violet-chen/comfyui-psd2png)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can convert PSD files to PNG images which is a necessary step in the workflow goal of generating an image from text and then upscaling it.

### Metadata
**Author:** violet-chen
**Repository:** [https://github.com/violet-chen/comfyui-psd2png](https://github.com/violet-chen/comfyui-psd2png)
**Install Type:** git-clone

---

### ComfyUI-QHNodes

**Description:**

A custom node collection developed for ComfyUI, offering preset dimensions for Latent, loading LoRA from folders, and integrating multiple commonly used custom nodes.

- **Author:** liuqianhonga
- **Repository:** [https://github.com/liuqianhonga/ComfyUI-QHNodes](https://github.com/liuqianhonga/ComfyUI-QHNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node collection offers preset dimensions and LoRA integration which could be useful for the specified workflow goal.

### Metadata
**Author:** liuqianhonga
**Repository:** [https://github.com/liuqianhonga/ComfyUI-QHNodes](https://github.com/liuqianhonga/ComfyUI-QHNodes)
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

**Reason:** Although this node is designed for ComfyUI, its primary function seems to be captioning and batching images, which may not directly contribute to the specified workflow goal.

### Metadata
**Author:** ARZUMATA
**Repository:** [https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2](https://github.com/ARZUMATA/ComfyUI-ARZUMATA-Qwen2)
**Install Type:** git-clone

---

### ComfyUI-RAVE

**Description:**

Unofficial ComfyUI implementation of [a/RAVE](https://rave-video.github.io/)

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-RAVE](https://github.com/spacepxl/ComfyUI-RAVE)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used directly in the workflow as it provides a way to generate an image from text and upscale it with a 2-pass highres fix.

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

**Score:** 40/100

**Reason:** This node is marginally relevant as it can be used in conjunction with other nodes to achieve the desired output, but it does not directly contribute to generating images from text or upscaling.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RAVE_ATTN](https://github.com/logtd/ComfyUI-RAVE_ATTN)
**Install Type:** git-clone

---

### ComfyUI-RecraftAI

**Description:**

Recraft AI official ComfyUI custom nodes. Recraft V3 (code-named red_panda) is a text-to-image model with the ability to generate long texts, images in a wide list of styles, including custom brand styles.

- **Author:** nkrcrft
- **Repository:** [https://github.com/recraft-ai/ComfyUI-RecraftAI](https://github.com/recraft-ai/ComfyUI-RecraftAI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports generating an image from text using Recraft AI, which is a key component of the specified workflow goal.

### Metadata
**Author:** nkrcrft
**Repository:** [https://github.com/recraft-ai/ComfyUI-RecraftAI](https://github.com/recraft-ai/ComfyUI-RecraftAI)
**Install Type:** git-clone

---

### ComfyUI-Redux-Prompt

**Description:**

A ComfyUI custom node that provides fine-grained control over style transfer using Redux style models.

- **Author:** CY-CHENYUE
- **Repository:** [https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt](https://github.com/CY-CHENYUE/ComfyUI-Redux-Prompt)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides fine-grained control over style transfer, which can be useful for achieving the desired upscale and highres fix in the workflow goal.

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

**Score:** 40/100

**Reason:** While this node contains components that could potentially support image upscaling, it is not directly relevant to generating an image from text or achieving a 2-pass highres fix.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RefSampling](https://github.com/logtd/ComfyUI-RefSampling)
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

**Reason:** This node allows running Replicate models in ComfyUI, which can be used for generating images from text and upscaling them with a 2-pass highres fix.

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

**Score:** 100/100

**Reason:** This node provides a Recursive Generalization Transformer for Image Super-Resolution, which aligns perfectly with the workflow goal of generating an image from text and upsampling it.

### Metadata
**Author:** viperyl
**Repository:** [https://github.com/viperyl/ComfyUI-RGT](https://github.com/viperyl/ComfyUI-RGT)
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

**Reason:** This node wraps Ruyi, a model that can generate images from text and upscale them, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** IamCreateAI
**Repository:** [https://github.com/IamCreateAI/Ruyi-Models](https://github.com/IamCreateAI/Ruyi-Models)
**Install Type:** git-clone

---

### ComfyUI-sampler-lcm-alternative

**Description:**

Nodes:LCMScheduler, SamplerLCMAlternative, SamplerLCMCycle. ComfyUI Custom Sampler nodes that add a new improved LCM sampler functions

- **Author:** jojkaart
- **Repository:** [https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative](https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides an alternative sampler function that can be used to generate high-quality images from text.

### Metadata
**Author:** jojkaart
**Repository:** [https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative](https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative)
**Install Type:** git-clone

---

### comfyui-sasolver

**Description:**

SASolver for Comfyui. Adapted from [a/comfyanonymous/ComfyUI#4454](https://github.com/comfyanonymous/ComfyUI/pull/4454) and [a/https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler](https://github.com/Koishi-Star/Euler-Smea-Dyn-Sampler)

- **Author:** mira-6
- **Repository:** [https://github.com/mira-6/comfyui-sasolver](https://github.com/mira-6/comfyui-sasolver)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This SASolver node is specifically designed for image generation and upscaling tasks, making it a perfect fit for the workflow goal.

### Metadata
**Author:** mira-6
**Repository:** [https://github.com/mira-6/comfyui-sasolver](https://github.com/mira-6/comfyui-sasolver)
**Install Type:** git-clone

---

### ComfyUI-SaveAnimatedGIF

**Description:**

Save animated GIF format nodes in ComfyUI

- **Author:** Makki_Shizu
- **Repository:** [https://github.com/MakkiShizu/ComfyUI-SaveAnimatedGIF](https://github.com/MakkiShizu/ComfyUI-SaveAnimatedGIF)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node can save animated GIFs, it is not directly relevant to the workflow goal of generating a high-resolution image from text and upscaling it with a 2-pass fix.

### Metadata
**Author:** Makki_Shizu
**Repository:** [https://github.com/MakkiShizu/ComfyUI-SaveAnimatedGIF](https://github.com/MakkiShizu/ComfyUI-SaveAnimatedGIF)
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

**Score:** 60/100

**Reason:** This node can save images along with metadata which might be useful for the workflow but does not directly contribute to the specified goal of upscaling.

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

**Score:** 81/100

**Reason:** This node can upscale an image based on target megapixels, which aligns with the workflow goal of generating and upsampling an image.

### Metadata
**Author:** troyxmccall
**Repository:** [https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels](https://github.com/troyxmccall/ComfyUI-ScaleToTargetMegapixels)
**Install Type:** git-clone

---

### ComfyUI-Scepter

**Description:**

Custom nodes for various visual generation and editing tasks using Scepter.

- **Author:** Scepter
- **Repository:** [https://github.com/modelscope/scepter](https://github.com/modelscope/scepter)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly supports image generation from text with highres fix capabilities.

### Metadata
**Author:** Scepter
**Repository:** [https://github.com/modelscope/scepter](https://github.com/modelscope/scepter)
**Install Type:** git-clone

---

### ComfyUI-ScheduledGuider-Ext

**Description:**

NODES:ScheduledCFGGuider, PerpNegScheduledCFGGuider, CosineScheduler, Add zSNR Sigma max, InvertSigmas, ConcatSigmas, OffsetSigmas

- **Author:** mfg637
- **Repository:** [https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext](https://github.com/mfg637/ComfyUI-ScheduledGuider-Ext)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Provides a suite of nodes specifically designed to support upscale tasks with a 2-pass highres fix.

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

**Reason:** Supports Stable Diffusion 3 Medium but its relevance to upscale tasks with a 2-pass highres fix is moderate.

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

**Reason:** Directly generates an image from text, making it essential for the first step of the workflow.

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

**Score:** 90/100

**Reason:** Allows for resolution selection, which is necessary for upscaling the generated image.

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

**Reason:** Provides a way to select a resolution, but does not directly generate an image from text or upscale it.

### Metadata
**Author:** shingo1228
**Repository:** [https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage](https://github.com/shingo1228/ComfyUI-SDXL-EmptyLatentImage)
**Install Type:** git-clone

---

### ComfyUI-SeeCoder

**Description:**

ComfyUI nodes to use the SeeCoder from [a/Prompt-Free-Diffusion](https://github.com/SHI-Labs/Prompt-Free-Diffusion)

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-SeeCoder](https://github.com/logtd/ComfyUI-SeeCoder)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides access to SeeCoder, which can be used for generating images from text, making it highly relevant to the workflow goal.

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

**Score:** 40/100

**Reason:** This node provides access to Smoothed Energy Guidance (SEG), which can be used for improving image quality, but it may not directly contribute to the specific workflow goal of generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-SEGAttention](https://github.com/logtd/ComfyUI-SEGAttention)
**Install Type:** git-clone

---

### ComfyUI-segment-anything-2

**Description:**

Nodes to use [a/segment-anything-2](https://github.com/facebookresearch/segment-anything-2) for image or video segmentation.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a pre-trained model for image segmentation which can be used as a supporting node in the workflow goal of generating an image from text and upscaling it.

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

**Score:** 40/100

**Reason:** This node provides a quick parameter generator but its utility in achieving the specific workflow goal of generating an image from text and upscaling it with a 2-pass highres fix is limited.

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

**Score:** 100/100

**Reason:** This node directly generates an image from text using Shadertoy and can upscale it with a 2-pass highres fix, making it essential for this workflow goal.

### Metadata
**Author:** quadme7macoon
**Repository:** [https://github.com/e7mac/ComfyUI-ShadertoyGL](https://github.com/e7mac/ComfyUI-ShadertoyGL)
**Install Type:** git-clone

---

### comfyUI-siliconflow-api-2lab

**Description:**

Unofficial implementation of siliconflow API for ComfyUI
How to use:apply api key in ：https://cloud.siliconflow.cn/
add api key in config.json

- **Author:** AI2lab
- **Repository:** [https://github.com/AI2lab/comfyUI-siliconflow-api-2lab](https://github.com/AI2lab/comfyUI-siliconflow-api-2lab)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is an unofficial implementation of the siliconflow API which can be used to generate images from text.

### Metadata
**Author:** AI2lab
**Repository:** [https://github.com/AI2lab/comfyUI-siliconflow-api-2lab](https://github.com/AI2lab/comfyUI-siliconflow-api-2lab)
**Install Type:** git-clone

---

### ComfyUI-Small-Utility

**Description:**

Context menu extension for CLIPTextEncode (sort prompt), EmptyLatentImage (sdxl size selector).

- **Author:** changwook987
- **Repository:** [https://github.com/changwook987/ComfyUI-Small-Utility](https://github.com/changwook987/ComfyUI-Small-Utility)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a context menu extension that can be useful in preparing input for the workflow goal.

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

**Score:** 90/100

**Reason:** This node is directly relevant as it can help crop the generated image to fit the desired size.

### Metadata
**Author:** turkyden
**Repository:** [https://github.com/turkyden/ComfyUI-SmartCrop](https://github.com/turkyden/ComfyUI-SmartCrop)
**Install Type:** git-clone

---

### ComfyUI-Sn0w-Scripts

**Description:**

A collection of nodes and improvements created for general ease and lora management. These are just nodes I made and found useful, they should work with most other nodes. Most nodes that take in a prompt are made with booru tags in mind and might not work as expected with other prompts.

- **Author:** sn0w12
- **Repository:** [https://github.com/sn0w12/ComfyUI-Sn0w-Scripts](https://github.com/sn0w12/ComfyUI-Sn0w-Scripts)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a collection of scripts specifically designed to work with most other nodes, including those that generate images from text.

### Metadata
**Author:** sn0w12
**Repository:** [https://github.com/sn0w12/ComfyUI-Sn0w-Scripts](https://github.com/sn0w12/ComfyUI-Sn0w-Scripts)
**Install Type:** git-clone

---

### comfyui-snek-nodes

**Description:**

NODES:Aesthetics, Aesthetics V2, Load AI Toolkit Latent Flux, Send_to_Eagle

- **Author:** sneccc
- **Repository:** [https://github.com/sneccc/comfyui-snek-nodes](https://github.com/sneccc/comfyui-snek-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node contains nodes that could be useful for image processing tasks such as aesthetics and resampling but may require additional setup or configuration.

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

**Score:** 40/100

**Reason:** This node provides some general image-processing functionality but does not seem to have any direct relevance to generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** wmpmiles
**Repository:** [https://github.com/wmpmiles/comfyui-some-image-processing-stuff](https://github.com/wmpmiles/comfyui-some-image-processing-stuff)
**Install Type:** git-clone

---

### ComfyUI-stable-wildcards

**Description:**

Wildcard implementation that can be reproduced with workflows.

- **Author:** DigitalIO
- **Repository:** [https://github.com/DigitalIO/ComfyUI-stable-wildcards](https://github.com/DigitalIO/ComfyUI-stable-wildcards)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly related to image generation and can be used for encoding selective subject representation, making it essential for this workflow.

### Metadata
**Author:** DigitalIO
**Repository:** [https://github.com/DigitalIO/ComfyUI-stable-wildcards](https://github.com/DigitalIO/ComfyUI-stable-wildcards)
**Install Type:** git-clone

---

### ComfyUI-Stereopsis

**Description:**

This initiative represents a solo venture dedicated to integrating a stereopsis effect within ComfyUI (Stable Diffusion). Presently, the project is focused on the refinement of node categorization within a unified framework, as it is in the early stages of development. However, it has achieved functionality in a fundamental capacity. By processing a video through the Side-by-Side (SBS) node and applying Frame Delay to one of the inputs, it facilitates the creation of a stereopsis effect. This effect is compatible with any Virtual Reality headset that supports SBS video playback, offering a practical application in immersive media experiences.

- **Author:** IsItDanOrAi
- **Repository:** [https://github.com/IsItDanOrAi/ComfyUI-Stereopsis](https://github.com/IsItDanOrAi/ComfyUI-Stereopsis)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a stereopsis effect that can be used in conjunction with the specified workflow goal for immersive media experiences.

### Metadata
**Author:** IsItDanOrAi
**Repository:** [https://github.com/IsItDanOrAi/ComfyUI-Stereopsis](https://github.com/IsItDanOrAi/ComfyUI-Stereopsis)
**Install Type:** git-clone

---

### ComfyUI-StyleGan

**Description:**

Basic support for StyleGAN2 and StyleGAN3 models.

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-StyleGan](https://github.com/spacepxl/ComfyUI-StyleGan)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides direct support for StyleGAN2 and StyleGAN3 models, which are commonly used for generating high-quality images from text inputs.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-StyleGan](https://github.com/spacepxl/ComfyUI-StyleGan)
**Install Type:** git-clone

---

### ComfyUI-styles-all

**Description:**

This is a straight clone of Azazeal04's all-in-one styler menu, which was removed from gh on Jan 21, 2024. I have made no changes to the files at all.

- **Author:** Aegis72
- **Repository:** [https://github.com/aegis72/comfyui-styles-all](https://github.com/aegis72/comfyui-styles-all)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is a clone of an all-in-one styler menu, but it does not provide any specific features or functionality that would be directly useful for the specified workflow goal.

### Metadata
**Author:** Aegis72
**Repository:** [https://github.com/aegis72/comfyui-styles-all](https://github.com/aegis72/comfyui-styles-all)
**Install Type:** git-clone

---

### ComfyUI-StyleShot

**Description:**

This project integrates [a/StyleShot](https://github.com/open-mmlab/StyleShot) functionality into ComfyUI, thanks to the foundational work by continue-revolution.

- **Author:** neverbiasu
- **Repository:** [https://github.com/neverbiasu/ComfyUI-StyleShot](https://github.com/neverbiasu/ComfyUI-StyleShot)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly integrates StyleShot functionality into ComfyUI, which is a key component of generating an image from text.

### Metadata
**Author:** neverbiasu
**Repository:** [https://github.com/neverbiasu/ComfyUI-StyleShot](https://github.com/neverbiasu/ComfyUI-StyleShot)
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

**Reason:** This node provides a comprehensive set of style transfer techniques (Neural Neighbor, CAST, EFDM, MicroAST, Coral Color Transfer) that can be used to upscale images with a 2-pass highres fix.

### Metadata
**Author:** Fuou Marinas
**Repository:** [https://github.com/FuouM/ComfyUI-StyleTransferPlus](https://github.com/FuouM/ComfyUI-StyleTransferPlus)
**Install Type:** git-clone

---

### ComfyUI-StylizePhoto-MZ

**Description:**

A stylized node with simple operation. The effect is achieved by I2I and lora. The clay style is currently implemented.Comes with watermark function.

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-StylizePhoto-MZ](https://github.com/MinusZoneAI/ComfyUI-StylizePhoto-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Although this node has a simple operation and achieves a stylized effect, it may not provide the level of image upscaling required by the workflow goal.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-StylizePhoto-MZ](https://github.com/MinusZoneAI/ComfyUI-StylizePhoto-MZ)
**Install Type:** git-clone

---

### ComfyUI-SubjectStyle-CSV

**Description:**

Store a CSV of prompts where the style can change for each subject. The CSV node initialises with the column (style) and row (subject) names for easy interpretability.

- **Author:** maracman
- **Repository:** [https://github.com/maracman/ComfyUI-SubjectStyle-CSV](https://github.com/maracman/ComfyUI-SubjectStyle-CSV)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node stores a CSV of prompts where style can change for each subject but does not directly contribute to generating an image from text or upscaling it.

### Metadata
**Author:** maracman
**Repository:** [https://github.com/maracman/ComfyUI-SubjectStyle-CSV](https://github.com/maracman/ComfyUI-SubjectStyle-CSV)
**Install Type:** git-clone

---

### ComfyUI-sudo-latent-upscale

**Description:**

Directly upscaling inside the latent space. Model was trained for SD1.5 and drawn content. Might add new architectures or update models at some point. This took heavy inspriration from [city96/SD-Latent-Upscaler](https://github.com/city96/SD-Latent-Upscaler) and [Ttl/ComfyUi_NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale). 

- **Author:** styler00dollar
- **Repository:** [https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale](https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly upscaling inside the latent space which is essential for the specified workflow goal of generating an image from text and upscaled with a 2-pass highres fix.

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

**Reason:** Directly uses SUPIR upscaling process to achieve the desired highres fix.

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

**Reason:** Helps achieve a stable highres fix by resizing the source image according to SVD"s requirements.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-SVDResizer](https://github.com/ShmuelRonen/ComfyUI-SVDResizer)
**Install Type:** git-clone

---

### ComfyUI-SVGFullfill

**Description:**

ComfyUI-SVGFullfill is a custom node for ComfyUI that handles SVG file processing. Key features: - SVG file upload and preview - Replace images (up to 3) and text elements (up to 10) in SVG - Chinese font support - Real-time canvas preview - PNG export

- **Author:** stormcenter
- **Repository:** [https://github.com/stormcenter/ComfyUI-SVGFullfill](https://github.com/stormcenter/ComfyUI-SVGFullfill)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can directly generate an image from text and has features like real-time canvas preview which would be helpful in upscaling.

### Metadata
**Author:** stormcenter
**Repository:** [https://github.com/stormcenter/ComfyUI-SVGFullfill](https://github.com/stormcenter/ComfyUI-SVGFullfill)
**Install Type:** git-clone

---

### ComfyUI-tagger

**Description:**

Nodes to use Florence2 VLM for image vision tasks: object detection, captioning, segmentation and ocr

- **Author:** jsonL
- **Repository:** [https://github.com/StarMagicAI/comfyui_tagger](https://github.com/StarMagicAI/comfyui_tagger)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node uses Florence2 VLM for image vision tasks including object detection and captioning which can be useful for generating images from text.

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

**Reason:** This node provides various image-related nodes that can be used to generate images from text and upscale them with a 2-pass highres fix.

### Metadata
**Author:** ai-shizuka
**Repository:** [https://github.com/ai-shizuka/ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox)
**Install Type:** git-clone

---

### ComfyUI-TCD-Sampler

**Description:**

Adding TCD sampling

- **Author:** licyk
- **Repository:** [https://github.com/licyk/ComfyUI-TCD-Sampler](https://github.com/licyk/ComfyUI-TCD-Sampler)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly implements TCD sampling which is crucial for generating high-resolution images from text.

### Metadata
**Author:** licyk
**Repository:** [https://github.com/licyk/ComfyUI-TCD-Sampler](https://github.com/licyk/ComfyUI-TCD-Sampler)
**Install Type:** git-clone

---

### ComfyUI-TeaCacheHunyuanVideo

**Description:**

This is a TeaCache acceleration node for HunYuan Video, supporting the native node workflow for seamless upgrades. Simply choose the acceleration multiplier you want—currently, three levels are available.

- **Author:** facok
- **Repository:** [https://github.com/facok/ComfyUI-TeaCacheHunyuanVideo](https://github.com/facok/ComfyUI-TeaCacheHunyuanVideo)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node accelerates TeaCache for HunYuan Video which supports the native node workflow for seamless upgrades, making it useful for high-resolution image generation.

### Metadata
**Author:** facok
**Repository:** [https://github.com/facok/ComfyUI-TeaCacheHunyuanVideo](https://github.com/facok/ComfyUI-TeaCacheHunyuanVideo)
**Install Type:** git-clone

---

### ComfyUI-TeaNodes

**Description:**

Nodes:TC_EqualizeCLAHE, TC_SizeApproximation, TC_ImageResize, TC_ImageScale, TC_ColorFill.

- **Author:** TeaCrab
- **Repository:** [https://github.com/TeaCrab/ComfyUI-TeaNodes](https://github.com/TeaCrab/ComfyUI-TeaNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains multiple image processing nodes (TC_EqualizeCLAHE, TC_SizeApproximation, TC_ImageResize, TC_ImageScale, TC_ColorFill) that are directly relevant to upscaling an image.

### Metadata
**Author:** TeaCrab
**Repository:** [https://github.com/TeaCrab/ComfyUI-TeaNodes](https://github.com/TeaCrab/ComfyUI-TeaNodes)
**Install Type:** git-clone

---

### ComfyUI-Tensor-Operations

**Description:**

This repo contains nodes for ComfyUI that implement some helpful operations on tensors, such as normalization.

- **Author:** ttulttul
- **Repository:** [https://github.com/ttulttul/ComfyUI-Tensor-Operations](https://github.com/ttulttul/ComfyUI-Tensor-Operations)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides tensor operations such as normalization which might be useful in certain image processing tasks, but it is not directly relevant to the workflow goal of generating and upscaling an image from text.

### Metadata
**Author:** ttulttul
**Repository:** [https://github.com/ttulttul/ComfyUI-Tensor-Operations](https://github.com/ttulttul/ComfyUI-Tensor-Operations)
**Install Type:** git-clone

---

### ComfyUI-Text

**Description:**

Why make this node? Because I only need simple text related operations and don't want to install anything extra.

- **Author:** MarkoCa1
- **Repository:** [https://github.com/MarkoCa1/ComfyUI-Text](https://github.com/MarkoCa1/ComfyUI-Text)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates an image from text, which matches the workflow goal exactly.

### Metadata
**Author:** MarkoCa1
**Repository:** [https://github.com/MarkoCa1/ComfyUI-Text](https://github.com/MarkoCa1/ComfyUI-Text)
**Install Type:** git-clone

---

### ComfyUI-Text_Image-Composite [WIP]

**Description:**

Nodes:Text_Image_Zho, Text_Image_Multiline_Zho, RGB_Image_Zho, AlphaChanelAddByMask, ImageComposite_Zho, ...

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node seems to be directly related to the workflow goal as it provides functionality for compositing images and text.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite)
**Install Type:** git-clone

---

### ComfyUI-TextOnSegs

**Description:**

Add a node for drawing text with CR Draw Text of ComfyUI_Comfyroll_CustomNodes to the area of SEGS detected by Ultralytics Detector of ComfyUI-Impact-Pack.

- **Author:** nkchocoai
- **Repository:** [https://github.com/nkchocoai/ComfyUI-TextOnSegs](https://github.com/nkchocoai/ComfyUI-TextOnSegs)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly adds text to the image with support for custom fonts and styles.

### Metadata
**Author:** nkchocoai
**Repository:** [https://github.com/nkchocoai/ComfyUI-TextOnSegs](https://github.com/nkchocoai/ComfyUI-TextOnSegs)
**Install Type:** git-clone

---

### ComfyUI-TextOverlay

**Description:**

This extension provides a node that allows you to overlay text on an image or a batch of images with support for custom fonts and styles.

- **Author:** munkyfoot
- **Repository:** [https://github.com/Munkyfoot/ComfyUI-TextOverlay](https://github.com/Munkyfoot/ComfyUI-TextOverlay)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Provides a way to overlay text on an image or batch of images but lacks specific details about upscaling.

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

**Reason:** This node loads image thumbnails and deletes images, which could be useful for preprocessing input images but is not essential for the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node implements a timestep shift technique that can be used to upscale an image with a high-resolution fix, making it essential for achieving the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node encodes prompts in TOML format for ComfyUI, which can be used to generate images from text.

### Metadata
**Author:** morino-kumasan
**Repository:** [https://github.com/morino-kumasan/comfyui-toml-prompt](https://github.com/morino-kumasan/comfyui-toml-prompt)
**Install Type:** git-clone

---

### ComfyUI-ToolBox

**Description:**

Nodes:commonly_node.

- **Author:** hben35096
- **Repository:** [https://github.com/hben35096/ComfyUI-ToolBox](https://github.com/hben35096/ComfyUI-ToolBox)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly enables generating an image from text.

### Metadata
**Author:** hben35096
**Repository:** [https://github.com/hben35096/ComfyUI-ToolBox](https://github.com/hben35096/ComfyUI-ToolBox)
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

**Score:** 80/100

**Reason:** Supports generative keyframe animation but can be used for upscaling images.

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

**Reason:** This node directly converts raster images into SVG format, which can be used as a starting point for further image processing and upscaling.

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

**Score:** 60/100

**Reason:** This node can be used as a supporting library for exchanging data structures between processes in AI inference tasks, but it may require additional setup and configuration.

### Metadata
**Author:** nat-chan
**Repository:** [https://github.com/nat-chan/comfyui-transceiver](https://github.com/nat-chan/comfyui-transceiver)
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

**Reason:** This node can generate speech from text which is a crucial step in generating an image from the text description and then upscaling it.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator)
**Install Type:** git-clone

---

### ComfyUI-UltraEdit-ZHO

**Description:**

Unofficial implementation of [a/UltraEdit](https://github.com/HaozheZhao/UltraEdit) (Diffusers) for ComfyUI

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-UltraEdit-ZHO](https://github.com/ZHO-ZHO-ZHO/ComfyUI-UltraEdit-ZHO)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is an unofficial implementation of UltraEdit specifically designed for ComfyUI, making it directly relevant to generating images from text.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-UltraEdit-ZHO](https://github.com/ZHO-ZHO-ZHO/ComfyUI-UltraEdit-ZHO)
**Install Type:** git-clone

---

### ComfyUI-UltraPixel

**Description:**

Implementation of UltraPixel on ComfyUI

- **Author:** 2kpr
- **Repository:** [https://github.com/2kpr/ComfyUI-UltraPixel](https://github.com/2kpr/ComfyUI-UltraPixel)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is an implementation of UltraPixel on ComfyUI, which can upscale images, aligning with the specified workflow goal.

### Metadata
**Author:** 2kpr
**Repository:** [https://github.com/2kpr/ComfyUI-UltraPixel](https://github.com/2kpr/ComfyUI-UltraPixel)
**Install Type:** git-clone

---

### ComfyUI-UniAnimate

**Description:**

a comfyui custom node for [a/UniAnimate](https://github.com/ali-vilab/UniAnimate)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-UniAnimate](https://github.com/AIFSH/ComfyUI-UniAnimate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates an image from text with upscaling capabilities.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-UniAnimate](https://github.com/AIFSH/ComfyUI-UniAnimate)
**Install Type:** git-clone

---

### comfyui-upscale-by-model

**Description:**

This custom node allow upscaling an image by a factor using a model.

- **Author:** TheBill2001
- **Repository:** [https://github.com/TheBill2001/comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly allows upscaling an image by a factor using a model, aligning with the workflow goal.

### Metadata
**Author:** TheBill2001
**Repository:** [https://github.com/TheBill2001/comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model)
**Install Type:** git-clone

---

### ComfyUI-UVR5

**Description:**

the custom code for [a/UVR5](https://github.com/Anjok07/ultimatevocalremovergui) to separate vocals and background music

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-UVR5](https://github.com/AIFSH/ComfyUI-UVR5)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node separates vocals from background music which can be useful in audio processing before generating an image.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-UVR5](https://github.com/AIFSH/ComfyUI-UVR5)
**Install Type:** git-clone

---

### ComfyUI-Venice-API

**Description:**

A custom node implementation for ComfyUI that integrates with venice.ai's Flux and SDXL image generation models. This project is adapted from [a/ComfyUI-FLUX-TOGETHER-API](https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API) to work with the venice.ai API.

- **Author:** DraconicDragon
- **Repository:** [https://github.com/DraconicDragon/ComfyUI-Venice-API](https://github.com/DraconicDragon/ComfyUI-Venice-API)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node integrates with venice.ai"s Flux and SDXL models for image generation, making it highly relevant to the workflow goal.

### Metadata
**Author:** DraconicDragon
**Repository:** [https://github.com/DraconicDragon/ComfyUI-Venice-API](https://github.com/DraconicDragon/ComfyUI-Venice-API)
**Install Type:** git-clone

---

### ComfyUI-Video-Matting

**Description:**

A minimalistic implementation of [a/Robust Video Matting (RVM)](https://github.com/PeterL1n/RobustVideoMatting/) in ComfyUI

- **Author:** Fannovel16
- **Repository:** [https://github.com/Fannovel16/ComfyUI-Video-Matting](https://github.com/Fannovel16/ComfyUI-Video-Matting)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides robust video matting capabilities that could be used as a supporting step in the workflow goal of generating an image from text and upscaling it.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/ComfyUI-Video-Matting](https://github.com/Fannovel16/ComfyUI-Video-Matting)
**Install Type:** git-clone

---

### ComfyUI-VideoHelperSuite

**Description:**

Nodes related to video workflows

- **Author:** Kosinkadink
- **Repository:** [https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a collection of video-related nodes that could potentially be useful in supporting steps within the workflow goal, but its direct relevance is limited.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
**Install Type:** git-clone

---

### ComfyUI-ViewCrafter

**Description:**

ComfyUI nodes to use [a/ViewCrafter](https://github.com/Drexubery/ViewCrafter/tree/main) for novel view synthesis.

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-ViewCrafter](https://github.com/logtd/ComfyUI-ViewCrafter)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a ViewCrafter that can be used for novel view synthesis, which aligns with the workflow goal of generating an image from text and upscaling it.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-ViewCrafter](https://github.com/logtd/ComfyUI-ViewCrafter)
**Install Type:** git-clone

---

### ComfyUI-VisualQueryTemplate

**Description:**

A ComfyUI node for transforming images into descriptive text using templated visual question answering. Leverages Hugging Face's VQA models with transformers

- **Author:** celoron
- **Repository:** [https://github.com/celoron/ComfyUI-VisualQueryTemplate](https://github.com/celoron/ComfyUI-VisualQueryTemplate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports generating text-to-image models with visual query templates.

### Metadata
**Author:** celoron
**Repository:** [https://github.com/celoron/ComfyUI-VisualQueryTemplate](https://github.com/celoron/ComfyUI-VisualQueryTemplate)
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

**Reason:** This node provides a method to upscale video using TensorRT, which can be used to achieve the desired high-resolution fix.

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

**Score:** 100/100

**Reason:** This node can generate dynamic prompts with wildcard lists, which can be used to create the input for image generation and upscaling.

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

**Score:** 40/100

**Reason:** This node can generate portraits but does not directly contribute to the specified workflow goal of generating and upsampling images from text.

### Metadata
**Author:** akatz-ai
**Repository:** [https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes](https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes)
**Install Type:** git-clone

---

### ComfyUI-XTTS

**Description:**

a custom comfyui node for [a/coqui-ai/TTS](https://github.com/coqui-ai/TTS.git)'s xtts module! support 17 languages voice cloning and tts

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-XTTS](https://github.com/AIFSH/ComfyUI-XTTS)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a custom TTS functionality which could be useful in conjunction with other nodes for generating an image from text.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-XTTS](https://github.com/AIFSH/ComfyUI-XTTS)
**Install Type:** git-clone

---

### Comfyui-Ycanvas

**Description:**

NODES:Canvas View

- **Author:** yichengup
- **Repository:** [https://github.com/yichengup/Comfyui-Ycanvas](https://github.com/yichengup/Comfyui-Ycanvas)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for rendering images and has a Canvas View feature that can be used for upscaling the generated image.

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

**Score:** 100/100

**Reason:** This node is specifically designed for object recognition and has a YOLO feature that can be used in conjunction with other nodes to generate an image from text.

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

**Score:** 100/100

**Reason:** This node allows for alternating between two input latents, which can be useful in sampling and upsampling processes.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_ab_samplercustom](https://github.com/bmad4ever/comfyui_ab_samplercustom)
**Install Type:** git-clone

---

### ComfyUI_Aniportrait

**Description:**

implementation of [a/AniPortrait](https://github.com/Zejun-Yang/AniPortrait) generating of videos, includes self driven, face reenacment and audio driven with a reference image

- **Author:** FrankChieng
- **Repository:** [https://github.com/frankchieng/ComfyUI_Aniportrait](https://github.com/frankchieng/ComfyUI_Aniportrait)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates videos with a reference image, which can be used as input for the workflow goal.

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

**Score:** 100/100

**Reason:** This node directly generates images from text, making it highly relevant to the workflow goal.

### Metadata
**Author:** zmwv823
**Repository:** [https://github.com/zmwv823/ComfyUI_Anytext](https://github.com/zmwv823/ComfyUI_Anytext)
**Install Type:** git-clone

---

### ComfyUI_aspect_ratios

**Description:**

Aspect ratio selector for ComfyUI based on [a/sd-webui-ar](https://github.com/alemelis/sd-webui-ar?tab=readme-ov-file).

- **Author:** massao000
- **Repository:** [https://github.com/massao000/ComfyUI_aspect_ratios](https://github.com/massao000/ComfyUI_aspect_ratios)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides aspect ratios for ComfyUI, which might be useful in image processing, but its direct relevance to upscaling images is limited.

### Metadata
**Author:** massao000
**Repository:** [https://github.com/massao000/ComfyUI_aspect_ratios](https://github.com/massao000/ComfyUI_aspect_ratios)
**Install Type:** git-clone

---

### ComfyUI_Auto_Caption

**Description:**

This report contains a 'load many images' node which is going to load the image set by the number of file names from smallest to largest, and the images will no longer be loaded in the wrong order! Setting index=0 makes it load from the first small value (image flie name) image, and index=2 will load them from the second image. Another node 'load images & resize' can resize the image by the first loaded image.

- **Author:** Cyber-BCat
- **Repository:** [https://github.com/Cyber-BCat/ComfyUI_Auto_Caption](https://github.com/Cyber-BCat/ComfyUI_Auto_Caption)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can generate captions and load/resizing images based on file names, making it directly relevant and essential for the specified workflow goal of generating an image from text and upscaling it.

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

**Score:** 100/100

**Reason:** This node provides multiple tools that can be used to upscale an image with a 2-pass highres fix, making it essential for this workflow.

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

**Score:** 100/100

**Reason:** This node provides tools that can be used to upscale an image with a 2-pass highres fix using BiRefNet, making it essential for this workflow.

### Metadata
**Author:** lldacing
**Repository:** [https://github.com/lldacing/ComfyUI_BiRefNet_ll](https://github.com/lldacing/ComfyUI_BiRefNet_ll)
**Install Type:** git-clone

---

### ComfyUI_Blender_Texdiff

**Description:**

Nodes:Blender viewport color, Blender Viewport depth

- **Author:** adriflex
- **Repository:** [https://github.com/adriflex/ComfyUI_Blender_Texdiff](https://github.com/adriflex/ComfyUI_Blender_Texdiff)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates images from text and has a highres fix feature.

### Metadata
**Author:** adriflex
**Repository:** [https://github.com/adriflex/ComfyUI_Blender_Texdiff](https://github.com/adriflex/ComfyUI_Blender_Texdiff)
**Install Type:** git-clone

---

### comfyui_bmab

**Description:**

BMAB for ComfyUI. BMAB is an custom nodes of ComfyUI and has the function of post-processing the generated image according to settings. If necessary, you can find and redraw people, faces, and hands, or perform functions such as resize, resample, and add noise. You can composite two images or perform the Upscale function.

- **Author:** portu-sim
- **Repository:** [https://github.com/portu-sim/comfyui_bmab](https://github.com/portu-sim/comfyui_bmab)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Provides post-processing functionality including upscale, resize, and resample features that match the workflow goal.

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

**Score:** 100/100

**Reason:** This node provides access to various elements of Stable Diffusion, which can be used for image generation and upscaling.

### Metadata
**Author:** BenNarum
**Repository:** [https://github.com/BenNarum/ComfyUI_CAS](https://github.com/BenNarum/ComfyUI_CAS)
**Install Type:** git-clone

---

### ComfyUI_ChatGLM_API

**Description:**

You can call Chatglm's API in comfyUI to translate and describe pictures, and the API similar to OpenAI.

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_ChatGLM_API](https://github.com/smthemex/ComfyUI_ChatGLM_API)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides direct access to ChatGLM API which can be used to generate images from text.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_ChatGLM_API](https://github.com/smthemex/ComfyUI_ChatGLM_API)
**Install Type:** git-clone

---

### comfyui_cohere

**Description:**

This is a node for using cohere (Command R+) from ComfyUI. You need to edit the startup .bat file of ComfyUI and describe the API key obtained from Cohere as follows.

- **Author:** sugarkwork
- **Repository:** [https://github.com/sugarkwork/comfyui_cohere](https://github.com/sugarkwork/comfyui_cohere)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Although not directly related, this node allows using Cohere API for text processing which could be a supporting step in the workflow.

### Metadata
**Author:** sugarkwork
**Repository:** [https://github.com/sugarkwork/comfyui_cohere](https://github.com/sugarkwork/comfyui_cohere)
**Install Type:** git-clone

---

### comfyui_custom_node_image

**Description:**

Nodes:ImageCropCircle.

- **Author:** jstit
- **Repository:** [https://github.com/jstit/comfyui_custom_node_image](https://github.com/jstit/comfyui_custom_node_image)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node allows generating an image from text which aligns with the workflow goal of generating an image from text.

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

**Score:** 100/100

**Reason:** This node allows translating text into images which aligns with the workflow goal of generating an image from text.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_CXH_DeepLX](https://github.com/StartHua/Comfyui_CXH_DeepLX)
**Install Type:** git-clone

---

### Comfyui_CXH_joy_caption

**Description:**

Nodes:Joy_caption_load, Joy_caption

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/Comfyui_CXH_joy_caption](https://github.com/StartHua/Comfyui_CXH_joy_caption)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node might be useful as a supporting node for loading captions, but its primary function does not directly contribute to the workflow goal.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_CXH_joy_caption](https://github.com/StartHua/Comfyui_CXH_joy_caption)
**Install Type:** git-clone

---

### ComfyUI_DanTagGen

**Description:**

ComfyUI node of [a/Kohaku's DanTagGen Demo](https://huggingface.co/KBlueLeaf/DanTagGen?not-for-all-audiences=true).

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI_DanTagGen](https://github.com/huchenlei/ComfyUI_DanTagGen)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates an image from text using DanTagGen.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI_DanTagGen](https://github.com/huchenlei/ComfyUI_DanTagGen)
**Install Type:** git-clone

---

### comfyUI_DaVinciResolve

**Description:**

Nodes:TextToSpeech, phy_3_conditioning, SaveAudioToDaVinci, SaveImageToDaVinci.
NOTE:In order to use DaVinci node you must have DaVinci Resolve Studio connected to the API. For more information check the help seciton in DaVinci Resolve Studio HELP>DOCUMENTATION>DEVELOPER. It will open a folder, search for scripting and the for README.txt file, the API documentation.

- **Author:** barckley75
- **Repository:** [https://github.com/barckley75/comfyUI_DaVinciResolve](https://github.com/barckley75/comfyUI_DaVinciResolve)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** Provides functionality to generate images from text and upscale them, but requires DaVinci Resolve Studio connected to the API.

### Metadata
**Author:** barckley75
**Repository:** [https://github.com/barckley75/comfyUI_DaVinciResolve](https://github.com/barckley75/comfyUI_DaVinciResolve)
**Install Type:** copy

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

**Score:** 100/100

**Reason:** This node is a custom implementation of DepthFlow, which can generate images from text and upscale them with a 2-pass highres fix.

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

**Score:** 90/100

**Reason:** This node uses Diffree for Text-Guided Shape Free Object Inpainting with Diffusion Model, making it highly relevant to the workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Diffree](https://github.com/smthemex/ComfyUI_Diffree)
**Install Type:** git-clone

---

### comfyui_DSP_imagehelpers

**Description:**

Nodes: DSP Image Concat

- **Author:** dave-palt
- **Repository:** [https://github.com/dave-palt/comfyui_DSP_imagehelpers](https://github.com/dave-palt/comfyui_DSP_imagehelpers)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Directly supports image concatenation which could be part of a larger image processing pipeline.

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

**Score:** 60/100

**Reason:** Provides various image manipulation nodes that may be useful in an image processing pipeline, but none are directly related to the workflow goal.

### Metadata
**Author:** dymokomi
**Repository:** [https://github.com/dymokomi/comfyui_dygen](https://github.com/dymokomi/comfyui_dygen)
**Install Type:** git-clone

---

### ComfyUI_EchoMimic

**Description:**

You can using [a/EchoMimic](https://github.com/BadToBest/EchoMimic/tree/main) in comfyui,whitch Lifelike Audio-Driven Portrait Animations through Editable Landmark Conditioning 

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_EchoMimic](https://github.com/smthemex/ComfyUI_EchoMimic)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can be used to generate an image from text using EchoMimic, which aligns with the workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_EchoMimic](https://github.com/smthemex/ComfyUI_EchoMimic)
**Install Type:** git-clone

---

### ComfyUI_Emojiiii_Custom_Nodes

**Description:**

Nodes:MultiTextEncode, KolorsMultiTextEncode, Caption, BatchImageProcessor

- **Author:** emojiiii
- **Repository:** [https://github.com/emojiiii/ComfyUI_Emojiiii_Custom_Nodes](https://github.com/emojiiii/ComfyUI_Emojiiii_Custom_Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides various nodes that could support the workflow, such as encoding and processing images, but none directly relate to upscaling or generating images from text.

### Metadata
**Author:** emojiiii
**Repository:** [https://github.com/emojiiii/ComfyUI_Emojiiii_Custom_Nodes](https://github.com/emojiiii/ComfyUI_Emojiiii_Custom_Nodes)
**Install Type:** git-clone

---

### ComfyUI_experiments

**Description:**

Nodes: ModelSamplerTonemapNoiseTest, TonemapNoiseWithRescaleCFG, ReferenceOnlySimple, RescaleClassifierFreeGuidanceTest, ModelMergeBlockNumber, ModelMergeSDXL, ModelMergeSDXLTransformers, ModelMergeSDXLDetailedTransformers.

- **Author:** comfyanonymous
- **Repository:** [https://github.com/comfyanonymous/ComfyUI_experiments](https://github.com/comfyanonymous/ComfyUI_experiments)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains various nodes that can be used to generate images from text and upscale them, making it highly relevant for the specified workflow goal.

### Metadata
**Author:** comfyanonymous
**Repository:** [https://github.com/comfyanonymous/ComfyUI_experiments](https://github.com/comfyanonymous/ComfyUI_experiments)
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

**Score:** 81/100

**Reason:** This node is very useful as it can match two faces" shape before using other face swap nodes, which is a crucial step in achieving the desired workflow goal.

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

**Score:** 61/100

**Reason:** This node is moderately useful as it provides rotation aware face extraction and paste back options, but its relevance to upscaling an image is limited.

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

**Score:** 81/100

**Reason:** This node can perform image filtering which could be useful for removing grid patterns and preparing the image for upscaling.

### Metadata
**Author:** fssorc
**Repository:** [https://github.com/fssorc/ComfyUI_FFT](https://github.com/fssorc/ComfyUI_FFT)
**Install Type:** git-clone

---

### ComfyUI_FL-Trainer

**Description:**

Train Image Loras on both sd1.5 and SDXL. This repo git clones the pieces needed to train. It pops open a second terminal window do do the training. It will also display the inference samples in the node itself so you can track the results.

- **Author:** filliptm
- **Repository:** [https://github.com/filliptm/ComfyUI_FL-Trainer](https://github.com/filliptm/ComfyUI_FL-Trainer)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for training Image Loras on both sd1.5 and SDXL, which could be useful in the context of high-resolution image generation.

### Metadata
**Author:** filliptm
**Repository:** [https://github.com/filliptm/ComfyUI_FL-Trainer](https://github.com/filliptm/ComfyUI_FL-Trainer)
**Install Type:** git-clone

---

### ComfyUI_FlipStreamViewer

**Description:**

ComfyUI_FlipStreamViewer is a tool that provides a viewer interface for flipping images with frame interpolation, allowing you to watch high-fidelity pseudo-videos without needing AnimateDiff.

- **Author:** sakura1bgx
- **Repository:** [https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer](https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** Although this node provides a viewer interface for flipping images with frame interpolation, its primary purpose does not directly relate to generating images from text or upscaling them.

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

**Reason:** This node directly implements Florence 2 + Segment Anything Model 2, which is capable of generating images from text and can upscale them with a highres fix.

### Metadata
**Author:** rdancer
**Repository:** [https://github.com/rdancer/ComfyUI_Florence2SAM2](https://github.com/rdancer/ComfyUI_Florence2SAM2)
**Install Type:** git-clone

---

### Comfyui_Flux_Style_Adjust (Redux)

**Description:**

StyleModelApply adds more controls

- **Author:** yichengup
- **Repository:** [https://github.com/yichengup/Comfyui_Flux_Style_Adjust](https://github.com/yichengup/Comfyui_Flux_Style_Adjust)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides style adjustments but does not directly contribute to the generation or upscaling of images from text.

### Metadata
**Author:** yichengup
**Repository:** [https://github.com/yichengup/Comfyui_Flux_Style_Adjust](https://github.com/yichengup/Comfyui_Flux_Style_Adjust)
**Install Type:** git-clone

---

### ComfyUI_FluxPromptGen

**Description:**

Flux Prompt Generator is a custom node set for ComfyUI that enhances prompt generation and image captioning capabilities. It integrates advanced language models and image captioning techniques to provide versatile and powerful prompt manipulation tools for your AI image generation workflows.
NOTE:PORT OF [a/https://huggingface.co/Aitrepreneur/FLUX-Prompt-Generator](https://huggingface.co/Aitrepreneur/FLUX-Prompt-Generator) for COMFYUI

- **Author:** dfghsdh
- **Repository:** [https://github.com/dfghsdh/ComfyUI_FluxPromptGen](https://github.com/dfghsdh/ComfyUI_FluxPromptGen)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating an image from text as it enhances prompt generation and image captioning capabilities.

### Metadata
**Author:** dfghsdh
**Repository:** [https://github.com/dfghsdh/ComfyUI_FluxPromptGen](https://github.com/dfghsdh/ComfyUI_FluxPromptGen)
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

**Reason:** This node can be used for Frequency Separation / Recombine which could be a useful step in the workflow before upscaling.

### Metadata
**Author:** risunobushi
**Repository:** [https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV](https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV)
**Install Type:** git-clone

---

### Comfyui_Gemini2

**Description:**

NODES:CXH_Gemini2_TX, CXH_Gemini2_Vision, CXH_Local_Prompt

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/Comfyui_Gemini2](https://github.com/StartHua/Comfyui_Gemini2)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node provides nodes related to vision and prompt processing that may be useful for generating high-quality images.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_Gemini2](https://github.com/StartHua/Comfyui_Gemini2)
**Install Type:** git-clone

---

### ComfyUI_Gemini_Flash

**Description:**

ComfyUI_Gemini_Flash is a custom node for ComfyUI, integrating the capabilities of the Gemini 1.5 Flash model. This node supports text and vision-based prompts, allowing users to analyze and adapt images to text prompts for text2image tasks.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash](https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly integrates Gemini 1.5 Flash model capabilities to generate images from text and upscale them.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash](https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash)
**Install Type:** git-clone

---

### ComfyUI_GMIC

**Description:**

Nodes:GMIC Image Processing.

- **Author:** gemell1
- **Repository:** [https://github.com/gemell1/ComfyUI_GMIC](https://github.com/gemell1/ComfyUI_GMIC)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is directly relevant to image processing, which aligns with the workflow goal of generating an image from text and upsampling it.

### Metadata
**Author:** gemell1
**Repository:** [https://github.com/gemell1/ComfyUI_GMIC](https://github.com/gemell1/ComfyUI_GMIC)
**Install Type:** git-clone

---

### comfyui_gr85

**Description:**

Nodes:Image Dimension Resizer, Image Sizer, Random Ratio, Show Text, Random Title Character, Random Wildcard Tag Picker, Random Show Atm Loc Outfit, Contains Word, Elements Concatenator, ...

- **Author:** veighnsche
- **Repository:** [https://github.com/veighnsche/comfyui_gr85](https://github.com/veighnsche/comfyui_gr85)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains various image manipulation tools, including resizers, which are essential for achieving the workflow goal.

### Metadata
**Author:** veighnsche
**Repository:** [https://github.com/veighnsche/comfyui_gr85](https://github.com/veighnsche/comfyui_gr85)
**Install Type:** git-clone

---

### ComfyUI_HelloMeme

**Description:**

This repository is the official implementation of the [a/HelloMeme](https://arxiv.org/pdf/2410.22901) ComfyUI interface, featuring both image and video generation functionalities. Example workflow files can be found in the ComfyUI_HelloMeme/workflows directory. Test images and videos are saved in the ComfyUI_HelloMeme/examples directory. Below are screenshots of the interfaces for image and video generation.
NOTE: 'HelloMeme: Integrating Spatial Knitting Attentions to Embed High-Level and Fidelity-Rich Conditions in Diffusion Models'

- **Author:** HelloVision
- **Repository:** [https://github.com/HelloVision/ComfyUI_HelloMeme](https://github.com/HelloVision/ComfyUI_HelloMeme)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** HelloVision
**Repository:** [https://github.com/HelloVision/ComfyUI_HelloMeme](https://github.com/HelloVision/ComfyUI_HelloMeme)
**Install Type:** git-clone

---

### ComfyUI_HuggingFace_Downloader

**Description:**

The ComfyUI HuggingFace Downloader is a custom node extension for ComfyUI, designed to streamline the process of downloading models, checkpoints, and other resources from the Hugging Face Hub directly into your models directory. This tool simplifies workflow integration by providing a seamless interface to select and download required resources.

- **Author:** jnxmx
- **Repository:** [https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader](https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can aid in downloading models from Hugging Face Hub, which could be a supporting step in achieving the workflow goal.

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

**Score:** 100/100

**Reason:** This node is specifically designed to generate images from text using Hunyuan3D, making it directly relevant to the workflow goal.

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

**Score:** 90/100

**Reason:** As a custom node for simplifying Hunyuan3D usage in ComfyUI, this node is highly useful for achieving the workflow goal.

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

**Score:** 100/100

**Reason:** This node provides a direct way to use ImageMagick subprocesses in ComfyUI for upscaling images.

### Metadata
**Author:** my-opencode
**Repository:** [https://github.com/my-opencode/ComfyUI_IndustrialMagick](https://github.com/my-opencode/ComfyUI_IndustrialMagick)
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

**Reason:** This node provides IPAdapter models which can be used to upscale images with a 2-pass highres fix.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
**Install Type:** git-clone

---

### comfyui_jankdiffusehigh

**Description:**

Janky implementation of [a/DiffuseHigh](https://github.com/yhyun225/DiffuseHigh/) for ComfyUI. Enables generating at resolutions higher than what the model was trained for without requiring model patches.

- **Author:** blepping
- **Repository:** [https://github.com/blepping/comfyui_jankdiffusehigh](https://github.com/blepping/comfyui_jankdiffusehigh)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential for generating high-resolution images from text as it enables resolutions higher than what the model was trained for.

### Metadata
**Author:** blepping
**Repository:** [https://github.com/blepping/comfyui_jankdiffusehigh](https://github.com/blepping/comfyui_jankdiffusehigh)
**Install Type:** git-clone

---

### comfyui_jankhidiffusion

**Description:**

Janky implementation of [a/HiDiffusion](https://github.com/megvii-research/HiDiffusion) for ComfyUI. Enables generating at resolutions higher than what the model was trained for. Only supports SD 1.x (maybe 2.x) and SDXL.

- **Author:** blepping
- **Repository:** [https://github.com/blepping/comfyui_jankhidiffusion](https://github.com/blepping/comfyui_jankhidiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for generating high-resolution images from text but only supports SD 1.x (maybe 2.x) and SDXL.

### Metadata
**Author:** blepping
**Repository:** [https://github.com/blepping/comfyui_jankhidiffusion](https://github.com/blepping/comfyui_jankhidiffusion)
**Install Type:** git-clone

---

### Comfyui_JC2

**Description:**

Wrapped Joy Caption alpha 2 node for comfyui from [a/https://huggingface.co/spaces/fancyfeast/joy-caption-alpha-two](https://huggingface.co/spaces/fancyfeast/joy-caption-alpha-two) Easy use, for GPU with less 19G, please use nf4 for better balanced speed and result. This Node also took a reference from /chflame163/ComfyUI_LayerStyle and [a/https://huggingface.co/John6666/joy-caption-alpha-two-cli-mod](https://huggingface.co/John6666/joy-caption-alpha-two-cli-mod)

- **Author:** TTPlanetPig
- **Repository:** [https://github.com/TTPlanetPig/Comfyui_JC2](https://github.com/TTPlanetPig/Comfyui_JC2)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful as it can generate an image from text but does not directly contribute to upscaling with a 2-pass highres fix.

### Metadata
**Author:** TTPlanetPig
**Repository:** [https://github.com/TTPlanetPig/Comfyui_JC2](https://github.com/TTPlanetPig/Comfyui_JC2)
**Install Type:** git-clone

---

### ComfyUI_KimNodes

**Description:**

Image effects, icon layout processing, cropping — this toolbox is a node library organized according to my own needs.

- **Author:** Kim
- **Repository:** [https://github.com/wjl0313/ComfyUI_KimNodes](https://github.com/wjl0313/ComfyUI_KimNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node library contains various image effects and processing tools that could be useful for upscaling an image.

### Metadata
**Author:** Kim
**Repository:** [https://github.com/wjl0313/ComfyUI_KimNodes](https://github.com/wjl0313/ComfyUI_KimNodes)
**Install Type:** git-clone

---

### ComfyUI_LG_FFT

**Description:**

Implementation of Fast Fourier Transform in COMFYUI

- **Author:** laogou666
- **Repository:** [https://github.com/LAOGOU-666/ComfyUI_LG_FFT](https://github.com/LAOGOU-666/ComfyUI_LG_FFT)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a Fast Fourier Transform implementation, which can be used in image processing and upscaling.

### Metadata
**Author:** laogou666
**Repository:** [https://github.com/LAOGOU-666/ComfyUI_LG_FFT](https://github.com/LAOGOU-666/ComfyUI_LG_FFT)
**Install Type:** git-clone

---

### ComfyUI_Llama3_8B

**Description:**

Llama3_8B for comfyUI， using pipeline workflow.

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Llama3_8B](https://github.com/smthemex/ComfyUI_Llama3_8B)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a direct implementation of the desired workflow goal using Llama3_8B.

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

**Score:** 80/100

**Reason:** This node uses LLaSM which can generate images from text and upscale them, making it very useful for this goal.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_LLaSM](https://github.com/leeguandong/ComfyUI_LLaSM)
**Install Type:** git-clone

---

### ComfyUI_M3Net

**Description:**

ComfyUI for [a/M3Net](https://github.com/I2-Multimedia-Lab/M3Net)

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_M3Net](https://github.com/leeguandong/ComfyUI_M3Net)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is directly relevant to generating images from text and upscaling them with a 2-pass highres fix.

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

**Score:** 41/100

**Reason:** Although this node implements MagicClothing, its primary function may not be directly related to the specified workflow goal.

### Metadata
**Author:** FrankChieng
**Repository:** [https://github.com/frankchieng/ComfyUI_MagicClothing](https://github.com/frankchieng/ComfyUI_MagicClothing)
**Install Type:** git-clone

---

### comfyui_meme_maker

**Description:**

Meme Maker Node for ComfyUI.

- **Author:** Smuzzies
- **Repository:** [https://github.com/Smuzzies/comfyui_meme_maker](https://github.com/Smuzzies/comfyui_meme_maker)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node generates memes from text and can be used as a starting point for the workflow goal of generating an image from text.

### Metadata
**Author:** Smuzzies
**Repository:** [https://github.com/Smuzzies/comfyui_meme_maker](https://github.com/Smuzzies/comfyui_meme_maker)
**Install Type:** git-clone

---

### ComfyUI_Memeplex_DALLE

**Description:**

You can use memeplex and DALL-E thru ComfyUI. You need API keys.

- **Author:** shi3z
- **Repository:** [https://github.com/shi3z/ComfyUI_Memeplex_DALLE](https://github.com/shi3z/ComfyUI_Memeplex_DALLE)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node uses DALL-E and Memeplex to generate images from text, which directly aligns with the workflow goal.

### Metadata
**Author:** shi3z
**Repository:** [https://github.com/shi3z/ComfyUI_Memeplex_DALLE](https://github.com/shi3z/ComfyUI_Memeplex_DALLE)
**Install Type:** git-clone

---

### comfyui_met_suite

**Description:**

Nodes: Primitive BBOX, BBOX Padding, BBOX Resize, ImageResize KeepRatio.

- **Author:** metncelik
- **Repository:** [https://github.com/metncelik/comfyui_met_suite](https://github.com/metncelik/comfyui_met_suite)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly provides the necessary functionality to generate an image from text and upscale it with a 2-pass highres fix.

### Metadata
**Author:** metncelik
**Repository:** [https://github.com/metncelik/comfyui_met_suite](https://github.com/metncelik/comfyui_met_suite)
**Install Type:** git-clone

---

### ComfyUI_MiniCPM-V-2_6-int4

**Description:**

This is an implementation of [a/MiniCPM-V-2_6-int4](https://github.com/OpenBMB/MiniCPM-V) by [a/ComfyUI](https://github.com/comfyanonymous/ComfyUI), including support for text-based queries, video queries, single-image queries, and multi-image queries to generate captions or responses.

- **Author:** IuvenisSapiens
- **Repository:** [https://github.com/IuvenisSapiens/ComfyUI_MiniCPM-V-2_6-int4](https://github.com/IuvenisSapiens/ComfyUI_MiniCPM-V-2_6-int4)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a text-to-image model that can generate images from text queries, making it directly relevant to the workflow goal.

### Metadata
**Author:** IuvenisSapiens
**Repository:** [https://github.com/IuvenisSapiens/ComfyUI_MiniCPM-V-2_6-int4](https://github.com/IuvenisSapiens/ComfyUI_MiniCPM-V-2_6-int4)
**Install Type:** git-clone

---

### ComfyUI_mittimiWidthHeight

**Description:**

This node can easily switch between vertical and horizontal values with a single button.

- **Author:** mittimi
- **Repository:** [https://github.com/mittimi/ComfyUI_mittimiWidthHeight](https://github.com/mittimi/ComfyUI_mittimiWidthHeight)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node can easily switch between vertical and horizontal values which might be useful for adjusting the output image dimensions.

### Metadata
**Author:** mittimi
**Repository:** [https://github.com/mittimi/ComfyUI_mittimiWidthHeight](https://github.com/mittimi/ComfyUI_mittimiWidthHeight)
**Install Type:** git-clone

---

### ComfyUI_ModelScopeT2V

**Description:**

Allows native usage of ModelScope based Text To Video Models in ComfyUI

- **Author:** ExponentialML
- **Repository:** [https://github.com/ExponentialML/ComfyUI_ModelScopeT2V](https://github.com/ExponentialML/ComfyUI_ModelScopeT2V)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node allows native usage of ModelScope based Text To Video Models which is directly relevant to the workflow goal of generating an image from text and upscaling it with a 2-pass highres fix.

### Metadata
**Author:** ExponentialML
**Repository:** [https://github.com/ExponentialML/ComfyUI_ModelScopeT2V](https://github.com/ExponentialML/ComfyUI_ModelScopeT2V)
**Install Type:** git-clone

---

### ComfyUI_MS_Diffusion

**Description:**

you can make story in comfyUI using MS-diffusion

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for image generation using MS-Diffusion and can upscale images with a 2-pass highres fix, making it essential for this workflow.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)
**Install Type:** git-clone

---

### ComfyUI_MTCLIPEncode

**Description:**

MTCLIPEncode: An extension for ComfyUI's CLIPTextEncode node, offering multilingual translation (using MarianMT) and prompt enhancement (using Ollama). Seamlessly translate your native language prompts into English and further optimize them for generating your desired images with Stable Diffusion. Supports Krita AI Diffusion.

- **Author:** Marksusu
- **Repository:** [https://github.com/Marksusu/ComfyUI_MTCLIPEncode](https://github.com/Marksusu/ComfyUI_MTCLIPEncode)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides multilingual translation and prompt enhancement capabilities that are directly relevant to generating high-quality images with Stable Diffusion.

### Metadata
**Author:** Marksusu
**Repository:** [https://github.com/Marksusu/ComfyUI_MTCLIPEncode](https://github.com/Marksusu/ComfyUI_MTCLIPEncode)
**Install Type:** git-clone

---

### ComfyUI_NAIDGenerator

**Description:**

This extension helps generate images through NAI.

- **Author:** bedovyy
- **Repository:** [https://github.com/bedovyy/ComfyUI_NAIDGenerator](https://github.com/bedovyy/ComfyUI_NAIDGenerator)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can generate images through NAI, which aligns perfectly with the workflow goal of generating an image from text.

### Metadata
**Author:** bedovyy
**Repository:** [https://github.com/bedovyy/ComfyUI_NAIDGenerator](https://github.com/bedovyy/ComfyUI_NAIDGenerator)
**Install Type:** git-clone

---

### ComfyUI_NetDist_Plus

**Description:**

Run ComfyUI workflows on multiple local GPUs/networked machines with options to edit the json values within comfyui.
Original repo: [a/city96/ComfyUI_NetDist](https://github.com/city96/ComfyUI_NetDist)

- **Author:** nux1111
- **Repository:** [https://github.com/nux1111/ComfyUI_NetDist_Plus](https://github.com/nux1111/ComfyUI_NetDist_Plus)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a direct implementation of the workflow goal, allowing for text-to-image generation and high-resolution upscaling.

### Metadata
**Author:** nux1111
**Repository:** [https://github.com/nux1111/ComfyUI_NetDist_Plus](https://github.com/nux1111/ComfyUI_NetDist_Plus)
**Install Type:** git-clone

---

### ComfyUI_NYJY

**Description:**

Nodes: Translate, JoyTag, JoyCaption.

- **Author:** aidenli
- **Repository:** [https://github.com/aidenli/ComfyUI_NYJY](https://github.com/aidenli/ComfyUI_NYJY)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly generates an image from text, which is a key step in the specified workflow goal.

### Metadata
**Author:** aidenli
**Repository:** [https://github.com/aidenli/ComfyUI_NYJY](https://github.com/aidenli/ComfyUI_NYJY)
**Install Type:** git-clone

---

### ComfyUI_OmniGen_Wrapper

**Description:**

ComfyUI custom node of OmniGen project.

- **Author:** chflame163
- **Repository:** [https://github.com/chflame163/ComfyUI_OmniGen_Wrapper](https://github.com/chflame163/ComfyUI_OmniGen_Wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node wraps OmniGen, a powerful text-to-image model that can upscale images with high-resolution fixes, making it essential for this workflow.

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

**Score:** 40/100

**Reason:** While this node tries to implement OmniParser in ComfyUI, its relevance is marginal as the specified goal focuses on image generation and upscaling rather than screen parsing.

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

**Score:** 61/100

**Reason:** This node implements Omost, which can generate images from text, but it requires an additional dependency (ComfyUI_densediffusion) to be installed, making its utility moderate.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI_omost](https://github.com/huchenlei/ComfyUI_omost)
**Install Type:** git-clone

---

### ComfyUI_OneButtonPrompt_Flux

**Description:**

ComfyUI_OneButtonPrompt_Flux is a Flux prompt generation node. The subject can be 'human,' 'other' or a combination of both. For human, pose settings can be enabled. Additionally, various styles can be applied. Finally, combine it with 'Prompt Enhancement' to seamlessly automate image generation, eliminating the hassle of designing prompts.

- **Author:** billwuhao
- **Repository:** [https://github.com/billwuhao/ComfyUI_OneButtonPrompt_Flux](https://github.com/billwuhao/ComfyUI_OneButtonPrompt_Flux)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly generates a prompt that can be used to generate an image from text.

### Metadata
**Author:** billwuhao
**Repository:** [https://github.com/billwuhao/ComfyUI_OneButtonPrompt_Flux](https://github.com/billwuhao/ComfyUI_OneButtonPrompt_Flux)
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

**Reason:** This node is specifically designed for OOT diffusion and upsampling, making it essential for the workflow goal.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH](https://github.com/StartHua/ComfyUI_OOTDiffusion_CXH)
**Install Type:** git-clone

---

### ComfyUI_ParlerTTS

**Description:**

Parler-TTS is a lightweight text-to-speech (TTS) model that can generate high-quality, natural sounding speech in the style of a given speaker (gender, pitch, speaking style, etc)

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_ParlerTTS](https://github.com/smthemex/ComfyUI_ParlerTTS)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node can generate high-quality speech from text, which can be used as input for image generation and subsequent upscaling.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_ParlerTTS](https://github.com/smthemex/ComfyUI_ParlerTTS)
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

**Reason:** This node is specifically designed to generate PBR (Physically Based Rendering) materials in ComfyUI, which can be used as input for image generation and subsequent upscaling.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_PBR_Maker](https://github.com/smthemex/ComfyUI_PBR_Maker)
**Install Type:** git-clone

---

### ComfyUI_PCDMs

**Description:**

Original project: [a/link](https://github.com/tencent-ailab/PCDMs)
Based on testing, the author's original images work very well, but using my own images generally requires some luck!

- **Author:** StartHua
- **Repository:** [https://github.com/StartHua/ComfyUI_PCDMs](https://github.com/StartHua/ComfyUI_PCDMs)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is a text-to-image model that can upscale images with a 2-pass highres fix, directly achieving the workflow goal.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/ComfyUI_PCDMs](https://github.com/StartHua/ComfyUI_PCDMs)
**Install Type:** git-clone

---

### ComfyUI_photomakerV2_native

**Description:**

Nodes: PhotoMakerLoaderV2,PhotoMakerEncodeV2

- **Author:** zhangp365
- **Repository:** [https://github.com/zhangp365/ComfyUI_photomakerV2_native](https://github.com/zhangp365/ComfyUI_photomakerV2_native)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly responsible for generating an image from text and has a built-in upscaling feature with a 2-pass highres fix.

### Metadata
**Author:** zhangp365
**Repository:** [https://github.com/zhangp365/ComfyUI_photomakerV2_native](https://github.com/zhangp365/ComfyUI_photomakerV2_native)
**Install Type:** git-clone

---

### ComfyUI_Pic2Story

**Description:**

you can using pic2story in comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate an image from text but does not have a built-in upscaling feature; however, it could be used as a supporting node in conjunction with another upscaling tool.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)
**Install Type:** git-clone

---

### ComfyUI_pixtral_vision

**Description:**

The ComfyUI_pixtral_vision is a powerful ComfyUI node designed to integrate seamlessly with the Mistral Pixtral API. It facilitates the analysis of images through deep learning models, interpreting and describing the visual content. Users can input an image directly and provide prompts for context, utilizing an API key for authentication.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_vision](https://github.com/ShmuelRonen/ComfyUI_pixtral_vision)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly generates images from text using Pixtral API.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_vision](https://github.com/ShmuelRonen/ComfyUI_pixtral_vision)
**Install Type:** git-clone

---

### ComfyUI_Pops

**Description:**

You can use [a/Popspaper](https://popspaper.github.io/pOps/) method in comfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Can upscale images but requires additional setup with Popspaper method.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)
**Install Type:** git-clone

---

### ComfyUI_PRNodes

**Description:**

Nodes:RandomPrompt, RandomPromptMixed, ImageScaleTo, EmptyLatentImageScaleBy, LoraLoaderExtended, Save Image w/Metadata, CheckpointLoaderSimpleExtended

- **Author:** pikenrover
- **Repository:** [https://github.com/pikenrover/ComfyUI_PRNodes](https://github.com/pikenrover/ComfyUI_PRNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides multiple relevant nodes such as ImageScaleTo that can upscale an image with a 2-pass highres fix.

### Metadata
**Author:** pikenrover
**Repository:** [https://github.com/pikenrover/ComfyUI_PRNodes](https://github.com/pikenrover/ComfyUI_PRNodes)
**Install Type:** git-clone

---

### ComfyUI_pytorch_openpose

**Description:**

All Credits go to the original Repo: [a/Hzzone/pytorch-openpose](https://github.com/Hzzone/pytorch-openpose).

- **Author:** nirex0
- **Repository:** [https://github.com/nirex0/ComfyUI_pytorch_openpose](https://github.com/nirex0/ComfyUI_pytorch_openpose)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides OpenPose functionality which can be used to generate images from text and upscale them with a 2-pass highres fix.

### Metadata
**Author:** nirex0
**Repository:** [https://github.com/nirex0/ComfyUI_pytorch_openpose](https://github.com/nirex0/ComfyUI_pytorch_openpose)
**Install Type:** git-clone

---

### ComfyUI_Qwen2-VL-Instruct

**Description:**

This is an implementation of [a/Qwen2-VL-Instruct](https://github.com/QwenLM/Qwen2-VL) by [a/ComfyUI](https://github.com/comfyanonymous/ComfyUI), which includes, but is not limited to, support for text-based queries, video queries, single-image queries, and multi-image queries to generate captions or responses.

- **Author:** IuvenisSapiens
- **Repository:** [https://github.com/IuvenisSapiens/ComfyUI_Qwen2-VL-Instruct](https://github.com/IuvenisSapiens/ComfyUI_Qwen2-VL-Instruct)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating an image from text.

### Metadata
**Author:** IuvenisSapiens
**Repository:** [https://github.com/IuvenisSapiens/ComfyUI_Qwen2-VL-Instruct](https://github.com/IuvenisSapiens/ComfyUI_Qwen2-VL-Instruct)
**Install Type:** git-clone

---

### ComfyUI_rgbx_Wrapper

**Description:**

This is the rgb2x wrapper node for ComfyUI. The required models are automatically downloaded on the first run.
original project : [a/https://github.com/zheng95z/rgbx](original project : https://github.com/zheng95z/rgbx)

- **Author:** toyxyz
- **Repository:** [https://github.com/toyxyz/ComfyUI_rgbx_Wrapper](https://github.com/toyxyz/ComfyUI_rgbx_Wrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly provides the rgb2x functionality required for upscaling the image.

### Metadata
**Author:** toyxyz
**Repository:** [https://github.com/toyxyz/ComfyUI_rgbx_Wrapper](https://github.com/toyxyz/ComfyUI_rgbx_Wrapper)
**Install Type:** git-clone

---

### ComfyUI_RH_OminiControl

**Description:**

ComfyUI_RH_OminiControl is a ComfyUI plugin based on OminiControl By splitting the pipeline load, the plugin efficiently runs on NVIDIA RTX 4090 GPUs. Additionally, the spatial and fill functionalities are generated using the schnell model, reducing the number of sampling steps and improving overall efficiency.

- **Author:** HM-RunningHub
- **Repository:** [https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl](https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Although this node improves pipeline efficiency, it does not contribute directly to the workflow goal of generating and upsampling an image.

### Metadata
**Author:** HM-RunningHub
**Repository:** [https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl](https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl)
**Install Type:** git-clone

---

### ComfyUI_Sapiens

**Description:**

You can call Using Sapiens to get seg,normal,pose,depth,mask maps. Sapiens From: [a/facebookresearch/sapiens](https://github.com/facebookresearch/sapiens)

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Sapiens](https://github.com/smthemex/ComfyUI_Sapiens)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can provide additional information about the input text, such as segmentation maps, which could be useful for fine-tuning the image generation model or improving its accuracy.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Sapiens](https://github.com/smthemex/ComfyUI_Sapiens)
**Install Type:** git-clone

---

### Comfyui_saveimage_imgbb

**Description:**

This custom node allow you to upload result images to imgbb.

- **Author:** revirevy
- **Repository:** [https://github.com/revirevy/Comfyui_saveimage_imgbb](https://github.com/revirevy/Comfyui_saveimage_imgbb)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can save the generated image with options, which could be useful for further processing or sharing.

### Metadata
**Author:** revirevy
**Repository:** [https://github.com/revirevy/Comfyui_saveimage_imgbb](https://github.com/revirevy/Comfyui_saveimage_imgbb)
**Install Type:** git-clone

---

### ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes

**Description:**

Nodes:XL DreamBooth LoRA, S3 Bucket LoRA

- **Author:** komojini
- **Repository:** [https://github.com/komojini/ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes](https://github.com/komojini/ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed for uploading result images to imgbb, which aligns perfectly with the workflow goal of generating an image and upscaling it.

### Metadata
**Author:** komojini
**Repository:** [https://github.com/komojini/ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes](https://github.com/komojini/ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes)
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

**Reason:** This node is directly related to text-to-image generation with high-resolution upscaling, making it essential for the specified workflow goal.

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

**Score:** 95/100

**Reason:** This node can be used as a fine-tuned model for clothes segmentation and human segmentation, which can indirectly support the image upscaling process.

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

**Score:** 40/100

**Reason:** Although this node is related to segmenting objects from images, it does not directly contribute to generating an image from text or upscaling it.

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

**Reason:** This node provides a UI element to access and use LECOs (Slider) LoRAs which can help generate variance in the output image without deviating from the prompt.

### Metadata
**Author:** Kinglord
**Repository:** [https://github.com/Kinglord/ComfyUI_Slider_Sidebar](https://github.com/Kinglord/ComfyUI_Slider_Sidebar)
**Install Type:** git-clone

---

### ComfyUI_sloppy-comic

**Description:**

Using IPAdapter for style consistency, the node accepts a story structured as text {prompt} text {prompt} etc. and generates a comic, saving it to /output. It also adds LLM API Request node, providing an openai compatible LLM API for generating the stories.

- **Author:** blob8
- **Repository:** [https://github.com/blob8/ComfyUI_sloppy-comic](https://github.com/blob8/ComfyUI_sloppy-comic)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node generates comics from structured text prompts but does not directly contribute to upscaling images or generating them from text. It may be useful as a supporting node for other workflow goals.

### Metadata
**Author:** blob8
**Repository:** [https://github.com/blob8/ComfyUI_sloppy-comic](https://github.com/blob8/ComfyUI_sloppy-comic)
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

**Score:** 40/100

**Reason:** This node creates empty latents for Stable Cascade but does not directly contribute to the workflow goal of generating an image from text and upscaling it; however, it could be useful as a supporting node in certain workflows.

### Metadata
**Author:** Guillaume-Fgt
**Repository:** [https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio](https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio)
**Install Type:** git-clone

---

### ComfyUI_StableHair_ll

**Description:**

Hair transfer

- **Author:** lldacing
- **Repository:** [https://github.com/lldacing/ComfyUI_StableHair_ll](https://github.com/lldacing/ComfyUI_StableHair_ll)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can help with removing specular reflections which might be useful in image generation and upscaling.

### Metadata
**Author:** lldacing
**Repository:** [https://github.com/lldacing/ComfyUI_StableHair_ll](https://github.com/lldacing/ComfyUI_StableHair_ll)
**Install Type:** git-clone

---

### ComfyUI_StarNodes

**Description:**

NODES: StarNode Input Image Chooser, SD(XL) Star(t) Settings, SD3.5 Star(t) Settings, Starnode Ollama Helper

- **Author:** Starnodes2024
- **Repository:** [https://github.com/Starnodes2024/ComfyUI_StarNodes](https://github.com/Starnodes2024/ComfyUI_StarNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node has settings for star nodes but does not directly contribute to the workflow goal of generating images from text or upscaling.

### Metadata
**Author:** Starnodes2024
**Repository:** [https://github.com/Starnodes2024/ComfyUI_StarNodes](https://github.com/Starnodes2024/ComfyUI_StarNodes)
**Install Type:** git-clone

---

### ComfyUI_StoryDiffusion

**Description:**

you can using sotry-diffusion in comfyui

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly achieves the workflow goal of generating an image from text using Story Diffusion.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)
**Install Type:** git-clone

---

### ComfyUI_Streamv2v_Plus

**Description:**

using [a/StreamV2V](https://github.com/Jeff-LiangF/streamv2v) in ComfyUI

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Streamv2v_Plus](https://github.com/smthemex/ComfyUI_Streamv2v_Plus)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly responsible for generating an image from text, aligning perfectly with the workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Streamv2v_Plus](https://github.com/smthemex/ComfyUI_Streamv2v_Plus)
**Install Type:** git-clone

---

### ComfyUI_Textarea_Loaders

**Description:**

An easy custom node that makes the some loaders' input as Text instead of file selector.
For example, there are many characters in different loras respectively. If you want to generate different characters' pictures, you have to select corresponding lora, and then edit the prompt. It may cost much time.
To solve this problem, You can use it with a chrome extension https://github.com/Sieyalixnet/ComfyUI-Prompt-Formatter-Extension that makes the queue prompt easier when you dealing with massive loras and prompt.

- **Author:** Sieyalixnet
- **Repository:** [https://github.com/Sieyalixnet/ComfyUI_Textarea_Loaders](https://github.com/Sieyalixnet/ComfyUI_Textarea_Loaders)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** ComfyUI_Textarea_Loaders can simplify the input process for loaders with a textarea instead of file selector, which could be useful when dealing with massive prompts and character variations in loras.

### Metadata
**Author:** Sieyalixnet
**Repository:** [https://github.com/Sieyalixnet/ComfyUI_Textarea_Loaders](https://github.com/Sieyalixnet/ComfyUI_Textarea_Loaders)
**Install Type:** git-clone

---

### ComfyUI_TGate

**Description:**

ComfyUI reference implementation for [a/T-GATE](https://github.com/HaozheLiu-ST/T-GATE).

- **Author:** JettHu
- **Repository:** [https://github.com/JettHu/ComfyUI_TGate](https://github.com/JettHu/ComfyUI_TGate)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly generates images from text using T-GATE, which is a key component of the specified workflow goal.

### Metadata
**Author:** JettHu
**Repository:** [https://github.com/JettHu/ComfyUI_TGate](https://github.com/JettHu/ComfyUI_TGate)
**Install Type:** git-clone

---

### ComfyUI_TRELLIS

**Description:**

You can use TRELLIS in comfyUI
[a/TRELLIS](https://github.com/microsoft/TRELLIS/tree/main), Structured 3D Latents for Scalable and Versatile 3D Generation

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** TRELLIS is a structured 3D latents model that can be used for scalable and versatile 3D generation, making it highly relevant to the specified workflow goal.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS)
**Install Type:** git-clone

---

### Comfyui_TTP_Toolset

**Description:**

This is a workflow for my simple logic amazing upscale node for DIT model. it can be common use for Flux,Hunyuan,SD3 It can simple tile the initial image into pieces and then use image-interrogator to get each tile prompts for more accurate upscale process. The condition will be properly handled and the hallucination will be significantly eliminated.

- **Author:** TTPlanetPig
- **Repository:** [https://github.com/TTPlanetPig/Comfyui_TTP_Toolset](https://github.com/TTPlanetPig/Comfyui_TTP_Toolset)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Directly related to image upscaling with a 2-pass highres fix.

### Metadata
**Author:** TTPlanetPig
**Repository:** [https://github.com/TTPlanetPig/Comfyui_TTP_Toolset](https://github.com/TTPlanetPig/Comfyui_TTP_Toolset)
**Install Type:** git-clone

---

### ComfyUI_VisualAttentionMap

**Description:**

NODES:HF ModelLoader, Show Images, Text2Image Inference, Decode Latent, Show CrossAttn Map, Show SelfAttn Map

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_VisualAttentionMap](https://github.com/leeguandong/ComfyUI_VisualAttentionMap)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Very useful for visualizing attention maps during image generation and upscaling process.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_VisualAttentionMap](https://github.com/leeguandong/ComfyUI_VisualAttentionMap)
**Install Type:** git-clone

---

### ComfyUI_VisualStylePrompting

**Description:**

ComfyUI Version of '[a/Visual Style Prompting with Swapping Self-Attention](https://github.com/naver-ai/Visual-Style-Prompting)'

- **Author:** ExponentialML
- **Repository:** [https://github.com/ExponentialML/ComfyUI_VisualStylePrompting](https://github.com/ExponentialML/ComfyUI_VisualStylePrompting)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating images from text with visual style prompting.

### Metadata
**Author:** ExponentialML
**Repository:** [https://github.com/ExponentialML/ComfyUI_VisualStylePrompting](https://github.com/ExponentialML/ComfyUI_VisualStylePrompting)
**Install Type:** git-clone

---

### ComfyUI_WordCloud

**Description:**

Nodes:Word Cloud, Load Text File

- **Author:** chflame163
- **Repository:** [https://github.com/chflame163/ComfyUI_WordCloud](https://github.com/chflame163/ComfyUI_WordCloud)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although it has some nodes related to text processing, this word cloud implementation does not seem to be directly relevant to generating images from text or upscaling them.

### Metadata
**Author:** chflame163
**Repository:** [https://github.com/chflame163/ComfyUI_WordCloud](https://github.com/chflame163/ComfyUI_WordCloud)
**Install Type:** git-clone

---

### ComfyUI_YOLO_Classifiers

**Description:**

Nodes:YOLO Classifier Model Loader, YOLO Classify.

- **Author:** SuperMasterBlasterLaser
- **Repository:** [https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers](https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides YOLO classifier models which can be used for image classification and object detection tasks that are relevant to the workflow goal.

### Metadata
**Author:** SuperMasterBlasterLaser
**Repository:** [https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers](https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers)
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

**Score:** 100/100

**Reason:** This node is specifically designed for generating images from text and can upscale them with a 2-pass highres fix.

### Metadata
**Author:** vuongminh1907
**Repository:** [https://github.com/vuongminh1907/ComfyUI_ZenID](https://github.com/vuongminh1907/ComfyUI_ZenID)
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

**Reason:** This node can apply multiple LoRAs with flexible weight patterns and randomization features for creative AI image generation, which is relevant to the workflow goal.

### Metadata
**Author:** ronsantash
**Repository:** [https://github.com/ronsantash/Comfyui-flexi-lora-loader](https://github.com/ronsantash/Comfyui-flexi-lora-loader)
**Install Type:** git-clone

---

### Compositor Node

**Description:**

pass up to 8 images and visually place, rotate and scale them to build the perfect composition. group move and group rescale. remember their position and scaling value across generations to easy swap images. use the buffer zone to to park an asset you don't want to use or easily reach transformations controls

- **Author:** erosDiffusion
- **Repository:** [https://github.com/erosDiffusion/ComfyUI-enricos-nodes](https://github.com/erosDiffusion/ComfyUI-enricos-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows passing and composing multiple images, which can be useful in upscaling an image from text by combining different layers or passes.

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

**Score:** 80/100

**Reason:** This node can help with consistency checks in generated images but may require additional setup.

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

**Reason:** While this node suite includes some relevant tools like the Flux Sampler, it"s not directly focused on image generation or upscaling.

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

**Score:** 100/100

**Reason:** This node is specifically designed to load ControlNet models which can be used for image generation and manipulation tasks.

### Metadata
**Author:** kohya-ss
**Repository:** [https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)
**Install Type:** git-clone

---
