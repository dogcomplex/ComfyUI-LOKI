# Filtered Nodes for: Image generation guided by canny edge detection

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

**Reason:** This node is very useful as it removes image backgrounds using a Anime Background Remover, which could be used in conjunction with canny edge detection for image processing.

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

**Score:** 81/100

**Reason:** This node directly supports adding custom text to the generated images, which aligns with the workflow goal.

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

**Reason:** This node allows changing the influence of the conditioning image on the final outcome using Redux, which is relevant for guided image generation.

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

**Reason:** These nodes provide utility functions like image and latent passer, but their direct relevance to guided image generation using canny edge detection is limited.

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

**Reason:** This node contains various tools for image processing, including loading models that could be used in conjunction with canny edge detection for image generation.

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

**Reason:** Amazon Bedrock nodes provide a foundation model that could be used in conjunction with canny edge detection for image generation.

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

**Reason:** AnimateDiff is specifically designed for image manipulation and animation, making it highly relevant to the workflow goal of generating images guided by canny edge detection.

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

**Reason:** AnimateDiff Evolved is an improved version of AnimateDiff, offering more features and flexibility, which would be very useful in achieving the workflow goal.

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

**Reason:** This node is specifically designed for anime character segmentation which would be useful in extracting edges for canny edge detection.

### Metadata
**Author:** LyazS
**Repository:** [https://github.com/LyazS/comfyui-anime-seg](https://github.com/LyazS/comfyui-anime-seg)
**Install Type:** git-clone

---

### Anyline

**Description:**

A Fast, Accurate, and Detailed Line Detection Preprocessor.
Anyline is a ControlNet line preprocessor that accurately extracts object edges, image details, and textual content from most images. Users can input any type of image to quickly obtain line drawings with clear edges, sufficient detail preservation, and high fidelity text, which are then used as input for conditional generation in Stable Diffusion.

- **Author:** TheMistoAI
- **Repository:** [https://github.com/TheMistoAI/ComfyUI-Anyline](https://github.com/TheMistoAI/ComfyUI-Anyline)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Anyline accurately extracts object edges which can be used as input for conditional generation in Stable Diffusion.

### Metadata
**Author:** TheMistoAI
**Repository:** [https://github.com/TheMistoAI/ComfyUI-Anyline](https://github.com/TheMistoAI/ComfyUI-Anyline)
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

**Reason:** This node library provides a set of nodes for extracting face embeddings and generating images based on these embeddings, making it highly relevant to the workflow goal.

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

**Reason:** This AsyncDiff node can be used to compare images before and after applying canny edge detection for quality assessment.

### Metadata
**Author:** SlackinJack
**Repository:** [https://github.com/SlackinJack/asyncdiff_comfyui](https://github.com/SlackinJack/asyncdiff_comfyui)
**Install Type:** git-clone

---

### Basix Image Filters

**Description:**

A handful of image filters for ComfyUI (darken, lighten, levels, saturate, hue)

- **Author:** basix
- **Repository:** [https://github.com/maludwig/basix_image_filters](https://github.com/maludwig/basix_image_filters)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides image filters that could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** basix
**Repository:** [https://github.com/maludwig/basix_image_filters](https://github.com/maludwig/basix_image_filters)
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

**Reason:** This node directly supports removing backgrounds of plural images which is a key step in the image generation guided by canny edge detection workflow goal.

### Metadata
**Author:** Mamaaaamooooo
**Repository:** [https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes](https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes)
**Install Type:** git-clone

---

### Bobs_Latent_Optimizer

**Description:**

This custom node for ComfyUI is designed to optimize latent generation for use with FLUX, SDXL and SD3. It provides flexible control over aspect ratios, megapixel sizes, and upscale factors, allowing users to dynamically create latents that fit specific tiling and resolution needs.

- **Author:** bobsblazed
- **Repository:** [https://github.com/BobsBlazed/Bobs_Latent_Optimizer](https://github.com/BobsBlazed/Bobs_Latent_Optimizer)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** This node provides flexible control over latent generation, which could be useful in optimizing the output of an image generation task guided by canny edge detection.

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

**Reason:** Some nodes within this collection (like Empty Latent Image from Aspect-Ratio) might be marginally relevant to the workflow goal, but overall relevance is low due to the diverse nature of the node collection.

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

**Score:** 81/100

**Reason:** BrushNet provides a native implementation of inpainting algorithms that could be used for image generation with canny edge detection.

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

**Score:** 40/100

**Reason:** bsz-cui-extras contains tools for manipulating the color of latents but its relevance to canny edge detection is marginal.

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

**Reason:** This node provides a full-page image editor with mask support, making it highly relevant for the specified workflow goal.

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

**Reason:** This node includes features like prompt switch and checkpoint switch that could be useful in a workflow involving canny edge detection for image generation.

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

**Reason:** This node provides a feature for adding text over an image before saving but it may not be directly applicable to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** Smuzzies
**Repository:** [https://github.com/Smuzzies/comfyui_chatbox_overlay](https://github.com/Smuzzies/comfyui_chatbox_overlay)
**Install Type:** copy

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

**Reason:** This node provides a collection of Civitai models and LoRAs that could potentially be used for image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node provides mathematical calculation functionality which could be used to process data before or after canny edge detection for image generation.

### Metadata
**Author:** clhui
**Repository:** [https://github.com/clhui/ComfyUi-clh-Tool](https://github.com/clhui/ComfyUi-clh-Tool)
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

**Reason:** This node directly addresses contextual words in prompts and could be useful in generating images with specific context based on the prompt.

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

**Score:** 60/100

**Reason:** This node provides a text encoder with BREAK formatting which might be used to preprocess or format input data for image generation.

### Metadata
**Author:** dfl
**Repository:** [https://github.com/dfl/comfyui-clip-with-break](https://github.com/dfl/comfyui-clip-with-break)
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

**Reason:** This node provides custom nodes for ComfyUI, potentially including functionality related to image processing and edge detection.

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

**Score:** 81/100

**Reason:** This node allows for GUI customization which could be useful in organizing nodes related to canny edge detection and image generation.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-controller](https://github.com/chrisgoringe/cg-controller)
**Install Type:** git-clone

---

### Comfy UI Prompt Agent

**Description:**

Nodes: Prompt Agent, Prompt Agent (String). This script provides a prompt agent node for the Comfy UI stable diffusion client.

- **Author:** yolanother
- **Repository:** [https://github.com/yolanother/DTAIComfyPromptAgent](https://github.com/yolanother/DTAIComfyPromptAgent)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a prompt agent that could potentially be used in conjunction with canny edge detection for image generation, but its direct relevance is limited.

### Metadata
**Author:** yolanother
**Repository:** [https://github.com/yolanother/DTAIComfyPromptAgent](https://github.com/yolanother/DTAIComfyPromptAgent)
**Install Type:** git-clone

---

### comfy-cliption

**Description:**

Image to caption with CLIP ViT-L/14. Small and fast addition to the CLIP-L model you already have loaded to generate captions for images within your workflow.

- **Author:** pharmapsychotic
- **Repository:** [https://github.com/pharmapsychotic/comfy-cliption](https://github.com/pharmapsychotic/comfy-cliption)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it generates captions for images using CLIP ViT-L/14 model which could be used in conjunction with edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node is essential for creating image grids and sequences that can be used to visualize the output of the canny edge detection guided image generation workflow.

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

**Reason:** This node provides multiple nodes that are directly relevant to the workflow goal, including load Image with metadata and General Purpose Controlnet Unit which could be used for canny edge detection.

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

**Reason:** This node is very useful for the specified workflow goal as it integrates Topaz Photo AI for image enhancement, which aligns with the goal of generating images guided by canny edge detection.

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

**Reason:** This node is moderately useful for the specified workflow goal as it provides a CLIP Encoder that can receive images as input, which could be used in conjunction with other nodes to achieve the goal of image generation guided by canny edge detection.

### Metadata
**Author:** paulo-coronado
**Repository:** [https://github.com/paulo-coronado/comfy_clip_blip_node](https://github.com/paulo-coronado/comfy_clip_blip_node)
**Install Type:** git-clone

---

### Comfy_KepKitchenSink

**Description:**

Nodes: KepRotateImage

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/Comfy_KepKitchenSink](https://github.com/M1kep/Comfy_KepKitchenSink)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node could be marginally useful if used in conjunction with other nodes for image manipulation, but its primary function is rotation which may not directly contribute to the workflow goal.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/Comfy_KepKitchenSink](https://github.com/M1kep/Comfy_KepKitchenSink)
**Install Type:** git-clone

---

### Comfy_KepMatteAnything

**Description:**

This extension provides a custom node that allows the use of [a/Matte Anything](https://github.com/hustvl/Matte-Anything) in ComfyUI.

- **Author:** M1kep
- **Repository:** [https://github.com/M1kep/Comfy_KepMatteAnything](https://github.com/M1kep/Comfy_KepMatteAnything)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node could be very useful if used in conjunction with other nodes for image manipulation, as it allows the use of Matte Anything, a tool that can help with image masking and edge detection.

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

**Score:** 90/100

**Reason:** This node includes a quick canny edge detection node with unconventional settings which is highly relevant for the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node provides a web interface for ComfyUI, which could be useful for generating images guided by canny edge detection.

### Metadata
**Author:** wei30172
**Repository:** [https://github.com/wei30172/comfygen](https://github.com/wei30172/comfygen)
**Install Type:** git-clone

---

### ComfyMath

**Description:**

Provides Math Nodes for ComfyUI. Boolean Logic, Integer Arithmetic, Floating Point Arithmetic and Functions, Vec2, Vec3, and Vec4 Arithmetic and Functions

- **Author:** evanspearman
- **Repository:** [https://github.com/evanspearman/ComfyMath](https://github.com/evanspearman/ComfyMath)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** ComfyMath offers various arithmetic operations and functions that are essential for implementing canny edge detection in the workflow.

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

**Reason:** ComfyQR provides QR code generation nodes but does not directly contribute to the workflow goal of image generation guided by canny edge detection.

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

**Reason:** ComfyS3 integrates with Amazon S3 which can be useful for loading and saving images used in the canny edge detection process.

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

**Score:** 81/100

**Reason:** This node provides a native DynamiCrafter that works with ComfyUI nodes and optimizations, which could be useful for generating images guided by canny edge detection.

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

**Score:** 61/100

**Reason:** This node integrates P2LDGAN into ComfyUI and extracts lineart from input images, which could be useful for generating images guided by canny edge detection, but requires additional setup.

### Metadata
**Author:** jamesWalker55
**Repository:** [https://github.com/jamesWalker55/comfyui-p2ldgan](https://github.com/jamesWalker55/comfyui-p2ldgan)
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

**Reason:** This node is very useful as it provides a custom solution for generating A1111-like prompts which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 90/100

**Reason:** This node can generate any type of node using LLMs, making it very useful for creating impossible workflows, including those that involve image generation guided by canny edge detection.

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

**Score:** 95/100

**Reason:** This node enhances old or low-quality images in ComfyUI, which aligns with the image generation guided by canny edge detection workflow goal.

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

**Score:** 40/100

**Reason:** This node helps with checkpoint configuration which could be useful for training models used in image generation but is not directly related to the workflow goal.

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

**Score:** 60/100

**Reason:** This node loads config for sampler nodes from a yaml file which can be helpful for fine-tuning model parameters used in image generation.

### Metadata
**Author:** Cyberschorsch
**Repository:** [https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader](https://github.com/Cyberschorsch/ComfyUI-checkpoint-config-loader)
**Install Type:** git-clone

---

### ComfyUI Color Detection Nodes

**Description:**

A collection of nodes for detecting color in images, leveraging RGB and LAB color spaces. These nodes aim to distinguish colored images from black and white, including those with color tints.

- **Author:** DrMWeigand
- **Repository:** [https://github.com/DrMWeigand/ComfyUI_ColorImageDetection](https://github.com/DrMWeigand/ComfyUI_ColorImageDetection)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is specifically designed for color detection in images, which could provide useful information for guiding image generation with canny edge detection.

### Metadata
**Author:** DrMWeigand
**Repository:** [https://github.com/DrMWeigand/ComfyUI_ColorImageDetection](https://github.com/DrMWeigand/ComfyUI_ColorImageDetection)
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

**Reason:** This node provides direct control over sigma values which are crucial for denoising and edge detection in image processing.

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

**Reason:** While this node provides batch processing convenience nodes, it is not directly relevant to the specific task of image generation guided by canny edge detection.

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

**Reason:** This node provides a deepface library which can be used for face recognition and edge detection in image generation.

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

**Reason:** This node implements DenseDiffusion, an algorithm that can generate high-quality images and may utilize canny edge detection internally.

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

**Reason:** This node provides a Dreamtalk implementation that can be used as a starting point for generating images based on canny edge detection.

### Metadata
**Author:** hay86
**Repository:** [https://github.com/hay86/ComfyUI_Dreamtalk](https://github.com/hay86/ComfyUI_Dreamtalk)
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

**Reason:** ComfyUI Essentials likely includes nodes necessary for image processing and edge detection.

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

**Score:** 90/100

**Reason:** This node allows for personalizing diffusion models with iterative feedback via attention-based reference image conditioning, which is relevant to the workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node supports Flux API which can be used for generating images and may have features that aid in edge detection or related tasks.

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

**Reason:** This node is specifically designed to accelerate image generation using the Flux.1 API, making it highly relevant to the workflow goal.

### Metadata
**Author:** discus0434
**Repository:** [https://github.com/discus0434/comfyui-flux-accelerator](https://github.com/discus0434/comfyui-flux-accelerator)
**Install Type:** git-clone

---

### ComfyUI Flux Continuum: Modular Interface

**Description:**

Set of custom nodes to use with the ComfyUI Flux Continuum: Modular Interface. NODES: Text Versions, Image64 Display, Tabs, Step Slider, Denoise Slider, Guidance Slider, Batch Slider, Max Shift Slider, ControlNet Slider

- **Author:** robertvoy
- **Repository:** [https://github.com/robertvoy/ComfyUI-Flux-Continuum](https://github.com/robertvoy/ComfyUI-Flux-Continuum)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node set includes various interface components, none of them directly relate to canny edge detection or image generation; they might be useful for other aspects of the workflow.

### Metadata
**Author:** robertvoy
**Repository:** [https://github.com/robertvoy/ComfyUI-Flux-Continuum](https://github.com/robertvoy/ComfyUI-Flux-Continuum)
**Install Type:** git-clone

---

### ComfyUI Frame Maker

**Description:**

This node creates a sequence of frames by moving and scaling a subject image over a background image.

- **Author:** diSty
- **Repository:** [https://github.com/diStyApps/ComfyUI_FrameMaker](https://github.com/diStyApps/ComfyUI_FrameMaker)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node creates a sequence of frames by moving and scaling a subject image over a background image, which aligns with the workflow goal of generating images guided by canny edge detection.

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

**Score:** 81/100

**Reason:** This node provides an implementation of Hallo, which is a model for image synthesis and could be useful for generating images guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This node provides a custom pack for enhancing images through various operations like Sampler, Upscaler, Mask, which could be useful for generating images guided by canny edge detection, especially with the mention of optimizations built upon ComfyUI-Impact-Pack.

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

**Reason:** This node pack offers various detector nodes that could be used for canny edge detection and iterative upscaling, making it very useful for this workflow goal.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
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

**Reason:** This node implements faceswapping based on InstantID and LCM Lora, which could be useful for generating images guided by canny edge detection. It works with SDXL checkpoints, making it a good fit for this workflow goal.

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

**Reason:** Although this node generates images like Adobe Photoshop"s Layer Style, its primary focus is on layer styles rather than edge detection.

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

**Score:** 90/100

**Reason:** This node directly supports the workflow goal by improving inpainting results with geometric patterns.

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

**Reason:** This minimap node provides navigation but also indirectly supports workflow visualization which could aid in understanding the canny edge detection process.

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

**Reason:** This model downloader node would be essential for downloading models required for canny edge detection-based image generation in the workflow.

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

**Reason:** This node is highly relevant as it utilizes MuseV for image generation and can potentially be guided by edge detection techniques.

### Metadata
**Author:** storyicon
**Repository:** [https://github.com/storyicon/comfyui_musev_evolved](https://github.com/storyicon/comfyui_musev_evolved)
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

**Reason:** This extensive toolkit includes nodes that could be useful for designing and training neural networks that incorporate canny edge detection.

### Metadata
**Author:** inventorado
**Repository:** [https://github.com/inventorado/ComfyUI_NNT](https://github.com/inventorado/ComfyUI_NNT)
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

**Reason:** These nodes provide pre-trained models for ControlNeXt-SVD v2, which is a relevant model for image generation tasks and can potentially be guided by canny edge detection.

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

**Score:** 81/100

**Reason:** CrossImageAttention is directly related to image attention mechanisms which can be used in conjunction with canny edge detection for guided image generation.

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

**Score:** 40/100

**Reason:** Style-Aligned is related to style transfer but it"s unclear how it would be used in conjunction with canny edge detection for guided image generation.

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

**Score:** 90/100

**Reason:** This node computes optical flow between images, which is closely related to edge detection and can be useful for guiding image generation.

### Metadata
**Author:** seanlynch
**Repository:** [https://github.com/seanlynch/comfyui-optical-flow](https://github.com/seanlynch/comfyui-optical-flow)
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

**Reason:** This node is very useful as it provides a reference implementation for PhotoMaker models, which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node manipulates pixel art images, which could potentially be used as a preprocessing step for canny edge detection. It"s very useful for preparing input images.

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

**Reason:** This node integrates Pixtral Large vision model that likely includes image processing capabilities including canny edge detection and other features that would be essential for the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node can generate images from text prompts using AI models, which could be useful for guiding the image generation process.

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

**Reason:** The Prompt ExtraNetworks node allows dynamic loading of LoRA or HN based on the specifications within the prompt, which could be useful in generating images guided by canny edge detection.

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

**Reason:** This ProPainter node is directly relevant to image generation and can be used with canny edge detection for guided inpainting.

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

**Score:** 80/100

**Reason:** The PyramidFlow wrapper provides a model that can be used for image generation and may include features related to edge detection or inpainting.

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

**Reason:** Resynthesizer is a texture generation technique that could be useful for inpainting and removing objects from an image, which aligns with the workflow goal.

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

**Reason:** Rife TensorRT provides a fast frame interpolation technique that could be useful for generating images with specific details, such as edges detected by canny edge detection.

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

**Reason:** This node implements SAM2 with functionalities from comfyui_segment_anything, which is highly relevant for image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node is specifically designed for segmenting images and could be useful in conjunction with canny edge detection for image generation.

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

**Score:** 90/100

**Reason:** This node provides an implementation of SegMoE, which is a diffusion model that can generate high-quality images. It aligns closely with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SegMoE)
**Install Type:** git-clone

---

### ComfyUI Slothful Attention

**Description:**

This custom node allow controlling output without training. The reducing method is similar to [a/Spatial-Reduction Attention](https://paperswithcode.com/method/spatial-reduction-attention), but generating speed may not be increased on typical image sizes due to overheads. (In some cases, slightly slower)

- **Author:** MitoshiroPJ
- **Repository:** [https://github.com/MitoshiroPJ/comfyui_slothful_attention](https://github.com/MitoshiroPJ/comfyui_slothful_attention)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** The Slothful Attention node is specifically designed for controlling output in image generation tasks and uses a method similar to Spatial-Reduction Attention, making it highly relevant to the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node provides a suite of nodes that includes StabilityAI models which are commonly used for image generation tasks and may include canny edge detection functionality.

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

**Reason:** This node provides a Stable Video Diffusion model which is commonly used for video and image generation tasks and may include canny edge detection functionality.

### Metadata
**Author:** thecooltechguy
**Repository:** [https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion)
**Install Type:** git-clone

---

### ComfyUI String Tools

**Description:**

 This extension provides the StringToolsConcat node, which concatenates multiple texts, and the StringToolsRandomChoice node, which selects one randomly from multiple texts.

- **Author:** Taremin
- **Repository:** [https://github.com/Taremin/comfyui-string-tools](https://github.com/Taremin/comfyui-string-tools)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node offers text manipulation tools but is marginally relevant as it may be used in conjunction with other nodes to generate text that could guide image generation.

### Metadata
**Author:** Taremin
**Repository:** [https://github.com/Taremin/comfyui-string-tools](https://github.com/Taremin/comfyui-string-tools)
**Install Type:** git-clone

---

### ComfyUI Suno API

**Description:**

An unofficial Python library for [a/Suno AI](https://www.suno.ai/) API

- **Author:** GentlemanHu
- **Repository:** [https://github.com/GentlemanHu/ComfyUI-SunoAI](https://github.com/GentlemanHu/ComfyUI-SunoAI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides access to a Suno AI API which could be used for generating images based on text input and can potentially utilize canny edge detection.

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

**Score:** 90/100

**Reason:** This node implements template matching which is closely related to image generation and can potentially use canny edge detection.

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

**Score:** 70/100

**Reason:** This node offers a universal styling solution that could be used in conjunction with canny edge detection for image generation.

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

**Score:** 40/100

**Reason:** This node provides fast image upscaling using TensorRT, but it is not directly related to canny edge detection or image generation.

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

**Score:** 80/100

**Reason:** This node provides color grading features that could be useful in conjunction with canny edge detection for image generation.

### Metadata
**Author:** pamparamm
**Repository:** [https://github.com/pamparamm/ComfyUI-vectorscope-cc](https://github.com/pamparamm/ComfyUI-vectorscope-cc)
**Install Type:** git-clone

---

### ComfyUI Web Viewer

**Description:**

The ComfyUI Web Viewer by [a/vrch.ai](https://vrch.ai) is a custom node collection offering a real-time AI-generated interactive art framework. This utility integrates realtime streaming into ComfyUI workflows, supporting keyboard control nodes, OSC control nodes, sound input nodes, and more. Accessible from any device with a web browser, it enables real time interaction with AI-generated content, making it ideal for interactive visual projects and enhancing ComfyUI workflows with efficient content management and display.

- **Author:** Vrch Studio (vrch.ai)
- **Repository:** [https://github.com/VrchStudio/comfyui-web-viewer](https://github.com/VrchStudio/comfyui-web-viewer)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** The ComfyUI Web Viewer provides real-time AI-generated interactive art framework and supports keyboard control nodes, OSC control nodes, sound input nodes, making it very useful for the specified workflow goal.

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

**Score:** 80/100

**Reason:** Comfyui Webcam capture node is moderately to very useful as it captures images from webcam one at a time, which can be used in img2img or controlnet workflows guided by canny edge detection.

### Metadata
**Author:** victorchall
**Repository:** [https://github.com/victorchall/comfyui_webcamcapture](https://github.com/victorchall/comfyui_webcamcapture)
**Install Type:** git-clone

---

### ComfyUI YetAnotherSafetyChecker

**Description:**

Just a simple node to filter out NSFW outputs. This node utilizes [a/AdamCodd/vit-base-nsfw-detector](https://huggingface.co/AdamCodd/vit-base-nsfw-detector) to score the outputs. I chose this model because it's small, fast, and performed very well in my testing. Nudity tends to be scored in the 0.95+ range, but I've set the default to 0.8 as a safe baseline.

- **Author:** BetaDoggo
- **Repository:** [https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker](https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node filters out NSFW outputs which could be useful in conjunction with image generation tasks to ensure safe and appropriate content is produced.

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

**Reason:** This node is moderately useful for the workflow goal as it includes nodes for Yolov8Detection and Yolov8Segmentation which could be used in conjunction with canny edge detection.

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

**Score:** 41/100

**Reason:** This node has some utility for the workflow goal but its relevance is limited by the lack of direct connection to canny edge detection.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM](https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM)
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

**Reason:** This node provides native implementation of IC-Light which could be useful in generating images with accurate lighting effects.

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

**Score:** 81/100

**Reason:** This extensive node suite enables ComfyUI to process 3D inputs using cutting-edge algorithms and models, which can be used for image generation guided by canny edge detection.

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

**Score:** 91/100

**Reason:** This custom node is specifically designed for 3D photo inpainting, which aligns closely with the workflow goal of generating images guided by canny edge detection.

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

**Reason:** This node allows for scheduling ControlNet strength and applying custom weights and attention masks, which are crucial components in guiding image generation with canny edge detection.

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

**Score:** 80/100

**Reason:** As an AI assistant, it could provide guidance on implementing canny edge detection in image generation.

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

**Score:** 61/100

**Reason:** This node supports text-to-video generation but might be useful as a supporting node for the workflow goal due to its ability to generate high-quality video outputs.

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

**Score:** 80/100

**Reason:** This node provides nodes and workflows for animation creation, including potential tools for image processing and manipulation that could be used in conjunction with canny edge detection for image generation.

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

**Score:** 81/100

**Reason:** This node uses APG scaling, which improves image quality and is relevant to the workflow goal of generating high-quality images.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-APGScaling](https://github.com/logtd/ComfyUI-APGScaling)
**Install Type:** git-clone

---

### ComfyUI-APQNodes

**Description:**

Without fine-tuning, FLUX.1 Dev model cannot understand exact color codes. However, it is known that FLUX.1 Dev can repeatedly produce certain colors with certain prompt(color name). Fortunately, on CIVITAI, [a/“novuschroma” shared 155 pre-tested color names](https://civitai.com/models/879997/color-wildcards-for-flux-and-sdxl) that FLUX.1 Dev can handle. Thanks to his resource, color palette consists exclusively of 155 colors can be configured. ‘ColorPalette’ node from ComfyUI APQNodes converts input hex color code to the most similar color name(from pre-tested 155 color names) of which FLUX.1 Dev is aware.

- **Author:** AIPOQUE
- **Repository:** [https://github.com/AIPOQUE/ComfyUI-APQNodes](https://github.com/AIPOQUE/ComfyUI-APQNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node helps with color palette configuration using pre-tested color names, which is a supporting task for the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** AIPOQUE
**Repository:** [https://github.com/AIPOQUE/ComfyUI-APQNodes](https://github.com/AIPOQUE/ComfyUI-APQNodes)
**Install Type:** git-clone

---

### comfyui-art-venture

**Description:**

A comprehensive set of custom nodes for ComfyUI, focusing on utilities for image processing, JSON manipulation, model operations and working with object via URLs

- **Author:** sipherxyz
- **Repository:** [https://github.com/sipherxyz/comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is a comprehensive set of custom nodes for image processing and manipulation which would be very useful for the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal. It can convert images into ASCII art strings which can be used in conjunction with canny edge detection for image processing and analysis.

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

**Score:** 90/100

**Reason:** This node is essential for the specified workflow goal as it enables smooth animations and dynamic sequences that can be used to visualize and analyze images processed using canny edge detection.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-AstralAnimator](https://github.com/ShmuelRonen/ComfyUI-AstralAnimator)
**Install Type:** git-clone

---

### ComfyUI-AudioScheduler

**Description:**

Load mp3 files and use the audio nodes to power animations and prompt scheduling. Use with FizzNodes.

- **Author:** a1lazydog
- **Repository:** [https://github.com/a1lazydog/ComfyUI-AudioScheduler](https://github.com/a1lazydog/ComfyUI-AudioScheduler)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides audio scheduling capabilities but does not directly relate to image generation or canny edge detection.

### Metadata
**Author:** a1lazydog
**Repository:** [https://github.com/a1lazydog/ComfyUI-AudioScheduler](https://github.com/a1lazydog/ComfyUI-AudioScheduler)
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

**Reason:** This node adjusts CFG settings which is crucial for improving image quality when using canny edge detection as a guide.

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

**Score:** 91/100

**Reason:** This node splits images based on edge detection and uniform division which aligns with the workflow goal of guided image generation using canny edge detection.

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

**Score:** 70/100

**Reason:** This node provides seamless integration with Azure blob storage, which could be useful for loading and saving images used in the workflow.

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

**Score:** 40/100

**Reason:** While this node edits backgrounds of images/videos, it may not be directly relevant to the specific goal of image generation guided by canny edge detection.

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

**Reason:** This node provides a CharacterPipe node that simplifies character-based image generation, which aligns closely with the specified workflow goal.

### Metadata
**Author:** blackcodetavern
**Repository:** [https://github.com/blackcodetavern/ComfyUI-Benripack](https://github.com/blackcodetavern/ComfyUI-Benripack)
**Install Type:** git-clone

---

### ComfyUI-BiRefNet-Hugo

**Description:**

This repository wraps the latest BiRefNet model as ComfyUI nodes. Compared to the previous model, the latest model offers higher and better matting accuracy.

- **Author:** Hugo
- **Repository:** [https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo](https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node wraps a BiRefNet model optimized for matting accuracy, which can be used as a base for guided image generation with canny edge detection.

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

**Score:** 100/100

**Reason:** This node packages the latest BiRefNet model with features like chunked loading and model caching, making it highly suitable for large-scale image generation tasks guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows users to easily add text overlays to images within their ComfyUI projects, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** Big-Idea-Technology
**Repository:** [https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools](https://github.com/Big-Idea-Technology/ComfyUI-Book-Tools)
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

**Reason:** This node allows saving generated images to BunnyStorage which could be useful after applying canny edge detection and generating an image.

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

**Score:** 100/100

**Reason:** This node implements CADS which could be used to generate images guided by canny edge detection.

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

**Score:** 81/100

**Reason:** This node provides numerical calculation capabilities that could be useful for implementing canny edge detection algorithms.

### Metadata
**Author:** Limitex
**Repository:** [https://github.com/Limitex/ComfyUI-Calculation](https://github.com/Limitex/ComfyUI-Calculation)
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

**Score:** 81/100

**Reason:** This node provides a virtual try-on diffusion model that can be used for image generation, and its efficiency makes it suitable for guided image generation with canny edge detection.

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

**Score:** 90/100

**Reason:** This node wraps the Catvton-Flux implementation of diffusers, making it directly applicable to image generation tasks guided by canny edge detection.

### Metadata
**Author:** lujiazho
**Repository:** [https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper](https://github.com/lujiazho/ComfyUI-CatvtonFluxWrapper)
**Install Type:** git-clone

---

### ComfyUI-Chat-Image

**Description:**

Use an online large language model to describe images.

- **Author:** wqjuser
- **Repository:** [https://github.com/wqjuser/ComfyUI-Chat-Image](https://github.com/wqjuser/ComfyUI-Chat-Image)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node uses an online large language model to describe images, which could be useful for generating text descriptions of images based on their edges.

### Metadata
**Author:** wqjuser
**Repository:** [https://github.com/wqjuser/ComfyUI-Chat-Image](https://github.com/wqjuser/ComfyUI-Chat-Image)
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

**Reason:** ImageScore node may be useful for evaluating the quality of generated images but does not directly contribute to canny edge detection.

### Metadata
**Author:** azure-dragon-ai
**Repository:** [https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes](https://github.com/azure-dragon-ai/ComfyUI-ClipScore-Nodes)
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

**Score:** 90/100

**Reason:** This node provides a convenient way to terminate the workflow processing based on a condition, which could be useful in certain scenarios of image generation guided by canny edge detection.

### Metadata
**Author:** SparknightLLC
**Repository:** [https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt](https://github.com/SparknightLLC/ComfyUI-ConditionalInterrupt)
**Install Type:** git-clone

---

### ComfyUI-CreaPrompt

**Description:**

Generate random prompts easily.

- **Author:** Tritant
- **Repository:** [https://github.com/tritant/ComfyUI_CreaPrompt](https://github.com/tritant/ComfyUI_CreaPrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node generates random prompts which could be used as input for the image generation process guided by canny edge detection.

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

**Score:** 80/100

**Reason:** The CSV loader provides access to a wide range of prompts that could be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node acts as a bridge between ComfyUI and Blender, which could be useful for generating images in Blender using canny edge detection.

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

**Score:** 40/100

**Reason:** This node contains various custom nodes, but none of them directly relate to image generation or canny edge detection. Some nodes might be useful in supporting tasks.

### Metadata
**Author:** wTechArtist
**Repository:** [https://github.com/wTechArtist/ComfyUI-CustomNodes](https://github.com/wTechArtist/ComfyUI-CustomNodes)
**Install Type:** git-clone

---

### ComfyUI-Danbooru-To-WD

**Description:**

Converts booru tags to a format suitable for Waifu Diffusion(or Danbooru based models).

- **Author:** RedRayz
- **Repository:** [https://github.com/RedRayz/ComfyUI-Danbooru-To-WD](https://github.com/RedRayz/ComfyUI-Danbooru-To-WD)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node converts Danbooru tags to a format suitable for Waifu Diffusion models, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** RedRayz
**Repository:** [https://github.com/RedRayz/ComfyUI-Danbooru-To-WD](https://github.com/RedRayz/ComfyUI-Danbooru-To-WD)
**Install Type:** git-clone

---

### ComfyUI-DataSet

**Description:**

Data research, preparation, and manipulation nodes for model trainers and artists.

- **Author:** daxcay
- **Repository:** [https://github.com/daxcay/ComfyUI-DataSet](https://github.com/daxcay/ComfyUI-DataSet)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node provides data research and manipulation capabilities, it is not directly relevant to the specified workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node directly uses DDUF which is powered by Diffusers and can be used for image generation guided by canny edge detection.

### Metadata
**Author:** Vaibhavs10
**Repository:** [https://github.com/Vaibhavs10/ComfyUI-DDUF](https://github.com/Vaibhavs10/ComfyUI-DDUF)
**Install Type:** git-clone

---

### ComfyUI-decadetw-spout-syphon-im-vj

**Description:**

I'm SD-VJ. (share SD-generating-process in realtime by gpu)

- **Author:** xlinx
- **Repository:** [https://github.com/xlinx/ComfyUI-decadetw-spout-syphon-im-vj](https://github.com/xlinx/ComfyUI-decadetw-spout-syphon-im-vj)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node shares SD-generating-process in realtime by gpu and can be used for real-time image processing which aligns with the workflow goal of guided image generation by canny edge detection.

### Metadata
**Author:** xlinx
**Repository:** [https://github.com/xlinx/ComfyUI-decadetw-spout-syphon-im-vj](https://github.com/xlinx/ComfyUI-decadetw-spout-syphon-im-vj)
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

**Reason:** This node accelerates ComfyUI nodes for faster image generation and ensures consistency pre and post-acceleration which aligns with the workflow goal of guided image generation by canny edge detection.

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

**Reason:** This node selectively applies a denoise mask at each step during the inpainting inference process in diffusion models, which is relevant to image generation and could potentially be used with canny edge detection.

### Metadata
**Author:** MiddleKD
**Repository:** [https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler](https://github.com/MiddleKD/ComfyUI-denoise-mask-scheduler)
**Install Type:** git-clone

---

### ComfyUI-depth-fm

**Description:**

Fast and accurate monocular depth estimation.

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-depth-fm](https://github.com/kijai/ComfyUI-depth-fm)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides fast and accurate monocular depth estimation which is directly relevant to the image generation guided by canny edge detection.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-depth-fm](https://github.com/kijai/ComfyUI-depth-fm)
**Install Type:** git-clone

---

### ComfyUI-Depth-Pro

**Description:**

Based on [a/https://github.com/apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)

- **Author:** spacepxl
- **Repository:** [https://github.com/spacepxl/ComfyUI-Depth-Pro](https://github.com/spacepxl/ComfyUI-Depth-Pro)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node is based on a model for depth estimation, it does not seem as directly relevant to the workflow goal compared to other nodes.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Depth-Pro](https://github.com/spacepxl/ComfyUI-Depth-Pro)
**Install Type:** git-clone

---

### ComfyUI-Depth-Visualization

**Description:**

Works with any Depth Map and visualizes the applied version it inside ComfyUI

- **Author:** gokayfem
- **Repository:** [https://github.com/gokayfem/ComfyUI-Depth-Visualization](https://github.com/gokayfem/ComfyUI-Depth-Visualization)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node visualizes depth maps which would be very useful in conjunction with canny edge detection for image generation.

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

**Score:** 61/100

**Reason:** This node provides a model for monocular depth estimation and autodownloads pre-trained models, making it moderately useful for the specified workflow goal.

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

**Score:** 81/100

**Reason:** This node allows adjusting sigmas that control detail which is directly relevant to the workflow goal of image generation guided by canny edge detection.

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

**Score:** 81/100

**Reason:** This node provides a diffuser pipeline that includes nodes related to Stream Diffusion and can be used for image generation guided by canny edge detection.

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

**Score:** 61/100

**Reason:** This node is moderately useful because it enables outpainting images with diffusers, which could potentially utilize canny edge detection as an input feature.

### Metadata
**Author:** GiusTex
**Repository:** [https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint](https://github.com/GiusTex/ComfyUI-DiffusersImageOutpaint)
**Install Type:** git-clone

---

### ComfyUI-DiffusersLoader

**Description:**

This node pack allows loading of SD checkpoints that uses diffusers format in comfyUI.

- **Author:** Scorpinaus
- **Repository:** [https://github.com/Scorpinaus/ComfyUI-DiffusersLoader](https://github.com/Scorpinaus/ComfyUI-DiffusersLoader)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** This node allows loading of SD checkpoints in the diffusers format but does not directly contribute to image generation guided by canny edge detection.

### Metadata
**Author:** Scorpinaus
**Repository:** [https://github.com/Scorpinaus/ComfyUI-DiffusersLoader](https://github.com/Scorpinaus/ComfyUI-DiffusersLoader)
**Install Type:** git-clone

---

### ComfyUI-Documents

**Description:**

ComfyUI-Documents is a powerful extension for ComfyUI that enhances workflows with advanced document processing capabilities. It includes nodes for loading and parsing various document types (PDF, TXT, DOC, DOCX), converting PDF pages to images, splitting PDFs into individual pages, and selecting specific images from batches. Features include text extraction, image conversion, and seamless integration with existing ComfyUI projects.

- **Author:** Indra's Mirror
- **Repository:** [https://github.com/Excidos/ComfyUI-Documents](https://github.com/Excidos/ComfyUI-Documents)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides advanced document processing capabilities that can be used in conjunction with image generation and edge detection.

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

**Score:** 81/100

**Reason:** This node provides a wrapper for calling Draw Things image generations which can be guided by canny edge detection, making it very useful for this workflow goal.

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

**Reason:** This node is highly relevant and useful for the specified workflow goal as it provides a custom ComfyUI node designed specifically for image generation guided by canny edge detection.

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

**Score:** 60/100

**Reason:** This node is moderately useful for the specified workflow goal as it provides a wrapper around DynamiCrafter models which may be used for image generation, but does not directly support canny edge detection.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-DynamiCrafterWrapper](https://github.com/kijai/ComfyUI-DynamiCrafterWrapper)
**Install Type:** git-clone

---

### ComfyUI-EasyAnimate

**Description:**

ComfyUI-EasyAnimate

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-EasyAnimate](https://github.com/chaojie/ComfyUI-EasyAnimate)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides animation capabilities but does not directly contribute to canny edge detection or image generation.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-EasyAnimate](https://github.com/chaojie/ComfyUI-EasyAnimate)
**Install Type:** git-clone

---

### ComfyUI-EasyPony

**Description:**

Easy Pony is a helper node that simplifies the process of adding scoring and other attributes to prompts when using Pony models.

- **Author:** itsjustregi
- **Repository:** [https://github.com/regiellis/ComfyUI-EasyPony](https://github.com/regiellis/ComfyUI-EasyPony)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node simplifies adding attributes to prompts for Pony models, it"s not directly related to canny edge detection or image generation.

### Metadata
**Author:** itsjustregi
**Repository:** [https://github.com/regiellis/ComfyUI-EasyPony](https://github.com/regiellis/ComfyUI-EasyPony)
**Install Type:** git-clone

---

### comfyui-edit-mask

**Description:**

Nodes:Edit Mask

- **Author:** shadowcz007
- **Repository:** [https://github.com/shadowcz007/comfyui-edit-mask](https://github.com/shadowcz007/comfyui-edit-mask)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows editing masks which could be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node implements EfficientTAM which is a technique used in image-to-image translation tasks that could be guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This ComfyUI wrapper node is highly relevant and very useful for using the Diffusers implementation of ELLA in image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This enhanced save node allows for flexible saving of generated images which can be useful in a workflow involving canny edge detection.

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

**Reason:** The partial redraw sampler and variant seed sampler could be useful for generating diverse images that might incorporate canny edge detection features.

### Metadata
**Author:** 11dogzi
**Repository:** [https://github.com/11dogzi/Comfyui-ergouzi-samplers](https://github.com/11dogzi/Comfyui-ergouzi-samplers)
**Install Type:** git-clone

---

### ComfyUI-EvTexture

**Description:**

Wrapper for EvTexture Video Upscaler: [a/https://github.com/DachunKai/EvTexture](https://github.com/DachunKai/EvTexture)

- **Author:** tocubed
- **Repository:** [https://github.com/tocubed/ComfyUI-EvTexture](https://github.com/tocubed/ComfyUI-EvTexture)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a video upscaler which may not directly contribute to the workflow goal of image generation guided by canny edge detection.

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

**Score:** 61/100

**Reason:** This node has great custom process controls and improves speed of reasoning which could be useful for complex workflows like image generation.

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

**Score:** 100/100

**Reason:** This node directly integrates the FLUX.1 model with LoRA API specifically for text-to-image generation making it essential for this workflow goal.

### Metadata
**Author:** yhayano-ponotech
**Repository:** [https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux](https://github.com/yhayano-ponotech/ComfyUI-Fal-API-Flux)
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

**Reason:** While this node contains string manipulation functions, they are unlikely to be useful for the specified workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node provides a JPEG de-artifacting function using FBCNN, which is directly relevant to improving image quality and could complement canny edge detection in the specified workflow goal.

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

**Score:** 80/100

**Reason:** This node is very useful in organizing output files and generating dynamic filenames based on user-defined parameters, which is essential for the specified workflow goal.

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

**Score:** 90/100

**Reason:** This node is extremely relevant to image generation guided by canny edge detection as it provides functionality for filling images using cv2 methods, which aligns with outpainting requirements.

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

**Reason:** This node provides functionality to resize images which could be useful in conjunction with canny edge detection for generating images.

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

**Reason:** This node seems to have a broad range of tools but none specifically related to edge detection or image generation.

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

**Reason:** This node is a Vision-Language Model (VLM) specifically designed for image vision tasks, including object detection which can be used in conjunction with canny edge detection.

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

**Score:** 91/100

**Reason:** This node is also a VLM that supports various image vision tasks such as object detection, captioning and segmentation, making it highly relevant to the workflow goal.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)
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

**Score:** 80/100

**Reason:** This node is very useful as it uses TripoSR which creates a 3D model from an image and can potentially be used in conjunction with canny edge detection for guided image generation.

### Metadata
**Author:** flowtyone
**Repository:** [https://github.com/flowtyone/ComfyUI-Flowty-TripoSR](https://github.com/flowtyone/ComfyUI-Flowty-TripoSR)
**Install Type:** git-clone

---

### ComfyUI-FLUX-TOGETHER-API

**Description:**

A custom node implementation for ComfyUI that integrates with Together.ai's FLUX image generation models. This project is inspired by and adapted from [a/ComfyUI-FLUX-BFL-API](https://github.com/gelasdev/ComfyUI-FLUX-BFL-API) to work with the Together.ai API.

- **Author:** BZcreativ
- **Repository:** [https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API](https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node integrates with Together.ai"s FLUX image generation models which could be useful for generating images guided by canny edge detection.

### Metadata
**Author:** BZcreativ
**Repository:** [https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API](https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API)
**Install Type:** git-clone

---

### ComfyUI-FluxExt-MZ

**Description:**

Nodes:MZ_Flux1PartialLoad_Patch. Tool nodes related to flux1

- **Author:** MinusZoneAI
- **Repository:** [https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ](https://github.com/MinusZoneAI/ComfyUI-FluxExt-MZ)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides tools related to Flux1, but its relevance to the workflow goal of image generation guided by canny edge detection is unclear.

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

**Score:** 60/100

**Reason:** This node contains a set of tooling nodes that could be useful for preparing images for processing, such as calculating width and height; however, it does not directly address the workflow goal.

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

**Score:** 80/100

**Reason:** ComfyUI-FrameFX provides features for frame interpolation and video processing which could be useful in conjunction with canny edge detection for image generation.

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

**Score:** 100/100

**Reason:** ComfyUI-FreeMemory provides advanced memory management capabilities which are essential for preventing out-of-memory errors during complex operations like image generation guided by canny edge detection.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI-FreeMemory](https://github.com/ShmuelRonen/ComfyUI-FreeMemory)
**Install Type:** git-clone

---

### Comfyui-Gelbooru

**Description:**

Get random images from gelbooru, support multiple tag searches, exclude tags, etc. user and api key are optional.

- **Author:** 1mckw
- **Repository:** [https://github.com/1mckw/Comfyui-Gelbooru](https://github.com/1mckw/Comfyui-Gelbooru)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant and useful for the workflow goal, allowing for random image retrieval from Gelbooru with customizable tag searches.

### Metadata
**Author:** 1mckw
**Repository:** [https://github.com/1mckw/Comfyui-Gelbooru](https://github.com/1mckw/Comfyui-Gelbooru)
**Install Type:** git-clone

---

### ComfyUI-Gemma

**Description:**

ComfyUI Gemma

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-Gemma](https://github.com/chaojie/ComfyUI-Gemma)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Directly related to image processing with canny edge detection.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-Gemma](https://github.com/chaojie/ComfyUI-Gemma)
**Install Type:** git-clone

---

### ComfyUI-GeneraNodes

**Description:**

Genera custom nodes and extensions

- **Author:** jetchopper
- **Repository:** [https://github.com/evolox/ComfyUI-GeneraNodes](https://github.com/evolox/ComfyUI-GeneraNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Generates custom nodes but no specific relation to canny edge detection or image generation.

### Metadata
**Author:** jetchopper
**Repository:** [https://github.com/evolox/ComfyUI-GeneraNodes](https://github.com/evolox/ComfyUI-GeneraNodes)
**Install Type:** git-clone

---

### ComfyUI-GG

**Description:**

ComfyUI-GG is a collection of ComfyUI nodes designed to enhance productivity in image processing workflows. This plugin provides a set of custom nodes that perform various image manipulations and metadata extractions to streamline your tasks.

- **Author:** leestuartx
- **Repository:** [https://github.com/leestuartx/ComfyUI-GG](https://github.com/leestuartx/ComfyUI-GG)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Collection of ComfyUI nodes designed for image processing workflows, including potential support for canny edge detection.

### Metadata
**Author:** leestuartx
**Repository:** [https://github.com/leestuartx/ComfyUI-GG](https://github.com/leestuartx/ComfyUI-GG)
**Install Type:** git-clone

---

### ComfyUI-GLHF

**Description:**

GLHF is a ComfyUI node that facilitates seamless interaction with the GLHF chat API. Designed to enhance user experience, it supports multiple language models, web search integration, and customizable instructions, making it a powerful extension for AI-driven workflows.

- **Author:** fairy-root
- **Repository:** [https://github.com/fairy-root/ComfyUI-GLHF](https://github.com/fairy-root/ComfyUI-GLHF)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a GLHF chat API integration which could potentially be used for generating instructions or guidance for image generation tasks, making it highly relevant.

### Metadata
**Author:** fairy-root
**Repository:** [https://github.com/fairy-root/ComfyUI-GLHF](https://github.com/fairy-root/ComfyUI-GLHF)
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

**Reason:** This node refines the initial latent noise in the diffusion process, enhancing both image quality and semantic coherence, which aligns with the goal of generating high-quality images using canny edge detection.

### Metadata
**Author:** LucipherDev
**Repository:** [https://github.com/LucipherDev/ComfyUI-Golden-Noise](https://github.com/LucipherDev/ComfyUI-Golden-Noise)
**Install Type:** git-clone

---

### ComfyUI-GPT_SoVITS

**Description:**

a comfyui custom node for [a/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)! you can voice cloning and tts in comfyui now
[w/NOTE:make sure ffmpeg is worked in your commandline]

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-GPT_SoVITS](https://github.com/AIFSH/ComfyUI-GPT_SoVITS)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node can be used to generate voice cloning and tts which could be used as input for image generation.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-GPT_SoVITS](https://github.com/AIFSH/ComfyUI-GPT_SoVITS)
**Install Type:** git-clone

---

### ComfyUI-graphToPrompt

**Description:**

workflow.json -> workflow_api.json

- **Author:** nat-chan
- **Repository:** [https://github.com/nat-chan/ComfyUI-graphToPrompt](https://github.com/nat-chan/ComfyUI-graphToPrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node converts a workflow into an API, but its direct relevance to image generation guided by canny edge detection is unclear.

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

**Score:** 90/100

**Reason:** This Haiper API node seems highly relevant as it likely provides access to AI-powered image processing capabilities, including edge detection and image generation.

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

**Score:** 80/100

**Reason:** HakuImg is an image processing tool that could be useful for tasks like canny edge detection or image enhancement, making it moderately essential for this workflow.

### Metadata
**Author:** licyk
**Repository:** [https://github.com/licyk/ComfyUI-HakuImg](https://github.com/licyk/ComfyUI-HakuImg)
**Install Type:** git-clone

---

### ComfyUI-Hallo

**Description:**

a comfyui custom node for [a/hallo](https://github.com/fudan-generative-vision/hallo)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-Hallo](https://github.com/AIFSH/ComfyUI-Hallo)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node seems to be related to text generation and doesn"t appear to have any direct connection to image generation or canny edge detection. It might be marginally useful as a supporting node.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/ComfyUI-Hallo](https://github.com/AIFSH/ComfyUI-Hallo)
**Install Type:** git-clone

---

### ComfyUI-Hangover-Nodes

**Description:**

Nodes: MS kosmos-2 Interrogator, Save Image w/o Metadata, Image Scale Bounding Box. An implementation of Microsoft [a/kosmos-2](https://huggingface.co/microsoft/kosmos-2-patch14-224) image to text transformer.

- **Author:** Hangover3832
- **Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Nodes](https://github.com/Hangover3832/ComfyUI-Hangover-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains multiple nodes related to image processing and transformation which could support the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** Hangover3832
**Repository:** [https://github.com/Hangover3832/ComfyUI-Hangover-Nodes](https://github.com/Hangover3832/ComfyUI-Hangover-Nodes)
**Install Type:** git-clone

---

### ComfyUI-HH-Image-Selector

**Description:**

comfy ui custom node that returns an image from a batch based on selected criteria such as RGB value, brightness, etc (credits to chris goringe's custom nodes tutorial ).

- **Author:** haohaocreates
- **Repository:** [https://github.com/haohaocreates/ComfyUI-HH-Image-Selector](https://github.com/haohaocreates/ComfyUI-HH-Image-Selector)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node directly contributes to the workflow goal by selecting images based on criteria such as RGB value and brightness, which is relevant to canny edge detection.

### Metadata
**Author:** haohaocreates
**Repository:** [https://github.com/haohaocreates/ComfyUI-HH-Image-Selector](https://github.com/haohaocreates/ComfyUI-HH-Image-Selector)
**Install Type:** git-clone

---

### ComfyUI-I2V-Adapter

**Description:**

a comfyui custom node for [a/I2V-Adapter](https://github.com/KwaiVGI/I2V-Adapter)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/ComfyUI-I2V-Adapter](https://github.com/AIFSH/ComfyUI-I2V-Adapter)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node adapts I2V-Adapter but its relevance to the workflow goal is unclear without more context.

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

**Score:** 80/100

**Reason:** This node implements i2vgen-xl which could be useful for generating images guided by canny edge detection.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-I2VGEN-XL](https://github.com/chaojie/ComfyUI-I2VGEN-XL)
**Install Type:** git-clone

---

### ComfyUI-ICC-nodes

**Description:**

This repository support processing Comfyui image nodes with ICC profile, load and save images with ICC profile

- **Author:** duhaifeng
- **Repository:** [https://github.com/rubi-du/ComfyUI-ICC-nodes](https://github.com/rubi-du/ComfyUI-ICC-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports image processing with ICC profiles and can load/save images with ICC profiles, making it essential for image generation guided by canny edge detection.

### Metadata
**Author:** duhaifeng
**Repository:** [https://github.com/rubi-du/ComfyUI-ICC-nodes](https://github.com/rubi-du/ComfyUI-ICC-nodes)
**Install Type:** git-clone

---

### ComfyUI-IF_AI_tools

**Description:**

Various AI tools to use in Comfy UI. Starting with VL and prompt making tools using Ollma as backend will evolve as I find time.

- **Author:** if-ai
- **Repository:** [https://github.com/if-ai/ComfyUI-IF_AI_tools](https://github.com/if-ai/ComfyUI-IF_AI_tools)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides various AI tools, but it"s unclear if any of them are specifically related to image generation guided by canny edge detection.

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

**Score:** 81/100

**Reason:** Motion-I2V adapts the Motion-to-Video model for image generation, which could be used in conjunction with canny edge detection for generating images.

### Metadata
**Author:** IDGallagher
**Repository:** [https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V](https://github.com/IDGallagher/ComfyUI-IG-Motion-I2V)
**Install Type:** git-clone

---

### ComfyUI-Image-Captioner

**Description:**

A ComfyUI extension for generating captions for your images. Runs on your own system, no external services used, no filter.
Uses various VLMs with APIs to generate captions for images. You can give instructions or ask questions in natural language.

- **Author:** neverbiasu
- **Repository:** [https://github.com/neverbiasu/ComfyUI-Image-Captioner](https://github.com/neverbiasu/ComfyUI-Image-Captioner)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Image Captioner could be useful as a supporting node for generating captions of images, but it does not directly relate to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** neverbiasu
**Repository:** [https://github.com/neverbiasu/ComfyUI-Image-Captioner](https://github.com/neverbiasu/ComfyUI-Image-Captioner)
**Install Type:** git-clone

---

### ComfyUI-Image-Evaluation

**Description:**

An extension to ComfyUI that evaluates images using multiple models.

- **Author:** wu12023
- **Repository:** [https://github.com/wu12023/ComfyUI-Image-Evaluation](https://github.com/wu12023/ComfyUI-Image-Evaluation)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful in evaluating images using multiple models which could be used for guiding the canny edge detection process.

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

**Score:** 40/100

**Reason:** This node provides image and matte filtering nodes but its direct relevance to canny edge detection is marginal.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)
**Install Type:** git-clone

---

### ComfyUI-Image-Matting

**Description:**

This node improves the quality of the image mask. more suitable for image composite matting

- **Author:** hackkhai
- **Repository:** [https://github.com/hackkhai/ComfyUI-Image-Matting](https://github.com/hackkhai/ComfyUI-Image-Matting)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node improves the quality of the image mask which is crucial for image generation guided by canny edge detection.

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

**Reason:** This node contains tools that are very useful for the specified workflow goal, including resizing and loading images which could be used as input for canny edge detection.

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

**Score:** 60/100

**Reason:** This node is moderately useful for the specified workflow goal as it allows for image cropping, a necessary step in preparing images for canny edge detection.

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

**Reason:** This node has some indirect relevance as it assists in converting an image to sketches or lineArts but does not directly relate to canny edge detection or image generation guided by it.

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

**Reason:** Directly generates images based on input, guided by canny edge detection.

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

**Score:** 40/100

**Reason:** This node converts an image mask to PNG, which is a supporting task in the workflow but not directly related to canny edge detection.

### Metadata
**Author:** freelifehacker
**Repository:** [https://github.com/freelifehacker/ComfyUI-ImgMask2PNG](https://github.com/freelifehacker/ComfyUI-ImgMask2PNG)
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

**Reason:** ✂️ Inpaint Crop and ✂️ Inpaint Stitch nodes are specifically designed for image inpainting tasks which align perfectly with the workflow goal of generating images guided by canny edge detection.

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

**Reason:** InpaintEasy is a set of optimized local repainting nodes that provide intelligent cropping and merging functions, making it very useful for image generation tasks guided by canny edge detection.

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

**Reason:** This node contains multiple nodes that are relevant to image processing and conversion, which could be useful for preparing images for canny edge detection.

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

**Reason:** This node allows interactive selection of options which can be useful for guiding the image generation process based on user input.

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

**Score:** 80/100

**Reason:** This node generates videos frame by frame based on IPAdapter+ControlNet, which could be useful for guiding image generation with canny edge detection.

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

**Score:** 80/100

**Reason:** As a ComfyUI workflow customization by Jake, this node may include customizations that support image generation guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This set of custom nodes includes functionality for saving and loading latents, which could support image generation guided by canny edge detection.

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

**Score:** 61/100

**Reason:** This node set includes various utility nodes that could be used in conjunction with other nodes for image processing tasks, such as thresholding or detail enhancement.

### Metadata
**Author:** kostenickj
**Repository:** [https://github.com/kostenickj/jk-comfyui-helpers](https://github.com/kostenickj/jk-comfyui-helpers)
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

**Reason:** This node allows for querying and processing input JSON data which could be useful in generating images based on canny edge detection results.

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

**Reason:** This extension adds utility functions but doesn"t directly relate to image generation or canny edge detection; it might have supporting features though.

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

**Score:** 95/100

**Reason:** This node is specifically designed for processing images with text prompts using the OpenAI API which aligns well with the workflow goal of generating images guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This keyframing node could be useful for animating parameters that control the canny edge detection process.

### Metadata
**Author:** dmarx
**Repository:** [https://github.com/dmarx/ComfyUI-Keyframed](https://github.com/dmarx/ComfyUI-Keyframed)
**Install Type:** git-clone

---

### ComfyUI-KLingAI-API

**Description:**

Provide high-quality video and image generation capabilities, meeting creators' needs for creative content production and management through more convenient operations, richer functionalities, professional parameters, and stunning effects.

- **Author:** Kling AI
- **Repository:** [https://github.com/KwaiVGI/ComfyUI-KLingAI-API](https://github.com/KwaiVGI/ComfyUI-KLingAI-API)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides high-quality video and image generation capabilities which aligns with the workflow goal of image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node provides a text2image pipeline using diffusers which can be used for image generation and has some relevance to the workflow goal.

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

**Score:** 81/100

**Reason:** ComfyUI-Whisk is likely a node that applies canny edge detection to an image.

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

**Score:** 40/100

**Reason:** LamaApply might be used for image generation but the connection to canny edge detection is unclear.

### Metadata
**Author:** hhhzzyang
**Repository:** [https://github.com/hhhzzyang/Comfyui_Lama](https://github.com/hhhzzyang/Comfyui_Lama)
**Install Type:** git-clone

---

### ComfyUI-layerdiffuse (layerdiffusion)

**Description:**

ComfyUI implementation of [a/LayerDiffusion](https://github.com/layerdiffusion/LayerDiffusion).

- **Author:** huchenlei
- **Repository:** [https://github.com/huchenlei/ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node implements layer diffusion, which is directly related to the workflow goal of generating images guided by canny edge detection.

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

**Reason:** This LightGlue implementation is very useful as it generates motion brush which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 40/100

**Reason:** This node generates portraits from videos but its direct connection to canny edge detection is unclear and may require additional processing steps.

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

**Reason:** This custom node directly enables animal image-based emoji generation from videos using Liveportrait_v2, which aligns closely with the specified workflow goal.

### Metadata
**Author:** VangengLab
**Repository:** [https://github.com/VangengLab/ComfyUI-LivePortrait_v2](https://github.com/VangengLab/ComfyUI-LivePortrait_v2)
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

**Reason:** This node directly mentions replicating the API for Live Portrait in ComfyUI, which is relevant to image generation and might involve edge detection.

### Metadata
**Author:** LightSketch-ai
**Repository:** [https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode](https://github.com/LightSketch-ai/ComfyUI-LivePortraitNode)
**Install Type:** git-clone

---

### comfyui-llm-assistant

**Description:**

Nodes:Generate Stable Diffsution Prompt With LLM, Translate Text With LLM, Chat With LLM

- **Author:** longgui0318
- **Repository:** [https://github.com/longgui0318/comfyui-llm-assistant](https://github.com/longgui0318/comfyui-llm-assistant)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node offers LLaMA-based functionality that includes generating stable diffusion prompts, which is directly relevant to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** longgui0318
**Repository:** [https://github.com/longgui0318/comfyui-llm-assistant](https://github.com/longgui0318/comfyui-llm-assistant)
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

**Reason:** This node allows calling various language models, including local ones, but it does not have any specific features related to image generation or canny edge detection, making its utility marginal for this workflow.

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

**Score:** 80/100

**Reason:** This node loads images and prompts from a directory, which could be useful for providing input data for the image generation task.

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

**Score:** 90/100

**Reason:** This node directly loads an image from a URL or local path, making it highly relevant to the workflow goal of generating images.

### Metadata
**Author:** tsogzark
**Repository:** [https://github.com/tsogzark/ComfyUI-load-image-from-url](https://github.com/tsogzark/ComfyUI-load-image-from-url)
**Install Type:** git-clone

---

### comfyui-load-image-in-seq

**Description:**

This node is load png image sequentially with metadata. Only supported for PNG format that has been created by ComfyUI.[w/renamed from comfyui-load-image-39. You need to remove previous one and reinstall to this.]

- **Author:** shinich39
- **Repository:** [https://github.com/shinich39/comfyui-load-image-in-seq](https://github.com/shinich39/comfyui-load-image-in-seq)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is specific to loading PNG images created by ComfyUI, which may not be directly applicable to the workflow goal unless using such images.

### Metadata
**Author:** shinich39
**Repository:** [https://github.com/shinich39/comfyui-load-image-in-seq](https://github.com/shinich39/comfyui-load-image-in-seq)
**Install Type:** git-clone

---

### ComfyUI-LoadImage-Advanced

**Description:**

This is a node that simply integrates LoadImage, Vae Encode, Upscale, Resolution factor correction, and Color Adjustment.

- **Author:** souki202
- **Repository:** [https://github.com/souki202/ComfyUI-LoadImage-Advanced](https://github.com/souki202/ComfyUI-LoadImage-Advanced)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node integrates multiple functionalities that are essential for image processing and generation, including loading images, encoding, upsampling, and color adjustment, making it very useful for this workflow goal.

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

**Score:** 80/100

**Reason:** This node extends the LoadImage functionality with subfolder support, which is moderately relevant to the workflow goal but can be a significant utility in accessing specific image folders.

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

**Reason:** This node directly supports long-clip token replacement in ComfyUI which could be useful for generating images with longer context based on canny edge detection results.

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

**Score:** 61/100

**Reason:** ComfyUI-Loop-image provides specific functions for image processing and segmentation, making it moderately useful for the specified workflow goal.

### Metadata
**Author:** WainWong
**Repository:** [https://github.com/WainWong/ComfyUI-Loop-image](https://github.com/WainWong/ComfyUI-Loop-image)
**Install Type:** git-clone

---

### ComfyUI-LTXTricks

**Description:**

A set of nodes that provide additional controls for the LTX Video model

- **Author:** logtd
- **Repository:** [https://github.com/logtd/ComfyUI-LTXTricks](https://github.com/logtd/ComfyUI-LTXTricks)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides additional controls that could be useful in conjunction with a model that uses canny edge detection for image generation.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-LTXTricks](https://github.com/logtd/ComfyUI-LTXTricks)
**Install Type:** git-clone

---

### ComfyUI-LuminaWrapper

**Description:**

ComfyUI wrapper nodes for Lumina models

- **Author:** kijai
- **Repository:** [https://github.com/kijai/ComfyUI-LuminaWrapper](https://github.com/kijai/ComfyUI-LuminaWrapper)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node integrates Lumina models, which are suitable for high-quality image generation and could be used in conjunction with canny edge detection.

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

**Score:** 90/100

**Reason:** This node provides a direct interface for ImageMagick which is commonly used in image processing and can be useful for tasks involving canny edge detection.

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

**Reason:** ComfyUI-Manager can manage custom nodes, which could include a canny edge detection node, making it essential for this workflow.

### Metadata
**Author:** Dr.Lt.Data
**Repository:** [https://github.com/ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
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

**Reason:** This node is essential for filtering masks based on criteria, which is crucial for guiding image generation with canny edge detection.

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

**Score:** 100/100

**Reason:** This node generates all possible additive combinations of a mask batch, which is directly relevant to exploring different edge detection scenarios in image generation.

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

**Reason:** This node enhances prompt engineering with a Magic Photo Prompter, which could be useful for generating high-quality prompts for image generation guided by canny edge detection.

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

**Score:** 81/100

**Reason:** Directly integrates with Midjourney API to generate images based on canny edge detection.

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

**Score:** 61/100

**Reason:** Supports image generation guided by canny edge detection through inpainting with a reference image.

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

**Score:** 41/100

**Reason:** Provides an optimized wrapper for MimicMotion but does not directly contribute to canny edge detection or image generation.

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

**Score:** 70/100

**Reason:** Provides nodes that could be useful in preprocessing images (e.g., converting grayscale channels) before applying canny edge detection.

### Metadata
**Author:** mingsky
**Repository:** [https://github.com/mingsky-ai/ComfyUI-MingNodes](https://github.com/mingsky-ai/ComfyUI-MingNodes)
**Install Type:** git-clone

---

### comfyui-mixlab-nodes

**Description:**

3D, ScreenShareNode & FloatingVideoNode, SpeechRecognition & SpeechSynthesis, GPT, LoadImagesFromLocal, Layers, Other Nodes, ...

- **Author:** shadowcz007
- **Repository:** [https://github.com/shadowcz007/comfyui-mixlab-nodes](https://github.com/shadowcz007/comfyui-mixlab-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node has many features that could be useful for image generation guided by canny edge detection, including 3D nodes and GPT integration.

### Metadata
**Author:** shadowcz007
**Repository:** [https://github.com/shadowcz007/comfyui-mixlab-nodes](https://github.com/shadowcz007/comfyui-mixlab-nodes)
**Install Type:** git-clone

---

### ComfyUI-ModelDownloader

**Description:**

A ComfyUI node to download models(Checkpoints and LoRA) from external links and act as an output standalone node.

- **Author:** holchan
- **Repository:** [https://github.com/holchan/ComfyUI-ModelDownloader](https://github.com/holchan/ComfyUI-ModelDownloader)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows for downloading external models which could be necessary for implementing canny edge detection in an image generation workflow.

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

**Reason:** This node provides a MoGe model and process but does not explicitly mention canny edge detection. It may still be useful as a supporting node but its relevance is uncertain.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-MoGe](https://github.com/kijai/ComfyUI-MoGe)
**Install Type:** git-clone

---

### ComfyUI-Moondream-Gaze-Detection

**Description:**

Moondream's gaze detection feature node from [a/ComfyUI-Moondream-Gaze-Detection](https://github.com/jhj0517/ComfyUI-Moondream-Gaze-Detection).

- **Author:** jhj0517
- **Repository:** [https://github.com/jhj0517/ComfyUI-Moondream-Gaze-Detection](https://github.com/jhj0517/ComfyUI-Moondream-Gaze-Detection)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node has gaze detection feature which could potentially utilize canny edge detection for accurate gaze tracking in the context of image generation.

### Metadata
**Author:** jhj0517
**Repository:** [https://github.com/jhj0517/ComfyUI-Moondream-Gaze-Detection](https://github.com/jhj0517/ComfyUI-Moondream-Gaze-Detection)
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

**Reason:** This node detects and masks mosaic areas which could be useful for pre-processing images before applying canny edge detection.

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

**Reason:** This node controls motion in images but its relevance to the workflow goal is indirect and may require additional context.

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

**Score:** 40/100

**Reason:** No reason provided

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

**Score:** 81/100

**Reason:** This remastered version of MusePose supports auto weights download and has fewer dependencies, making it a very useful choice for the specified workflow goal.

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

**Score:** 90/100

**Reason:** This node integrates MV-Adapter which can generate multi-view consistent images and might utilize canny edge detection for image processing.

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

**Score:** 90/100

**Reason:** This node contains mask processing nodes that could be useful for generating masks from canny edge detection results.

### Metadata
**Author:** jerrylongyan
**Repository:** [https://github.com/jerrylongyan/ComfyUI-My-Mask](https://github.com/jerrylongyan/ComfyUI-My-Mask)
**Install Type:** git-clone

---

### ComfyUI-NegiTools

**Description:**

Nodes:OpenAI DALLe3, OpenAI Translate to English, String Function, Seed Generator

- **Author:** natto-maki
- **Repository:** [https://github.com/natto-maki/ComfyUI-NegiTools](https://github.com/natto-maki/ComfyUI-NegiTools)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node includes several nodes that could be useful for the specified workflow goal, such as OpenAI DALLe3 and String Function, which could aid in generating images based on text or other input.

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

**Reason:** This node is a set of custom nodes but does not have any specific features mentioned that would directly contribute to image generation guided by canny edge detection.

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

**Score:** 81/100

**Reason:** This node provides a layout plugin that includes features like node alignment and resizing, which could be useful for arranging nodes in a visual editor or custom UI component related to image generation.

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

**Score:** 80/100

**Reason:** This node provides various custom nodes that could be useful for image processing and generation tasks, including those related to latent variables and sampling.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows for intuitive adjustment of numerous numerical parameters, which could be used to fine-tune image generation settings based on canny edge detection results.

### Metadata
**Author:** Assistant
**Repository:** [https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders](https://github.com/NakamuraShippo/ComfyUI-NS-ManySliders)
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

**Reason:** This node allows for integration with LLM models that can understand and describe images, making it very useful for image generation guided by canny edge detection.

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

**Reason:** This custom node suite is specifically designed to work with Ollama servers, which can be used for generating images based on descriptions or other input, making it highly relevant and useful for the specified workflow goal.

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

**Score:** 100/100

**Reason:** This node directly uses ollama to generate prompts based on reference text in comfyui, which can be used as input for canny edge detection and subsequent image generation.

### Metadata
**Author:** Tlant
**Repository:** [https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant](https://github.com/Tlant/ComfyUI-OllamaPromptsGeneratorTlant)
**Install Type:** git-clone

---

### ComfyUI-OneForOne

**Description:**

Node:Image Fit Calculator

- **Author:** Meettya
- **Repository:** [https://github.com/Meettya/ComfyUI-OneForOne](https://github.com/Meettya/ComfyUI-OneForOne)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly calculates image fit which could be useful for aligning generated images with the detected edges from canny edge detection.

### Metadata
**Author:** Meettya
**Repository:** [https://github.com/Meettya/ComfyUI-OneForOne](https://github.com/Meettya/ComfyUI-OneForOne)
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

**Reason:** This wrapper node supports Open-Sora t2i and i2i, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-OpenDiTWrapper](https://github.com/kijai/ComfyUI-OpenDiTWrapper)
**Install Type:** git-clone

---

### ComfyUI-Openpose-Editor-Plus

**Description:**

Nodes:Openpose Editor Plus

- **Author:** whmc76
- **Repository:** [https://github.com/whmc76/ComfyUI-Openpose-Editor-Plus](https://github.com/whmc76/ComfyUI-Openpose-Editor-Plus)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node appears to be an extension of Openpose Editor, but its relevance and utility for the specified workflow goal are unclear without further information.

### Metadata
**Author:** whmc76
**Repository:** [https://github.com/whmc76/ComfyUI-Openpose-Editor-Plus](https://github.com/whmc76/ComfyUI-Openpose-Editor-Plus)
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

**Reason:** This node provides a VAE decode function which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** M1kep
**Repository:** [https://github.com/M1kep/ComfyUI-OtherVAEs](https://github.com/M1kep/ComfyUI-OtherVAEs)
**Install Type:** git-clone

---

### ComfyUI-Paint3D-Nodes

**Description:**

Paint3D Nodes is a custom ComfyUI node for 3D model texture inpainting based on [a/Paint3D](https://arxiv.org/pdf/2312.13913).

- **Author:** N3rd00d
- **Repository:** [https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is related to 3D model texture inpainting but its relevance to image generation guided by canny edge detection is unclear.

### Metadata
**Author:** N3rd00d
**Repository:** [https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes)
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

**Reason:** This node provides a powerful bridge to Photoshop, which is commonly used for image editing and manipulation, including canny edge detection.

### Metadata
**Author:** NimaNzrii
**Repository:** [https://github.com/NimaNzrii/comfyui-photoshop](https://github.com/NimaNzrii/comfyui-photoshop)
**Install Type:** git-clone

---

### ComfyUI-PhyCV

**Description:**

Nodes:PhyCV - Phase-Stretch Transform (PST), PhyCV - VEViD, PhyCV - Page.

- **Author:** JPrevots
- **Repository:** [https://github.com/JPrevots/ComfyUI-PhyCV](https://github.com/JPrevots/ComfyUI-PhyCV)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node offers various PhyCV nodes that could be useful in image processing tasks, but none of them are specifically related to canny edge detection or image generation.

### Metadata
**Author:** JPrevots
**Repository:** [https://github.com/JPrevots/ComfyUI-PhyCV](https://github.com/JPrevots/ComfyUI-PhyCV)
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

**Reason:** Pillow provides a suite of basic image manipulation tools that can be used for image generation and processing, including potential use with canny edge detection.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI-PIL](https://github.com/SoftMeng/ComfyUI-PIL)
**Install Type:** git-clone

---

### comfyui-pixel

**Description:**

pixel art workshop nodes for comfyui.

- **Author:** wandbrandon
- **Repository:** [https://github.com/wandbrandon/comfyui-pixel](https://github.com/wandbrandon/comfyui-pixel)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Pixel art workshop nodes for comfyui may include tools that could be used for image generation and processing, but it"s less directly relevant than Pillow.

### Metadata
**Author:** wandbrandon
**Repository:** [https://github.com/wandbrandon/comfyui-pixel](https://github.com/wandbrandon/comfyui-pixel)
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

**Reason:** This node calculates pixel resolution and aspect ratio which could be useful in the context of canny edge detection for image generation.

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

**Reason:** This node directly generates portraits based on canny edge detection, making it essential for the specified workflow goal.

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

**Reason:** Although this node collection focuses on post-processing tasks, it may contain nodes that can be used in conjunction with other tools for image generation guided by canny edge detection.

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

**Reason:** This node provides customizable classifier-free guidance for ComfyUI, which aligns well with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** redhottensors
**Repository:** [https://github.com/redhottensors/ComfyUI-Prediction](https://github.com/redhottensors/ComfyUI-Prediction)
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

**Reason:** This node allows for previewing latents without VAE decoding, which can be useful for intermediate results and faster image previews during the workflow process.

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

**Score:** 80/100

**Reason:** This node provides a suite of tools for prompt management, which is essential for generating high-quality images guided by canny edge detection.

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

**Reason:** This node uses llama.cpp and might be able to generate some nodes related to prompt word work, but it"s unclear how this would apply to canny edge detection.

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

**Score:** 40/100

**Reason:** This node provides a prompt helper but its relevance to canny edge detection in image generation is unclear.

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

**Reason:** This node provides various utility functions for prompts, which could be useful in generating text that guides the image generation process.

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

**Score:** 70/100

**Reason:** This node offers filename and keyword generation features, which might be helpful in creating descriptive file names or keywords related to the generated images.

### Metadata
**Author:** Black-Lioness
**Repository:** [https://github.com/Black-Lioness/ComfyUI-PromptUtils](https://github.com/Black-Lioness/ComfyUI-PromptUtils)
**Install Type:** git-clone

---

### ComfyUI-Qais-Helper

**Description:**

This Extension adds a few custom QOL nodes that ComfyUI lacks by default.

- **Author:** Qais Malkawi
- **Repository:** [https://github.com/QaisMalkawi/ComfyUI-QaisHelper](https://github.com/QaisMalkawi/ComfyUI-QaisHelper)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this extension provides some quality-of-life features, none of them directly relate to canny edge detection or image generation.

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

**Reason:** This node collection may offer batching and captioning capabilities but its relevance to the specified workflow goal of image generation guided by canny edge detection is uncertain due to the presence of bugs and lack of direct relation to edge detection.

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

**Score:** 81/100

**Reason:** This node implements RAFT, which is a motion field estimation algorithm that could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** chaojie
**Repository:** [https://github.com/chaojie/ComfyUI-RAFT](https://github.com/chaojie/ComfyUI-RAFT)
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

**Score:** 90/100

**Reason:** This node specifically uses RAVE attention as a temporal mechanism that aligns well with the workflow goal of guided image generation using canny edge detection.

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

**Reason:** This node provides fine-grained control over style transfer which could be useful for generating images guided by canny edge detection.

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

**Reason:** This node may provide some utility in terms of reference sampling but its relevance to canny edge detection is unclear.

### Metadata
**Author:** logtd
**Repository:** [https://github.com/logtd/ComfyUI-RefSampling](https://github.com/logtd/ComfyUI-RefSampling)
**Install Type:** git-clone

---

### ComfyUI-Remover

**Description:**

Custom node for ComfyUI that makes parts of the image transparent (face, background...)

- **Author:** Shraknard
- **Repository:** [https://github.com/Shraknard/ComfyUI-Remover](https://github.com/Shraknard/ComfyUI-Remover)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can make parts of an image transparent, which could be useful for edge detection.

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

**Score:** 80/100

**Reason:** This node allows direct access to Replicate models, which can be used for image generation and may include canny edge detection capabilities.

### Metadata
**Author:** fofr
**Repository:** [https://github.com/replicate/comfyui-replicate](https://github.com/replicate/comfyui-replicate)
**Install Type:** git-clone

---

### ComfyUI-RequestPoster

**Description:**

This extension can send HTTP Requests. You can request image generation to StableDiffusion3 and post images to X (Twitter) and Discord.

- **Author:** aburahamu
- **Repository:** [https://github.com/aburahamu/ComfyUI-RequestsPoster](https://github.com/aburahamu/ComfyUI-RequestsPoster)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node enables sending HTTP requests, allowing you to request image generation from StableDiffusion3 and post images to social media platforms, making it highly relevant to the workflow goal.

### Metadata
**Author:** aburahamu
**Repository:** [https://github.com/aburahamu/ComfyUI-RequestsPoster](https://github.com/aburahamu/ComfyUI-RequestsPoster)
**Install Type:** git-clone

---

### ComfyUI-RGT

**Description:**

This repo cast Recursive Generalization Transformer for Image Super-Resolution to ComfyUI, the original [a/paper link](https://arxiv.org/abs/2303.06373) and [a/github link](https://github.com/zhengchen1999/RGT)

- **Author:** viperyl
- **Repository:** [https://github.com/viperyl/ComfyUI-RGT](https://github.com/viperyl/ComfyUI-RGT)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node implements Recursive Generalization Transformer for Image Super-Resolution, which could be used in conjunction with canny edge detection for advanced image processing tasks.

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

**Score:** 85/100

**Reason:** This node provides a variety of image manipulation nodes that could be useful for preparing images for canny edge detection or post-processing the results.

### Metadata
**Author:** ricklove
**Repository:** [https://github.com/ricklove/comfyui-ricklove](https://github.com/ricklove/comfyui-ricklove)
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

**Reason:** This node is a wrapper for an image-to-video model that could be used in conjunction with canny edge detection to generate images or videos.

### Metadata
**Author:** IamCreateAI
**Repository:** [https://github.com/IamCreateAI/Ruyi-Models](https://github.com/IamCreateAI/Ruyi-Models)
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

**Reason:** This SASolver node directly supports the workflow goal by utilizing canny edge detection for image generation.

### Metadata
**Author:** mira-6
**Repository:** [https://github.com/mira-6/comfyui-sasolver](https://github.com/mira-6/comfyui-sasolver)
**Install Type:** git-clone

---

### ComfyUI-SaveImageCivitAI

**Description:**

A custom node allowing to save images with CIVITAI readable datas

- **Author:** Wakfull33
- **Repository:** [https://github.com/Wakfull33/ComfyUI-SaveImageCivitAI](https://github.com/Wakfull33/ComfyUI-SaveImageCivitAI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for saving images with CIVITAI readable data, which could be used in the image generation process.

### Metadata
**Author:** Wakfull33
**Repository:** [https://github.com/Wakfull33/ComfyUI-SaveImageCivitAI](https://github.com/Wakfull33/ComfyUI-SaveImageCivitAI)
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

**Score:** 90/100

**Reason:** This node is essential for saving images with metadata extracted from the input values of each node, which could be used in the image generation process and also allows for dynamic value addition.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows scaling images to a target megapixel size, which could be necessary after applying canny edge detection.

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

**Reason:** This node is very useful for the specified workflow goal as it contains nodes that support scheduled CFG guider which is related to canny edge detection.

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

**Score:** 40/100

**Reason:** This node is moderately useful as it supports Stable Diffusion 3 Medium which might be related to image generation, but the direct connection to canny edge detection is unclear.

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

**Reason:** SD3 Attention To Image is directly relevant to generating an image, which aligns with the workflow goal.

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

**Reason:** SD3 Latent Select Resolution allows for selecting a resolution that can be used in conjunction with canny edge detection for image generation.

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

**Score:** 41/100

**Reason:** SDXL Empty Latent Image provides a way to select a resolution, but its direct relevance to canny edge detection is limited.

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

**Score:** 100/100

**Reason:** Image Resize (seam carving) directly supports the workflow goal by intelligently resizing images while keeping important contents undistorted and allowing for object removal without artifacts.

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

**Score:** 80/100

**Reason:** This node provides access to SeeCoder from Prompt-Free-Diffusion, which could be useful for generating images based on canny edge detection.

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

**Score:** 90/100

**Reason:** This node provides access to Smoothed Energy Guidance from SEG-SDXL, which could be essential for generating images based on canny edge detection.

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

**Reason:** This node provides an image or video segmentation feature that could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** kijai
**Repository:** [https://github.com/kijai/ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2)
**Install Type:** git-clone

---

### ComfyUI-SimDA

**Description:**

Nodes:SimDATrain, SimDALoader, SimDARun, VHS_FILENAMES_STRING_SimDA

- **Author:** chaojie
- **Repository:** [https://github.com/chaojie/ComfyUI-SimDA](https://github.com/chaojie/ComfyUI-SimDA)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a set of nodes that could be used for image generation guided by canny edge detection, including training, loading, and running SimDA.

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

**Score:** 40/100

**Reason:** This node is marginally relevant as it could be used to save and review previous workflow attempts, but it doesn"t directly contribute to image generation or canny edge detection.

### Metadata
**Author:** moustafa-nasr
**Repository:** [https://github.com/moustafa-nasr/ComfyUI-SimpleLogger](https://github.com/moustafa-nasr/ComfyUI-SimpleLogger)
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

**Reason:** This node is very useful as it applies smart cropping which could be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node provides access to snake oil nLoRAs and negative LoRAs which are directly related to the workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node contains some nodes that may be relevant to image processing, but it does not specifically mention canny edge detection or image generation.

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

**Score:** 80/100

**Reason:** This node provides a collection of ComfyUI nodes with various image-processing functionalities, which could potentially be used for canny edge detection and image generation.

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

**Score:** 80/100

**Reason:** ComfyUI-SoundHub offers a collection of audio processing nodes which could be useful for generating sounds that might interact with the image generated by canny edge detection.

### Metadata
**Author:** Yuan-ManX
**Repository:** [https://github.com/Yuan-ManX/ComfyUI-SoundHub](https://github.com/Yuan-ManX/ComfyUI-SoundHub)
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

**Reason:** This node provides a mechanism for implementing wildcard patterns that could be used in conjunction with canny edge detection for image generation.

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

**Score:** 90/100

**Reason:** This node provides a stereopsis effect which can be used in conjunction with canny edge detection for immersive media experiences.

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

**Reason:** Although this node pack contains miscellaneous nodes for debugging string data, it may still provide some utility as a supporting node for collecting generation data in the workflow.

### Metadata
**Author:** PressWagon
**Repository:** [https://github.com/PressWagon/ComfyUI-StringsAndThings](https://github.com/PressWagon/ComfyUI-StringsAndThings)
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

**Reason:** This node provides direct support for StyleGAN2 and StyleGAN3 models, which can be used to generate images. It is highly relevant to the specified workflow goal.

### Metadata
**Author:** spacepxl
**Repository:** [https://github.com/spacepxl/ComfyUI-StyleGan](https://github.com/spacepxl/ComfyUI-StyleGan)
**Install Type:** git-clone

---

### ComfyUI-StyleTransferPlus

**Description:**

Nodes:Neural Neighbor, CAST, EFDM, MicroAST, Coral Color Transfer.

- **Author:** Fuou Marinas
- **Repository:** [https://github.com/FuouM/ComfyUI-StyleTransferPlus](https://github.com/FuouM/ComfyUI-StyleTransferPlus)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a style transfer functionality that can utilize canny edge detection for guided image generation.

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

**Reason:** This node directly upscaling inside the latent space which is useful for image generation and can be used in conjunction with canny edge detection.

### Metadata
**Author:** styler00dollar
**Repository:** [https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale](https://github.com/styler00dollar/ComfyUI-sudo-latent-upscale)
**Install Type:** git-clone

---

### ComfyUI-SVDResizer

**Description:**

SVDResizer is a helper for resizing the source image, according to the sizes enabled in Stable Video Diffusion. The rationale behind the possibility of changing the size of the image in steps between the ranges of 576 and 1024, is the use of the greatest common denominator of these two numbers which is 64. SVD is lenient with resizing that adheres to this rule, so the chance of coherent video that is not the standard size of 576X1024 is greater. It is advisable to keep the value 1024 constant and play with the second size to maintain the stability of the result.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI-SVDResizer](https://github.com/ShmuelRonen/ComfyUI-SVDResizer)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node specifically deals with resizing the source image according to the sizes enabled in Stable Video Diffusion, which is essential for maintaining stability when using canny edge detection for image generation.

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

**Score:** 100/100

**Reason:** This node provides a preview of the SVG file which could be useful for visualizing the output of the canny edge detection process.

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

**Score:** 90/100

**Reason:** This node is highly relevant and useful for the specified workflow goal as it uses Florence2 VLM for tasks such as object detection, captioning, segmentation and ocr which are closely related to image generation.

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

**Reason:** This node contains various image processing nodes that could be useful for generating images guided by canny edge detection, such as ImageLoader, ImageSaver, and GFPGANNode.

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

**Reason:** This node implements Trajectory Consistency Distillation based on Zheng et al., which is closely related to the workflow goal of image generation guided by canny edge detection.

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

**Score:** 90/100

**Reason:** ComfyUI Template Loader is not directly relevant to image generation, but it can help streamline the workflow by loading frequently used prompts with just a few clicks.

### Metadata
**Author:** r3dsd
**Repository:** [https://github.com/r3dsd/comfyui-template-loader](https://github.com/r3dsd/comfyui-template-loader)
**Install Type:** git-clone

---

### ComfyUI-TemporaryLoader

**Description:**

This is a custom node of ComfyUI that downloads and loads models from the input URL. The model is temporarily downloaded into memory and not saved to storage.
This could be useful when trying out models or when using various models on machines with limited storage. Since the model is downloaded into memory, expect higher memory usage than usual.

- **Author:** pkpk
- **Repository:** [https://github.com/pkpkTech/ComfyUI-TemporaryLoader](https://github.com/pkpkTech/ComfyUI-TemporaryLoader)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** TemporaryLoader might be useful for downloading models required for canny edge detection, but its primary purpose is model loading and memory management.

### Metadata
**Author:** pkpk
**Repository:** [https://github.com/pkpkTech/ComfyUI-TemporaryLoader](https://github.com/pkpkTech/ComfyUI-TemporaryLoader)
**Install Type:** git-clone

---

### ComfyUI-Tensor-Operations

**Description:**

This repo contains nodes for ComfyUI that implement some helpful operations on tensors, such as normalization.

- **Author:** ttulttul
- **Repository:** [https://github.com/ttulttul/ComfyUI-Tensor-Operations](https://github.com/ttulttul/ComfyUI-Tensor-Operations)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Tensor-Operations nodes could potentially be used in conjunction with other nodes to implement canny edge detection or related image processing tasks.

### Metadata
**Author:** ttulttul
**Repository:** [https://github.com/ttulttul/ComfyUI-Tensor-Operations](https://github.com/ttulttul/ComfyUI-Tensor-Operations)
**Install Type:** git-clone

---

### ComfyUI-Text_Image-Composite [WIP]

**Description:**

Nodes:Text_Image_Zho, Text_Image_Multiline_Zho, RGB_Image_Zho, AlphaChanelAddByMask, ImageComposite_Zho, ...

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides functionality related to image composition and manipulation, which could be useful for generating images guided by canny edge detection.

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

**Score:** 81/100

**Reason:** Directly adds text to areas detected by canny edge detection, aligning with the workflow goal.

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

**Reason:** Provides a flexible way to overlay text on images, which is essential for adding context to edge-detection results.

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

**Reason:** While this node is related to image processing, its primary functions (loading thumbnails, deleting images) are not directly relevant to canny edge detection or image generation.

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

**Reason:** This node implements the timestep shift technique, which could be useful for image generation. The specific implementation in ComfyUI makes it a potentially valuable tool for this workflow goal.

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

**Score:** 80/100

**Reason:** This node is essential as it allows encoding prompts in TOML format which could be used for guiding the image generation process based on canny edge detection.

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

**Score:** 40/100

**Reason:** This node provides preview and save functionality but does not directly relate to canny edge detection or image generation. However, it could potentially support tasks related to visualizing generated images.

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

**Score:** 80/100

**Reason:** This node provides ToonCrafter integration with ComfyUI, which could be useful for generative keyframe animation and may involve edge detection techniques.

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

**Score:** 81/100

**Reason:** This node is very useful as it converts raster images into SVG format which could be used for vector graphics and potentially canny edge detection.

### Metadata
**Author:** Yanick112
**Repository:** [https://github.com/Yanick112/ComfyUI-ToSVG](https://github.com/Yanick112/ComfyUI-ToSVG)
**Install Type:** git-clone

---

### ComfyUI-TrollSuite

**Description:**

Nodes: BinaryImageMask, ImagePadding, LoadLastCreatedImage, RandomMask, TransparentImage.

- **Author:** oyvindg
- **Repository:** [https://github.com/oyvindg/ComfyUI-TrollSuite](https://github.com/oyvindg/ComfyUI-TrollSuite)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** The suite contains various nodes that could be useful for image processing tasks, but none are specifically related to canny edge detection.

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

**Score:** 90/100

**Reason:** This node is very useful as it performs pose estimation and rendering, which are directly related to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-estimator)
**Install Type:** git-clone

---

### ComfyUI-ultimate-openpose-estimator

**Description:**

Enhanced features with flexible choice of inputs and outputs, fine control for pose plotting, freedom to composite poses and fast local pose editting.

- **Author:** westNeighbor
- **Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is essential for this workflow as it provides fine control over pose plotting and allows for composition and editing of poses, supporting the goal of image generation.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor)
**Install Type:** git-clone

---

### ComfyUI-ultimate-openpose-render

**Description:**

The ultimate openpose render node for ComfyUI with flexible input, output and adjustment.

- **Author:** westNeighbor
- **Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node is very useful as it offers flexible input and output options for openpose rendering, which aligns with the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** westNeighbor
**Repository:** [https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-render)
**Install Type:** git-clone

---

### comfyui-undistort

**Description:**

Node:Load Checkerboard Images for Calibrate Camera, Matrix and distortion coefficient to text, Undistort

- **Author:** iFREEGROUP
- **Repository:** [https://github.com/iFREEGROUP/comfyui-undistort](https://github.com/iFREEGROUP/comfyui-undistort)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly supports loading and undistorting images which could be used as input for canny edge detection or as part of an image generation pipeline.

### Metadata
**Author:** iFREEGROUP
**Repository:** [https://github.com/iFREEGROUP/comfyui-undistort](https://github.com/iFREEGROUP/comfyui-undistort)
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

**Reason:** This node allows unloading models which can free up memory for other tasks like edge detection and image generation.

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

**Reason:** This node allows upscaling images using a model which is relevant for generating high-quality images that may be used in conjunction with edge detection.

### Metadata
**Author:** TheBill2001
**Repository:** [https://github.com/TheBill2001/comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model)
**Install Type:** git-clone

---

### ComfyUI-Venice-API

**Description:**

A custom node implementation for ComfyUI that integrates with venice.ai's Flux and SDXL image generation models. This project is adapted from [a/ComfyUI-FLUX-TOGETHER-API](https://github.com/BZcreativ/ComfyUI-FLUX-TOGETHER-API) to work with the venice.ai API.

- **Author:** DraconicDragon
- **Repository:** [https://github.com/DraconicDragon/ComfyUI-Venice-API](https://github.com/DraconicDragon/ComfyUI-Venice-API)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for the specified workflow goal as it provides a custom API integration with venice.ai"s Flux and SDXL image generation models that utilize canny edge detection.

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

**Reason:** This node provides video matting capabilities which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** Fannovel16
**Repository:** [https://github.com/Fannovel16/ComfyUI-Video-Matting](https://github.com/Fannovel16/ComfyUI-Video-Matting)
**Install Type:** git-clone

---

### ComfyUI-VisualQueryTemplate

**Description:**

A ComfyUI node for transforming images into descriptive text using templated visual question answering. Leverages Hugging Face's VQA models with transformers

- **Author:** celoron
- **Repository:** [https://github.com/celoron/ComfyUI-VisualQueryTemplate](https://github.com/celoron/ComfyUI-VisualQueryTemplate)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node leverages Hugging Face"s VQA models with transformers and can transform images into descriptive text, which could be useful for generating guided image descriptions based on canny edge detection results.

### Metadata
**Author:** celoron
**Repository:** [https://github.com/celoron/ComfyUI-VisualQueryTemplate](https://github.com/celoron/ComfyUI-VisualQueryTemplate)
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

**Reason:** This node uses VLM capabilities from Claude or ChatGPT 4 to generate captions/tags for images, which could be useful for generating guided image descriptions based on canny edge detection results.

### Metadata
**Author:** 5x00
**Repository:** [https://github.com/5x00/ComfyUI-VLM-Captions](https://github.com/5x00/ComfyUI-VLM-Captions)
**Install Type:** git-clone

---

### comfyui-webcam-node

**Description:**

Nodes:Webcam Capture

- **Author:** uetuluk
- **Repository:** [https://github.com/uetuluk/comfyui-webcam-node](https://github.com/uetuluk/comfyui-webcam-node)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node captures webcam feed which might be useful for some image processing tasks but lacks direct relevance to canny edge detection.

### Metadata
**Author:** uetuluk
**Repository:** [https://github.com/uetuluk/comfyui-webcam-node](https://github.com/uetuluk/comfyui-webcam-node)
**Install Type:** git-clone

---

### ComfyUI-X-Portrait-Nodes

**Description:**

Implementation of X-Portrait nodes for ComfyUI, animate portraits with an input video and a reference image.

- **Author:** akatz-ai
- **Repository:** [https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes](https://github.com/akatz-ai/ComfyUI-X-Portrait-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node directly supports image generation by providing animated portrait functionality guided by a reference image.

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

**Score:** 100/100

**Reason:** This node directly relates to image processing and provides a canvas view which is essential for displaying images generated by the workflow.

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

**Reason:** This node directly relates to object recognition and uses YOLO (You Only Look Once) algorithm which is useful for detecting edges in images and guiding the workflow goal.

### Metadata
**Author:** kadirnar
**Repository:** [https://github.com/kadirnar/ComfyUI-YOLO](https://github.com/kadirnar/ComfyUI-YOLO)
**Install Type:** git-clone

---

### ComfyUI-Yuan

**Description:**

Some simple&practical ComfyUI image processing nodes.

- **Author:** Cyber-Blacat
- **Repository:** [https://github.com/Cyber-Blacat/ComfyUI-Yuan](https://github.com/Cyber-Blacat/ComfyUI-Yuan)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains some simple and practical ComfyUI image processing nodes, but there is no specific mention of canny edge detection or its application in image generation.

### Metadata
**Author:** Cyber-Blacat
**Repository:** [https://github.com/Cyber-Blacat/ComfyUI-Yuan](https://github.com/Cyber-Blacat/ComfyUI-Yuan)
**Install Type:** git-clone

---

### ComfyUI_Auto_Caption

**Description:**

This report contains a 'load many images' node which is going to load the image set by the number of file names from smallest to largest, and the images will no longer be loaded in the wrong order! Setting index=0 makes it load from the first small value (image flie name) image, and index=2 will load them from the second image. Another node 'load images & resize' can resize the image by the first loaded image.

- **Author:** Cyber-BCat
- **Repository:** [https://github.com/Cyber-BCat/ComfyUI_Auto_Caption](https://github.com/Cyber-BCat/ComfyUI_Auto_Caption)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it automatically loads images in the correct order and resizes them based on the first loaded image, which could be used as a supporting step for generating images guided by canny edge detection.

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

**Reason:** This node contains multiple tools related to image processing and manipulation, including potential overlap detection which could aid in canny edge detection.

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

**Reason:** This node provides tools for using BiRefNet, a model that can perform image background removal which could be useful in conjunction with canny edge detection for image generation purposes.

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

**Score:** 80/100

**Reason:** BMAB provides post-processing functions that could be useful for refining images generated with canny edge detection.

### Metadata
**Author:** portu-sim
**Repository:** [https://github.com/portu-sim/comfyui_bmab](https://github.com/portu-sim/comfyui_bmab)
**Install Type:** git-clone

---

### ComfyUI_Camera

**Description:**

ComfyUI processes local real-time camera feed and provides real-time preview of the result.

- **Author:** xuhongming251
- **Repository:** [https://github.com/xuhongming251/ComfyUI_Camera](https://github.com/xuhongming251/ComfyUI_Camera)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** ComfyUI_Camera provides real-time camera feed processing but does not directly relate to canny edge detection or image refinement.

### Metadata
**Author:** xuhongming251
**Repository:** [https://github.com/xuhongming251/ComfyUI_Camera](https://github.com/xuhongming251/ComfyUI_Camera)
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

**Reason:** This node provides a front end for experimentation with various elements of Stable Diffusion, including samplers and latent space manipulation, which are essential components in generating images guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node has features related to image editing and processing which could be useful in conjunction with canny edge detection for image generation.

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

**Score:** 90/100

**Reason:** This node provides functionality for custom images which could be used as input for canny edge detection or as an output for the workflow goal.

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

**Score:** 80/100

**Reason:** This node provides functionality for deep learning models which could be used for tasks such as image generation or feature extraction that may be related to canny edge detection.

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

**Score:** 90/100

**Reason:** This node appears to load or generate captions for images, which could be useful in conjunction with canny edge detection for image generation.

### Metadata
**Author:** StartHua
**Repository:** [https://github.com/StartHua/Comfyui_CXH_joy_caption](https://github.com/StartHua/Comfyui_CXH_joy_caption)
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

**Reason:** This node provides a wide range of functionality including smart masking which could be useful for edge detection.

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

**Score:** 90/100

**Reason:** This node is very useful as it enables music source separation using Demucs, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Demucs](https://github.com/smthemex/ComfyUI_Demucs)
**Install Type:** git-clone

---

### ComfyUI_Diffree

**Description:**

using diffree: Text-Guided Shape Free Object Inpainting with Diffusion Model

- **Author:** smthemex
- **Repository:** [https://github.com/smthemex/ComfyUI_Diffree](https://github.com/smthemex/ComfyUI_Diffree)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node uses Diffree for text-guided shape-free object inpainting with a diffusion model, which aligns well with the workflow goal of generating images guided by canny edge detection.

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

**Score:** 100/100

**Reason:** The DSP Image Concat node can help concatenate images, which could be useful for combining edge maps from the canny edge detection process.

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

**Score:** 100/100

**Reason:** The DY Image Masks node could be useful for generating masks from the canny edge detection process, which is essential for image generation workflows.

### Metadata
**Author:** dymokomi
**Repository:** [https://github.com/dymokomi/comfyui_dygen](https://github.com/dymokomi/comfyui_dygen)
**Install Type:** git-clone

---

### ComfyUI_EmojiOverlay

**Description:**

Nodes:Image Emoji Overlay

- **Author:** chandlergis
- **Repository:** [https://github.com/chandlergis/ComfyUI_EmojiOverlay](https://github.com/chandlergis/ComfyUI_EmojiOverlay)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a direct solution for adding emojis as overlays on images which is closely related to the workflow goal of generating images with guided canny edge detection.

### Metadata
**Author:** chandlergis
**Repository:** [https://github.com/chandlergis/ComfyUI_EmojiOverlay](https://github.com/chandlergis/ComfyUI_EmojiOverlay)
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

**Reason:** Although this node provides additional endpoints for ComfyUI API, it does not have a direct relation to canny edge detection or image generation.

### Metadata
**Author:** injet-zhou
**Repository:** [https://github.com/injet-zhou/comfyui_extra_api](https://github.com/injet-zhou/comfyui_extra_api)
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

**Reason:** This node provides face-shaping functionality that aligns with the workflow goal of guided canny edge detection for image generation.

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

**Score:** 91/100

**Reason:** This node offers rotation-aware face extraction and masking options which are directly relevant to the workflow goal.

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

**Reason:** This node performs Fast Fourier Transform and allows users to filter the image, which aligns with the goal of removing grid patterns for canny edge detection.

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

**Reason:** This plugin trains Image Loras on both sd1.5 and SDXL, which is relevant to the workflow goal of generating images.

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

**Score:** 80/100

**Reason:** ComfyUI_FlipStreamViewer provides a viewer interface for flipping images with frame interpolation, making it moderately useful for this workflow goal.

### Metadata
**Author:** sakura1bgx
**Repository:** [https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer](https://github.com/sakura1bgx/ComfyUI_FlipStreamViewer)
**Install Type:** git-clone

---

### Comfyui_Flux_Style_Adjust (Redux)

**Description:**

StyleModelApply adds more controls

- **Author:** yichengup
- **Repository:** [https://github.com/yichengup/Comfyui_Flux_Style_Adjust](https://github.com/yichengup/Comfyui_Flux_Style_Adjust)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides style adjustment controls which could be useful in fine-tuning images generated by a model that uses canny edge detection.

### Metadata
**Author:** yichengup
**Repository:** [https://github.com/yichengup/Comfyui_Flux_Style_Adjust](https://github.com/yichengup/Comfyui_Flux_Style_Adjust)
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

**Score:** 60/100

**Reason:** This node provides a collection of tools that may include image processing capabilities but does not directly relate to canny edge detection.

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

**Score:** 90/100

**Reason:** This node provides frequency separation and recombination methods, which are relevant to image generation and could potentially utilize canny edge detection results.

### Metadata
**Author:** risunobushi
**Repository:** [https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV](https://github.com/risunobushi/comfyUI_FrequencySeparation_RGB-HSV)
**Install Type:** git-clone

---

### ComfyUI_Gemini_Flash

**Description:**

ComfyUI_Gemini_Flash is a custom node for ComfyUI, integrating the capabilities of the Gemini 1.5 Flash model. This node supports text and vision-based prompts, allowing users to analyze and adapt images to text prompts for text2image tasks.

- **Author:** ShmuelRonen
- **Repository:** [https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash](https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is essential for the image generation guided by canny edge detection as it provides a custom integration of the Gemini 1.5 Flash model, supporting text and vision-based prompts.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash](https://github.com/ShmuelRonen/ComfyUI_Gemini_Flash)
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

**Reason:** Image Dimension Resizer and other nodes in this package could be useful for resizing images after applying canny edge detection, making them essential for the workflow.

### Metadata
**Author:** veighnsche
**Repository:** [https://github.com/veighnsche/comfyui_gr85](https://github.com/veighnsche/comfyui_gr85)
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

**Reason:** This node provides direct access to Hugging Face"s hosted inference, which could support the workflow goal but may require additional integration steps.

### Metadata
**Author:** bitaffinity
**Repository:** [https://github.com/bitaffinity/ComfyUI_HF_Inference](https://github.com/bitaffinity/ComfyUI_HF_Inference)
**Install Type:** git-clone

---

### ComfyUI_HuggingFace_Downloader

**Description:**

The ComfyUI HuggingFace Downloader is a custom node extension for ComfyUI, designed to streamline the process of downloading models, checkpoints, and other resources from the Hugging Face Hub directly into your models directory. This tool simplifies workflow integration by providing a seamless interface to select and download required resources.

- **Author:** jnxmx
- **Repository:** [https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader](https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node provides a seamless interface for downloading models and resources from the Hugging Face Hub, which could be essential for integrating canny edge detection into an image generation workflow.

### Metadata
**Author:** jnxmx
**Repository:** [https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader](https://github.com/jnxmx/ComfyUI_HuggingFace_Downloader)
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

**Reason:** This custom node is designed to simplify the use of Hunyuan3D in ComfyUI and is directly relevant to the workflow goal of image generation guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This node provides access to ImageMagick subprocesses which are essential for image processing and canny edge detection.

### Metadata
**Author:** my-opencode
**Repository:** [https://github.com/my-opencode/ComfyUI_IndustrialMagick](https://github.com/my-opencode/ComfyUI_IndustrialMagick)
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

**Reason:** This node enables generating images at resolutions higher than what the model was trained for, which aligns with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** blepping
**Repository:** [https://github.com/blepping/comfyui_jankhidiffusion](https://github.com/blepping/comfyui_jankhidiffusion)
**Install Type:** git-clone

---

### ComfyUI_KimNodes

**Description:**

Image effects, icon layout processing, cropping — this toolbox is a node library organized according to my own needs.

- **Author:** Kim
- **Repository:** [https://github.com/wjl0313/ComfyUI_KimNodes](https://github.com/wjl0313/ComfyUI_KimNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node library contains various image effects and processing tools that could be useful for applying canny edge detection in the workflow.

### Metadata
**Author:** Kim
**Repository:** [https://github.com/wjl0313/ComfyUI_KimNodes](https://github.com/wjl0313/ComfyUI_KimNodes)
**Install Type:** git-clone

---

### comfyui_kmeans_filter

**Description:**

Nodes:Apply Kmeans Filter

- **Author:** githubYiheng
- **Repository:** [https://github.com/githubYiheng/comfyui_kmeans_filter](https://github.com/githubYiheng/comfyui_kmeans_filter)
- **Install Type:** git-clone


### Applicability

**Score:** 70/100

**Reason:** This node applies a K-means filter, which could be useful in preprocessing images before applying canny edge detection and generating the final image.

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

**Reason:** This node provides a Fast Fourier Transform implementation which can be used in conjunction with canny edge detection for image processing.

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

**Score:** 81/100

**Reason:** ComfyUI_Llama3_8B is a direct implementation of Llama3, which can be used for image generation tasks guided by canny edge detection.

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

**Score:** 61/100

**Reason:** ComfyUI_LLaSM provides an interface to the LLaSM model, but its relevance to canny edge detection is indirect and would require additional configuration or nodes to achieve the desired workflow goal.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_LLaSM](https://github.com/leeguandong/ComfyUI_LLaSM)
**Install Type:** git-clone

---

### ComfyUI_llm_easyanimiate

**Description:**

implementation easyanimate with llama3-8b-6bit instruction LLM generation prompt help

- **Author:** FrankChieng
- **Repository:** [https://github.com/frankchieng/ComfyUI_llm_easyanimiate](https://github.com/frankchieng/ComfyUI_llm_easyanimiate)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** ComfyUI_llm_easyanimiate seems to be focused on animation tasks using Llama3-8B, which may not directly relate to canny edge detection for image generation. However, it could potentially serve as a supporting node if the animation task involves edge detection.

### Metadata
**Author:** FrankChieng
**Repository:** [https://github.com/frankchieng/ComfyUI_llm_easyanimiate](https://github.com/frankchieng/ComfyUI_llm_easyanimiate)
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

**Reason:** This node directly implements MagicClothing which can generate images guided by garment and prompt, aligning well with the workflow goal.

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

**Reason:** This node generates memes which could be used as input for image generation guided by canny edge detection, but its primary purpose is unrelated.

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

**Reason:** This node uses memeplex and DALL-E to generate images which directly aligns with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** shi3z
**Repository:** [https://github.com/shi3z/ComfyUI_Memeplex_DALLE](https://github.com/shi3z/ComfyUI_Memeplex_DALLE)
**Install Type:** git-clone

---

### ComfyUI_Mexx_Styler

**Description:**

Nodes: ComfyUI Mexx Styler, ComfyUI Mexx Styler Advanced

- **Author:** SoftMeng
- **Repository:** [https://github.com/SoftMeng/ComfyUI_Mexx_Styler](https://github.com/SoftMeng/ComfyUI_Mexx_Styler)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides advanced styler functionality, which might include image processing operations. However, its direct relevance to canny edge detection and image generation is unclear without further information.

### Metadata
**Author:** SoftMeng
**Repository:** [https://github.com/SoftMeng/ComfyUI_Mexx_Styler](https://github.com/SoftMeng/ComfyUI_Mexx_Styler)
**Install Type:** git-clone

---

### ComfyUI_MileHighStyler

**Description:**

This extension provides various SDXL Prompt Stylers. See: [a/youtube](https://youtu.be/WBHI-2uww7o?si=dijvDaUI4nmx4VkF)

- **Author:** TripleHeadedMonkey
- **Repository:** [https://github.com/TripleHeadedMonkey/ComfyUI_MileHighStyler](https://github.com/TripleHeadedMonkey/ComfyUI_MileHighStyler)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node specifically mentions SDXL Prompt Stylers and has a YouTube link that may explain how it relates to image generation guided by canny edge detection, making it potentially very useful for the workflow goal.

### Metadata
**Author:** TripleHeadedMonkey
**Repository:** [https://github.com/TripleHeadedMonkey/ComfyUI_MileHighStyler](https://github.com/TripleHeadedMonkey/ComfyUI_MileHighStyler)
**Install Type:** git-clone

---

### Comfyui_MiniCPMv2_6-prompt-generator

**Description:**

This is an implementation of [MiniCPMv2_6-prompt-generator](https://huggingface.co/pzc163/MiniCPMv2_6-prompt-generator) by [ComfyUI](https://github.com/comfyanonymous/ComfyUI), including support for single-image caption, generate prompt by upload image and batch-images Prompt generation.

- **Author:** pzc163
- **Repository:** [https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator](https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node supports prompt generation from images and has features that could be useful for generating images guided by canny edge detection.

### Metadata
**Author:** pzc163
**Repository:** [https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator](https://github.com/pzc163/Comfyui_MiniCPMv2_6-prompt-generator)
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

**Reason:** This node uses MS-diffusion for story generation and could be adapted to guide image generation using canny edge detection.

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

**Score:** 81/100

**Reason:** This node allows integration with Nai, which could be useful for generating images based on canny edge detection.

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

**Score:** 100/100

**Reason:** This node directly generates images through NAI, making it essential for the specified workflow goal.

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

**Reason:** This node provides specific nodes (Image Square Adapter Node and Image Resize And Crop Node) that could support the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** sergekatzmann
**Repository:** [https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack](https://github.com/sergekatzmann/ComfyUI_Nimbus-Pack)
**Install Type:** git-clone

---

### comfyUI_Nodes_nicolai256

**Description:**

Nodes: yugioh_Presets. by Nicolai256 inspired by throttlekitty SDXLAspectRatio

- **Author:** nicolai256
- **Repository:** [https://github.com/nicolai256/comfyUI_Nodes_nicolai256](https://github.com/nicolai256/comfyUI_Nodes_nicolai256)
- **Install Type:** copy


### Applicability

**Score:** 40/100

**Reason:** This node contains various presets but does not directly relate to image generation or canny edge detection. However, it might provide some inspiration for custom nodes.

### Metadata
**Author:** nicolai256
**Repository:** [https://github.com/nicolai256/comfyUI_Nodes_nicolai256](https://github.com/nicolai256/comfyUI_Nodes_nicolai256)
**Install Type:** copy

---

### ComfyUI_NoxinNodes

**Description:**

Nodes: Noxin Complete Chime, Noxin Scaled Resolutions, Load from Noxin Prompt Library, Save to Noxin Prompt Library

- **Author:** noxinias
- **Repository:** [https://github.com/noxinias/ComfyUI_NoxinNodes](https://github.com/noxinias/ComfyUI_NoxinNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node includes nodes that could support the workflow goal, such as loading and saving images from a library, which might be useful in conjunction with other nodes for generating images guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node is a wrapper for OmniGen project which can generate images. It has the potential to guide image generation using canny edge detection.

### Metadata
**Author:** chflame163
**Repository:** [https://github.com/chflame163/ComfyUI_OmniGen_Wrapper](https://github.com/chflame163/ComfyUI_OmniGen_Wrapper)
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

**Score:** 40/100

**Reason:** This node is an implementation of Omost which is a regional prompt model. It may have some utility in generating images but it requires additional installation of ComfyUI_densediffusion.

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

**Reason:** This node is directly relevant to generating prompts for image generation tasks.

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

**Reason:** This node provides a direct interface to OOTDiffusion, which can be used for image generation guided by canny edge detection.

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

**Reason:** This node is essential for this workflow as it allows users to generate PBR (Physically Based Rendering) images which can be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node provides a perpendicular CFG that could help reduce oversaturation issues when using high guidance scale values in conjunction with canny edge detection.

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

**Score:** 40/100

**Reason:** While this node is related to image generation, its novel weighting scheme for token vectors from CLIP may not be directly applicable to canny edge detection.

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

**Score:** 100/100

**Reason:** This node provides a direct implementation of Pic2Story, which can be used for image generation guided by canny edge detection.

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

**Reason:** Directly integrates with Mistral Pixtral API to analyze images through deep learning models.

### Metadata
**Author:** ShmuelRonen
**Repository:** [https://github.com/ShmuelRonen/ComfyUI_pixtral_vision](https://github.com/ShmuelRonen/ComfyUI_pixtral_vision)
**Install Type:** git-clone

---

### ComfyUI_pose_inter

**Description:**

Generate transition frames between two character posture images. The prerequisite for running is to have installed comfyui_controlnet_aux, using its Open Pose or DWPose preprocessor

- **Author:** fssorc
- **Repository:** [https://github.com/fssorc/ComfyUI_pose_inter](https://github.com/fssorc/ComfyUI_pose_inter)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Generates transition frames between two character posture images, which could be used as a basis for guided image generation.

### Metadata
**Author:** fssorc
**Repository:** [https://github.com/fssorc/ComfyUI_pose_inter](https://github.com/fssorc/ComfyUI_pose_inter)
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

**Reason:** The PSBlendNode enables blending two images together, which could be useful for combining edge detection results with other image features to guide the image generation process.

### Metadata
**Author:** bluevisor
**Repository:** [https://github.com/bluevisor/ComfyUI_PS_Blend_Node](https://github.com/bluevisor/ComfyUI_PS_Blend_Node)
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

**Reason:** This node implements OpenPose, a computer vision library that detects human poses and can be used for canny edge detection in images.

### Metadata
**Author:** nirex0
**Repository:** [https://github.com/nirex0/ComfyUI_pytorch_openpose](https://github.com/nirex0/ComfyUI_pytorch_openpose)
**Install Type:** git-clone

---

### comfyui_reimgsize

**Description:**

a simple reimgsize node(s) in comfyui.

- **Author:** Makki_Shizu
- **Repository:** [https://github.com/MakkiShizu/comfyui_reimgsize](https://github.com/MakkiShizu/comfyui_reimgsize)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows resizing images which could be a necessary step in preparing input data for canny edge detection.

### Metadata
**Author:** Makki_Shizu
**Repository:** [https://github.com/MakkiShizu/comfyui_reimgsize](https://github.com/MakkiShizu/comfyui_reimgsize)
**Install Type:** git-clone

---

### ComfyUI_RErouter_CustomNodes

**Description:**

Nodes: RErouter, String (RE), Int (RE)

- **Author:** an90ray
- **Repository:** [https://github.com/an90ray/ComfyUI_RErouter_CustomNodes](https://github.com/an90ray/ComfyUI_RErouter_CustomNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides custom nodes that might be useful in routing or processing data but does not directly contribute to image generation guided by canny edge detection.

### Metadata
**Author:** an90ray
**Repository:** [https://github.com/an90ray/ComfyUI_RErouter_CustomNodes](https://github.com/an90ray/ComfyUI_RErouter_CustomNodes)
**Install Type:** git-clone

---

### ComfyUI_RH_OminiControl

**Description:**

ComfyUI_RH_OminiControl is a ComfyUI plugin based on OminiControl By splitting the pipeline load, the plugin efficiently runs on NVIDIA RTX 4090 GPUs. Additionally, the spatial and fill functionalities are generated using the schnell model, reducing the number of sampling steps and improving overall efficiency.

- **Author:** HM-RunningHub
- **Repository:** [https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl](https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node efficiently runs pipelines on NVIDIA RTX 4090 GPUs using OminiControl and snel model for spatial and fill functionalities, making it very useful for image generation guided by canny edge detection.

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

**Score:** 100/100

**Reason:** This node is essential for this workflow goal because it provides a way to get segmentation maps using Sapiens, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_Sapiens](https://github.com/smthemex/ComfyUI_Sapiens)
**Install Type:** git-clone

---

### ComfyUI_Seamless_Patten

**Description:**

It make any text2image create seamless patten

- **Author:** moyi7712
- **Repository:** [https://github.com/moyi7712/ComfyUI_Seamless_Patten](https://github.com/moyi7712/ComfyUI_Seamless_Patten)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node creates seamless patterns using text2image models, which could be useful in conjunction with canny edge detection for generating images with specific textures or effects.

### Metadata
**Author:** moyi7712
**Repository:** [https://github.com/moyi7712/ComfyUI_Seamless_Patten](https://github.com/moyi7712/ComfyUI_Seamless_Patten)
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

**Score:** 90/100

**Reason:** This node is specifically designed for clothes and human segmentation using SegFormer model fine-tuned on ATR dataset which aligns with the workflow goal of image generation guided by canny edge detection.

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

**Reason:** Although this node uses Segment Anything, it primarily focuses on mask cutout rather than direct connection to canny edge detection or image generation.

### Metadata
**Author:** MarkoCa1
**Repository:** [https://github.com/MarkoCa1/ComfyUI_Segment_Mask](https://github.com/MarkoCa1/ComfyUI_Segment_Mask)
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

**Score:** 80/100

**Reason:** This node allows for custom latent ratio creation which could be useful in generating images with specific characteristics that might involve edge detection features.

### Metadata
**Author:** Guillaume-Fgt
**Repository:** [https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio](https://github.com/Guillaume-Fgt/ComfyUI_StableCascadeLatentRatio)
**Install Type:** git-clone

---

### comfyui_stealth_pnginfo

**Description:**

Fork of [a/sd_webui_stealth_pnginfo](https://github.com/ashen-sensored/sd_webui_stealth_pnginfo) with ComfyUI support.

- **Author:** catboxanon
- **Repository:** [https://github.com/catboxanon/comfyui_stealth_pnginfo](https://github.com/catboxanon/comfyui_stealth_pnginfo)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides PNG metadata information but does not directly support the specified workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** catboxanon
**Repository:** [https://github.com/catboxanon/comfyui_stealth_pnginfo](https://github.com/catboxanon/comfyui_stealth_pnginfo)
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

**Reason:** This node uses story-diffusion which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node implements StreamDiffusion which is a pipeline-level solution that could be useful for real-time interactive generation guided by canny edge detection.

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

**Reason:** This node provides string manipulation capabilities which might be useful for preprocessing or post-processing image data, but it is not directly relevant to the workflow goal.

### Metadata
**Author:** wolfden
**Repository:** [https://github.com/wolfden/ComfyUi_String_Function_Tree](https://github.com/wolfden/ComfyUi_String_Function_Tree)
**Install Type:** git-clone

---

### ComfyUI_StringToHex

**Description:**

This is a simple ComfyUI node that will take in a string of 'color' (i.e. 'blue') and output a hex color format.

- **Author:** kudou-reira
- **Repository:** [https://github.com/kasukanra/ComfyUI_StringToHex](https://github.com/kasukanra/ComfyUI_StringToHex)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node converts color strings to hex format, which could be useful in generating images with specific colors based on canny edge detection results.

### Metadata
**Author:** kudou-reira
**Repository:** [https://github.com/kasukanra/ComfyUI_StringToHex](https://github.com/kasukanra/ComfyUI_StringToHex)
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

**Reason:** ComfyUI_Textarea_Loaders is very useful for this workflow as it simplifies the process of generating different characters" pictures by allowing users to input text instead of selecting files, reducing time and effort.

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

**Score:** 80/100

**Reason:** This node provides a T-GATE implementation which could be useful for edge detection in image processing.

### Metadata
**Author:** JettHu
**Repository:** [https://github.com/JettHu/ComfyUI_TGate](https://github.com/JettHu/ComfyUI_TGate)
**Install Type:** git-clone

---

### ComfyUI_TravelSuite

**Description:**

ComfyUI custom nodes to apply various latent travel techniques.

- **Author:** NicholasMcCarthy
- **Repository:** [https://github.com/NicholasMcCarthy/ComfyUI_TravelSuite](https://github.com/NicholasMcCarthy/ComfyUI_TravelSuite)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node applies latent travel techniques which may be useful for generating images but is not specifically related to canny edge detection.

### Metadata
**Author:** NicholasMcCarthy
**Repository:** [https://github.com/NicholasMcCarthy/ComfyUI_TravelSuite](https://github.com/NicholasMcCarthy/ComfyUI_TravelSuite)
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

**Score:** 100/100

**Reason:** TRELLIS is a structured 3D latent model that can generate images and has been used in conjunction with canny edge detection for image generation tasks.

### Metadata
**Author:** smthemex
**Repository:** [https://github.com/smthemex/ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS)
**Install Type:** git-clone

---

### ComfyUI_VisualAttentionMap

**Description:**

NODES:HF ModelLoader, Show Images, Text2Image Inference, Decode Latent, Show CrossAttn Map, Show SelfAttn Map

- **Author:** leeguandong
- **Repository:** [https://github.com/leeguandong/ComfyUI_VisualAttentionMap](https://github.com/leeguandong/ComfyUI_VisualAttentionMap)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is directly related to visual attention maps which are often used in conjunction with canny edge detection for image generation tasks.

### Metadata
**Author:** leeguandong
**Repository:** [https://github.com/leeguandong/ComfyUI_VisualAttentionMap](https://github.com/leeguandong/ComfyUI_VisualAttentionMap)
**Install Type:** git-clone

---

### comfyui_wfc_like

**Description:**

An 'opinionated' Wave Function Collapse implementation with a set of nodes for comfyui

- **Author:** bmad4ever
- **Repository:** [https://github.com/bmad4ever/comfyui_wfc_like](https://github.com/bmad4ever/comfyui_wfc_like)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a Wave Function Collapse implementation which can be used for image generation and may utilize edge detection techniques like canny edge detection.

### Metadata
**Author:** bmad4ever
**Repository:** [https://github.com/bmad4ever/comfyui_wfc_like](https://github.com/bmad4ever/comfyui_wfc_like)
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

**Reason:** This node provides YOLO classifier models which can be used for object detection in images, making it very useful for the specified workflow goal.

### Metadata
**Author:** SuperMasterBlasterLaser
**Repository:** [https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers](https://github.com/SuperMasterBlasterLaser/ComfyUI_YOLO_Classifiers)
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

**Score:** 90/100

**Reason:** This node is specifically designed for Yolo segment mask functionality and has an object mask node that can help with image generation guided by canny edge detection.

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

**Reason:** This node can be used for image processing tasks, potentially useful for edge detection.

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

**Score:** 40/100

**Reason:** This node includes nodes that load and manipulate images, which could be used as supporting nodes in the workflow.

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

**Score:** 81/100

**Reason:** FlexiLoRALoader supports dynamic LoRA weight management which can be useful for image generation guided by canny edge detection.

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

**Reason:** This node allows for visual composition and manipulation of images, which is directly relevant to the goal of generating images guided by canny edge detection.

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

**Reason:** This Consistency Decoder node is very useful for the specified workflow goal as it helps maintain consistency in generated images.

### Metadata
**Author:** shadowcz007
**Repository:** [https://github.com/shadowcz007/comfyui-consistency-decoder](https://github.com/shadowcz007/comfyui-consistency-decoder)
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

**Reason:** This node is a ControlNet implementation which includes LLLiteLoader and is relevant for the specified workflow goal.

### Metadata
**Author:** kohya-ss
**Repository:** [https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)
**Install Type:** git-clone

---

### Core ML Suite for ComfyUI

**Description:**

This extension contains a set of custom nodes for ComfyUI that allow you to use Core ML models in your ComfyUI workflows. The models can be obtained here, or you can convert your own models using coremltools. The main motivation behind using Core ML models in ComfyUI is to allow you to utilize the ANE (Apple Neural Engine) on Apple Silicon (M1/M2) machines to improve performance.

- **Author:** aszc-dev
- **Repository:** [https://github.com/aszc-dev/ComfyUI-CoreMLSuite](https://github.com/aszc-dev/ComfyUI-CoreMLSuite)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** Although this node provides Core ML models, it does not directly relate to canny edge detection or image generation. However, it could be useful as a supporting node for other tasks.

### Metadata
**Author:** aszc-dev
**Repository:** [https://github.com/aszc-dev/ComfyUI-CoreMLSuite](https://github.com/aszc-dev/ComfyUI-CoreMLSuite)
**Install Type:** git-clone

---

### Cozy Human Parser

**Description:**

A ComfyUI node to automatically extract masks for body regions and clothing/fashion items. Made with 💚 by the CozyMantis squad.

- **Author:** CozyMantis
- **Repository:** [https://github.com/cozymantis/human-parser-comfyui-node](https://github.com/cozymantis/human-parser-comfyui-node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it provides automatic extraction of masks for body regions and clothing/fashion items, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** CozyMantis
**Repository:** [https://github.com/cozymantis/human-parser-comfyui-node](https://github.com/cozymantis/human-parser-comfyui-node)
**Install Type:** git-clone

---

### Cozy Reference Pose Generator

**Description:**

Generate OpenPose face/body reference poses in ComfyUI with ease. Made with 💚 by the CozyMantis squad.

- **Author:** CozyMantis
- **Repository:** [https://github.com/cozymantis/pose-generator-comfyui-node](https://github.com/cozymantis/pose-generator-comfyui-node)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node could be moderately useful as a supporting node for generating reference poses, but it does not directly contribute to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** CozyMantis
**Repository:** [https://github.com/cozymantis/pose-generator-comfyui-node](https://github.com/cozymantis/pose-generator-comfyui-node)
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

**Score:** 40/100

**Reason:** This node has some utility nodes that could be useful in the workflow, but none directly relate to canny edge detection or image generation. It provides better nodes for loading and saving images, which might be useful in a broader sense.

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

**Score:** 80/100

**Reason:** This node could be useful in scaling or rotating an image after applying canny edge detection.

### Metadata
**Author:** claussteinmassl
**Repository:** [https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes](https://github.com/claussteinmassl/ComfyUI-CS-CustomNodes)
**Install Type:** git-clone

---

### D2 Send Eagle

**Description:**

Send images generated by ComfyUI to Eagle image management software

- **Author:** da2el-ai
- **Repository:** [https://github.com/da2el-ai/ComfyUI-d2-send-eagle](https://github.com/da2el-ai/ComfyUI-d2-send-eagle)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is essential for this workflow as it sends images generated by ComfyUI to Eagle image management software, which aligns with the goal of guided image generation and canny edge detection.

### Metadata
**Author:** da2el-ai
**Repository:** [https://github.com/da2el-ai/ComfyUI-d2-send-eagle](https://github.com/da2el-ai/ComfyUI-d2-send-eagle)
**Install Type:** git-clone

---

### D2 Size Selector

**Description:**

This is a custom node that allows you to easily call up and set image size presets. Settings can be made by editing the included config.yaml. It is almost identical to Comfyroll Studio's CR AspectRatio. I created it because I wanted to easily edit the presets.

- **Author:** da2el-ai
- **Repository:** [https://github.com/da2el-ai/ComfyUI-d2-size-selector](https://github.com/da2el-ai/ComfyUI-d2-size-selector)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows setting image size presets but does not directly relate to canny edge detection or image generation; however, it could be useful as a supporting node for adjusting image sizes.

### Metadata
**Author:** da2el-ai
**Repository:** [https://github.com/da2el-ai/ComfyUI-d2-size-selector](https://github.com/da2el-ai/ComfyUI-d2-size-selector)
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

**Reason:** DarkPrompts offers improved random prompt generation tools that could be useful in generating images guided by canny edge detection.

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

**Score:** 95/100

**Reason:** Dashscope FLUX API provides superior image generation capabilities and optimized support for Chinese prompts, making it highly relevant to the workflow goal.

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

**Reason:** Deforum Nodes are highly relevant as they provide a unique way to create frame-by-frame generative motion art, which aligns with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** deforum
**Repository:** [https://github.com/XmYx/deforum-comfy-nodes](https://github.com/XmYx/deforum-comfy-nodes)
**Install Type:** git-clone

---

### Den_ComfyUI_Workflows

**Description:**

Custom nodes make easy Advanced Workflows. Focus on Image/Video and ControlNet efficiency and performances. Manipulation of Latent Space, Automatic pipeline with a bit efforts.

- **Author:** denfrost
- **Repository:** [https://github.com/denfrost/Den_ComfyUI_Workflow](https://github.com/denfrost/Den_ComfyUI_Workflow)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Den_ComfyUI_Workflows are marginally relevant as they focus on image/video manipulation and controlnet efficiency, but their primary emphasis is not on canny edge detection.

### Metadata
**Author:** denfrost
**Repository:** [https://github.com/denfrost/Den_ComfyUI_Workflow](https://github.com/denfrost/Den_ComfyUI_Workflow)
**Install Type:** git-clone

---

### DiffSynth-ComfyUI

**Description:**

a custom node for [a/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/DiffSynth-ComfyUI](https://github.com/AIFSH/DiffSynth-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node directly supports the workflow goal by providing a custom interface for DiffSynth-Studio, which can be used for image generation guided by canny edge detection.

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

**Reason:** This node is a collection of custom nodes that allow using most Diffusers pipelines and components in Comfy, which includes canny edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node seems highly relevant as it uses diffusion models for generating images and might be able to incorporate edge detection techniques.

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

**Score:** 70/100

**Reason:** This node is moderately relevant as it generates Perlin noise in the latent space, which could be used for guiding image generation, but may require additional processing steps for canny edge detection.

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

**Score:** 100/100

**Reason:** This node provides a modularized version of Disco Diffusion, which is directly relevant to the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** space-nuko
**Repository:** [https://github.com/space-nuko/ComfyUI-Disco-Diffusion](https://github.com/space-nuko/ComfyUI-Disco-Diffusion)
**Install Type:** git-clone

---

### Dynamic Thresholding

**Description:**

Adds nodes for Dynamic Thresholding, CFG scheduling, and related techniques.

- **Author:** mcmonkeyprojects
- **Repository:** [https://github.com/mcmonkeyprojects/sd-dynamic-thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Dynamic Thresholding nodes would be very useful for implementing dynamic thresholding techniques that could guide the canny edge detection process in image generation workflows.

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

**Score:** 90/100

**Reason:** This node appears to provide a comprehensive solution for pose estimation and dynamic sampling, which could be useful for guiding image generation with canny edge detection.

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

**Score:** 80/100

**Reason:** This custom nodes library seems to enable the use of dynamic prompts in ComfyUI, which could be helpful for generating images guided by canny edge detection.

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

**Score:** 60/100

**Reason:** This node is related to face detailer and mask creation using Mediapipe and YOLOv8n, but it may not directly contribute to image generation guided by canny edge detection.

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

**Reason:** This node is very useful for the specified workflow goal as it provides a simple and easy-to-use way to create square image crops and masks using YoloV8, which can be used in conjunction with controlnet and ip adapters.

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

**Reason:** This node is moderately useful for the specified workflow goal as it provides a way to capture window content from other programs, but it does not directly relate to canny edge detection or image generation.

### Metadata
**Author:** zhuanqianfish
**Repository:** [https://github.com/zhuanqianfish/ComfyUI-EasyNode](https://github.com/zhuanqianfish/ComfyUI-EasyNode)
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

**Reason:** This node is a trainer that could potentially be used to train models for image generation with canny edge detection, making it very useful.

### Metadata
**Author:** aiXander
**Repository:** [https://github.com/edenartlab/eden_comfy_pipelines](https://github.com/edenartlab/eden_comfy_pipelines)
**Install Type:** git-clone

---

### Efficiency Nodes ExtendeD

**Description:**

Expansion of Efficiency Nodes for ComfyUI. Significant UX improvements.[w/NOTE: This node requires [a/Efficiency Nodes for ComfyUI Version 2.0+](https://github.com/jags111/efficiency-nodes-comfyui) and [a/ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts). Also, this node makes changes to user.css.]

- **Author:** NyaamZ
- **Repository:** [https://github.com/NyaamZ/efficiency-nodes-ED](https://github.com/NyaamZ/efficiency-nodes-ED)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** As part of the Eden.art nodesuite, this node likely contains custom nodes that could support image generation guided by canny edge detection, making it highly relevant and useful.

### Metadata
**Author:** NyaamZ
**Repository:** [https://github.com/NyaamZ/efficiency-nodes-ED](https://github.com/NyaamZ/efficiency-nodes-ED)
**Install Type:** git-clone

---

### Embedding Merge for ComfyUI

**Description:**

Extremely inspired and forked from: [a/https://github.com/klimaleksus/stable-diffusion-webui-embedding-merge](https://github.com/klimaleksus/stable-diffusion-webui-embedding-merge)

- **Author:** duskfallcrew
- **Repository:** [https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node](https://github.com/duskfallcrew/Comfyui_EmbeddingMerge_Node)
- **Install Type:** copy


### Applicability

**Score:** 100/100

**Reason:** This Embedding Merge node is highly relevant as it allows for the combination of multiple embeddings, potentially including those used in canny edge detection.

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

**Reason:** Although the Embedding Picker is useful for managing embeddings, its direct relevance to image generation guided by canny edge detection is limited, as it doesn"t directly contribute to the process of using canny edge detection in image generation.

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

**Reason:** This node pack includes various numerical and text inputs that could be useful for preprocessing or post-processing in an image generation workflow guided by canny edge detection.

### Metadata
**Author:** BiffMunky
**Repository:** [https://github.com/tusharbhutt/Endless-Nodes](https://github.com/tusharbhutt/Endless-Nodes)
**Install Type:** git-clone

---

### Extended Image Formats for ComfyUI

**Description:**

Adds a custom node for saving images in webp, jpeg, avif, jxl (no metadata) and supports loading workflows from saved images

- **Author:** kaanyalova
- **Repository:** [https://github.com/kaanyalova/ComfyUI_ExtendedImageFormats](https://github.com/kaanyalova/ComfyUI_ExtendedImageFormats)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node adds support for various image formats which could be useful for saving or loading images in the workflow, making it moderately useful.

### Metadata
**Author:** kaanyalova
**Repository:** [https://github.com/kaanyalova/ComfyUI_ExtendedImageFormats](https://github.com/kaanyalova/ComfyUI_ExtendedImageFormats)
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

**Reason:** This node is essential for the specified workflow goal as it provides custom functionality for F5-TTS, which may be used in conjunction with canny edge detection.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/F5-TTS-ComfyUI](https://github.com/AIFSH/F5-TTS-ComfyUI)
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

**Score:** 80/100

**Reason:** This node is very useful for image generation guided by canny edge detection as it allows face restoration, which could be a crucial step in creating realistic images.

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

**Reason:** This node is very useful as it provides a set of custom nodes that can potentially include one for canny edge detection.

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

**Score:** 100/100

**Reason:** This node provides a custom module for generating loras at different strengths, which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** fitCorder
**Repository:** [https://github.com/fitCorder/fcSuite](https://github.com/fitCorder/fcSuite)
**Install Type:** copy

---

### florence_dw

**Description:**

Based on the original repository [a/https://github.com/spacepxl/ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2), the model loading and storage methods have been improved, and sd3 has been newly added with enhanced speed and accuracy.

- **Author:** yiwangsimple
- **Repository:** [https://github.com/yiwangsimple/florence_dw](https://github.com/yiwangsimple/florence_dw)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** florence_dw provides model loading and storage methods which could be useful for generating images with canny edge detection.

### Metadata
**Author:** yiwangsimple
**Repository:** [https://github.com/yiwangsimple/florence_dw](https://github.com/yiwangsimple/florence_dw)
**Install Type:** git-clone

---

### Flow - Streamlined Way to ComfyUI

**Description:**

Flow is a custom node designed to provide a more user-friendly interface for ComfyUI by acting as an alternative user interface for running workflows. It is not a replacement for workflow creation.
Flow is currently in the early stages of development, so expect bugs and ongoing feature enhancements. With your support and feedback, Flow will settle into a steady stream.

- **Author:** diSty
- **Repository:** [https://github.com/diStyApps/ComfyUI-disty-Flow](https://github.com/diStyApps/ComfyUI-disty-Flow)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Flow is a custom node that aims to provide a user-friendly interface but does not directly contribute to image generation guided by canny edge detection.

### Metadata
**Author:** diSty
**Repository:** [https://github.com/diStyApps/ComfyUI-disty-Flow](https://github.com/diStyApps/ComfyUI-disty-Flow)
**Install Type:** git-clone

---

### Flux Prompt Generator for ComfyUI

**Description:**

A flexible and customizable prompt generator for generating detailed and creative prompts for image generation models for ComfyUI

- **Author:** fairy-root
- **Repository:** [https://github.com/fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides a flexible and customizable prompt generator that can generate detailed and creative prompts for image generation models, which aligns well with the specified workflow goal.

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

**Score:** 61/100

**Reason:** This node converts negative prompts into positive ones, which could be useful for workflows that require generating images based on complex prompt specifications, including those involving canny edge detection.

### Metadata
**Author:** NeuralSamurAI
**Repository:** [https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt](https://github.com/NeuralSamurAI/ComfyUI-FluxPseudoNegativePrompt)
**Install Type:** git-clone

---

### for comfyui image proprocessor

**Description:**

Adapt for Hunyuan now
NOTE: The files in the repo are not organized, which may lead to update issues.

- **Author:** TTPlanetPig
- **Repository:** [https://github.com/TTPlanetPig/Comfyui_TTP_CN_Preprocessor](https://github.com/TTPlanetPig/Comfyui_TTP_CN_Preprocessor)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** for comfyui image proprocessor is relevant as it involves image processing and could potentially incorporate canny edge detection for guiding image generation.

### Metadata
**Author:** TTPlanetPig
**Repository:** [https://github.com/TTPlanetPig/Comfyui_TTP_CN_Preprocessor](https://github.com/TTPlanetPig/Comfyui_TTP_CN_Preprocessor)
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

**Reason:** The node adds a gallery to load images but does not directly contribute to canny edge detection.

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

**Reason:** This node integrates Gemini API and Ollama into ComfyUI, which can be used for generating images based on canny edge detection.

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

**Reason:** This custom node provides advanced background removal capabilities which could be useful for preprocessing images before applying canny edge detection.

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

**Reason:** This collection of nodes supports GLSL shaders which might be useful for post-processing images after applying canny edge detection but does not directly contribute to the goal.

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

**Score:** 100/100

**Reason:** This node is essential for preventing GPU overheating during image generation tasks.

### Metadata
**Author:** meap158
**Repository:** [https://github.com/meap158/ComfyUI-GPU-temperature-protection](https://github.com/meap158/ComfyUI-GPU-temperature-protection)
**Install Type:** git-clone

---

### Hayo comfyui nodes

**Description:**

Nodes:tensor_trans_pil, Make Transparent mask, MergeImages, words_generatee, load_PIL image

- **Author:** LZC
- **Repository:** [https://github.com/1shadow1/hayo_comfyui_nodes](https://github.com/1shadow1/hayo_comfyui_nodes)
- **Install Type:** copy


### Applicability

**Score:** 70/100

**Reason:** This node contains several nodes that could be useful for image processing tasks related to the workflow goal, such as loading and merging images.

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

**Reason:** This node includes HD SmoothEdge, which is directly relevant to canny edge detection, making it essential for this workflow.

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

**Score:** 90/100

**Reason:** This node is very useful for downloading models from huggingface which can be used in image generation workflows.

### Metadata
**Author:** icesun963
**Repository:** [https://github.com/icesun963/ComfyUI_HFDownLoad](https://github.com/icesun963/ComfyUI_HFDownLoad)
**Install Type:** git-clone

---

### Huggingface Api Serverless

**Description:**

Huggingface Api Serverless request

- **Author:** Alex Genovese
- **Repository:** [https://github.com/alexgenovese/ComfyUI_HF_Servelress_Inference](https://github.com/alexgenovese/ComfyUI_HF_Servelress_Inference)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows for Hugging Face API requests but is not specifically designed for canny edge detection or image generation.

### Metadata
**Author:** Alex Genovese
**Repository:** [https://github.com/alexgenovese/ComfyUI_HF_Servelress_Inference](https://github.com/alexgenovese/ComfyUI_HF_Servelress_Inference)
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

**Reason:** This node detects human parts using a DeepLabV3+ ResNet50 model which could be used in conjunction with canny edge detection to generate images of humans.

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

**Score:** 90/100

**Reason:** This node appears to be highly relevant for the specified workflow goal as it includes models specifically designed for image generation tasks like IC-Light and Photon_v1.

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

**Reason:** This node allows for user selection of images which is a crucial step in the workflow goal.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-image-picker](https://github.com/chrisgoringe/cg-image-picker)
**Install Type:** git-clone

---

### Image loader with subfolders

**Description:**

Adds an Image Loader node that also shows images in subfolders of the default input directory

- **Author:** catscandrive
- **Repository:** [https://github.com/catscandrive/comfyui-imagesubfolders](https://github.com/catscandrive/comfyui-imagesubfolders)
- **Install Type:** copy


### Applicability

**Score:** 81/100

**Reason:** Directly loads images from subfolders, matching the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** catscandrive
**Repository:** [https://github.com/catscandrive/comfyui-imagesubfolders](https://github.com/catscandrive/comfyui-imagesubfolders)
**Install Type:** copy

---

### Image Metadata Nodes

**Description:**

Nodes for loading and saving images with metadata in ComfyUI.

- **Author:** Light-x02
- **Repository:** [https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes](https://github.com/Light-x02/ComfyUI-Image-Metadata-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Provides metadata functionality, which could be useful for storing or retrieving data related to the generated images, but is not directly relevant to the workflow goal.

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

**Score:** 100/100

**Reason:** Contains specialized image processing nodes that likely include canny edge detection, making it essential for achieving the workflow goal.

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

**Score:** 61/100

**Reason:** Provides tools for resizing images without distorting proportions, which is a supporting task in the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** palant
**Repository:** [https://github.com/palant/image-resize-comfyui](https://github.com/palant/image-resize-comfyui)
**Install Type:** git-clone

---

### Image to Text Node

**Description:**

Nodes: Image URL to Text, Image to Text.

- **Author:** yolanother
- **Repository:** [https://github.com/yolanother/DTAIImageToTextNode](https://github.com/yolanother/DTAIImageToTextNode)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node can be used to generate text from images, which could be a useful input for an image generation workflow.

### Metadata
**Author:** yolanother
**Repository:** [https://github.com/yolanother/DTAIImageToTextNode](https://github.com/yolanother/DTAIImageToTextNode)
**Install Type:** git-clone

---

### image-caption-comfyui

**Description:**

Using image caption models to extract prompts in ComfyUI

- **Author:** alpertunga-bile
- **Repository:** [https://github.com/alpertunga-bile/image-caption-comfyui](https://github.com/alpertunga-bile/image-caption-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can be used to extract prompts from images, which could potentially be used in an image generation workflow, but its direct relevance is limited.

### Metadata
**Author:** alpertunga-bile
**Repository:** [https://github.com/alpertunga-bile/image-caption-comfyui](https://github.com/alpertunga-bile/image-caption-comfyui)
**Install Type:** git-clone

---

### Image2Halftone Node for ComfyUI

**Description:**

This is a node to convert an image into a CMYK Halftone dot image.

- **Author:** aimingfail
- **Repository:** [https://civitai.com/models/143293/image2halftone-node-for-comfyui](https://civitai.com/models/143293/image2halftone-node-for-comfyui)
- **Install Type:** unzip


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant as it converts an image into a CMYK Halftone dot image but does not utilize canny edge detection for guidance.

### Metadata
**Author:** aimingfail
**Repository:** [https://civitai.com/models/143293/image2halftone-node-for-comfyui](https://civitai.com/models/143293/image2halftone-node-for-comfyui)
**Install Type:** unzip

---

### ImageProcessing

**Description:**

ComfyUI custom nodes to apply various image processing techniques.

- **Author:** bvhari
- **Repository:** [https://github.com/bvhari/ComfyUI_ImageProcessing](https://github.com/bvhari/ComfyUI_ImageProcessing)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a broad range of image processing techniques that could be used in conjunction with canny edge detection for image generation.

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

**Reason:** A grid viewer might be useful for displaying multiple images generated using canny edge detection, but it does not directly contribute to the generation process.

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

**Reason:** This node can extract colors from an image which could be useful for guiding the image generation process based on color information.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/img2colors-comfyui-node](https://github.com/christian-byrne/img2colors-comfyui-node)
**Install Type:** git-clone

---

### img2txt-comfyui-nodes

**Description:**

Get general description or specify questions to ask about images (medium, art style, background, etc.). Supports Chinese 🇨🇳 questions via MiniCPM model.

- **Author:** christian-byrne
- **Repository:** [https://github.com/christian-byrne/img2txt-comfyui-nodes](https://github.com/christian-byrne/img2txt-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node can provide a general description of an image but it may not directly contribute to canny edge detection or image generation.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/img2txt-comfyui-nodes](https://github.com/christian-byrne/img2txt-comfyui-nodes)
**Install Type:** git-clone

---

### Info Utils

**Description:**

Nodes that facilitate simpler information providing and gathering, such as Text Box, Show Data and Token Counter nodes.

- **Author:** exectails
- **Repository:** [https://github.com/exectails/comfyui-et_infoutils](https://github.com/exectails/comfyui-et_infoutils)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides various information-gathering and display nodes that could be useful for providing feedback on the image generation process.

### Metadata
**Author:** exectails
**Repository:** [https://github.com/exectails/comfyui-et_infoutils](https://github.com/exectails/comfyui-et_infoutils)
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

**Reason:** Node provides miscellaneous nodes that might be useful in a general sense but do not directly support the workflow goal.

### Metadata
**Author:** jefferyharrell
**Repository:** [https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes](https://github.com/ComfyUI-JH/ComfyUI-JH-Misc-Nodes)
**Install Type:** git-clone

---

### Jovi_GLSL

**Description:**

Integrates GLSL shader support.

- **Author:** amorano
- **Repository:** [https://github.com/Amorano/Jovi_GLSL](https://github.com/Amorano/Jovi_GLSL)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node integrates GLSL shader support which could be used for complex image processing tasks including edge detection.

### Metadata
**Author:** amorano
**Repository:** [https://github.com/Amorano/Jovi_GLSL](https://github.com/Amorano/Jovi_GLSL)
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

**Reason:** This node provides image metrics nodes that could be useful in evaluating the output of canny edge detection or other image processing tasks.

### Metadata
**Author:** amorano
**Repository:** [https://github.com/Amorano/Jovi_Measure](https://github.com/Amorano/Jovi_Measure)
**Install Type:** git-clone

---

### Jurdns Groq API Node

**Description:**

This node utilizes the Groq.com API to enhance prompts. (Place API key and main system prompt in the groq_config.json)

- **Author:** Jurdn
- **Repository:** [https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node](https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node enhances prompts using the Groq.com API which could be useful for generating images guided by canny edge detection.

### Metadata
**Author:** Jurdn
**Repository:** [https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node](https://github.com/jurdnisglobby/ComfyUI-Jurdns-Groq-Node)
**Install Type:** git-clone

---

### kb-comfyui-nodes

**Description:**

Nodes:SingleImageDataUrlLoader

- **Author:** smagnetize
- **Repository:** [https://github.com/smagnetize/kb-comfyui-nodes](https://github.com/smagnetize/kb-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows loading single images from data URLs, which could be useful for feeding into an image generation workflow.

### Metadata
**Author:** smagnetize
**Repository:** [https://github.com/smagnetize/kb-comfyui-nodes](https://github.com/smagnetize/kb-comfyui-nodes)
**Install Type:** git-clone

---

### Knodes

**Description:**

Nodes: Image(s) To Websocket (Base64), Load Image (Base64),Load Images (Base64)

- **Author:** kft334
- **Repository:** [https://github.com/kft334/Knodes](https://github.com/kft334/Knodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides functionality for loading and sending images over websocket, which could be useful in conjunction with canny edge detection for real-time image processing.

### Metadata
**Author:** kft334
**Repository:** [https://github.com/kft334/Knodes](https://github.com/kft334/Knodes)
**Install Type:** git-clone

---

### KSampler GPU

**Description:**

KSampler is provided, based on GPU random noise

- **Author:** dawangraoming
- **Repository:** [https://github.com/dawangraoming/ComfyUI_ksampler_gpu](https://github.com/dawangraoming/ComfyUI_ksampler_gpu)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** This node generates random noise which could be used as input for image generation guided by canny edge detection.

### Metadata
**Author:** dawangraoming
**Repository:** [https://github.com/dawangraoming/ComfyUI_ksampler_gpu](https://github.com/dawangraoming/ComfyUI_ksampler_gpu)
**Install Type:** copy

---

### Latent Mirror node for ComfyUI

**Description:**

Nodes: Latent Mirror. Node to mirror a latent along the Y (vertical / left to right) or X (horizontal / top to bottom) axis.

- **Author:** spro
- **Repository:** [https://github.com/spro/comfyui-mirror](https://github.com/spro/comfyui-mirror)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** The Latent Mirror node can mirror a latent along the Y or X axis, which could be useful for analyzing and manipulating the output of the canny edge detection process.

### Metadata
**Author:** spro
**Repository:** [https://github.com/spro/comfyui-mirror](https://github.com/spro/comfyui-mirror)
**Install Type:** git-clone

---

### Lazy Pony Prompter

**Description:**

A booru API powered prompt generator for A1111 and ComfyUI with flexible tag filtering system and customizable prompt templates.

- **Author:** Siberpone
- **Repository:** [https://github.com/Siberpone/lazy-pony-prompter](https://github.com/Siberpone/lazy-pony-prompter)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node generates prompts using a booru API, which could be useful for guiding image generation with specific tags and templates.

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

**Score:** 95/100

**Reason:** This node provides custom inpainting/outpainting functionality using LCM, directly related to the workflow goal of canny edge detection.

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

**Score:** 60/100

**Reason:** This node offers various custom features including history and logic switches which could support the workflow, although it does not directly address canny edge detection.

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

**Score:** 80/100

**Reason:** This node provides several image processing nodes that are directly relevant to the workflow goal, such as converting images to gray scale, which is a common step in canny edge detection.

### Metadata
**Author:** ai-liam
**Repository:** [https://github.com/ai-liam/comfyui-liam](https://github.com/ai-liam/comfyui-liam)
**Install Type:** git-clone

---

### LiquidTime - by PabloGFX

**Description:**

LiquidTime is a simple yet powerful frame interpolation node for ComfyUI. Just input your sequence and desired frame count - the node handles all complex calculations and generates smooth in-between frames for you. A must-have tool for AI animation and video creation that lets you shape time like liquid.

- **Author:** PabloGFX
- **Repository:** [https://github.com/lazniak/LiquidTime-Interpolation](https://github.com/lazniak/LiquidTime-Interpolation)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** LiquidTime is a frame interpolation node that could be useful for creating intermediate frames in the image generation process guided by canny edge detection.

### Metadata
**Author:** PabloGFX
**Repository:** [https://github.com/lazniak/LiquidTime-Interpolation](https://github.com/lazniak/LiquidTime-Interpolation)
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

**Reason:** This node is very useful as it loads an image from a base64-encoded data URI, which could be used to input the output of canny edge detection into the workflow.

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

**Reason:** This custom logo generator node uses Google Fonts and could potentially be used in conjunction with canny edge detection for image generation.

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

**Score:** 95/100

**Reason:** This node suite harnesses the power of LLMs to improve image generation quality, which aligns closely with the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** ParisNeo
**Repository:** [https://github.com/ParisNeo/lollms_nodes_suite](https://github.com/ParisNeo/lollms_nodes_suite)
**Install Type:** git-clone

---

### LoraInfo

**Description:**

Shows Lora information from CivitAI and outputs trigger words and example prompt

- **Author:** jitcoder
- **Repository:** [https://github.com/jitcoder/lora-info](https://github.com/jitcoder/lora-info)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node shows Lora information and outputs trigger words and example prompts which might be useful for generating images but is not directly related to canny edge detection.

### Metadata
**Author:** jitcoder
**Repository:** [https://github.com/jitcoder/lora-info](https://github.com/jitcoder/lora-info)
**Install Type:** git-clone

---

### mape's helpers

**Description:**

Multi-monitor image preview, Variable Assigment/Wireless Nodes, Prompt Tweaking, Command Palette, Pinned favourite nodes, Node navigation, Fuzzy search, Node time tracking, Organizing and Error management. For more info visit: [a/https://comfyui.ma.pe/](https://comfyui.ma.pe/)

- **Author:** mape
- **Repository:** [https://github.com/mape/ComfyUI-mape-Helpers](https://github.com/mape/ComfyUI-mape-Helpers)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** While this node offers various workflow settings and management tools, it is not directly relevant to image generation or canny edge detection.

### Metadata
**Author:** mape
**Repository:** [https://github.com/mape/ComfyUI-mape-Helpers](https://github.com/mape/ComfyUI-mape-Helpers)
**Install Type:** git-clone

---

### MBM's Music Visualizer

**Description:**

An image generation based music visualizer integrated into comfyanonymous/ComfyUI as custom nodes.

- **Author:** Sorcerio
- **Repository:** [https://github.com/Sorcerio/MBM-Music-Visualizer](https://github.com/Sorcerio/MBM-Music-Visualizer)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This music visualizer can generate images based on audio input, which could potentially utilize canny edge detection or similar techniques for image generation.

### Metadata
**Author:** Sorcerio
**Repository:** [https://github.com/Sorcerio/MBM-Music-Visualizer](https://github.com/Sorcerio/MBM-Music-Visualizer)
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

**Reason:** This node might be useful in a supporting role, but its primary function of weighted block merging does not directly relate to the workflow goal.

### Metadata
**Author:** YinBailiang
**Repository:** [https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI](https://github.com/YinBailiang/MergeBlockWeighted_fo_ComfyUI)
**Install Type:** git-clone

---

### Mflux-ComfyUI

**Description:**

Simple use of [a/Mflux](https://github.com/filipstrand/mflux) in ComfyUI, suitable for users who are not familiar with terminal usage.
NOTE: A MLX port of FLUX based on the Huggingface Diffusers implementation.

- **Author:** raysers
- **Repository:** [https://github.com/raysers/Mflux-ComfyUI](https://github.com/raysers/Mflux-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a simple interface to Mflux, but its direct relevance to canny edge detection is unclear.

### Metadata
**Author:** raysers
**Repository:** [https://github.com/raysers/Mflux-ComfyUI](https://github.com/raysers/Mflux-ComfyUI)
**Install Type:** git-clone

---

### mihaiiancu/Inpaint

**Description:**

Nodes: InpaintMediapipe. This node provides a simple interface to inpaint.

- **Author:** mihaiiancu
- **Repository:** [https://github.com/mihaiiancu/ComfyUI_Inpaint](https://github.com/mihaiiancu/ComfyUI_Inpaint)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node directly supports inpainting, which can be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** mihaiiancu
**Repository:** [https://github.com/mihaiiancu/ComfyUI_Inpaint](https://github.com/mihaiiancu/ComfyUI_Inpaint)
**Install Type:** git-clone

---

### MLTask_ComfyUI

**Description:**

a set of nodes to help u run ai code using MLTask

- **Author:** mltask
- **Repository:** [https://github.com/misterjoessef/MLTask_ComfyUI](https://github.com/misterjoessef/MLTask_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a general-purpose framework for running AI code but lacks specific features for canny edge detection.

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

**Score:** 80/100

**Reason:** This node provides functionality related to mask images which could be useful in conjunction with canny edge detection for image generation tasks.

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

**Reason:** This node is essential for loading models that support NF4 and FP4 formats, which are crucial for the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** silveroxides
**Repository:** [https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders](https://github.com/silveroxides/ComfyUI_bnb_nf4_fp4_Loaders)
**Install Type:** git-clone

---

### Mosaica

**Description:**

Create colorful mosaic images in ComfyUI by computing label images and applying lookup tables.

- **Author:** Mason-McGough
- **Repository:** [https://github.com/Mason-McGough/ComfyUI-Mosaica](https://github.com/Mason-McGough/ComfyUI-Mosaica)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node creates colorful mosaic images but does not directly relate to canny edge detection; however, it could be useful as a supporting node in the workflow.

### Metadata
**Author:** Mason-McGough
**Repository:** [https://github.com/Mason-McGough/ComfyUI-Mosaica](https://github.com/Mason-McGough/ComfyUI-Mosaica)
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

**Reason:** This node contains various image processing nodes, some of which might be marginally relevant to the workflow goal, but none are directly related or essential.

### Metadata
**Author:** melMass
**Repository:** [https://github.com/melMass/comfy_mtb](https://github.com/melMass/comfy_mtb)
**Install Type:** git-clone

---

### Node - Size Matcher

**Description:**

Match image/mask sizes

- **Author:** christian-byrne
- **Repository:** [https://github.com/christian-byrne/size-match-compositing-nodes](https://github.com/christian-byrne/size-match-compositing-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node matches image/mask sizes which is essential for applying canny edge detection and generating images based on it.

### Metadata
**Author:** christian-byrne
**Repository:** [https://github.com/christian-byrne/size-match-compositing-nodes](https://github.com/christian-byrne/size-match-compositing-nodes)
**Install Type:** git-clone

---

### Nodes for use with real-time applications of ComfyUI

**Description:**

These nodes are for real-time applications of ComfyUI.

- **Author:** RyanOnTheInside
- **Repository:** [https://github.com/ryanontheinside/ComfyUI_RealTimeNodes](https://github.com/ryanontheinside/ComfyUI_RealTimeNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Nodes for real-time applications of ComfyUI might have some relevance due to their focus on performance, but it"s unclear how they would be directly applied to the workflow goal.

### Metadata
**Author:** RyanOnTheInside
**Repository:** [https://github.com/ryanontheinside/ComfyUI_RealTimeNodes](https://github.com/ryanontheinside/ComfyUI_RealTimeNodes)
**Install Type:** git-clone

---

### noEmbryo nodes

**Description:**

PromptTermList (1-6): are some nodes that help with the creation of Prompts inside ComfyUI. Resolution Scale outputs image dimensions using a scale factor. Regex Text Chopper outputs the chopped parts of a text using RegEx.

- **Author:** noEmbryo
- **Repository:** [https://github.com/noembryo/ComfyUI-noEmbryo](https://github.com/noembryo/ComfyUI-noEmbryo)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** noEmbryo nodes seem moderately useful as they provide tools for creating prompts and manipulating image dimensions, which could be indirectly related to guiding canny edge detection in image generation.

### Metadata
**Author:** noEmbryo
**Repository:** [https://github.com/noembryo/ComfyUI-noEmbryo](https://github.com/noembryo/ComfyUI-noEmbryo)
**Install Type:** git-clone

---

### NSFW Check for ComfyUI

**Description:**

This project is designed to detect whether images generated by ComfyUI are Not Safe For Work (NSFW). It uses a machine learning model to classify images as either safe or not safe for work and returns a confidence score for the NSFW classification.

- **Author:** iamandeepsandhu
- **Repository:** [https://github.com/iamandeepsandhu/ComfyUI-NSFW-Check](https://github.com/iamandeepsandhu/ComfyUI-NSFW-Check)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node directly checks if generated images are NSFW, which could be a requirement for the workflow goal.

### Metadata
**Author:** iamandeepsandhu
**Repository:** [https://github.com/iamandeepsandhu/ComfyUI-NSFW-Check](https://github.com/iamandeepsandhu/ComfyUI-NSFW-Check)
**Install Type:** git-clone

---

### nsfw-image-check-comfyui

**Description:**

NODES:Nsfw Image Check Node

- **Author:** fallingmeteorite
- **Repository:** [https://github.com/fallingmeteorite/nsfw-image-check-comfyui](https://github.com/fallingmeteorite/nsfw-image-check-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node also directly checks if generated images are NSFW, making it essential for this workflow.

### Metadata
**Author:** fallingmeteorite
**Repository:** [https://github.com/fallingmeteorite/nsfw-image-check-comfyui](https://github.com/fallingmeteorite/nsfw-image-check-comfyui)
**Install Type:** git-clone

---

### nsfwrecog-comfyui

**Description:**

Nodes:NSFW Detector

- **Author:** goburiin
- **Repository:** [https://github.com/goburiin/nsfwrecog-comfyui](https://github.com/goburiin/nsfwrecog-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is another implementation of an NSFW detector, making it highly relevant and useful for the specified workflow goal.

### Metadata
**Author:** goburiin
**Repository:** [https://github.com/goburiin/nsfwrecog-comfyui](https://github.com/goburiin/nsfwrecog-comfyui)
**Install Type:** git-clone

---

### Ollama and Llava Vision integration for ComfyUI

**Description:**

Ollama and Llava vision integration for ComfyUI

- **Author:** fairy-root
- **Repository:** [https://github.com/fairy-root/comfyui-ollama-llms](https://github.com/fairy-root/comfyui-ollama-llms)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal as it integrates Ollama and Llava vision models that could be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node is essential for the specified workflow goal as it provides a prompt generator and CLIP encoder using AI provided by Ollama, which could be directly integrated with canny edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node is very useful as it integrates OmniGen, a model that can perform tasks like image generation and edge detection.

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

**Score:** 80/100

**Reason:** This node is very useful as it integrates OmniGen, a model that can perform tasks like image generation and edge detection.

### Metadata
**Author:** hzane
**Repository:** [https://github.com/hzane/OmniGen-ComfyUI](https://github.com/hzane/OmniGen-ComfyUI)
**Install Type:** git-clone

---

### One Button Prompt

**Description:**

One Button Prompt has a prompt generation node for beginners who have problems writing a good prompt, or advanced users who want to get inspired. It generates an entire prompt from scratch. It is random, but controlled. You simply load up the script and press generate, and let it surprise you.

- **Author:** AIrjen
- **Repository:** [https://github.com/AIrjen/OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant to the workflow goal as it generates prompts but does not directly contribute to image generation or edge detection.

### Metadata
**Author:** AIrjen
**Repository:** [https://github.com/AIrjen/OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt)
**Install Type:** git-clone

---

### OpenPose Editor

**Description:**

A port of the openpose-editor extension for stable-diffusion-webui. NOTE: Requires [a/this ComfyUI patch](https://github.com/comfyanonymous/ComfyUI/pull/711) to work correctly

- **Author:** space-nuko
- **Repository:** [https://github.com/space-nuko/ComfyUI-OpenPose-Editor](https://github.com/space-nuko/ComfyUI-OpenPose-Editor)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** OpenPose Editor node provides direct functionality for image generation guided by canny edge detection, making it essential for this workflow.

### Metadata
**Author:** space-nuko
**Repository:** [https://github.com/space-nuko/ComfyUI-OpenPose-Editor](https://github.com/space-nuko/ComfyUI-OpenPose-Editor)
**Install Type:** git-clone

---

### OpenPose Node

**Description:**

This extension contains a custom node for ComfyUI. The node, called 'Bounding Box Crop', is designed to compute the top-left coordinates of a cropped bounding box based on input coordinates and dimensions of the final cropped image. It does so computing the center of the cropping area and then computing where the top-left coordinates would be.

- **Author:** alessandrozonta
- **Repository:** [https://github.com/alessandrozonta/ComfyUI-OpenPose](https://github.com/alessandrozonta/ComfyUI-OpenPose)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node computes the top-left coordinates of a cropped bounding box based on input coordinates and dimensions, which is useful for applying canny edge detection in image generation.

### Metadata
**Author:** alessandrozonta
**Repository:** [https://github.com/alessandrozonta/ComfyUI-OpenPose](https://github.com/alessandrozonta/ComfyUI-OpenPose)
**Install Type:** git-clone

---

### optimal-crop-resolution

**Description:**

ComfyUI node to calculate optimal resolution to crop the image to (from a list of aspect ratios)

- **Author:** hodanajan
- **Repository:** [https://github.com/hodanajan/optimal-crop-resolution](https://github.com/hodanajan/optimal-crop-resolution)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node calculates the optimal resolution to crop an image to based on a list of aspect ratios, which can be useful for preparing images for edge detection.

### Metadata
**Author:** hodanajan
**Repository:** [https://github.com/hodanajan/optimal-crop-resolution](https://github.com/hodanajan/optimal-crop-resolution)
**Install Type:** git-clone

---

### Painting Coder Utils

**Description:**

A practical collection of nodes for ComfyUI that streamlines image and text processing workflows. Features include image optimized resolution adjustment, text cleaning tools, dynamic image/text combination, and mask preview utilities. Perfect for artists and developers looking to enhance their AI art creation pipeline.

- **Author:** jammyfu
- **Repository:** [https://github.com/jammyfu/ComfyUI_PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a collection of practical nodes that streamlines image and text processing workflows, including mask preview utilities which could be useful in conjunction with canny edge detection for image generation.

### Metadata
**Author:** jammyfu
**Repository:** [https://github.com/jammyfu/ComfyUI_PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)
**Install Type:** git-clone

---

### pfaeff-comfyui

**Description:**

Nodes: AstropulsePixelDetector, BackgroundRemover, ImagePadForBetterOutpaint, InpaintingPipelineLoader, Inpainting, ...

- **Author:** Pfaeff
- **Repository:** [https://github.com/Pfaeff/pfaeff-comfyui](https://github.com/Pfaeff/pfaeff-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node has a collection of nodes related to image processing and inpainting, making it highly relevant to the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** Pfaeff
**Repository:** [https://github.com/Pfaeff/pfaeff-comfyui](https://github.com/Pfaeff/pfaeff-comfyui)
**Install Type:** git-clone

---

### Phi-3-mini in ComfyUI

**Description:**

Nodes:Phi3mini_4k_ModelLoader_Zho, Phi3mini_4k_Zho, Phi3mini_4k_Chat_Zho

- **Author:** ZHO-ZHO-ZHO
- **Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains a model that could be used for image generation and potentially includes edge detection capabilities.

### Metadata
**Author:** ZHO-ZHO-ZHO
**Repository:** [https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Phi-3-mini)
**Install Type:** git-clone

---

### Pipeline Parallel ComfyUI

**Description:**

provide extra api to run prompt request with parallel execution of independent node

- **Author:** DeJoker
- **Repository:** [https://github.com/DeJoker/pipeline-parallel-comfy](https://github.com/DeJoker/pipeline-parallel-comfy)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides parallel execution of independent nodes but does not directly contribute to canny edge detection or image generation.

### Metadata
**Author:** DeJoker
**Repository:** [https://github.com/DeJoker/pipeline-parallel-comfy](https://github.com/DeJoker/pipeline-parallel-comfy)
**Install Type:** git-clone

---

### Pixelization

**Description:**

ComfyUI node that pixelizes images.

- **Author:** filipemeneses
- **Repository:** [https://github.com/filipemeneses/comfy_pixelization](https://github.com/filipemeneses/comfy_pixelization)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is specifically designed to pixelize images which aligns with the goal of generating images guided by canny edge detection.

### Metadata
**Author:** filipemeneses
**Repository:** [https://github.com/filipemeneses/comfy_pixelization](https://github.com/filipemeneses/comfy_pixelization)
**Install Type:** git-clone

---

### Plush-for-ComfyUI

**Description:**

Nodes: Style Prompt, OAI Dall_e Image. Plush contains two OpenAI enabled nodes: Style Prompt: Takes your prompt and the art style you specify and generates a prompt from ChatGPT3 or 4 that Stable Diffusion can use to generate an image in that style. OAI Dall_e 3: Takes your prompt and parameters and produces a Dall_e3 image in ComfyUI.

- **Author:** glibsonoran
- **Repository:** [https://github.com/glibsonoran/Plush-for-ComfyUI](https://github.com/glibsonoran/Plush-for-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains two OpenAI enabled nodes that can generate images in specific styles based on user prompts which aligns with the goal of generating images guided by canny edge detection.

### Metadata
**Author:** glibsonoran
**Repository:** [https://github.com/glibsonoran/Plush-for-ComfyUI](https://github.com/glibsonoran/Plush-for-ComfyUI)
**Install Type:** git-clone

---

### pre_cfg_comfy_nodes_for_ComfyUI

**Description:**

A set of nodes to prepare the noise predictions before the CFG function

- **Author:** Extraltodeus
- **Repository:** [https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI](https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node prepares the noise predictions before the CFG function which is directly related to image generation and could be useful in conjunction with canny edge detection.

### Metadata
**Author:** Extraltodeus
**Repository:** [https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI](https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI)
**Install Type:** git-clone

---

### Preset Dimensions

**Description:**

Simple node for sharing latent image size between nodes. Preset dimensions for SD and XL.

- **Author:** modusCell
- **Repository:** [https://github.com/modusCell/ComfyUI-dimension-node-modusCell](https://github.com/modusCell/ComfyUI-dimension-node-modusCell)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node allows sharing latent image size between nodes but does not directly contribute to canny edge detection or image generation.

### Metadata
**Author:** modusCell
**Repository:** [https://github.com/modusCell/ComfyUI-dimension-node-modusCell](https://github.com/modusCell/ComfyUI-dimension-node-modusCell)
**Install Type:** git-clone

---

### Prompt Injection Node for ComfyUI

**Description:**

This custom node for ComfyUI allows you to inject specific prompts at specific blocks of the Stable Diffusion UNet, providing fine-grained control over the generated image. It is based on the concept that the content/subject understanding of the model is primarily contained within the MID0 and MID1 blocks, as demonstrated in the B-Lora (Content Style implicit separation) paper. Features.
Inject different prompts into specific UNet blocks Three different node variations for flexible workflow integration Customize the learning rate of specific blocks to focus on content, lighting, style, or other aspects Potential for developing a 'Mix of Experts' approach by swapping blocks on-the-fly based on prompt content

- **Author:** DataCTE
- **Repository:** [https://github.com/DataCTE/prompt_injection](https://github.com/DataCTE/prompt_injection)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This custom node allows injecting specific prompts at specific blocks of the Stable Diffusion UNet, providing fine-grained control over the generated image and aligns perfectly with the workflow goal.

### Metadata
**Author:** DataCTE
**Repository:** [https://github.com/DataCTE/prompt_injection](https://github.com/DataCTE/prompt_injection)
**Install Type:** git-clone

---

### Prompt List JSON

**Description:**

This repository provides a custom node for ComfyUI that allows managing positive and negative prompts in a structured JSON format. The node supports adding, updating, and logging prompts, ensuring seamless integration into your workflow.

- **Author:** TKRLAB
- **Repository:** [https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a structured way to manage positive and negative prompts in JSON format which can be useful for refining image generation but does not directly relate to canny edge detection.

### Metadata
**Author:** TKRLAB
**Repository:** [https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON)
**Install Type:** git-clone

---

### Prompt Stash Saver Node for ComfyUI

**Description:**

Prompt Stash is a simple plugin for ComfyUI that lets you save your prompts and organize them into multiple lists. It also features a pass-through functionality, so you can hook it up to an LLM node (or any text outputting node) and capture its outputs directly.

- **Author:** phazei
- **Repository:** [https://github.com/phazei/ConfyUI-node-prompt-stash-saver](https://github.com/phazei/ConfyUI-node-prompt-stash-saver)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows saving and organizing prompts which could be useful in a workflow involving multiple iterations of image generation.

### Metadata
**Author:** phazei
**Repository:** [https://github.com/phazei/ConfyUI-node-prompt-stash-saver](https://github.com/phazei/ConfyUI-node-prompt-stash-saver)
**Install Type:** git-clone

---

### PromptCollapse

**Description:**

A prompt generation system that manages relationships between prompt components to maintain logical consistency. Integrates with ComfyUI as a custom node.

- **Author:** kraglik
- **Repository:** [https://github.com/kraglik/prompt_collapse](https://github.com/kraglik/prompt_collapse)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node manages relationships between prompt components which could be useful in generating consistent and logical prompts for image generation guided by canny edge detection.

### Metadata
**Author:** kraglik
**Repository:** [https://github.com/kraglik/prompt_collapse](https://github.com/kraglik/prompt_collapse)
**Install Type:** git-clone

---

### Propmt Worker

**Description:**

Node:Prompt Worker. A text manipulation node for postprocessing of prompt.

- **Author:** lenskikh
- **Repository:** [https://github.com/lenskikh/ComfyUI-Prompt-Worker](https://github.com/lenskikh/ComfyUI-Prompt-Worker)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as a supporting node for postprocessing of prompts after canny edge detection has been applied.

### Metadata
**Author:** lenskikh
**Repository:** [https://github.com/lenskikh/ComfyUI-Prompt-Worker](https://github.com/lenskikh/ComfyUI-Prompt-Worker)
**Install Type:** git-clone

---

### PuLID_ComfyUI

**Description:**

[a/PuLID](https://github.com/ToTheBeginning/PuLID) ComfyUI native implementation.

- **Author:** cubiq
- **Repository:** [https://github.com/cubiq/PuLID_ComfyUI](https://github.com/cubiq/PuLID_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node may be marginally useful as a supporting node for integrating PuLID with ComfyUI, but it does not directly contribute to the application of canny edge detection in image generation.

### Metadata
**Author:** cubiq
**Repository:** [https://github.com/cubiq/PuLID_ComfyUI](https://github.com/cubiq/PuLID_ComfyUI)
**Install Type:** git-clone

---

### PyramidFlow-ComfyUI

**Description:**

a custom node for [a/Pyramid-Flow](https://github.com/jy0205/Pyramid-Flow)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/PyramidFlow-ComfyUI](https://github.com/AIFSH/PyramidFlow-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This custom node for Pyramid-Flow seems highly relevant as it is specifically designed for image processing tasks and may include canny edge detection functionality.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/PyramidFlow-ComfyUI](https://github.com/AIFSH/PyramidFlow-ComfyUI)
**Install Type:** git-clone

---

### qq-nodes-comfyui

**Description:**

Nodes:Any List, Image Accumulator Start, Image Accumulator End, Load Lines From Text File, XY Grid Helper, Slice List, Axis To String/Int/Float/Model, ...

- **Author:** kenjiqq
- **Repository:** [https://github.com/kenjiqq/qq-nodes-comfyui](https://github.com/kenjiqq/qq-nodes-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Some nodes in this collection (e.g. Image Accumulator Start/End) might be marginally relevant for image processing tasks, but their direct connection to canny edge detection is unclear.

### Metadata
**Author:** kenjiqq
**Repository:** [https://github.com/kenjiqq/qq-nodes-comfyui](https://github.com/kenjiqq/qq-nodes-comfyui)
**Install Type:** git-clone

---

### Quality of Life Nodes for ComfyUI

**Description:**

These nodes aid with batching image processing and maintaining input file names in output files and other quality of life nodes.

- **Author:** SozeInc
- **Repository:** [https://github.com/SozeInc/ComfyUI_Soze](https://github.com/SozeInc/ComfyUI_Soze)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides quality of life features that are useful for maintaining input file names and batching image processing, which could aid in the specified workflow goal.

### Metadata
**Author:** SozeInc
**Repository:** [https://github.com/SozeInc/ComfyUI_Soze](https://github.com/SozeInc/ComfyUI_Soze)
**Install Type:** git-clone

---

### Quality of life Suit:V2

**Description:**

openAI suite, String suite, Latent Tools, Image Tools: These custom nodes provide expanded functionality for image and string processing, latent processing, as well as the ability to interface with models such as ChatGPT/DallE-2.
NOTE: Currently, this extension does not support the new OpenAI API, leading to compatibility issues.

- **Author:** omar92
- **Repository:** [https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Although this node has compatibility issues with the OpenAI API, its expanded functionality for image and string processing can be beneficial for tasks related to image generation guided by canny edge detection.

### Metadata
**Author:** omar92
**Repository:** [https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)
**Install Type:** git-clone

---

### Quick Connections

**Description:**

Quick connections, Circuit board connections

- **Author:** niknah
- **Repository:** [https://github.com/niknah/quick-connections](https://github.com/niknah/quick-connections)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Quick connections might be marginally relevant if the workflow involves circuit board connections that could be used as an analogy for edge detection, but this connection is quite a stretch.

### Metadata
**Author:** niknah
**Repository:** [https://github.com/niknah/quick-connections](https://github.com/niknah/quick-connections)
**Install Type:** git-clone

---

### Quick Image Sequence Process

**Description:**

A ComfyUI plugin for quick image sequence processing. This plugin allows users to manipulate frame sequences with various operations including frame insertion, deletion, and duplication.

- **Author:** kazeyori
- **Repository:** [https://github.com/kazeyori/ComfyUI-QuickImageSequenceProcess](https://github.com/kazeyori/ComfyUI-QuickImageSequenceProcess)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is very useful because it directly supports image sequence processing, which can be used in conjunction with edge detection to generate images.

### Metadata
**Author:** kazeyori
**Repository:** [https://github.com/kazeyori/ComfyUI-QuickImageSequenceProcess](https://github.com/kazeyori/ComfyUI-QuickImageSequenceProcess)
**Install Type:** git-clone

---

### rcsaquino/comfyui-custom-nodes

**Description:**

Nodes: VAE Processor, VAE Loader, Background Remover

- **Author:** rcsaquino
- **Repository:** [https://github.com/rcsaquino/comfyui-custom-nodes](https://github.com/rcsaquino/comfyui-custom-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This repository contains multiple nodes that could be useful for image generation tasks, including VAE Processor and Background Remover. These nodes may support or enhance the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** rcsaquino
**Repository:** [https://github.com/rcsaquino/comfyui-custom-nodes](https://github.com/rcsaquino/comfyui-custom-nodes)
**Install Type:** git-clone

---

### Recommended Resolution Calculator

**Description:**

Input your desired output final resolution, it will automaticaly set the initial recommended SDXL ratio/size and its Upscale Factor to reach that output final resolution, also there's an option for 2x/4x reverse Upscale Factor. These all to avoid using bad/arbitary initial ratio/resolution.

- **Author:** marhensa
- **Repository:** [https://github.com/marhensa/sdxl-recommended-res-calc](https://github.com/marhensa/sdxl-recommended-res-calc)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node calculates recommended resolution settings for SDXL images which could be useful in preparing input images for the specified workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** marhensa
**Repository:** [https://github.com/marhensa/sdxl-recommended-res-calc](https://github.com/marhensa/sdxl-recommended-res-calc)
**Install Type:** git-clone

---

### Remade_nodes

**Description:**

Nodes:Batch Image Blend by Mask, Batch Enlarged Overlay, Batch Image Overlay, Remove Black Pixels to Transparent, Canny Shrink and Recenter, ...

- **Author:** Pheat-AI
- **Repository:** [https://github.com/Pheat-AI/Remade_nodes](https://github.com/Pheat-AI/Remade_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node contains multiple nodes that could be used for image processing tasks, including Canny Shrink and Recenter which aligns with the workflow goal.

### Metadata
**Author:** Pheat-AI
**Repository:** [https://github.com/Pheat-AI/Remade_nodes](https://github.com/Pheat-AI/Remade_nodes)
**Install Type:** git-clone

---

### Rembg Background Removal Node for ComfyUI

**Description:**

Nodes: Image Remove Background (rembg)

- **Author:** Jcd1230
- **Repository:** [https://github.com/Jcd1230/rembg-comfyui-node](https://github.com/Jcd1230/rembg-comfyui-node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is directly relevant to removing backgrounds from images, a crucial step in preparing images for canny edge detection.

### Metadata
**Author:** Jcd1230
**Repository:** [https://github.com/Jcd1230/rembg-comfyui-node](https://github.com/Jcd1230/rembg-comfyui-node)
**Install Type:** git-clone

---

### Rembg Background Removal Node for ComfyUI

**Description:**

Rembg Background Removal Node for ComfyUI

- **Author:** 0x-jerry
- **Repository:** [https://github.com/0x-jerry/comfyui-rembg](https://github.com/0x-jerry/comfyui-rembg)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is also directly relevant to removing backgrounds from images, similar to Node 3.

### Metadata
**Author:** 0x-jerry
**Repository:** [https://github.com/0x-jerry/comfyui-rembg](https://github.com/0x-jerry/comfyui-rembg)
**Install Type:** git-clone

---

### Remembering utils

**Description:**

Helper nodes to display last seed and prompt.

- **Author:** York Xiang
- **Repository:** [https://github.com/bombless/comfyUI-RememberingUtils](https://github.com/bombless/comfyUI-RememberingUtils)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a way to display last seed and prompt, which could be useful for remembering previous parameters used in the workflow.

### Metadata
**Author:** York Xiang
**Repository:** [https://github.com/bombless/comfyUI-RememberingUtils](https://github.com/bombless/comfyUI-RememberingUtils)
**Install Type:** git-clone

---

### RES4LYF

**Description:**

Advanced samplers with new noise scaling math to enable SDE sampling with all publicly available rectified flow models; new unsampling/noise inversion methods and other advanced techniques for inpainting and/or guiding the sampling process with latent images. 40 sampler types, 20 noise types, 7 noise scaling modes, in a single node. Also includes a wide variety of QoF and other utility nodes for manipulating sigmas, latents, images, and more.

- **Author:** ClownsharkBatwing
- **Repository:** [https://github.com/ClownsharkBatwing/RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This node includes advanced samplers with new noise scaling math, unsampling/noise inversion methods, and other techniques that can guide the sampling process with latent images, making it highly relevant to the workflow goal.

### Metadata
**Author:** ClownsharkBatwing
**Repository:** [https://github.com/ClownsharkBatwing/RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF)
**Install Type:** git-clone

---

### Restart Sampling

**Description:**

Unofficial ComfyUI nodes for restart sampling based on the paper 'Restart Sampling for Improving Generative Processes' ([a/paper](https://arxiv.org/abs/2306.14878), [a/repo](https://github.com/Newbeeer/diffusion_restart_sampling))

- **Author:** ssitu
- **Repository:** [https://github.com/ssitu/ComfyUI_restart_sampling](https://github.com/ssitu/ComfyUI_restart_sampling)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal as restart sampling can improve generative processes and potentially enhance the effectiveness of canny edge detection in guiding image generation.

### Metadata
**Author:** ssitu
**Repository:** [https://github.com/ssitu/ComfyUI_restart_sampling](https://github.com/ssitu/ComfyUI_restart_sampling)
**Install Type:** git-clone

---

### roblox-comfyui-nodes

**Description:**

NODES:Scale Image Node, Switch Image Node, Switch Text Node, First Number Node, Mirror Effect Node, Text To ImageNode, Flow Nodes, Simple Save Image Node

- **Author:** VertexStudio
- **Repository:** [https://github.com/VertexStudio/roblox-comfyui-nodes](https://github.com/VertexStudio/roblox-comfyui-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 41/100

**Reason:** Scale Image Node could be useful in resizing images after edge detection, but it does not directly contribute to canny edge detection.

### Metadata
**Author:** VertexStudio
**Repository:** [https://github.com/VertexStudio/roblox-comfyui-nodes](https://github.com/VertexStudio/roblox-comfyui-nodes)
**Install Type:** git-clone

---

### RUI-Nodes

**Description:**

Rui's workflow-specific custom node, written using GPT.

- **Author:** Rui
- **Repository:** [https://github.com/rui40000/RUI-Nodes](https://github.com/rui40000/RUI-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** Text To ImageNode is moderately relevant as it can generate images from text inputs, potentially used for image generation tasks.

### Metadata
**Author:** Rui
**Repository:** [https://github.com/rui40000/RUI-Nodes](https://github.com/rui40000/RUI-Nodes)
**Install Type:** git-clone

---

### Runtime44 ComfyUI Nodes

**Description:**

Nodes: Runtime44Upscaler, Runtime44ColorMatch, Runtime44DynamicKSampler, Runtime44ImageOverlay, Runtime44ImageResizer, Runtime44ImageToNoise, Runtime44MaskSampler, Runtime44TiledMaskSampler, Runtime44IterativeUpscaleFactor, Runtime44ImageEnhance, Runtime44FilmGrain

- **Author:** runtime44
- **Repository:** [https://github.com/runtime44/comfyui_r44_nodes](https://github.com/runtime44/comfyui_r44_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** Runtime44 ComfyUI Nodes is essential for this workflow goal due to its various nodes that can be used in image processing and enhancement tasks after edge detection.

### Metadata
**Author:** runtime44
**Repository:** [https://github.com/runtime44/comfyui_r44_nodes](https://github.com/runtime44/comfyui_r44_nodes)
**Install Type:** git-clone

---

### RyanOnTheInside

**Description:**

Custom nodes introducing particle simulations, optical flow, audio manipulation & reactivity, and temporal masks

- **Author:** ryanontheinside
- **Repository:** [https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside](https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node introduces custom nodes for particle simulations and optical flow which could be useful in generating images guided by canny edge detection.

### Metadata
**Author:** ryanontheinside
**Repository:** [https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside](https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside)
**Install Type:** git-clone

---

### Save Image Extended for ComfyUI

**Description:**

Upgrade the Save File node: customize subfolders, file names with checkpoint names, or any sampler attribute your want! [w/NOTE: This node is a fork from @thedyze, since the [a/original repository](https://github.com/thedyze/save-image-extended-comfyui) is no longer maintained. Simply *uninstall* the original version and **REINSTALL** this one.]

- **Author:** audioscavenger
- **Repository:** [https://github.com/audioscavenger/save-image-extended-comfyui](https://github.com/audioscavenger/save-image-extended-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is directly relevant to saving images generated by canny edge detection, with customizable subfolders and file names.

### Metadata
**Author:** audioscavenger
**Repository:** [https://github.com/audioscavenger/save-image-extended-comfyui](https://github.com/audioscavenger/save-image-extended-comfyui)
**Install Type:** git-clone

---

### Save Image Plus for ComfyUI

**Description:**

Save Image Plus is a custom node for ComfyUI that allows you to save images in JPEG and WEBP formats with optional metadata embedding.

- **Author:** goktug
- **Repository:** [https://github.com/Goktug/comfyui-saveimage-plus](https://github.com/Goktug/comfyui-saveimage-plus)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node allows saving images in JPEG and WEBP formats, which could be useful for the workflow goal, but lacks customization options.

### Metadata
**Author:** goktug
**Repository:** [https://github.com/Goktug/comfyui-saveimage-plus](https://github.com/Goktug/comfyui-saveimage-plus)
**Install Type:** git-clone

---

### Save Image with Generation Metadata

**Description:**

All the tools you need to save images with their generation metadata on ComfyUI. Compatible with Civitai & Prompthero geninfo auto-detection. Works with png, jpeg and webp.

- **Author:** Girish Gopaul
- **Repository:** [https://github.com/giriss/comfy-image-saver](https://github.com/giriss/comfy-image-saver)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant to saving images generated by canny edge detection with their metadata, including compatibility with Civitai & Prompthero geninfo auto-detection.

### Metadata
**Author:** Girish Gopaul
**Repository:** [https://github.com/giriss/comfy-image-saver](https://github.com/giriss/comfy-image-saver)
**Install Type:** git-clone

---

### Save Uncompressed 16 Bit PNG

**Description:**

The SaveImageARGB16PNG node provides functionality for saving images as uncompressed PNG files with ARGB16 precision. This node is particularly useful for workflows that require high-quality image saving with metadata such as prompts and additional PNG info.

- **Author:** yolanother
- **Repository:** [https://github.com/yolanother/ComfyUI-Save16bitPng](https://github.com/yolanother/ComfyUI-Save16bitPng)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for saving high-quality images with metadata such as prompts and additional PNG info.

### Metadata
**Author:** yolanother
**Repository:** [https://github.com/yolanother/ComfyUI-Save16bitPng](https://github.com/yolanother/ComfyUI-Save16bitPng)
**Install Type:** git-clone

---

### SD Prompt Reader

**Description:**

The ultimate solution for managing image metadata and multi-tool compatibility. ComfyUI node version of the SD Prompt Reader.

- **Author:** receyuki
- **Repository:** [https://github.com/receyuki/comfyui-prompt-reader-node](https://github.com/receyuki/comfyui-prompt-reader-node)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows for reading SD prompts which could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** receyuki
**Repository:** [https://github.com/receyuki/comfyui-prompt-reader-node](https://github.com/receyuki/comfyui-prompt-reader-node)
**Install Type:** git-clone

---

### SD-Latent-Upscaler

**Description:**

Upscaling stable diffusion latents using a small neural network.

- **Author:** city96
- **Repository:** [https://github.com/city96/SD-Latent-Upscaler](https://github.com/city96/SD-Latent-Upscaler)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node upscaling stable diffusion latents but does not directly relate to canny edge detection or image generation.

### Metadata
**Author:** city96
**Repository:** [https://github.com/city96/SD-Latent-Upscaler](https://github.com/city96/SD-Latent-Upscaler)
**Install Type:** git-clone

---

### sd-perturbed-attention

**Description:**

Perturbed-Attention Guidance, Smoothed Energy Guidance and Sliding Window Guidance for ComfyUI and SD Forge/reForge. (PAG)

- **Author:** pamparamm
- **Repository:** [https://github.com/pamparamm/sd-perturbed-attention](https://github.com/pamparamm/sd-perturbed-attention)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides perturbed-attention guidance which is a technique often used in conjunction with canny edge detection for improved image generation.

### Metadata
**Author:** pamparamm
**Repository:** [https://github.com/pamparamm/sd-perturbed-attention](https://github.com/pamparamm/sd-perturbed-attention)
**Install Type:** git-clone

---

### SD3-Scaling

**Description:**

Tools for scaling images and latents appropriate to SD3 in ComfyUI.

- **Author:** TylerZoro
- **Repository:** [https://github.com/TylerZoro/SD3-Scaling](https://github.com/TylerZoro/SD3-Scaling)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides tools for scaling images and latents in SD3, which might be useful as a supporting step before applying canny edge detection, but it is not directly related to the goal.

### Metadata
**Author:** TylerZoro
**Repository:** [https://github.com/TylerZoro/SD3-Scaling](https://github.com/TylerZoro/SD3-Scaling)
**Install Type:** git-clone

---

### SD3.5 Empty Latent Size Picker

**Description:**

A utility node for generating empty latent tensors in Stable Diffusion v3.5-compatible resolutions. This node allows for custom batch sizes, width/height overrides, and inverting aspect ratios, ensuring flexibility and compatibility in ComfyUI workflows.

- **Author:** mithamunda
- **Repository:** [https://github.com/mithamunda/ComfyUI-SD3.5-Latent-Size-Picker](https://github.com/mithamunda/ComfyUI-SD3.5-Latent-Size-Picker)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node allows generating empty latent tensors with custom batch sizes and resolutions, making it very useful for preparing inputs for image generation guided by canny edge detection in ComfyUI workflows.

### Metadata
**Author:** mithamunda
**Repository:** [https://github.com/mithamunda/ComfyUI-SD3.5-Latent-Size-Picker](https://github.com/mithamunda/ComfyUI-SD3.5-Latent-Size-Picker)
**Install Type:** git-clone

---

### SDXL Auto Prompter

**Description:**

Easy prompting for generation of endless random art pieces and photographs!

- **Author:** dagthomas
- **Repository:** [https://github.com/dagthomas/comfyui_dagthomas](https://github.com/dagthomas/comfyui_dagthomas)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides easy prompting capabilities which could be useful for generating images based on canny edge detection.

### Metadata
**Author:** dagthomas
**Repository:** [https://github.com/dagthomas/comfyui_dagthomas](https://github.com/dagthomas/comfyui_dagthomas)
**Install Type:** git-clone

---

### SDXL Prompt Styler

**Description:**

SDXL Prompt Styler is a node that enables you to style prompts based on predefined templates stored in a JSON file.

- **Author:** twri
- **Repository:** [https://github.com/twri/sdxl_prompt_styler](https://github.com/twri/sdxl_prompt_styler)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node enables styling prompts based on predefined templates, which is directly relevant to customizing the prompt for canny edge detection.

### Metadata
**Author:** twri
**Repository:** [https://github.com/twri/sdxl_prompt_styler](https://github.com/twri/sdxl_prompt_styler)
**Install Type:** git-clone

---

### SDXL Prompt Styler (customized version by wolfden)

**Description:**

These custom nodes provide a variety of customized prompt stylers based on [a/twri/SDXL Prompt Styler](https://github.com/twri/sdxl_prompt_styler).

- **Author:** wolfden
- **Repository:** [https://github.com/wolfden/ComfyUi_PromptStylers](https://github.com/wolfden/ComfyUi_PromptStylers)
- **Install Type:** git-clone


### Applicability

**Score:** 95/100

**Reason:** This customized version of SDXL Prompt Styler provides a variety of pre-defined styles that could be useful for generating images based on canny edge detection.

### Metadata
**Author:** wolfden
**Repository:** [https://github.com/wolfden/ComfyUi_PromptStylers](https://github.com/wolfden/ComfyUi_PromptStylers)
**Install Type:** git-clone

---

### SDXLCustomAspectRatio

**Description:**

A quick and easy ComfyUI custom node for setting SDXL-friendly aspect ratios.

- **Author:** throttlekitty
- **Repository:** [https://github.com/throttlekitty/SDXLCustomAspectRatio](https://github.com/throttlekitty/SDXLCustomAspectRatio)
- **Install Type:** copy


### Applicability

**Score:** 80/100

**Reason:** This node allows for setting SDXL-friendly aspect ratios which could be useful in conjunction with canny edge detection for image generation.

### Metadata
**Author:** throttlekitty
**Repository:** [https://github.com/throttlekitty/SDXLCustomAspectRatio](https://github.com/throttlekitty/SDXLCustomAspectRatio)
**Install Type:** copy

---

### SDXLResolutionPresets

**Description:**

Nodes: SDXLResolutionPresets. Easy access to the officially supported resolutions, in both horizontal and vertical formats: 1024x1024, 1152x896, 1216x832, 1344x768, 1536x640

- **Author:** wsippel
- **Repository:** [https://github.com/wsippel/comfyui_ws](https://github.com/wsippel/comfyui_ws)
- **Install Type:** copy


### Applicability

**Score:** 90/100

**Reason:** This node provides easy access to officially supported resolutions which is directly relevant to the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** wsippel
**Repository:** [https://github.com/wsippel/comfyui_ws](https://github.com/wsippel/comfyui_ws)
**Install Type:** copy

---

### Searge-LLM for ComfyUI v1.0

**Description:**

A prompt-generator or prompt-improvement node for ComfyUI, utilizing the power of a language model to turn a provided text-to-image prompt into a more detailed and improved prompt.

- **Author:** SeargeDP
- **Repository:** [https://github.com/SeargeDP/ComfyUI_Searge_LLM](https://github.com/SeargeDP/ComfyUI_Searge_LLM)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Searge-LLM can improve text-to-image prompts which could indirectly aid in canny edge detection based image generation.

### Metadata
**Author:** SeargeDP
**Repository:** [https://github.com/SeargeDP/ComfyUI_Searge_LLM](https://github.com/SeargeDP/ComfyUI_Searge_LLM)
**Install Type:** git-clone

---

### SeargeSDXL

**Description:**

Custom nodes for easier use of SDXL in ComfyUI including an img2img workflow that utilizes both the base and refiner checkpoints.

- **Author:** SeargeDP
- **Repository:** [https://github.com/SeargeDP/SeargeSDXL](https://github.com/SeargeDP/SeargeSDXL)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** SeargeSDXL includes an img2img workflow that utilizes SDXL checkpoints and refiner checkpoints, making it highly relevant to the specified workflow goal.

### Metadata
**Author:** SeargeDP
**Repository:** [https://github.com/SeargeDP/SeargeSDXL](https://github.com/SeargeDP/SeargeSDXL)
**Install Type:** git-clone

---

### Segment Any Bedroom Interior

**Description:**

Segment Any Bedroom Interior is a Python-based project designed to segment furniture and objects within a bedroom image. The segmentation process uses RGB codes to accurately differentiate between various pieces of furniture, providing a precise mask output for each segmented object. This project is integrated with ComfyUI to allow easy and intuitive usage.

- **Author:** NguynHungNguyen
- **Repository:** [https://github.com/NguynHungNguyen/Segment-Bedroom-Interior](https://github.com/NguynHungNguyen/Segment-Bedroom-Interior)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node directly addresses the segmentation task required by the workflow goal.

### Metadata
**Author:** NguynHungNguyen
**Repository:** [https://github.com/NguynHungNguyen/Segment-Bedroom-Interior](https://github.com/NguynHungNguyen/Segment-Bedroom-Interior)
**Install Type:** git-clone

---

### segment anything

**Description:**

Based on GroundingDino and SAM, use semantic strings to segment any element in an image. The comfyui version of sd-webui-segment-anything.

- **Author:** storyicon
- **Repository:** [https://github.com/storyicon/comfyui_segment_anything](https://github.com/storyicon/comfyui_segment_anything)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node is specifically designed to segment any element in an image using semantic strings, aligning perfectly with the workflow goal.

### Metadata
**Author:** storyicon
**Repository:** [https://github.com/storyicon/comfyui_segment_anything](https://github.com/storyicon/comfyui_segment_anything)
**Install Type:** git-clone

---

### segment_to_mask_comfyui

**Description:**

Nodes:SegToMask

- **Author:** ginlov
- **Repository:** [https://github.com/ginlov/segment_to_mask_comfyui](https://github.com/ginlov/segment_to_mask_comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Although this node can be used for segmentation, its description does not explicitly mention canny edge detection or image generation, making it marginally relevant.

### Metadata
**Author:** ginlov
**Repository:** [https://github.com/ginlov/segment_to_mask_comfyui](https://github.com/ginlov/segment_to_mask_comfyui)
**Install Type:** git-clone

---

### Semantic-aware Guidance (S-CFG)

**Description:**

ComfyUI node for Semantic-aware Guidance based on the [a/paper](https://arxiv.org/abs/2404.05384) 'Rethinking the Spatial Inconsistency in Classifier-Free Diffusion Guidance'

- **Author:** shiimizu
- **Repository:** [https://github.com/shiimizu/ComfyUI-semantic-aware-guidance](https://github.com/shiimizu/ComfyUI-semantic-aware-guidance)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** Semantic-aware Guidance (S-CFG) uses classifier-free diffusion guidance which could be relevant for image generation and has potential connections to edge detection.

### Metadata
**Author:** shiimizu
**Repository:** [https://github.com/shiimizu/ComfyUI-semantic-aware-guidance](https://github.com/shiimizu/ComfyUI-semantic-aware-guidance)
**Install Type:** git-clone

---

### Semantic-SAM

**Description:**

Segment and Recognize Anything at Any Granularity.

- **Author:** eastoc
- **Repository:** [https://github.com/eastoc/ComfyUI_SemanticSAM](https://github.com/eastoc/ComfyUI_SemanticSAM)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** Semantic-SAM is a segment and recognize anything node that might have some indirect relevance but lacks direct connection to canny edge detection or image generation.

### Metadata
**Author:** eastoc
**Repository:** [https://github.com/eastoc/ComfyUI_SemanticSAM](https://github.com/eastoc/ComfyUI_SemanticSAM)
**Install Type:** git-clone

---

### SigmaWaveFormNodes

**Description:**

A set of tools for generating and altering sigmas in ComfyUI.

- **Author:** BenNarum
- **Repository:** [https://github.com/BenNarum/SigmaWaveFormNode](https://github.com/BenNarum/SigmaWaveFormNode)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides tools for generating and altering sigmas in ComfyUI, which is closely related to image generation and canny edge detection.

### Metadata
**Author:** BenNarum
**Repository:** [https://github.com/BenNarum/SigmaWaveFormNode](https://github.com/BenNarum/SigmaWaveFormNode)
**Install Type:** git-clone

---

### Simple Wildcard

**Description:**

A simple wildcard node for ComfyUI. Can also be used a style prompt node.

- **Author:** vanillacode314
- **Repository:** [https://github.com/vanillacode314/SimpleWildcardsComfyUI](https://github.com/vanillacode314/SimpleWildcardsComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This wildcard node can be used as a style prompt node but its relevance to canny edge detection is indirect at best.

### Metadata
**Author:** vanillacode314
**Repository:** [https://github.com/vanillacode314/SimpleWildcardsComfyUI](https://github.com/vanillacode314/SimpleWildcardsComfyUI)
**Install Type:** git-clone

---

### simple wildcard for ComfyUI

**Description:**

These custom nodes provides a feature to insert arbitrary inputs through wildcards in the prompt. Additionally, this tool provides features that help simplify workflows, such as VAELoaderDecoder and SimplerSample.

- **Author:** lilly1987
- **Repository:** [https://github.com/lilly1987/ComfyUI_node_Lilly](https://github.com/lilly1987/ComfyUI_node_Lilly)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides features like wildcards and VAELoaderDecoder which could help simplify workflows for image generation guided by canny edge detection.

### Metadata
**Author:** lilly1987
**Repository:** [https://github.com/lilly1987/ComfyUI_node_Lilly](https://github.com/lilly1987/ComfyUI_node_Lilly)
**Install Type:** git-clone

---

### SimpleTiles

**Description:**

Nodes:TileSplit, TileMerge.

- **Author:** kinfolk0117
- **Repository:** [https://github.com/kinfolk0117/ComfyUI_SimpleTiles](https://github.com/kinfolk0117/ComfyUI_SimpleTiles)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node includes nodes related to tile splitting and merging which could potentially be used in conjunction with canny edge detection for image processing.

### Metadata
**Author:** kinfolk0117
**Repository:** [https://github.com/kinfolk0117/ComfyUI_SimpleTiles](https://github.com/kinfolk0117/ComfyUI_SimpleTiles)
**Install Type:** git-clone

---

### Simswap Node for ComfyUI

**Description:**

A hacky implementation of Simswap based on [a/Comfyui ReActor Node 0.5.1](https://github.com/Gourieff/comfyui-reactor-node) and [a/Simswap](https://github.com/neuralchen/SimSwap).

- **Author:** TaiTair
- **Repository:** [https://github.com/TaiTair/comfyui-simswap](https://github.com/TaiTair/comfyui-simswap)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node appears to be a direct implementation of Simswap which could potentially utilize canny edge detection for image generation, making it highly relevant to the specified workflow goal.

### Metadata
**Author:** TaiTair
**Repository:** [https://github.com/TaiTair/comfyui-simswap](https://github.com/TaiTair/comfyui-simswap)
**Install Type:** git-clone

---

### Skin Tone Detector for ComfyUI

**Description:**

A ComfyUI node that detects the skin tone of a person in an image and matches it to the standard emoji skin tone palette.

- **Author:** kevinmcmahondev
- **Repository:** [https://github.com/kevinmcmahondev/comfyui-skin-tone-detector](https://github.com/kevinmcmahondev/comfyui-skin-tone-detector)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides a feature that could be useful for preprocessing images before applying canny edge detection, but it is not directly related to the workflow goal.

### Metadata
**Author:** kevinmcmahondev
**Repository:** [https://github.com/kevinmcmahondev/comfyui-skin-tone-detector](https://github.com/kevinmcmahondev/comfyui-skin-tone-detector)
**Install Type:** git-clone

---

### smZNodes

**Description:**

Nodes such as CLIP Text Encode++ to achieve identical embeddings from stable-diffusion-webui for ComfyUI.

- **Author:** shiimizu
- **Repository:** [https://github.com/shiimizu/ComfyUI_smZNodes](https://github.com/shiimizu/ComfyUI_smZNodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node contains nodes such as CLIP Text Encode++ which can achieve identical embeddings from stable-diffusion-webui, making it essential for image generation guided by canny edge detection in ComfyUI.

### Metadata
**Author:** shiimizu
**Repository:** [https://github.com/shiimizu/ComfyUI_smZNodes](https://github.com/shiimizu/ComfyUI_smZNodes)
**Install Type:** git-clone

---

### SP-Nodes

**Description:**

Node Pack: PromptChecker for token toggling, KoboldCPP API, ModelMerging, Telegram-Bot-API, and more

- **Author:** SeniorPioner
- **Repository:** [https://github.com/bananasss00/ComfyUI-SP-Nodes](https://github.com/bananasss00/ComfyUI-SP-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node pack includes a variety of useful tools, including token toggling and model merging, which could be applied in conjunction with canny edge detection for image generation.

### Metadata
**Author:** SeniorPioner
**Repository:** [https://github.com/bananasss00/ComfyUI-SP-Nodes](https://github.com/bananasss00/ComfyUI-SP-Nodes)
**Install Type:** git-clone

---

### SpliceTools

**Description:**

Experimental utility nodes with a focus on manipulation of noised latents

- **Author:** AustinMroz
- **Repository:** [https://github.com/AustinMroz/ComfyUI-SpliceTools](https://github.com/AustinMroz/ComfyUI-SpliceTools)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node provides experimental utility nodes focused on manipulation of noised latents but does not directly relate to canny edge detection or image generation.

### Metadata
**Author:** AustinMroz
**Repository:** [https://github.com/AustinMroz/ComfyUI-SpliceTools](https://github.com/AustinMroz/ComfyUI-SpliceTools)
**Install Type:** git-clone

---

### stability-ComfyUI-nodes

**Description:**

Nodes: ColorBlend, ControlLoraSave, GetImageSize. NOTE: Control-LoRA recolor example uses these nodes.

- **Author:** Stability-AI
- **Repository:** [https://github.com/Stability-AI/stability-ComfyUI-nodes](https://github.com/Stability-AI/stability-ComfyUI-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a GetImageSize function that could be used to analyze and process the input images for canny edge detection.

### Metadata
**Author:** Stability-AI
**Repository:** [https://github.com/Stability-AI/stability-ComfyUI-nodes](https://github.com/Stability-AI/stability-ComfyUI-nodes)
**Install Type:** git-clone

---

### String Converter

**Description:**

Nodes: Convert String To Int, Convert String To Float

- **Author:** glowcone
- **Repository:** [https://github.com/glowcone/comfyui-string-converter](https://github.com/glowcone/comfyui-string-converter)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides functionality to convert strings to integers or floats which could be used in the implementation of canny edge detection algorithm.

### Metadata
**Author:** glowcone
**Repository:** [https://github.com/glowcone/comfyui-string-converter](https://github.com/glowcone/comfyui-string-converter)
**Install Type:** git-clone

---

### StyleShot-ComfyUI

**Description:**

a custom node for [a/StyleShot](https://github.com/open-mmlab/StyleShot.git)

- **Author:** AIFSH
- **Repository:** [https://github.com/AIFSH/StyleShot-ComfyUI](https://github.com/AIFSH/StyleShot-ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node might be marginally useful if StyleShot has a feature related to edge detection or image generation. However, without more information, its relevance is unclear.

### Metadata
**Author:** AIFSH
**Repository:** [https://github.com/AIFSH/StyleShot-ComfyUI](https://github.com/AIFSH/StyleShot-ComfyUI)
**Install Type:** git-clone

---

### tdxh_node_comfyui

**Description:**

Add Switch on nodes, Make nodes amount small! It helps conveniently to use less nodes for doing the same things.

- **Author:** youyegit
- **Repository:** [https://github.com/youyegit/tdxh_node_comfyui](https://github.com/youyegit/tdxh_node_comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** No reason provided

### Metadata
**Author:** youyegit
**Repository:** [https://github.com/youyegit/tdxh_node_comfyui](https://github.com/youyegit/tdxh_node_comfyui)
**Install Type:** git-clone

---

### TensorRT Node for ComfyUI

**Description:**

This node enables the best performance on NVIDIA RTX™ Graphics Cards  (GPUs) for Stable Diffusion by leveraging NVIDIA TensorRT.

- **Author:** comfyanonymous
- **Repository:** [https://github.com/comfyanonymous/ComfyUI_TensorRT](https://github.com/comfyanonymous/ComfyUI_TensorRT)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node leverages NVIDIA TensorRT for optimal performance on RTX GPUs, which could be beneficial for computationally intensive tasks like image generation guided by canny edge detection.

### Metadata
**Author:** comfyanonymous
**Repository:** [https://github.com/comfyanonymous/ComfyUI_TensorRT](https://github.com/comfyanonymous/ComfyUI_TensorRT)
**Install Type:** git-clone

---

### TheAlly's Custom Nodes

**Description:**

Custom nodes for ComfyUI by TheAlly.

- **Author:** theally
- **Repository:** [https://civitai.com/models/19625?modelVersionId=23296](https://civitai.com/models/19625?modelVersionId=23296)
- **Install Type:** unzip


### Applicability

**Score:** 80/100

**Reason:** TheAlly"s Custom Nodes are very useful as they likely contain nodes that support image processing and manipulation.

### Metadata
**Author:** theally
**Repository:** [https://civitai.com/models/19625?modelVersionId=23296](https://civitai.com/models/19625?modelVersionId=23296)
**Install Type:** unzip

---

### Tiled Diffusion & VAE for ComfyUI

**Description:**

The extension enables large image drawing & upscaling with limited VRAM via the following techniques:
1.Two SOTA diffusion tiling algorithms: [a/Mixture of Diffusers](https://github.com/albarji/mixture-of-diffusers) and [a/MultiDiffusion](https://github.com/omerbt/MultiDiffusion)
2.pkuliyi2015's Tiled VAE algorithm.

- **Author:** shiimizu
- **Repository:** [https://github.com/shiimizu/ComfyUI-TiledDiffusion](https://github.com/shiimizu/ComfyUI-TiledDiffusion)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** Tiled Diffusion & VAE for ComfyUI is essential for this workflow goal as it provides techniques to draw and upscale large images using canny edge detection.

### Metadata
**Author:** shiimizu
**Repository:** [https://github.com/shiimizu/ComfyUI-TiledDiffusion](https://github.com/shiimizu/ComfyUI-TiledDiffusion)
**Install Type:** git-clone

---

### Tiled sampling for ComfyUI

**Description:**

This extension contains a tiled sampler for ComfyUI. It allows for denoising larger images by splitting it up into smaller tiles and denoising these. It tries to minimize any seams for showing up in the end result by gradually denoising all tiles one step at the time and randomizing tile positions for every step.

- **Author:** BlenderNeko
- **Repository:** [https://github.com/BlenderNeko/ComfyUI_TiledKSampler](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** Tiled sampling for ComfyUI is very useful as it allows for denoising larger images by splitting them up into smaller tiles, which aligns with the image generation guided by canny edge detection goal.

### Metadata
**Author:** BlenderNeko
**Repository:** [https://github.com/BlenderNeko/ComfyUI_TiledKSampler](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)
**Install Type:** git-clone

---

### TIPO-extension

**Description:**

A general extension to utilize TIPO or DanTagGen to do 'text-presampling' based on KGen library: [a/https://github.com/KohakuBlueleaf/KGen](https://github.com/KohakuBlueleaf/KGen)

- **Author:** KohakuBlueleaf
- **Repository:** [https://github.com/KohakuBlueleaf/z-tipo-extension](https://github.com/KohakuBlueleaf/z-tipo-extension)
- **Install Type:** git-clone


### Applicability

**Score:** 60/100

**Reason:** This node provides a way to utilize text-presampling based on KGen library, which could be useful for generating images with specific features like edges.

### Metadata
**Author:** KohakuBlueleaf
**Repository:** [https://github.com/KohakuBlueleaf/z-tipo-extension](https://github.com/KohakuBlueleaf/z-tipo-extension)
**Install Type:** git-clone

---

### Together Vision Node

**Description:**

A custom ComfyUI node for generating AI-powered image descriptions using Together AI's Vision models (both free and paid versions). Features include customizable prompts, advanced generation parameters, and robust image handling with comprehensive error management.

- **Author:** mithamunda
- **Repository:** [https://github.com/mithamunda/ComfyUI-TogetherVision](https://github.com/mithamunda/ComfyUI-TogetherVision)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node is highly relevant and useful as it directly supports image generation guided by canny edge detection using Together AI"s Vision models.

### Metadata
**Author:** mithamunda
**Repository:** [https://github.com/mithamunda/ComfyUI-TogetherVision](https://github.com/mithamunda/ComfyUI-TogetherVision)
**Install Type:** git-clone

---

### TZOOTZ VHS Effect Node

**Description:**

The TZOOTZ VHS Effect Node is designed for multimedia creators who want to blend digital precision with analog imperfection ↔️. Inspired by retro VHS aesthetics, this node lets you apply grain, color bleeding, saturation adjustments, and more, giving any image a touch of analog warmth and noise.

- **Author:** TZOOTZ
- **Repository:** [https://github.com/TZOOTZ/ComfyUI-TZOOTZ_VHS](https://github.com/TZOOTZ/ComfyUI-TZOOTZ_VHS)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node applies VHS effects which could be used in conjunction with canny edge detection for a unique aesthetic.

### Metadata
**Author:** TZOOTZ
**Repository:** [https://github.com/TZOOTZ/ComfyUI-TZOOTZ_VHS](https://github.com/TZOOTZ/ComfyUI-TZOOTZ_VHS)
**Install Type:** git-clone

---

### ULTools for ComfyUI

**Description:**

Nodes:SaveImgAdv, CLIPTextEncodeWithStats. Collection of tools supporting txt2img generation in ComfyUI and other tasks.

- **Author:** jkrauss82
- **Repository:** [https://github.com/jkrauss82/ultools-comfyui](https://github.com/jkrauss82/ultools-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 50/100

**Reason:** This node includes tools that support txt2img generation which could be useful in the context of image generation, but its direct relevance to canny edge detection is limited.

### Metadata
**Author:** jkrauss82
**Repository:** [https://github.com/jkrauss82/ultools-comfyui](https://github.com/jkrauss82/ultools-comfyui)
**Install Type:** git-clone

---

### unwdef-nodes

**Description:**

Custom nodes for ComfyUI by unwdef.

- **Author:** unwdef
- **Repository:** [https://github.com/unwdef/unwdef-nodes-comfyui](https://github.com/unwdef/unwdef-nodes-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** These custom nodes might offer some utility but their relevance to the specific workflow goal of canny edge detection is unclear.

### Metadata
**Author:** unwdef
**Repository:** [https://github.com/unwdef/unwdef-nodes-comfyui](https://github.com/unwdef/unwdef-nodes-comfyui)
**Install Type:** git-clone

---

### Use Everywhere (UE Nodes)

**Description:**

A set of nodes that allow data to be 'broadcast' to some or all unconnected inputs. Greatly reduces link spaghetti.

- **Author:** chrisgoringe
- **Repository:** [https://github.com/chrisgoringe/cg-use-everywhere](https://github.com/chrisgoringe/cg-use-everywhere)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a way to broadcast data across multiple inputs, which could be useful for implementing complex image generation workflows that involve canny edge detection.

### Metadata
**Author:** chrisgoringe
**Repository:** [https://github.com/chrisgoringe/cg-use-everywhere](https://github.com/chrisgoringe/cg-use-everywhere)
**Install Type:** git-clone

---

### Variables for Comfy UI

**Description:**

Nodes: String, Int, Float, Short String, CLIP Text Encode (With Variables), String Format, Short String Format. This extension introduces quality of life improvements by providing variable nodes and shared global variables.

- **Author:** yolanother
- **Repository:** [https://github.com/yolanother/DTAIComfyVariables](https://github.com/yolanother/DTAIComfyVariables)
- **Install Type:** git-clone


### Applicability

**Score:** 81/100

**Reason:** This node provides various types of variables that could be useful as input or intermediate data for the workflow goal.

### Metadata
**Author:** yolanother
**Repository:** [https://github.com/yolanother/DTAIComfyVariables](https://github.com/yolanother/DTAIComfyVariables)
**Install Type:** git-clone

---

### Vector_Sculptor_ComfyUI

**Description:**

The main node makes your conditioning go towards similar concepts so to enrich your composition or further away so to make it more precise. It gathers similar pre-cond vectors for as long as the cosine similarity score diminishes. If it climbs back it stops. This allows to set a relative direction to similar concepts.
There are examples at the end but [a/you can also check this imgur album](https://imgur.com/a/WvPd81Y) which demonstrates the capability of improving variety.

- **Author:** Extraltodeus
- **Repository:** [https://github.com/Extraltodeus/Vector_Sculptor_ComfyUI](https://github.com/Extraltodeus/Vector_Sculptor_ComfyUI)
- **Install Type:** git-clone


### Applicability

**Score:** 61/100

**Reason:** This node could be useful as a supporting node for the workflow goal, allowing the model to gather similar pre-conditioning vectors and enrich the composition or make it more precise.

### Metadata
**Author:** Extraltodeus
**Repository:** [https://github.com/Extraltodeus/Vector_Sculptor_ComfyUI](https://github.com/Extraltodeus/Vector_Sculptor_ComfyUI)
**Install Type:** git-clone

---

### Vid2vid

**Description:**

A node suite for ComfyUI that allows you to load image sequence and generate new image sequence with different styles or content.

- **Author:** sylym
- **Repository:** [https://github.com/sylym/comfy_vid2vid](https://github.com/sylym/comfy_vid2vid)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node suite allows loading an image sequence and generating new sequences with different styles or content, which aligns perfectly with the workflow goal of image generation guided by canny edge detection.

### Metadata
**Author:** sylym
**Repository:** [https://github.com/sylym/comfy_vid2vid](https://github.com/sylym/comfy_vid2vid)
**Install Type:** git-clone

---

### Virtuoso Nodes for ComfyUI

**Description:**

Photoshop type functions and adjustment layers: 30 blend modes, Selective Color, Blend If, Color Balance, Solid Color Images, Black and White, Hue/Saturation, Levels, and RGB Splitting and Merging.

- **Author:** cfreilich
- **Repository:** [https://github.com/chrisfreilich/virtuoso-nodes](https://github.com/chrisfreilich/virtuoso-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node provides a wide range of Photoshop-like functions that could be used in conjunction with canny edge detection for image generation.

### Metadata
**Author:** cfreilich
**Repository:** [https://github.com/chrisfreilich/virtuoso-nodes](https://github.com/chrisfreilich/virtuoso-nodes)
**Install Type:** git-clone

---

### WebUI Monaco Prompt

**Description:**

Make it possible to edit the prompt using the Monaco Editor, an editor implementation used in VSCode.
NOTE: This extension supports both ComfyUI and A1111 simultaneously.

- **Author:** Taremin
- **Repository:** [https://github.com/Taremin/webui-monaco-prompt](https://github.com/Taremin/webui-monaco-prompt)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows for editing prompts using a Monaco editor which is useful for crafting specific text inputs required in canny edge detection based image generation.

### Metadata
**Author:** Taremin
**Repository:** [https://github.com/Taremin/webui-monaco-prompt](https://github.com/Taremin/webui-monaco-prompt)
**Install Type:** git-clone

---

### Wild Divide

**Description:**

This extension provides the ability to build prompts using wildcards for each region of a split image.

- **Author:** Jjulianadv
- **Repository:** [https://github.com/Julian-adv/WildDivide](https://github.com/Julian-adv/WildDivide)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides the ability to build prompts using wildcards for each region of a split image, which is highly relevant and useful for generating images guided by canny edge detection. It allows users to specify different regions of an image and generate corresponding outputs.

### Metadata
**Author:** Jjulianadv
**Repository:** [https://github.com/Julian-adv/WildDivide](https://github.com/Julian-adv/WildDivide)
**Install Type:** git-clone

---

### wlsh_nodes

**Description:**

Nodes: Checkpoint Loader with Name, Save Prompt Info, Outpaint to Image, CLIP Positive-Negative, SDXL Quick Empty Latent, Empty Latent by Ratio, Time String, SDXL Steps, SDXL Resolutions ...

- **Author:** wallish77
- **Repository:** [https://github.com/wallish77/wlsh_nodes](https://github.com/wallish77/wlsh_nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 40/100

**Reason:** This node contains various nodes that might be useful in different stages of the workflow, such as checkpoint loading and outpainting to an image. However, none of these nodes are directly related to canny edge detection or image generation guided by it.

### Metadata
**Author:** wallish77
**Repository:** [https://github.com/wallish77/wlsh_nodes](https://github.com/wallish77/wlsh_nodes)
**Install Type:** git-clone

---

### x-flux-comfyui

**Description:**

Nodes:Load Flux LoRA, Load Flux ControlNet, Apply Flux ControlNet, Xlabs Sampler

- **Author:** XLabs-AI
- **Repository:** [https://github.com/XLabs-AI/x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node provides a set of nodes that include Load Flux LoRA and Apply Flux ControlNet which are directly related to the workflow goal.

### Metadata
**Author:** XLabs-AI
**Repository:** [https://github.com/XLabs-AI/x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui)
**Install Type:** git-clone

---

### YARS: Yet Another Resolution Selector

**Description:**

A slightly different Resolution Selector node, allowing to freely change base resolution and aspect ratio, with options to maintain the pixel count or use the base resolution as the highest or lowest dimension.

- **Author:** Tropfchen
- **Repository:** [https://github.com/Tropfchen/ComfyUI-yaResolutionSelector](https://github.com/Tropfchen/ComfyUI-yaResolutionSelector)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node allows for resolution selection and aspect ratio adjustment, which could be useful in preparing images for the workflow goal.

### Metadata
**Author:** Tropfchen
**Repository:** [https://github.com/Tropfchen/ComfyUI-yaResolutionSelector](https://github.com/Tropfchen/ComfyUI-yaResolutionSelector)
**Install Type:** git-clone

---

### ymc-node-suite-comfyui

**Description:**

ymc 's nodes for comfyui. This extension is composed of nodes that provide various utility features such as text, region, and I/O.

- **Author:** YMC
- **Repository:** [https://github.com/YMC-GitHub/ymc-node-suite-comfyui](https://github.com/YMC-GitHub/ymc-node-suite-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This suite of nodes likely contains a node for canny edge detection, making it very useful for this workflow goal.

### Metadata
**Author:** YMC
**Repository:** [https://github.com/YMC-GitHub/ymc-node-suite-comfyui](https://github.com/YMC-GitHub/ymc-node-suite-comfyui)
**Install Type:** git-clone

---

### zhangp365/ComfyUI-utils-nodes

**Description:**

Nodes:LoadImageWithSwitch, ImageBatchOneOrMore, ModifyTextGender, ImageCompositeMaskedWithSwitch, ColorCorrectOfUtils, SplitMask, MaskFastGrow, CheckpointLoaderSimpleWithSwitch, ImageResizeTo8x, MatchImageRatioToPreset etc.

- **Author:** zhangp365
- **Repository:** [https://github.com/zhangp365/ComfyUI-utils-nodes](https://github.com/zhangp365/ComfyUI-utils-nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node contains several image processing nodes including LoadImageWithSwitch and ImageCompositeMaskedWithSwitch which could be useful for the specified workflow goal.

### Metadata
**Author:** zhangp365
**Repository:** [https://github.com/zhangp365/ComfyUI-utils-nodes](https://github.com/zhangp365/ComfyUI-utils-nodes)
**Install Type:** git-clone

---

### zhihuige-nodes-comfyui

**Description:**

Nodes: Combine ZHGMasks, Cover ZHGMasks, ZHG FaceIndex, ZHG SaveImage, ZHG SmoothEdge, ZHG GetMaskArea, ...

- **Author:** rcfcu2000
- **Repository:** [https://github.com/rcfcu2000/zhihuige-nodes-comfyui](https://github.com/rcfcu2000/zhihuige-nodes-comfyui)
- **Install Type:** git-clone


### Applicability

**Score:** 90/100

**Reason:** This node includes ZHG SmoothEdge which is directly related to edge detection and could be very useful for the specified workflow goal.

### Metadata
**Author:** rcfcu2000
**Repository:** [https://github.com/rcfcu2000/zhihuige-nodes-comfyui](https://github.com/rcfcu2000/zhihuige-nodes-comfyui)
**Install Type:** git-clone

---

### Zuellni/ComfyUI-Custom-Nodes

**Description:**

Nodes: DeepFloyd, Filter, Select, Save, Decode, Encode, Repeat, Noise, Noise

- **Author:** Zuellni
- **Repository:** [https://github.com/Zuellni/ComfyUI-Custom-Nodes](https://github.com/Zuellni/ComfyUI-Custom-Nodes)
- **Install Type:** git-clone


### Applicability

**Score:** 80/100

**Reason:** This node includes a DeepFloyd node which is likely related to image generation and possibly guided by edge detection or other visual features.

### Metadata
**Author:** Zuellni
**Repository:** [https://github.com/Zuellni/ComfyUI-Custom-Nodes](https://github.com/Zuellni/ComfyUI-Custom-Nodes)
**Install Type:** git-clone

---

### ✨ Clarity AI - Creative Image Upscaler and Enhancer for ComfyUI

**Description:**

[a/Clarity AI](https://clarityai.cc) is a creative image enhancer and is able to upscale to high resolution. [w/NOTE: This is a Magnific AI alternative for ComfyUI.] 
Create an API key on [a/ClarityAI.cc/api](https://clarityai.cc/api) and add to environment variable 'CAI_API_KEY'
Alternatively you can write your API key to file 'cai_platform_key.txt'
You can also use and/or override the above by entering your API key in the 'api_key_override' field of the node.

- **Author:** philz1337x
- **Repository:** [https://github.com/philz1337x/ComfyUI-ClarityAI](https://github.com/philz1337x/ComfyUI-ClarityAI)
- **Install Type:** git-clone


### Applicability

**Score:** 100/100

**Reason:** This node provides a creative image enhancer that can upscale images to high resolution, directly supporting the workflow goal of generating images guided by canny edge detection.

### Metadata
**Author:** philz1337x
**Repository:** [https://github.com/philz1337x/ComfyUI-ClarityAI](https://github.com/philz1337x/ComfyUI-ClarityAI)
**Install Type:** git-clone

---
