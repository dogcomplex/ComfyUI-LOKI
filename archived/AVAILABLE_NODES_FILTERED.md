# Filtered Nodes for: upscale an image

Total Available Nodes: 1865
Batch Size: 4
Estimated Processing Time: 38.9 minutes

## Results

### abg-comfyui

**Description:**

Nodes: Remove Image Background (abg). A Anime Background Remover node for comfyui, based on this hf space, works same as AGB extention in automatic1111.

- **Author:** kwaroran
- **Repository:** [https://github.com/kwaroran/abg-comfyui](https://github.com/kwaroran/abg-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node removes image backgrounds which can be useful in preparing images for upscaling.

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

**Score:** 80/100

**Reason:** This node is very useful as it allows adding custom text to the generated images, which can be used in conjunction with upscaling.

### Metadata
**Author:** fanfanfan
**Repository:** [https://github.com/yuan199696/add_text_2_img](https://github.com/yuan199696/add_text_2_img)
**Install Type:** git-clone

---

### Advanced Reflux control

**Description:**

This extension offers a new Apply-Style node for Redux that allows for changing the influence of the conditioning image on the final outcome. This effectively allows for changing the style or content of an image using a prompt while using Redux.

- **Author:** Kai Duehrkop
- **Repository:** [https://github.com/kaibioinfo/ComfyUI_AdvancedRefluxControl](https://github.com/kaibioinfo/ComfyUI_AdvancedRefluxControl)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This extension allows changing the influence of conditioning images on the final outcome, which can be useful for image manipulation and potentially upscaling.

### Metadata
**Author:** Kai Duehrkop
**Repository:** [https://github.com/kaibioinfo/ComfyUI_AdvancedRefluxControl](https://github.com/kaibioinfo/ComfyUI_AdvancedRefluxControl)
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

**Reason:** These utility nodes provide functionality for passing images and latents in AegisFlow Shima, but their direct relevance to image upscaling is limited.

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

**Reason:** This node is a comprehensive toolkit with multiple nodes that can be used for various tasks including potentially image processing or manipulation.

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

**Score:** 100/100

**Reason:** This node is directly related to image upscaling using Amazon Bedrock service.

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

**Reason:** AnimateDiff integration can upscale images but may require additional setup and model downloads.

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

**Reason:** AnimateDiff Evolved provides improved AnimateDiff integration for image upscaling with various motion models available.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
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

**Reason:** This node pack contains some image handling nodes that could be useful for tasks like inpainting but it may not directly contribute to the goal of upsampling an image.

### Metadata
**Author:** antrobot
**Repository:** [https://github.com/antrobot1234/antrobots-comfyUI-nodepack](https://github.com/antrobot1234/antrobots-comfyUI-nodepack)
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

**Reason:** This AsyncDiff node can be used to efficiently compute differences between images, which could be useful in certain image upscaling techniques.

### Metadata
**Author:** SlackinJack
**Repository:** [https://github.com/SlackinJack/asyncdiff_comfyui](https://github.com/SlackinJack/asyncdiff_comfyui)
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

**Reason:** This node is very useful for removing background from multiple images at once, which might be necessary before upscaling.

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

**Reason:** This node contains several relevant operations such as Resize Image and Combine images (Background+Overlay alpha) that can be used for upscaling an image.

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

**Reason:** This custom node provides flexible control over aspect ratios and upscale factors making it very useful for dynamically creating latents that fit specific tiling and resolution needs.

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

**Reason:** Some nodes in this collection (e.g. Empty Latent Image from Aspect-Ratio) might be marginally relevant to upscaling an image but the overall relevance is limited due to the diverse set of nodes available.

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

**Reason:** This node is a BRIA AI API node designed specifically for image processing tasks, making it essential for upscaling an image.

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

**Score:** 90/100

**Reason:** BrushNet nodes are native to ComfyUI and include a higher resolution feature (HiDiffusion) that can be used for upscaling images.

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

**Score:** 80/100

**Reason:** This node contains various tools for scaling and refining images, making it moderately useful for the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node provides a full-page image editor with mask support, making it very useful for upscaling an image.

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

**Reason:** This node has various animation-related nodes that could be useful in a broader AI art workflow, but none directly relevant to upscaling an image.

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

**Score:** 41/100

**Reason:** This node can pad an image to be square but does not directly upscale the image, making it moderately useful for this workflow goal.

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

**Reason:** This node provides a collection of custom nodes that can potentially include upscaling functionality, making it essential for this workflow goal.

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

**Score:** 41/100

**Reason:** This node can be used as a supporting tool for mathematical calculations that might be required in certain image processing tasks.

### Metadata
**Author:** clhui
**Repository:** [https://github.com/clhui/ComfyUi-clh-Tool](https://github.com/clhui/ComfyUi-clh-Tool)
**Install Type:** git-clone

---

### Comfy Controller

**Description:**

Quickly and easily build a GUI on top of your workflow. Gather just the nodes that you want to see, with no spaghetti, onto controller panels, leaving your workflow untouched in the background.

- **Author:** chrisgoringe
- **Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can help organize nodes related to upscaling an image into a GUI for easier management and visualization.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
**Install Type:** git-clone

---

### Comfy DV

**Description:**

Nodes: String Formatting (f-string and jinja2), Random Choice, Model Memory management, and other quality of life improvements.

- **Author:** Darth-Veitcher
- **Repository:** [https://github.com/darth-veitcher/comfydv](https://github.com/darth-veitcher/comfydv)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides quality of life improvements but does not directly contribute to upscaling an image; however, it could potentially be used as a supporting node.

### Metadata
**Author:** Darth-Veitcher
**Repository:** [https://github.com/darth-veitcher/comfydv](https://github.com/darth-veitcher/comfydv)
**Install Type:** git-clone

---

### comfy-cliption

**Description:**

Image to caption with CLIP ViT-L/14. Small and fast addition to the CLIP-L model you already have loaded to generate captions for images within your workflow.

- **Author:** pharmapsychotic
- **Repository:** [https://github.com/pharmapsychotic/comfy-cliption](https://github.com/pharmapsychotic/comfy-cliption)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can generate captions for images using CLIP ViT-L/14, which could be useful as part of the workflow goal to upscale an image and potentially use the generated caption for further processing or analysis.

### Metadata
**Author:** pharmapsychotic
**Repository:** [https://github.com/pharmapsychotic/comfy-cliption](https://github.com/pharmapsychotic/comfy-cliption)
**Install Type:** git-clone

---

### comfy-easy-grids

**Description:**

A set of custom nodes for creating image grids, sequences, and batches in ComfyUI.

- **Author:** shockz0rz
- **Repository:** [https://github.com/shockz0rz/comfy-easy-grids](https://github.com/shockz0rz/comfy-easy-grids)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node is moderately relevant as it provides functionality for creating image grids, sequences, and batches. However, upscaling an image is not a direct function of this node.

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

**Reason:** This node contains multiple nodes related to image processing, including loading images with metadata, generating latent noise, and combining latents into batches, making it highly relevant for upscaling an image.

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

**Reason:** This node directly integrates with Topaz Photo AI, which can upscale images.

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

**Score:** 40/100

**Reason:** Although this node provides a CLIP Encoder, it is not directly related to upscaling images.

### Metadata
**Author:** paulo-coronado
**Repository:** [https://github.com/paulo-coronado/comfy_clip_blip_node](https://github.com/paulo-coronado/comfy_clip_blip_node)
**Install Type:** git-clone

---

### comfy_PoP

**Description:**

A collection of custom nodes for ComfyUI. Includes a quick canny edge detection node with unconventional settings, simple LoRA stack nodes for workflow efficiency, and a customizable aspect ratio node.

- **Author:** picturesonpictures
- **Repository:** [https://github.com/picturesonpictures/comfy_PoP](https://github.com/picturesonpictures/comfy_PoP)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a collection of custom nodes that can aid in image upscaling and processing.

### Metadata
**Author:** picturesonpictures
**Repository:** [https://github.com/picturesonpictures/comfy_PoP](https://github.com/picturesonpictures/comfy_PoP)
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

**Score:** 80/100

**Reason:** comfygen provides a web interface that could potentially be used to upscale an image, but it"s more of a setup node rather than a direct solution.

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

**Score:** 90/100

**Reason:** ComfyI2I is specifically designed for image-to-image functions, making it highly relevant and useful for upscaling images.

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

**Reason:** ComfyKit Custom Nodes provides some general-purpose nodes that might be indirectly useful for upscaling an image, but they are not directly related to the goal.

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

**Reason:** This node offers a wide range of mathematical operations that could be useful for implementing complex algorithms required in image upscaling.

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

**Score:** 90/100

**Reason:** ComfyS3 provides seamless integration with Amazon S3 for loading and saving images, which is relevant to the workflow goal of upsampling an image.

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

**Score:** 90/100

**Reason:** This node is very useful as it provides native support for DynamiCrafter, which can be used in conjunction with other nodes to upscale an image.

### Metadata
**Author:** ExponentialML
**Repository:** [https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter)
**Install Type:** git-clone

---

### ComfyUI AnyNode: Any Node you ask for

**Description:**

Nodes: AnyNode. Nodes that can be anything you ask. Auto-Generate functional nodes using LLMs. Create impossible workflows. API Compatibility: (OpenAI, LocalLLMs, Gemini).

- **Author:** lks-ai
- **Repository:** [https://github.com/lks-ai/anynode](https://github.com/lks-ai/anynode)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for upscaling an image as it can auto-generate functional nodes using LLMs, allowing for the creation of custom workflows tailored to this specific goal.

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

**Score:** 80/100

**Reason:** This node enhances old or low-quality images and can be used for upscaling purposes.

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

**Reason:** This node loads config for sampler nodes from a yaml file which might be useful in certain deep learning workflows, but its direct relevance to image upscaling is limited.

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

**Reason:** This node enables coherent video generation while maintaining efficient memory usage, making it very useful for tasks that involve video processing or upsampling.

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

**Reason:** This node allows setting sigma values directly which can be useful for denoising and potentially upscaling images.

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

**Score:** 50/100

**Reason:** This extension provides batch processing nodes which could be useful in a workflow that involves multiple images or tasks related to upscaling.

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

**Score:** 80/100

**Reason:** This node provides a deep learning-based face recognition model that can also be used for image manipulation and enhancement, making it moderately useful for upscaling images.

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

**Score:** 90/100

**Reason:** This node is specifically designed for image upscaling using the DenseDiffusion algorithm, making it very useful for this workflow goal.

### Metadata
**Author:** huchenlei
**Repository:** [https://github.com/huchenlei/ComfyUI_densediffusion](https://github.com/huchenlei/ComfyUI_densediffusion)
**Install Type:** git-clone

---

### ComfyUI Easy Civitai (XTNodes)

**Description:**

Load your model with image previews, or directly download and import Civitai models via URL. This custom ComfyUI node supports Checkpoint, LoRA, and LoRA Stack models, offering features like bypass options.

- **Author:** X-T-E-R
- **Repository:** [https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes](https://github.com/X-T-E-R/ComfyUI-EasyCivitai-XTNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows easy Civitai model loading with features like bypass options, which can be useful in conjunction with other nodes for image upscaling.

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

**Score:** 40/100

**Reason:** While not directly relevant, it could potentially be used as a supporting node for preparing the image before upscaling.

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

**Score:** 80/100

**Reason:** This node provides essential functionality that could be necessary for various tasks including upscaling an image.

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

**Score:** 81/100

**Reason:** ComfyUI fabric is specifically designed for image upscaling and offers advanced features like attention-based reference image conditioning.

### Metadata
**Author:** ssitu
**Repository:** [https://github.com/ssitu/ComfyUI_fabric](https://github.com/ssitu/ComfyUI_fabric)
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

**Reason:** This node accelerates Flux.1 image generation which can be useful for upscaling images.

### Metadata
**Author:** discus0434
**Repository:** [https://github.com/discus0434/comfyui-flux-accelerator](https://github.com/discus0434/comfyui-flux-accelerator)
**Install Type:** git-clone

---

### ComfyUI Frame Maker

**Description:**

This node creates a sequence of frames by moving and scaling a subject image over a background image.

- **Author:** diSty
- **Repository:** [https://github.com/diStyApps/ComfyUI_FrameMaker](https://github.com/diStyApps/ComfyUI_FrameMaker)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can create intermediate frames by scaling and moving the subject image over the background image, which can be useful for image upscaling.

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

**Score:** 80/100

**Reason:** This node provides an implementation of the Hallo model for image upscaling, making it highly relevant and useful for this workflow goal.

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

**Reason:** This node is a simple custom implementation of HiDiffusion technology but lacks specific features or details about its utility for image upscaling.

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

**Score:** 90/100

**Reason:** This node provides a custom pack with nodes to enhance images through Sampler, Upscaler, Mask, and more, making it very useful for this workflow goal.

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

**Reason:** This node pack offers various nodes that can be used for iterative upscaling and enhancing facial details.

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

**Score:** 40/100

**Reason:** This subpack is necessary for the Impact Pack but does not directly contribute to upscaling an image on its own.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
**Install Type:** git-clone

---

### ComfyUI InstantID (Native Support)

**Description:**

Native [a/InstantID](https://github.com/InstantID/InstantID) support for ComfyUI.
This extension differs from the many already available as it doesn't use diffusers but instead implements InstantID natively and it fully integrates with ComfyUI.
Please note this still could be considered beta stage, looking forward to your feedback.

- **Author:** cubiq
- **Repository:** [https://github.com/cubiq/ComfyUI_InstantID](https://github.com/cubiq/ComfyUI_InstantID)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This native InstantID support could be useful for tasks like inpainting or face manipulation which are related to image processing.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/ComfyUI_InstantID](https://github.com/cubiq/ComfyUI_InstantID)
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

**Reason:** This faceswapper node is specifically designed for face swapping and can be useful in image upscaling workflows that involve manipulating facial features.

### Metadata
**Author:** nosiu
**Repository:** [https://github.com/nosiu/comfyui-instantId-faceswap](https://github.com/nosiu/comfyui-instantId-faceswap)
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

**Reason:** This node provides some utility for image manipulation but does not directly contribute to the goal of upscaling an image.

### Metadata
**Author:** chflame163
**Repository:** [https://github.com/chflame163/ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle)
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

**Reason:** This node can improve the inpainting results which are often used in conjunction with upscaling techniques.

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

**Reason:** This minimap can help navigate the full workflow, making it easier to find and use nodes for upscaling an image.

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

**Reason:** This node allows downloading models necessary for image upscaling, making it essential for this workflow.

### Metadata
**Author:** ciri
**Repository:** [https://github.com/ciri/comfyui-model-downloader](https://github.com/ciri/comfyui-model-downloader)
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

**Reason:** This node seems to be related to video generation and may indirectly aid in image upscaling by providing a video upscale option.

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

**Score:** 100/100

**Reason:** This node is specifically designed for rapid latent upscaling using a compact neural network, making it essential for the workflow goal of upsampling an image.

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

**Score:** 90/100

**Reason:** Although this toolkit provides extensive functionality for designing and training neural networks, its Neural Network Toolkit (NNT) nodes can be used to create custom upscaling models, making it very useful for the specified workflow goal.

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

**Reason:** This node can be marginally useful for resetting nodes in the workflow, but it does not directly contribute to upscaling an image.

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

**Score:** 90/100

**Reason:** This node is very relevant as it provides pre-trained models specifically designed for upscaling images using ControlNext-SVD v2.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-ControlNeXt-SVD](https://github.com/kijai/ComfyUI-ControlNeXt-SVD)
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

**Reason:** Style-Aligned appears to be a node for style transfer and could potentially be used in conjunction with other nodes for image upscaling.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_Style_Aligned](https://github.com/leeguandong/ComfyUI_Style_Aligned)
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

**Reason:** This node computes optical flow between pairs of images and can be used to upscale an image by applying the flow.

### Metadata
**Author:** seanlynch
**Repository:** [https://github.com/seanlynch/comfyui-optical-flow](https://github.com/seanlynch/comfyui-optical-flow)
**Install Type:** git-clone

---

### ComfyUI PhotoMaker (ZHO)

**Description:**

Unofficial implementation of [a/PhotoMaker](https://github.com/TencentARC/PhotoMaker) for ComfyUI

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO](https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node is an unofficial implementation of PhotoMaker, it does not directly support upscaling images, making it marginally relevant to the workflow goal.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO](https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO)
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

**Score:** 80/100

**Reason:** This node provides a ComfyUI reference implementation for PhotoMaker models, including V2, which supports image upscaling and makes it very useful for this workflow goal.

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

**Score:** 100/100

**Reason:** This node is essential for this workflow as it integrates a powerful vision model specifically designed for image upscaling and multimodal AI capabilities within ComfyUI.

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

**Score:** 81/100

**Reason:** This node can generate images from text prompts using AI models, which could be used as a starting point for further processing or editing to upscale the image.

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

**Score:** 60/100

**Reason:** This node can apply LoRA or HN based on specifications within a prompt, which could be useful in upscaling an image if the prompt includes relevant information.

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

**Reason:** This node is a custom implementation of ProPainter, which is specifically designed for video inpainting tasks, making it directly relevant to upscaling images.

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

**Reason:** This node wraps the PyramidFlow model, which is known for its image and video super-resolution capabilities, making it highly useful for upscaling images.

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

**Reason:** This node provides a direct implementation of a texture generation technique specifically useful for removing objects from images or inpainting, which can be related to upscaling and detail manipulation.

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

**Reason:** This node provides a TensorRT implementation of RIFE for ultra fast frame interpolation which can be related to upscaling and detail manipulation.

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

**Reason:** The SAM2 node specifically adapts functionalities for image manipulation, making it highly relevant for the workflow goal of upsampling an image.

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

**Reason:** This node allows for segmenting images, which could be a necessary step in preparing an image for upscaling.

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

**Reason:** This node provides a diffusion-based model for image segmentation and manipulation, which might be useful for preprocessing or enhancing the image before upscaling.

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

**Score:** 80/100

**Reason:** This node bundle contains several nodes that could be useful for upscaling an image, such as SeamlessTexture and AspectRatioPlus.

### Metadata
**Author:** SKBv0
**Repository:** [https://github.com/SKBv0/ComfyUI_SKBundle](https://github.com/SKBv0/ComfyUI_SKBundle)
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

**Reason:** This node directly supports image upscaling using Stable Video Diffusion, making it very useful for achieving the workflow goal.

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

**Score:** 100/100

**Reason:** This node is directly relevant to the workflow goal as it can be used to upscale images by matching templates or patterns in the image.

### Metadata
**Author:** wentao-uw
**Repository:** [https://github.com/wentao-uw/ComfyUI-template-matching](https://github.com/wentao-uw/ComfyUI-template-matching)
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

**Reason:** This node provides a direct implementation for fast image upscaling inside ComfyUI, making it very useful for this specific workflow goal.

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

**Score:** 100/100

**Reason:** This node provides direct control over brightness, contrast, saturation, and hue during image generation, making it essential for fine-tuning the output of an image upscaling workflow.

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

**Score:** 80/100

**Reason:** This node supports features such as video super-resolution, which can be used for image upscaling, making it very useful for this workflow goal.

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

**Score:** 80/100

**Reason:** This node is very useful as a supporting tool for interactive visual projects and enhancing ComfyUI workflows with efficient content management and display, but not directly related to upscaling an image.

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

**Score:** 90/100

**Reason:** This node is highly relevant and useful as it captures images from your webcam one at a time, which can be used in img2img or controlnet workflows for upscaling an image.

### Metadata
**Author:** victorchall
**Repository:** [https://github.com/victorchall/comfyui_webcamcapture](https://github.com/victorchall/comfyui_webcamcapture)
**Install Type:** git-clone

---

### comfyui's gaffer(ComfyUI native implementation of IC-Light. )

**Description:**

Nodes:Load ICLight Model,Apply ICLight,Simple Light Source,Calculate Normal Map

- **Author:** ray
- **Repository:** [https://github.com/huagetai/ComfyUI-Gaffer](https://github.com/huagetai/ComfyUI-Gaffer)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a native implementation of IC-Light, which can be used as a preprocessor for image upscaling tasks.

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

**Score:** 100/100

**Reason:** This node suite enables ComfyUI to process images and videos using cutting-edge algorithms, making it essential for upscaling an image.

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

**Reason:** This custom node can upscale an image by rendering a zoom-in or dolly zoom video, making it very useful for the specified workflow goal.

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

**Reason:** This node allows for scheduling ControlNet strength across timesteps and applying custom weights and attention masks, which can be useful in advanced image upscaling techniques.

### Metadata
**Author:** Kosinkadink
**Repository:** [https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
**Install Type:** git-clone

---

### ComfyUI-AI-Assistant

**Description:**

ComfyUI native implementation of [a/AI-Assistant](https://github.com/tori29umai0123/AI-Assistant).

- **Author:** JackEllie
- **Repository:** [https://github.com/JackEllie/ComfyUI_AI_Assistant](https://github.com/JackEllie/ComfyUI_AI_Assistant)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is an AI assistant which can be used to upscale images by providing guidance on the process or suggesting relevant techniques.

### Metadata
**Author:** JackEllie
**Repository:** [https://github.com/JackEllie/ComfyUI_AI_Assistant](https://github.com/JackEllie/ComfyUI_AI_Assistant)
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

**Reason:** This node directly supports image generation using text prompts and can upscale images with high quality.

### Metadata
**Author:** bombax-xiaoice
**Repository:** [https://github.com/bombax-xiaoice/ComfyUI-Allegro](https://github.com/bombax-xiaoice/ComfyUI-Allegro)
**Install Type:** git-clone

---

### ComfyUI-Animation_Nodes_and_Workflows

**Description:**

These are nodes and workflows that can facilitate the creation of animations and video compilations.

- **Author:** Isi-dev
- **Repository:** [https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows](https://github.com/Isi-dev/ComfyUI-Animation_Nodes_and_Workflows)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node provides a collection of animation nodes and workflows, it does not directly address the task of image upscaling.

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

**Score:** 100/100

**Reason:** Directly provides image upscaling functionality.

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

**Reason:** Provides APG scaling for better image quality, relevant to upscaling an image.

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

**Score:** 80/100

**Reason:** Offers upscale models specifically designed for ComfyUI, making it moderately useful for the goal.

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

**Reason:** This comprehensive set of custom nodes includes utilities for image processing making it very useful for upscaling an image.

### Metadata
**Author:** sipherxyz
**Repository:** [https://github.com/sipherxyz/comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture)
**Install Type:** git-clone

---

### ComfyUI-ascii-art

**Description:**

This is a custom node to convert image to ascii art string.

- **Author:** Tomudo
- **Repository:** [https://github.com/tomudo/ComfyUI-ascii-art](https://github.com/tomudo/ComfyUI-ascii-art)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can convert images to ASCII art, which is marginally relevant to the workflow goal of upscaling an image.

### Metadata
**Author:** Tomudo
**Repository:** [https://github.com/tomudo/ComfyUI-ascii-art](https://github.com/tomudo/ComfyUI-ascii-art)
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

**Reason:** This node provides a keyframe-based animation feature that could be used in conjunction with other nodes for more complex image processing tasks, including potentially upscaling an image as part of a larger animation pipeline.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-AstralAnimator](https://github.com/ShmuelRonen/ComfyUI-AstralAnimator)
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

**Reason:** This node provides color correction functionality which may be useful in post-processing an upscaled image.

### Metadata
**Author:** A4P7J1N7M05OT
**Repository:** [https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp](https://github.com/A4P7J1N7M05OT/ComfyUI-AutoColorGimp)
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

**Score:** 81/100

**Reason:** This node is very useful for upscaling an image as it can automatically adjust CFG settings to improve quality and reduce artifacts.

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

**Score:** 61/100

**Reason:** This node is moderately useful for upscaling an image as it optimizes the latent space for generating high-quality results.

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

**Score:** 80/100

**Reason:** This node directly contributes to editing backgrounds of images, which can be a necessary step before upscaling an image.

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

**Score:** 60/100

**Reason:** This node provides a CharacterPipe node that can manage various elements such as images, prompts, and models in a single structure, making it moderately useful for upscaling character-based images.

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

**Reason:** This node is a Bilateral Reference Network model specifically designed for image upscaling, making it essential for the workflow goal.

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

**Score:** 100/100

**Reason:** This node is also a Bilateral Reference Network model optimized for better matting accuracy in image upscaling, making it highly relevant and useful.

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

**Reason:** This node is a lightweight version of BiRefNet with features like chunked loading and model caching, which can significantly improve the efficiency of the image upscaling workflow.

### Metadata
**Author:** duhaifeng
**Repository:** [https://github.com/rubi-du/ComfyUI-BiRefNet-Super](https://github.com/rubi-du/ComfyUI-BiRefNet-Super)
**Install Type:** git-clone

---

### ComfyUI-Book-Tools Nodes for ComfyUI

**Description:**

ComfyUI-Book-Tools is a set o new nodes for ComfyUI that allows users to easily add text overlays to images within their ComfyUI projects. This Node leverages Python Imaging Library (PIL) and PyTorch to dynamically render text on images, supporting a wide range of customization options including font size, alignment, color, and padding. Loop with any parameters (*), prompt batch schedule with prompt selector, end queue for automatic ending current queue.

- **Author:** Big-Idea-Technology
- **Repository:** [https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools](https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node allows users to add text overlays to images and can be used to provide additional context or information about the upscaled image.

### Metadata
**Author:** Big-Idea-Technology
**Repository:** [https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools](https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools)
**Install Type:** git-clone

---

### ComfyUI-CADS

**Description:**

Attempts to implement [a/CADS](https://arxiv.org/abs/2310.17347) for ComfyUI. Credit also to the [a/A1111 implementation](https://github.com/v0xie/sd-webui-cads/tree/main) that I used as a reference.

- **Author:** asagi4
- **Repository:** [https://github.com/asagi4/ComfyUI-CADS](https://github.com/asagi4/ComfyUI-CADS)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node attempts to implement a/CADS which could be useful for image upscaling, but its effectiveness depends on the specific implementation and requirements of the workflow goal.

### Metadata
**Author:** asagi4
**Repository:** [https://github.com/asagi4/ComfyUI-CADS](https://github.com/asagi4/ComfyUI-CADS)
**Install Type:** git-clone

---

### ComfyUI-CascadeResolutions

**Description:**

Nodes:Cascade Resolutions

- **Author:** al-swaiti
- **Repository:** [https://github.com/al-swaiti/ComfyUI-CascadeResolutions](https://github.com/al-swaiti/ComfyUI-CascadeResolutions)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is specifically designed for handling resolutions which can be useful in upscaling an image.

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

**Reason:** This node is a virtual try-on diffusion model specifically designed for image upscaling.

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

**Reason:** This node provides ComfyUI nodes for diffusers implementation of Catvton-Flux, which can be used for image upscaling.

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

**Score:** 100/100

**Reason:** This node is a dedicated upscaler that can upscale images.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-CCSR](https://github.com/kijai/ComfyUI-CCSR)
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

**Reason:** This node directly enables the manipulation of images using CLIP-based sliders which can be used for upscaling an image.

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

**Score:** 80/100

**Reason:** This node seems to be a model specifically designed for video tasks but has a related name; it could potentially be used in conjunction with another node for image upscaling.

### Metadata
**Author:** MinusZoneAI
**Repository:** [https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ](https://github.com/MinusZoneAI/ComfyUI-CogVideoX-MZ)
**Install Type:** git-clone

---
