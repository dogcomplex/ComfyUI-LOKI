# Filtered Nodes for: Text to image generation with LoRA model support

Total Available Nodes: 456
Batch Size: 4
Estimated Processing Time: 9.5 minutes

## Results

### 2🐕Seam Mask Generator (`EG_JF_ZZSC`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `senerate_width` (required): `INT`
  - Options: `{{'default': 10, 'min': 1, 'max': 666, 'step': 1}}`
- `smooth` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 50/100

**Reason:** This node can refine a mask by generating seams and might be useful as a supporting node for the workflow.

### Metadata

---

### 2🐕Mask image exchange (`EG_TXZZ_ZH`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask_input` (optional): `MASK`
- `image_input` (optional): `IMAGE`

#### Outputs

- `output_image`: `IMAGE`
- `output_mask`: `MASK`


### Applicability

**Score:** 80/100

**Reason:** This node exchanges images and masks, which could be essential for handling input/output data in text-to-image generation with LoRA model support.

### Metadata

---

### 2🐕Mask can be cut arbitrarily (`EG_ZZHBCJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `operation` (required): `['merge', 'crop', 'intersect', 'not_intersect']`
- `target_image` (optional): `IMAGE`
- `target_mask` (optional): `MASK`
- `source_image` (optional): `IMAGE`
- `source_mask` (optional): `MASK`

#### Outputs

- `result_mask`: `MASK`
- `result_image`: `IMAGE`


### Applicability

**Score:** 70/100

**Reason:** This node can manipulate masks by merging, cropping, intersecting or excluding them from images, supporting the workflow goal.

### Metadata

---

### 2🐕Mask slider extension (`EG_ZZKZ_HT_node`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `extend_size` (required): `INT`
  - Options: `{{'default': 0, 'min': -1000, 'max': 1000, 'step': 1, 'display': 'slider'}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for text to image generation with LoRA model support as it allows for mask extension which is a critical step in the process.

### Metadata

---

### 2🐕Mask Expansion (`EG_ZZ_SSKZ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `extend_size` (required): `INT`
  - Options: `{{'default': 0, 'min': -1000, 'max': 1000, 'step': 1}}`

#### Outputs

- `mask`: `MASK`

## 2🐕/⛱️MASK/🪶FUZZY FEATHERING


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for text to image generation with LoRA model support as it provides an alternative method of mask expansion but lacks specific features compared to the first node.

### Metadata

---

### 2🐕Mask Blurred white edges (`EG_ZZ_BSYH`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `kernel_size` (optional): `INT`
  - Options: `{{'default': 50, 'min': 3, 'max': 200, 'step': 2}}`
- `sigma` (optional): `FLOAT`
  - Options: `{{'default': 15.0, 'min': 0.1, 'max': 200.0, 'step': 0.1}}`
- `shrink_pixels` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 50, 'step': 1}}`
- `expand_pixels` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 50, 'step': 1}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 41/100

**Reason:** This node is marginally relevant for text to image generation with LoRA model support as it blurs white edges in a mask which may not be directly applicable to the workflow goal.

### Metadata

---

### 2🐕Custom template (`EG_TSCMB_GL`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Read` (optional): `['XLNegative']`
  - Options: `{{'default': 'XLNegative'}}`
- `New_Name` (optional): `STRING`
  - Options: `{{'default': 'Please enter a name'}}`
- `New_Content` (optional): `STRING`
  - Options: `{{'default': 'Please enter the content'}}`
- `Function` (optional): `['Read', 'New', 'Delete']`
  - Options: `{{'default': 'Read'}}`

#### Outputs

- `Text`: `STRING`

## 2🐕/🏷️PROMPT WORD MASTER/📌FIXED


### Applicability

**Score:** 80/100

**Reason:** This custom template node allows users to create and modify templates for text-to-image generation, which aligns closely with the workflow goal of generating images from text inputs with LoRA model support.

### Metadata

---

### 2🐕Scene class (`EG_TSCDS_CJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Background` (required): `('None', 'simple background', 'white background', 'outdoors', 'indoors', 'gradient background', 'transparent background', 'christmas', 'halloween', 'science fiction', 'valentine', 'magic circle', 'landscape', 'pentagram', 'feather', 'beautiful detailed water')`
  - Options: `{{'default': 'None'}}`
- `Backgroundweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Sky` (required): `('None', 'sky', 'day', 'cloud', 'night', 'moon', 'night sky', 'full moon', 'starry sky', 'rain', 'sunset', 'sun', 'shooting star', 'moonlight', 'dusk', 'sunburst background', 'skyline', 'blue moon', 'rainy days', 'beautiful detailed sky', 'in spring', 'in summer', 'in autumn', 'in winter', 'stars', 'cloudy', 'in the rain')`
  - Options: `{{'default': 'None'}}`
- `Skyweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Indoor` (required): `('None', 'classroom', 'bedroom', 'bathroom', 'bathtub', 'kitchen', 'library', 'stage', 'dressing room', 'office', 'gym storeroom', 'gym', 'messy room', 'infirmary', 'fitting room', 'dungeon', 'closet', 'toilet stall', 'laboratory', 'prison cell', 'living room', 'hotel room', 'otaku room', 'courtroom', 'storage room', 'cubicle', 'cafeteria', 'conservatory', 'workshop', 'clubroom', 'dining room', 'armory', 'staff room', 'shower')`
  - Options: `{{'default': 'None'}}`
- `Indoorweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Outdoor` (required): `('None', 'city', 'road', 'field', 'bridge', 'poolside', 'street', 'path', 'town', 'railroad tracks', 'alley', 'graveyard', 'garden', 'crosswalk', 'ferris wheel', 'geyser', 'dock', 'sidewalk', 'village', 'railroad crossing', 'rice paddy', 'carousel', 'rural', 'market stall', 'amusement park', 'tunnel', 'running track', 'wheat field', 'canal', 'harbor', 'market', 'stone walkway', 'well', 'phone booth', 'roller coaster', 'dirt road', 'highway', 'runway', 'wooden bridge', 'floating city', 'soccer field', 'waterpark', 'trench', 'shipyard', 'zoo', 'aqueduct', 'rope bridge', 'dam', 'jetty', 'airfield', 'drydock', 'paper lantern', 'water', 'ocean', 'beach', 'nature', 'forest', 'mountain', 'river', 'flower field', 'waterfall', 'lake', 'shore', 'bamboo forest', 'hill', 'desert', 'cliff', 'cave', 'pond', 'stream', 'park', 'island', 'floating island', 'jungle', 'volcano', 'meadow', 'playground', 'canyon', 'wetland', 'savannah', 'parking lot', 'ocean bottom', 'wasteland', 'plain', 'oasis', 'glacier')`
  - Options: `{{'default': 'None'}}`
- `Outdoorweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Building` (required): `('None', 'onsen', 'pool', 'ruins', 'house', 'castle', 'skyscrapers', 'tower', 'school', 'shop', 'shrine', 'rooftop', 'restaurant', 'church', 'train station', 'cafe', 'stadium', 'bell tower', 'bus stop', 'aquarium', 'convenience store', 'lighthouse', 'windmill', 'pagoda', 'hospital', 'apartment', 'temple', 'prison', 'casino', 'hangar', 'arcade', 'movie theater', 'greenhouse', 'bakery', 'factory', 'supermarket', 'airport', 'gazebo', 'tavern', 'treehouse', 'industrial', 'barn', 'garage', 'warehouse', 'shack', 'nightclub', 'arena', 'theater', 'megastructure', 'floating castle', 'bookstore', 'mall', 'convention', 'construction site', 'flower shop', 'museum', 'gas station', 'hotel', 'izakaya', 'skating rink', 'space elevator', 'planetarium', 'bowling alley', 'military base', 'observatory', 'stilt house', 'art gallery', 'weapon shop', 'bunker', 'control tower', 'cooling tower', 'minaret', 'pharmacy', 'nuclear powerplant', 'refinery', 'mosque', 'powerplant', 'salon', 'guard tower', 'amphitheater', 'bar', 'building', 'cityscape', 'neon lights', 'fences')`
  - Options: `{{'default': 'None'}}`
- `Buildingweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Scene Atmosphere` (required): `('None', 'Dark Atmosphere', 'Reflective Atmosphere', 'Enchanting Atmosphere', 'Mystical Atmosphere', 'Whimsical Atmosphere', 'Enigmatic Atmosphere', 'Tranquil Atmosphere', 'Relaxing Atmosphere', 'Blissful Atmosphere', 'Moody Atmosphere', 'Intense Atmosphere', 'Nostalgic Atmosphere', 'Industrial Atmosphere', 'Gothic Atmosphere', 'Light Atmosphere', 'Hazy Atmosphere', 'Dreamy Atmosphere', 'Playful Atmosphere', 'Mysterious Atmosphere', 'Mellow Atmosphere', 'Calm Atmosphere', 'Sophisticated Atmosphere', 'Zen Atmosphere', 'Chill Atmosphere,', 'Melancholic Atmosphere', 'Festive Atmosphere', 'Rustic Atmosphere', 'Romantic Atmosphere')`
  - Options: `{{'default': 'None'}}`
- `Scene Atmosphereweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Architect` (required): `('None', 'Woody Allen', 'Wes Anderson', 'Dario Argento', 'Mario Bava', 'Luc Besson', 'Bong Joon Ho', 'Charlie Chaplin', 'The Coen Brothers', 'Xavier Dolan', 'Clint Eastwood', 'Federico Fellini', 'John Ford', 'Terry Gilliam', 'Michel Gondry', 'Alfred Hitchcock', 'Alejandro Jodorowsky', 'Stanley Kubrick', "Spike Jonze's workThe p", 'Akira Kurosawa', 'Spike Lee', 'George Lucas', 'Terrence Malick', 'Takashi Miike', 'Rachel Morrison', 'Christopher Nolan', 'Ray Harryhausen', 'Roman Polanski', 'Guy Ritchie', 'Ridley Scott', 'Steven Spielberg', 'Quentin Tarantino', 'Santosh Sivan', 'Paul Verhoeven', 'Ed Wood', 'Karel Zeman', 'Guillermo del Toro', 'Bradford Young', 'Denis Villeneuve', 'Johnnie To', 'Jan Svankmajer', 'Zack Snyder', 'Martin Scorsese', 'Tony Scott', 'Park Chan Wook', 'Emeric Pressburger', 'Sergei Parajanov', 'F.W.Murnau', 'George Miller', 'Russ Meyer', 'David Lynch', 'Sergio Leone', 'Kim Ki-Duk', 'Fritz Lang', 'Wong Kar-wai', 'Takeshi Kitano', 'Peter Jackson', 'Jim Henson', 'Jean-Luc Godard', 'Francis Ford Coppola', 'David Fincher', 'Sergei Eisenstein', 'Carl Theodor Dreyer', 'Brian De Palma', 'Jean Cocteau', 'John Cassavetes', 'James Bidgood', 'Ingmar Bergman', 'Darren Aronofsky', 'Paul Thomas Anderson', 'Pedro Almodovar')`
  - Options: `{{'default': 'None'}}`
- `Architectweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node provides scene class options that can be used to generate diverse backgrounds, which is essential for text-to-image generation.

### Metadata

---

### 2🐕Lighting Class (`EG_TSCDS_DG`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Light perception` (required): `('None', 'studio lighting', 'film lighting', 'beautiful lighting', 'Soft illumination', 'dramatic lighting', 'Volumetric lighting', 'mood lighting', 'rim lights', 'Back lighting', 'Split Lighting', 'Rembrandt Lighting', 'bioluminescence', 'Crepuscular Ray', 'rays of shimmering light')`
  - Options: `{{'default': 'None'}}`
- `Light perceptionweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `lighting` (required): `('None', 'lens flare', 'backlighting', 'sparkle', 'bokeh', 'caustics', 'chiaroscuro', 'anaglyph', 'cinematic lighting', 'ray tracing', 'god rays', 'glowing', 'violet', 'neon', 'indigo', 'yellow', 'blue', 'reflection')`
  - Options: `{{'default': 'None'}}`
- `lightingweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 61/100

**Reason:** This node offers lighting class options but they are more focused on specific effects rather than overall scene illumination, making it moderately useful for the workflow goal.

### Metadata

---

### 2🐕Style category (`EG_TSCDS_FG`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Graphic effects` (required): `('None', 'blurry', 'sparkle', 'depth of field', 'motion lines', 'foreshortening', 'lens flare', 'backlighting', 'jpeg artifacts', 'emphasis lines', 'motion blur', 'silhouette', 'chromatic aberration', 'halftone', 'speed lines', 'bokeh', 'film grain', 'drop shadow', 'diffraction spikes', 'bloom', 'caustics', 'multiple monochrome', 'dithering', 'blending', 'vignetting', 'scanlines', 'overexposure', 'lens flare abuse', 'optical illusion', 'chiaroscuro', 'stereogram', 'image fill', 'anaglyph', 'cinematic lighting', 'glowing light', 'god rays', 'ray tracing', 'reflection light', 'chromatic aberration abuse')`
  - Options: `{{'default': 'None'}}`
- `Graphic effectsweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Art style` (required): `('None', 'sketch', 'cosplay', 'traditional media', 'dakimakura (medium)', 'realistic', 'retro artstyle', 'style parody', 'painting (medium)', 'marker (medium)', 'graphite (medium)', 'watercolor (medium)', 'unfinished', 'flat color', 'colored pencil (medium)', 'surreal', 'abstract', 'millipen (medium)', 'faux traditional media', 'fourth wall', 'cyberpunk', 'fine art parody', 'nib pen (medium)', 'variations', 'faux figurine', 'acrylic paint (medium)', 'art nouveau', 'color trace', 'photorealistic', 'expression chart', 'watercolor pencil (medium)', 'calligraphy brush (medium)', 'ink (medium)', 'ballpoint pen (medium)', 'nihonga', 'pastel (medium)', 'mousepad (medium)', 'oil painting (medium)', 'ligne claire', 'pen (medium)', 'ukiyo-e', 'color ink (medium)', 'minimalism', 'brush (medium)', 'lego (medium)', 'impressionism', 'crayon (medium)', 'airbrush (medium)', 'coupy pencil (medium)', 'art deco', 'gouache (medium)', 'charcoal (medium)', 'sumi-e', 'canvas (medium)', 'calligraphy pen (medium)', 'print (medium)', 'cursor (medium)', 'clay (medium)', 'amigurumi (medium)', 'swapnote (medium)', 'graffiti (medium)', 'whiteboard (medium)', 'book cover (medium)', 'flame painter', 'fudepen (medium)', 'leaf (medium)', 'theatre (medium)', 'brushpen (medium)', 'chalk (medium)', 'google sketchup (medium)', 'washi tape (medium)', 'disc (medium)', 'g-pen (medium)', 'illustrator (medium)', 'porcelain (medium)', 'tempera (medium)', 'alphonse mucha', 'pastel color')`
  - Options: `{{'default': 'None'}}`
- `Art styleweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Theme` (required): `('None', 'Hyper Real', 'Photorealism', 'Fantastic Realism', 'Classical Realism', 'Contemporary Realism', 'Surrealism', 'Non-Fiction', 'Imagined', 'Imagination', 'Fever-Dream', 'Daydreampunk', 'Weirdcore', 'Otherworldly', 'From Another Realm', 'Lucid', 'Ethereality', 'Déjà vu', 'Abstraction', 'Fantasy', 'Dark Fantasy', 'Illusion', 'Nonsense', 'Intangible', 'Visual Exaggeration', 'Exaggeration', 'Retrowave', 'Retro', 'Cyberpunk', 'Nanopunk', 'Rusticcore', 'Rollerwave', 'Pre-Historic', 'Historic', 'Prehistoricore', 'Atompunk', 'Jurassic', 'Ice Age', 'Wild West', 'Modern', 'Modernismo', 'Futuristic', 'Cassette Futurism', 'Retro-Futurism', 'Future Funk', 'Afrofuturist', 'Extraterrestrial', 'Invasion', 'Sci-fi', 'Magic', 'Psychic', 'Decopunk', 'Aetherpunk', 'Dragoncore', 'Mythpunk', 'Fairy Folk', 'Anime', 'Cartoon', 'Kawaii', 'Horror Anime', 'Manga', 'Marvel Comics', 'UwU', 'Vampirella', 'Rococopunk', 'Rustic', 'Raypunk', 'Postcyberpunk', 'Antique', 'Nostalgiacore', 'Exaggerated', 'Visual Rhetoric', 'Immaterial', 'Impossible', 'Fantasy Map', 'Ethereal Fantasy', 'Lyrical Abstraction', 'Abstract', 'Anemoiacore', 'Ethereal', 'Wonderland', 'Unworldly', 'Worldly', 'Dreamcore', 'Dreampunk', 'Dreamlike', 'Imaginative', 'Science Fiction', 'Unrealistic', 'Surreal', 'New Realism', 'Magic Realism', 'Realism', 'Photorealistic')`
  - Options: `{{'default': 'None'}}`
- `Themeweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Art unconventional` (required): `('None', 'alternate costume', 'alternate hairstyle', 'aged down', 'genderswap', 'adapted costume', 'no headwear', 'genderswap (mtf)', 'humanization', 'alternate breast size', 'aged up', 'hair down', 'contemporary', 'enmaided', 'alternate color', 'alternate hair length', 'character doll', 'alternate eye color', 'hair up', 'alternate hair color', 'dark persona', 'genderswap (ftm)', 'animalization', 'costume switch', 'fusion', 'alternate universe', 'alternate headwear', 'no eyewear', 'if they mated', 'no wings', 'monsterification', 'role reversal', 'age progression', 'alternate skin color', 'mechanization', 'alternate weapon', 'furrification', 'player 2', 'no tail', 'objectification', 'unusually open eyes', 'alternate wings', 'personality switch', 'no mask', 'age comparison', 'out of character', 'headwear switch', 'palette swap', 'zombification', 'light persona', 'foodification', 'alternate element', 'no animal ears', 'no horn', 'vehicalization', 'slimification', 'costume combination', 'no fire')`
  - Options: `{{'default': 'None'}}`
- `Art unconventionalweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Illustration style` (required): `('None', 'Anatomical Drawing', 'Caricature', 'Assembly Drawing', 'Cartographic', 'Children’s Drawing', 'Crosshatch', 'Graffiti', 'Dot Art', 'Painting', 'Etch-A-Sketch Drawing', 'Figure Drawing', 'Graphic Novel', 'Hand-Drawn', 'Hand-Written', 'Illuminated Manuscript', 'Illustrated-Booklet', 'Illustration', 'Line Art', 'Masterpiece', 'Pointillism', 'Sketch', 'Stipple', 'Storybook Illustration', 'Visual Novel', 'Whimsical Illustration', 'Ballpoint Pen', 'Blackboard', 'Calligraphy', 'Chalk', 'Charcoal Art', 'Colored Pencil', 'Conductive Ink', 'Conte', 'Crayon', 'Dry-Erase Marker', 'Flexographic Ink', 'Fountain Pen Art', 'Gel Pen', 'Graphite', 'Grease Pencil', 'India Ink', 'Iron Gall Ink', 'Ink', 'Marker Art', 'Pastel Art', 'Pencil Art', 'Viscosity Print', 'Wet-Erase Marker', 'Whiteboard', 'Airbrush', '1980s Airbrush Art', 'Ancient Roman Painting', 'Artwork', 'Blacklight Paint', 'Brushwork', 'Caravaggio Painting', 'Canvas', 'Casein Paint', 'Cave Art', 'Chinese Painting', 'Coffee Paint', 'Color Field Painting', 'Detailed Painting', 'Easter Egg', 'Dripping Paint', 'Egg Decorating', 'Encaustic Painting', 'Faux Painting', 'Fayum Portrait', 'Glass Paint', 'Fine Art', 'Gond Painting', 'Gouache Paint', 'Hard Edge Painting', 'Impasto', 'Hydro-Dipping', 'Japanese Painting', 'Kalamkari Painting', 'Madhubani Painting', 'Matte Painting', 'Modern Art', 'Oil Paint', 'Mural', 'Paintwork', 'Paper-Marbling', 'Puffy Paint', 'Phad Painting', 'Rock Art', 'Romanesque Painting', 'Sandpainting', 'Scroll Painting', 'Speedpainting', 'Splatter Paint', 'Spray', 'Stencil Graffiti', 'Still-Life', 'Street Art', 'Warli Painting', 'Tibetan Painting', 'Watercolor', 'Wet Paint', 'Ukiyo-e art', 'watercolor painting', 'ghibli style', 'vinyl figure', 'illustration by Beatrix potter', 'palette knife painting', 'pixar style', 'cartoon style', 'die cut out sticker', 'in Kyoto Animation style', 'in the style of mike winkelmann', 'in the style of rolf armstrong: fractal', 'painted in traditional French art style', 'Eiichiro Oda style', 'by alberto vargas and h.r. giger', 'by Andrey Remnev', 'by Gustav Klimt', 'art by Atey Ghailan', 'Tomer Hanukaart by yoji shinkawa', 'in the style of winsor mccay')`
  - Options: `{{'default': 'None'}}`
- `Illustration styleweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Artist` (required): `('None', 'Zhang Daqian', 'Tan Yin', 'Sonia Delaunay', 'William Eggleston', 'Sandy Skoglund', 'Joel Meyerowitz', 'Arnold Böcklin', 'Frida Kahlo', 'Paul Gauguin', 'Roy Lichtenstein', 'David Hockney', 'Georges Seurat', 'Yayoi Kusama', 'Alfred Sisley', 'Hannah Höch', 'Wassily Kandinsky', 'Eugene Grasset', 'Louis Comfort Tiffany', 'Cy Twombly', 'Robert Motherwell', 'Clyfford Still', 'Barnett Newman', 'Franz Kline', 'On Kawara', 'Paul Klee', 'Henri de Toulouse-Lautrec', 'Gustav Klimt', 'Helen Frankenthaler', 'Egon Schiele', 'Kurt Schwitters', 'Frank Stella', 'Dan Flavin', 'Robert Rauschenberg', 'Henri Rousseau', 'Shepard Fairey', 'Joan Miró', 'Cindy Sherman', 'Paul Outerbridge', 'Stephen Shore', 'Hector Guimard', 'Poiret', 'Aubrey Beardsley', 'Alphonse Mucha')`
  - Options: `{{'default': 'None'}}`
- `Artistweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Film director` (required): `('None', 'David Chipperfield', 'Norman Foster', 'Antoni Gaudi', 'Michael Graves', 'Zaha Hadid', 'Victor Horta', 'Toyo Ito', 'Rem Koolhaas', 'Daniel Libeskind', 'Richard Meier', 'Jean Nouvel', 'Renzo Piano', 'Eero Saarinen', 'Harry Seidler', 'Paolo Soleri', 'James Stirling', 'Kenzo Tange', 'Robert Venturi', 'Peter Zumthor', 'Frank Lloyd Wright', 'Tadao Ando', 'Alejandro Aravena', 'Ricardo Bofill', 'Vincent Callebaut', 'Le Corbusier', 'Buckminster Fuller', 'Frank Gehry', 'Walter Gropius', 'Steven Holld', 'Bjarke Ingels', 'Philip Johnson', 'Kengo Kuma', 'Adolf Loos', 'Oscar Niemeyer', 'Valerio Olgiati', 'Richard Rogers', 'Moshe Safdie', 'Alvaro Siza', 'Ettore Sottsass', 'Louis Sullivan', 'Bernard Tschumi', 'Otto Wagner', 'Ludwig Mies van der Rohe')`
  - Options: `{{'default': 'None'}}`
- `Film directorweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Coding method` (required): `('None', 'censored', 'mosaic censoring', 'bar censor', 'uncensored', 'convenient censoring', 'pointless censoring', 'heart censor', 'hair censor', 'out-of-frame censoring', 'hair over breasts', 'novelty censor', 'nude cover', 'steam censor', 'identity censor', 'tail censor', 'character censor', 'hair over one breast', 'clothes in front', 'censored food', 'fake censor', 'hair over crotch', 'wing censor', "can't show this", 'censored violence', 'bubble filter', 'outside of play area', 'treasure mark censor', 'intimate covering', 'non-intimate covering', 'one finger selfie challenge')`
  - Options: `{{'default': 'None'}}`
- `Coding methodweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 91/100

**Reason:** This node provides a wide range of style category options that can be used to generate diverse artistic styles, which is very useful for text-to-image generation with LoRA model support.

### Metadata

---

### 2🐕Lens class (`EG_TSCDS_JT`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Perspective` (required): `('None', 'cowboy shot', 'from behind', 'from side', 'dutch angle', 'multiple views', 'pov', 'from above', 'from below', 'close-up', 'between legs', 'upside-down', 'blurry foreground', 'wide shot', 'perspective', 'between fingers', 'hatching (texture)', 'fisheye', 'between thighs', 'breast conscious', 'sideways', 'vanishing point', 'from outside', 'cut-in', 'rotated', 'breast awe', 'panorama', 'atmospheric perspective', 'first-person view', 'three sided view')`
  - Options: `{{'default': 'None'}}`
- `Perspectiveweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Positioning` (required): `('None', 'looking at viewer', 'full body', 'upper body', 'solo focus', 'looking back', 'looking at another', 'looking to the side', 'profile', 'looking away', 'looking down', 'looking up', 'portrait', 'facing viewer', 'eye contact', 'upskirt', 'cropped legs', 'cropped torso', 'ass focus', 'facing away', 'sideways glance', 'foot focus', 'pov hands', 'looking afar', 'straight-on', 'pov crotch', 'taking picture', 'lower body', 'staring', 'female pov', 'looking at phone', 'peeping', 'cropped shoulders', 'back focus', 'upshorts', 'upshirt', 'cropped arms', 'cropped torso upper body', 'selfiemirror')`
  - Options: `{{'default': 'None'}}`
- `Positioningweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Action` (required): `('None', 'holding', 'sitting', 'standing', 'lying', 'spread legs', 'on back', 'armpits', 'clothes lift', 'arm up', 'arms up', 'head tilt', 'hand on hip', 'kneeling', 'victory pose', 'leaning forward', 'holding hands', 'arm support', 'on side', 'wariza', 'grabbing', 'arms behind back', 'clothes pull', 'dress lift', 'crossed arms', 'leg up', 'squatting', 'standing on one leg', 'figure four sitting', 'outstretched arms', 'own hands together', 'undressing', 'bent over', 'straddling', 'on stomach', 'outstretched arm', 'lifted by self', 'pointing', 'all fours', 'hand on own chest', 'clenched hand', 'arms behind head', 'index finger raised', 'seiza', 'hand on own face', 'clenched hands', 'legs up', 'dual wielding', 'walking', 'legs apart', "hand on another's head", 'hands on hips', 'running', 'head rest', 'paw pose', 'hand in pocket', 'hand between legs', 'jumping', 'outstretched hand', 'fighting stance', 'beckoning', 'hands in pockets', 'top-down bottom-up', 'adjusting hair', 'spread arms', 'arms at sides', 'double v', 'arched back', 'yokozuwari', 'leg lift', 'hand on own cheek', 'hand on headwear', 'back-to-back', "hand on another's shoulder", 'leaning back', 'holding flower', 'arm grab', 'adjusting eyewear', 'salute', 'hand to own mouth', 'hugging own legs', 'claw pose', 'indian style', 'own hands clasped', 'hands on own face', 'heart hands', 'stretching', "hand on another's", 'hand on own head', 'princess carry', 'one knee', 'w', 'open hand', 'thumbs up', 'skirt pull', 'bikini pull', 'hand on own knee', 'split', 'sheet grab', 'sitting on lap', 'pointing at viewer', 'tying hair', 'feeding', '\\m/', 'pinky out', 'reclining', 'leaning to the side', 'yawning', 'twisted torso', 'standing split', 'hand on own stomach', 'hand on own ass', 'holding eyewear', 'reaching', 'armpit peek', 'fox shadow puppet', 'convenient leg', 'knees to chest', 'shushing', "grabbing another's hair", 'holding strap', 'hands on own knees', "hand on another's cheek", "hand on another's chin", 'pointing up', 'v over eye', 'the pose', 'pointing at self', 'arm hug', 'leaning', 'hair tucking', 'steepled fingers', 'middle finger', 'open dress', 'finger gun', 'upright straddle', 'hair twirling', "hands on another's face", 'arms around neck', 'watson cross', 'fetal position', 'zombie pose', 'crossed ankles', 'arm held back', 'arm around neck', 'rubbing eyes', 'convenient arm', 'holding arrow', 'shading eyes', 'carrying over shoulder', 'spread fingers', 'bunny pose', 'heart hands duo', 'head back', 'ok sign', 'shared food', 'holding syringe', 'mimikaki', 'dress tug', '\\||/', 'holding whip', 'cuddling', 'bowing', 'presenting armpit', 'heart tail', "hand on another's stomach", 'curtsey', 'raised fist', 'carrying under arm', 'glomp', 'talking on phone', 'cupping hands', 'hands on feet', 'balancing', 'hat tip', 'hand on own shoulder', 'stroking own chin', 'hands on ass', 'legs over head', 'adjusting legwear', 'head down', 'necktie grab', 'outstretched leg', 'hair flip', 'belly grab', 'drying hair', 'akanbe', 'dress removed', 'hand on own neck', "hand on another's neck", '\\n/', 'handstand', 'bunching hair', 'adjusting panties', 'shoujo kitou-chuu', 'prostration', 'butterfly sitting', 'crawling', 'fidgeting', 'tying', 'fist bump', 'flapping', 'shrugging', 'toe-point', 'two-finger salute', 'cowering', 'finger frame', 'high five', 'pointing forward', "hand on another's hand", 'thumbs down', 'kissing neck', 'hand on own forehead', 'caramelldansen', 'kuji-in', 'faceplant', 'saturday night fever', 'finger heart', 'hand on ear', 'v over mouth', 'tsuki ni kawatte oshioki yo', 'crucifixion', 'thigh straddling', 'neck biting', 'pointing down', 'pinky swear', 'smelling flower', 'money gesture', 'yoga', 'fist in hand', 'power fist', 'slouching', 'battoujutsu stance', 'middle w', 'convenient head', 'fig sign', 'vulcan salute', 'crossed fingers', 'horns pose', 'shadow puppet', 'carry me', 'superhero landing', 'heart tail duo', 'inward v', 'palm-fist greeting', 'lotus position', 'kamina pose', 'heart arms', 'air guitar', 'headstand', 'pigeon pose', 'palm-fist tap', 'noogie', 'chest stand', 'shaka sign', 'necking', 'finger counting', 'hand glasses', 'wallwalking', 'air quotes', 'heart hands trio', 'shocker (gesture)', 'slit throat (gesture)', 'scorpion pose', 'full scorpion', 'ohikaenasutte', 'orchid fingers', 'arms crossed', 'palm', 'hand in hair', 'humpbacked')`
  - Options: `{{'default': 'None'}}`
- `Actionweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Composition Method` (required): `('None', 'feet out of frame', 'border', 'letterboxed', 'out of frame', 'outside border', 'zoom layer', 'head out of frame', 'tachi-e', 'reference sheet', 'afterimage', 'cropped', 'framed', 'lineup', 'viewfinder', 'collage', 'pillarboxed', 'symmetry', 'column lineup', 'diagram', 'projected inset', 'rotational symmetry', 'glitch', 'partially underwater shot', 'rounded corners', 'stats', 'negative space', 'isometric', 'bust chart', 'relationship graph', 'omake', 'trim marks', 'fading border', 'polar opposites', 'character chart', 'fake scrollbar', 'mosaic art', 'photomosaic', 'move chart', 'seating chart', 'social media composition')`
  - Options: `{{'default': 'None'}}`
- `Composition Methodweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Character Lens` (required): `('None', 'full body', 'Detail Shot(ECU)', 'Face Shot (VCU)', 'Big Close-Up(BCU)', 'Close-Up(CU)', 'Chest Shot(MCU)', 'Waist Shot(WS)')`
  - Options: `{{'default': 'None'}}`
- `Character Lensweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Lens` (required): `('None', 'wide angle', 'depth of field blur', 'depth of field', 'macro lens', 'fisheye lens', '85mm long lens', 'close-up portrait', '24mm wide-angle lens', 'wide angle portrait', '70mm telephoto lens', 'face close-up', '14mm wide angle lens', 'panoramic landscape', 'far close-up', 'vignette', 'high defintion', 'half face close-up', 'gopro view', 'ultra wide angle', 'aerial view', 'birds eye view', 'low angle shot', 'reference sheet', 'focus sharp')`
  - Options: `{{'default': 'None'}}`
- `Lensweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Camera Lens` (required): `('None', 'DSLR', '360 panorama', 'telephoto lens', 'super wide angle', 'tilt-shift', 'depth of field (dof)', 'microscopic view', 'super resolution microscopy')`
  - Options: `{{'default': 'None'}}`
- `Camera Lensweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node offers lens class options that can be used to control the perspective and composition of the generated image, making it essential for achieving specific visual effects in text-to-image generation.

### Metadata

---

### 2🐕Character category (`EG_TSCDS_RW`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Type` (required): `('None', '1girl', 'solo', '1boy', '2girls', 'glasses', '2boys', 'chibi', 'yuri', 'maid', 'loli', 'no humans', 'siblings', 'magical girl', 'demon girl', 'cat girl', 'sisters', 'elf', 'fox girl', 'horse girl', 'child', 'bara', 'yaoi', 'furry', 'crossdressing', 'monster', 'minigirl', 'ghost', 'twins', 'dragon girl', 'miko', 'doll', 'brother and sister', 'gothic lolita', 'shota', 'dog girl', 'angel', 'wolf girl', 'witch', 'waitress', 'cheerleader', 'nun', 'nurse', 'ninja', 'mecha musume', 'fairy', 'office lady', 'vampire', 'mother and daughter', 'mermaid', 'idol', 'yukkuri shiteitte ne', 'cow girl', 'gyaru', 'giantess', 'police', 'race queen', 'female pervert', 'kitsune', 'dark elf', 'oppai loli', 'husband and wife', 'mother and son', 'policewoman', 'dancer', 'raccoon girl', 'kyuubi', 'kogal', 'wa maid', 'orc', 'princess', 'teenage', 'spider girl', 'harem', 'butler', 'voyakiloid', 'cousins', 'centaur', 'priest', 'goblin', 'doctor', 'angel and devil', 'ballerina', 'k/da (league of legends)', 'sailor senshi', 'valkyrie', 'wa lolita', 'long neck', 'kyuudou', 'chef', 'kirisame marisa (cosplay)', 'imp', 'devil', 'female', 'male', 'milf', 'adolescent', 'bunny girl', 'goddess', 'gym leader')`
  - Options: `{{'default': 'None'}}`
- `Typeweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Character in the work` (required): `('None', 'alice margatroid', 'akemi homura', 'akiyama mio', 'aki minoriko', 'akiyama yukari', 'aki shizuha', 'aerith gainsborough', 'aisaka taiga', 'akizuki ritsuko', 'akagi (azur lane)', 'aida mana', 'akuma homura', 'akaza akari', 'akagi miria', 'akatsuki kirika', 'aegis (persona)', 'aino minako', 'alice margatroid (pc-98)', 'altera (fate)', 'akizuki ryo', 'alisa ilinichina amiella', 'alpaca suri (kemono friends)', 'abe nana', 'akali', 'alphonse elric', 'aisha landar', 'aino megumi', 'alisa (girls und panzer)', 'aki (girls und panzer)', 'alastor (shakugan no shana)', 'akashi (azur lane)', 'admiral graf spee (azur lane)', 'agrias oaks', 'akita neru', '2k-tan', 'alena (dq4)', 'afuro terumi', 'alice cartelet', 'aircraft carrier oni', 'ahri')`
  - Options: `{{'default': 'None'}}`
- `Character in the workweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Face` (required): `('None', 'blush', 'smile', 'open mouth', 'blue eyes', 'red eyes', 'brown eyes', 'closed mouth', 'green eyes', 'purple eyes', 'closed eyes', 'yellow eyes', ':d', 'parted lips', 'one eye closed', 'teeth', 'tongue', 'fang', 'tears', 'tongue out', 'pink eyes', 'grin', 'surprised', 'black eyes', 'aqua eyes', 'lips', 'v-shaped eyebrows', 'orange eyes', 'grey eyes', 'symbol-shaped pupils', 'eyelashes', 'saliva', 'makeup', ':3', 'nose blush', 'facial hair', 'heterochromia', 'frown', 'embarrassed', 'fangs', 'upper teeth', 'mouth hold', 'blush stickers', 'expressionless', 'heart-shaped pupils', 'wavy mouth', 'half-closed eyes', 'happy', 'trembling', 'eyes visible through hair', ';d', 'crying', 'light smile', 'lipstick', 'slit pupils', '^^^', 'clenched teeth', 'drooling', 'covering face', 'glowing eyes', 'anger vein', 'angry', 'bright pupils', ':p', 'tareme', 'tsurime', 'forehead', 'skin fang', 'heavy breathing', 'tearing up', 'naughty', ':q', 'empty eyes', 'crying with eyes open', 'jitome', 'light blush', 'o o', '+ +', 'serious', 'smirk', '@ @', 'wide-eyed', 'full blush', 'glint', 'pout', 'multicolored eyes', 'raised eyebrows', 'covering mouth', 'furrowed brow', 'licking lips', 'wince', 'black sclera', 'dot nose', 'eyeball', 'ahegao', 'food on face', 'saliva trail', 'no nose', 'red lips', 'doyagao', 'eyeliner', '>:)', 'aegyo sal', 'laughing', 'star-shaped pupils', 'drunk', 'fang out', 'nosebleed', 'evil smile', 'scared', 'glowing eye', 'annoyed', 'ringed eyes', 'cheek-to-cheek', 'sad', 'white eyes', 'constricted pupils', 'no pupils', 'rolling eyes', '3:', 'torogao', 'sleepy', 'seductive smile', 'nervous', 'blank eyes', 'expressions', 'ear blush', 'split mouth', ':|', 'sparkling eyes', 'facing another', 'yandere', 'sanpaku', 'moaning', 'solid circle eyes', 'turn pale', 'glaring', 'yellow sclera', 'no mouth', '>:(', 'crazy eyes', 'streaming tears', 'tsundere', 'long tongue', 'sideways mouth', 'raised eyebrow', 'gradient eyes', 'shy', 'half-closed eye', 'flower-shaped pupils', 'scowl', 'heart in eye', 'thinking', 'gloom (expression)', 'covering eyes', 'jealous', 'red sclera', 'sigh', 'horizontal pupils', 'nervous smile', 'mouth drool', 'puckered lips', 'screaming', 'smelling', 'grimace', 'cheek pinching', 'cheek poking', 'diamond-shaped pupils', 'happy tears', 'pain', 'confused', 'worried', 'expressionless eyes', 'mismatched pupils', 'crazy smile', 'forehead-to-forehead', 'flustered', 'dot mouth', 'cheek bulge', 'disgust', 'button eyes', 'fume', 'blue sclera', 'bored', 'spit take', 'rectangular mouth', 'facepalm', 'crazy', 'holding breath', 'excited', 'cephalopod eyes', 'cheek pull', 'x-shaped pupils', 'upturned eyes', 'green sclera', 'evil', 'heart-shaped eyes', 'fingersmile', 'panicking', 'rape face', 'hollow eyes', 'determined', 'dashed eyes', 'flower in mouth', 'sobbing', 'mismatched sclera', 'eye reflection', 'cross-eyed', 'lonely', 'compound eyes', 'no sclera', 'depressed', 'bloodshot eyes', 'forced smile', ':c', 'flaming eyes', 'glasgow smile', 'sad smile', ':<>', 'pac-man eyes', 'orange sclera', 'bruised eye', 'despair', 'color drain', 'frustrated', 'upset', 'sulking', 'disappointed', 'horrified', 'stifled laugh', 'disdain', 'uwu', 'dilated pupils', 'envy', '\\(^o^)/', '>3<', 'pensive', 'troll', 'kubrick stare', 'amphibian eyes', 'guilt', 'mako eyes', '> @', 'endured face', 'shaded', 'smiley', 'chin grab', 'wide eyed', 'eyes closed', 'eyebrows behind hair', 'eyebrows visible through hair', 'tired', '(-3-)', '=^=', '=v=', 'amber eyes')`
  - Options: `{{'default': 'None'}}`
- `Faceweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Rare hairstyle` (required): `('None', 'beach waves hair', 'shaggy hair', 'braided hairstyle', 'bun hair', 'crimped hair', 'drill hair', 'dutch braid', 'fishtail braid', 'fringe hair', 'hair flaps', 'half-up half-down hairstyle', 'layered hair', 'lob hair', 'long hair', 'medium hair', 'messy hair', 'ponytail', 'prom hairstyle', 'razor cut hair', 'ringlets hair', 'short hair', 'sleek hair', 'straight hair', 'textured hair', 'twin drills hair', 'updo hairstyle', 'waterfall braid', 'wavy hair', 'wedge cut hair')`
  - Options: `{{'default': 'None'}}`
- `Rare hairstyleweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Rare hairstyle man` (required): `('None', 'clean-shaven', 'comb over', 'drop fade', 'fade', 'fade with beard', 'fade with goatee', 'fade with mustache', 'fade with sideburns', 'french crop', 'goatee', 'high-fade', 'layer cut', 'long beard', 'long hair', 'long mustache', 'low-fade', 'medium hair', 'mid-fade', 'mustache', 'mutton chops', 'pompadour', 'quiff', 'razor cut', 'scissor cut', 'shaggy hair', 'shaved head', 'short back and sides', 'short mustache', 'short hair', 'side part', 'side-swept fringe', 'sideburns', 'slick back', 'spiky hair', 'straight hair', 'taper fade', 'temp fade', 'textured crop', 'textured fringe', 'thick beard', 'thin beard')`
  - Options: `{{'default': 'None'}}`
- `Rare hairstyle manweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Upper body decoration` (required): `('None', 'gloves', 'long sleeves', 'bow', 'bare shoulders', 'collarbone', 'detached sleeves', 'wings', 'open clothes', 'elbow gloves', 'collared shirt', 'fingerless gloves', 'off shoulder', 'cape', 'mole', 'vest', 'bangle', 'coat', 'crop top', 'wrist cuffs', 'sleeves past wrists', 'dress shirt', 'hoodie', 'capelet', 'bandages', 'topless', 'blazer', 'cardigan', 'bat wings', 'tank top', 'blouse', 'casual', 't-shirt', 'wristband', 'armband', 'front-tie top', 'hooded jacket', 'cloak', 'arm belt', 'camisole', 'sleeves past fingers', 'black wings', 'demon wings', 'high-waist skirt', 'angel wings', 'robe', 'bandaged arm', 'center opening', 'lowleg', 'labcoat', 'hat flower', 'criss-cross halter', 'fairy wings', 'center frills', 'sailor shirt', 'wet shirt', 'bracer', 'layered sleeves', 'half gloves', 'badge', 'hooded cloak', 'faulds', 'bead bracelet', 'harness', 'heart cutout', 'gym shirt', 'military jacket', 'hooded coat', 'detached wings', 'unbuttoned shirt', 'butterfly wings', 'cat cutout', 'cropped shirt', 'cat lingerie', 'virgin killer sweater', 'sleeves pushed up', 'command spell', 'dragon wings', 'barcode', 'collared jacket', 'suit jacket', 'open-chest sweater', 'pant suit', 'coattails', 'heart tattoo', 'number tattoo', 'tailcoat', 'hooded cape', 'belly chain', 'bikini top removed', 'hooded sweater', 'jersey', 'cropped vest', 'oversized shirt', 'gloves removed', 'latex gloves', 'duffel coat', 'gathers', 'open robe', 'kesa', 'hooded track jacket', 'load bearing vest', 'heartbeat', 'dudou', 'diamond (gemstone)', 'clothes between breasts', 'heart lock (kantai collection)', 'checkered shirt', 'whip marks', 'muscle', 'bandaged hands', 'bikini top', 'sleeves folded up')`
  - Options: `{{'default': 'None'}}`
- `Upper body decorationweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Lower body decoration` (required): `('None', 'skirt', 'navel', 'panties', 'tail', 'thighs', 'pleated skirt', 'shorts', 'barefoot', 'midriff', 'belt', 'miniskirt', 'white panties', 'apron', 'cutoffs', 'bare legs', 'toes', 'fox tail', 'bottomless', 'thick thighs', 'bike shorts', 'pink panties', 'striped panties', 'side-tie panties', 'demon tail', 'bow panties', 'hakama skirt', 'horse tail', 'panties under pantyhose', 'thong', 'denim shorts', 'buruma', 'dog tail', 'jeans', 'bloomers', 'anklet', 'dragon tail', 'highleg panties', 'kneepits', 'lace-trimmed panties', 'greaves', 'bandaged leg', 'bandaid on leg', 'panty & stocking with garterbelt', 'jumpsuit', 'leotard under clothes', 'bound legs', 'leg tattoo', 'checkered skirt', 'skirt suit', 'trefoil', 'butt plug', 'swimsuit aside', 'capri pants', 'gym shorts', 'cat ear panties', 'mechanical legs', 'denim skirt', 'ankle lace-up', 'chaps', 'leg belt', 'back-print panties', 'diaper', 'thighhighs over pantyhose', 'lowleg pants', 'strawberry panties', 'black garter straps', 'neck garter', 'front-print panties', 'bear panties', 'panties over pantyhose', 'pantyhose under swimsuit', 'white garter straps', 'ankle garter', 'socks over thighhighs', 'hips', 'foot', 'girdling', 'legwear', 'leg garter', 'bikini bottom')`
  - Options: `{{'default': 'None'}}`
- `Lower body decorationweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Full body decoration` (required): `('None', 'tattoo', 'buttons', 'bandaid', 'cuffs', 'sarong', 'shackles', 'handcuffs', 'cane', 'chains')`
  - Options: `{{'default': 'None'}}`
- `Full body decorationweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Hair` (required): `('None', 'long hair', 'short hair', 'bangs', 'blonde hair', 'brown hair', 'black hair', 'hair between eyes', 'twintails', 'very long hair', 'blue hair', 'ponytail', 'purple hair', 'pink hair', 'braid', 'ahoge', 'white hair', 'sidelocks', 'red hair', 'grey hair', 'multicolored hair', 'green hair', 'blunt bangs', 'medium hair', 'silver hair', 'hair bun', 'hair over one eye', 'twin braids', 'shiny hair', 'long braid', 'two side up', 'streaked hair', 'parted bangs', 'single braid', 'double bun', 'gradient hair', 'floating hair', 'swept bangs', 'low twintails', 'one side up', 'wavy hair', 'drill hair', 'hair intakes', 'light brown hair', 'bob cut', 'antenna hair', 'side braids', 'short twintails', 'spiked hair', 'messy hair', 'low-tied long hair', 'hair flaps', 'hair over shoulder', 'twin drills', 'side braid', 'french braid', 'low ponytail', 'hair rings', 'half updo', 'short ponytail', 'curly hair', 'asymmetrical hair', 'tied hair', 'folded ponytail', 'braided ponytail', 'tentacle hair', 'crossed bangs', 'colored inner hair', 'hime cut', 'asymmetrical bangs', 'flipped hair', 'absurdly long hair', 'light blue hair', 'hair over eyes', 'hair behind ear', 'crown braid', 'wet hair', 'cone hair bun', 'bald', 'very short hair', 'undercut', 'big hair', 'front ponytail', 'ringlets', 'huge ahoge', 'pointy hair', 'hair pulled back', 'braided bun', 'topknot', 'braided bangs', 'heart ahoge', 'dark blue hair', 'pompadour', 'hair strand', 'multi-tied hair', 'single sidelock', 'quad tails', 'bangs pinned back', 'diagonal bangs', 'mohawk', 'hair spread out', 'tri tails', 'dreadlocks', 'single hair intake', 'afro', 'bow-shaped hair', 'low twin braids', 'hair in mouth', 'buzz cut', 'bowl cut', 'expressive hair', 'doughnut hair bun', 'crystal hair', 'hair ears', 'split ponytail', 'multiple braids', 'single hair ring', 'rainbow hair', 'side drill', 'curtained hair', 'uneven twintails', 'flattop', 'tri braids', "widow's peak", 'low-braided long hair', 'quad drills', 'mullet', 'pixie cut', 'cornrows', 'nihongami', 'quad braids', 'beehive hairdo', 'heart hair bun', 'hair scarf', 'bald girl', 'quiff', 'lone nape hair', 'front braid', 'crew cut', 'cloud hair', 'mizura', 'shouten pegasus mix mori', 'comb over', 'chonmage', 'triple bun', 'huge afro', 'quin tails', 'hair bikini', 'side swept bangs', 'hair one side up', 'hair two side up', 'side bun', 'okappa')`
  - Options: `{{'default': 'None'}}`
- `Hairweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Head accessories` (required): `('None', 'hair ornament', 'ribbon', 'jewelry', 'hair tie', 'hair bow', 'hairband', 'horns', 'hairclip', 'hair flower', 'hood', 'maid headdress', 'mole under eye', 'bell', 'mask', 'witch hat', 'headphones', 'beret', 'halo', 'eyepatch', 'sunglasses', 'hood down', 'crown', 'tiara', 'black hairband', 'x hair ornament', 'hair bobbles', 'goggles', 'demon horns', 'peaked cap', 'tokin hat', 'mole under mouth', 'eyewear on head', 'hair scrunchie', 'santa hat', 'hood up', 'dragon horns', 'goggles on head', 'bespectacled', 'hairpin', 'white hairband', 'star hair ornament', 'animal hood', 'hair bell', 'forehead mark', 'nurse cap', 'sailor hat', 'scar across eye', 'mouth mask', 'blindfold', 'frog hair ornament', 'heart hair ornament', 'red hairband', 'butterfly hair ornament', 'food-themed hair ornament', 'snake hair ornament', 'mask on head', 'lolita hairband', 'crescent hair ornament', 'feather hair ornament', 'facepaint', 'antlers', 'head wreath', 'blue hairband', 'fox mask', 'scar on cheek', 'covered eyes', 'anchor hair ornament', 'leaf hair ornament', 'forehead jewel', 'rimless eyewear', 'mini top hat', 'bead necklace', 'skull hair ornament', 'forehead protector', 'yellow hairband', 'pink hairband', 'elbow pads', 'fedora', 'bow hairband', 'surgical mask', 'cat hair ornament', 'mask removed', 'musical note hair ornament', 'carrot hair ornament', 'purple hairband', 'wizard hat', 'hair beads', 'bandage over one eye', 'hairpods', 'heart-shaped eyewear', 'multiple hair bows', 'bat hair ornament', 'bone hair ornament', 'gas mask', 'goggles on headwear', 'orange hairband', 'kanzashi', 'snowflake hair ornament', 'over-rim eyewear', 'whistle around neck', 'clover hair ornament', 'winged helmet', 'mask pull', 'fish hair ornament', 'mouth veil', 'coke-bottle glasses', 'jeweled branch of hourai', 'anchor choker', 'tengu mask', 'behind-the-head headphones', 'flower on head', 'kamina shades', 'head mounted display', 'bandage on', 'bunny hair ornament')`
  - Options: `{{'default': 'None'}}`
- `Head accessoriesweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Ears` (required): `('None', 'animal ears', 'earrings', 'pointy ears', 'cat ears', 'rabbit ears', 'fox ears', 'fake animal ears', 'wolf ears', 'horse ears', 'dog ears', 'kemonomimi mode', 'hoop earrings', 'mouse ears', 'cow ears', 'raccoon ears', 'tiger ears', 'lion ears', 'heart earrings', 'bear ears', 'squirrel ears', 'sheep ears', 'crescent earrings', 'cat ear headphones', 'long pointy ears', 'deer ears', 'panda ears', 'monkey ears', 'goat ears', 'bat ears', 'crystal earrings', 'pig ears', 'covering ears', 'pikachu ears', 'ferret ears')`
  - Options: `{{'default': 'None'}}`
- `Earsweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Neck` (required): `('None', 'necktie', 'collar', 'bowtie', 'sailor collar', 'chain necklace', 'scarf', 'neckerchief', 'ascot', 'neck ribbon', 'detached collar', 'turtleneck', 'halterneck', 'wing collar', 'neck bell', 'pendant', 'fur collar', 'high collar', 'ribbon choker', 'magatama', 'sleeveless turtleneck', 'headphones around neck', 'necktie between breasts', 'spiked collar', 'blue neckwear', 'neck ring', 'black neckwear', 'animal collar', 'v-neck', 'popped collar', 'pearl necklace', 'lanyard', 'metal collar', 'heart choker', 'goggles around neck', 'feather boa', 'green neckwear', 'neck ruff', 'open collar', 'plunging neckline', 'pentacle', 'bolo tie', 'plaid neckwear', 'flower necklace', 'red neckwear', 'amulet', 'stole', 'necktie removed', 'cross tie', 'jabot', 'lei', 'collar grab', 'collar tug', 'checkered neckwear', 'locket', 'adjusting collar', 'necktie on head', 'pet cone', 'friendship charm', 'dog collar', 'aqua neckwear', 'brown neckwear', 'grey neckwear', 'orange neckwear', 'pink neckwear', 'purple neckwear', 'white neckwear', 'yellow neckwear', 'striped neckwear')`
  - Options: `{{'default': 'None'}}`
- `Neckweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Clothing` (required): `('None', 'dress', 'underwear', 'school uniform', 'swimsuit', 'bikini', 'frills', 'kimono', 'sailor', 'striped', 'white dress', 'uniform', 'black dress', 'leotard', 'see-through', 'torn clothes', 'one-piece swimsuit', 'bodysuit', 'military uniform', 'sleeveless dress', 'blue dress', 'plaid skirt', 'chinese clothes', 'obi', 'short dress', 'formal', 'red dress', 'school swimsuit', 'lingerie', 'frilled dress', 'polka dot', 'suit', 'pink dress', 'waist apron', 'china dress', 'lace', 'strapless dress', 'corset', 'micro bikini', 'purple dress', 'side slit', 'highleg leotard', 'pencil skirt', 'sailor dress', 'santa costume', 'gym uniform', 'lolita fashion', 'green dress', 'competition swimsuit', 'yukata', 'nightgown', 'wedding dress', 'backless outfit', 'off-shoulder dress', 'long dress', 'bandeau', 'microskirt', 'collared dress', 'armored dress', 'suspender skirt', 'sundress', 'pinafore dress', 'bikini under clothes', 'brown dress', 'pleated dress', 'grey dress', 'bikini skirt', 'highleg bikini', 'layered dress', 'short kimono', 'layered skirt', 'yellow dress', 'open kimono', 'backless dress', 'slingshot swimsuit', 'striped dress', 'bikini armor', 'babydoll', 'two-tone dress', 'sweater dress', 'casual one-piece swimsuit', 'untied bikini', 'sailor senshi uniform', 'latex', 'multi-strapped bikini', 'multicolored dress', 'police uniform', 'competition school swimsuit', 'dougi', 'thong bikini', 'halter dress', 'lowleg bikini', 'fur-trimmed dress', 'business suit', 'torn dress', 'orange dress', 'bikini lift', 'strapless bikini', 'print dress', 'maid bikini', 'meiji schoolgirl uniform', 'kindergarten uniform', 'gothic', 'reverse bunnysuit', 'plaid dress', 'sailor bikini', 'layered bikini', 'baseball uniform', 'vertical-striped dress', 'bodysuit under clothes', 'ribbed dress', 'negligee', 'eyepatch bikini', 'evening gown', 'bow bikini', 'lace-trimmed dress', 'clothes down', 'gown', 'impossible bodysuit', 'harem outfit', 'sports bikini', 'hanfu', 'volleyball uniform', 'aqua dress', 'impossible dress', 'straitjacket', 'see-through dress', 'polka dot dress', 'biker clothes', 'pencil dress', 'bondage outfit', 'taut dress', 'santa dress', 'dirndl', 'kimono skirt', 'cocktail dress', 'athletic leotard', 'living clothes', 'bikesuit', 'uchikake', 'ribbon-trimmed dress', 'shell bikini', 'loungewear', 'virgin killer outfit', 'skirt basket', 'dress basket', 'wet dress', 'cute & girly (idolmaster)', 'tube dress', 'tutu', 'vietnamese dress', 'checkered dress', 'stile uniform', 'varia suit', 'front zipper swimsuit', 'funeral dress', 'coat dress', 'pinstripe dress', 'argyle dress', 'high-low skirt', 'latex dress', 'dress flip', 'highleg dress', 'dress grab', 'crinoline', 'mermaid dress', 'tennis dress', 'denim dress', 'hobble dress', 'half-dress', 'flag dress', 'cake dress', 'trapeze dress', 'sepia dress', 'santa', 'side-tie bikini', 'western', 'tartan', 'sheath dress', 'pettiskirt', 'organza lace', 'playboy bunny leotard')`
  - Options: `{{'default': 'None'}}`
- `Clothingweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Shoes and socks` (required): `('None', 'thighhighs', 'pantyhose', 'boots', 'socks', 'black thighhighs', 'black legwear', 'high heels', 'white thighhighs', 'white legwear', 'kneehighs', 'thigh boots', 'garter straps', 'knee boots', 'loafers', 'fishnets', 'torn legwear', 'mary janes', 'striped thighhighs', 'striped legwear', 'cross-laced footwear', 'high heel boots', 'asymmetrical legwear', 'garter belt', 'brown legwear', 'tabi', 'uneven legwear', 'toeless legwear', 'print legwear', 'lace-trimmed legwear', 'bodystocking', 'red legwear', 'mismatched legwear', 'slippers', 'fishnet legwear', 'legwear under shorts', 'leggings', 'purple legwear', 'bobby socks', 'pink thighhighs', 'grey legwear', 'uwabaki', 'loose socks', 'pink legwear', 'blue legwear', 'argyle legwear', 'leg warmers', 'ribbon-trimmed legwear', 'american flag legwear', 'green legwear', 'pantylines', 'vertical-striped legwear', 'frilled legwear', 'rudder footwear', 'stirrup legwear', 'alternate legwear', 'seamed legwear', 'yellow legwear', 'striped socks', 'multicolored legwear', 'ribbed legwear', 'fur-trimmed legwear', 'strappy heels', 'ankle socks', 'see-through legwear', 'fine fabric emphasis', 'legwear garter', 'stiletto heels', 'back-seamed legwear', 'boots removed', 'two-tone legwear', 'ballet slippers', 'bow legwear', 'barefoot sandals', 'latex legwear', 'torn thighhighs', 'leg cutout', 'garters', 'toeless boots')`
  - Options: `{{'default': 'None'}}`
- `Shoes and socksweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it allows for character customization, including face, hair, and clothing options, which are essential for text-to-image generation with LoRA model support.

### Metadata

---

### 2🐕Item category (`EG_TSCDS_WP`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Items` (required): `('None', 'sword', 'gun', 'umbrella', 'chair', 'backpack', 'microphone', 'handgun', 'teacup', 'cigarette', 'ofuda', 'chopsticks', 'camera', 'wand', 'gohei', 'guitar', 'scythe', 'dagger', 'yin yang', 'whip', 'riding crop', 'piano', 'crease', 'weapons', 'arrow', 'lantern/lamp')`
  - Options: `{{'default': 'None'}}`
- `Itemsweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Flowers` (required): `('None', 'flower', 'petals', 'rose', 'floral print', 'plant', 'cherry blossoms', 'red rose', 'bouquet', 'sunflower', 'potted plant', 'hibiscus', 'blue rose', 'white rose', 'pink rose', 'hydrangea', 'rose petals', 'clover', 'spider lily', 'purple rose', 'lily pad', 'yellow rose', 'lotus', 'plum blossoms', 'flower (symbol)', 'black rose', 'wreath', 'daisy', 'wisteria', 'lily of the valley', 'camellia', 'tulip', 'petals on liquid', 'morning glory', 'dandelion', 'flower bracelet', 'chrysanthemum', 'orange rose', 'qingxin flower', 'green rose', 'hanafuda', 'plumeria', 'flower on liquid', 'carnation', 'flower bed', 'strawberry blossoms', 'grey rose', 'glaze lily', 'water lily flower', 'gardening', 'pansy', 'orchid', 'daffodil', 'poinsettia', 'bellflower', 'lunar tear', 'silent princess', 'on flower', 'brown rose', 'fire flower', 'rapeseed blossoms', 'flower trim', 'calla lily', 'red carnation', 'chinese bellflower', 'gerbera', 'osmanthus', 'marigold', 'dahlia', "baby's-breath", 'multicolored rose', 'magnolia', 'epiphyllum', 'lilac', 'bird of paradise flower', 'anthurium', 'trumpet creeper', 'hollyhock', 'hyacinth', 'gracidea', 'peach blossom', 'orange blossoms', 'sweet flower', 'chamomile', 'ice flower', 'mimosa (flower)', 'fuchsia', 'tiger lily', 'thistle', 'cornflower', 'gladiolus', 'petunia (flower)', 'ranunculus', 'geranium', 'gold osmanthus', 'dianthus', 'passion flower', 'pomegranate flower', 'bougainvillea', 'coughing flowers', 'foxglove', 'gentiana (flower)', 'edelweiss', 'snowdrop', 'spathiphyllum', 'zinnia', 'cosmos', 'oncidium', 'rhododendron', 'gloriosa (flower)', 'oleander', 'alstroemeria (flower)', 'amaryllis (flower)', 'cymbidium', 'eustoma', 'forsythia', 'heliconia', 'kerria japonica', 'rudbeckia', 'columbine', 'cockscomb (flower)', 'black lotus', "angel's trumpet", "four o'clock (flower)", 'nigella', 'portulaca', 'buttercup', 'begonia', 'blueberry blossoms', 'forget-me-not', 'genista (flower)', 'grass lily', 'dusty miller', 'freesia', 'kalanchoe', 'potato flower', 'wolfsbane', 'black-eyed susan', 'clivia', 'crocus', 'dipsacaceae', 'great burnet', 'lisianthus (flower)', 'paulownia', 'snapdragon', 'wax flower', 'dimorphotheca', 'hawthorn (plant)', 'hellebore', 'lantana (flower)', 'marsh marigold', 'gourd blossom', 'pentas (flower)', 'periwinkle', 'pieris japonica', 'potentilla', 'flowers meadows', 'anemone', 'azalea', 'bleeding heart', 'chinese lantern (plant)', 'clematis', 'flax', 'jasmine', 'iris', 'larkspur', 'lavender', 'lily', 'moonflower', 'nemophila', 'peony', 'perennial', 'poppy', 'rafflesia', 'red ginger', 'reimu', 'violet', 'silk flower')`
  - Options: `{{'default': 'None'}}`
- `Flowersweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Food` (required): `('None', 'burger', 'sushi', 'pizza', 'baozi', 'sandwich', 'bento', 'curry', 'omelet', 'french fries', 'makizushi', 'takoyaki', 'curry rice', 'soup', 'tempura', 'hot dog', 'holding pizza', 'jiaozi', 'pizza slice', 'salad', 'shrimp tempura', 'crumbs', 'pizza box', 'tofu', 'party', 'aburaage', 'oden', 'narutomaki', 'nigirizushi', 'zouni soup', 'nabe', 'corn dog', 'miso soup', 'croquette', 'canned food', 'breakfast', 'salt', 'mapo tofu', 'birthday party', 'tea party', 'okonomiyaki', 'flour', 'taco', 'dinner', 'meal', 'pizza delivery', 'gunkanmaki', 'takuan', 'inarizushi', 'feast', 'dim sum', 'okosama lunch', 'conveyor belt sushi', 'tamagokake gohan', 'sushi geta', 'sukiyaki', 'lunch', 'zongzi', 'fondue', 'cooking oil', 'fish and chips', 'french toast', 'unadon (food)', 'ribs (food)', 'tang yuan', 'megamac', 'shumai', 'stinky tofu', 'twice cooked pork', 'katsu', 'katsudon', 'konnyaku', 'milk', 'cream', 'cheese', 'milk bottle', 'milk carton', 'whipped cream', 'butter', 'baby bottle', 'milkshake', 'yogurt', 'yakult', 'milk churn', 'strawberry milk', 'swiss cheese', 'condensed milk', 'chocolate milk', 'smoked cheese', 'kefir', 'milk mustache', 'eggnog', 'strawberry', 'apple', 'peach', 'watermelon', 'cherry', 'grapes', 'mandarin orange', 'banana', 'lemon', 'lemon slice', 'blueberry', 'orange slice', 'berry', 'red apple', 'melon', 'pineapple', 'raspberry', 'fruit cup', 'banana peel', 'chocolate banana', 'persimmon', 'golden apple', 'pear', 'lime slice', 'banana boat', 'kiwi slice', 'pomegranate', 'yuzu (fruit)', 'fruit bowl', 'apple bunny', 'banana slice', 'green apple', 'on banana', 'olive', 'bitten apple', 'mango', 'apple core', 'umeboshi', 'grapefruit', 'cantaloupe', 'plum', 'lychee', 'avocado', 'apple peel', 'fig', 'orangette', 'grape stomping', 'dragon fruit', 'banana popsicle', 'papaya', 'muskmelon', 'starfruit', 'gel banana', 'cacao fruit', 'currant', 'akebia fruit', 'mangosteen', 'nashi pear', 'kiwi', 'rambutan', 'blackberry', 'lime', 'honeydew', 'orange', 'candy', 'cake', 'popsicle', 'lollipop', 'chocolate', 'ice cream', 'pocky', 'wagashi', 'tootsweets', 'cookie', 'dango', 'heart-shaped chocolate', 'ice cream cone', 'macaron', 'cake slice', 'candy apple', 'chewing gum', 'parfait', 'mochi', 'cupcake', 'candy cane', 'pudding', 'pastry', 'shaved ice', 'swirl lollipop', 'potato chips', 'taiyaki', 'birthday cake', 'crepe', 'strawberry shortcake', 'chocolate bar', 'checkerboard cookie', 'marshmallow', 'pie', 'watermelon bar', 'sundae', 'popcorn', 'youkan', 'icing', 'soft serve', 'chocolate cake', 'ice cream float', 'popsicle stick', 'wafer stick', 'sprinkles', 'swiss roll', 'songpyeon', 'tupet', 'cream puff', 'double scoop', 'gingerbread man', 'chocolate cornet', 'chocolate chip cookie', 'pastry box', 'jelly bean', 'konpeitou', 'chikuwa', 'sakura mochi', 'cheesecake', 'gelatin', 'french cruller', 'apple pie', 'pretzel', 'mont blanc (food)', 'wafer', 'shaped lollipop', 'strawberry parfait', 'thumbprint cookie', 'doritos', 'umaibou', 'chupa chups', 'triple scoop', 'waffle cone', 'white chocolate', 'pringles', 'oreo', 'dorayaki', 'anpan', 'batter', 'fruit tart', 'kashiwa mochi (food)', 'sandwich cookie', 'mooncake', 'kinoko no yama', 'chocolate doughnut', 'churro', 'layer cake', 'dough', 'too many scoops', 'bugles', 'tanghulu', 'baumkuchen', 'christmas cake', 'apollo chocolate', 'old-fashioned doughnut', 'eclair (food)', 'wedding cake', 'anmitsu (dessert)', 'cinnamon roll', 'ichigo daifuku', 'gingerbread house', 'nerunerunerune', 'caramel', 'single scoop', 'chocolate fountain', 'strawberry tart', 'kitkat', 'gumball', 'tiramisu', 'yule log', 'gingerbread cookie', "m&m's", 'toppo', 'custard', 'ice cream sandwich', 'cigarette candy', 'mille-feuille', 'momiji manjuu', 'quadruple scoop', 'madeleine', 'noppo bread', 'black forest cake', 'pinata', 'pound cake', 'stollen', 'banana split', 'chitose ame', 'imagawayaki', 'slushie', 'pudding a la mode', "country ma'am", 'rare cheesecake', 'blueberry tart', 'charlotte cake', 'marble chocolate', 'red velvet cake', 'coolish', 'warabimochi', 'opera cake', 'sakura french', 'namagashi', 'strawberry swiss roll', 'mitsumame', 'hot cross bun', 'fondant au chocolat', 'chocolate framboise', 'chocolate marquise', 'bavarois', 'suama (food)', 'brownie', 'creme egg', 'takenoko no sato', 'tart', 'uirou', 'chips', 'fish', 'egg', 'crab', 'chicken', 'fried egg', 'shrimp', 'boned meat', 'sausage', 'steak', 'egg laying', 'fish bone', 'bacon', 'fried chicken', 'kebab', 'eggshell', 'chicken leg', 'tako-san wiener', 'kamaboko', 'lobster', 'egg yolk', 'hamburger steak', 'sashimi', 'yakitori', 'meatball', 'gyuudon', 'hardboiled egg', 'roe', 'ham', 'chicken nuggets', 'broken egg', 'eggshell hat', 'pork', 'turkey', 'turkey leg', 'scrambled egg', 'caviar', 'century egg (food)', 'katsuo no tataki', 'kani-san wiener', 'ikura', "jack-o'-lantern", 'carrot', 'pumpkin', 'mushroom', 'spring onion', 'tomato', 'sweet potato', 'cucumber', 'eggplant', 'potato', 'lettuce', 'beans', 'corn', 'seaweed', 'coconut', 'onion', 'daikon', 'cabbage', 'chili pepper', 'broccoli', 'yakiimo', 'pepper shaker', 'mint', 'chestnut', 'cherry tomato', 'bell pepper', 'nattou', 'turnip', 'peanut', 'garlic', 'pickle', 'habanero pepper', 'bitter melon', 'squash', 'asparagus', 'red bean paste', 'onion rings', 'almond', 'parsley', 'green pepper', 'cauliflower', 'bok choy', 'red pepper', 'jalapeno pepper', 'kimchi', 'warabi', 'yellow pepper', 'hijiki', 'nori', 'ketchup', 'honey', 'sugar cube', 'jam', 'soy sauce', 'sauce', 'mayonnaise', 'salt shaker', 'chocolate syrup', 'wasabi', 'hot sauce', 'sugar (food)', 'strawberry syrup', 'peanut butter', 'marmalade', 'furikake', 'bread', 'rice', 'onigiri', 'noodles', 'pancake', 'ramen', 'toast', 'omurice', 'baguette', 'cup ramen', 'spaghetti', 'rice on face', 'japari bun', 'melon bread', 'pancake stack', 'senbei', 'croissant', 'udon', 'fried rice', 'waffle', 'yakisoba', 'cracker', 'soba', 'scone', 'bread bun', 'bread eating race', 'cereal', 'kitsune udon', 'yakisobapan', 'biscuit (bread)', 'spaghetti and meatballs', 'soumen', 'jirou (ramen)', 'rice porridge', 'lasagne', 'bread crust', 'nanakusa-no-sekku', 'black spaghetti', 'empanada', 'risotto', 'italian (niigata)', 'arare', 'alcohol', 'tea', 'beer', 'sake', 'coffee', 'wine', 'soda can', 'bubble tea', 'ramune', 'coca-cola', 'tropical drink', 'champagne', 'soda', 'cocktail', 'starbucks', 'green tea', 'juice', 'whiskey', 'canned coffee', 'vodka', 'orange juice', 'pepsi', 'liquor', 'coffee beans', 'dr pepper', 'black tea', 'cocktail umbrella', 'blue hawaii', 'melon soda', 'lemonade', 'latte art', 'iced tea', 'fanta', 'martini', 'mountain dew', 'calpis', 'milk tea', 'tequila', 'georgia max coffee', 'pepsi ice cucumber', 'margarita', 'root beer', 'guinness (beer)', '7up', 'barley tea', 'rose hip tea', 'cafe au lait', 'earl grey tea', 'darjeeling tea', 'herbal tea', 'non-alcoholic beer', 'caesar (drink)', 'dandelion coffee', 'spear mint tea', 'amazake')`
  - Options: `{{'default': 'None'}}`
- `Foodweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Printing Materials` (required): `('None', '3D Printed', 'Bagh Print', 'Barcode', 'Blueprint', 'Business Card', 'Concept Art', 'Edge-To-Edge Photographic Print', 'IKEA Guide', 'Instruction Manual', 'Laser Printed', 'Logo', 'Monotype', 'Newspaper', 'Pop-up Book', 'Poster', 'QR Code', 'Sticker', 'Transfer Printing', 'Watermark', 'Album Art', 'Bagru Print', 'Block Printing', 'Booklet', 'Comic Book', 'Concert Poster', 'Flexography', 'Inkjet Printed', 'Kids Book', 'Lithography', 'Magazine', 'Movie Poster', 'Pokemon Card', 'Postage Stamp', 'Printed', 'Risograph', 'Tarot Card', 'Underground Comix')`
  - Options: `{{'default': 'None'}}`
- `Printing Materialsweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Physical Materials` (required): `('None', 'Paper Model', 'Laser-Cut', 'Agateware', 'Arts and Crafts', 'Ancient Roman Mosaic', 'Ice-Carving', 'Chinese Paper Art', 'Aquatint', 'Assemblage', 'Banner', 'Azulejo', 'Beads and String', 'Beadwork', 'Bejeweled', 'Bentwood', 'Bone China', 'Cameo Glass', 'Card', 'Carpentry', 'Carving', 'Chintzware', 'Chip-Carving', 'Circuit', 'Coffee Stain', 'Computer Chip', 'Confetti', 'Decal', 'Decoupage', 'Diorama', 'Drypoint', 'Egyptian Faience', 'Enamel Pin', 'Enameled Glass', 'Encaustic Tile', 'Engraved Gem', 'Etching', 'Featherwork', 'Figurine', 'Frame', 'Fretwork', 'Glass Mosaic', 'Glass Blowing', 'Glass-Etching', 'Glaze', 'Hatmaking', 'Hardstone Carving', 'Hedge Trimming', 'Installation Art', 'Intarsia', 'Intaglio', 'Iris-Folding', 'Ironwork', 'Lacquer', 'Kirigami', 'Land Art', 'Lath Art', 'Leather Crafting', 'Latte Art', 'Light Painting', 'Linocut', 'Lithophane', 'Lustreware', 'Marquetry', 'Metalcut', 'Micromosaic', 'Mezzotint', 'Minoan Mural', 'Model', 'Mosaic', 'Origami', 'Overglaze', 'Ornament', 'Papercutting', 'Paper-Mache', 'Paper-Colle', 'Photo collage', 'Pietra Dura', 'Photo gravure', 'Projection Mapping', 'Puppet', 'Pyrography', 'Relief-Carving', 'Salt Glaze Pottery', 'Resin', 'Scrapbooking', 'Scrimshaw', 'Sgraffito', 'Sculpture', 'Signage', 'Site-Specific art', 'Smoke Art', 'Stencil', 'Stoneware', 'Sticker Bomb', 'String-Art', 'Tableware', 'Tapestry', 'Tattoo', 'Tie-dye', 'Tin-Glazed Pottery', 'Whittling', 'Underglaze', 'Woodblock Print', 'Wood-Carving', 'Woodcut')`
  - Options: `{{'default': 'None'}}`
- `Physical Materialsweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node is extremely useful as it provides a wide range of item categories, including food, flowers, and physical materials, which can be used to generate diverse images with LoRA model support.

### Metadata

---

### 2🐕Quality category (`EG_TSCDS_ZL`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Image type` (required): `('None', 'highres', 'absurdres', 'original', 'comic', 'official art', 'lowres', 'scan', '4koma', 'back', 'parody', 'cover page', 'game cg', 'animated', 'revision', 'doujin cover', 'outline', 'oekaki', 'video', 'animated gif', 'card (medium)', 'tall image', 'anime screencap', 'logo', 'silent comic', 'everyone', '2koma', '3d', 'pixel art', 'lineart', '3koma', 'error', 'looping animation', 'checkered', 'fake screenshot', 'multiple 4koma', '1koma', 'album cover', 'official wallpaper', 'artbook', 'magazine cover', '5koma', 'left-to-right manga', 'incredibly absurdres', 'calendar (medium)', 'tegaki', 'vector trace', 'wide image', 'flash', 'fake cover', 'no lineart', 'live2d', 'manga cover', 'dvd cover', 'video game cover', 'music video', 'right-to-left comic', 'corrupted file', 'animated png', 'paper child', 'postcard', 'borderless panels', 'phonecard', 'paper cutout', 'kirigami', 'character single', 'non-repeating animation', 'roulette animation', 'easytoon', 'tileable', 'shitajiki', 'papercraft', 'triptych (art)', 'archived file', 'gyotaku (medium)', 'huge filesize', 'sample', 'wallpaper', 'masterpiece', 'best quality', 'worst quality', 'low quality', 'normal quality', 'extremely detailed cg unity 8k wallpaper', 'illustration', 'nsfw', 'eromanga', 'icon', 'photo', 'poster', 'widescreen')`
  - Options: `{{'default': 'None'}}`
- `Image typeweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Renderer` (required): `('None', 'Unreal engine', 'Rendered in octane', 'Corona Render', 'V-Ray', 'UE5', 'UE4', 'octane render', 'architectural visualisation/Architectural rendering', 'Quixel Megascans Render')`
  - Options: `{{'default': 'None'}}`
- `Rendererweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Positive prompt word` (required): `('None', 'best quality', 'Amazing', 'masterpiece', 'delicate', 'ultra high res', 'ultra detailed', 'highly detailed', 'intricate detail', 'beautiful detailed', 'finely detailed', '8K', '8k resolution', 'professional lighting', 'physically-based rendering', 'cool', 'good balance', 'Camcorder Effect', 'symmetrical face', '((no text))', '(rim lighting)', 'professional photography', 'sharp focus', '(extremely detailed CG unity 8k wallpaper)', '(photo realistic:1.4)', 'realistic model', '(photorealistic:1.4)', 'Realistic art', '(RAW photo:1.4)', 'HDR')`
  - Options: `{{'default': 'None'}}`
- `Positive prompt wordweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Negative prompt word` (required): `('None', '(low quality:2)', '(worst quality:2)', 'lowers', 'lowres', 'blurry', 'out of focus', 'error', 'easynegative', '(signature:1.2)', '(artist name:1.2)', '(watermark:1.2)', '((backlight:2))', 'wood', 'wood texture', '(watermark, logo)', 'bad anatomy', '(bad proportions:1.331)', '((grayscale))', '((monochrome))', 'extra ears', 'fewer fingers', 'extra fingers', 'missing fingers', 'mutated hands', '(extra hands)', '(fused fingers:1.61051)', '(poorly drawn hands:1.331)', 'poorly drawn face', 'poorly drawn eyes', '(extra legs:1.331)', 'extra arms', 'extra limbs', 'malformed limbs', 'malformed hands', 'ugly face', '(ugly:1.331)', 'bad hands', 'bad legs', 'bad knees', 'bad neck', 'skin spot', 'age spot', 'acnes', 'teeth', 'cross-eyed', 'skin blemishes', '((freckle))', 'mutation', 'deformed', '(duplicate:1.331)', '(morbid:1.21)', '(mutilated:1.21)', '(tranny:1.331)', '(disfigured:1.331)', '(unclear eyes:1.331)', 'bad body', 'missing limb', 'extra limb', 'floating limbs', 'disconnected limbs', 'long neck', 'long body', 'multiple shoulders', 'feet out of view', 'head out of view', 'uncensored', '((((nude, naked,))))', 'topless', 'nsfw')`
  - Options: `{{'default': 'None'}}`
- `Negative prompt wordweight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `random` (required): `['yes', 'no']`
  - Options: `{{'default': 'no'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`

## 2🐕/🏷️PROMPT WORD MASTER/🔀RANDOM CLASS


### Applicability

**Score:** 60/100

**Reason:** This node is moderately useful as it allows for image quality customization, but its direct relevance to text-to-image generation with LoRA model support is limited compared to other nodes.

### Metadata

---

### 2🐕Random prompt (`EG_SJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Custom_Type1` (optional): `['None', 'Sky', 'Indoor', 'Outdoor', 'Building', 'Flowers', 'Graphic effects', 'Image type', 'Coding method', 'Composition Method', 'Art style', 'Background', 'Color', 'Art unconventional', 'Perspective', 'Upper body decoration', 'Lower body decoration', 'Character in the work', 'Full body decoration', 'Action', 'Hair', 'Head accessories', 'Positioning', 'Type', 'Ears', 'Neck', 'Clothing', 'Face', 'Shoes and socks', 'Items', 'Food', 'Negative prompt word', 'Positive prompt word', 'Theme', 'Character Lens', 'Light perception', 'Twelve Constellations', 'Printing Materials', 'Scene Atmosphere', 'Architect', 'Illustration style', 'Renderer', 'lighting', 'Physical Materials', 'Film director', 'Camera Lens', 'Rare hairstyle', 'Rare hairstyle man', 'Rare Colors', 'Artist', 'Art style2', 'Lens', 'Magic Elements']`
  - Options: `{{'default': 'None'}}`
- `weight1` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Custom_Type2` (optional): `['None', 'Sky', 'Indoor', 'Outdoor', 'Building', 'Flowers', 'Graphic effects', 'Image type', 'Coding method', 'Composition Method', 'Art style', 'Background', 'Color', 'Art unconventional', 'Perspective', 'Upper body decoration', 'Lower body decoration', 'Character in the work', 'Full body decoration', 'Action', 'Hair', 'Head accessories', 'Positioning', 'Type', 'Ears', 'Neck', 'Clothing', 'Face', 'Shoes and socks', 'Items', 'Food', 'Negative prompt word', 'Positive prompt word', 'Theme', 'Character Lens', 'Light perception', 'Twelve Constellations', 'Printing Materials', 'Scene Atmosphere', 'Architect', 'Illustration style', 'Renderer', 'lighting', 'Physical Materials', 'Film director', 'Camera Lens', 'Rare hairstyle', 'Rare hairstyle man', 'Rare Colors', 'Artist', 'Art style2', 'Lens', 'Magic Elements']`
  - Options: `{{'default': 'None'}}`
- `weight2` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Custom_Type3` (optional): `['None', 'Sky', 'Indoor', 'Outdoor', 'Building', 'Flowers', 'Graphic effects', 'Image type', 'Coding method', 'Composition Method', 'Art style', 'Background', 'Color', 'Art unconventional', 'Perspective', 'Upper body decoration', 'Lower body decoration', 'Character in the work', 'Full body decoration', 'Action', 'Hair', 'Head accessories', 'Positioning', 'Type', 'Ears', 'Neck', 'Clothing', 'Face', 'Shoes and socks', 'Items', 'Food', 'Negative prompt word', 'Positive prompt word', 'Theme', 'Character Lens', 'Light perception', 'Twelve Constellations', 'Printing Materials', 'Scene Atmosphere', 'Architect', 'Illustration style', 'Renderer', 'lighting', 'Physical Materials', 'Film director', 'Camera Lens', 'Rare hairstyle', 'Rare hairstyle man', 'Rare Colors', 'Artist', 'Art style2', 'Lens', 'Magic Elements']`
  - Options: `{{'default': 'None'}}`
- `weight3` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Custom_Type4` (optional): `['None', 'Sky', 'Indoor', 'Outdoor', 'Building', 'Flowers', 'Graphic effects', 'Image type', 'Coding method', 'Composition Method', 'Art style', 'Background', 'Color', 'Art unconventional', 'Perspective', 'Upper body decoration', 'Lower body decoration', 'Character in the work', 'Full body decoration', 'Action', 'Hair', 'Head accessories', 'Positioning', 'Type', 'Ears', 'Neck', 'Clothing', 'Face', 'Shoes and socks', 'Items', 'Food', 'Negative prompt word', 'Positive prompt word', 'Theme', 'Character Lens', 'Light perception', 'Twelve Constellations', 'Printing Materials', 'Scene Atmosphere', 'Architect', 'Illustration style', 'Renderer', 'lighting', 'Physical Materials', 'Film director', 'Camera Lens', 'Rare hairstyle', 'Rare hairstyle man', 'Rare Colors', 'Artist', 'Art style2', 'Lens', 'Magic Elements']`
  - Options: `{{'default': 'None'}}`
- `weight4` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `Custom_Type5` (optional): `['None', 'Sky', 'Indoor', 'Outdoor', 'Building', 'Flowers', 'Graphic effects', 'Image type', 'Coding method', 'Composition Method', 'Art style', 'Background', 'Color', 'Art unconventional', 'Perspective', 'Upper body decoration', 'Lower body decoration', 'Character in the work', 'Full body decoration', 'Action', 'Hair', 'Head accessories', 'Positioning', 'Type', 'Ears', 'Neck', 'Clothing', 'Face', 'Shoes and socks', 'Items', 'Food', 'Negative prompt word', 'Positive prompt word', 'Theme', 'Character Lens', 'Light perception', 'Twelve Constellations', 'Printing Materials', 'Scene Atmosphere', 'Architect', 'Illustration style', 'Renderer', 'lighting', 'Physical Materials', 'Film director', 'Camera Lens', 'Rare hairstyle', 'Rare hairstyle man', 'Rare Colors', 'Artist', 'Art style2', 'Lens', 'Magic Elements']`
  - Options: `{{'default': 'None'}}`
- `weight5` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'max': 2, 'step': 0.1, 'display': 'slider'}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `prompt`: `STRING`

## 2🐕/🔍REFINEMENT PROCESSING


### Applicability

**Score:** 81/100

**Reason:** This node generates a random prompt which is essential for text-to-image generation with LoRA model support.

### Metadata

---

### 2🐕Cropping image mask areas (`ER_TX_ZZCJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `original_image` (required): `IMAGE`
- `original_mask` (required): `MASK`
- `Up` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `Down` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `Left` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `Right` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0}}`

#### Outputs

- `cropped_image`: `IMAGE`
- `cropped_mask`: `MASK`
- `Crop_data`: `COORDS`

## 2🐕/🔖WATERMARK ADDITION


### Applicability

**Score:** 61/100

**Reason:** This node crops an image mask area which is moderately useful for text-to-image generation with LoRA model support as it can be used to refine the generated image.

### Metadata

---

### 2🐕Text watermark addition (`EG-YSZT-ZT`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 20000}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 20000}}`
- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'Please enter the watermark text that needs to be generated. The fonts in this plugin are all publicly available online resources and are for learning and communication purposes only. If you need a commercial font, please replace it yourself. The font storage path is in the Comfyui ergouzi DGNJD \\ fonts folder. For more SD tutorials, please refer to theB站@灵仙儿和二狗子🐕'}}`
- `Font` (required): `['优设标题黑.ttf']`
- `Font_size` (required): `INT`
  - Options: `{{'default': 50, 'min': 1, 'max': 1024}}`
- `Font_color` (required): `['custom', 'white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple', 'pink', 'brown', 'gray', 'lightgray', 'darkgray', 'olive', 'lime', 'teal', 'navy', 'maroon', 'fuchsia', 'aqua', 'silver', 'gold', 'turquoise', 'lavender', 'violet', 'coral', 'indigo']`
- `Background_color` (required): `['custom', 'white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple', 'pink', 'brown', 'gray', 'lightgray', 'darkgray', 'olive', 'lime', 'teal', 'navy', 'maroon', 'fuchsia', 'aqua', 'silver', 'gold', 'turquoise', 'lavender', 'violet', 'coral', 'indigo']`
- `Vertical_position` (required): `['Centered', 'Up', 'Down']`
- `Horizontal_position` (required): `['Centered', 'Left', 'Right']`
- `Text_margin` (required): `INT`
  - Options: `{{'default': 0, 'min': -1024, 'max': 1024}}`
- `Row_spacing` (required): `INT`
  - Options: `{{'default': 0, 'min': -1024, 'max': 1024}}`
- `X_offset` (required): `INT`
  - Options: `{{'default': 0, 'min': -20000, 'max': 20000}}`
- `Y_offset` (required): `INT`
  - Options: `{{'default': 0, 'min': -20000, 'max': 20000}}`
- `Rotate` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}}`
- `Rotation_center` (required): `['Center_by_Text', 'Center_by_Image']`
- `Font_transparency` (required): `INT`
  - Options: `{{'default': 255, 'min': 0, 'max': 255, 'display': 'slider'}}`
- `Font_colour_Hexadecimal` (optional): `STRING`
  - Options: `{{'multiline': False, 'default': '#000000'}}`
- `Background_colour_Hexadecimal` (optional): `STRING`
  - Options: `{{'multiline': False, 'default': '#000000'}}`
- `image` (optional): `IMAGE`

#### Outputs

- `Output_Image`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node adds a watermark to an image which is essential for text-to-image generation with LoRA model support as it allows users to add custom watermarks to their generated images.

### Metadata

---

### 2🐕Int Float Text Swap (`EG_SS_RYZH`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `Any_input` (required): `*`

#### Outputs

- `Int`: `*`
- `Float`: `*`
- `Text`: `*`


### Applicability

**Score:** 80/100

**Reason:** This node can swap integer, float, and text inputs which are useful in text to image generation workflows.

### Metadata

---

### 2🐕+-x÷ (`EG_SZ_JDYS`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `number1` (required): `STRING`
  - Options: `{{'multiline': True, 'default': ''}}`
- `operation` (required): `['+', '-', 'x', '÷']`
- `number2` (required): `STRING`
  - Options: `{{'multiline': True, 'default': ''}}`

#### Outputs

- `result_int`: `INT`
- `result_float`: `FLOAT`
- `result_str`: `STRING`

## 2🐕/🖼️IMAGE


### Applicability

**Score:** 60/100

**Reason:** This node performs basic arithmetic operations which might be useful in certain text to image generation tasks but is not directly related to the workflow goal.

### Metadata

---

### 2🐕Load any image (`EG_TX_JZRY`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `file_path` (required): `STRING`
- `fill_color` (required): `['None', 'white', 'gray', 'black']`
- `smooth` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 80/100

**Reason:** This node loads any image from a file path which is essential for text to image generation with LoRA model support.

### Metadata

---

### 2🐕Specify image save path (`EG_TX_LJBC`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `images` (required): `IMAGE`
- `filename_prefix` (required): `STRING`
  - Options: `{{'default': 'ComfyUI'}}`
- `custom_output_dir` (required): `STRING`
  - Options: `{{'default': '', 'optional': True}}`


### Applicability

**Score:** 40/100

**Reason:** This node specifies an output directory for saving images but does not directly contribute to the workflow goal of generating images with LoRA models.

### Metadata

---

### 2🐕Color adjustment (`EG_HT_YSTZ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `image` (required): `IMAGE`
- `temperature` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -100, 'max': 100, 'step': 100, 'precision': 5, 'display': 'slider'}}`
- `hue` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -90, 'max': 90, 'step': 5, 'precision': 180, 'display': 'slider'}}`
- `brightness` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -100, 'max': 100, 'step': 5, 'precision': 200, 'display': 'slider'}}`
- `contrast` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -100, 'max': 100, 'step': 5, 'precision': 200, 'display': 'slider'}}`
- `saturation` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -100, 'max': 100, 'step': 5, 'precision': 200, 'display': 'slider'}}`
- `gamma` (required): `INT`
  - Options: `{{'default': 1, 'min': -0.2, 'max': 2.2, 'step': 0.1, 'precision': 200, 'display': 'slider'}}`
- `blur` (required): `INT`
  - Options: `{{'default': 0, 'min': -200, 'max': 200, 'step': 1, 'precision': 200, 'display': 'slider'}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 80/100

**Reason:** This node provides color adjustment features that can be useful for fine-tuning the generated images.

### Metadata

---

### 2🐕Conventional filters (`EG_TX_LJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `image` (required): `IMAGE`
- `filter_type` (required): `['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'GaussianBlur', 'MaxFilter', 'MedianFilter', 'MinFilter', 'ModeFilter', 'SHARPEN', 'SMOOTH', 'SMOOTH_MORE', 'UnsharpMask']`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** This node applies conventional filters but may not directly contribute to the workflow goal of text to image generation with LoRA model support.

### Metadata

---

### 2🐕Text random splicing (`EG_SJPJ_Node`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `text1` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text2` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text3` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text4` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text5` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `Splicing_Characters` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `Exclude_Characters` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `Exclude_words` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': -1125899906842624, 'max': 1125899906842624}}`

#### Outputs

- `concatenated_text`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node allows for random splicing of text which can be useful in generating diverse and creative input texts for image generation models.

### Metadata

---

### 2🐕Text arbitrary splicing (`EG_TC_Node`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `text1` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text2` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text3` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text4` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `text5` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `Splicing_Characters` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `Exclude_Characters` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `Exclude_words` (optional): `STRING`
  - Options: `{{'default': ''}}`

#### Outputs

- `concatenated_text`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** Similar to Node 3, this node enables arbitrary text splicing which can aid in generating varied input texts for the workflow goal.

### Metadata

---

### 2🐕Proportional empty Latent (`EG_K_LATENT`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 8}}`
- `ratio` (required): `['1:1', '3:2', '16:9', '2:3', '9:16']`
  - Options: `{{'default': '1:1'}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`
- `equal_scale` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `LATENT`: `LATENT`
- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for text to image generation with LoRA model support as it allows users to specify the latent space dimensions (width, height, ratio), batch size, and equal scale, which are essential parameters for this workflow.

### Metadata

---

### DALL-E 3 Generator (`DallE3_PoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `prompt` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`
- `image_size` (required): `['1792x1024', '1024x1024', '1024x1792']`
- `image_quality` (required): `['standard', 'hd']`
- `style` (required): `['vivid', 'natural']`
  - Options: `{{'default': 'natural'}}`

#### Outputs

- `IMAGE`: `IMAGE`

## ART/STYLES


### Applicability

**Score:** 100/100

**Reason:** This node is directly responsible for generating images based on input prompts using a LoRA model.

### Metadata

---

### 🖼️ Isulion Art Style Generator (`IsulionArtStyleGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 999999999}}`
- `style` (required): `['Realistic', 'Watercolor', 'Oil Painting', 'Sketch', 'Digital Art', 'Impressionism', 'Expressionism', 'Surrealism', 'Pop Art', 'Abstract', 'Minimalist', 'Comic Book', 'Manga', 'Anime', 'Pixel Art', 'Vector Art', 'Low Poly', '3D Rendering', 'Concept Art', 'Fantasy Art', 'Gothic', 'Baroque', 'Renaissance', 'Art Nouveau', 'Art Deco', 'Cubism', 'Pointillism', 'Photorealism', 'Hyperrealism', 'Naive Art', 'Folk Art', 'Street Art', 'Graffiti', 'Retro', 'Vintage', 'Steampunk', 'Cyberpunk', 'Vaporwave', 'Ukiyo-e', 'Chinese Painting']`

#### Outputs

- `style`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 80/100

**Reason:** This node generates art styles that can be used in conjunction with the DALL-E 3 Generator for diverse image generation.

### Metadata

---

### 😊 Isulion Emotion Generator (`IsulionEmotionGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 999999999}}`
- `emotion` (required): `['Happy', 'Sad', 'Angry', 'Excited', 'Nervous', 'Calm', 'Peaceful', 'Anxious', 'Joyful', 'Melancholic', 'Furious', 'Cheerful', 'Depressed', 'Enthusiastic', 'Frustrated', 'Content', 'Worried', 'Serene', 'Irritated', 'Ecstatic', 'Gloomy', 'Relaxed', 'Stressed', 'Satisfied', 'Disappointed', 'Proud', 'Scared', 'Confident', 'Shy', 'Jealous', 'Grateful', 'Lonely', 'Loved', 'Confused', 'Determined', 'Hopeful', 'Tired', 'Energetic', 'Bored', 'Surprised', 'Curious', 'Embarrassed', 'Guilty', 'Relief', 'Nostalgic']`

#### Outputs

- `prompt`: `STRING`
- `emotion`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 90/100

**Reason:** This node generates a prompt based on an emotion, which can be useful for text-to-image generation with LoRA model support by providing a specific and detailed description of the image to generate.

### Metadata

---

### 🌅 Isulion Time of Day Generator (`IsulionTimeOfDayGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 999999999}}`
- `time` (required): `['Dawn', 'Sunrise', 'Early Morning', 'Morning', 'Late Morning', 'Noon', 'Early Afternoon', 'Afternoon', 'Late Afternoon', 'Golden Hour', 'Sunset', 'Dusk', 'Twilight', 'Evening', 'Night', 'Midnight', 'Blue Hour', 'First Light', 'Magic Hour', 'Civil Twilight', 'Astronomical Twilight', 'Nautical Twilight', 'Witching Hour', 'Pre-dawn', 'Post-sunset']`

#### Outputs

- `time`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 80/100

**Reason:** This node generates a time of day, which can be useful for text-to-image generation with LoRA model support by providing a specific and detailed description of the lighting conditions in the image to generate.

### Metadata

---

### LoadEmbedding (`LoadEmbedding`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`
- `embedding` (required): `[[]]`
- `weight` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': -2, 'max': 2, 'step': 0.1, 'round': 0.01}}`

#### Outputs

- `text`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node loads embeddings which can be used in text-to-image generation with LoRA model support.

### Metadata

---

### Loader (`Loader`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `Checkpoint` (required): `['1-5\\dreamshaper_8.safetensors', 'hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors', 'ltx-video-2b-v0.9.safetensors', 'xl\\irisLuxPolyvalentPrototype_v1051VAEIncluded.safetensors', 'xl\\juggernautXL_v7Rundiffusion.safetensors', 'xl\\realismEngineSDXL_v20VAE.safetensors', 'xl\\sd_xl_base_1.0.safetensors', 'xl\\sd_xl_refiner_1.0.safetensors', 'xl\\sdxxxl_v30.safetensors']`
- `Vae` (required): `['Included', 'hunyuan_video_vae_bf16.safetensors']`
- `stop_at_clip_layer` (required): `INT`
  - Options: `{{'default': -1, 'min': -24, 'max': -1, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 32768, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 32768, 'step': 8}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`

#### Outputs

- `MODEL`: `MODEL`
- `VAE`: `VAE`
- `CLIP`: `CLIP`
- `LATENT`: `LATENT`


### Applicability

**Score:** 95/100

**Reason:** This node loads a pre-trained model for text-to-image generation with LoRA model support.

### Metadata

---

### Prompts (`Prompts`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `Positive` (required): `STRING`
  - Options: `{{'default': 'Positive Prompt', 'multiline': True}}`
- `Negative` (required): `STRING`
  - Options: `{{'default': 'Negative Prompt', 'multiline': True}}`
- `clip` (optional): `CLIP`

#### Outputs

- `Positive CONDITIONING`: `CONDITIONING`
- `Negative CONDITIONING`: `CONDITIONING`
- `CLIP`: `CLIP`
- `Positive text`: `STRING`
- `Negative text`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node generates prompts but does not directly contribute to text-to-image generation with LoRA model support.

### Metadata

---

### SaveImages (`SaveImages`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `filename_type` (required): `['Timestamp', 'Fixed', 'Fixed Single']`
- `fixed_filename` (required): `STRING`
  - Options: `{{'default': 'output'}}`
- `images` (optional): `IMAGE`
- `latents` (optional): `LATENT`
- `vae` (optional): `VAE`
- `fixed_filename_override` (optional): `STRING`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `images`: `IMAGE`
- `filename_list`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for saving generated images in the text to image generation with LoRA model support workflow.

### Metadata

---

### SimpleSampler (`SimpleSampler`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `model` (required): `MODEL`
- `sampler` (required): `['Normal - euler', 'Normal - uni_pc', 'LCM Lora - lcm', 'SDXL Turbo - dpmpp_sde karras']`
- `positive` (required): `CONDITIONING`
- `negative` (required): `CONDITIONING`
- `latents` (required): `LATENT`
- `mode` (required): `['txt2img', 'img2img']`
- `seed` (optional): `INT`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful as a sampler for generating latents in the text to image generation with LoRA model support workflow.

### Metadata

---

### ImageAddText (`ImageAddText`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'default': 'Chibi-Nodes', 'multiline': True}}`
- `font` (required): `[['Ubuntu-Bold.ttf', 'Ubuntu-BoldItalic.ttf', 'Ubuntu-Italic.ttf', 'Ubuntu-Light.ttf', 'Ubuntu-LightItalic.ttf', 'Ubuntu-Medium.ttf', 'Ubuntu-MediumItalic.ttf', 'Ubuntu-Regular.ttf', 'UbuntuCondensed-Regular.ttf', 'UbuntuMono-Bold.ttf', 'UbuntuMono-BoldItalic.ttf', 'UbuntuMono-Italic.ttf', 'UbuntuMono-Regular.ttf']]`
- `font_size` (required): `INT`
  - Options: `{{'default': 24, 'min': 0, 'max': 200, 'step': 1}}`
- `font_colour` (required): `['black', 'white', 'red', 'green', 'blue']`
- `invert_mask` (required): `[False, True]`
- `position_x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 32768, 'step': 1}}`
- `position_y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 32768, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 32768, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 32768, 'step': 1}}`
- `image` (optional): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`
- `text`: `STRING`


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful for adding text to images in the text to image generation with LoRA model support workflow, but its primary function is not directly related to the main task.

### Metadata

---

### ImageSimpleResize (`ImageSimpleResize`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `image` (required): `IMAGE`
- `size` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 32768, 'step': 1}}`
- `edge` (required): `['largest', 'smallest', 'all', 'width', 'height']`
- `size_override` (optional): `INT`
  - Options: `{{'forceInput': True}}`
- `vae` (optional): `VAE`

#### Outputs

- `IMAGE`: `IMAGE`
- `LATENT`: `LATENT`


### Applicability

**Score:** 41/100

**Reason:** Resizes images but doesn"t directly support LoRA models or text to image generation.

### Metadata

---

### ImageSizeInfo (`ImageSizeInfo`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `image` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`
- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 81/100

**Reason:** Provides essential information about an image"s width and height for the workflow goal.

### Metadata

---

### LoadImageExtended (`LoadImageExtended`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `image` (required): `['example.png', 'pond_girl1.png', 'pond_girl2.png', 'pond_girl3.png']`
  - Options: `{{'image_upload': True}}`
- `vae` (optional): `VAE`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`
- `LATENT`: `LATENT`
- `filename`: `STRING`
- `image Info`: `STRING`
- `width`: `INT`
- `height`: `INT`

## CHIBI-NODES/NUMBERS


### Applicability

**Score:** 61/100

**Reason:** Loads images from a list or upload, providing necessary input for the workflow goal, but also outputs additional information not directly required.

### Metadata

---

### SeedGenerator (`SeedGenerator`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `mode` (required): `['Random', 'Fixed']`
- `fixed_seed` (required): `INT`
  - Options: `{{'default': 8008135, 'min': 0, 'max': 18446744073709551615, 'step': 1}}`

#### Outputs

- `seed`: `INT`
- `text`: `STRING`

## CHIBI-NODES/TEXT


### Applicability

**Score:** 100/100

**Reason:** This node provides a fixed seed for reproducibility and consistency in the workflow, which is essential for text-to-image generation with LoRA model support.

### Metadata

---

### Random (`DF_Random`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value_A` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `Value_B` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4294967295, 'step': 1, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`

## DERFUU_NODES/FUNCTIONS/CONVERTERS


### Applicability

**Score:** 80/100

**Reason:** This random number generator could be used for various tasks such as sampling or initialization in the text to image generation process.

### Metadata

---

### Search In Text (`DF_Search_In_Text`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`
- `Pattern` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`
- `ConsiderRegister` (required): `BOOLEAN`
  - Options: `{{'default': False, 'force': False}}`
- `Mode` (required): `['Strict', 'RegEx']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `BOOLEAN`: `BOOLEAN`
- `OCCURRENCES`: `INT`


### Applicability

**Score:** 60/100

**Reason:** Search In Text can be moderately useful for searching specific patterns within text inputs used in the workflow, but its relevance is somewhat indirect.

### Metadata

---

### Square root (`DF_Square_root`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `FLOAT`: `FLOAT`


### Applicability

**Score:** 80/100

**Reason:** This node can be used as a supporting node to normalize input values for the LoRA model.

### Metadata

---

### Subtract (`DF_Subtract`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value_A` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `Value_B` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 40/100

**Reason:** This node can be used as a supporting node to subtract one value from another in text-to-image generation with LoRA model support, but it is not directly relevant.

### Metadata

---

### Sum (`DF_Sum`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value_A` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `Value_B` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`

## DERFUU_NODES/MATH/TRIGONOMETRY


### Applicability

**Score:** 40/100

**Reason:** This node can be used as a supporting node to sum two values together in text-to-image generation with LoRA model support, but it is not directly relevant.

### Metadata

---

### Image scale by ratio (`DF_Image_scale_by_ratio`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `image` (required): `IMAGE`
  - Options: `{{'forceInput': False}}`
- `upscale_by` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'bicubic', 'bislerp', 'area', 'lanczos']`
  - Options: `{{'forceInput': False}}`
- `crop` (required): `['disabled', 'center']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for scaling images to a desired ratio, which is necessary for text-to-image generation.

### Metadata

---

### Image scale to side (`DF_Image_scale_to_side`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `image` (required): `IMAGE`
  - Options: `{{'forceInput': False}}`
- `side_length` (required): `INT`
  - Options: `{{'default': 1, 'min': -9223372036854775807, 'max': 9223372036854775807, 'step': 1, 'forceInput': False}}`
- `side` (required): `['Longest', 'Shortest', 'Width', 'Height']`
  - Options: `{{'forceInput': False}}`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'bicubic', 'bislerp', 'area', 'lanczos']`
  - Options: `{{'forceInput': False}}`
- `crop` (required): `['disabled', 'center']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `IMAGE`: `IMAGE`

## DERFUU_NODES/MODDED NODES/LATENT


### Applicability

**Score:** 91/100

**Reason:** This node is very useful for scaling images to a specific side length, allowing for more precise control over the output image.

### Metadata

---

### Latent Scale by ratio (`DF_Latent_Scale_by_ratio`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `latent` (required): `LATENT`
  - Options: `{{'forceInput': False}}`
- `modifier` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': 0, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `scale_method` (required): `['nearest-exact', 'bilinear', 'bicubic', 'bislerp', 'area', 'lanczos']`
  - Options: `{{'forceInput': False}}`
- `crop` (required): `['disabled', 'center']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 61/100

**Reason:** This node can be moderately useful for scaling latent vectors by ratio, but its utility depends on the specific requirements of the workflow.

### Metadata

---

### Latent Scale to side (`DF_Latent_Scale_to_side`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `latent` (required): `LATENT`
  - Options: `{{'forceInput': False}}`
- `side_length` (required): `INT`
  - Options: `{{'default': 512, 'min': -9223372036854775807, 'max': 9223372036854775807, 'step': 1, 'forceInput': False}}`
- `side` (required): `['Longest', 'Shortest', 'Width', 'Height']`
  - Options: `{{'forceInput': False}}`
- `scale_method` (required): `['nearest-exact', 'bilinear', 'bicubic', 'bislerp', 'area', 'lanczos']`
  - Options: `{{'forceInput': False}}`
- `crop` (required): `['disabled', 'center']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `LATENT`: `LATENT`

## DERFUU_NODES/VARIABLES


### Applicability

**Score:** 81/100

**Reason:** This node is essential for scaling latent vectors to a specific side length, which is necessary for text-to-image generation with LoRA model support.

### Metadata

---

### Text (`DF_Text`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it provides a static text input which can be used to generate images based on the provided text.

### Metadata

---

### Text Box (`DF_Text_Box`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True, 'forceInput': False, 'dynamicPrompts': False}}`

#### Outputs

- `STRING`: `STRING`

## FIZZNODES 📅🅕🅝/BATCHSCHEDULENODES


### Applicability

**Score:** 81/100

**Reason:** This node is essential for providing a text input to the workflow, which is necessary for text-to-image generation.

### Metadata

---

### Batch Prompt Schedule 📅🅕🅝 (`BatchPromptSchedule`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '"0" :"",\n"11" :"",\n"23" :"",\n"35" :"",\n"47" :"",\n"59" :"",\n"71" :"",\n"83" :"",\n"95" :"",\n"107" :"",\n"119" :""\n'}}`
- `clip` (required): `CLIP`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `start_frame` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'start_frame(print_only)'}}`
- `end_frame` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'end_frame(print_only)'}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`


### Applicability

**Score:** 99/100

**Reason:** This node is very useful as it allows scheduling of prompts and can be used to generate multiple images with different conditions.

### Metadata

---

### Batch Prompt Schedule SDXL 📅🅕🅝 (`BatchPromptScheduleEncodeSDXL`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `crop_w` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `crop_h` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `target_width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `target_height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `text_g` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `clip` (required): `CLIP`
- `text_l` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pre_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `start_frame` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'start_frame(print_only)'}}`
- `end_frame` (optional): `INT`
  - Options: `{{'default': 120, 'min': 0, 'max': 9999, 'step': 1, 'display': 'end_frame(print_only)'}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`


### Applicability

**Score:** 91/100

**Reason:** Similar to Node 2, this node is also very useful for scheduling prompts but has additional features such as support for SDXL encoding.

### Metadata

---

### Batch Prompt Schedule (Latent Input) 📅🅕🅝 (`BatchPromptScheduleLatentInput`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '"0" :"",\n"11" :"",\n"23" :"",\n"35" :"",\n"47" :"",\n"59" :"",\n"71" :"",\n"83" :"",\n"95" :"",\n"107" :"",\n"119" :""\n'}}`
- `clip` (required): `CLIP`
- `num_latents` (required): `LATENT`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `start_frame` (optional): `INT`
  - Options: `{{'default': 0.0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'start_frame(print_only)'}}`
- `end_frame` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'end_frame(print_only)'}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`
- `INPUT_LATENTS`: `LATENT`


### Applicability

**Score:** 98/100

**Reason:** This node is very useful as it allows the input of latent vectors and can be used to generate multiple images with different conditions.

### Metadata

---

### Batch Prompt Schedule SDXL (Latent Input) 📅🅕🅝 (`BatchPromptScheduleSDXLLatentInput`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `crop_w` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `crop_h` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `target_width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `target_height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `text_g` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `clip` (required): `CLIP`
- `text_l` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `num_latents` (required): `LATENT`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pre_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `start_frame` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 9999, 'step': 1, 'display': 'start_frame(print_only)'}}`
- `end_frame` (optional): `INT`
  - Options: `{{'default': 120, 'min': 0, 'max': 9999, 'step': 1, 'display': 'end_frame(print_only)'}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`
- `INPUT_LATENTS`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for text to image generation with LoRA model support as it allows scheduling of prompts, which is a crucial step in generating high-quality images.

### Metadata

---

### Batch Value Schedule (Latent Input) 📅🅕🅝 (`BatchValueScheduleLatentInput`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '0:(0),\n11:(0),\n23:(0),\n35:(0),\n47:(0),\n59:(0),\n71:(0),\n83:(0),\n95:(0),\n107:(0),\n119:(0)\n'}}`
- `num_latents` (required): `LATENT`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`
- `LATENT`: `LATENT`

## FIZZNODES 📅🅕🅝/FRAMENODES


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for text to image generation with LoRA model support as it allows scheduling of values with latent input, which can be used in conjunction with other nodes to achieve the workflow goal.

### Metadata

---

### Node Frame 📅🅕🅝 (`FizzFrame`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `frame` (required): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `previous_frame` (required): `FIZZFRAME`
  - Options: `{{'forceInput': True}}`
- `positive_text` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `negative_text` (optional): `STRING`
  - Options: `{{'multiline': True}}`

#### Outputs

- `FIZZFRAME`: `FIZZFRAME`
- `POS_COND`: `CONDITIONING`
- `NEG_COND`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential as it allows users to input positive and negative text which are crucial for generating images with LoRA model support.

### Metadata

---

### Frame Concatenate 📅🅕🅝 (`FizzFrameConcatenate`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `frame` (required): `FIZZFRAME`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 41/100

**Reason:** This node has some utility but its primary function of concatenating frames does not directly contribute to the workflow goal. It could be useful in a supporting role.

### Metadata

---

### Init Node Frame 📅🅕🅝 (`Init FizzFrame`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `frame` (required): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `positive_text` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `negative_text` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `general_positive` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `general_negative` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `previous_frame` (optional): `FIZZFRAME`
  - Options: `{{'forceInput': True}}`
- `clip` (optional): `CLIP`

#### Outputs

- `FIZZFRAME`: `FIZZFRAME`
- `POS_COND`: `CONDITIONING`
- `NEG_COND`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** Similar to Node 1, this node is essential as it provides users with options for inputting text and frame information which are necessary for generating images with LoRA model support.

### Metadata

---

### Concat String (Single) 📅🅕🅝 (`ConcatStringSingle`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `string_a` (required): `STRING`
  - Options: `{{'forceInput': True, 'default': '', 'multiline': True}}`
- `string_b` (required): `STRING`
  - Options: `{{'forceInput': True, 'default': '', 'multiline': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** Concatenates two strings which can be useful for combining input text or other metadata in the workflow.

### Metadata

---

### Image Select Schedule 📅🅕🅝 (`ImagesFromBatchSchedule`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `images` (required): `IMAGE`
- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '"0" :"",\n"11" :"",\n"23" :"",\n"35" :"",\n"47" :"",\n"59" :"",\n"71" :"",\n"83" :"",\n"95" :"",\n"107" :"",\n"119" :""\n'}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 70/100

**Reason:** Selects images based on a schedule which can be useful for generating images at specific frames or intervals in the workflow.

### Metadata

---

### Prompt Schedule 📅🅕🅝 (`PromptSchedule`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '"0" :"",\n"11" :"",\n"23" :"",\n"35" :"",\n"47" :"",\n"59" :"",\n"71" :"",\n"83" :"",\n"95" :"",\n"107" :"",\n"119" :""\n'}}`
- `clip` (required): `CLIP`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0, 'forceInput': True}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for scheduling prompts in a text to image generation workflow with LoRA model support.

### Metadata

---

### Prompt Schedule SDXL 📅🅕🅝 (`PromptScheduleEncodeSDXL`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `crop_w` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `crop_h` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 8192}}`
- `target_width` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `target_height` (required): `INT`
  - Options: `{{'default': 1024.0, 'min': 0, 'max': 8192}}`
- `text_g` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `clip` (required): `CLIP`
- `text_l` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `pre_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_G` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pre_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text_L` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`


### Applicability

**Score:** 91/100

**Reason:** This node is very useful as it allows for encoding SDXL and scheduling prompts in a text to image generation workflow with LoRA model support.

### Metadata

---

### Prompt Schedule NodeFlow 📅🅕🅝 (`PromptScheduleNodeFlow`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `num_frames` (required): `INT`
  - Options: `{{'default': 24.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `in_text` (optional): `STRING`
  - Options: `{{'multiline': False}}`
- `max_frames` (optional): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}}`

#### Outputs

- `INT`: `INT`
- `STRING`: `STRING`


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful as it provides an alternative prompt schedule but lacks specific features for LoRA model support.

### Metadata

---

### Prompt Schedule NodeFlow End 📅🅕🅝 (`PromptScheduleNodeFlowEnd`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': False, 'forceInput': True}}`
- `clip` (required): `CLIP`
- `max_frames` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0, 'forceInput': True}}`
- `pre_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `app_text` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `pw_a` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_b` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_c` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`
- `pw_d` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1, 'forceInput': True}}`

#### Outputs

- `POS`: `CONDITIONING`
- `NEG`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for scheduling prompts and ending the workflow in a text to image generation with LoRA model support.

### Metadata

---

### SquareWave 📅🅕🅝 (`SquareWave`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `phase` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `amplitude` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}}`
- `x_translation` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `y_translation` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node generates a square wave, similar to the sine and sawtooth waves. Its utility is also limited in this workflow.

### Metadata

---

### Hugging Face Download🤗 (`IF_HFDownloadNode`)

**Description:**

**Module:** `ComfyUI-IF_AI_HFDownloaderNode`

#### Inputs

- `repo_id` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `file_paths` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'comma-separated list of files or leave empty for all'}}`
- `folder_path` (required): `STRING`
  - Options: `{{'multiline': False, 'default': '/path/to/download/folder'}}`
- `comfy_paths` (required): `['none', 'animatediff_models', 'animatediff_motion_lora', 'animatediff_video_formats', 'blip', 'checkpoints', 'classifiers', 'clip', 'clip_vision', 'CogVideo', 'configs', 'controlnet', 'control-lora', 'deforum', 'diffusers', 'diffusion_models', 'embeddings', 'emotion2vec', 'facedetection', 'FILM', 'gligen', 'hypernetworks', 'insightface', 'Joy_caption', 'layerstyle', 'liveportrait', 'LLM', 'loras', 'onnx', 'photomaker', 'style_models', 'unet', 'upscale_models', 'vae', 'vae_approx', 'wav2vec', 'xlabs']`
  - Options: `{{'default': 'none'}}`
- `exclude_files` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'comma-separated list to exclude'}}`
- `mode` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label_on': 'All Repo/Space', 'label_off': 'Individual Files'}}`
- `provided_token` (optional): `STRING`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`

## ISULION - MULTIPLE PROMPT GENERATOR


### Applicability

**Score:** 80/100

**Reason:** This node is essential for downloading LoRA model support, which is a crucial component of text-to-image generation.

### Metadata

---

### 👔 Isulion Clothing Generator (`IsulionClothingGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `clothing` (required): `['ornate robes', 'leather armor', 'silk dress', 'royal garments', "mage's cloak", "warrior's plate", "peasant's tunic", "noble's attire", 'dragon scale armor', 'elven silk robes', 'dwarven battle gear', "wizard's hat", 'enchanted cloak', 'mythril chainmail', "ranger's camouflage", "paladin's armor", "druid's vestments", "assassin's garb", 'ceremonial robes', 'battle mage armor', 'fairy gossamer dress', "necromancer's robes", 'barbarian furs', 'royal crown jewels', 'business suit', 'casual wear', 'formal dress', 'streetwear', 'sporty outfit', 'bohemian style', 'punk fashion', 'minimalist clothing', 'vintage dress', 'designer jeans', 'leather jacket', 'summer dress', 'athletic wear', 'cocktail dress', 'winter coat', 'beach wear', 'office attire', 'evening gown', 'urban streetwear', 'loungewear', 'hipster fashion', 'gothic style', 'preppy outfit', 'activewear', 'space suit', 'cybernetic armor', 'holographic clothing', 'neon bodysuit', 'power armor', 'anti-gravity boots', 'plasma shield wear', 'quantum fabric dress', 'cyborg enhancements', 'energy field suit', 'stealth camouflage', 'bio-luminescent wear', 'techno-organic suit', 'neural interface gear', 'phase shift clothing', 'zero-g suit']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `style` (optional): `['any', 'fantasy', 'modern', 'sci_fi']`
  - Options: `{{'default': 'any'}}`

#### Outputs

- `clothing`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 60/100

**Reason:** This node can generate clothing items that might be useful for a specific prompt in text-to-image generation, but its utility is limited compared to other nodes that directly contribute to the workflow goal.

### Metadata

---

### ⏳ Isulion Epoch Generator (`IsulionEpochGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `epoch` (required): `['Ancient Egypt', 'Ancient Greece', 'Roman Empire', 'Middle Ages', 'Renaissance', 'Industrial Revolution', 'Victorian Era', 'Roaring Twenties', 'Modern Era', 'Digital Age', 'Bronze Age', 'Iron Age', 'Stone Age', 'Byzantine Empire', 'Ming Dynasty', 'Edo Period', 'Colonial Period', 'Belle Époque', 'Art Deco Period', 'Space Age', 'Information Age', 'Medieval Japan', 'Viking Age', 'Golden Age of Piracy', 'Wild West', 'Prehistoric Times', 'Age of Enlightenment', 'Age of Exploration', 'Classical Antiquity', 'Dark Ages', 'Age of Discovery', 'Baroque Period', 'Gothic Era', 'Romantic Period', 'Jazz Age', 'Post-Modern Era', 'Cyberpunk Future', 'Steampunk Era']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`

#### Outputs

- `epoch`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node generates epochs or time periods, which may not be directly relevant to text-to-image generation with LoRA model support. However, it could potentially be used as a supporting node for generating prompts related to historical settings.

### Metadata

---

### IsulionMegaPromptV3 (`IsulionMegaPromptV3`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `theme` (required): `['🎲 Dynamic Random', '🧺 50s Commercial', '🎨 Abstract', '📺 Animation Cartoon', '🎌 Anime', '🏛️ Architectural', '🧬 Bio-Organic Technology', '🖼️ Binet Surreal', '😄 Caricature', '👤 Character Designer', '🦄 Chimera Animals', '🐰 Chimera Cute Animals', '🏮 Chinese New Year', '🎄 Christmas', '🎬 Cinema Studio', '🏺 Clay Art', '📚 Comic Book', '🎨 Concept Art', '🖍️ Crayon Art', '💎 Crystalpunk', '🍳 Culinary/Food', '👗 Curvy Fashion', '🌆 Cyberpunk', '👹 Dia de los Muertos', '💠 Dimension 3D', '🖼️ Digital Art', '🎡 Disney', '🎬 Dreamworks', '🐰 Easter', '✨ Enchanted Fantasy', '📸 Essential Realistic', '🕰️ Essential Vintage', '✨ Ethereal Dreams', '🔬 Experimental Art', '⚔️ Fantasy', '🌆 Futuristic City', '⚔️ Futuristic Battlefield', '🌆 Futuristic City Metropolis', '🚀 Futuristic Sci-Fi', '🍃 Ghibli', '🎃 Halloween', '👻 Halloween Ethereal', '👻 Horror', '🎨 Impressionist', '📱 Instagram', '📱 Instagram Lifestyle', '🏠 Interior Spaces', '🎯 Logo', '📺 Manga Panel', '🦸 Marvel', '🔬 Microscopic', '⬜ Minimalist', '⚔️ Miura Dark Fantasy', '🌿 Nature', "🎆 New Year's Eve", '🎬 Nolan Epic', '🕴️\u200d♂️ Peaky Blinders', '💫 Pixar', '🌪️ Post Apocalyptic', '🧩 Puzzle Dimension', '🚀 Sci-Fi', '📚 School Manga', '📱 Selfie', '💗 Spectral Mist', "🍀 St. Patrick's Day", '🚀 Star Wars', '⚙️ Steampunk', '🎭 Stop Motion', '🥙 Street Food Kebab', '🦃 Thanksgiving', '🌊 Underwater Civilization', '🏙️ Urban Tag', "💘 Valentine's Day", '🏠 Village World', '📸 Vintage 1800s Photography', '👴 Vintage Anthropomorphic', '🎨 Watercolor', '🏛️ Historical Monuments', '⚔️ Medieval']`
  - Options: `{{'default': '🎲 Dynamic Random'}}`
- `complexity` (required): `['simple', 'detailed', 'complex']`
  - Options: `{{'default': 'detailed'}}`
- `randomize` (required): `['enable', 'disable']`
  - Options: `{{'default': 'enable'}}`
- `debug_mode` (required): `['off', 'on']`
  - Options: `{{'default': 'off'}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `custom_subject` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`
- `custom_location` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`
- `include_environment` (optional): `['yes', 'no']`
  - Options: `{{'default': 'yes'}}`
- `include_style` (optional): `['yes', 'no']`
  - Options: `{{'default': 'yes'}}`
- `include_effects` (optional): `['yes', 'no']`
  - Options: `{{'default': 'yes'}}`

#### Outputs

- `prompt`: `STRING`
- `subject`: `STRING`
- `environment`: `STRING`
- `style`: `STRING`
- `effects`: `STRING`
- `seed`: `INT`

## ISULION/ENHANCEMENT


### Applicability

**Score:** 90/100

**Reason:** This node can generate complex and detailed prompts for text to image generation with various themes and styles, which is very useful for the specified workflow goal.

### Metadata

---

### 💫 Isulion Prompt Enhancer (`IsulionPromptEnhancer`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `base_prompt` (required): `STRING`
  - Options: `{{'default': ''}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `enhancement_level` (optional): `['subtle', 'moderate', 'dramatic']`
  - Options: `{{'default': 'moderate'}}`
- `focus` (optional): `['detail', 'mood', 'composition', 'lighting', 'color']`
  - Options: `{{'default': 'detail'}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node enhances the input prompt with various options to improve text-to-image generation quality.

### Metadata

---

### 🎨 Isulion Style Mixer (`IsulionStyleMixer`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `style1` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `style2` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `blend_mode` (required): `['balanced', 'style1_dominant', 'style2_dominant']`
  - Options: `{{'default': 'balanced'}}`

#### Outputs

- `STRING`: `STRING`

## ISULION/FANTASY


### Applicability

**Score:** 61/100

**Reason:** This node combines two styles to generate a new image based on the given styles and blend mode.

### Metadata

---

### ✨ Isulion Magical Effect Generator (`IsulionMagicalEffectGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `effect` (required): `['blazing aura', 'flame burst', 'phoenix wings', 'inferno vortex', 'frost crystals', 'blizzard swirl', 'arctic mist', 'frozen aura', 'crackling energy', 'thunder bolts', 'static field', 'plasma arc', 'vine growth', 'flower bloom', 'leaf storm', 'forest spirits', 'magical runes', 'mystic circles', 'astral projection', 'ethereal wisps']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `element` (optional): `['any', 'fire', 'ice', 'lightning', 'nature', 'arcane']`
  - Options: `{{'default': 'any'}}`

#### Outputs

- `effect`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 41/100

**Reason:** This node generates a magical effect (e.g., blazing aura or frost crystals) that could be used in conjunction with text-to-image generation, but its direct relevance is limited.

### Metadata

---

### 🖼️ Isulion Image Collage (`IsuCollage_Node`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `images` (required): `IMAGE`
- `seed` (required): `INT`
  - Options: `{{'optional': True}}`

#### Outputs

- `collage_image`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** This node can be used to generate a collage of images that can be used as input for the text-to-image generation process.

### Metadata

---

### 📁 Isulion Load Images from Directory (`IsulionLoadImagesNode`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `directory` (required): `STRING`
  - Options: `{{'default': './input'}}`
- `target_row_height` (required): `INT`
  - Options: `{{'default': 300, 'min': 100, 'max': 1024, 'step': 50}}`

#### Outputs

- `images`: `IMAGE`

## ISULION/PROMPT


### Applicability

**Score:** 41/100

**Reason:** This node can load multiple images from a directory, which can be useful if you need to generate multiple images at once.

### Metadata

---

### IsulionVideoPromptGenerator (`IsulionVideoPromptGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `preset` (required): `['None', 'Nature Documentary', 'Travel Vlog', 'Wedding Video', 'Music Video', 'News Report', 'Sports Coverage', 'Fashion Show', 'Food Review', 'Real Estate Tour', 'Product Commercial']`
  - Options: `{{'default': 'None', 'display': '📽️ Preset Scenario', 'description': 'Pre-configured video scenarios with professional settings'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `quality_level` (required): `['Standard', 'High Quality', 'Best Quality', 'Experimental', 'Raw Footage', 'Film', 'Broadcast']`
  - Options: `{{'default': 'Standard'}}`
- `custom_subject` (required): `STRING`
  - Options: `{{'default': ''}}`
- `custom_location` (required): `STRING`
  - Options: `{{'default': ''}}`
- `camera_angle` (required): `['None', 'Random', '((The camera remains stationary))', '((The camera pans slowly))', '((The camera follows the subject))', '((The camera zooms in gradually))', '((The camera circles around))', '((The camera moves from left to right))', '((The camera captures from a low angle))', '((The camera shoots from above))', '((The camera tracks backward))', '((The camera moves in for a close-up))', '((The camera glides smoothly))', '((The camera sweeps across))', '((The camera rises upward))', '((The camera descends slowly))', '((The camera spirals around))']`
  - Options: `{{'default': 'None'}}`
- `lighting` (required): `['None', 'Random', 'natural sunlight streams through windows', 'warm artificial lighting creates a cozy atmosphere', 'harsh fluorescent lights illuminate the space', 'soft ambient lighting fills the room', 'dramatic shadows create contrast', 'golden hour sunlight bathes the scene', 'moody low-key lighting', 'bright and even lighting', 'dappled light filtering through trees', 'cool blue evening light', 'misty morning light creates a dreamy atmosphere', 'dramatic storm clouds cast shifting shadows', 'moonlight casts a silvery glow', 'neon lights create vibrant color contrasts', 'candlelight flickers softly', 'sunrise paints the sky in pastel hues', 'sunset creates long dramatic shadows', 'starlight twinkles in the darkness', 'fog diffuses the light mysteriously', 'rainbow light refracts through crystal']`
  - Options: `{{'default': 'None'}}`
- `theme` (required): `['None', '🎲 Dynamic Random', '🧺 50s Commercial', '🎨 Abstract', '📺 Animation Cartoon', '🎌 Anime', '🏛️ Architectural', '🧬 Bio-Organic Technology', '🖼️ Binet Surreal', '😄 Caricature', '👤 Character Designer', '🦄 Chimera Animals', '🐰 Chimera Cute Animals', '🏮 Chinese New Year', '🎄 Christmas', '🎬 Cinema Studio', '🏺 Clay Art', '📚 Comic Book', '🎨 Concept Art', '🖍️ Crayon Art', '💎 Crystalpunk', '🍳 Culinary/Food', '👗 Curvy Fashion', '🌆 Cyberpunk', '👹 Dia de los Muertos', '💠 Dimension 3D', '🖼️ Digital Art', '🎡 Disney', '🎬 Dreamworks', '🐰 Easter', '✨ Enchanted Fantasy', '📸 Essential Realistic', '🕰️ Essential Vintage', '✨ Ethereal Dreams', '🔬 Experimental Art', '⚔️ Fantasy', '🌆 Futuristic City', '⚔️ Futuristic Battlefield', '🌆 Futuristic City Metropolis', '🚀 Futuristic Sci-Fi', '🍃 Ghibli', '🎃 Halloween', '👻 Halloween Ethereal', '👻 Horror', '🎨 Impressionist', '📱 Instagram', '📱 Instagram Lifestyle', '🏠 Interior Spaces', '🎯 Logo', '📺 Manga Panel', '🦸 Marvel', '🔬 Microscopic', '⬜ Minimalist', '⚔️ Miura Dark Fantasy', '🌿 Nature', "🎆 New Year's Eve", '🎬 Nolan Epic', '🕴️\u200d♂️ Peaky Blinders', '💫 Pixar', '🌪️ Post Apocalyptic', '🧩 Puzzle Dimension', '🚀 Sci-Fi', '📚 School Manga', '📱 Selfie', '💗 Spectral Mist', "🍀 St. Patrick's Day", '🚀 Star Wars', '⚙️ Steampunk', '🎭 Stop Motion', '🥙 Street Food Kebab', '🦃 Thanksgiving', '🌊 Underwater Civilization', '🏙️ Urban Tag', "💘 Valentine's Day", '🏠 Village World', '📸 Vintage 1800s Photography', '👴 Vintage Anthropomorphic', '🎨 Watercolor', '🏛️ Historical Monuments', '⚔️ Medieval']`
  - Options: `{{'default': 'None'}}`

#### Outputs

- `STRING`: `STRING`

## ISULION/PROMPT TOOLS


### Applicability

**Score:** 100/100

**Reason:** This node is directly relevant to generating video prompts for text-to-image generation with LoRA model support, and provides many options for customizing the prompt.

### Metadata

---

### 🖼️ Isulion Civitai Image Display (`IsulionCivitaiImageDisplay`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `image_info` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '', 'placeholder': 'Paste Civitai image information here...'}}`
- `mode` (required): `['Single', 'All']`
  - Options: `{{'default': 'Single'}}`
- `image_index` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'step': 1}}`
- `target_size` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 2048, 'step': 64}}`

#### Outputs

- `image`: `IMAGE`
- `title`: `STRING`
- `prompt`: `STRING`
- `image_url`: `STRING`
- `model`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for displaying generated images with LoRA model support.

### Metadata

---

### 👽 Isulion Alien World Generator (`IsulionAlienWorldGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `atmosphere` (required): `['toxic', 'breathable', 'dense', 'thin', 'crystalline', 'plasma', 'gaseous', 'corrosive', 'radioactive', 'electromagnetic', 'quantum', 'temporal', 'bio-organic', 'multi-phasic', 'energy-based']`
- `terrain` (required): `['crystalline desert', 'floating islands', 'metallic plains', 'bio-luminescent jungle', 'liquid methane ocean', 'plasma storms', 'geometric mountains', 'silicon forests', 'magnetic fields', 'quantum crystals', 'living metal', 'energy vortexes', 'gravity wells', 'temporal rifts', 'phase-shifted landscapes', 'void chasms', 'antimatter lakes', 'fractal canyons', 'morphic plains', 'sentient coral']`
- `color` (required): `['purple', 'emerald', 'crimson', 'azure', 'golden', 'silver', 'iridescent', 'prismatic', 'void-black', 'plasma-blue', 'quantum-white', 'temporal-green', 'nebula-pink', 'star-gold', 'cosmic-violet']`
- `feature` (required): `['multiple moons', 'binary suns', 'ring system', 'quantum anomalies', 'temporal rifts', 'space elevator', 'orbital habitats', 'ancient megastructures', 'artificial moons', 'plasma rivers', 'crystal spires', 'gravity anomalies', 'bio-mechanical forests', 'energy storms', 'dimensional portals', 'living cities', 'floating continents']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`

#### Outputs

- `world_desc`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 81/100

**Reason:** This node can generate alien worlds that could be used as a background or environment for the generated image.

### Metadata

---

### 🛸 Isulion Spacecraft Generator (`IsulionSpacecraftGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `ship` (required): `['battlecruiser', 'stealth frigate', 'carrier', 'destroyer', 'dreadnought', 'assault ship', 'combat vessel', 'strike craft', 'war barge', 'missile frigate', 'plasma cruiser', 'void hunter', 'quantum warship', 'battle station', 'star fortress', 'passenger liner', 'cargo hauler', 'mining vessel', 'colony ship', 'space yacht', 'trading vessel', 'transport ship', 'cruise liner', 'construction ship', 'medical frigate', 'research vessel', 'supply ship', 'merchant vessel', 'repair ship', 'salvage craft', 'scout ship', 'research vessel', 'survey craft', 'deep space probe', 'pathfinder ship', 'expedition craft', 'discovery vessel', 'stellar explorer', 'cartographer ship', 'science vessel', 'observatory ship', 'mapping drone', 'reconnaissance craft', 'sensor platform', 'probe carrier', 'dimensional ship', 'time vessel', 'living ship', 'quantum craft', 'phase shifter', 'void walker', 'reality bender', 'star seed', 'consciousness vessel', 'dream ship', 'infinity craft', 'cosmic weaver', 'paradox jumper', 'eternity vessel', 'dimension breaker']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `ship_class` (optional): `['any', 'military', 'civilian', 'exploration', 'special']`
  - Options: `{{'default': 'any'}}`

#### Outputs

- `ship`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 82/100

**Reason:** This node can generate spacecraft that could be used as a subject or object in the generated image.

### Metadata

---

### 🤖 Isulion Tech Generator (`IsulionTechGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `tech` (required): `['plasma rifle', 'quantum blade', 'sonic cannon', 'gravity gun', 'particle beam', 'fusion blaster', 'antimatter cannon', 'phase disruptor', 'laser sword', 'temporal gun', 'void cannon', 'energy whip', 'nano swarm launcher', 'dark matter projector', 'tachyon emitter', 'holographic display', 'neural interface', 'quantum computer', 'teleporter', 'force field generator', 'cloaking device', 'matter replicator', 'bio scanner', 'universal translator', 'time dilation device', 'gravity manipulator', 'mind probe', 'energy shield', 'wormhole generator', 'quantum entangler', 'cybernetic implant', 'nano-enhancer', 'bio-mod', 'exoskeleton', 'neural booster', 'synthetic organ', 'quantum processor', 'memory augment', 'reflex enhancer', 'strength amplifier', 'sensory upgrade', 'stealth system', 'healing matrix', 'combat suite', 'energy core', 'fusion core', 'antimatter reactor', 'zero-point module', 'quantum battery', 'dark energy tap', 'plasma converter', 'neutron source', 'void crystal', 'temporal capacitor', 'stellar cell', 'dimensional core', 'entropy inverter', 'quantum flux generator', 'cosmic energy collector', 'singularity engine']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `tech_type` (optional): `['any', 'weapons', 'gadgets', 'augments', 'power']`
  - Options: `{{'default': 'any'}}`

#### Outputs

- `tech`: `STRING`
- `seed`: `INT`

## KJNODES


### Applicability

**Score:** 80/100

**Reason:** This node can generate technology items such as guns and gadgets that could be used as objects or props in the generated image.

### Metadata

---

### Empty Latent Image Custom Presets (`EmptyLatentImageCustomPresets`)

**Description:**


Generates an empty latent image with the specified dimensions.  
The choices are loaded from 'custom_dimensions.json' in the nodes folder.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `dimensions` (required): `[]`
- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`

#### Outputs

- `Latent`: `LATENT`
- `Width`: `INT`
- `Height`: `INT`


### Applicability

**Score:** 41/100

**Reason:** Generates an empty latent image with dimensions that can be used as a starting point for text to image generation.

### Metadata

---

### Empty Latent Image Presets (`EmptyLatentImagePresets`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `dimensions` (required): `['512 x 512 (1:1)', '768 x 512 (1.5:1)', '960 x 512 (1.875:1)', '1024 x 512 (2:1)', '1024 x 576 (1.778:1)', '1536 x 640 (2.4:1)', '1344 x 768 (1.75:1)', '1216 x 832 (1.46:1)', '1152 x 896 (1.286:1)', '1024 x 1024 (1:1)']`
  - Options: `{{'default': '512 x 512 (1:1)'}}`
- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`

#### Outputs

- `Latent`: `LATENT`
- `Width`: `INT`
- `Height`: `INT`


### Applicability

**Score:** 81/100

**Reason:** Provides pre-defined dimensions for generating images which is essential for the workflow goal of text to image generation with LoRA model support.

### Metadata

---

### Get Latents From Batch Indexed (`GetLatentsFromBatchIndexed`)

**Description:**


Selects and returns the latents at the specified indices as an latent batch.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `latents` (required): `LATENT`
- `indexes` (required): `STRING`
  - Options: `{{'default': '0, 1, 2', 'multiline': True}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 61/100

**Reason:** Selects and returns specific latents from a batch which can be useful in fine-tuning or selecting specific outputs from the text to image generation process.

### Metadata

---

### Intrinsic Lora Sampling (`Intrinsic_lora_sampling`)

**Description:**


Sampler to use the intrinsic loras:  
https://github.com/duxiaodan/intrinsic-lora  
These LoRAs are tiny and thus included  
with this node pack.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `lora_name` (required): `['intrinsic_lora_sd15_albedo.safetensors', 'intrinsic_lora_sd15_depth.safetensors', 'intrinsic_lora_sd15_normal.safetensors', 'intrinsic_lora_sd15_shading.safetensors', 'intrinsic_loras.txt']`
- `task` (required): `['depth map', 'surface normals', 'albedo', 'shading']`
  - Options: `{{'default': 'depth map'}}`
- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': ''}}`
- `clip` (required): `CLIP`
- `vae` (required): `VAE`
- `per_batch` (required): `INT`
  - Options: `{{'default': 16, 'min': 1, 'max': 4096, 'step': 1}}`
- `image` (optional): `IMAGE`
- `optional_latent` (optional): `LATENT`

#### Outputs

- `IMAGE`: `IMAGE`
- `LATENT`: `LATENT`


### Applicability

**Score:** 95/100

**Reason:** This node is essential for text to image generation with LoRA model support as it allows sampling from intrinsic LoRAs.

### Metadata

---

### AppendInstanceDiffusionTracking (`AppendInstanceDiffusionTracking`)

**Description:**


Appends tracking data to be used with InstanceDiffusion:  
https://github.com/logtd/ComfyUI-InstanceDiffusion  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `tracking_1` (required): `TRACKING`
  - Options: `{{'forceInput': True}}`
- `tracking_2` (required): `TRACKING`
  - Options: `{{'forceInput': True}}`
- `prompt_1` (optional): `STRING`
  - Options: `{{'default': '', 'forceInput': True}}`
- `prompt_2` (optional): `STRING`
  - Options: `{{'default': '', 'forceInput': True}}`

#### Outputs

- `tracking`: `TRACKING`
- `prompt`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal as it appends tracking data to be used with InstanceDiffusion, which can enhance the quality of generated images.

### Metadata

---

### DrawInstanceDiffusionTracking (`DrawInstanceDiffusionTracking`)

**Description:**


Draws the tracking data from  
CreateInstanceDiffusionTracking -node.



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `tracking` (required): `TRACKING`
  - Options: `{{'forceInput': True}}`
- `box_line_width` (required): `INT`
  - Options: `{{'default': 2, 'min': 1, 'max': 10, 'step': 1}}`
- `draw_text` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `font` (required): `['FreeMono.ttf', 'FreeMonoBoldOblique.otf', 'TTNorms-Black.otf']`
- `font_size` (required): `INT`
  - Options: `{{'default': 20}}`

#### Outputs

- `image`: `IMAGE`

## KJNODES/AUDIO


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it draws the tracking data from CreateInstanceDiffusionTracking-node, which is essential for visualizing and understanding the generated images.

### Metadata

---

### NormalizedAmplitudeToFloatList (`NormalizedAmplitudeToFloatList`)

**Description:**


Works as a bridge to the AudioScheduler -nodes:  
https://github.com/a1lazydog/ComfyUI-AudioScheduler  
Creates a list of floats from the normalized amplitude.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `normalized_amp` (required): `NORMALIZED_AMPLITUDE`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 41/100

**Reason:** This node converts normalized amplitude to a list of floats, which might be useful as an intermediate step in text-to-image generation.

### Metadata

---

### NormalizedAmplitudeToMask (`NormalizedAmplitudeToMask`)

**Description:**


Works as a bridge to the AudioScheduler -nodes:  
https://github.com/a1lazydog/ComfyUI-AudioScheduler  
Creates masks based on the normalized amplitude.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `normalized_amp` (required): `NORMALIZED_AMPLITUDE`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_offset` (required): `INT`
  - Options: `{{'default': 0, 'min': -255, 'max': 255, 'step': 1}}`
- `location_x` (required): `INT`
  - Options: `{{'default': 256, 'min': 0, 'max': 4096, 'step': 1}}`
- `location_y` (required): `INT`
  - Options: `{{'default': 256, 'min': 0, 'max': 4096, 'step': 1}}`
- `size` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 1}}`
- `shape` (required): `['none', 'circle', 'square', 'triangle']`
  - Options: `{{'default': 'none'}}`
- `color` (required): `['white', 'amplitude']`
  - Options: `{{'default': 'amplitude'}}`

#### Outputs

- `MASK`: `MASK`


### Applicability

**Score:** 61/100

**Reason:** This node creates masks based on the normalized amplitude and provides various options for customization, making it moderately useful for text-to-image generation with LoRA model support.

### Metadata

---

### OffsetMaskByNormalizedAmplitude (`OffsetMaskByNormalizedAmplitude`)

**Description:**


Works as a bridge to the AudioScheduler -nodes:  
https://github.com/a1lazydog/ComfyUI-AudioScheduler  
Offsets masks based on the normalized amplitude.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `normalized_amp` (required): `NORMALIZED_AMPLITUDE`
- `mask` (required): `MASK`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': -4096, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': -4096, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `rotate` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `angle_multiplier` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -1.0, 'max': 1.0, 'step': 0.001, 'display': 'number'}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 51/100

**Reason:** This node offsets masks based on the normalized amplitude, which could be a supporting step in text-to-image generation, but its direct relevance is limited.

### Metadata

---

### String Constant (`StringConstant`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `string` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** Provides a constant string value that can be used as input or output in the workflow

### Metadata

---

### String Constant Multiline (`StringConstantMultiline`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `string` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`
- `strip_newlines` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `STRING`: `STRING`

## KJNODES/CONTROLNET


### Applicability

**Score:** 70/100

**Reason:** Allows for multiline string constants which may be useful for generating complex text inputs

### Metadata

---

### CheckpointPerturbWeights (`CheckpointPerturbWeights`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `joint_blocks` (required): `FLOAT`
  - Options: `{{'default': 0.02, 'min': 0.001, 'max': 10.0, 'step': 0.001}}`
- `final_layer` (required): `FLOAT`
  - Options: `{{'default': 0.02, 'min': 0.001, 'max': 10.0, 'step': 0.001}}`
- `rest_of_the_blocks` (required): `FLOAT`
  - Options: `{{'default': 0.02, 'min': 0.001, 'max': 10.0, 'step': 0.001}}`
- `seed` (required): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 18446744073709551615, 'step': 1}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 80/100

**Reason:** This node can be used to perturb weights of a loaded model, which could potentially improve the performance of the LoRA model in text-to-image generation.

### Metadata

---

### Diffusion Model Loader KJ (`DiffusionModelLoaderKJ`)

**Description:**

Node for patching torch.nn.Linear with CublasLinear.

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `ckpt_name` (required): `['hunyuan_video_t2v_720p_bf16.safetensors']`
  - The name of the checkpoint (model) to load.
  - Options: `{{'tooltip': 'The name of the checkpoint (model) to load.'}}`
- `weight_dtype` (required): `['default', 'fp8_e4m3fn', 'fp8_e4m3fn_fast', 'fp8_e5m2']`
- `patch_cublaslinear` (required): `BOOLEAN`
  - Enable or disable the patching, won't take effect on already loaded models!
  - Options: `{{'default': False, 'tooltip': "Enable or disable the patching, won't take effect on already loaded models!"}}`
- `sage_attention` (required): `['disabled', 'auto', 'sageattn_qk_int8_pv_fp16_cuda', 'sageattn_qk_int8_pv_fp16_triton', 'sageattn_qk_int8_pv_fp8_cuda']`
  - Patch comfy attention to use sageattn.
  - Options: `{{'default': False, 'tooltip': 'Patch comfy attention to use sageattn.'}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 81/100

**Reason:** Directly loads a diffusion model with LoRA support, making it essential for text-to-image generation.

### Metadata

---

### Flux Block Lora Loader (`FluxBlockLoraLoader`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
  - The diffusion model the LoRA will be applied to.
  - Options: `{{'tooltip': 'The diffusion model the LoRA will be applied to.'}}`
- `strength_model` (required): `FLOAT`
  - How strongly to modify the diffusion model. This value can be negative.
  - Options: `{{'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01, 'tooltip': 'How strongly to modify the diffusion model. This value can be negative.'}}`
- `lora_name` (optional): `['MODELS\\JuggerCineXL2.safetensors', 'MODELS\\JuggernautNegative-neg.pt', 'MODELS\\TCD-Hyper-SD15-1step-lora.safetensors', 'MODELS\\TCD-Hyper-SDXL-1step-lora.safetensors', 'MODELS\\TCD-SD15-LoRA.safetensors', 'MODELS\\TCD-SDXL-LoRA.safetensors', 'MODELS\\URPMv1.3_LORA_296.safetensors', 'MODELS\\cogvideox_5b_transpixar.safetensors', 'MODELS\\hyvideo_FastVideo_LoRA-fp8.safetensors', 'MODELS\\lcm\\LCM&TurboMix.safetensors', 'MODELS\\lcm\\LCMTurboMix_DPM_SDE_Karras.safetensors', 'MODELS\\lcm\\LCMTurboMix_Euler_A_fix.safetensors', 'MODELS\\lcm\\LCMTurboMix_LCM_Sampler.safetensors', 'MODELS\\lcm\\LCM_LoRA_Weights.safetensors', 'MODELS\\lcm\\LCM_LoRA_Weights_SD15.safetensors', 'MODELS\\lcm\\PAseer-SDXL-LCM+Turbo.safetensors', 'MODELS\\lcm\\lcm-lora-sdxl.safetensors', 'MODELS\\sd_1_5_dpo_lora_v1-128dim.safetensors', 'MODELS\\sd_v15_dpo_lora_v1.safetensors', 'MODELS\\sd_xl_dpo_lora_v1.safetensors', 'MODELS\\sd_xl_dpo_turbo_lora_v1-128dim.safetensors', 'MODELS\\sd_xl_turbo_lora_v1.safetensors', 'N\\1.5\\GITSJessicaALora.safetensors', 'N\\1.5\\JessicaAlbaDogu.safetensors', 'N\\1.5\\SusanStorm.safetensors', 'N\\1.5\\anneHathaway_v2.safetensors', 'N\\1.5\\appearance\\Doggy_and_kitty-000003.safetensors', 'N\\1.5\\appearance\\Grool LORA.safetensors', 'N\\1.5\\appearance\\JS_MiniSkirt.safetensors', 'N\\1.5\\appearance\\Pure sleep V1-000005.safetensors', 'N\\1.5\\appearance\\Pussy_Lily_v5.safetensors', 'N\\1.5\\appearance\\Pussy_Peach_Rear_v1.safetensors', 'N\\1.5\\appearance\\RealDownblouse4.safetensors', 'N\\1.5\\appearance\\ahegao_V1.safetensors', 'N\\1.5\\appearance\\ahegao_control_v1.0.safetensors', 'N\\1.5\\appearance\\bb_size_select.pt', 'N\\1.5\\appearance\\bralessv2.safetensors', 'N\\1.5\\appearance\\cmhair-000003.safetensors', 'N\\1.5\\appearance\\cum_b1.safetensors', 'N\\1.5\\appearance\\darkSushi_realisticPussy_v9.safetensors', 'N\\1.5\\appearance\\edgBodytape_MINI.safetensors', 'N\\1.5\\appearance\\edgPinayDollLikeness.safetensors', 'N\\1.5\\appearance\\eyes.safetensors', 'N\\1.5\\appearance\\largebulg1-000012.safetensors', 'N\\1.5\\appearance\\my_breast_helper.safetensors', 'N\\1.5\\appearance\\orgasm_face_v10.safetensors', 'N\\1.5\\appearance\\perky_breasts1.safetensors', 'N\\1.5\\appearance\\polyhedron_all_eyes.safetensors', 'N\\1.5\\appearance\\pulge-stomach_bulge.safetensors', 'N\\1.5\\appearance\\pureerosface_v1.pt', 'N\\1.5\\appearance\\quiron_BigDickDredD_v4_Lora.safetensors', 'N\\1.5\\appearance\\realistic_eyes-000004.safetensors', 'N\\1.5\\appearance\\russian.safetensors', 'N\\1.5\\appearance\\shocked_v1.safetensors', 'N\\1.5\\appearance\\skin_texture_v2.safetensors', 'N\\1.5\\appearance\\thicc_v2.3.safetensors', 'N\\1.5\\appearance\\wink_and_smile.safetensors', 'N\\1.5\\arcane_offset.safetensors', 'N\\1.5\\breastinclassBetter.safetensors', 'N\\1.5\\chars\\Anya Joy.safetensors', 'N\\1.5\\chars\\Azula-v1-02.safetensors', 'N\\1.5\\chars\\Egirl.safetensors', 'N\\1.5\\chars\\EmiliaClarke.safetensors', 'N\\1.5\\chars\\Frog_CT.safetensors', 'N\\1.5\\chars\\JessicaPare.pt', 'N\\1.5\\chars\\JinxLol.safetensors', 'N\\1.5\\chars\\KidCC.safetensors', 'N\\1.5\\chars\\KidChronoCross2.safetensors', 'N\\1.5\\chars\\Tylee.safetensors', 'N\\1.5\\chars\\[P]-RikkuFFX.safetensors', 'N\\1.5\\chars\\aiomonstergirls_aiov4LoraLycoris.safetensors', 'N\\1.5\\chars\\arianaav2.safetensors', 'N\\1.5\\chars\\arianagrande.safetensors', 'N\\1.5\\chars\\caricevh.safetensors', 'N\\1.5\\chars\\centaur2.safetensors', 'N\\1.5\\chars\\doll_likeness_irish.cm-info.safetensors', 'N\\1.5\\chars\\fleurgeffrier.safetensors', 'N\\1.5\\chars\\gadget_hackwrench_by_UnstableNick_v10.safetensors', 'N\\1.5\\chars\\giantess.safetensors', 'N\\1.5\\chars\\hazelmoore.safetensors', 'N\\1.5\\chars\\igbaddie.safetensors', 'N\\1.5\\chars\\jessicaalba_ti.pt', 'N\\1.5\\chars\\jessicachastain.safetensors', 'N\\1.5\\chars\\kiri.safetensors', 'N\\1.5\\chars\\lenaheadey-000006.safetensors', 'N\\1.5\\chars\\marle.safetensors', 'N\\1.5\\chars\\myfoxyland.safetensors', 'N\\1.5\\chars\\nataliedormer-000008.safetensors', 'N\\1.5\\chars\\olgachocolate.safetensors', 'N\\1.5\\chars\\r0seleslie.safetensors', 'N\\1.5\\chars\\shinkiro.safetensors', 'N\\1.5\\chars\\sophieturner.safetensors', 'N\\1.5\\fashion\\ClothingAdjuster3.safetensors', 'N\\1.5\\fashion\\Gothpunkgirl-000009.safetensors', 'N\\1.5\\fashion\\meltymochi_scene_girl.safetensors', 'N\\1.5\\fashion\\naked_ribbon-v1.safetensors', 'N\\1.5\\fashion\\only pantyhose.safetensors', 'N\\1.5\\fashion\\sexy_clothing_collection.safetensors', 'N\\1.5\\group\\MultipleAsses_v1.safetensors', 'N\\1.5\\group\\MultipleGirlsGroup.safetensors', 'N\\1.5\\group\\PovGroupSex_v10.safetensors', 'N\\1.5\\group\\PregnantHarem.safetensors', 'N\\1.5\\group\\Threesome_FefaAIart.safetensors', 'N\\1.5\\group\\group sex missionary_v1.4-9_lbw.safetensors', 'N\\1.5\\group\\group_mf-10.safetensors', 'N\\1.5\\group\\multiple boys_v1.1-5_lbw.safetensors', 'N\\1.5\\knolling_20.safetensors', 'N\\1.5\\pos\\BentOverTable-v1-Test2.safetensors', 'N\\1.5\\pos\\BondageAndDildos.safetensors', 'N\\1.5\\pos\\CONCEPT_pov_dating_ownwaifu-15.safetensors', 'N\\1.5\\pos\\ClitPussy1 v1.safetensors', 'N\\1.5\\pos\\CloseUpVaginal-v1.safetensors', 'N\\1.5\\pos\\CowgirlPosition-10.safetensors', 'N\\1.5\\pos\\DoggyPov1.safetensors', 'N\\1.5\\pos\\DoggystyleFromside1.safetensors', 'N\\1.5\\pos\\Doggyv0.2.safetensors', 'N\\1.5\\pos\\FFM_Poses_step_by_step.safetensors', 'N\\1.5\\pos\\FFM_exposed_oral-000004.safetensors', 'N\\1.5\\pos\\LargeInsertion-v1.safetensors', 'N\\1.5\\pos\\Missionary.safetensors', 'N\\1.5\\pos\\MissionaryVaginal-v2.safetensors', 'N\\1.5\\pos\\POVAssGrab.safetensors', 'N\\1.5\\pos\\POVDoggy.safetensors', 'N\\1.5\\pos\\POVMissionary.safetensors', 'N\\1.5\\pos\\PSCowgirl.safetensors', 'N\\1.5\\pos\\PovBentOverTable-v1.safetensors', 'N\\1.5\\pos\\PovDoggyAnal-v4.safetensors', 'N\\1.5\\pos\\PovReverseCowgirlAnal-v2.safetensors', 'N\\1.5\\pos\\Princesses_in_trouble_-_tentacle_mix.safetensors', 'N\\1.5\\pos\\ProneBone-000010.safetensors', 'N\\1.5\\pos\\ProneboneVaginal-v3.safetensors', 'N\\1.5\\pos\\Pussy_Spreading_v1c.safetensors', 'N\\1.5\\pos\\Reversesuspended1-000011.safetensors', 'N\\1.5\\pos\\StandingSplit_27867.safetensors', 'N\\1.5\\pos\\StandingVaginal-v1.safetensors', 'N\\1.5\\pos\\Standing_split_xxx.safetensors', 'N\\1.5\\pos\\Tentacled_V2.safetensors', 'N\\1.5\\pos\\TripleLickingOral.safetensors', 'N\\1.5\\pos\\Zerk_Lying_Pose.safetensors', 'N\\1.5\\pos\\akiyama_against_the_wall.safetensors', 'N\\1.5\\pos\\all_tits_fuck.v1.0-000085.safetensors', 'N\\1.5\\pos\\concept-tip-mid-base-vaginal-v1.safetensors', 'N\\1.5\\pos\\cowgirl position_353035.safetensors', 'N\\1.5\\pos\\creamypie-v2.0-000003.safetensors', 'N\\1.5\\pos\\ddjo_v1.safetensors', 'N\\1.5\\pos\\ddjoff_v1.safetensors', 'N\\1.5\\pos\\dildoRiding2-000005.safetensors', 'N\\1.5\\pos\\double penetration-from frontV2.safetensors', 'N\\1.5\\pos\\extended_downblouse.safetensors', 'N\\1.5\\pos\\front_view_all_fours_doggystyle_v1.0.safetensors', 'N\\1.5\\pos\\front_view_carrying_sex_v1.0.safetensors', 'N\\1.5\\pos\\hogtied3-05.safetensors', 'N\\1.5\\pos\\legs_up_missionary_v1.0.safetensors', 'N\\1.5\\pos\\lyingRope.safetensors', 'N\\1.5\\pos\\p0vr3vc0wg1rl_pruned.safetensors', 'N\\1.5\\pos\\povFacesitting.safetensors', 'N\\1.5\\pos\\pov_imminent_penetration.safetensors', 'N\\1.5\\pos\\pov_male_masturbation_v0.1.safetensors', 'N\\1.5\\pos\\qqq-gangbang-v2-000010.safetensors', 'N\\1.5\\pos\\standingspreadeagle2-05.safetensors', 'N\\1.5\\pos\\tentacleNestBelow.safetensors', 'N\\1.5\\pos\\top-down bottom-up_202761.safetensors', 'N\\1.5\\pos\\uncensored_cpt_v03.05.safetensors', 'N\\1.5\\pos\\viewbj4.6.safetensors', 'N\\1.5\\pos\\waistGrab.safetensors', 'N\\1.5\\scenes\\LR-pregnant-x-ray1.3.safetensors', 'N\\1.5\\scenes\\futanari_horse_penis_050623.safetensors', 'N\\1.5\\scenes\\onoff4.safetensors', 'N\\1.5\\shirtliftv1.safetensors', 'N\\1.5\\size\\Girls in Glass Jars v3.safetensors', 'N\\1.5\\size\\minigirls-000002.safetensors', 'N\\1.5\\size\\minigts_v3_lycoris.safetensors', 'N\\FDHDandUpscale.safetensors', 'N\\XL\\NsfwPovAllInOneLoraSdxl-000009.safetensors', 'N\\XL\\Pussy_Lily_v5_XL.safetensors', 'N\\XL\\TgirlsXL.safetensors', 'N\\XL\\appearance\\2BoutOvalSDXL2-000002.safetensors', 'N\\XL\\appearance\\flat_chested_v3.5.safetensors', 'N\\XL\\appearance\\slimwoman_v2.safetensors', 'N\\XL\\crowd_of_people.safetensors', 'N\\XL\\loha_giants_shrinks-tokens_see_civitai_page-0.8_weight-by_AI_Characters.safetensors', 'N\\XL\\princess_xl_v2.safetensors', 'N\\flux\\pyros_flux_atj.safetensors', 'N\\hunyuan\\chars\\EmiliaClarke_V1_ep20.safetensors', 'N\\hunyuan\\chars\\Nicole_Kidman_Huny_converted.safetensors', 'N\\hunyuan\\chars\\annie_epoch100.safetensors', 'N\\hunyuan\\chars\\belleHunyuan.safetensors', 'N\\hunyuan\\chars\\elsa_e70_512.safetensors', 'N\\hunyuan\\chars\\gamora_epoch30.safetensors', 'N\\hunyuan\\chars\\gr00cket_e50_512.safetensors', 'N\\hunyuan\\chars\\inara_epoch100.safetensors', 'N\\hunyuan\\chars\\luna_lovegood_e60_512.safetensors', 'N\\hunyuan\\chars\\mantisEpoch50.safetensors', 'N\\hunyuan\\chars\\wickEpoch50.safetensors', 'N\\hunyuan\\chars\\yoda_e60_512.safetensors', 'N\\hunyuan\\edge_of_reality_ep30_25200stp_lora_theaidoctor.safetensors', 'N\\hunyuan\\face\\ahegao_hunyuan_video_v1_e18.safetensors', 'N\\hunyuan\\face\\ahegaov1.safetensors', 'N\\hunyuan\\fashion\\HyVid_egirl_lora_theaidoctor.safetensors', 'N\\hunyuan\\fashion\\Latex Hunyuan Ver 1.0.safetensors', 'N\\hunyuan\\fashion\\crossTop.safetensors', 'N\\hunyuan\\fashion\\swimsuit.safetensors', 'N\\hunyuan\\general\\Influencer Poses_PolyPhaze10.safetensors', 'N\\hunyuan\\general\\SECRET SAUCE HERO V2.1.safetensors', 'N\\hunyuan\\motion\\Sexy_Dance_e15.safetensors', 'N\\hunyuan\\motion\\Tw3rk_e15.safetensors', 'N\\hunyuan\\motion\\bouncing_breasts_hunyuan.safetensors', 'N\\hunyuan\\motion\\str1p.safetensors', 'N\\hunyuan\\motion\\t1ttydr0p_v0.safetensors', 'N\\hunyuan\\positions\\Ass Worship Version 1.0.safetensors', 'N\\hunyuan\\positions\\BreastMassage.safetensors', 'N\\hunyuan\\positions\\DoggystyleFacingCamera.safetensors', 'N\\hunyuan\\positions\\Facesitting Hunyuan Ver 1.0.safetensors', 'N\\hunyuan\\positions\\Full Nelson Position Ver 0.5.safetensors', 'N\\hunyuan\\positions\\Hunyuan.c0wg1rl_335.safetensors', 'N\\hunyuan\\positions\\POVReverseCowgirl.safetensors', 'N\\hunyuan\\positions\\Titjob.safetensors', 'N\\hunyuan\\positions\\asstwerk.safetensors', 'N\\hunyuan\\positions\\cumshot.safetensors', 'N\\hunyuan\\positions\\doggystyle-from-the-side.safetensors', 'N\\hunyuan\\positions\\female_masturbation.safetensors', 'N\\hunyuan\\positions\\hj_epoch99.safetensors', 'N\\hunyuan\\positions\\missionary_pov.safetensors', 'N\\hunyuan\\positions\\missionary_pov_v1.1.safetensors', 'N\\hunyuan\\positions\\oral\\POVOral.safetensors', 'N\\hunyuan\\positions\\oral\\oral_e9.safetensors', 'N\\hunyuan\\positions\\oral\\oral_sex.safetensors', 'N\\hunyuan\\positions\\oral\\oral_vision-0.3b.safetensors', 'N\\hunyuan\\positions\\pov_blowjob.safetensors', 'N\\hunyuan\\positions\\pov_cowgirlposition_hunyuan_V3.safetensors', 'N\\hunyuan\\positions\\pr0neb0ne100-converted.safetensors', 'N\\hunyuan\\positions\\pussyjob_v1.safetensors', 'N\\hunyuan\\positions\\riding_dildo_v1_hunyuan.safetensors', 'N\\hunyuan\\scenes\\midis_CumShower_V0.5[HYVideo].safetensors', 'N\\hunyuan\\style\\125226-e20-csetiarcane_style_v3-s6660.safetensors', 'N\\pony\\0726 lecture theater_v1_pony.safetensors', 'N\\pony\\0778 submerged_v1_pony.safetensors', 'N\\pony\\1dkXLP.safetensors', 'N\\pony\\90s_pony.safetensors', 'N\\pony\\Adventure_Time_pony.safetensors', 'N\\pony\\AliceInWonderlandXLPony_character-10V2.safetensors', 'N\\pony\\AssUpSDXLv1Pony.safetensors', 'N\\pony\\Assisted_exposure_-_Mean_girls.safetensors', 'N\\pony\\Autumn_forrest-000009.safetensors', 'N\\pony\\Balls_Deep_V3LL.safetensors', 'N\\pony\\BetterDoggy.safetensors', 'N\\pony\\BossBattleSpiritPony.safetensors', 'N\\pony\\Captured_by_Goblins-000005.safetensors', 'N\\pony\\Captured_by_plants.safetensors', 'N\\pony\\Cheating__Cuckold.safetensors', 'N\\pony\\Creampie_Eating_Felching.safetensors', 'N\\pony\\DRKDL-R.safetensors', 'N\\pony\\FComic1To3Page_Pony_V1.safetensors', 'N\\pony\\FFFM_Foursome.safetensors', 'N\\pony\\FFM__FMF_Rabbit_Threesome_for_Pony.safetensors', 'N\\pony\\FFM_threesome_-_Kiss_and_Fellatio.safetensors', 'N\\pony\\FFM_threesome__1st_girl_on_top_with_2nd_licking_penisvagina.safetensors', 'N\\pony\\FLMGR-R.safetensors', 'N\\pony\\Femdom_Sandwich_FFM_Threesome-000009.safetensors', 'N\\pony\\Forest 3.safetensors', 'N\\pony\\FreeusePonyXL-20.safetensors', 'N\\pony\\HDA_DeepPenetrationFromBehindXL.safetensors', 'N\\pony\\Hair_Pull_Doggy_-_Pony.safetensors', 'N\\pony\\Insertion Slider_alpha1.0_rank4_noxattn_last.safetensors', 'N\\pony\\Intimate_Missionarycowgirl_1.0.safetensors', 'N\\pony\\MFF_Pussy_Sandwich.safetensors', 'N\\pony\\MGE_V6.2_retrain.safetensors', 'N\\pony\\Mating_Press__Piledriver_press_TEMPORARY_2.safetensors', 'N\\pony\\Multigrope.safetensors', 'N\\pony\\Piggyback_Doggy_3.safetensors', 'N\\pony\\Public_Sex.safetensors', 'N\\pony\\R1880N-000025.safetensors', 'N\\pony\\RE-Large Insertion XL V0.2.safetensors', 'N\\pony\\Reversed_Gangbang_Pony.safetensors', 'N\\pony\\StS_PonyXL_Detail_Slider_v1.4_iteration_3 (1).safetensors', 'N\\pony\\StS_PonyXL_Detail_Slider_v1.4_iteration_3.safetensors', 'N\\pony\\Strappado_XL.safetensors', 'N\\pony\\Test.safetensors', 'N\\pony\\Tinker_Bell.safetensors', 'N\\pony\\Transparent_Tentacles.safetensors', 'N\\pony\\TyleeXL.safetensors', 'N\\pony\\Walk-in_caught_by_Fire_Keeper-000004.safetensors', 'N\\pony\\agepony8.safetensors', 'N\\pony\\belleXL.safetensors', 'N\\pony\\bullied-harassment.pony.v1.safetensors', 'N\\pony\\device-bondage-v1.0.safetensors', 'N\\pony\\doggystyle facing viewer xl.safetensors', 'N\\pony\\explodingclothes_pony.safetensors', 'N\\pony\\facehumping.safetensors', 'N\\pony\\freeuse-000019.safetensors', 'N\\pony\\group sex_pony_V1.0.safetensors', 'N\\pony\\helddown.safetensors', 'N\\pony\\incase_style_v3-1_ponyxl_ilff.safetensors', 'N\\pony\\legdangle.safetensors', 'N\\pony\\mating_press_pdxl_goofy.safetensors', 'N\\pony\\mating_press_v0.2-pony.safetensors', 'N\\pony\\princess_pony_v1.safetensors', 'N\\pony\\pussy_sandwich_v0.2-pony.safetensors', 'N\\pony\\sdxl_vae.safetensors', 'N\\pony\\stasis_tank_v0.3-pony.safetensors', 'N\\pony\\styles\\AmaiAnimePony.safetensors', 'N\\pony\\styles\\AniAnimePony.safetensors', 'N\\pony\\styles\\BanashiPony.safetensors', 'N\\pony\\styles\\BlackComicPony.safetensors', 'N\\pony\\styles\\BulbaComicPony.safetensors', 'N\\pony\\styles\\ChokusenPony.safetensors', 'N\\pony\\styles\\EgakaPony.safetensors', 'N\\pony\\styles\\EnpitAnimePony.safetensors', 'N\\pony\\styles\\EregaAnimePony.safetensors', 'N\\pony\\styles\\FComic_HardCore_Pony_V1.safetensors', 'N\\pony\\styles\\FantajiSketchPony.safetensors', 'N\\pony\\styles\\FlatAnimePony.safetensors', 'N\\pony\\styles\\FurutsuHentaiPony.safetensors', 'N\\pony\\styles\\FutoiAnimePony.safetensors', 'N\\pony\\styles\\GaimoHentaiPony.safetensors', 'N\\pony\\styles\\GemAnimePony.safetensors', 'N\\pony\\styles\\GemuHentaiPony.safetensors', 'N\\pony\\styles\\HyperHentaiPony.safetensors', 'N\\pony\\styles\\IngAnimePony.safetensors', 'N\\pony\\styles\\JinseiAnimePony.safetensors', 'N\\pony\\styles\\KajonToonPony.safetensors', 'N\\pony\\styles\\KakkoiPonyV3.safetensors', 'N\\pony\\styles\\KakkoiiPony.safetensors', 'N\\pony\\styles\\KakkoiiPony2.safetensors', 'N\\pony\\styles\\KatounPony.safetensors', 'N\\pony\\styles\\KimPossiblePony.safetensors', 'N\\pony\\styles\\KureyonPony.safetensors', 'N\\pony\\styles\\KuronoiManhwaPony.safetensors', 'N\\pony\\styles\\LevoPony.safetensors', 'N\\pony\\styles\\MakuraAnimePony.safetensors', 'N\\pony\\styles\\MikuAnimePony.safetensors', 'N\\pony\\styles\\MoonPony.safetensors', 'N\\pony\\styles\\OttoPony.safetensors', 'N\\pony\\styles\\PastelAnimePony.safetensors', 'N\\pony\\styles\\PasuPony.safetensors', 'N\\pony\\styles\\PonPony.safetensors', 'N\\pony\\styles\\Pony_Diffusion_V6_Art_Style_-_Best_Of_Flux.safetensors', 'N\\pony\\styles\\PsyCartoonPony.safetensors', 'N\\pony\\styles\\RengaComicPony.safetensors', 'N\\pony\\styles\\RiboruPony.safetensors', 'N\\pony\\styles\\ShinbonPony.safetensors', 'N\\pony\\styles\\ShonkaPony.safetensors', 'N\\pony\\styles\\TrianglePony (1).safetensors', 'N\\pony\\styles\\TrianglePony.safetensors', 'N\\pony\\styles\\UrikaHentaiPony.safetensors', 'N\\pony\\styles\\WasurePony.safetensors', 'N\\pony\\styles\\WatashiAnimePony.safetensors', 'N\\pony\\styles\\WatashiHentaiPony.safetensors', 'N\\pony\\tentacle-pony-xl.safetensors', 'N\\pony\\tiedtopole.safetensors', 'N\\pony\\tutelage.safetensors', 'N\\pony\\uterus-ponyxl-lora-nochekaiser.safetensors', 'N\\pony\\venus_bikini_v0.1-pony.safetensors', 'S\\1.5\\XL\\EnvyZoomSliderXL01.safetensors', 'S\\1.5\\XL\\anime\\Rider_Waite_Tarot.safetensors', 'S\\1.5\\XL\\anime\\StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors', 'S\\1.5\\XL\\anime\\ghibli_last.safetensors', 'S\\1.5\\XL\\anime\\rws-tarot-r16.safetensors', 'S\\1.5\\XL\\craft\\cereal_box_sdxl_v1.safetensors', 'S\\1.5\\XL\\craft\\crayons_v1_sdxl.safetensors', 'S\\1.5\\XL\\craft\\embroidered_style_v1_sdxl.safetensors', 'S\\1.5\\XL\\craft\\ikea_instructions_xl_v1_5.safetensors', 'S\\1.5\\XL\\craft\\ral-orgmi-sdxl.safetensors', 'S\\1.5\\XL\\craft\\sdxl-PaperCutouts-Dreambooth.safetensors', 'S\\1.5\\XL\\craft\\stained_glass_style_v1_sdxl.safetensors', 'S\\1.5\\XL\\craft\\watercolor_v1_sdxl.safetensors', 'S\\1.5\\XL\\craft\\wood\\woodfigurez-sdxl.safetensors', 'S\\1.5\\XL\\detailed_notrigger.safetensors', 'S\\1.5\\XL\\face_xl_v0_1.safetensors', 'S\\1.5\\XL\\ovrgrwth-sdxl.safetensors', 'S\\1.5\\XL\\sdxl_loha_miniature2_v2-000080.safetensors', 'S\\1.5\\XL\\sdxl_photorealistic_slider_v1-0.safetensors', 'S\\1.5\\XL\\shrunk_xl_v11.safetensors', 'S\\1.5\\XL\\voxel\\LegoXL-v1.safetensors', 'S\\1.5\\XL\\voxel\\low_poly_count.safetensors', 'S\\1.5\\XL\\voxel\\minecraft.safetensors', 'S\\1.5\\XL\\voxel\\voxels.safetensors', 'S\\1.5\\appearance\\bootlicker.safetensors', 'S\\1.5\\appearance\\curly_hair_slider_v1.safetensors', 'S\\1.5\\appearance\\emotion_happy_slider_v1.safetensors', 'S\\1.5\\appearance\\emotions_lora.safetensors', 'S\\1.5\\appearance\\eye_size_slider_v1.safetensors', 'S\\1.5\\appearance\\eyeliner_v1.safetensors', 'S\\1.5\\appearance\\hair_length_slider_v1.safetensors', 'S\\1.5\\appearance\\muscle_slider_v1.safetensors', 'S\\1.5\\appearance\\skin_tone_slider_v1.safetensors', 'S\\1.5\\camera\\add-detail-xl.safetensors', 'S\\1.5\\camera\\color_temperature_slider_v1.safetensors', 'S\\1.5\\camera\\depth_of_field_slider_v1.safetensors', 'S\\1.5\\camera\\detail_slider_v4.safetensors', 'S\\1.5\\camera\\detailed_eye-10.safetensors', 'S\\1.5\\camera\\miniature_V1.safetensors', 'S\\1.5\\camera\\zoom_slider_v1.safetensors', 'S\\1.5\\chars\\ShrekDoguVersion2.safetensors', 'S\\1.5\\chars\\Tibetanfox.safetensors', 'S\\1.5\\chars\\chris_tucker_sd15_lora.safetensors', 'S\\1.5\\chars\\chris_tucker_sd15_lora_1200.safetensors', 'S\\1.5\\chars\\maria_menounos_sd15_lora.safetensors', 'S\\1.5\\environment\\2d_game_scence.safetensors', 'S\\1.5\\environment\\CircleV2.safetensors', 'S\\1.5\\environment\\Stylized tree.safetensors', 'S\\1.5\\environment\\WD_beautyview01.safetensors', 'S\\1.5\\environment\\nighttime_v1.safetensors', 'S\\1.5\\environment\\time_slider_v1.safetensors', 'S\\1.5\\fashion\\FireFashion.safetensors', 'S\\1.5\\fashion\\FlowersFashion.safetensors', 'S\\1.5\\fashion\\Heaven&HellFashion.safetensors', 'S\\1.5\\fashion\\IceFashion.safetensors', 'S\\1.5\\fashion\\StoneFashion.safetensors', 'S\\1.5\\fashion\\WaterFashion.safetensors', 'S\\1.5\\fashion\\dreads.safetensors', 'S\\1.5\\fashion\\edgEuropean_Vintage.safetensors', 'S\\1.5\\fashion\\edgHC_GOWN.safetensors', 'S\\1.5\\fashion\\edgSwedishDoll.safetensors', 'S\\1.5\\fashion\\fullbodytattoo-v1.1.safetensors', 'S\\1.5\\fashion\\goth.safetensors', 'S\\1.5\\fashion\\scene_girls1.safetensors', 'S\\1.5\\fashion\\tattoogirls.safetensors', 'S\\1.5\\fashion\\xmas_dress.safetensors', 'S\\1.5\\negatives\\BadDream.pt', 'S\\1.5\\negatives\\BeyondV3-neg.pt', 'S\\1.5\\negatives\\FastNegativeV2.pt', 'S\\1.5\\negatives\\NegfeetV2.pt', 'S\\1.5\\negatives\\UnrealisticDream.pt', 'S\\1.5\\negatives\\Unspeakable-Horrors-Composition-4v (1).pt', 'S\\1.5\\negatives\\Unspeakable-Horrors-Composition-4v.pt', 'S\\1.5\\negatives\\negative_hand-neg.pt', 'S\\1.5\\negatives\\ng_deepnegative_v1_75t.pt', 'S\\1.5\\sliders\\add_detail.safetensors', 'S\\1.5\\sliders\\age.pt', 'S\\1.5\\sliders\\cartoon_style.pt', 'S\\1.5\\sliders\\chubby.pt', 'S\\1.5\\sliders\\clay_style.pt', 'S\\1.5\\sliders\\cluttered_room.pt', 'S\\1.5\\sliders\\curlyhair.pt', 'S\\1.5\\sliders\\dark_weather.pt', 'S\\1.5\\sliders\\eyebrow.pt', 'S\\1.5\\sliders\\eyesize.pt', 'S\\1.5\\sliders\\festive.pt', 'S\\1.5\\sliders\\fix_hands.pt', 'S\\1.5\\sliders\\hd_helper_v1.safetensors', 'S\\1.5\\sliders\\long_hair.pt', 'S\\1.5\\sliders\\muscular.pt', 'S\\1.5\\sliders\\people_count_slider_v1.safetensors', 'S\\1.5\\sliders\\pixar_style.pt', 'S\\1.5\\sliders\\professional.pt', 'S\\1.5\\sliders\\repair_slider.pt', 'S\\1.5\\sliders\\riding_a.safetensors', 'S\\1.5\\sliders\\sculpture_style.pt', 'S\\1.5\\sliders\\smiling.pt', 'S\\1.5\\sliders\\stylegan_latent1.pt', 'S\\1.5\\sliders\\stylegan_latent2.pt', 'S\\1.5\\sliders\\suprised_look.pt', 'S\\1.5\\sliders\\tropical_weather.pt', 'S\\1.5\\sliders\\winter_weather.pt', 'S\\1.5\\styles\\3d\\3DMM_V12.safetensors', 'S\\1.5\\styles\\Modern Chinese Ink Painting_V04.safetensors', 'S\\1.5\\styles\\anime\\brands\\Pokemon (Style).safetensors', 'S\\1.5\\styles\\anime\\brands\\Style_of_the_Winds.safetensors', 'S\\1.5\\styles\\anime\\comic\\CTStyle.safetensors', 'S\\1.5\\styles\\anime\\comic\\Dandonfuga [MockAi - v1.0].safetensors', 'S\\1.5\\styles\\anime\\comic\\Minimalistic_Style.safetensors', 'S\\1.5\\styles\\anime\\comic\\artbytokiame.safetensors', 'S\\1.5\\styles\\anime\\comic\\balsamique.safetensors', 'S\\1.5\\styles\\anime\\comic\\carrot_mix.safetensors', 'S\\1.5\\styles\\anime\\comic\\khokhloma_style.safetensors', 'S\\1.5\\styles\\anime\\comic\\strawberry_mix.safetensors', 'S\\1.5\\styles\\anime\\comic\\style by snatti-000018.safetensors', 'S\\1.5\\styles\\anime\\ghibli\\Ghibli-v2.safetensors', 'S\\1.5\\styles\\anime\\ghibli\\Ghibli_v4.safetensors', 'S\\1.5\\styles\\anime\\ghibli\\Ghibli_v6.safetensors', 'S\\1.5\\styles\\anime\\ghibli\\ghibli_style_offset.safetensors', 'S\\1.5\\styles\\anime\\ghibli\\howlbgsv3.safetensors', 'S\\1.5\\styles\\anime\\tarot\\Tarot.safetensors', 'S\\1.5\\styles\\anime\\tarot\\Tarotv0.2.safetensors', 'S\\1.5\\styles\\craft\\crayons_v1.safetensors', 'S\\1.5\\styles\\craft\\glass\\Glass paintingV1-000016.safetensors', 'S\\1.5\\styles\\craft\\glass\\stained_glass.safetensors', 'S\\1.5\\styles\\craft\\paint\\Paint_style-000007.safetensors', 'S\\1.5\\styles\\miniature\\Isometric_Setting.safetensors', 'S\\1.5\\styles\\miniature\\knolling3.safetensors', 'S\\1.5\\styles\\miniature\\laydown.safetensors', 'S\\1.5\\styles\\miniature\\quiron_KnollingCase_v1_lora.safetensors', 'S\\1.5\\styles\\mocha style.safetensors', 'S\\1.5\\styles\\pixel\\Pixel bottle.safetensors', 'S\\1.5\\styles\\pixel\\VOXEL.safetensors', 'S\\1.5\\styles\\pixel\\pixel book.safetensors', 'S\\1.5\\styles\\pixel\\pixel plant growth.safetensors', 'S\\1.5\\styles\\pixel\\pixel sprites.safetensors', 'S\\1.5\\styles\\pixel\\pixel sword.safetensors', 'S\\1.5\\styles\\pixel\\pixel_f2.safetensors', 'S\\1.5\\styles\\pixel\\pixel_sprites_32.safetensors', 'S\\1.5\\styles\\pixel\\pixelartV3.safetensors', 'S\\1.5\\styles\\realism\\Realism-10.safetensors', 'S\\1.5\\styles\\realism\\de-anime-er_v10.safetensors', 'S\\1.5\\styles\\realism\\humans_realistic_lyCORIS.safetensors', 'S\\1.5\\styles\\realism\\photorealism_last.safetensors', 'S\\1.5\\styles\\realism\\real_slider_v2.safetensors', 'S\\hunyuan\\camera\\360_face_camera.safetensors', 'S\\hunyuan\\camera\\cl053up_e6.safetensors', 'S\\hunyuan\\camera\\kxsr_orbitcam_v2.safetensors', 'S\\hunyuan\\camera\\sanic.safetensors', 'S\\hunyuan\\chars\\Hunyuan Video - Alf - Trigger is alfman - LoRA.safetensors', 'S\\hunyuan\\chars\\b4by_d1n0_e12.safetensors', 'S\\hunyuan\\chars\\hunyuan_vivi_model20.safetensors', 'S\\hunyuan\\chars\\irl\\HunyuanVideo - Arnold Schwarzenegger LoRA - Trigger is Ohwx-Person.safetensors', 'S\\hunyuan\\chars\\irl\\HunyuanVideo - Elon Musk - Trigger is ohwx man.safetensors', 'S\\hunyuan\\chars\\irl\\NataLee_v4_epoch16.safetensors', 'S\\hunyuan\\chars\\irl\\ella-purn3ll-hunyuan-v1.0-vfx_ai.safetensors', 'S\\hunyuan\\chars\\irl\\emmawatson-hunyuan.safetensors', 'S\\hunyuan\\chars\\irl\\fat_elvis_ep10.safetensors', 'S\\hunyuan\\chars\\irl\\grandmaster-goldblum-e100.safetensors', 'S\\hunyuan\\chars\\irl\\jennifer lawrence_epoch60.safetensors', 'S\\hunyuan\\chars\\irl\\joan_mad_men_v1_epoch40.safetensors', 'S\\hunyuan\\chars\\irl\\kaylee_epoch100.safetensors', 'S\\hunyuan\\chars\\irl\\liz_hurley-hunyuan.safetensors', 'S\\hunyuan\\chars\\irl\\portman-hunyuan.safetensors', 'S\\hunyuan\\chars\\irl\\scarjo-hunyuan.safetensors', 'S\\hunyuan\\chars\\irl\\st4rl1ght_epoch50.safetensors', 'S\\hunyuan\\chars\\irl\\wednesday_addams_epoch30.safetensors', 'S\\hunyuan\\chars\\jinx.safetensors', 'S\\hunyuan\\chars\\pandora_30_model.safetensors', 'S\\hunyuan\\fashion\\social_fashion_hunyuan.safetensors', 'S\\hunyuan\\motion\\kxsr_walking_anim_v1-5.safetensors', 'S\\hunyuan\\scenes\\0Hunyuan_centralperk20.safetensors', 'S\\hunyuan\\scenes\\0Hunyuan_mosapar24.safetensors', 'S\\hunyuan\\scenes\\coolguyexplosion.safetensors', 'S\\hunyuan\\scenes\\this_is_fine_hunyuan.safetensors', 'S\\hunyuan\\styles\\anime_shots.safetensors', 'S\\hunyuan\\styles\\kxsr_super_saiyan_hunyuan_v1.safetensors', 'S\\hunyuan\\styles\\pixelated_retro.safetensors', 'S\\hunyuan\\styles\\studio_ghibli_hv_v03_19.safetensors', 'hyvideo_FastVideo_LoRA-fp8.safetensors']`
  - The name of the LoRA.
  - Options: `{{'tooltip': 'The name of the LoRA.'}}`
- `opt_lora_path` (optional): `STRING`
  - Absolute path of the LoRA.
  - Options: `{{'forceInput': True, 'tooltip': 'Absolute path of the LoRA.'}}`
- `blocks` (optional): `SELECTEDBLOCKS`

#### Outputs

- `model`: `MODEL`
  - The modified diffusion model.
- `rank`: `STRING`
  - possible rank of the LoRA.


### Applicability

**Score:** 91/100

**Reason:** Directly applies a LoRA to a loaded diffusion model, making it essential for fine-tuning and adapting the model to specific tasks.

### Metadata

---

### Flux Block Lora Select (`FluxBlockLoraSelect`)

**Description:**

Select individual block alpha values, value of 0 removes the block altogether

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `double_blocks.0.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.1.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.2.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.3.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.4.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.5.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.6.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.7.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.8.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.9.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.10.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.11.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.12.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.13.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.14.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.15.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.16.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.17.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `double_blocks.18.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.0.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.1.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.2.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.3.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.4.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.5.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.6.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.7.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.8.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.9.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.10.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.11.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.12.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.13.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.14.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.15.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.16.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.17.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.18.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.19.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.20.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.21.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.22.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.23.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.24.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.25.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.26.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.27.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.28.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.29.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.30.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.31.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.32.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.33.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.34.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.35.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.36.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`
- `single_blocks.37.` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}}`

#### Outputs

- `blocks`: `SELECTEDBLOCKS`
  - The modified diffusion model.


### Applicability

**Score:** 100/100

**Reason:** Allows for precise control over individual block alpha values in the LoRA, making it essential for fine-tuning.

### Metadata

---

### GLIGENTextBoxApplyBatchCoords (`GLIGENTextBoxApplyBatchCoords`)

**Description:**


This node allows scheduling GLIGEN text box positions in a batch,  
to be used with AnimateDiff-Evolved. Intended to pair with the  
Spline Editor -node.  

GLIGEN model can be downloaded through the Manage's "Install Models" menu.  
Or directly from here:  
https://huggingface.co/comfyanonymous/GLIGEN_pruned_safetensors/tree/main  
  
Inputs:  
- **latents** input is used to calculate batch size  
- **clip** is your standard text encoder, use same as for the main prompt  
- **gligen_textbox_model** connects to GLIGEN Loader  
- **coordinates** takes a json string of points, directly compatible  
with the spline editor node.
- **text** is the part of the prompt to set position for  
- **width** and **height** are the size of the GLIGEN bounding box  
  
Outputs:
- **conditioning** goes between to clip text encode and the sampler  
- **coord_preview** is an optional preview of the coordinates and  
bounding boxes.



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `latents` (required): `LATENT`
- `clip` (required): `CLIP`
- `gligen_textbox_model` (required): `GLIGEN`
- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `text` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `width` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 8}}`
- `size_multiplier` (optional): `FLOAT`
  - Options: `{{'default': [1.0], 'forceInput': True}}`

#### Outputs

- `conditioning`: `CONDITIONING`
- `coord_preview`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for scheduling GLIGEN text box positions in a batch, which is directly relevant to the Text to image generation with LoRA model support workflow goal.

### Metadata

---

### Interpolate Coords (`InterpolateCoords`)

**Description:**


Interpolates coordinates based on a curve.   


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `interpolation_curve` (required): `FLOAT`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `coordinates`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for interpolating coordinates based on a curve, which can be used in conjunction with other nodes to achieve the Text to image generation with LoRA model support workflow goal.

### Metadata

---

### Patch Model Patcher Order (`PatchModelPatcherOrder`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `patch_order` (required): `['object_patch_first', 'weight_patch_first']`
  - Patch the comfy patch_model function to load weight patches (LoRAs) before compiling the model
  - Options: `{{'default': 'weight_patch_first', 'tooltip': 'Patch the comfy patch_model function to load weight patches (LoRAs) before compiling the model'}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for patching LoRA models into the model architecture.

### Metadata

---

### SV3D Batch Schedule (`SV3D_BatchSchedule`)

**Description:**


Allow scheduling of the azimuth and elevation conditions for SV3D.  
Note that SV3D is still a video model and the schedule needs to always go forward  
https://huggingface.co/stabilityai/sv3d


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `clip_vision` (required): `CLIP_VISION`
- `init_image` (required): `IMAGE`
- `vae` (required): `VAE`
- `width` (required): `INT`
  - Options: `{{'default': 576, 'min': 16, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 576, 'min': 16, 'max': 16384, 'step': 8}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 21, 'min': 1, 'max': 4096}}`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out']`
- `azimuth_points_string` (required): `STRING`
  - Options: `{{'default': '0:(0.0),\n9:(180.0),\n20:(360.0)\n', 'multiline': True}}`
- `elevation_points_string` (required): `STRING`
  - Options: `{{'default': '0:(0.0),\n9:(0.0),\n20:(0.0)\n', 'multiline': True}}`

#### Outputs

- `positive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `latent`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** Directly schedules SV3D conditions which is necessary for text to image generation with LoRA model support.

### Metadata

---

### Stability API SD3 (`StabilityAPI_SD3`)

**Description:**


## Calls StabilityAI API
   
Although you may have multiple keys in your account,  
you should use the same key for all requests to this API.  

Get your API key here: https://platform.stability.ai/account/keys  
Recommended to set the key in the config.json -file under this  
node packs folder.  
# WARNING:  
Otherwise the API key may get saved in the image metadata even  
with "disable_metadata" on if the workflow includes save nodes  
separate from this node.  
   
sd3 requires 6.5 credits per generation  
sd3-turbo requires 4 credits per generation  

If no image is provided, mode is set to text-to-image  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `prompt` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `n_prompt` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `seed` (required): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 4294967294, 'step': 1}}`
- `model` (required): `['sd3', 'sd3-turbo']`
  - Options: `{{'default': 'sd3'}}`
- `aspect_ratio` (required): `['1:1', '16:9', '21:9', '2:3', '3:2', '4:5', '5:4', '9:16', '9:21']`
  - Options: `{{'default': '1:1'}}`
- `output_format` (required): `['png', 'jpeg']`
  - Options: `{{'default': 'jpeg'}}`
- `api_key` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `image` (optional): `IMAGE`
- `img2img_strength` (optional): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `disable_metadata` (optional): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** Calls StabilityAI API which supports text to image generation and has LoRA model support.

### Metadata

---

### Stable Zero123 Batch Schedule (`StableZero123_BatchSchedule`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `clip_vision` (required): `CLIP_VISION`
- `init_image` (required): `IMAGE`
- `vae` (required): `VAE`
- `width` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 16384, 'step': 8}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out']`
- `azimuth_points_string` (required): `STRING`
  - Options: `{{'default': '0:(0.0),\n7:(1.0),\n15:(0.0)\n', 'multiline': True}}`
- `elevation_points_string` (required): `STRING`
  - Options: `{{'default': '0:(0.0),\n7:(0.0),\n15:(0.0)\n', 'multiline': True}}`

#### Outputs

- `positive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `latent`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** Directly schedules Stable Zero123 conditions which is necessary for text to image generation with LoRA model support.

### Metadata

---

### Style Model Apply Advanced (`StyleModelApplyAdvanced`)

**Description:**

StyleModelApply but with strength parameter

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `style_model` (required): `STYLE_MODEL`
- `clip_vision_output` (required): `CLIP_VISION_OUTPUT`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.001}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for applying a style model with adjustable strength to the input conditioning.

### Metadata

---

### TorchCompileControlNet (`TorchCompileControlNet`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `controlnet` (required): `CONTROL_NET`
- `backend` (required): `['inductor', 'cudagraphs']`
- `fullgraph` (required): `BOOLEAN`
  - Enable full graph mode
  - Options: `{{'default': False, 'tooltip': 'Enable full graph mode'}}`
- `mode` (required): `['default', 'max-autotune', 'max-autotune-no-cudagraphs', 'reduce-overhead']`
  - Options: `{{'default': 'default'}}`

#### Outputs

- `CONTROL_NET`: `CONTROL_NET`


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful as it compiles the control net, but its relevance depends on the specific requirements of the workflow.

### Metadata

---

### TorchCompileLTXModel (`TorchCompileLTXModel`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `backend` (required): `['inductor', 'cudagraphs']`
- `fullgraph` (required): `BOOLEAN`
  - Enable full graph mode
  - Options: `{{'default': False, 'tooltip': 'Enable full graph mode'}}`
- `mode` (required): `['default', 'max-autotune', 'max-autotune-no-cudagraphs', 'reduce-overhead']`
  - Options: `{{'default': 'default'}}`
- `dynamic` (required): `BOOLEAN`
  - Enable dynamic mode
  - Options: `{{'default': False, 'tooltip': 'Enable dynamic mode'}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 61/100

**Reason:** This node is very useful for compiling an LTX model with various optimization options, which can be beneficial for text-to-image generation.

### Metadata

---

### TorchCompileModelFluxAdvanced (`TorchCompileModelFluxAdvanced`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `backend` (required): `['inductor', 'cudagraphs']`
- `fullgraph` (required): `BOOLEAN`
  - Enable full graph mode
  - Options: `{{'default': False, 'tooltip': 'Enable full graph mode'}}`
- `mode` (required): `['default', 'max-autotune', 'max-autotune-no-cudagraphs', 'reduce-overhead']`
  - Options: `{{'default': 'default'}}`
- `double_blocks` (required): `STRING`
  - Options: `{{'default': '0-18', 'multiline': True}}`
- `single_blocks` (required): `STRING`
  - Options: `{{'default': '0-37', 'multiline': True}}`
- `dynamic` (required): `BOOLEAN`
  - Enable dynamic mode
  - Options: `{{'default': False, 'tooltip': 'Enable dynamic mode'}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for compiling a model flux advanced with adjustable double and single blocks, which is crucial for optimizing the workflow.

### Metadata

---

### Webcam Capture CV2 (`WebcamCaptureCV2`)

**Description:**


Captures a frame from a webcam using CV2.  
Can be used for realtime diffusion with autoqueue.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4096, 'step': 1}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4096, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 4096, 'step': 1}}`
- `cam_index` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 255, 'step': 1}}`
- `release` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `image`: `IMAGE`

## KJNODES/IMAGE


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for the workflow goal as it captures real-time images from a webcam, which can be used as input for text-to-image generation models.

### Metadata

---

### Create Gradient From Coords (`CreateGradientFromCoords`)

**Description:**


Creates a gradient image from coordinates.    


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `start_color` (required): `STRING`
  - Options: `{{'default': 'white'}}`
- `end_color` (required): `STRING`
  - Options: `{{'default': 'black'}}`
- `multiplier` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.01, 'max': 100.0, 'step': 0.01}}`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for the workflow goal as it creates a gradient image from coordinates, which can be used as input or intermediate result for text-to-image generation models.

### Metadata

---

### Cross Fade Images (`CrossFadeImages`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images_1` (required): `IMAGE`
- `images_2` (required): `IMAGE`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out', 'bounce', 'elastic', 'glitchy', 'exponential_ease_out']`
- `transition_start_index` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 4096, 'step': 1}}`
- `transitioning_frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 4096, 'step': 1}}`
- `start_level` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `end_level` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for combining images in a cross-fade transition, which can be used in the final output of the workflow.

### Metadata

---

### Cross Fade Images Multi (`CrossFadeImagesMulti`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 1000, 'step': 1}}`
- `image_1` (required): `IMAGE`
- `image_2` (required): `IMAGE`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out', 'bounce', 'elastic', 'glitchy', 'exponential_ease_out']`
- `transitioning_frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 4096, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for combining multiple images in a cross-fade transition, which can be used in the final output of the workflow.

### Metadata

---

### Get Image Size & Count (`GetImageSizeAndCount`)

**Description:**


Returns width, height and batch size of the image,  
and passes it through unchanged.  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`

#### Outputs

- `image`: `IMAGE`
- `width`: `INT`
- `height`: `INT`
- `count`: `INT`


### Applicability

**Score:** 41/100

**Reason:** Provides image size and count information but does not directly contribute to text to image generation.

### Metadata

---

### Get Images From Batch Indexed (`GetImagesFromBatchIndexed`)

**Description:**


Selects and returns the images at the specified indices as an image batch.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `indexes` (required): `STRING`
  - Options: `{{'default': '0, 1, 2', 'multiline': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Selects images at specific indices which can be useful in processing batches of images for text to image generation.

### Metadata

---

### ImageBatchRepeatInterleaving (`ImageBatchRepeatInterleaving`)

**Description:**


Repeats each image in a batch by the specified number of times.  
Example batch of 5 images: 0, 1 ,2, 3, 4  
with repeats 2 becomes batch of 10 images: 0, 0, 1, 1, 2, 2, 3, 3, 4, 4  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `repeats` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** This node is very useful for the workflow goal as it repeats each image in a batch by the specified number of times, which can be used to generate more diverse images for training or testing.

### Metadata

---

### Image Concatenate From Batch (`ImageConcatFromBatch`)

**Description:**


    Concatenates images from a batch into a grid with a specified number of columns.
    

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `num_columns` (required): `INT`
  - Options: `{{'default': 3, 'min': 1, 'max': 255, 'step': 1}}`
- `match_image_size` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `max_resolution` (required): `INT`
  - Options: `{{'default': 4096}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for the workflow goal as it can be used to concatenate multiple images from a batch into a grid, which can be useful for visualizing or displaying generated images.

### Metadata

---

### Image Crop By Mask And Resize (`ImageCropByMaskAndResize`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `mask` (required): `MASK`
- `base_resolution` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `padding` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 1}}`
- `min_crop_resolution` (required): `INT`
  - Options: `{{'default': 128, 'min': 0, 'max': 16384, 'step': 8}}`
- `max_crop_resolution` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`

#### Outputs

- `images`: `IMAGE`
- `masks`: `MASK`
- `bbox`: `BBOX`


### Applicability

**Score:** 81/100

**Reason:** This node can be used to resize and crop images which are necessary steps in the text to image generation process.

### Metadata

---

### Image Grid Composite 2x2 (`ImageGridComposite2x2`)

**Description:**


Concatenates the 4 input images into a 2x2 grid. 


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image1` (required): `IMAGE`
- `image2` (required): `IMAGE`
- `image3` (required): `IMAGE`
- `image4` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** This node can be used to arrange multiple images into a grid, which could be useful for displaying generated images.

### Metadata

---

### Image Grid Composite 3x3 (`ImageGridComposite3x3`)

**Description:**


Concatenates the 9 input images into a 3x3 grid. 


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image1` (required): `IMAGE`
- `image2` (required): `IMAGE`
- `image3` (required): `IMAGE`
- `image4` (required): `IMAGE`
- `image5` (required): `IMAGE`
- `image6` (required): `IMAGE`
- `image7` (required): `IMAGE`
- `image8` (required): `IMAGE`
- `image9` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 41/100

**Reason:** This node can be used to arrange multiple images into a larger grid, but it may not be directly applicable to the text to image generation process.

### Metadata

---

### Image Normalize -1 to 1 (`ImageNormalize_Neg1_To_1`)

**Description:**


Normalize the images to be in the range [-1, 1]  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 91/100

**Reason:** Essential for this workflow as normalizing images is crucial for many deep learning models including LoRA.

### Metadata

---

### Resize Image (`ImageResizeKJ`)

**Description:**


Resizes the image to the specified width and height.  
Size can be retrieved from the inputs, and the final scale  
is  determined in this order of importance:  
- get_image_size  
- width_input and height_input  
- width and height widgets  
  
Keep proportions keeps the aspect ratio of the image, by  
highest dimension.  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `keep_proportion` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `divisible_by` (required): `INT`
  - Options: `{{'default': 2, 'min': 0, 'max': 512, 'step': 1}}`
- `width_input` (optional): `INT`
  - Options: `{{'forceInput': True}}`
- `height_input` (optional): `INT`
  - Options: `{{'forceInput': True}}`
- `get_image_size` (optional): `IMAGE`
- `crop` (optional): `['disabled', 'center']`

#### Outputs

- `IMAGE`: `IMAGE`
- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 83/100

**Reason:** Very useful as resizing images is a common preprocessing step in many computer vision tasks, including text to image generation with LoRA model support.

### Metadata

---

### Image Uncrop By Mask (`ImageUncropByMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `destination` (required): `IMAGE`
- `source` (required): `IMAGE`
- `mask` (required): `MASK`
- `bbox` (required): `BBOX`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** This node can be used to upscale images after they have been generated by a LoRA model, but it is not directly relevant to text-to-image generation.

### Metadata

---

### Image Upscale With Model Batched (`ImageUpscaleWithModelBatched`)

**Description:**


Same as ComfyUI native model upscaling node,  
but allows setting sub-batches for reduced VRAM usage.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `upscale_model` (required): `UPSCALE_MODEL`
- `images` (required): `IMAGE`
- `per_batch` (required): `INT`
  - Options: `{{'default': 16, 'min': 1, 'max': 4096, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 80/100

**Reason:** This node is essential for upscaling images with reduced VRAM usage, which is crucial for large-scale image generation tasks.

### Metadata

---

### Insert Images To Batch Indexed (`InsertImagesToBatchIndexed`)

**Description:**


Inserts images at the specified indices into the original image batch.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `images_to_insert` (required): `IMAGE`
- `indexes` (required): `STRING`
  - Options: `{{'default': '0, 1, 2', 'multiline': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 60/100

**Reason:** This node can be used to insert images into an existing batch, which could be useful in certain text-to-image generation workflows.

### Metadata

---

### Load & Resize Image (`LoadAndResizeImage`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `['example.png', 'pond_girl1.png', 'pond_girl2.png', 'pond_girl3.png']`
  - Options: `{{'image_upload': True}}`
- `resize` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `repeat` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096, 'step': 1}}`
- `keep_proportion` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `divisible_by` (required): `INT`
  - Options: `{{'default': 2, 'min': 0, 'max': 512, 'step': 1}}`
- `mask_channel` (required): `['alpha', 'red', 'green', 'blue']`
  - Channel to use for the mask output
  - Options: `{{'tooltip': 'Channel to use for the mask output'}}`
- `background_color` (required): `STRING`
  - Fills the alpha channel with the specified color.
  - Options: `{{'default': '', 'tooltip': 'Fills the alpha channel with the specified color.'}}`

#### Outputs

- `image`: `IMAGE`
- `mask`: `MASK`
- `width`: `INT`
- `height`: `INT`
- `image_path`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for loading and resizing images which are a crucial step in text to image generation.

### Metadata

---

### Merge Image Channels (`MergeImageChannels`)

**Description:**


Merges channel data into an image.  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `red` (required): `IMAGE`
- `green` (required): `IMAGE`
- `blue` (required): `IMAGE`
- `alpha` (optional): `MASK`
  - Options: `{{'default': None}}`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** Although not directly relevant, this node can be useful as a supporting node by merging channels of the generated image.

### Metadata

---

### Remap Image Range (`RemapImageRange`)

**Description:**


Remaps the image values to the specified range. 


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `min` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -10.0, 'max': 1.0, 'step': 0.01}}`
- `max` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `clamp` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 41/100

**Reason:** This node can be moderately useful as a supporting node by remapping the image values of the generated image, but its relevance depends on the specific requirements of the workflow.

### Metadata

---

### Reverse Image Batch (`ReverseImageBatch`)

**Description:**


Reverses the order of the images in a batch.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** Reverses the order of images in a batch, which can be useful as a supporting node for workflow tasks like data preparation or visualization.

### Metadata

---

### Save Image KJ (`SaveImageKJ`)

**Description:**

Saves the input images to your ComfyUI output directory.

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
  - The images to save.
  - Options: `{{'tooltip': 'The images to save.'}}`
- `filename_prefix` (required): `STRING`
  - The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes.
  - Options: `{{'default': 'ComfyUI', 'tooltip': 'The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes.'}}`
- `output_folder` (required): `STRING`
  - The folder to save the images to.
  - Options: `{{'default': 'output', 'tooltip': 'The folder to save the images to.'}}`
- `caption_file_extension` (optional): `STRING`
  - The extension for the caption file.
  - Options: `{{'default': '.txt', 'tooltip': 'The extension for the caption file.'}}`
- `caption` (optional): `STRING`
  - string to save as .txt file
  - Options: `{{'forceInput': True, 'tooltip': 'string to save as .txt file'}}`

#### Outputs

- `filename`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** Essential for saving generated images to the output directory with customizable file names and captions.

### Metadata

---

### Split Image Channels (`SplitImageChannels`)

**Description:**


Splits image channels into images where the selected channel  
is repeated for all channels, and the alpha as a mask. 


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`

#### Outputs

- `red`: `IMAGE`
- `green`: `IMAGE`
- `blue`: `IMAGE`
- `mask`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** Splits image channels which is necessary for processing and manipulating images in text-to-image generation with LoRA model support

### Metadata

---

### Batch CLIPSeg (`BatchCLIPSeg`)

**Description:**


Segments an image or batch of images using CLIPSeg.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `text` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `threshold` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 10.0, 'step': 0.001}}`
- `binary_mask` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `combine_mask` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `use_cuda` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `blur_sigma` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1}}`
- `opt_model` (optional): `CLIPSEGMODEL`
- `prev_mask` (optional): `MASK`
  - Options: `{{'default': None}}`
- `image_bg_level` (optional): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `invert` (optional): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `Mask`: `MASK`
- `Image`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Directly segments images using CLIPSeg, a crucial step in text-to-image generation with LoRA model support.

### Metadata

---

### Batch Crop From Mask (`BatchCropFromMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `masks` (required): `MASK`
- `crop_size_mult` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}}`
- `bbox_smooth_alpha` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `original_images`: `IMAGE`
- `cropped_images`: `IMAGE`
- `bboxes`: `BBOX`
- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 61/100

**Reason:** Crops images from masks, supporting the text-to-image generation process by preparing input images for further processing.

### Metadata

---

### Batch Crop From Mask Advanced (`BatchCropFromMaskAdvanced`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `masks` (required): `MASK`
- `crop_size_mult` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `bbox_smooth_alpha` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `original_images`: `IMAGE`
- `cropped_images`: `IMAGE`
- `cropped_masks`: `MASK`
- `combined_crop_image`: `IMAGE`
- `combined_crop_masks`: `MASK`
- `bboxes`: `BBOX`
- `combined_bounding_box`: `BBOX`
- `bbox_width`: `INT`
- `bbox_height`: `INT`


### Applicability

**Score:** 91/100

**Reason:** Advanced cropping functionality that combines multiple outputs, essential for refining and combining image segments in text-to-image generation with LoRA model support.

### Metadata

---

### Batch Uncrop (`BatchUncrop`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `cropped_images` (required): `IMAGE`
- `bboxes` (required): `BBOX`
- `border_blending` (required): `FLOAT`
  - Options: `{{'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `crop_rescale` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `border_top` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `border_bottom` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `border_left` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `border_right` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Uncrops cropped images back to their original size, a necessary step in the text-to-image generation workflow after segmenting and processing individual image parts.

### Metadata

---

### Bbox To Int (`BboxToInt`)

**Description:**


Returns selected index from bounding box list as integers.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `bboxes` (required): `BBOX`
- `index` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 99999999, 'step': 1}}`

#### Outputs

- `x_min`: `INT`
- `y_min`: `INT`
- `width`: `INT`
- `height`: `INT`
- `center_x`: `INT`
- `center_y`: `INT`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it can extract bounding box coordinates from a list of bboxes and an index, which could be used in the workflow for tasks like image cropping or object detection.

### Metadata

---

### Bbox Visualize (`BboxVisualize`)

**Description:**


Visualizes the specified bbox on the image.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `bboxes` (required): `BBOX`
- `line_width` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 10, 'step': 1}}`

#### Outputs

- `images`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant to text-to-image generation with LoRA model support as it can visualize bounding boxes on images, but its primary use case seems more related to debugging and visualization rather than direct contribution to the workflow goal.

### Metadata

---

### Color To Mask (`ColorToMask`)

**Description:**


Converts chosen RGB value to a mask.  
With batch inputs, the **per_batch**  
controls the number of images processed at once.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `red` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 255, 'step': 1}}`
- `green` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 255, 'step': 1}}`
- `blue` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 255, 'step': 1}}`
- `threshold` (required): `INT`
  - Options: `{{'default': 10, 'min': 0, 'max': 255, 'step': 1}}`
- `per_batch` (required): `INT`
  - Options: `{{'default': 16, 'min': 1, 'max': 4096, 'step': 1}}`

#### Outputs

- `MASK`: `MASK`


### Applicability

**Score:** 60/100

**Reason:** This node is moderately useful as it can convert RGB values to masks, which could be used in tasks like object segmentation or image processing. However, its relevance to text-to-image generation with LoRA model support is not immediately clear without further context.

### Metadata

---

### (Down)load CLIPSeg (`DownloadAndLoadCLIPSeg`)

**Description:**


Downloads and loads CLIPSeg model with huggingface_hub,  
to ComfyUI/models/clip_seg


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `['Kijai/clipseg-rd64-refined-fp16', 'CIDAS/clipseg-rd64-refined']`

#### Outputs

- `clipseg_model`: `CLIPSEGMODEL`


### Applicability

**Score:** 100/100

**Reason:** This node downloads and loads the CLIPSeg model with huggingface_hub, which is essential for text to image generation.

### Metadata

---

### FilterZeroMasksAndCorrespondingImages (`FilterZeroMasksAndCorrespondingImages`)

**Description:**


Filter out all the empty (i.e. all zero) mask in masks  
Also filter out all the corresponding images in original_images by indexes if provide  
  
original_images (optional): If provided, need have same length as masks.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `masks` (required): `MASK`
- `original_images` (optional): `IMAGE`

#### Outputs

- `non_zero_masks_out`: `MASK`
- `non_zero_mask_images_out`: `IMAGE`
- `zero_mask_images_out`: `IMAGE`
- `zero_mask_images_out_indexes`: `INDEXES`


### Applicability

**Score:** 90/100

**Reason:** This node filters out empty masks and corresponding images, making it moderately useful for pre-processing data before generating images.

### Metadata

---

### Get Mask Size & Count (`GetMaskSizeAndCount`)

**Description:**


Returns the width, height and batch size of the mask,  
and passes it through unchanged.  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`

#### Outputs

- `mask`: `MASK`
- `width`: `INT`
- `height`: `INT`
- `count`: `INT`


### Applicability

**Score:** 80/100

**Reason:** This node returns the width, height, and batch size of a mask, which is very useful for understanding the structure of input data.

### Metadata

---

### Grow Mask With Blur (`GrowMaskWithBlur`)

**Description:**


# GrowMaskWithBlur
- mask: Input mask or mask batch
- expand: Expand or contract mask or mask batch by a given amount
- incremental_expandrate: increase expand rate by a given amount per frame
- tapered_corners: use tapered corners
- flip_input: flip input mask
- blur_radius: value higher than 0 will blur the mask
- lerp_alpha: alpha value for interpolation between frames
- decay_factor: decay value for interpolation between frames
- fill_holes: fill holes in the mask (slow)

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`
- `expand` (required): `INT`
  - Options: `{{'default': 0, 'min': -16384, 'max': 16384, 'step': 1}}`
- `incremental_expandrate` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1}}`
- `tapered_corners` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `flip_input` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `blur_radius` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 100, 'step': 0.1}}`
- `lerp_alpha` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `decay_factor` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `fill_holes` (optional): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 40/100

**Reason:** This node grows or contracts a mask with blur, but its relevance to text to image generation with LoRA model support is limited as it does not directly contribute to the generation process.

### Metadata

---

### Offset Mask (`OffsetMask`)

**Description:**


Offsets the mask by the specified amount.  
 - mask: Input mask or mask batch
 - x: Horizontal offset
 - y: Vertical offset
 - angle: Angle in degrees
 - roll: roll edge wrapping
 - duplication_factor: Number of times to duplicate the mask to form a batch
 - border padding_mode: Padding mode for the mask


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': -4096, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': -4096, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `angle` (required): `INT`
  - Options: `{{'default': 0, 'min': -360, 'max': 360, 'step': 1, 'display': 'number'}}`
- `duplication_factor` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 1000, 'step': 1, 'display': 'number'}}`
- `roll` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `incremental` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `padding_mode` (required): `['empty', 'border', 'reflection']`
  - Options: `{{'default': 'empty'}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node is very useful as it can be used to adjust mask positions and sizes for better alignment with the generated images.

### Metadata

---

### Remap Mask Range (`RemapMaskRange`)

**Description:**


Sets new min and max values for the mask.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`
- `min` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -10.0, 'max': 1.0, 'step': 0.01}}`
- `max` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful as it can be used to rescale masks to match the dimensions of the generated images.

### Metadata

---

### Resize Mask (`ResizeMask`)

**Description:**


Resizes the mask or batch of masks to the specified width and height.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8, 'display': 'number'}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8, 'display': 'number'}}`
- `keep_proportions` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `crop` (required): `['disabled', 'center']`

#### Outputs

- `mask`: `MASK`
- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 41/100

**Reason:** This node is marginally relevant as it can be used to adjust mask values but does not directly contribute to text to image generation with LoRA model support.

### Metadata

---

### Split Bboxes (`SplitBboxes`)

**Description:**


Splits the specified bbox list at the given index into two lists.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `bboxes` (required): `BBOX`
- `index` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 99999999, 'step': 1}}`

#### Outputs

- `bboxes_a`: `BBOX`
- `bboxes_b`: `BBOX`

## KJNODES/MASKING/CONDITIONING


### Applicability

**Score:** 81/100

**Reason:** This node is very useful as it splits bounding boxes into two lists at a given index, which can be used in the workflow for further processing or manipulation of bboxes.

### Metadata

---

### Conditioning Multi Combine (`ConditioningMultiCombine`)

**Description:**


Combines multiple conditioning nodes into one


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 20, 'step': 1}}`
- `operation` (required): `['combine', 'concat']`
  - Options: `{{'default': 'combine'}}`
- `conditioning_1` (required): `CONDITIONING`
- `conditioning_2` (required): `CONDITIONING`

#### Outputs

- `combined`: `CONDITIONING`
- `inputcount`: `INT`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for this workflow as it combines multiple conditioning nodes into one, allowing for more complex and flexible text to image generation with LoRA model support.

### Metadata

---

### ConditioningSetMaskAndCombine3 (`ConditioningSetMaskAndCombine3`)

**Description:**


Bundles multiple conditioning mask and combine nodes into one,functionality is identical to ComfyUI native nodes


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `positive_1` (required): `CONDITIONING`
- `negative_1` (required): `CONDITIONING`
- `positive_2` (required): `CONDITIONING`
- `negative_2` (required): `CONDITIONING`
- `positive_3` (required): `CONDITIONING`
- `negative_3` (required): `CONDITIONING`
- `mask_1` (required): `MASK`
- `mask_2` (required): `MASK`
- `mask_3` (required): `MASK`
- `mask_1_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_2_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_3_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `set_cond_area` (required): `['default', 'mask bounds']`

#### Outputs

- `combined_positive`: `CONDITIONING`
- `combined_negative`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, making it essential for streamlining the workflow.

### Metadata

---

### ConditioningSetMaskAndCombine4 (`ConditioningSetMaskAndCombine4`)

**Description:**


Bundles multiple conditioning mask and combine nodes into one,functionality is identical to ComfyUI native nodes


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `positive_1` (required): `CONDITIONING`
- `negative_1` (required): `CONDITIONING`
- `positive_2` (required): `CONDITIONING`
- `negative_2` (required): `CONDITIONING`
- `positive_3` (required): `CONDITIONING`
- `negative_3` (required): `CONDITIONING`
- `positive_4` (required): `CONDITIONING`
- `negative_4` (required): `CONDITIONING`
- `mask_1` (required): `MASK`
- `mask_2` (required): `MASK`
- `mask_3` (required): `MASK`
- `mask_4` (required): `MASK`
- `mask_1_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_2_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_3_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_4_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `set_cond_area` (required): `['default', 'mask bounds']`

#### Outputs

- `combined_positive`: `CONDITIONING`
- `combined_negative`: `CONDITIONING`


### Applicability

**Score:** 82/100

**Reason:** Similar to Node 1, this node also bundles multiple conditioning mask and combine nodes into one, making it crucial for simplifying the workflow.

### Metadata

---

### ConditioningSetMaskAndCombine5 (`ConditioningSetMaskAndCombine5`)

**Description:**


Bundles multiple conditioning mask and combine nodes into one,functionality is identical to ComfyUI native nodes


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `positive_1` (required): `CONDITIONING`
- `negative_1` (required): `CONDITIONING`
- `positive_2` (required): `CONDITIONING`
- `negative_2` (required): `CONDITIONING`
- `positive_3` (required): `CONDITIONING`
- `negative_3` (required): `CONDITIONING`
- `positive_4` (required): `CONDITIONING`
- `negative_4` (required): `CONDITIONING`
- `positive_5` (required): `CONDITIONING`
- `negative_5` (required): `CONDITIONING`
- `mask_1` (required): `MASK`
- `mask_2` (required): `MASK`
- `mask_3` (required): `MASK`
- `mask_4` (required): `MASK`
- `mask_5` (required): `MASK`
- `mask_1_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_2_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_3_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_4_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `mask_5_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `set_cond_area` (required): `['default', 'mask bounds']`

#### Outputs

- `combined_positive`: `CONDITIONING`
- `combined_negative`: `CONDITIONING`

## KJNODES/MASKING/GENERATE


### Applicability

**Score:** 83/100

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, with an additional input, making it very useful for complex workflows.

### Metadata

---

### Create Fade Mask Advanced (`CreateFadeMaskAdvanced`)

**Description:**


Create a batch of masks interpolated between given frames and values. 
Uses same syntax as Fizz' BatchValueSchedule.
First value is the frame index (not that this starts from 0, not 1) 
and the second value inside the brackets is the float value of the mask in range 0.0 - 1.0  

For example the default values:  
0:(0.0)  
7:(1.0)  
15:(0.0)  
  
Would create a mask batch fo 16 frames, starting from black, 
interpolating with the chosen curve to fully white at the 8th frame, 
and interpolating from that to fully black at the 16th frame.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `points_string` (required): `STRING`
  - Options: `{{'default': '0:(0.0),\n7:(1.0),\n15:(0.0)\n', 'multiline': True}}`
- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `frames` (required): `INT`
  - Options: `{{'default': 16, 'min': 2, 'max': 10000, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 1, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 1, 'max': 4096, 'step': 1}}`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out']`

#### Outputs

- `MASK`: `MASK`


### Applicability

**Score:** 95/100

**Reason:** This node creates a batch of masks interpolated between given frames and values, which is directly relevant to the workflow goal of text-to-image generation with LoRA model support.

### Metadata

---

### Create Gradient Mask (`CreateGradientMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `frames` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 255, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`

#### Outputs

- `MASK`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node can generate a gradient mask which could be used as an input for the text to image generation process.

### Metadata

---

### Create Shape Mask (`CreateShapeMask`)

**Description:**


Creates a mask or batch of masks with the specified shape.  
Locations are center locations.  
Grow value is the amount to grow the shape on each frame, creating animated masks.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `shape` (required): `['circle', 'square', 'triangle']`
  - Options: `{{'default': 'circle'}}`
- `frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096, 'step': 1}}`
- `location_x` (required): `INT`
  - Options: `{{'default': 256, 'min': 0, 'max': 4096, 'step': 1}}`
- `location_y` (required): `INT`
  - Options: `{{'default': 256, 'min': 0, 'max': 4096, 'step': 1}}`
- `grow` (required): `INT`
  - Options: `{{'default': 0, 'min': -512, 'max': 512, 'step': 1}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `shape_width` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 1}}`
- `shape_height` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 1}}`

#### Outputs

- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 61/100

**Reason:** This node can create a shape mask which could be used as an input for the text to image generation process or as a component of the final output image.

### Metadata

---

### Create Text On Path (`CreateTextOnPath`)

**Description:**


Creates a mask or batch of masks with the specified text.  
Locations are center locations.  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `text` (required): `STRING`
  - Options: `{{'default': 'text', 'multiline': True}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `font` (required): `['FreeMono.ttf', 'FreeMonoBoldOblique.otf', 'TTNorms-Black.otf']`
- `font_size` (required): `INT`
  - Options: `{{'default': 42}}`
- `alignment` (required): `['left', 'center', 'right']`
  - Options: `{{'default': 'center'}}`
- `text_color` (required): `STRING`
  - Options: `{{'default': 'white'}}`
- `size_multiplier` (optional): `FLOAT`
  - Options: `{{'default': [1.0], 'forceInput': True}}`

#### Outputs

- `image`: `IMAGE`
- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 100/100

**Reason:** This node directly generates an image that can be used as input for a LoRA model, making it essential for the workflow goal.

### Metadata

---

### Float To Mask (`FloatToMask`)

**Description:**


Generates a batch of masks based on the input float values.
The batch size is determined by the length of the input float values.
Each mask is generated with the specified width and height.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `input_values` (required): `FLOAT`
  - Options: `{{'forceInput': True, 'default': 0}}`
- `width` (required): `INT`
  - Options: `{{'default': 100, 'min': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 100, 'min': 1}}`

#### Outputs

- `MASK`: `MASK`

## KJNODES/MISC


### Applicability

**Score:** 40/100

**Reason:** This node can be used as a supporting node for the workflow by generating masks from float values, but its direct relevance to the goal is limited.

### Metadata

---

### CondPassThrough (`CondPassThrough`)

**Description:**


    Simply passes through the positive and negative conditioning,
    workaround for Set node not allowing bypassed inputs.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `positive` (optional): `CONDITIONING`
- `negative` (optional): `CONDITIONING`

#### Outputs

- `positive`: `CONDITIONING`
- `negative`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node is essential as it allows bypassing of inputs in the Set node, which can be useful for conditioning in text-to-image generation.

### Metadata

---

### Custom Sigmas (`CustomSigmas`)

**Description:**


Creates a sigmas tensor from a string of comma separated values.  
Examples: 
   
Nvidia's optimized AYS 10 step schedule for SD 1.5:  
14.615, 6.475, 3.861, 2.697, 1.886, 1.396, 0.963, 0.652, 0.399, 0.152, 0.029  
SDXL:   
14.615, 6.315, 3.771, 2.181, 1.342, 0.862, 0.555, 0.380, 0.234, 0.113, 0.029  
SVD:  
700.00, 54.5, 15.886, 7.977, 4.248, 1.789, 0.981, 0.403, 0.173, 0.034, 0.002  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `sigmas_string` (required): `STRING`
  - Options: `{{'default': '14.615, 6.475, 3.861, 2.697, 1.886, 1.396, 0.963, 0.652, 0.399, 0.152, 0.029', 'multiline': True}}`
- `interpolate_to_steps` (required): `INT`
  - Options: `{{'default': 10, 'min': 0, 'max': 255, 'step': 1}}`

#### Outputs

- `SIGMAS`: `SIGMAS`


### Applicability

**Score:** 80/100

**Reason:** This node allows for custom sigma tensor creation which is relevant to the workflow goal of text to image generation with LoRA model support.

### Metadata

---

### Flip Sigmas Adjusted (`FlipSigmasAdjusted`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `sigmas` (required): `SIGMAS`
- `divide_by_last_sigma` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `divide_by` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': 1, 'max': 255, 'step': 0.01}}`
- `offset_by` (required): `INT`
  - Options: `{{'default': 1, 'min': -100, 'max': 100, 'step': 1}}`

#### Outputs

- `SIGMAS`: `SIGMAS`
- `sigmas_string`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node adjusts sigmas tensors which can be useful in fine-tuning the performance of the LoRA model during text to image generation.

### Metadata

---

### Generate Noise (`GenerateNoise`)

**Description:**


Generates noise for injection or to be used as empty latents on samplers with add_noise off.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`
- `seed` (required): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 18446744073709551615, 'step': 1}}`
- `multiplier` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 4096, 'step': 0.01}}`
- `constant_batch_noise` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `normalize` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `model` (optional): `MODEL`
- `sigmas` (optional): `SIGMAS`
- `latent_channels` (optional): `['4', '16']`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 80/100

**Reason:** This node generates noise which can be used in text-to-image generation and supports various parameters for customization.

### Metadata

---

### Inject Noise To Latent (`InjectNoiseToLatent`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `latents` (required): `LATENT`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 0.1, 'min': 0.0, 'max': 200.0, 'step': 0.0001}}`
- `noise` (required): `LATENT`
- `normalize` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `average` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `mask` (optional): `MASK`
- `mix_randn_amount` (optional): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.001}}`
- `seed` (optional): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 18446744073709551615, 'step': 1}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 90/100

**Reason:** This node injects noise into latents which is a crucial step in text-to-image generation with LoRA model support.

### Metadata

---

### Add Label (`AddLabel`)

**Description:**


Creates a new with the given text, and concatenates it to  
either above or below the input image.  
Note that this changes the input image's height!  
Fonts are loaded from this folder:  
ComfyUI/custom_nodes/ComfyUI-KJNodes/fonts


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `text_x` (required): `INT`
  - Options: `{{'default': 10, 'min': 0, 'max': 4096, 'step': 1}}`
- `text_y` (required): `INT`
  - Options: `{{'default': 2, 'min': 0, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 48, 'min': -1, 'max': 4096, 'step': 1}}`
- `font_size` (required): `INT`
  - Options: `{{'default': 32, 'min': 0, 'max': 4096, 'step': 1}}`
- `font_color` (required): `STRING`
  - Options: `{{'default': 'white'}}`
- `label_color` (required): `STRING`
  - Options: `{{'default': 'black'}}`
- `font` (required): `['FreeMono.ttf', 'FreeMonoBoldOblique.otf', 'TTNorms-Black.otf']`
- `text` (required): `STRING`
  - Options: `{{'default': 'Text'}}`
- `direction` (required): `['up', 'down', 'left', 'right', 'overlay']`
  - Options: `{{'default': 'up'}}`
- `caption` (optional): `STRING`
  - Options: `{{'default': '', 'forceInput': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Directly adds text to an image with customizable font and color options.

### Metadata

---

### Create Text Mask (`CreateTextMask`)

**Description:**


Creates a text image and mask.  
Looks for fonts from this folder:  
ComfyUI/custom_nodes/ComfyUI-KJNodes/fonts
  
If start_rotation and/or end_rotation are different values,  
creates animation between them.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096, 'step': 1}}`
- `text_x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4096, 'step': 1}}`
- `text_y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4096, 'step': 1}}`
- `font_size` (required): `INT`
  - Options: `{{'default': 32, 'min': 8, 'max': 4096, 'step': 1}}`
- `font_color` (required): `STRING`
  - Options: `{{'default': 'white'}}`
- `text` (required): `STRING`
  - Options: `{{'default': 'HELLO!', 'multiline': True}}`
- `font` (required): `['FreeMono.ttf', 'FreeMonoBoldOblique.otf', 'TTNorms-Black.otf']`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `start_rotation` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 359, 'step': 1}}`
- `end_rotation` (required): `INT`
  - Options: `{{'default': 0, 'min': -359, 'max': 359, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 61/100

**Reason:** Creates a text mask that can be used in conjunction with other nodes for text-to-image generation.

### Metadata

---

### Something To String (`SomethingToString`)

**Description:**


Converts any type to a string.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `input` (required): `*`
- `prefix` (optional): `STRING`
  - Options: `{{'default': ''}}`
- `suffix` (optional): `STRING`
  - Options: `{{'default': ''}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 41/100

**Reason:** This node is useful as a general-purpose utility function but does not specifically support LoRA model-based text-to-image generation.

### Metadata

---

### Superprompt (`Superprompt`)

**Description:**


# SuperPrompt
A T5 model fine-tuned on the SuperPrompt dataset for  
upsampling text prompts to more detailed descriptions.  
Meant to be used as a pre-generation step for text-to-image  
models that benefit from more detailed prompts.  
https://huggingface.co/roborovski/superprompt-v1


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `instruction_prompt` (required): `STRING`
  - Options: `{{'default': 'Expand the following prompt to add more detail', 'multiline': True}}`
- `prompt` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True, 'forceInput': True}}`
- `max_new_tokens` (required): `INT`
  - Options: `{{'default': 128, 'min': 1, 'max': 4096, 'step': 1}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 81/100

**Reason:** Directly generates detailed text prompts from input text, which is essential for text-to-image generation with LoRA model support.

### Metadata

---

### 🤖 LLMs Chat | 智能对话 (`LLMs Chat`)

**Description:**

**Module:** `ComfyUI-LLMs`

#### Inputs

- `api` (required): `['default']`
  - Options: `{{'default': 'default'}}`
- `model` (required): `['glm-4', 'chatglm_pro', 'ERNIE-Bot-4', 'qwen-turbo-internet', 'gpt-4o', 'gpt-4o-2024-05-13', 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-16k-0613', 'gpt-4-0613', 'gpt-4-1106-preview']`
  - Options: `{{'default': 'gpt-3.5-turbo'}}`
- `system_prompt` (required): `STRING`
  - Options: `{{'default': 'act as prompt generator, I will give you text and you describe an image that matches that text in details, answer with one response only.if I input in Chinese to communicate with you, but it is crucial that your response be in English.', 'multiline': True, 'dynamicPrompts': False}}`
- `user_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'your user prompt here'}}`
- `temperature` (required): `FLOAT`
  - Options: `{{'default': 0.99, 'min': 0.0, 'max': 2.0, 'step': 0.01}}`
- `top_p` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.001, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `gpt_response`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node is essential for text-to-image generation with LoRA model support as it interacts with LLMs to generate responses based on user prompts.

### Metadata

---

### 🎯 LLMs Vision | 图像理解 (`LLMs Vision Unified`)

**Description:**

**Module:** `ComfyUI-LLMs`

#### Inputs

- `image` (required): `IMAGE`
- `model_type` (required): `['openai', 'glm4', 'ali', 'gemini']`
- `model` (required): `['gpt-4o', 'glm-4v', 'glm-4', 'qwen-vl-plus', 'qwen-vl-max', 'gemini-1.5-flash-latest', 'gemini-1.5-flash-002', 'gemini-1.5-pro-latest', 'gemini-1.5-pro-002']`
- `prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'Please provide a detailed description of this image, including:\n- The main subject(s) and their appearance\n- The setting and environment\n- Colors, lighting, and visual elements\n- Any notable details or unique features\n- The overall mood and atmosphere\n\nDescribe as if you are explaining the image to someone who cannot see it.'}}`

#### Outputs

- `STRING`: `STRING`

## LOGIC


### Applicability

**Score:** 80/100

**Reason:** This node is very useful for text-to-image generation with LoRA model support as it uses LLMs Vision to understand and describe images based on provided prompts.

### Metadata

---

### Compare (`Compare-🔬`)

**Description:**

**Module:** `ComfyUI-Logic`

#### Inputs

- `a` (required): `*`
  - Options: `{{'default': 0}}`
- `b` (required): `*`
  - Options: `{{'default': 0}}`
- `comparison` (required): `['a == b', 'a != b', 'a < b', 'a > b', 'a <= b', 'a >= b']`
  - Options: `{{'default': 'a == b'}}`

#### Outputs

- `BOOLEAN`: `BOOLEAN`


### Applicability

**Score:** 60/100

**Reason:** This node can be used to compare values in the workflow, which could be useful for certain steps in text to image generation.

### Metadata

---

### String (`String-🔬`)

**Description:**

**Module:** `ComfyUI-Logic`

#### Inputs

- `value` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`

#### Outputs

- `STRING`: `STRING`

## POP


### Applicability

**Score:** 80/100

**Reason:** This node is useful for handling string inputs which are necessary for text to image generation with LoRA model support.

### Metadata

---

### AnyAspectRatio (`AnyAspectRatio`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `width_ratio` (required): `INT`
  - Options: `{{'default': 16, 'min': 1, 'max': 4096, 'step': 1, 'display': 'number'}}`
- `height_ratio` (required): `INT`
  - Options: `{{'default': 9, 'min': 1, 'max': 4096, 'step': 1, 'display': 'number'}}`
- `side_length` (required): `INT`
  - Options: `{{'default': 1024, 'min': 1, 'max': 4096, 'step': 1, 'display': 'number'}}`
- `rounding_value` (required): `INT`
  - Options: `{{'default': 64, 'min': 1, 'max': 4096, 'step': 1, 'display': 'number'}}`

#### Outputs

- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 60/100

**Reason:** This node can be used to generate aspect ratios but does not directly contribute to the workflow goal of text to image generation with LoRA model support.

### Metadata

---

### Conditioning Multiplier PoP (`ConditioningMultiplier_PoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `multiplier` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': -1, 'max': 3.0}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 41/100

**Reason:** The Conditioning Multiplier PoP is moderately useful as it can adjust the conditioning input for the LoRA model, but its direct relevance to text-to-image generation is limited.

### Metadata

---

### Conditioning Normalizer PoP (`ConditioningNormalizer_PoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `conditioning` (required): `CONDITIONING`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 61/100

**Reason:** The Conditioning Normalizer PoP is very useful as it normalizes the conditioning input, which is crucial for the LoRA model in text-to-image generation.

### Metadata

---

### Load Image Resizer PoP (`LoadImageResizer_PoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `image` (required): `['example.png', 'pond_girl1.png', 'pond_girl2.png', 'pond_girl3.png']`
  - Options: `{{'image_upload': True}}`
- `megapixels` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.01, 'max': 64.0, 'step': 0.01}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`

## POP/ATTENTION


### Applicability

**Score:** 81/100

**Reason:** The Load Image Resizer PoP is essential for this workflow goal as it resizes images to a specified megapixel value, which is necessary for image processing in text-to-image generation.

### Metadata

---

### Log (INT) (`LogInt`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `INT`
  - Options: `{{'forceInput': True}}`
- `prefix` (optional): `STRING`
  - Options: `{{'multiline': True, 'default': 'Value:'}}`

#### Outputs

- `INT`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node could be used as a supporting node to log integer values during the workflow, but it"s not directly related to the goal.

### Metadata

---

### To string (INT) (`RF_IntToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `INT`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 40/100

**Reason:** This node is moderately useful as it converts integer values to strings which might be necessary in certain steps of the text to image generation workflow, such as formatting model parameters or hyperparameters.

### Metadata

---

### Style from JSON file (`RF_JsonStyleLoader`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `style` (required): `[]`
- `prompt` (required): `STRING`
  - Options: `{{'default': '{{prompt}}'}}`
- `negative_prompt` (required): `STRING`
  - Options: `{{'default': '{{negative_prompt}}'}}`
- `positive` (optional): `STRING`
  - Options: `{{'multiline': True}}`
- `negative` (optional): `STRING`
  - Options: `{{'multiline': True}}`

#### Outputs

- `positive`: `STRING`
- `negative`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for this workflow goal. It loads style information from a JSON file, which is crucial for customizing the generated images with LoRA models.

### Metadata

---

### Input (STRING) (`RF_TextInput`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `STRING`
  - Options: `{{'multiline': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node provides a direct input for text to image generation workflow, allowing users to input text values.

### Metadata

---

### Replace text (`RF_TextReplace`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'Template {{text}} to replace!', 'defaultInput': True}}`
- `search` (required): `STRING`
  - Options: `{{'default': '{{text}}'}}`
- `replace` (required): `STRING`
  - Options: `{{'multiline': True, 'default': 'value'}}`

#### Outputs

- `text`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node enables replacing text in templates which can be useful for generating images with specific text content.

### Metadata

---

### To string (VEC2) (`RF_Vec2ToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `VEC2`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node can convert VEC2 values to strings which could be useful for generating image coordinates or other vector-based data.

### Metadata

---

### To string (VEC3) (`RF_Vec3ToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `VEC3`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 70/100

**Reason:** Similar to RF_Vec2ToString, this node can convert VEC3 values to strings which could be useful for 3D image generation.

### Metadata

---

### Searge Advanced Options Node (`Searge_AdvOptionsNode`)

**Description:**

**Module:** `ComfyUI_Searge_LLM`

#### Inputs

- `temperature` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.1, 'step': 0.05}}`
- `top_p` (required): `FLOAT`
  - Options: `{{'default': 0.9, 'min': 0.1, 'step': 0.05}}`
- `top_k` (required): `INT`
  - Options: `{{'default': 50, 'min': 0}}`
- `repetition_penalty` (required): `FLOAT`
  - Options: `{{'default': 1.2, 'min': 0.1, 'step': 0.05}}`

#### Outputs

- `adv_options_config`: `SRGADVOPTIONSCONFIG`


### Applicability

**Score:** 81/100

**Reason:** This node provides advanced options configuration which is essential for fine-tuning LoRA model support in text-to-image generation.

### Metadata

---

### Searge LLM Node (`Searge_LLM_Node`)

**Description:**

**Module:** `ComfyUI_Searge_LLM`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': ''}}`
- `random_seed` (required): `INT`
  - Options: `{{'default': 1234567890, 'min': 0, 'max': 18446744073709551615}}`
- `model` (required): `[]`
- `max_tokens` (required): `INT`
  - Options: `{{'default': 4096, 'min': 1, 'max': 8192}}`
- `apply_instructions` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `instructions` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'Generate a prompt from "{{prompt}}"'}}`
- `adv_options_config` (optional): `SRGADVOPTIONSCONFIG`

#### Outputs

- `generated`: `STRING`
- `original`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node directly generates images from text input with LoRA model support, making it a crucial component of the workflow.

### Metadata

---

### Differential Diffusion Advanced (`DifferentialDiffusionAdvanced`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `samples` (required): `LATENT`
- `mask` (required): `MASK`
- `multiplier` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.001}}`

#### Outputs

- `MODEL`: `MODEL`
- `LATENT`: `LATENT`


### Applicability

**Score:** 61/100

**Reason:** Although this node supports differential diffusion models, its direct relevance to LoRA model support is moderate due to differences in underlying technology.

### Metadata

---

### Latent Blend (`LatentBlend`)

**Description:**

#### Inputs

- `samples1` (required): `LATENT`
- `samples2` (required): `LATENT`
- `blend_factor` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for blending latent vectors from two different sources, which can be used in text to image generation with LoRA model support.

### Metadata

---

### SaveLatent (`SaveLatent`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `filename_prefix` (required): `STRING`
  - Options: `{{'default': 'latents/ComfyUI'}}`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for saving generated latent vectors from the text to image generation process with LoRA model support.

### Metadata

---

### VAE Encode (Tiled) (`VAEEncodeTiled`)

**Description:**

#### Inputs

- `pixels` (required): `IMAGE`
- `vae` (required): `VAE`
- `tile_size` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 4096, 'step': 64}}`
- `overlap` (required): `INT`
  - Options: `{{'default': 64, 'min': 0, 'max': 4096, 'step': 32}}`

#### Outputs

- `LATENT`: `LATENT`

## ADVANCED/CONDITIONING


### Applicability

**Score:** 81/100

**Reason:** This node is essential for encoding input images into a latent space that can be used by LoRA models.

### Metadata

---

### ConditioningSetTimestepRange (`ConditioningSetTimestepRange`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `start` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}}`
- `end` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful as it allows setting the timestep range for conditioning, but its relevance depends on the specific requirements of the workflow.

### Metadata

---

### Load CLIP (`CLIPLoader`)

**Description:**

[Recipes]

stable_diffusion: clip-l
stable_cascade: clip-g
sd3: t5 / clip-g / clip-l
stable_audio: t5
mochi: t5

#### Inputs

- `clip_name` (required): `['clip_l.safetensors', 'clip_vision_g.safetensors', 'llava_llama3_fp8_scaled.safetensors', 't5\\google_t5-v1_1-xxl_encoderonly-fp8_e4m3fn.safetensors', 't5\\model-00001-of-00004.safetensors', 't5\\model-00002-of-00004.safetensors', 't5\\model-00003-of-00004.safetensors', 't5\\model-00004-of-00004.safetensors']`
- `type` (required): `['stable_diffusion', 'stable_cascade', 'sd3', 'stable_audio', 'mochi', 'ltxv']`

#### Outputs

- `CLIP`: `CLIP`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for loading CLIP models that are required for text-to-image generation with LoRA model support.

### Metadata

---

### DualCLIPLoader (`DualCLIPLoader`)

**Description:**

[Recipes]

sdxl: clip-l, clip-g
sd3: clip-l, clip-g / clip-l, t5 / clip-g, t5
flux: clip-l, t5

#### Inputs

- `clip_name1` (required): `['clip_l.safetensors', 'clip_vision_g.safetensors', 'llava_llama3_fp8_scaled.safetensors', 't5\\google_t5-v1_1-xxl_encoderonly-fp8_e4m3fn.safetensors', 't5\\model-00001-of-00004.safetensors', 't5\\model-00002-of-00004.safetensors', 't5\\model-00003-of-00004.safetensors', 't5\\model-00004-of-00004.safetensors']`
- `clip_name2` (required): `['clip_l.safetensors', 'clip_vision_g.safetensors', 'llava_llama3_fp8_scaled.safetensors', 't5\\google_t5-v1_1-xxl_encoderonly-fp8_e4m3fn.safetensors', 't5\\model-00001-of-00004.safetensors', 't5\\model-00002-of-00004.safetensors', 't5\\model-00003-of-00004.safetensors', 't5\\model-00004-of-00004.safetensors']`
- `type` (required): `['sdxl', 'sd3', 'flux', 'hunyuan_video']`

#### Outputs

- `CLIP`: `CLIP`


### Applicability

**Score:** 80/100

**Reason:** This node supports dual CLIP model loading which can be useful for text to image generation with LoRA model support.

### Metadata

---

### CLIP Vector Sculptor text encode (`CLIP Vector Sculptor text encode`)

**Description:**

**Module:** `Vector_Sculptor_ComfyUI`

#### Inputs

- `clip` (required): `CLIP`
- `text` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `sculptor_intensity` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': 0, 'max': 10, 'step': 0.01}}`
- `sculptor_method` (required): `['forward', 'backward', 'maximum_absolute', 'add_minimum_absolute']`
- `token_normalization` (required): `['none', 'mean', 'set at 1', 'default * attention', 'mean * attention', 'set at attention', 'mean of all tokens']`

#### Outputs

- `Conditioning`: `CONDITIONING`
- `Parameters_as_string`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it can encode text into a format that can be used by the LoRA model for image generation.

### Metadata

---

### CLIP Set Last Layer (`CLIPSetLastLayer`)

**Description:**

#### Inputs

- `clip` (required): `CLIP`
- `stop_at_clip_layer` (required): `INT`
  - Options: `{{'default': -1, 'min': -24, 'max': -1, 'step': 1}}`

#### Outputs

- `CLIP`: `CLIP`


### Applicability

**Score:** 80/100

**Reason:** This node is essential for this workflow as it allows selecting the last layer of the CLIP model which is necessary for the LoRA model support.

### Metadata

---

### CLIP Text Encode (Prompt) (`CLIPTextEncode`)

**Description:**

Encodes a text prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images.

#### Inputs

- `text` (required): `STRING`
  - The text to be encoded.
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'tooltip': 'The text to be encoded.'}}`
- `clip` (required): `CLIP`
  - The CLIP model used for encoding the text.
  - Options: `{{'tooltip': 'The CLIP model used for encoding the text.'}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`
  - A conditioning containing the embedded text used to guide the diffusion model.


### Applicability

**Score:** 95/100

**Reason:** This node is extremely useful as it directly encodes a text prompt into an embedding that can be used to guide the diffusion model towards generating specific images with LoRA model support.

### Metadata

---

### CLIP Vision Encode (`CLIPVisionEncode`)

**Description:**

#### Inputs

- `clip_vision` (required): `CLIP_VISION`
- `image` (required): `IMAGE`
- `crop` (required): `['center', 'none']`

#### Outputs

- `CLIP_VISION_OUTPUT`: `CLIP_VISION_OUTPUT`


### Applicability

**Score:** 100/100

**Reason:** Essential for encoding input text into a CLIP vision representation.

### Metadata

---

### Conditioning (Average keep magnitude) (`Conditioning (Average keep magnitude)`)

**Description:**

**Module:** `Vector_Sculptor_ComfyUI`

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `conditioning_from` (required): `CONDITIONING`
- `conditioning_to_strength` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 60/100

**Reason:** Moderately useful as a supporting node to adjust conditioning strength.

### Metadata

---

### Conditioning (Slerp) (`Conditioning (Slerp)`)

**Description:**

**Module:** `Vector_Sculptor_ComfyUI`

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `conditioning_from` (required): `CONDITIONING`
- `conditioning_to_strength` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 40/100

**Reason:** Marginally relevant as it can be used to interpolate between two conditioning vectors.

### Metadata

---

### ConditioningAverage (`ConditioningAverage`)

**Description:**

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `conditioning_from` (required): `CONDITIONING`
- `conditioning_to_strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 80/100

**Reason:** This node is useful for normalizing conditioning inputs which could be beneficial in text-to-image generation with LoRA models.

### Metadata

---

### Conditioning (Combine) (`ConditioningCombine`)

**Description:**

#### Inputs

- `conditioning_1` (required): `CONDITIONING`
- `conditioning_2` (required): `CONDITIONING`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 90/100

**Reason:** This node allows combining multiple conditioning inputs which is essential for generating diverse and complex images using LoRA models.

### Metadata

---

### Conditioning (Concat) (`ConditioningConcat`)

**Description:**

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `conditioning_from` (required): `CONDITIONING`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 70/100

**Reason:** This node enables concatenating two conditioning inputs which could be useful in text-to-image generation with LoRA models, but its utility depends on the specific use case.

### Metadata

---

### Conditioning (Set Area) (`ConditioningSetArea`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `width` (required): `INT`
  - Options: `{{'default': 64, 'min': 64, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 64, 'min': 64, 'max': 16384, 'step': 8}}`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 81/100

**Reason:** This node directly sets an area in the conditioning step which is essential for text to image generation with LoRA model support.

### Metadata

---

### Conditioning (Set Area with Percentage) (`ConditioningSetAreaPercentage`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `width` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0, 'max': 1.0, 'step': 0.01}}`
- `height` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0, 'max': 1.0, 'step': 0.01}}`
- `x` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01}}`
- `y` (required): `FLOAT`
  - Options: `{{'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01}}`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 91/100

**Reason:** This node extends the previous one by allowing percentage-based area setting which is very useful for fine-grained control over the conditioning step.

### Metadata

---

### ConditioningSetAreaStrength (`ConditioningSetAreaStrength`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 41/100

**Reason:** This node only allows adjusting the strength of the conditioning, which is moderately useful but lacks direct relevance to the workflow goal.

### Metadata

---

### Conditioning (Set Mask) (`ConditioningSetMask`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `mask` (required): `MASK`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `set_cond_area` (required): `['default', 'mask bounds']`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 61/100

**Reason:** This node sets a mask in the conditioning step which is very useful for text to image generation with LoRA model support, especially when combined with other nodes.

### Metadata

---

### unCLIPConditioning (`unCLIPConditioning`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `clip_vision_output` (required): `CLIP_VISION_OUTPUT`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}}`
- `noise_augmentation` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`

## CONDITIONING/CONTROLNET


### Applicability

**Score:** 81/100

**Reason:** This node is essential for text to image generation with LoRA model support as it conditions the input based on CLIP vision output.

### Metadata

---

### Apply ControlNet (OLD) (`ControlNetApply`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `control_net` (required): `CONTROL_NET`
- `image` (required): `IMAGE`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 100/100

**Reason:** This node is crucial for text to image generation with LoRA model support as it applies ControlNet conditioning to the input image.

### Metadata

---

### Apply ControlNet (`ControlNetApplyAdvanced`)

**Description:**

#### Inputs

- `positive` (required): `CONDITIONING`
- `negative` (required): `CONDITIONING`
- `control_net` (required): `CONTROL_NET`
- `image` (required): `IMAGE`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `start_percent` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}}`
- `end_percent` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}}`
- `vae` (optional): `VAE`

#### Outputs

- `positive`: `CONDITIONING`
- `negative`: `CONDITIONING`


### Applicability

**Score:** 91/100

**Reason:** This node is very useful for text to image generation with LoRA model support as it provides advanced ControlNet conditioning capabilities.

### Metadata

---

### Set Shakker Labs Union ControlNet Type (`SetShakkerLabsUnionControlNetType`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `control_net` (required): `CONTROL_NET`
- `type` (required): `['auto', 'canny', 'tile', 'depth', 'blur', 'pose', 'gray', 'low quality']`

#### Outputs

- `CONTROL_NET`: `CONTROL_NET`

## CONDITIONING/GLIGEN


### Applicability

**Score:** 43/100

**Reason:** This node has moderate utility for text to image generation with LoRA model support as it sets the type of ControlNet used in the workflow, but does not directly contribute to the generation process.

### Metadata

---

### GLIGENTextBoxApply (`GLIGENTextBoxApply`)

**Description:**

#### Inputs

- `conditioning_to` (required): `CONDITIONING`
- `clip` (required): `CLIP`
- `gligen_textbox_model` (required): `GLIGEN`
- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True}}`
- `width` (required): `INT`
  - Options: `{{'default': 64, 'min': 8, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 64, 'min': 8, 'max': 16384, 'step': 8}}`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`

## CONDITIONING/INPAINT


### Applicability

**Score:** 81/100

**Reason:** Directly applies LoRA model support to text input, making it essential for the specified workflow goal.

### Metadata

---

### InpaintModelConditioning (`InpaintModelConditioning`)

**Description:**

#### Inputs

- `positive` (required): `CONDITIONING`
- `negative` (required): `CONDITIONING`
- `vae` (required): `VAE`
- `pixels` (required): `IMAGE`
- `mask` (required): `MASK`
- `noise_mask` (required): `BOOLEAN`
  - Add a noise mask to the latent so sampling will only happen within the mask. Might improve results or completely break things depending on the model.
  - Options: `{{'default': True, 'tooltip': 'Add a noise mask to the latent so sampling will only happen within the mask. Might improve results or completely break things depending on the model.'}}`

#### Outputs

- `positive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `latent`: `LATENT`

## CONDITIONING/STYLE_MODEL


### Applicability

**Score:** 41/100

**Reason:** Supports text-to-image generation but requires additional nodes for full functionality and may not directly integrate with LoRA models.

### Metadata

---

### Apply Style Model (`StyleModelApply`)

**Description:**

#### Inputs

- `conditioning` (required): `CONDITIONING`
- `style_model` (required): `STYLE_MODEL`
- `clip_vision_output` (required): `CLIP_VISION_OUTPUT`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}}`
- `strength_type` (required): `['multiply', 'attn_bias']`

#### Outputs

- `CONDITIONING`: `CONDITIONING`

## IMAGE


### Applicability

**Score:** 61/100

**Reason:** Applies style model support to conditioning input, making it moderately useful for the specified workflow goal.

### Metadata

---

### Invert Image (`ImageInvert`)

**Description:**

#### Inputs

- `image` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** While this node can invert an image, its utility in the context of text-to-image generation with LoRA model support is limited.

### Metadata

---

### Pad Image for Outpainting (`ImagePadForOutpaint`)

**Description:**

#### Inputs

- `image` (required): `IMAGE`
- `left` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `top` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `right` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `bottom` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `feathering` (required): `INT`
  - Options: `{{'default': 40, 'min': 0, 'max': 16384, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 80/100

**Reason:** This node pads an image for outpainting which could be useful as a supporting step to generate a larger image from a given prompt and then use that image as input for further processing or generation.

### Metadata

---

### LLaVA Captioner 🌊 (`LlavaCaptioner`)

**Description:**

**Module:** `ComfyUI-LLaVA-Captioner`

#### Inputs

- `image` (required): `IMAGE`
- `model` (required): `[]`
- `mm_proj` (required): `[]`
- `prompt` (required): `STRING`
  - Options: `{{'default': 'Please describe this image in 10 to 20 words.', 'multiline': True}}`
- `max_tokens` (required): `INT`
  - Options: `{{'default': 40, 'min': 0, 'max': 200, 'step': 5}}`
- `temperature` (required): `FLOAT`
  - Options: `{{'default': 0.2, 'min': 0.0, 'max': 1, 'step': 0.1}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for generating captions based on images using LLaVA models, which can be used in conjunction with LoRA model support for text to image generation.

### Metadata

---

### Load Image (`LoadImage`)

**Description:**

#### Inputs

- `image` (required): `['example.png', 'pond_girl1.png', 'pond_girl2.png', 'pond_girl3.png']`
  - Options: `{{'image_upload': True}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for loading the input image required for text to image generation with LoRA model support.

### Metadata

---

### Preview Image (`PreviewImage`)

**Description:**

Saves the input images to your ComfyUI output directory.

#### Inputs

- `images` (required): `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** Essential for displaying generated images in the workflow

### Metadata

---

### Save Image (`SaveImage`)

**Description:**

Saves the input images to your ComfyUI output directory.

#### Inputs

- `images` (required): `IMAGE`
  - The images to save.
  - Options: `{{'tooltip': 'The images to save.'}}`
- `filename_prefix` (required): `STRING`
  - The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes.
  - Options: `{{'default': 'ComfyUI', 'tooltip': 'The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes.'}}`

## IMAGE/UPSCALING


### Applicability

**Score:** 80/100

**Reason:** Very useful for saving generated images in the output directory

### Metadata

---

### Upscale Image (`ImageScale`)

**Description:**

#### Inputs

- `image` (required): `IMAGE`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 1}}`
- `crop` (required): `['disabled', 'center']`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** Marginally relevant for image processing but not directly related to text to image generation

### Metadata

---

### Upscale Image By (`ImageScaleBy`)

**Description:**

#### Inputs

- `image` (required): `IMAGE`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `scale_by` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.01, 'max': 8.0, 'step': 0.01}}`

#### Outputs

- `IMAGE`: `IMAGE`

## LATENT


### Applicability

**Score:** 41/100

**Reason:** Upscales an image but does not directly support LoRA model or text to image generation.

### Metadata

---

### Empty Latent Image (`EmptyLatentImage`)

**Description:**

Create a new batch of empty latent images to be denoised via sampling.

#### Inputs

- `width` (required): `INT`
  - The width of the latent images in pixels.
  - Options: `{{'default': 512, 'min': 16, 'max': 16384, 'step': 8, 'tooltip': 'The width of the latent images in pixels.'}}`
- `height` (required): `INT`
  - The height of the latent images in pixels.
  - Options: `{{'default': 512, 'min': 16, 'max': 16384, 'step': 8, 'tooltip': 'The height of the latent images in pixels.'}}`
- `batch_size` (required): `INT`
  - The number of latent images in the batch.
  - Options: `{{'default': 1, 'min': 1, 'max': 4096, 'tooltip': 'The number of latent images in the batch.'}}`

#### Outputs

- `LATENT`: `LATENT`
  - The empty latent image batch.


### Applicability

**Score:** 98/100

**Reason:** Creates empty latent images which is a crucial step in text to image generation with LoRA model support.

### Metadata

---

### Upscale Latent (`LatentUpscale`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp']`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 16384, 'step': 8}}`
- `crop` (required): `['disabled', 'center']`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 92/100

**Reason:** Upscales latent images which is necessary for generating high-quality images from text inputs in a LoRA model supported workflow.

### Metadata

---

### Upscale Latent By (`LatentUpscaleBy`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp']`
- `scale_by` (required): `FLOAT`
  - Options: `{{'default': 1.5, 'min': 0.01, 'max': 8.0, 'step': 0.01}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** Essential for upscaling latent images to support LoRA model in text-to-image generation.

### Metadata

---

### VAE Decode (`VAEDecode`)

**Description:**

Decodes latent images back into pixel space images.

#### Inputs

- `samples` (required): `LATENT`
  - The latent to be decoded.
  - Options: `{{'tooltip': 'The latent to be decoded.'}}`
- `vae` (required): `VAE`
  - The VAE model used for decoding the latent.
  - Options: `{{'tooltip': 'The VAE model used for decoding the latent.'}}`

#### Outputs

- `IMAGE`: `IMAGE`
  - The decoded image.


### Applicability

**Score:** 100/100

**Reason:** Critical for decoding latent images into pixel space images, a necessary step in text-to-image generation with LoRA model support.

### Metadata

---

### Repeat Latent Batch (`RepeatLatentBatch`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `amount` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 64}}`

#### Outputs

- `LATENT`: `LATENT`

## LATENT/INPAINT


### Applicability

**Score:** 61/100

**Reason:** This node can repeat latent batches to generate multiple images from a single input, which is useful in text-to-image generation.

### Metadata

---

### Set Latent Noise Mask (`SetLatentNoiseMask`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `mask` (required): `MASK`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 41/100

**Reason:** This node applies noise masks to latent samples, but its relevance to LoRA model support and text-to-image generation is moderate.

### Metadata

---

### Crop Latent (`LatentCrop`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 16384, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 16384, 'step': 8}}`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** Cropping latent samples can be essential in text-to-image generation to adjust image dimensions and align them with the desired output size.

### Metadata

---

### Rotate Latent (`LatentRotate`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `rotation` (required): `['none', '90 degrees', '180 degrees', '270 degrees']`

#### Outputs

- `LATENT`: `LATENT`

## LLM


### Applicability

**Score:** 60/100

**Reason:** This node can be moderately useful as a supporting node by rotating latent vectors for the LoRA model.

### Metadata

---

### Load CLIP Vision (`CLIPVisionLoader`)

**Description:**

#### Inputs

- `clip_name` (required): `[]`

#### Outputs

- `CLIP_VISION`: `CLIP_VISION`


### Applicability

**Score:** 90/100

**Reason:** This node can be very useful as a supporting node by loading CLIP vision models for the LoRA model.

### Metadata

---

### Load Checkpoint (`CheckpointLoaderSimple`)

**Description:**

Loads a diffusion model checkpoint, diffusion models are used to denoise latents.

#### Inputs

- `ckpt_name` (required): `['1-5\\dreamshaper_8.safetensors', 'hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors', 'ltx-video-2b-v0.9.safetensors', 'xl\\irisLuxPolyvalentPrototype_v1051VAEIncluded.safetensors', 'xl\\juggernautXL_v7Rundiffusion.safetensors', 'xl\\realismEngineSDXL_v20VAE.safetensors', 'xl\\sd_xl_base_1.0.safetensors', 'xl\\sd_xl_refiner_1.0.safetensors', 'xl\\sdxxxl_v30.safetensors']`
  - The name of the checkpoint (model) to load.
  - Options: `{{'tooltip': 'The name of the checkpoint (model) to load.'}}`

#### Outputs

- `MODEL`: `MODEL`
  - The model used for denoising latents.
- `CLIP`: `CLIP`
  - The CLIP model used for encoding text prompts.
- `VAE`: `VAE`
  - The VAE model used for encoding and decoding images to and from latent space.


### Applicability

**Score:** 100/100

**Reason:** Loads a diffusion model checkpoint which is essential for text to image generation with LoRA model support.

### Metadata

---

### Load VAE (`VAELoader`)

**Description:**

#### Inputs

- `vae_name` (required): `['hunyuan_video_vae_bf16.safetensors']`

#### Outputs

- `VAE`: `VAE`


### Applicability

**Score:** 80/100

**Reason:** This node loads a VAE which is crucial for the text to image generation workflow with LoRA model support.

### Metadata

---

### unCLIPCheckpointLoader (`unCLIPCheckpointLoader`)

**Description:**

#### Inputs

- `ckpt_name` (required): `['1-5\\dreamshaper_8.safetensors', 'hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors', 'ltx-video-2b-v0.9.safetensors', 'xl\\irisLuxPolyvalentPrototype_v1051VAEIncluded.safetensors', 'xl\\juggernautXL_v7Rundiffusion.safetensors', 'xl\\realismEngineSDXL_v20VAE.safetensors', 'xl\\sd_xl_base_1.0.safetensors', 'xl\\sd_xl_refiner_1.0.safetensors', 'xl\\sdxxxl_v30.safetensors']`

#### Outputs

- `MODEL`: `MODEL`
- `CLIP`: `CLIP`
- `VAE`: `VAE`
- `CLIP_VISION`: `CLIP_VISION`

## MASK


### Applicability

**Score:** 90/100

**Reason:** This node loads an unCLIP checkpoint which includes a VAE and supports LoRA models, making it highly relevant to the workflow goal.

### Metadata

---

### Primitive (STRING MULTI-LINE) (`StringMlStaticPrimitive`)

**Description:**

**Module:** `ComfyUI-Static-Primitives`

#### Inputs

- `Input_STRING` (required): `STRING`
  - Options: `{{'multiline': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it can handle multi-line string inputs which could be used to generate images from longer text descriptions.

### Metadata

---

### Primitive (STRING) (`StringStaticPrimitive`)

**Description:**

**Module:** `ComfyUI-Static-Primitives`

#### Inputs

- `Input_STRING` (required): `STRING`
  - Options: `{{'multiline': False}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 40/100

**Reason:** This node is moderately useful as it can handle single-line string inputs but lacks the ability to handle more complex text inputs that are often required for image generation.

### Metadata

---

### Collection Primitive (sampler) (`samplerStaticCollectionPrimitive`)

**Description:**

**Module:** `ComfyUI-Static-Primitives`

#### Inputs

- `Input_sampler` (required): `['euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ddim', 'uni_pc', 'uni_pc_bh2']`

#### Outputs

- `['euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ddim', 'uni_pc', 'uni_pc_bh2']`: `['euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ddim', 'uni_pc', 'uni_pc_bh2']`


### Applicability

**Score:** 40/100

**Reason:** This node provides a sampler but its specific functionality does not directly support text to image generation with LoRA model support.

### Metadata

---

### Collection Primitive (scheduler) (`schedulerStaticCollectionPrimitive`)

**Description:**

**Module:** `ComfyUI-Static-Primitives`

#### Inputs

- `Input_scheduler` (required): `['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform']`

#### Outputs

- `['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform']`: `['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform']`

## SAMPLING


### Applicability

**Score:** 80/100

**Reason:** This node is relevant as it supports scheduling for the sampling process which can be useful for optimizing text to image generation workflows.

### Metadata

---

### KSampler (`KSampler`)

**Description:**

Uses the provided model, positive and negative conditioning to denoise the latent image.

#### Inputs

- `model` (required): `MODEL`
  - The model used for denoising the input latent.
  - Options: `{{'tooltip': 'The model used for denoising the input latent.'}}`
- `seed` (required): `INT`
  - The random seed used for creating the noise.
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615, 'tooltip': 'The random seed used for creating the noise.'}}`
- `steps` (required): `INT`
  - The number of steps used in the denoising process.
  - Options: `{{'default': 20, 'min': 1, 'max': 10000, 'tooltip': 'The number of steps used in the denoising process.'}}`
- `cfg` (required): `FLOAT`
  - The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality.
  - Options: `{{'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01, 'tooltip': 'The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality.'}}`
- `sampler_name` (required): `['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_2s_ancestral_cfg_pp', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_cfg_pp', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'ddim', 'uni_pc', 'uni_pc_bh2']`
  - The algorithm used when sampling, this can affect the quality, speed, and style of the generated output.
  - Options: `{{'tooltip': 'The algorithm used when sampling, this can affect the quality, speed, and style of the generated output.'}}`
- `scheduler` (required): `['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'beta', 'linear_quadratic']`
  - The scheduler controls how noise is gradually removed to form the image.
  - Options: `{{'tooltip': 'The scheduler controls how noise is gradually removed to form the image.'}}`
- `positive` (required): `CONDITIONING`
  - The conditioning describing the attributes you want to include in the image.
  - Options: `{{'tooltip': 'The conditioning describing the attributes you want to include in the image.'}}`
- `negative` (required): `CONDITIONING`
  - The conditioning describing the attributes you want to exclude from the image.
  - Options: `{{'tooltip': 'The conditioning describing the attributes you want to exclude from the image.'}}`
- `latent_image` (required): `LATENT`
  - The latent image to denoise.
  - Options: `{{'tooltip': 'The latent image to denoise.'}}`
- `denoise` (required): `FLOAT`
  - The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling.
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01, 'tooltip': 'The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling.'}}`

#### Outputs

- `LATENT`: `LATENT`
  - The denoised latent.


### Applicability

**Score:** 90/100

**Reason:** This node provides a KSampler that uses the provided model and conditioning to denoise the latent image, making it highly relevant for text to image generation with LoRA model support.

### Metadata

---

### KSampler (Advanced) (`KSamplerAdvanced`)

**Description:**

#### Inputs

- `model` (required): `MODEL`
- `add_noise` (required): `['enable', 'disable']`
- `noise_seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `steps` (required): `INT`
  - Options: `{{'default': 20, 'min': 1, 'max': 10000}}`
- `cfg` (required): `FLOAT`
  - Options: `{{'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}}`
- `sampler_name` (required): `['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_2s_ancestral_cfg_pp', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_cfg_pp', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'ddim', 'uni_pc', 'uni_pc_bh2']`
- `scheduler` (required): `['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'beta', 'linear_quadratic']`
- `positive` (required): `CONDITIONING`
- `negative` (required): `CONDITIONING`
- `latent_image` (required): `LATENT`
- `start_at_step` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 10000}}`
- `end_at_step` (required): `INT`
  - Options: `{{'default': 10000, 'min': 0, 'max': 10000}}`
- `return_with_leftover_noise` (required): `['disable', 'enable']`

#### Outputs

- `LATENT`: `LATENT`

## TARA-LLM


### Applicability

**Score:** 85/100

**Reason:** This advanced version of KSampler offers additional features such as noise control and step customization which can be useful for fine-tuning text to image generation workflows.

### Metadata

---

### Tara Advanced LLM Composition Node (`TaraAdvancedComposition`)

**Description:**

**Module:** `ComfyUI-Tara-LLM-Integration`

#### Inputs

- `llm_config` (required): `TARA_LLM_CONFIG`
  - Options: `{{'forceInput': True}}`
- `guidance` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `prompt` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `positive` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`
- `negative` (optional): `STRING`
  - Options: `{{'multiline': True, 'forceInput': True}}`

#### Outputs

- `output_text`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for generating text with LoRA model support by composing multiple LLMs.

### Metadata

---

### Tara LLM Config Node (`TaraLLMConfig`)

**Description:**

**Module:** `ComfyUI-Tara-LLM-Integration`

#### Inputs

- `base_url` (required): `STRING`
  - Options: `{{'default': 'http://localhost:11434/v1'}}`
- `api_key` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`
- `llm_model` (required): `STRING`
  - Options: `{{'default': 'mixtral'}}`
- `temperature` (required): `FLOAT`
  - Options: `{{'default': 0.4}}`
- `seed` (required): `INT`
  - Options: `{{'default': 42}}`
- `max_tokens` (required): `INT`
  - Options: `{{'default': 1000}}`
- `top_p` (required): `FLOAT`
  - Options: `{{'default': 1}}`
- `frequency_penalty` (required): `FLOAT`
  - Options: `{{'default': 0}}`
- `presence_penalty` (required): `FLOAT`
  - Options: `{{'default': 0}}`
- `timeout` (required): `INT`
  - Options: `{{'default': 60}}`

#### Outputs

- `llm_config`: `TARA_LLM_CONFIG`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for generating text with LoRA model support by configuring LLM settings such as temperature, seed, and max tokens.

### Metadata

---

### Tara Preset LLM Config Node (`TaraPresetLLMConfig`)

**Description:**

**Module:** `ComfyUI-Tara-LLM-Integration`

#### Inputs

- `llm_models` (required): `['openai/gpt-3.5-turbo', 'openai/gpt-4-turbo-preview', 'groq/llama2-70b-4096', 'groq/llama3-70b-8192', 'groq/llama3-8b-8192', 'groq/mixtral-8x7b-32768', 'groq/gemma-7b-it', 'together/coming-soon']`
- `temperature` (required): `FLOAT`
  - Options: `{{'default': 0.4}}`
- `seed` (required): `INT`
  - Options: `{{'default': 42}}`
- `max_tokens` (required): `INT`
  - Options: `{{'default': 1000}}`
- `top_p` (required): `FLOAT`
  - Options: `{{'default': 1}}`
- `frequency_penalty` (required): `FLOAT`
  - Options: `{{'default': 0}}`
- `presence_penalty` (required): `FLOAT`
  - Options: `{{'default': 0}}`
- `timeout` (required): `INT`
  - Options: `{{'default': 60}}`
- `use_loader` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `loader_temporary` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `api_key` (optional): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`

#### Outputs

- `llm_config`: `TARA_LLM_CONFIG`


### Applicability

**Score:** 100/100

**Reason:** This node directly configures LLM settings which is essential for text to image generation with LoRA model support.

### Metadata

---

### Tara Advanced LLM Node (`TaraPrompterAdvanced`)

**Description:**

**Module:** `ComfyUI-Tara-LLM-Integration`

#### Inputs

- `llm_config` (required): `TARA_LLM_CONFIG`
  - Options: `{{'forceInput': True}}`
- `guidance` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `prompt_positive` (required): `STRING`
  - Options: `{{'multiline': True}}`
- `prompt_negative` (optional): `STRING`
  - Options: `{{'multiline': True}}`

#### Outputs

- `positive`: `STRING`
- `negative`: `STRING`

## UNKNOWN


### Applicability

**Score:** 80/100

**Reason:** Although this node can be used for text to image generation, it requires additional nodes to handle LLM configuration which reduces its utility.

### Metadata

---

### VAE Decoder PoP (`VAEDecoderPoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `samples` (required): `LATENT`
- `vae_name` (required): `['hunyuan_video_vae_bf16.safetensors']`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node generates images from latent samples which can be used in text-to-image generation with LoRA model support.

### Metadata

---

### VAE Encoder PoP (`VAEEncoderPoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `pixels` (required): `IMAGE`
- `vae_name` (required): `['hunyuan_video_vae_bf16.safetensors']`

#### Outputs

- `samples`: `LATENT`

## UTILS


### Applicability

**Score:** 80/100

**Reason:** This node encodes images into latent samples which is a necessary step for text-to-image generation with LoRA model support.

### Metadata

---

### ✨ Auto-LLM-Text (`Auto-LLM-Text`)

**Description:**

**Module:** `ComfyUI-decadetw-auto-prompt-llm`

#### Inputs

- `clip` (required): `CLIP`
- `llm_text_result_append_enabled` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `text_prompt_postive` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': '1girl,'}}`
- `text_prompt_negative` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True}}`
- `llm_keep_your_prompt_ahead` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_recursive_use` (required): `BOOLEAN`
  - Options: `{{'default': False, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_apiurl` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'http://localhost:1234/v1/chat/completions'}}`
- `llm_apikey` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'lm-studio'}}`
- `llm_api_model_name` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'llama3.1'}}`
- `llm_text_max_token` (required): `INT`
  - Options: `{{'default': 50, 'min': 10, 'max': 1024, 'step': 1}}`
- `llm_text_tempture` (required): `FLOAT`
  - Options: `{{'default': 0.3, 'min': -2.0, 'max': 2.0, 'step': 0.01}}`
- `llm_text_system_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'You are an AI prompt word engineer. Use the provided keywords to create a beautiful composition. Only the prompt words are needed, not your feelings. Customize the style, scene, decoration, etc., and be as detailed as possible without endings.'}}`
- `llm_text_ur_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'A superstar on stage.'}}`
- `llm_before_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_before_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`
- `llm_post_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_post_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`

#### Outputs

- `postive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `orignal-postive`: `STRING`
- `orignal-negative`: `STRING`
- `🌀LLM-Text`: `STRING`
- `🌀LLM-Vision`: `STRING`
- `🌀postive+LLM-Text+LLM-Vision`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node provides a comprehensive set of inputs and outputs that can be used for text to image generation with LoRA model support, including clip, llm_text_result_append_enabled, and llm_vision_result_append_enabled.

### Metadata

---

### ✨ Auto-LLM-Text-Vision (`Auto-LLM-Text-Vision`)

**Description:**

**Module:** `ComfyUI-decadetw-auto-prompt-llm`

#### Inputs

- `clip` (required): `CLIP`
- `image_to_llm_vision` (required): `IMAGE`
- `is_trigger_every_generated` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_text_result_append_enabled` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_vision_result_append_enabled` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `text_prompt_postive` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': '1girl,'}}`
- `text_prompt_negative` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True}}`
- `llm_keep_your_prompt_ahead` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_recursive_use` (required): `BOOLEAN`
  - Options: `{{'default': False, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_apiurl` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'http://localhost:1234/v1/chat/completions'}}`
- `llm_apikey` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'lm-studio'}}`
- `llm_api_model_name` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'llama3.1'}}`
- `llm_text_max_token` (required): `INT`
  - Options: `{{'default': 50, 'min': 10, 'max': 1024, 'step': 1}}`
- `llm_text_tempture` (required): `FLOAT`
  - Options: `{{'default': 0.3, 'min': -2.0, 'max': 2.0, 'step': 0.01}}`
- `llm_text_system_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'You are an AI prompt word engineer. Use the provided keywords to create a beautiful composition. Only the prompt words are needed, not your feelings. Customize the style, scene, decoration, etc., and be as detailed as possible without endings.'}}`
- `llm_text_ur_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'A superstar on stage.'}}`
- `llm_vision_max_token` (required): `INT`
  - Options: `{{'default': 50, 'min': 10, 'max': 1024, 'step': 1}}`
- `llm_vision_tempture` (required): `FLOAT`
  - Options: `{{'default': 0.8, 'min': -2.0, 'max': 2.0, 'step': 0.01}}`
- `llm_vision_system_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'This is a chat between a user and an assistant. The assistant is helping the user to describe an image.'}}`
- `llm_vision_ur_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': "What's in this image?"}}`
- `llm_before_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_before_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`
- `llm_post_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_post_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`

#### Outputs

- `postive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `orignal-postive`: `STRING`
- `orignal-negative`: `STRING`
- `🌀LLM-Text`: `STRING`
- `🌀LLM-Vision`: `STRING`
- `🌀postive+LLM-Text+LLM-Vision`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node provides a comprehensive set of inputs and outputs that can be used for text to image generation with LoRA model support, including clip, image_to_llm_vision, and llm_vision_result_append_enabled.

### Metadata

---

### ✨ Auto-LLM-Vision (`Auto-LLM-Vision`)

**Description:**

**Module:** `ComfyUI-decadetw-auto-prompt-llm`

#### Inputs

- `clip` (required): `CLIP`
- `image_to_llm_vision` (required): `IMAGE`
- `llm_vision_result_append_enabled` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `text_prompt_postive` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': '1girl,'}}`
- `text_prompt_negative` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True}}`
- `llm_keep_your_prompt_ahead` (required): `BOOLEAN`
  - Options: `{{'default': True, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_recursive_use` (required): `BOOLEAN`
  - Options: `{{'default': False, 'label_off': 'OFF', 'label_on': 'ON'}}`
- `llm_apiurl` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'http://localhost:1234/v1/chat/completions'}}`
- `llm_apikey` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'lm-studio'}}`
- `llm_api_model_name` (required): `STRING`
  - Options: `{{'multiline': False, 'default': 'llama3.1'}}`
- `llm_vision_max_token` (required): `INT`
  - Options: `{{'default': 50, 'min': 10, 'max': 1024, 'step': 1}}`
- `llm_vision_tempture` (required): `FLOAT`
  - Options: `{{'default': 0.8, 'min': -2.0, 'max': 2.0, 'step': 0.01}}`
- `llm_vision_system_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': 'This is a chat between a user and an assistant. The assistant is helping the user to describe an image.'}}`
- `llm_vision_ur_prompt` (required): `STRING`
  - Options: `{{'multiline': True, 'dynamicPrompts': True, 'default': "What's in this image?"}}`
- `llm_before_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_before_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`
- `llm_post_action_cmd_feedback_type` (required): `['Pass', 'just-call', 'LLM-USER-PROMPT', 'LLM-VISION-IMG_PATH']`
- `llm_post_action_cmd` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`

#### Outputs

- `postive`: `CONDITIONING`
- `negative`: `CONDITIONING`
- `orignal-postive`: `STRING`
- `orignal-negative`: `STRING`
- `🌀LLM-Text`: `STRING`
- `🌀LLM-Vision`: `STRING`
- `🌀postive+LLM-Text+LLM-Vision`: `STRING`



### Applicability

**Score:** 100/100

**Reason:** This node provides a comprehensive set of inputs and outputs that can be used for text to image generation with LoRA model support, including clip, image_to_llm_vision, and llm_vision_result_append_enabled.

### Metadata

---
