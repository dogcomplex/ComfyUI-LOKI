# Filtered Nodes for: Transfer style from reference image to input image

Total Available Nodes: 456
Batch Size: 4
Estimated Processing Time: 9.5 minutes

## Results

### 2🐕Fuzzy fast intensity (`EG_ZZ_MHHT`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `Fuzzyintensity` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 150, 'step': 1, 'display': 'slider'}}`

#### Outputs

- `MASK`: `MASK`

## 2🐕/⛱️MASK


### Applicability

**Score:** 41/100

**Reason:** This node applies a fuzzy filter to the mask, but its direct relevance to transferring style from reference image to input image is limited.

### Metadata

---

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

**Score:** 61/100

**Reason:** This node generates a seam mask based on the input mask, which can be useful for guiding the transfer of style in certain scenarios.

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

**Score:** 81/100

**Reason:** This node exchanges or swaps the mask and image inputs, making it essential for preparing the input images for style transfer.

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

**Score:** 41/100

**Reason:** This node allows arbitrary cutting or merging of masks, but its direct relevance to transferring style from reference image to input image is limited without additional context.

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

**Reason:** This node directly modifies a mask based on user input, which is essential for transferring style from reference to input image.

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

**Reason:** Similar to Node 1, this node also expands the mask but with less control over extend size, making it moderately useful for the workflow goal.

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

**Score:** 91/100

**Reason:** This node provides more options for blurring white edges in a mask, including kernel size and sigma, making it very useful for refining the style transfer process.

### Metadata

---

### 2🐕Mask edges blurred (`EG_ZZ_BYYH`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `mask` (required): `MASK`
- `Fuzzy_weight` (optional): `INT`
  - Options: `{{'default': 50, 'min': 1, 'max': 1000, 'step': 2}}`
- `Blur_size` (optional): `INT`
  - Options: `{{'default': 50, 'min': 1, 'max': 1000, 'step': 1}}`

#### Outputs

- `mask`: `MASK`


### Applicability

**Score:** 71/100

**Reason:** This node offers some control over fuzzy weight and blur size but lacks the comprehensive options of Node 3, making it moderately useful for the workflow goal.

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

**Reason:** This custom template node can be used to create a new template for the reference image, which would be useful for transferring style from one image to another.

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

**Reason:** This node allows for detailed control over scene composition, including background, sky, indoor, outdoor, building, and atmosphere. It is essential for achieving a specific style transfer.

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

**Reason:** This node provides options for controlling lighting perception and effects, which can be useful in achieving the desired style transfer, but it may not be as directly relevant as other nodes.

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

**Score:** 41/100

**Reason:** This node offers a wide range of graphic effects and art styles, which could potentially be used to achieve the desired style transfer. However, its relevance is somewhat limited by the specificity of the workflow goal.

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

**Score:** 91/100

**Reason:** This node provides extensive control over lens class, including perspective, positioning, action, composition method, character lens, and camera lens. It is highly relevant to achieving a specific style transfer.

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

**Reason:** This node seems highly relevant as it deals with item categories which could be useful in transferring style from reference image to input image.

### Metadata

---

### 2🐕Image cropping data stitching (`EG_TX_CJPJ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `original_image` (required): `IMAGE`
- `cropped_image` (required): `IMAGE`
- `Crop_data` (required): `COORDS`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** This node stitches cropping data together and can be used as a supporting node for the workflow goal by preparing the input images for style transfer.

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

**Score:** 91/100

**Reason:** This node crops an image based on a mask and can be used to prepare the input images for style transfer.

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

**Reason:** This node loads an image which is a necessary step in transferring style from reference image to input image.

### Metadata

---

### 2🐕Saturation migration (`EG_SCQY_BHDQY`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `source_image` (required): `IMAGE`
- `target_image` (required): `IMAGE`

#### Outputs

- `result_image`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it transfers color information (saturation) between two images, aligning with the workflow goal of transferring style.

### Metadata

---

### 2🐕Regular color migration (`EG_SCQY_QBQY`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `source_image` (required): `IMAGE`
- `target_image` (required): `IMAGE`
- `strength` (optional): `FLOAT`
  - Options: `{{'default': 50, 'min': 0, 'max': 100, 'step': 1, 'precision': 100, 'display': 'slider'}}`

#### Outputs

- `result_image`: `IMAGE`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it transfers regular color information between two images, supporting the workflow goal of transferring style.

### Metadata

---

### 2🐕Hue migration (`EG_SCQY_SXQY`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `source_image` (required): `IMAGE`
- `target_image` (required): `IMAGE`

#### Outputs

- `result_image`: `IMAGE`


### Applicability

**Score:** 85/100

**Reason:** This node is very useful as it transfers hue information between two images, aligning with the workflow goal of transferring style.

### Metadata

---

### 2🐕Do not retain brightness (`EG_YSQY_BBLLD`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `source_image` (required): `IMAGE`
- `target_image` (required): `IMAGE`

#### Outputs

- `result_image`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** This node does not retain brightness which might be useful if you want to intentionally remove or alter brightness in your transferred image.

### Metadata

---

### 2🐕Preserve brightness (`EG_YSQY_BLLD`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `source_image` (required): `IMAGE`
- `target_image` (required): `IMAGE`

#### Outputs

- `result_image`: `IMAGE`

## 2🐕/🖼️IMAGE/🪞FILTER


### Applicability

**Score:** 80/100

**Reason:** This node preserves brightness making it very useful for maintaining the original brightness of the input and reference images during style transfer.

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

**Score:** 100/100

**Reason:** This node allows for color adjustments which is essential for fine-tuning the color palette of the transferred image to match the reference image.

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

**Reason:** This node applies conventional filters which might be marginally useful if you want to add a specific filter effect to your transferred image, but it does not directly contribute to style transfer.

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

**Reason:** This node generates an empty latent space that can be used for the style transfer process.

### Metadata

---

### 2🐕Redraw encoder (`ER_JBCH`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `pixels` (required): `IMAGE`
- `vae` (required): `VAE`
- `mask` (required): `MASK`
- `grow_mask_by` (required): `INT`
  - Options: `{{'default': 6, 'min': 0, 'max': 64, 'step': 1}}`
- `use_original_image` (required): `['original', 'filling']`

#### Outputs

- `LATENT`: `LATENT`

## AI GENERATION


### Applicability

**Score:** 90/100

**Reason:** This node redraws the encoder and is crucial in generating the latent representation required for style transfer.

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

**Reason:** This node directly generates an image with a specific style based on a reference image, making it essential for transferring style from one image to another.

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

**Score:** 100/100

**Reason:** This node directly generates an art style based on a reference image, making it essential for transferring style from one image to another.

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

**Score:** 81/100

**Reason:** This node can generate emotions that could be used as prompts or styles for the transfer process.

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

**Score:** 41/100

**Reason:** This node can generate times of day that could be used as prompts or styles for the transfer process, but it is not essential for this workflow goal.

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

**Score:** 81/100

**Reason:** This node loads an embedding which can be used as a starting point for the style transfer process.

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

**Score:** 100/100

**Reason:** This node loads a pre-trained model that can be directly used for transferring style from reference image to input image.

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

**Score:** 41/100

**Reason:** This node generates prompts but does not directly contribute to the style transfer process. However, it can be useful as a supporting node for generating text conditions.

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

**Reason:** This node is essential for saving the output images after style transfer.

### Metadata

---

### Wildcards (`Wildcards`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `textfile` (required): `[['animals.txt', 'art-styles.txt', 'clothes.txt', 'colours.txt', 'descriptors.txt', 'fabrics.txt', 'foods.txt', 'household-objects.txt', 'landscapes.txt', 'poses.txt']]`
- `keyword` (required): `STRING`
  - Options: `{{'default': '__wildcard__', 'multiline': False}}`
- `entries_returned` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 10, 'step': 1}}`
- `clip` (optional): `CLIP`
- `seed` (optional): `INT`
  - Options: `{{'forceInput': True}}`
- `text` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`
- `text`: `STRING`

## CHIBI-NODES/IMAGE


### Applicability

**Score:** 41/100

**Reason:** This node can be used as a supporting node to sample latents for the style transfer process.

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

**Score:** 61/100

**Reason:** This node is moderately useful for adding text to the input image before style transfer or displaying the output after style transfer.

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

**Score:** 80/100

**Reason:** This node provides useful information about image size which could be used in conjunction with other nodes for the workflow goal.

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

**Score:** 81/100

**Reason:** This node provides a seed value which is crucial for reproducibility and consistency in style transfer tasks.

### Metadata

---

### ConditionTextMulti (`ConditionTextMulti`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `clip` (required): `CLIP`
- `first` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`
- `second` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`
- `third` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`
- `fourth` (optional): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': True}}`

#### Outputs

- `CLIP`: `CLIP`
- `first`: `CONDITIONING`
- `second`: `CONDITIONING`
- `third`: `CONDITIONING`
- `fourth`: `CONDITIONING`


### Applicability

**Score:** 40/100

**Reason:** This node allows multi-conditioning of text on an input clip but its direct relevance to style transfer is limited.

### Metadata

---

### Int2String (`Int2String`)

**Description:**

**Module:** `ComfyUI-Chibi-Nodes`

#### Inputs

- `Int` (required): `INT`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it can convert integer values into strings that may be used in other nodes.

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

**Reason:** This node calculates the square root of its input, which could be used to normalize or preprocess the input data for the style transfer task.

### Metadata

---

### Conditioning area scale by ratio (`DF_Conditioning_area_scale_by_ratio`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `conditioning` (required): `CONDITIONING`
  - Options: `{{'forceInput': False}}`
- `modifier` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `strength_modifier` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`

#### Outputs

- `CONDITIONING`: `CONDITIONING`

## DERFUU_NODES/MODDED NODES/IMAGE


### Applicability

**Score:** 90/100

**Reason:** This node scales the conditioning area by a ratio which can be used to adjust the style transfer process, making it very useful for this workflow goal.

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

**Reason:** This node allows scaling an image by a specific ratio, which is directly relevant to resizing the reference image.

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

**Score:** 61/100

**Reason:** This node scales an image to a specific side length, but it may not be as precise or flexible as the first node for some workflow goals.

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

**Score:** 41/100

**Reason:** This node scales latent data by ratio, which might be useful if working with latent space transformations.

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

**Score:** 61/100

**Reason:** This node scales latent data to a specific side length, similar to the second image scaling node, but for latent data.

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

**Score:** 90/100

**Reason:** This node is very useful for scheduling batch prompts and can be used in conjunction with other nodes to achieve the workflow goal.

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

**Score:** 95/100

**Reason:** This node is essential for scheduling batch prompts with specific dimensions and can be used in conjunction with other nodes to achieve the workflow goal.

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

**Score:** 85/100

**Reason:** This node is very useful for scheduling batch prompts with latent input and can be used in conjunction with other nodes to achieve the workflow goal.

### Metadata

---

### Batch String Schedule 📅🅕🅝 (`BatchStringSchedule`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '"0" :"",\n"11" :"",\n"23" :"",\n"35" :"",\n"47" :"",\n"59" :"",\n"71" :"",\n"83" :"",\n"95" :"",\n"107" :"",\n"119" :""\n'}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
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

- `POS`: `STRING`
- `NEG`: `STRING`


### Applicability

**Score:** 61/100

**Reason:** This node can schedule batch strings and may be useful as a supporting node for generating text inputs or outputs.

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

**Score:** 81/100

**Reason:** This node can schedule batch values and is specifically designed for latent input, making it very useful for this workflow goal.

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

**Reason:** This node is essential for displaying a progress frame with positive and negative text in the style transfer process.

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

**Reason:** This node can be used to concatenate frames but its direct relevance to the workflow goal is moderate.

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

**Score:** 61/100

**Reason:** This node is moderately useful as it initializes a new frame with positive and negative text for the style transfer process.

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

**Reason:** Concatenates two strings which can be used in style transfer by combining text or labels.

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

**Score:** 40/100

**Reason:** Selects images based on a schedule and current frame number, which could be useful for style transfer with time-dependent inputs.

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

**Score:** 80/100

**Reason:** This node appears to be a scheduling node that can handle text and frame-related inputs which are relevant to the workflow goal.

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

**Score:** 90/100

**Reason:** This node is very similar to Node 3 but seems to be an end-point for scheduling nodes in the NodeFlow module.

### Metadata

---

### CosWave 📅🅕🅝 (`CosWave`)

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

**Score:** 41/100

**Reason:** This node can be used to create a wave pattern in the input image, but its direct relevance to transferring style from reference image is limited.

### Metadata

---

### InvCosWave 📅🅕🅝 (`InvCosWave`)

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

**Score:** 42/100

**Reason:** Similar to CosWave, InvCosWave creates a wave pattern and has limited direct relevance to transferring style from reference image.

### Metadata

---

### InvSinWave 📅🅕🅝 (`InvSinWave`)

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

**Score:** 43/100

**Reason:** InvSinWave also creates a wave pattern and its direct relevance to the workflow goal is minimal.

### Metadata

---

### Lerp 📅🅕🅝 (`Lerp`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `num_Images` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `strength` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999, 'step': 1.0}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`


### Applicability

**Score:** 61/100

**Reason:** Lerp can be used to interpolate between multiple images, which could be useful in transferring style from reference image by blending different styles or frames.

### Metadata

---

### SinWave 📅🅕🅝 (`SinWave`)

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

**Reason:** This node generates a sine wave which could be useful in generating oscillations for style transfer, but its direct relevance is limited.

### Metadata

---

### 🔄 Isulion Multiple Prompt Generator (`IsulionMultiplePromptGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `selection_mode` (required): `['Theme Selection', 'All Themes']`
  - Options: `{{'default': 'Theme Selection'}}`
- `custom_subject` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True, 'placeholder': 'Enter custom subject...'}}`
- `custom_location` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True, 'placeholder': 'Enter custom location...'}}`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `category_animation_entertainment` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Animation & Entertainment'}}`
- `category_architectural_spaces` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Architectural & Spaces'}}`
- `category_art_styles_techniques` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Art Styles & Techniques'}}`
- `category_character_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Character Art'}}`
- `category_dark_horror` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Dark & Horror'}}`
- `category_food` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Food'}}`
- `category_holiday_themes` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Holiday Themes'}}`
- `category_nature_environment` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Nature & Environment'}}`
- `category_photography_fashion` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Photography & Fashion'}}`
- `category_post-apocalyptic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Post-Apocalyptic'}}`
- `category_random` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Random'}}`
- `category_science_fiction_fantasy` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Science Fiction & Fantasy'}}`
- `category_surreal_dreams` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Surreal & Dreams'}}`
- `category_vintage_historical` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': 'Select All Vintage & Historical'}}`
- `🧺_50s_commercial` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🧺 50s Commercial'}}`
- `🎨_abstract` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎨 Abstract'}}`
- `📺_animation_cartoon` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📺 Animation Cartoon'}}`
- `🎌_anime` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎌 Anime'}}`
- `🏛️_architectural` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏛️ Architectural'}}`
- `🖼️_binet_surreal` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🖼️ Binet Surreal'}}`
- `🧬_bio_organic_technology` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🧬 Bio-Organic Technology'}}`
- `😄_caricature` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '😄 Caricature'}}`
- `👤_character_designer` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👤 Character Designer'}}`
- `🦄_chimera_animals` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🦄 Chimera Animals'}}`
- `🐰_chimera_cute_animals` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🐰 Chimera Cute Animals'}}`
- `🏮_chinese_new_year` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏮 Chinese New Year'}}`
- `🎄_christmas` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎄 Christmas'}}`
- `🎬_cinema_studio` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎬 Cinema Studio'}}`
- `🏺_clay_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏺 Clay Art'}}`
- `📚_comic_book` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📚 Comic Book'}}`
- `🎨_concept_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎨 Concept Art'}}`
- `🖍️_crayon_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🖍️ Crayon Art'}}`
- `💎_crystalpunk` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💎 Crystalpunk'}}`
- `🍳_culinary_food` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🍳 Culinary/Food'}}`
- `👗_curvy_fashion` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👗 Curvy Fashion'}}`
- `🌆_cyberpunk` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌆 Cyberpunk'}}`
- `👹_dia_de_los_muertos` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👹 Dia de los Muertos'}}`
- `💻_digital_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💻 Digital Art'}}`
- `💠_dimension_3d` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💠 Dimension 3D'}}`
- `🎡_disney` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎡 Disney'}}`
- `🎬_dreamworks` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎬 Dreamworks'}}`
- `🎲_dynamic_random` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎲 Dynamic Random'}}`
- `🐰_easter` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🐰 Easter'}}`
- `✨_enchanted_fantasy` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '✨ Enchanted Fantasy'}}`
- `📸_essential_realistic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📸 Essential Realistic'}}`
- `🕰️_essential_vintage` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🕰️ Essential Vintage'}}`
- `💫_ethereal_dreams` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💫 Ethereal Dreams'}}`
- `🔬_experimental_art` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🔬 Experimental Art'}}`
- `⚔️_fantasy` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '⚔️ Fantasy'}}`
- `⚔️_futuristic_battlefield` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '⚔️ Futuristic Battlefield'}}`
- `🌃_futuristic_city` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌃 Futuristic City'}}`
- `🌆_futuristic_city_metropolis` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌆 Futuristic City Metropolis'}}`
- `🚀_futuristic_sci_fi` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🚀 Futuristic Sci-Fi'}}`
- `🍃_ghibli` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🍃 Ghibli'}}`
- `🎃_halloween` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎃 Halloween'}}`
- `👻_halloween_ethereal` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👻 Halloween Ethereal'}}`
- `🏛️_historical_monuments` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏛️ Historical Monuments'}}`
- `👻_horror` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👻 Horror'}}`
- `🎨_impressionist` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎨 Impressionist'}}`
- `📱_instagram` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📱 Instagram'}}`
- `📱_instagram_lifestyle` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📱 Instagram Lifestyle'}}`
- `🏠_interior_spaces` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏠 Interior Spaces'}}`
- `🎯_logo` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎯 Logo'}}`
- `📚_manga_panel` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📚 Manga Panel'}}`
- `🦸_marvel` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🦸 Marvel'}}`
- `🔬_microscopic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🔬 Microscopic'}}`
- `⬜_minimalist` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '⬜ Minimalist'}}`
- `⚔️_miura_dark_fantasy` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '⚔️ Miura Dark Fantasy'}}`
- `🌿_nature` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌿 Nature'}}`
- `🎆_new_year's_eve` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': "🎆 New Year's Eve"}}`
- `🎬_nolan_epic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎬 Nolan Epic'}}`
- `🕴️‍♂️_peaky_blinders` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🕴️\u200d♂️ Peaky Blinders'}}`
- `💫_pixar` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💫 Pixar'}}`
- `🌪️_post_apocalyptic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌪️ Post Apocalyptic'}}`
- `🧩_puzzle_dimension` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🧩 Puzzle Dimension'}}`
- `📚_school_manga` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📚 School Manga'}}`
- `🚀_sci_fi` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🚀 Sci-Fi'}}`
- `📱_selfie` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📱 Selfie'}}`
- `💗_spectral_mist` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '💗 Spectral Mist'}}`
- `🍀_st._patrick's_day` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': "🍀 St. Patrick's Day"}}`
- `🚀_star_wars` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🚀 Star Wars'}}`
- `⚙️_steampunk` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '⚙️ Steampunk'}}`
- `🎭_stop_motion` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎭 Stop Motion'}}`
- `🥙_street_food_kebab` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🥙 Street Food Kebab'}}`
- `🦃_thanksgiving` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🦃 Thanksgiving'}}`
- `🌊_underwater_civilization` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🌊 Underwater Civilization'}}`
- `🏙️_urban_tag` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏙️ Urban Tag'}}`
- `💘_valentine's_day` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': "💘 Valentine's Day"}}`
- `🏠_village_world` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🏠 Village World'}}`
- `📸_vintage_1800s_photography` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '📸 Vintage 1800s Photography'}}`
- `👴_vintage_anthropomorphic` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '👴 Vintage Anthropomorphic'}}`
- `🎨_watercolor` (optional): `BOOLEAN`
  - Options: `{{'default': False, 'label': '🎨 Watercolor'}}`
- `theme_names` (optional): `['[Animation & Entertainment]', '[Architectural & Spaces]', '[Art Styles & Techniques]', '[Character Art]', '[Dark & Horror]', '[Food]', '[Holiday Themes]', '[Nature & Environment]', '[Photography & Fashion]', '[Post-Apocalyptic]', '[Random]', '[Science Fiction & Fantasy]', '[Surreal & Dreams]', '[Vintage & Historical]', '🧺 50s Commercial', '🎨 Abstract', '📺 Animation Cartoon', '🎌 Anime', '🏛️ Architectural', '🖼️ Binet Surreal', '🧬 Bio-Organic Technology', '😄 Caricature', '👤 Character Designer', '🦄 Chimera Animals', '🐰 Chimera Cute Animals', '🏮 Chinese New Year', '🎄 Christmas', '🎬 Cinema Studio', '🏺 Clay Art', '📚 Comic Book', '🎨 Concept Art', '🖍️ Crayon Art', '💎 Crystalpunk', '🍳 Culinary/Food', '👗 Curvy Fashion', '🌆 Cyberpunk', '👹 Dia de los Muertos', '💻 Digital Art', '💠 Dimension 3D', '🎡 Disney', '🎬 Dreamworks', '🎲 Dynamic Random', '🐰 Easter', '✨ Enchanted Fantasy', '📸 Essential Realistic', '🕰️ Essential Vintage', '💫 Ethereal Dreams', '🔬 Experimental Art', '⚔️ Fantasy', '⚔️ Futuristic Battlefield', '🌃 Futuristic City', '🌆 Futuristic City Metropolis', '🚀 Futuristic Sci-Fi', '🍃 Ghibli', '🎃 Halloween', '👻 Halloween Ethereal', '👻 Halloween Ethereal', '🏛️ Historical Monuments', '👻 Horror', '🎨 Impressionist', '📱 Instagram', '📱 Instagram Lifestyle', '🏠 Interior Spaces', '🎯 Logo', '📚 Manga Panel', '🦸 Marvel', '🔬 Microscopic', '⬜ Minimalist', '⚔️ Miura Dark Fantasy', '⚔️ Miura Dark Fantasy', '🌿 Nature', "🎆 New Year's Eve", '🎬 Nolan Epic', '🕴️\u200d♂️ Peaky Blinders', '💫 Pixar', '🌪️ Post Apocalyptic', '🧩 Puzzle Dimension', '📚 School Manga', '🚀 Sci-Fi', '📱 Selfie', '💗 Spectral Mist', "🍀 St. Patrick's Day", '🚀 Star Wars', '⚙️ Steampunk', '🎭 Stop Motion', '🥙 Street Food Kebab', '🦃 Thanksgiving', '🌊 Underwater Civilization', '🌊 Underwater Civilization', '🏙️ Urban Tag', "💘 Valentine's Day", '🏠 Village World', '📸 Vintage 1800s Photography', '👴 Vintage Anthropomorphic', '🎨 Watercolor']`
  - Options: `{{'default': '[Animation & Entertainment]', 'hidden': True}}`

#### Outputs

- `positive`: `STRING` (LIST)
- `name`: `STRING` (LIST)

## ISULION/CHARACTER


### Applicability

**Score:** 80/100

**Reason:** This node can generate multiple prompts based on various themes, which could be useful for generating diverse styles. However, it may require manual selection and customization to achieve the desired output.

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

**Score:** 90/100

**Reason:** This node generates clothing items with specific styles, which could be directly used as a reference image or input for style transfer. It also allows randomization of clothing items, making it a very useful node for this workflow goal.

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

**Score:** 70/100

**Reason:** This node generates epochs with specific historical periods, which could be used to create reference images or inputs for style transfer. However, the output may require additional processing or customization to achieve the desired style transfer result.

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

**Score:** 100/100

**Reason:** This node can generate a prompt with a specific theme and style that can be used as the reference for transferring style from reference image to input image.

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

**Reason:** This node enhances the input prompt to improve style transfer results, which is directly relevant to the workflow goal.

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

**Score:** 100/100

**Reason:** This node mixes two styles together, which is exactly what the workflow goal requires for transferring style from a reference image to an input image.

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

**Reason:** This node can generate an image collage using the style of the reference image, making it very useful for the workflow goal.

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

**Score:** 80/100

**Reason:** This node provides pre-defined dimensions that can be used for the transfer process, making it moderately useful.

### Metadata

---

### Join String Multi (`JoinStringMulti`)

**Description:**


Creates single string, or a list of strings, from  
multiple input strings.  
You can set how many inputs the node has,  
with the **inputcount** and clicking update.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 1000, 'step': 1}}`
- `string_1` (required): `STRING`
  - Options: `{{'default': '', 'forceInput': True}}`
- `string_2` (required): `STRING`
  - Options: `{{'default': '', 'forceInput': True}}`
- `delimiter` (required): `STRING`
  - Options: `{{'default': ' ', 'multiline': False}}`
- `return_list` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `string`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node can be used to concatenate strings that may contain information about the reference and input images, making it very useful for this workflow goal.

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

**Score:** 80/100

**Reason:** This node draws tracking data from CreateInstanceDiffusionTracking-node and visualizes it on an image, which can be useful for understanding the transfer process.

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

**Score:** 80/100

**Reason:** This node creates masks based on the normalized amplitude which is relevant for transferring style from reference image to input image.

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

**Score:** 60/100

**Reason:** This node offsets masks based on the normalized amplitude but does not directly contribute to transferring style from reference image to input image.

### Metadata

---

### Create Fade Mask (`CreateFadeMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `frames` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 10000, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`
- `interpolation` (required): `['linear', 'ease_in', 'ease_out', 'ease_in_out']`
- `start_level` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `midpoint_level` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `end_level` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `midpoint_frame` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 4096, 'step': 1}}`

#### Outputs

- `MASK`: `MASK`

## KJNODES/EXPERIMENTAL


### Applicability

**Score:** 80/100

**Reason:** This node can create a fade mask that could be used as a supporting node for the workflow goal of transferring style from reference image to input image.

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

**Score:** 40/100

**Reason:** This node can perturb the weights of a model but its direct relevance to transferring style from reference image to input image is limited.

### Metadata

---

### Fast Preview (`FastPreview`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `format` (required): `['JPEG', 'PNG', 'WEBP']`
  - Options: `{{'default': 'JPEG'}}`
- `quality` (required): `INT`
  - Options: `{{'default': 75, 'min': 1, 'max': 100, 'step': 1}}`


### Applicability

**Score:** 80/100

**Reason:** This node provides a fast preview of an image, which could be useful for evaluating the output of a style transfer operation before proceeding with further processing.

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

**Score:** 90/100

**Reason:** This node loads a LoRA (Learning Rate Adaptation) model and applies it to a diffusion model, which is directly relevant to the task of modifying the style of an image.

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

**Reason:** This node allows for fine-grained control over the modification of individual blocks in a diffusion model, making it highly relevant and useful for the style transfer task.

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

**Score:** 81/100

**Reason:** This node is essential for transferring style from reference image to input image as it allows scheduling GLIGEN text box positions in a batch.

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

**Score:** 61/100

**Reason:** This node is moderately useful for the workflow goal as it interpolates coordinates based on a curve, which can be helpful in fine-tuning the style transfer process.

### Metadata

---

### Pathch Sage Attention KJ (`PathchSageAttentionKJ`)

**Description:**

Experimental node for patching attention mode.

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (required): `MODEL`
- `sage_attention` (required): `['disabled', 'auto', 'sageattn_qk_int8_pv_fp16_cuda', 'sageattn_qk_int8_pv_fp16_triton', 'sageattn_qk_int8_pv_fp8_cuda']`
  - Patch comfy attention to use sageattn.
  - Options: `{{'default': False, 'tooltip': 'Patch comfy attention to use sageattn.'}}`

#### Outputs

- `MODEL`: `MODEL`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for patching attention mode in the model, which is crucial for the style transfer process.

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

**Reason:** Directly schedules azimuth and elevation conditions for SV3D model, which is essential for style transfer from reference image to input image.

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

**Reason:** Calls StabilityAI API for text-to-image or image-to-image generation, which is essential for transferring style from a reference image to an input image.

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

**Reason:** Directly schedules azimuth and elevation conditions for Stable Zero123 model, which is essential for style transfer from reference image to input image.

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

**Reason:** This node directly applies a style model to the input image with adjustable strength, making it essential for transferring style from reference images.

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

**Score:** 40/100

**Reason:** This node compiles a model flux advanced but has limited utility in this specific workflow as it doesn"t directly apply style or adjust strength.

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

**Reason:** This node can capture real-time images from a webcam and potentially be used as input for the style transfer process.

### Metadata

---

### Color Match (`ColorMatch`)

**Description:**


color-matcher enables color transfer across images which comes in handy for automatic  
color-grading of photographs, paintings and film sequences as well as light-field  
and stopmotion corrections.  

The methods behind the mappings are based on the approach from Reinhard et al.,  
the Monge-Kantorovich Linearization (MKL) as proposed by Pitie et al. and our analytical solution  
to a Multi-Variate Gaussian Distribution (MVGD) transfer in conjunction with classical histogram   
matching. As shown below our HM-MVGD-HM compound outperforms existing methods.   
https://github.com/hahnec/color-matcher/



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image_ref` (required): `IMAGE`
- `image_target` (required): `IMAGE`
- `method` (required): `['mkl', 'hm', 'reinhard', 'mvgd', 'hm-mvgd-hm', 'hm-mkl-hm']`
  - Options: `{{'default': 'mkl'}}`
- `strength` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 95/100

**Reason:** This node enables color matching across images, which is directly relevant to transferring style from a reference image to an input image.

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

**Reason:** This node is very useful as it can blend two images together based on a specific transition effect.

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

**Score:** 82/100

**Reason:** This node is very useful as it can extend the functionality of Cross Fade Images by allowing multiple images to be faded into each other.

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

**Score:** 80/100

**Reason:** This node is essential for selecting specific images from a batch for style transfer.

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

**Reason:** This node is very useful in repeating each image in a batch by the specified number of times, allowing for more efficient processing and analysis of the input images.

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

**Score:** 40/100

**Reason:** This node has some utility in concatenating images from a batch into a grid, but its relevance and applicability depend on the specific requirements of the workflow goal.

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

**Score:** 100/100

**Reason:** This node can be used to crop and resize images, which may be necessary for the workflow goal.

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

**Score:** 80/100

**Reason:** This node is very useful as it normalizes the input image to be in the range [-1, 1] which is often required for style transfer tasks.

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

**Score:** 81/100

**Reason:** Directly relevant to uncrop reference image before style transfer.

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

**Score:** 41/100

**Reason:** Can upscale input image but may not be directly necessary for style transfer.

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

**Score:** 61/100

**Reason:** Can insert images at specified indices, potentially useful as a supporting node.

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

**Reason:** This node is essential for loading and resizing the reference image which will be used as input for style transfer.

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

**Score:** 41/100

**Reason:** This node can be moderately useful if you need to merge channels from different images but it"s not directly relevant to the workflow goal of transferring style from a reference image.

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

**Score:** 61/100

**Reason:** This node can be very useful if you need to adjust the color range of the input images but it"s not directly relevant to the workflow goal of transferring style from a reference image.

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

**Score:** 81/100

**Reason:** This node can reverse the order of images in a batch which may be necessary for certain style transfer algorithms or workflows.

### Metadata

---

### Save Image With Alpha (`SaveImageWithAlpha`)

**Description:**


Saves an image and mask as .PNG with the mask as the alpha channel. 


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `mask` (required): `MASK`
- `filename_prefix` (required): `STRING`
  - Options: `{{'default': 'ComfyUI'}}`


### Applicability

**Score:** 40/100

**Reason:** This node can save an image and mask as .PNG with the mask as the alpha channel which may be necessary for certain style transfer algorithms or workflows.

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

**Score:** 80/100

**Reason:** This node is very useful as it splits image channels into separate images which can be used for further processing or analysis in the style transfer workflow.

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

**Reason:** Directly segments images using CLIPSeg, relevant to style transfer.

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

**Score:** 41/100

**Reason:** Crops images from masks but does not directly contribute to style transfer.

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

**Score:** 61/100

**Reason:** Advanced version of cropping with more outputs, still indirectly contributes to style transfer.

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

**Score:** 100/100

**Reason:** Uncrops images after cropping, essential for completing the style transfer workflow.

### Metadata

---

### Batch Uncrop Advanced (`BatchUncropAdvanced`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `cropped_images` (required): `IMAGE`
- `cropped_masks` (required): `MASK`
- `combined_crop_mask` (required): `MASK`
- `bboxes` (required): `BBOX`
- `border_blending` (required): `FLOAT`
  - Options: `{{'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `crop_rescale` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`
- `use_combined_mask` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `use_square_mask` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `combined_bounding_box` (optional): `BBOX`
  - Options: `{{'default': None}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for uncropping images which is a crucial step in transferring style from reference to input image.

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

**Score:** 40/100

**Reason:** This node may be useful in certain scenarios where color-based masking is required but it"s not directly relevant to transferring style from reference to input image.

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

**Score:** 81/100

**Reason:** This node filters out empty masks and corresponding images, which is essential for the workflow goal of transferring style from reference image to input image.

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

**Score:** 41/100

**Reason:** This node returns the width, height, and batch size of the mask, but it does not directly contribute to the transfer process. It could be useful as a supporting node for debugging or logging purposes.

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

**Score:** 91/100

**Reason:** Very useful for adjusting mask positions which can affect the style transfer result.

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

**Score:** 81/100

**Reason:** Essential for resizing masks to match the input image size, which is crucial for successful style transfer.

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

**Score:** 80/100

**Reason:** This node is very useful for combining multiple conditioning nodes into one, which is essential for the style transfer workflow.

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

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, making it essential for the workflow goal of transferring style from a reference image to an input image.

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

**Reason:** Similar to Node 1, this node also bundles multiple conditioning mask and combine nodes into one, making it very useful for the workflow goal of transferring style from a reference image to an input image.

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

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, with an additional positive and negative condition, making it very useful for the workflow goal of transferring style from a reference image to an input image.

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

**Score:** 85/100

**Reason:** This node creates a batch of masks interpolated between given frames and values, which can be used as a mask in the style transfer process, making it essential for the workflow goal of transferring style from a reference image to an input image.

### Metadata

---

### Create Fluid Mask (`CreateFluidMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `invert` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 256, 'min': 16, 'max': 4096, 'step': 1}}`
- `inflow_count` (required): `INT`
  - Options: `{{'default': 3, 'min': 0, 'max': 255, 'step': 1}}`
- `inflow_velocity` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 255, 'step': 1}}`
- `inflow_radius` (required): `INT`
  - Options: `{{'default': 8, 'min': 0, 'max': 255, 'step': 1}}`
- `inflow_padding` (required): `INT`
  - Options: `{{'default': 50, 'min': 0, 'max': 255, 'step': 1}}`
- `inflow_duration` (required): `INT`
  - Options: `{{'default': 60, 'min': 0, 'max': 255, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node directly creates a fluid mask that can be used to transfer style from reference image to input image.

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

**Score:** 41/100

**Reason:** This node creates a gradient mask which may not be as effective for transferring style compared to other nodes but could still be useful in certain situations.

### Metadata

---

### Create Magic Mask (`CreateMagicMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `frames` (required): `INT`
  - Options: `{{'default': 16, 'min': 2, 'max': 4096, 'step': 1}}`
- `depth` (required): `INT`
  - Options: `{{'default': 12, 'min': 1, 'max': 500, 'step': 1}}`
- `distortion` (required): `FLOAT`
  - Options: `{{'default': 1.5, 'min': 0.0, 'max': 100.0, 'step': 0.01}}`
- `seed` (required): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 99999999, 'step': 1}}`
- `transitions` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 20, 'step': 1}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`

#### Outputs

- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 61/100

**Reason:** This node creates a magic mask that can be used to transfer style from reference image to input image. However, its effectiveness depends on the specific settings chosen.

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

**Score:** 41/100

**Reason:** This node creates a shape mask which may not be as effective for transferring style compared to other nodes but could still be useful in certain situations where a simple shape is desired.

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

**Score:** 80/100

**Reason:** This node can create a mask or batch of masks with text, which could be useful for the workflow goal.

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

**Score:** 100/100

**Reason:** This node can generate masks based on float values, which could be useful for the workflow goal, especially if the float values represent style transfer information.

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

**Reason:** This node is very useful as it allows bypassing inputs for positive and negative conditioning, which is necessary for the specified workflow goal.

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

**Score:** 90/100

**Reason:** This node creates sigmas tensor from a string of comma-separated values which is crucial for the style transfer process in ComfyUI. It can help achieve the workflow goal by providing necessary input parameters.

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

**Score:** 80/100

**Reason:** This node adjusts sigmas tensor based on user-defined parameters which can be useful for fine-tuning the style transfer process. However, it relies on the output of other nodes like CustomSigmas to function properly.

### Metadata

---

### Float To Sigmas (`FloatToSigmas`)

**Description:**


Creates a sigmas tensor from list of float values.  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `float_list` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'forceInput': True}}`

#### Outputs

- `SIGMAS`: `SIGMAS`


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful as it can convert float values to sigmas tensor which might be required in the style transfer process.

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

**Score:** 81/100

**Reason:** This node is essential for this workflow as it generates noise that can be used as input for other nodes in the style transfer process.

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

**Score:** 91/100

**Reason:** This node is very useful as it directly injects noise into latents which is a crucial step in the style transfer process.

### Metadata

---

### Sigmas To Float (`SigmasToFloat`)

**Description:**


Creates a float list from sigmas tensors.  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `sigmas` (required): `SIGMAS`

#### Outputs

- `float`: `FLOAT`

## KJNODES/TEXT


### Applicability

**Score:** 41/100

**Reason:** This node is moderately useful as it can convert sigmas tensors to float values which might be required in the style transfer process.

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

**Score:** 80/100

**Reason:** This node creates a text mask which can be used to transfer style from reference image to input image by applying the mask to the input image.

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

**Score:** 60/100

**Reason:** This node can generate a more detailed prompt to aid in transferring style from reference image to input image.

### Metadata

---

### Mask Or Image To Weight (`MaskOrImageToWeight`)

**Description:**


Gets the mean values from mask or image batch  
and returns that as the selected output type.   


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `output_type` (required): `['list', 'pandas series', 'tensor', 'string']`
  - Options: `{{'default': 'list'}}`
- `images` (optional): `IMAGE`
- `masks` (optional): `MASK`

#### Outputs

- `FLOAT`: `FLOAT`
- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node can help extract mean values from mask or image batches which are crucial for transferring style between images.

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

**Reason:** This node uses LLMs for chat functionality which can be used to generate text prompts for style transfer, making it very useful for this workflow goal.

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

**Reason:** This node uses LLMs for vision understanding and can provide detailed descriptions of images, which can be used as a reference for style transfer, making it essential for this workflow goal.

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

**Score:** 80/100

**Reason:** This compare node can be used to determine if two images are identical, which could be useful in the workflow goal.

### Metadata

---

### Float (`Float-🔬`)

**Description:**

**Module:** `ComfyUI-Logic`

#### Inputs

- `value` (required): `FLOAT`
  - Options: `{{'default': 0, 'step': 0.01}}`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 40/100

**Reason:** This float node can be used to manipulate image values, but its direct relevance to transferring style from a reference image is limited.

### Metadata

---

### Int (`Int-🔬`)

**Description:**

**Module:** `ComfyUI-Logic`

#### Inputs

- `value` (required): `INT`
  - Options: `{{'default': 0}}`

#### Outputs

- `INT`: `INT`


### Applicability

**Score:** 90/100

**Reason:** This node can convert input values to integers which might be necessary for certain style transfer algorithms or operations.

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

**Reason:** This node can handle string inputs and outputs which could be useful for tasks like image file paths or other metadata manipulation.

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

**Reason:** The Conditioning Multiplier PoP can be useful in adjusting the style transfer process by modifying the conditioning input, but its direct relevance to the workflow goal is moderate.

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

**Score:** 81/100

**Reason:** The Conditioning Normalizer PoP is essential for normalizing the conditioning input, which is a crucial step in the style transfer process.

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

**Score:** 61/100

**Reason:** The Load Image Resizer PoP can be moderately useful in resizing the input image to match the desired megapixels, but it may not directly contribute to the style transfer goal.

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

**Reason:** This node might be useful for logging integer values during the style transfer process, but its utility is limited compared to other nodes.

### Metadata

---

### To string (FLOAT) (`RF_FloatToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `FLOAT`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant because it can convert floating-point values to strings, but this conversion does not directly impact the style transfer process.

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

**Score:** 60/100

**Reason:** This node is moderately useful as it converts integer values to strings, which might be necessary for certain input parameters or output formats in the style transfer workflow.

### Metadata

---

### One of (STRING) (`RF_OptionsString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `index` (required): `INT`
  - Options: `{{'default': 0}}`
- `text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`

#### Outputs

- `text`: `STRING`


### Applicability

**Score:** 40/100

**Reason:** This node allows selecting one of multiple options but its relevance is limited in this specific workflow.

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

**Reason:** This node provides the necessary input for the workflow goal by allowing users to enter a string value.

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

**Score:** 40/100

**Reason:** This node could be used as a supporting node if the text to be replaced is known and needs to be swapped with another value. However, it doesn"t directly contribute to style transfer.

### Metadata

---

### To string (ANY) (`RF_ToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `INT,BOOL,FLOAT,NUMBER`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for converting input values to strings, which is a crucial step in transferring style from reference images.

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

**Score:** 100/100

**Reason:** This node directly controls advanced options for the style transfer process.

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

**Reason:** This node performs the actual style transfer from reference image to input image.

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

**Score:** 80/100

**Reason:** This node is directly relevant for controlling the differential diffusion process in the style transfer pipeline.

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

**Reason:** This node directly blends latent representations from two input images based on a blend factor, which is essential for transferring style between them.

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

**Score:** 100/100

**Reason:** This node is essential for encoding the input image into a latent space that can be used for style transfer.

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

**Score:** 80/100

**Reason:** This node is very useful as it loads a CLIP model that can be used for style transfer from reference images.

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

**Score:** 81/100

**Reason:** This node loads two clips which are necessary for the dual-clip style transfer workflow goal.

### Metadata

---

### Load Diffusion Model (`UNETLoader`)

**Description:**

#### Inputs

- `unet_name` (required): `['hunyuan_video_t2v_720p_bf16.safetensors']`
- `weight_dtype` (required): `['default', 'fp8_e4m3fn', 'fp8_e4m3fn_fast', 'fp8_e5m2']`

#### Outputs

- `MODEL`: `MODEL`

## ADVANCED/LOADERS/DEPRECATED


### Applicability

**Score:** 61/100

**Reason:** This node loads a diffusion model but only has one specific unet name and weight dtype option, limiting its utility in this workflow.

### Metadata

---

### DiffusersLoader (`DiffusersLoader`)

**Description:**

#### Inputs

- `model_path` (required): `[]`

#### Outputs

- `MODEL`: `MODEL`
- `CLIP`: `CLIP`
- `VAE`: `VAE`

## ADVANCED/MODEL_MERGING


### Applicability

**Score:** 41/100

**Reason:** This node is intended for loading diffusers models but does not have any input options specified, making it marginally relevant to the style transfer goal.

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

**Reason:** This node can be used to generate text embeddings that can guide the diffusion model towards generating specific images, making it very useful for the specified workflow goal.

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

**Reason:** This node can be used to truncate a CLIP model at a specific layer, which is moderately useful for fine-tuning or adapting the model for the specified workflow goal.

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

**Reason:** This node encodes text prompts into embeddings that can be used to guide the diffusion model towards generating specific images, making it essential for the specified workflow goal.

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

**Reason:** Directly encodes visual features from the reference image.

### Metadata

---

### Conditioning SDXL merge clip_g / clip_l (`Conditioning SDXL merge clip_g / clip_l`)

**Description:**

**Module:** `Vector_Sculptor_ComfyUI`

#### Inputs

- `cond_clip_l` (required): `CONDITIONING`
- `cond_clip_g` (required): `CONDITIONING`

#### Outputs

- `CONDITIONING`: `CONDITIONING`


### Applicability

**Score:** 90/100

**Reason:** Merges two conditioning vectors which can be used in the style transfer process.

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

**Score:** 81/100

**Reason:** This node is essential for the workflow goal as it averages two conditioning inputs, allowing for the combination of styles from different images.

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

**Score:** 61/100

**Reason:** This node is moderately useful for the workflow goal as it combines two conditioning inputs, enabling the blending of styles from different sources.

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

**Reason:** This node is essential for setting a specific area in the input image where style transfer will be applied.

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

**Reason:** This node is very useful as it allows for flexible and precise control over the area of interest with percentage-based coordinates.

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

**Reason:** This node has moderate utility as it allows adjusting the strength of conditioning but lacks flexibility in setting the area of interest.

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

**Reason:** This node is moderately useful for setting a mask to control where style transfer will be applied, but its utility depends on the specific requirements of the workflow.

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

**Score:** 61/100

**Reason:** This node prepares the input image for style transfer by conditioning it with a CLIP vision output.

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

**Score:** 81/100

**Reason:** This node directly applies ControlNet to the input image based on the provided conditioning and control net.

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

**Reason:** This advanced node provides more flexibility in applying ControlNet, allowing for positive and negative conditioning, as well as adjustable start and end percentages.

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

**Score:** 41/100

**Reason:** This node sets the type of Shakker Labs Union ControlNet, but it does not directly contribute to style transfer from a reference image.

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

**Score:** 100/100

**Reason:** This node conditions the model for inpainting which is necessary for transferring style from a reference image.

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

**Score:** 90/100

**Reason:** This node applies a style model to the input image using conditioning and style model inputs.

### Metadata

---

### Batch Images (`ImageBatch`)

**Description:**

#### Inputs

- `image1` (required): `IMAGE`
- `image2` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful as it allows batch processing of images for style transfer.

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

**Score:** 60/100

**Reason:** This node pads the input image for outpainting, which may be a supporting task for style transfer, depending on the specific requirements of the workflow.

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

**Reason:** This node is essential for the workflow goal as it loads the reference and/or input images required for style transfer.

### Metadata

---

### Preview Image (`PreviewImage`)

**Description:**

Saves the input images to your ComfyUI output directory.

#### Inputs

- `images` (required): `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node is essential for previewing input images before proceeding with the style transfer task.

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

**Reason:** This node can upscale an image but does not directly contribute to transferring style between images; it could be useful for preparing input images.

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

**Score:** 100/100

**Reason:** This node directly upscaling an image by a specified scale factor is essential for transferring style from reference to input images.

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

**Score:** 80/100

**Reason:** This node upscaling a latent image by a specified scale factor is very useful for transferring style from reference to input images.

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

**Reason:** This node is essential for upscaling the latent representation of the input image to match the reference image.

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

**Reason:** This node is necessary for decoding the latent representation back into a pixel space image, which can then be used as the input for style transfer.

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

**Score:** 41/100

**Reason:** Repeats latent batch but doesn"t directly contribute to style transfer.

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

**Score:** 81/100

**Reason:** Sets noise mask which is necessary for some inpainting algorithms.

### Metadata

---

### VAE Encode (for Inpainting) (`VAEEncodeForInpaint`)

**Description:**

#### Inputs

- `pixels` (required): `IMAGE`
- `vae` (required): `VAE`
- `mask` (required): `MASK`
- `grow_mask_by` (required): `INT`
  - Options: `{{'default': 6, 'min': 0, 'max': 64, 'step': 1}}`

#### Outputs

- `LATENT`: `LATENT`

## LATENT/TRANSFORM


### Applicability

**Score:** 61/100

**Reason:** Encodes image into latent space, a crucial step in many style transfer workflows.

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

**Score:** 41/100

**Reason:** Crops latent samples but doesn"t directly contribute to style transfer or inpainting.

### Metadata

---

### Load CLIP Vision (`CLIPVisionLoader`)

**Description:**

#### Inputs

- `clip_name` (required): `[]`

#### Outputs

- `CLIP_VISION`: `CLIP_VISION`


### Applicability

**Score:** 80/100

**Reason:** This node is very useful as it loads CLIP vision models which are crucial for the transfer process of styles between images.

### Metadata

---

### Load ControlNet Model (`ControlNetLoader`)

**Description:**

#### Inputs

- `control_net_name` (required): `[]`

#### Outputs

- `CONTROL_NET`: `CONTROL_NET`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for loading a ControlNet model which can be used in the style transfer process.

### Metadata

---

### Load ControlNet Model (diff) (`DiffControlNetLoader`)

**Description:**

#### Inputs

- `model` (required): `MODEL`
- `control_net_name` (required): `[]`

#### Outputs

- `CONTROL_NET`: `CONTROL_NET`


### Applicability

**Score:** 40/100

**Reason:** This node provides an alternative way to load a ControlNet model but requires additional information (MODEL) that might not always be available.

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

**Score:** 80/100

**Reason:** This node is very useful for the specified workflow goal. It loads an unCLIP checkpoint that contains both CLIP and VAE models, making it directly relevant to transferring style from reference image to input image.

### Metadata

---

### Load Image (as Mask) (`LoadImageMask`)

**Description:**

#### Inputs

- `image` (required): `['example.png', 'pond_girl1.png', 'pond_girl2.png', 'pond_girl3.png']`
  - Options: `{{'image_upload': True}}`
- `channel` (required): `['alpha', 'red', 'green', 'blue']`

#### Outputs

- `MASK`: `MASK`

## PRIMITIVES


### Applicability

**Score:** 90/100

**Reason:** This node is essential for the specified workflow goal as it loads an image (as a mask) which could be used in conjunction with other nodes to perform tasks related to the transfer of style from reference image to input image.

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

**Score:** 80/100

**Reason:** This node is very useful for transferring style from reference image to input image as it allows handling single-line text data which could represent style information or metadata.

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

**Score:** 80/100

**Reason:** This KSampler node can be used for denoising the latent image and transferring style from reference image to input image by conditioning on positive and negative attributes.

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

**Score:** 60/100

**Reason:** This KSamplerAdvanced node is similar to the previous one but with additional options like adding noise and returning leftover noise. It can also be used for style transfer but may not offer as much flexibility as the previous node.

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

**Reason:** This node is essential for generating text with a specific style based on a reference image.

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

**Reason:** This node is essential for configuring LLM settings that are necessary for the workflow goal.

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

**Reason:** This node provides a complete LLM configuration that can be used to transfer style from reference image to input image.

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

**Reason:** This node requires an existing LLM configuration and provides advanced prompt handling capabilities that can be used to transfer style from reference image to input image.

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

**Reason:** This VAE decoder node directly generates an output image based on latent samples, which is essential for the workflow goal of transferring style from a reference image to an input image.

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

**Reason:** This VAE encoder node is very useful as it can convert an input image into latent samples that can be used by other nodes in the workflow, such as the VAE decoder node.

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

**Reason:** This node is essential for the workflow goal as it can generate text prompts based on the input image and reference image, which is crucial for style transfer.

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

**Score:** 90/100

**Reason:** This node is very useful for the workflow goal as it can generate both text and vision prompts based on the input image and reference image, making it a powerful tool for style transfer.

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

**Score:** 80/100

**Reason:** This node is moderately useful for the workflow goal as it can generate vision prompts based on the input image and reference image, which can be used to guide the style transfer process.

### Metadata

---
