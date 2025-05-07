# AI Workflow Taxonomy and Naming Convention

## 1. Introduction & Purpose

Please consider the following taxonomy for classifying various AI generation workflows. Its purpose is to loosely categorize and encourage simplistic single-purpose workflow steps which can provide abstract characterizations of functional behavior. In particular, these will be used to classify and abstractly define ComfyUI and python script workflows for AI generation and curation.

The goal is to build a list of distinctive tasks that would likely require functionally-different workflows, rather than being semantic or stylistic differences.

## 2. Format Categories

The core categories represent distinct types of data commonly used in AI workflows:

*   **T** (text) 📜
*   **I** (image) 🎨
*   **V** (video) 🎬
*   **M** (mesh) 🕸️
*   **S** (sound/speech) 🎵
*   **C** (command/code) ⚙️
*   **D** (data, structured text) 🧮
*   **G** (game, interactive media) 🃏
*   **R** (robotics, real-world) 🦾

In general, we refer to any category as "X".

### 2.1. Scale Modifiers (Singular vs. Multiple/Large)

Each category may have additional nuance based on scale:

*   **X** (singular): Represents a single instance or small scale (e.g., a singular image, a short text prompt).
*   **X+** (multiple/large) ➕: Represents multiple instances or large scale (e.g., very large images, batches of images, a large text corpus, a complex codebase).

**Examples:**

*   **T** vs. **T+**: A single prompt (T) 💬 vs. a batch of documents or a whole book (T+) 📚.
*   **I** vs. **I+**: A single photo (I) 🖼️ vs. a dataset of 1000 images or a gigapixel panorama (I+) 🎨➕_dataset.
*   **V** vs. **V+**: A single video clip (V) ⏱️🎬 vs. an entire library of clips or a long continuous stream (V+) 🎬➕_lib.
*   **S** vs. **S+**: A single sound file (S) 🎶 vs. an album of songs or a 10-hour lecture (S+) 🎵➕_album.
*   **M** vs. **M+**: A single 3D object (M) 🧱 vs. a complex scene with many objects or multiple distinct meshes (M+) 🕸️➕_scene.
*   **C** vs. **C+**: A single script or function (C) 🐍 vs. a large codebase with many files (C+) ⚙️➕_repo.
*   **D** vs. **D+**: A single CSV file or JSON object (D) 🧮 vs. multiple datasets or a multi-gigabyte database (D+) 🗄️.
*   **G** vs. **G+**: A single game level or scenario (G) 🗺️🃏 vs. a franchise or a massive open-world environment (G+) 🌍🃏.

Tasks involving **X+** ➕ often imply batch processing, handling of larger data structures, or iterative operations not required for singular **X** tasks.



### T (Text): 📜
*   **Prompt:** 💬
*   **LLM Response:** 🤖💬
*   **Paragraph:** ¶️
*   **Image Caption:** 🖼️✍️
*   **Plain Text File (.txt):** 📄
*   **Book / Multiple Books:** 📚 (T+)
*   **Chapter:** 📖 (T+)
*   **ComfyUI log:** 🪵 (T+)
*   **Movie Script / Character Personality Script:** 🎭📜 (T+)
*   **Word Document (.docx) / Google Doc:** 📝 (T+)
*   **Markdown File (.md):** Ⓜ️ (T+)
*   **Choose-Your-Own-Adventure Book:** 📖🌲 (T+)
*   **Github Readme:** 🚀📄 (T/T+)
*   **Investment Plan:** 📜📈 (T+)
*   **Log File (e.g., server logs):** 🪵 (T+/D+)
*   **Reddit Thread:** 👽 (D/T+)
*   **PDF Document:** 📄_pdf (I+/T+/D+/G; Default T+)

### I (Image): 🎨
*   **512x512 Image:** 🖼️
*   **Image Diff:** 🖼️∆
*   **Image Mask / Video Frame:** 🖼️🎭 / 🖼️🎞️
*   **Music Sheet (Scanned Image):** 🎼🖼️
*   **4k Image:** 🖼️4k (I/I+)
*   **Image folder:** 📁🖼️ (I+)
*   **Architectural Drawing / Map:** 🗺️📐 (I+)
*   **Geographic Map Tiles (Raster):** 🗺️➕ (I+)
*   **Satellite Imagery / Aerial Photo:** 🛰️🖼️ (I+)
*   **Scanned Paper Map:** 🗺️📜 (I+)
*   **Font:** 🔤 (I+)
*   **QR Code:** 🖼️🔗 (I, encoding D/C)
*   **Photoshop/GIMP File (.psd, .xcf):** 🖌️🖼️ / 🃏_psd (I+/G)
*   **Circuit Diagram:** ⚡️🗺️ / ⚙️_circuit / 🧮_circuit (I/C/D)

### V (Video): 🎬
*   **5 second Video / GIF:** 🎬5s
*   **Video Frames:** 🎞️➕
*   **Live Video Stream (e.g., webcam):** 🎬🔴 (V/V+)
*   **5 minute Video:** 🎬5min (V/V+)
*   **Movie:** 🎬🍿 (V+)
*   **Screen Recording:** 💻🎬 (V+)
*   **360-degree Video:** 🎬🔄 (V+)
*   **Motion Capture Data (.bvh, etc.):** 🕺🎬 / 🕺🧮 (V+/D+)
*   **Video Game Replay File:** 🎮🎬 (G+/V+)

### M (Mesh): 🕸️
*   **3D Printer Object / CAD Design / Blender Object:** 🧱 / 📐 / 🧊 (*Blender*)
*   **Procedurally Generated Mesh (in memory):** ✨🕸️ (M/M+)
*   **Blender Scene:** 🧊➕ (M+)
*   **Point Cloud Data (.ply, .las):** ✨☁️ / 🕸️➕_cloud / 🧮➕_cloud (M+/D+)
*   **Voxel Data (e.g., medical scans):** 🎲➕ (M+)
*   **3D Scan Data (Raw Output):** 🤳🕸️ (M+)
*   **Fractal Geometry (3D):** 🌀🕸️ (M+)
*   **Digital Elevation Model (DEM):** ⛰️🕸️ / ⛰️🧮 (M+/D+)
*   **3D City Model:** 🏙️🕸️ (M+)
*   **Architectural Blueprint (CAD File):** 📐🕸️ / 📐🧮 (M/D)

### S (Sound/Speech): 🎵
*   **Song 30s / Speech / Song 3m:** 🎤 / 🗣️ / 🎶
*   **Synthesized Musical Performance (from MIDI/Score):** ✨🎶
*   **Ultrasound Audio (Doppler, etc.):** 🩺🎵
*   **Morse Code (Audio Transmission):** 📻🎵
*   **Youtube Commentary:** ▶️🗣️ (S+)
*   **Audio Book:** 🎧📚 (S+)
*   **Environmental Sound Recording (Field Recording):** 🌳🔊 (S+)
*   **Audio Spectrogram (as data array):** 📊🔊 (D+)

### C (Command/Code): ⚙️
*   **System Trigger / Internal Call (implicit input):** ⚡️⚙️
*   **Command-line script / Python Script / Zapier API call:** 🖥️ / 🐍 / ⚡️⚙️
*   **HTML text element:** </>_el
*   **URL / Filename:** 🔗 / 📁🔗
*   **ComfyUI Node Settings:** 🧩⚙️
*   **CSS File:** 🖌️
*   **JavaScript File (.js):** 📜JS
*   **Bash / Shell Script (.sh):** 🖥️SH
*   **Torrent Magnet URI:** 🧲🔗
*   **Github code repo:** 🐙 (C+)
*   **HTML text file:** </> (C+)
*   **ComfyUI Workflow (JSON):** 🗺️ (C+)
*   **Android App:** 🤖 (C+)
*   **Firmware Binary:** 💾⚙️ (C+)
*   **LaTeX Document (.tex):** Σ📄 (C+)
*   **Git Commit Diff:** ∆⚙️ / ∆📜 (C/T)
*   **MIDI File:** 🎹⚙️ / 🎹🧮 (C/D)
*   **SVG (Scalable Vector Graphics):** ✏️⚙️ / ✏️🎨 (C/I)
*   **SQL Database Dump (.sql):** 💾⚙️ / 💾🧮 (C+/D+)
*   **Spreadsheet with Macros:** 📊⚙️ / 📊🃏 (C+/G)

### D (Data, structured text): 🧮
*   **File (generic):** 📁
*   **RAR File:** 📚🗜️
*   **Embeddings:** 🔗🧮
*   **Torrent File:** 🧲📄
*   **VCard (.vcf):** 📇
*   **iCalendar (.ics):** 📅
*   **Web Browser Cookie:** 🍪
*   **Security Certificate (.pem, .crt):** 🔒📄
*   **Environment Variables (Set):** 🌳⚙️
*   **Color Palette File (.aco, .gpl):** 🎨📁
*   **Latitude/Longitude Coordinates:** 🌐📍
*   **Hard Drive Space Information:** 💾ℹ️
*   **JSON:** 🧮
*   **CSV Table:** 📊 
*   **requirements.txt:** ✅📄
*   **Subtitle File (.srt, .vtt):** 🎬✍️
*   **LoRA:** 🧬🧮 (D+)
*   **AI model:** 🧠🧮 (D+)
*   **CSV Tables / Database / File Folder / Disk Drive:** 📊➕ / 🗄️ / 📁➕ / 💾➕ (D+)
*   **Trained Neural Network Weights:** 🧠⚖️ (D+)
*   **User Profile (Settings, Preferences, History):** 👤⚙️ (D+)
*   **EEG Brain Scan Data:** 🧠〰️ (D+)
*   **DNA Sequence Data:** 🧬 (D+)
*   **GeoJSON / Shapefile:** 🗺️🧮 (D+)
*   **ZIP / GZ / TAR Archive:** 🗜️➕ (D+)
*   **Windows Registry Hive:** 🪟🧮 (D+)
*   **Scientific Data Format (e.g., HDF5, NetCDF):** 🔬🧮 (D+)
*   **RSS / Atom Feed:** 📡 (D+)
*   **System Process List:** ⚙️📋 (D+)
*   **Network Packet Capture (.pcap):** 🌐🎣 (D+)
*   **Geographic Map Tiles (Vector):** 🗺️📐 (D+)
*   **Route/Boundary Data (GPX, KML):** 🗺️📍 (D+)
*   **Email (.eml file / Standard Format):** 📧 (D+)
*   **YAML / XML / INI Config Files:** 📄cfg / 🌐XML / ⚙️cfg (D)
*   **Image Rating:** 🎨⭐ (D)
*   **Music Sheet (Digital Format e.g., MusicXML):** 🎼🧮 (D/C)
*   **ComfyUI Metadata JSON:** 🧩🧮 / 🗺️⚙️ (D/C+)
*   **Live Stock Market Ticker:** 📈💹 (D+)
*   **Live Sensor Feed (Temperature):**🌡️🌡️ / 🌡️🦾 (D+/R)
*   **GPS Coordinates (live feed):** 🛰️📍 (D+)
*   **API Endpoint Definition (e.g., OpenAPI/Swagger spec):** 🔌🧮 / 🔌⚙️ (D+/C+)

### G (Game, interactive media): 🃏
*   **Shader:** ✨🖥️
*   **ComfyUI Interactive UI:** 🧩🃏
*   **Video Editor with UI:** 🎬✂️
*   **Interactive Fiction (Text Adventure):** 📖🎲
*   **PowerPoint (.pptx) / Google Slides:** 📊▶️
*   **Compiled Shader (Binary):** ✨🖥️💾
*   **UI Element Deletion / State Change (result):** ❌🃏 / ∆🃏
*   **Windows UI Program / Rendered HTML page / Image Viewer / IDE / Executable Program:** 🖼️🃏 / 🌐🃏 / 🖼️👁️ / 💻🃏 / ▶️🃏
*   **Game-playing Agent:** 🤖🎮 (G+)
*   **Docker Image:** 🐳📦 (G+)
*   **Virtual Machine Disk Image (.vdi, .vmdk):** 🖥️💾 (G+)
*   **AI Agent:** 🤖⚙️ / 🤖🃏 (C+/G+)

### R (Robotics, real-world): 🦾
*   **3D Printer Print:** 🧱🦾
*   **Robot Arm (Cobot) Commands / Drone Flightplan:** 💪🦾 / 🚁🗺️
*   **Haptic Feedback Pattern:** ✋〰️
*   **Cooking Recipe / Textile Recipe:** 🍳📖 / 🧵📖
*   **Cookie Recipe (as Instructions):** 🍪📖
*   **Factory Plan:** 🏭🗺️ (R+)

## 6. Conclusion

This taxonomy provides a framework for consistently describing and decomposing complex AI workflows into more manageable, reusable components based on their core data transformations.

