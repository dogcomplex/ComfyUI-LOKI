# Filtered Nodes for: Image generation guided by canny edge detection

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

**Score:** 81/100

**Reason:** This node directly applies canny edge detection to generate a fuzzy fast intensity mask, which is essential for guiding image generation.

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

**Reason:** Although not directly related to canny edge detection, this node generates a seam mask that could be used in conjunction with other nodes to guide image generation.

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

**Reason:** This node allows for arbitrary operations on masks and images, which could be used in conjunction with other nodes to guide image generation, but it does not directly apply canny edge detection.

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

**Reason:** This node is essential for expanding the mask based on canny edge detection results.

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

**Reason:** This node is moderately useful as it also expands the mask but lacks specific features compared to the first node.

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

**Score:** 99/100

**Reason:** This node is almost essential for blurring white edges in the mask based on canny edge detection results.

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

**Score:** 41/100

**Reason:** This node is marginally useful as it blurs the edges but lacks specific features and direct relevance to the workflow goal compared to other nodes.

### Metadata

---

### 2🐕Mask Blurred Black edges (`EG_ZZ_HSYH`)

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

## 2🐕/🆎CHOICE


### Applicability

**Score:** 81/100

**Reason:** This node blurs black edges from a given mask, which is directly relevant to canny edge detection.

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

**Score:** 40/100

**Reason:** Although this custom template node is not directly relevant, it could potentially be used as a supporting tool for creating templates related to image generation.

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

**Reason:** This node provides a wide range of scene settings that can be used to generate images with specific characteristics, which is relevant to the workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node allows for control over lighting, but it does not directly relate to canny edge detection. However, it could be useful as a supporting node to enhance the overall image quality.

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

**Reason:** This node provides various graphic effects and styles that can be used to create images with specific visual characteristics, but its relevance to canny edge detection is limited.

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

**Reason:** This node allows for control over lens settings, including perspective, positioning, action, composition method, character lens, and camera lens. These settings are directly relevant to the workflow goal of image generation guided by canny edge detection.

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

**Score:** 100/100

**Reason:** This node provides a wide range of item categories that could be used in conjunction with canny edge detection for image generation.

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

**Score:** 80/100

**Reason:** This node stitches cropped images together which is useful for refining the image after applying canny edge detection.

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

**Score:** 90/100

**Reason:** This node crops an image based on a mask, which could be used to isolate edges detected by canny edge detection.

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

**Score:** 80/100

**Reason:** This node allows for mathematical operations and could be used to calculate parameters needed for canny edge detection or other image processing steps.

### Metadata

---

### 2🐕Image size acquisition (`EG_TX_CCHQ`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `image_in` (required): `IMAGE`

#### Outputs

- `width`: `INT`
- `height`: `INT`


### Applicability

**Score:** 80/100

**Reason:** This node provides essential information about the input image size which is crucial for canny edge detection.

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

**Score:** 100/100

**Reason:** This node loads any image and can be used as a starting point for the workflow goal of generating images guided by canny edge detection.

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

**Reason:** This node is very useful as it can adjust saturation levels in an image, which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 85/100

**Reason:** This node is very useful as it can adjust color levels in an image, which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 95/100

**Reason:** This node is essential for this workflow as it can adjust hue levels in an image, which is a crucial step in image generation guided by canny edge detection.

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

**Score:** 81/100

**Reason:** This node preserves brightness which is a crucial aspect of maintaining image quality in the specified workflow goal.

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

**Score:** 41/100

**Reason:** While this node provides color adjustment options, its relevance to canny edge detection is not directly apparent and may require additional processing steps.

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

**Score:** 90/100

**Reason:** This node is very useful for the workflow goal as it allows setting the dimensions of an image, which is essential for canny edge detection and subsequent image generation.

### Metadata

---

### 🦊 Isulion Animal Behavior Generator (`IsulionAnimalBehaviorGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `seed` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 999999999}}`
- `behavior` (required): `['Hunting', 'Sleeping', 'Playing', 'Flying', 'Swimming', 'Running', 'Walking', 'Eating', 'Drinking', 'Grooming', 'Nesting', 'Perching', 'Climbing', 'Jumping', 'Diving', 'Stalking', 'Resting', 'Foraging', 'Grazing', 'Prowling', 'Pouncing', 'Soaring', 'Gliding', 'Hovering', 'Fishing', 'Basking', 'Burrowing', 'Hibernating', 'Migrating', 'Mating', 'Nurturing', 'Teaching', 'Fighting', 'Defending', 'Exploring', 'Hiding', 'Camouflaging', 'Gathering', 'Building', 'Communicating']`

#### Outputs

- `behavior`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it can generate animal behaviors that can be used in conjunction with image generation nodes to create images guided by canny edge detection.

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

**Reason:** This node is essential for the workflow goal as it can generate art styles that can be used in conjunction with image generation nodes to create images guided by canny edge detection.

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

**Reason:** This node generates an emotion that could be used as a prompt or input for the image generation process.

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

**Reason:** This node loads a model that can be used for image generation and may include canny edge detection as part of its architecture.

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

**Reason:** This node generates prompts that can guide the image generation process but does not directly perform canny edge detection.

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

**Score:** 80/100

**Reason:** This node is very useful for generating images with specific conditions, which could be used as input for the canny edge detection process.

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

**Score:** 40/100

**Reason:** This node is marginally relevant to image generation guided by canny edge detection. It provides a way to select text from a file based on keywords, but it does not perform any edge detection or processing.

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

**Score:** 81/100

**Reason:** Directly resizes images based on canny edge detection output, making it essential for image generation.

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

**Score:** 41/100

**Reason:** Provides width and height information about an input image but does not directly contribute to the workflow goal.

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

**Reason:** This node conditions multiple texts on a CLIP model, but it does not directly contribute to the image generation guided by canny edge detection. It could be useful for adding additional text-based conditioning to the input.

### Metadata

---

### Logic node (`DF_Logic_node`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Operation` (required): `['A > B', 'A < B', 'A = B', 'A AND B', 'A OR B', 'A XOR B']`
  - Options: `{{'forceInput': False}}`
- `CompareValue_A` (required): `*`
  - Options: `{{'forceInput': False}}`
- `CompareValue_B` (optional): `*`
  - Options: `{{'forceInput': False}}`
- `OnTrue` (optional): `*`
  - Options: `{{'forceInput': False}}`
- `OnFalse` (optional): `*`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `*`: `*`


### Applicability

**Score:** 50/100

**Reason:** This logic node could be used as a supporting node to make decisions based on the output of other nodes in the workflow, but it does not directly contribute to the goal.

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

**Reason:** Square root could be used to process edge map values in the canny edge detection algorithm.

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

**Reason:** Subtract operation might be useful for adjusting threshold values or subtracting background noise from the image.

### Metadata

---

### Tangent (`DF_Tangent`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `value` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `type_` (required): `['RAD', 'DEG']`
  - Options: `{{'forceInput': False}}`
- `arcTan` (required): `[False, True]`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`

## DERFUU_NODES/MODDED NODES/CONDITIONS


### Applicability

**Score:** 41/100

**Reason:** Tangent (`DF_Tangent`) has some relevance as it can be used to calculate edge angles, and its arcTan input allows for conversion between radians and degrees, making it more useful than cosines or sinus in this workflow.

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

**Reason:** This node is moderately useful as it allows scaling images to a specific side length, which could be helpful in preparing images for further processing or analysis.

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

**Reason:** This node is moderately useful as it allows scaling latents to a specific side length, which could be helpful in preparing latents for further processing or analysis.

### Metadata

---

### Float (`DF_Float`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 61/100

**Reason:** This node can be used to input a float value that could be used in the canny edge detection process.

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

**Reason:** This node is very useful as it allows scheduling of batch prompts with specific settings such as clip, max frames, and print output.

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

**Score:** 80/100

**Reason:** This node is essential for this workflow as it provides a more advanced version of the Batch Prompt Schedule node with additional features like text generation for grayscale and latent input.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows scheduling of batch prompts with specific settings such as clip, num latents, and print output, making it suitable for workflows involving latent inputs.

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

**Score:** 81/100

**Reason:** This node is very useful as it can schedule a batch of strings for the workflow goal, which may be necessary for generating images based on canny edge detection.

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

**Reason:** This node is very useful as it can schedule a batch of values (potentially latents) for the workflow goal, which may be necessary for generating images based on canny edge detection.

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

**Reason:** Directly generates a frame based on canny edge detection, which is essential for the image generation guided by canny edge detection workflow goal.

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

**Score:** 41/100

**Reason:** Initializes a frame with text and optional previous frame, which is moderately useful for the workflow goal but requires additional processing steps.

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

**Reason:** Concatenates strings which could be useful for generating text overlays in the generated images.

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

**Score:** 80/100

**Reason:** Selects images based on a schedule which aligns with the workflow goal of image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node provides input parameters that could be used for image generation and canny edge detection, such as width, height, and clip.

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

**Score:** 40/100

**Reason:** This node is related to scheduling but does not directly contribute to canny edge detection or image generation. It also lacks specific features useful for the workflow goal.

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

**Reason:** This node generates multiple prompts based on various themes and styles, which could be useful for generating diverse images that might include edges detected through canny edge detection.

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

**Reason:** This node generates clothing items with specific styles and designs, but it does not directly relate to image generation guided by canny edge detection. However, it could be used as a supporting node in a workflow that involves generating images of objects or scenes with detected edges.

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

**Reason:** This node generates a prompt that can be used for image generation and allows customization of various parameters including theme, complexity, and style which could potentially include canny edge detection effects.

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

**Reason:** This node is essential for this workflow as it allows the mixing of styles to guide image generation, aligning with the goal of using canny edge detection.

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

**Score:** 100/100

**Reason:** This node is essential for this workflow as it allows the generation of magical effects that can be used in conjunction with canny edge detection to guide image generation.

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

**Score:** 61/100

**Reason:** This node can be used as a supporting node to generate images that will later undergo canny edge detection. It allows for the creation of collages from multiple images.

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

**Score:** 81/100

**Reason:** This node is essential for loading images from a directory, which are likely to be used in image generation tasks guided by canny edge detection.

### Metadata

---

### 🔍 Isulion Civitai Model Explorer (`IsulionCivitaiModelExplorer`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `search_query` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'placeholder': 'Enter search terms...'}}`
- `sort_by` (required): `['Highest Rated', 'Most Downloaded', 'Newest']`
  - Options: `{{'default': 'Highest Rated'}}`
- `nsfw_filter` (required): `['Hide NSFW', 'Show All', 'Only NSFW']`
  - Options: `{{'default': 'Hide NSFW'}}`
- `model_type` (required): `['Checkpoint', 'LORA', 'Embedding', 'All']`
  - Options: `{{'default': 'All'}}`
- `page` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 100}}`
- `api_key` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'placeholder': 'Enter your Civitai API token...'}}`

#### Outputs

- `model_info`: `STRING`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for finding models that support canny edge detection and generating prompts based on those models.

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

**Score:** 40/100

**Reason:** Although this node generates technology descriptions, its output is a string rather than an image, making it marginally relevant for the workflow goal.

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

**Reason:** This node provides a list of predefined dimensions for image generation, which aligns with the workflow goal of generating images guided by canny edge detection.

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

**Score:** 90/100

**Reason:** This node is very useful for combining multiple strings into a single string or list of strings, which could be used in conjunction with other nodes to generate text prompts for image generation.

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

**Reason:** This node is essential for appending tracking data to be used with InstanceDiffusion, which could be a crucial step in the workflow goal of generating images guided by canny edge detection.

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

**Reason:** This node draws tracking data from CreateInstanceDiffusionTracking-node, which is directly related to the workflow goal of image generation guided by canny edge detection.

### Metadata

---

### ImageTransformByNormalizedAmplitude (`ImageTransformByNormalizedAmplitude`)

**Description:**


Works as a bridge to the AudioScheduler -nodes:  
https://github.com/a1lazydog/ComfyUI-AudioScheduler  
Transforms image based on the normalized amplitude.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `normalized_amp` (required): `NORMALIZED_AMPLITUDE`
- `zoom_scale` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': -1.0, 'max': 1.0, 'step': 0.001, 'display': 'number'}}`
- `x_offset` (required): `INT`
  - Options: `{{'default': 0, 'min': -16383, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `y_offset` (required): `INT`
  - Options: `{{'default': 0, 'min': -16383, 'max': 16384, 'step': 1, 'display': 'number'}}`
- `cumulative` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `image` (required): `IMAGE`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 40/100

**Reason:** This node transforms an image based on normalized amplitude, but it is not directly related to the workflow goal of image generation guided by canny edge detection. It might be useful as a supporting node if audio information is used in conjunction with image processing.

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

**Reason:** This node creates masks based on normalized amplitude, which could be useful in image generation.

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

**Score:** 81/100

**Reason:** This node offsets masks based on the normalized amplitude, making it essential for fine-tuning image generation guided by canny edge detection.

### Metadata

---

### BOOL Constant (`BOOLConstant`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `value` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `value`: `BOOLEAN`


### Applicability

**Score:** 80/100

**Reason:** This boolean constant could be used to control a conditional branch in the workflow based on a specific condition related to canny edge detection.

### Metadata

---

### INT Constant (`INTConstant`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `value` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`

#### Outputs

- `value`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This integer constant could be used as a threshold value in the canny edge detection process, but its relevance depends on the specific implementation details.

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

**Score:** 40/100

**Reason:** This node allows for multiline strings but does not directly contribute to the image generation task.

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

**Score:** 40/100

**Reason:** This node is marginally relevant as it creates a fade mask which could be used in conjunction with edge detection for image processing.

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

**Score:** 60/100

**Reason:** This node is moderately useful as it perturbs model weights which could be used in conjunction with edge detection for image processing or generation.

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

**Score:** 60/100

**Reason:** Fast Preview is moderately useful as it can display a preview of the generated image, but it does not directly relate to canny edge detection or the workflow goal.

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

**Reason:** This node is essential for generating images with GLIGEN text box positions guided by canny edge detection.

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

**Score:** 100/100

**Reason:** This node is crucial for capturing screen coordinates and applying them to the image generation process.

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

**Reason:** This node is very useful as it allows patching attention mode which could be used for guiding the image generation process.

### Metadata

---

### Screencap mss (`Screencap_mss`)

**Description:**


Captures an area specified by screen coordinates.  
Can be used for realtime diffusion with autoqueue.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 10000, 'step': 1}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 10000, 'step': 1}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 10000, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 10000, 'step': 1}}`
- `num_frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 255, 'step': 1}}`
- `delay` (required): `FLOAT`
  - Options: `{{'default': 0.1, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node captures an area specified by screen coordinates and can be used for real-time diffusion with autoqueue, which is moderately useful for the workflow goal of image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node calls the StabilityAI API to generate images based on a prompt, making it very useful for the workflow goal of image generation. However, it does not perform any canny edge detection itself.

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

**Score:** 60/100

**Reason:** This node schedules conditions for Stable Zero123 but does not perform any canny edge detection or directly contribute to image generation guided by canny edge detection.

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

**Score:** 61/100

**Reason:** StyleModelApplyAdvanced is moderately useful as it can apply a style model to the input image but lacks direct relevance to canny edge detection.

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

**Reason:** TorchCompileControlNet has marginal utility for this workflow goal as it compiles a control net but does not directly relate to image generation with canny edge detection.

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

**Reason:** TorchCompileModelFluxAdvanced is essential for this workflow goal as it can compile a model flux advanced, which directly supports the application of canny edge detection in image generation.

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

**Reason:** This node captures a frame from a webcam using CV2 and returns an image, which is directly relevant to the workflow goal of generating images guided by canny edge detection. It can be used as input for further processing steps such as edge detection or image generation.

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

**Reason:** This node creates a gradient image from coordinates and returns an image, which can be used as input for further processing steps such as edge detection or image generation. It may be useful in a workflow that involves generating images with specific gradient patterns.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows cross-fading between two images based on the specified interpolation type, which could be used in conjunction with canny edge detection for generating images.

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

**Reason:** This node is essential for this workflow as it extends the functionality of Cross Fade Images to handle multiple input images, allowing for more complex image generation guided by canny edge detection.

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

**Reason:** This node is very useful as it allows selecting specific images from a batch for further processing in the canny edge detection guided image generation workflow.

### Metadata

---

### Gradient To Float (`GradientToFloat`)

**Description:**


Calculates list of floats from image.    


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `steps` (required): `INT`
  - Options: `{{'default': 10, 'min': 2, 'max': 10000, 'step': 1}}`

#### Outputs

- `float_x`: `FLOAT`
- `float_y`: `FLOAT`


### Applicability

**Score:** 40/100

**Reason:** This node has moderate utility as it calculates gradients from an image, which could be used as input for canny edge detection, but its direct relevance to the goal is limited.

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

**Score:** 90/100

**Reason:** This node is very useful as it repeats each image in a batch, which could be used for generating multiple images with the same features detected by canny edge detection.

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

**Score:** 80/100

**Reason:** This node is very useful as it can concatenate multiple images from a batch into a grid, which could be used for generating multiple images with features detected by canny edge detection.

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

**Reason:** This node is essential for the specified workflow goal as it crops and resizes an image based on a mask, which could be used to isolate edges detected using canny edge detection.

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

**Score:** 95/100

**Reason:** This node normalizes images to a range that could be useful for further processing in the workflow.

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

**Score:** 61/100

**Reason:** This node is moderately useful as it can help uncrop images based on a mask, which could be used in conjunction with canny edge detection to guide image generation.

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

**Score:** 81/100

**Reason:** This node is essential for this workflow goal as it allows upscaling of images using a model, which is necessary for generating high-quality images guided by canny edge detection.

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

**Score:** 41/100

**Reason:** This node is moderately useful for this workflow goal as it inserts images at specified indices, which could be used in conjunction with other nodes to generate an image batch guided by canny edge detection.

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

**Score:** 61/100

**Reason:** Directly loads and resizes images which can be used as input for edge detection.

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

**Score:** 81/100

**Reason:** Essential for merging image channels to create a final output image after edge detection.

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

**Reason:** Moderately useful for adjusting the image range which can be used in conjunction with edge detection results.

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

**Reason:** Reverses the order of images in a batch which could be useful for processing images in a specific order based on their edges.

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

**Reason:** This node is essential for the workflow goal as it splits image channels which can be used in canny edge detection and subsequent image generation.

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

**Score:** 90/100

**Reason:** This node is highly relevant and very useful for the specified workflow goal as it allows cropping images based on masks which is a crucial step in canny edge detection.

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

**Score:** 95/100

**Reason:** This node is extremely relevant and essential for the specified workflow goal as it provides advanced features such as combining cropped images and masks, making it an ideal choice for image generation guided by canny edge detection.

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

**Score:** 80/100

**Reason:** This node is very useful and highly relevant to the specified workflow goal as it allows uncropping images which is a necessary step after cropping based on masks in canny edge detection.

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

**Reason:** This node extracts bounding box coordinates from a list of bboxes and an index, which could be useful for further processing in the workflow.

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

**Score:** 80/100

**Reason:** This node visualizes bounding boxes on images, but it does not directly contribute to canny edge detection or image generation.

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

**Score:** 80/100

**Reason:** This node filters out empty masks which could be used in canny edge detection for image generation.

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

**Score:** 70/100

**Reason:** This node provides the size and count of a mask which is useful for understanding the input data for canny edge detection.

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

**Score:** 90/100

**Reason:** This node grows or contracts masks with blur which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 95/100

**Reason:** This node is very useful as it allows offsetting masks which could be used in conjunction with canny edge detection for image generation.

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

**Score:** 60/100

**Reason:** This node is moderately useful as it allows remapping the range of a mask, but may not directly contribute to the workflow goal.

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

**Score:** 80/100

**Reason:** This node is very useful as it allows resizing masks which could be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node is very useful as it splits bounding boxes into two lists at a given index, which could be used for further processing in the workflow.

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

**Score:** 41/100

**Reason:** This node combines multiple conditioning nodes, but its direct relevance to canny edge detection or image generation is limited. It may be moderately useful as a supporting node.

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

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, which is directly relevant to the workflow goal of image generation guided by canny edge detection.

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

**Reason:** This node also bundles multiple conditioning mask and combine nodes into one, making it very useful for the specified workflow goal.

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

**Reason:** Similar to the previous two nodes, this node bundles multiple conditioning mask and combine nodes into one, which is essential for achieving the workflow goal.

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

**Score:** 92/100

**Reason:** This node creates a batch of masks interpolated between given frames and values, which can be used in conjunction with canny edge detection to generate images. It is very useful for this workflow goal.

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

**Reason:** This node directly generates a mask based on gradient information which can be used as input for canny edge detection.

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

**Score:** 60/100

**Reason:** This node creates a shape-based mask that could potentially be used in conjunction with other nodes for canny edge detection, but it is not directly relevant.

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

**Reason:** This node directly generates text on a path which aligns with the workflow goal and provides useful outputs such as an image and masks.

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

**Reason:** This node is very useful as a supporting node for the workflow, allowing bypassed inputs from conditioning nodes.

### Metadata

---

### VRAM Debug (`VRAM_Debug`)

**Description:**


Returns the inputs unchanged, they are only used as triggers,  
and performs comfy model management functions and garbage collection,  
reports free VRAM before and after the operations.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `empty_cache` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `gc_collect` (required): `BOOLEAN`
  - Options: `{{'default': True}}`
- `unload_all_models` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `any_input` (optional): `*`
- `image_pass` (optional): `IMAGE`
- `model_pass` (optional): `MODEL`

#### Outputs

- `any_output`: `*`
- `image_pass`: `IMAGE`
- `model_pass`: `MODEL`
- `freemem_before`: `INT`
- `freemem_after`: `INT`

## KJNODES/NOISE


### Applicability

**Score:** 61/100

**Reason:** This node performs comfy model management functions and garbage collection, which could be useful for optimizing VRAM usage in the workflow.

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

**Score:** 81/100

**Reason:** This node creates a sigmas tensor from a string of comma-separated values, which is directly relevant to canny edge detection in image generation.

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

**Score:** 41/100

**Reason:** This node adjusts sigmas, but its relevance and utility depend on the specific requirements of the workflow, such as adjusting sigma values for canny edge detection.

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

**Reason:** FloatToSigmas is marginally relevant as it converts float values to sigmas tensors, which might be useful in edge detection but its direct application is unclear.

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

**Reason:** GenerateNoise is very useful for this workflow goal as it generates noise that can be used in image generation guided by canny edge detection.

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

**Reason:** InjectNoiseToLatent is essential for this workflow goal as it injects noise into latents, which is a crucial step in generating images using canny edge detection.

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

**Reason:** SigmasToFloat is marginally relevant as it converts sigmas tensors to float values, but its direct application in image generation guided by canny edge detection is unclear.

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

**Score:** 91/100

**Reason:** This node creates a text mask which could be useful in conjunction with canny edge detection for image generation.

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

**Reason:** This node is essential for generating detailed text prompts to guide image generation.

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

**Score:** 41/100

**Reason:** This node is marginally relevant as it could be used to extract values from other nodes in the workflow, but its direct relevance to the workflow goal is limited.

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

**Reason:** This node is very useful for generating images guided by canny edge detection as it uses LLMs for chat-based text-to-image synthesis.

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

**Score:** 95/100

**Reason:** This node is essential for image generation guided by canny edge detection as it uses LLMs for vision tasks such as image understanding and description.

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

**Score:** 81/100

**Reason:** The Compare node is very useful for the specified workflow goal as it allows for comparisons between values, which can be crucial in edge detection and image processing.

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

**Score:** 41/100

**Reason:** This node could be useful as a supporting node to convert input values, but it does not directly contribute to the workflow goal.

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

**Score:** 61/100

**Reason:** This node could provide additional context or metadata for image generation, but its direct relevance is moderate.

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

**Score:** 90/100

**Reason:** Very useful for resizing images which is a necessary step in the workflow goal

### Metadata

---

### At index (STRING) (`RF_AtIndexString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `lines` (required): `STRING`
  - Options: `{{'default': '', 'multiline': True}}`
- `index` (required): `INT`
  - Options: `{{'default': 0}}`

#### Outputs

- `text`: `STRING`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant because it allows accessing specific lines of text in the workflow logs which might be useful for debugging purposes related to image generation.

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

**Reason:** This node might be marginally relevant if the output of the canny edge detection is an integer value that needs to be converted to string, but it still doesn"t directly contribute to the image generation process.

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

**Reason:** This node might be useful if you need to select one of multiple string options based on an index value, but it"s not directly related to canny edge detection.

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

**Score:** 80/100

**Reason:** Provides input text which is necessary for subsequent nodes in the workflow, such as edge detection and image generation.

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

**Score:** 60/100

**Reason:** Can replace specific text patterns within a string but does not directly contribute to image generation or canny edge detection.

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

**Score:** 100/100

**Reason:** This node converts VEC2 data into a string, which could be useful for displaying or logging edge detection results.

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

**Score:** 100/100

**Reason:** This node converts VEC3 data into a string, which could be useful for displaying or logging edge detection results.

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

**Score:** 91/100

**Reason:** Very useful as it generates images based on text prompts and can be guided by the output of other nodes in the workflow.

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

**Reason:** Moderately useful as it provides a way to generate images using differential diffusion but may require additional nodes to guide the process with canny edge detection.

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

**Score:** 41/100

**Reason:** Moderately useful as it can blend two latent representations but does not directly contribute to edge detection.

### Metadata

---

### LoadLatent (`LoadLatent`)

**Description:**

#### Inputs

- `latent` (required): `[[]]`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 81/100

**Reason:** Essential for loading pre-trained or existing latent representations into the workflow.

### Metadata

---

### VAE Decode (Tiled) (`VAEDecodeTiled`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `vae` (required): `VAE`
- `tile_size` (required): `INT`
  - Options: `{{'default': 512, 'min': 64, 'max': 4096, 'step': 32}}`
- `overlap` (required): `INT`
  - Options: `{{'default': 64, 'min': 0, 'max': 4096, 'step': 32}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** Essential for decoding VAE-encoded latents which are likely generated from an edge detection process and then rendering the image.

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

**Score:** 100/100

**Reason:** This node sets the timestep range for conditioning, which is directly related to canny edge detection in image generation.

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

**Reason:** This node loads CLIP models which are essential for guiding image generation with canny edge detection.

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

**Reason:** This node can load two different clip models which are useful for generating images guided by canny edge detection.

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

**Score:** 60/100

**Reason:** This node can load a diffusion model but it seems to be limited to only one specific type of model. It may not be as versatile as other nodes.

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

**Score:** 100/100

**Reason:** This node encodes text into a CLIP vector that can be used for guiding the diffusion model towards generating specific images based on edge detection.

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

**Score:** 100/100

**Reason:** This node encodes text into a CLIP vector that can be used for guiding the diffusion model towards generating specific images based on edge detection.

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

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it averages the magnitude of conditioning inputs, which could be used to refine the canny edge detection results.

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

**Reason:** This node calculates an average of two conditionings, which could be useful in generating a smoothed version of the canny edge detection output.

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

**Reason:** This node combines two conditionings, allowing for more complex manipulation of the canny edge detection output.

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

**Score:** 40/100

**Reason:** This node concatenates two conditionings, but it is not clear how this would be useful in image generation guided by canny edge detection.

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

**Reason:** This node directly sets an area for canny edge detection, which is a crucial step in the image generation process.

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

**Reason:** This node allows setting an area with percentage, making it more flexible and suitable for the workflow goal.

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

**Reason:** This node only sets the strength of canny edge detection, which is not directly relevant to the image generation process but could be useful as a supporting node.

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

**Reason:** This node allows setting a mask for canny edge detection, making it a moderately useful node in the workflow.

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

**Score:** 80/100

**Reason:** This node applies ControlNet, which is relevant to the workflow goal of image generation guided by canny edge detection. It takes in conditioning and control net inputs and applies them to an image.

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

**Score:** 90/100

**Reason:** This node also applies ControlNet, but with more advanced features such as positive and negative conditioning. This makes it very useful for the specified workflow goal.

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

**Score:** 95/100

**Reason:** This node sets the type of ControlNet to be used in the image generation process, which is directly related to canny edge detection. It allows for various types of control nets to be applied, making it essential for this workflow.

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

**Reason:** This node conditions the inpainting model based on canny edge detection and is essential for guiding image generation.

### Metadata

---

### 🖼️ Isulion Display Image From URL (`DisplayImageFromURL`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `image_url` (required): `STRING`
  - Options: `{{'multiline': False, 'default': ''}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node displays an image from a URL which could be used as input for the image generation guided by canny edge detection workflow goal.

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

**Reason:** This node combines two images which could be useful for comparing edges detected in each image.

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

**Reason:** Inverting the image is a preprocessing step that may help with edge detection but its relevance depends on the specific canny edge detection algorithm used.

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

**Reason:** This node pads the image for outpainting which could be useful if the goal involves generating images larger than the original input.

### Metadata

---

### Image Pad For Outpaint Target Size (`ImagePadForOutpaintTargetSize`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `target_width` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `target_height` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `feathering` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 1}}`
- `upscale_method` (required): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `mask` (optional): `MASK`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 100/100

**Reason:** This node directly pads images to a target size which could be useful in preparing images for outpainting.

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

**Score:** 80/100

**Reason:** This node loads an image which is a necessary step in the workflow goal of generating images guided by canny edge detection.

### Metadata

---

### Load Images From Folder (KJ) (`LoadImagesFromFolderKJ`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `folder` (required): `STRING`
  - Options: `{{'default': ''}}`
- `image_load_cap` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'step': 1}}`
- `start_index` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'step': 1}}`

#### Outputs

- `image`: `IMAGE`
- `mask`: `MASK`
- `count`: `INT`
- `image_path`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** Directly loads images from a folder which is necessary for canny edge detection.

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

**Score:** 90/100

**Reason:** Upscales images which may be necessary for canny edge detection depending on the desired output resolution.

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

**Score:** 81/100

**Reason:** This node is directly relevant to the workflow goal as it can upscale images, which is a necessary step in image generation guided by canny edge detection.

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

**Score:** 100/100

**Reason:** This node is essential for the workflow goal as it creates empty latent images that are required for denoising via sampling, a crucial step in generating images guided by canny edge detection.

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

**Score:** 95/100

**Reason:** This node is very useful for the workflow goal as it can upscale latent images, which is a necessary step in image generation guided by canny edge detection.

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

**Reason:** This node is essential for decoding latent images back into pixel space images which will be used as input for the canny edge detection.

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

**Score:** 80/100

**Reason:** This node is very useful as it allows setting a noise mask on latent samples which could be used for inpainting or other tasks related to canny edge detection.

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

**Score:** 90/100

**Reason:** This node is essential for the workflow goal as it uses VAE encoding for inpainting, directly aligning with the task of image generation guided by canny edge detection.

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

**Score:** 40/100

**Reason:** This node is marginally relevant to the workflow goal as it allows cropping latent samples, but this does not directly contribute to the task of image generation guided by canny edge detection.

### Metadata

---

### Load CLIP Vision (`CLIPVisionLoader`)

**Description:**

#### Inputs

- `clip_name` (required): `[]`

#### Outputs

- `CLIP_VISION`: `CLIP_VISION`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for this workflow as it loads CLIP vision models which are crucial for canny edge detection in image generation.

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

**Reason:** This node loads a ControlNet model which can be used with canny edge detection for image generation.

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

**Score:** 100/100

**Reason:** This node loads a ControlNet model and uses the loaded model to generate a control net, making it essential for this workflow.

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

**Reason:** This node loads a VAE model which could be used as a prior for image generation.

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

**Reason:** This node loads an unCLIP checkpoint which includes a VAE and could be used to generate images with canny edge detection.

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

**Score:** 100/100

**Reason:** This node loads an image as a mask, which is directly relevant to image generation guided by canny edge detection.

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

**Reason:** This primitive is a string value that could potentially be used as input for image processing but lacks direct relevance to the goal of canny edge detection.

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

**Reason:** This node uses denoising techniques and conditioning to generate images based on provided prompts and latent images, which aligns with the goal of image generation guided by canny edge detection.

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

**Score:** 40/100

**Reason:** This node is an advanced version of the KSampler that includes additional parameters for noise control but does not directly relate to canny edge detection or provide significant utility beyond the standard KSampler.

### Metadata

---

### Tara LLM API Key Loader (`TaraApiKeyLoader`)

**Description:**

**Module:** `ComfyUI-Tara-LLM-Integration`

#### Inputs

- `model` (required): `['openai/gpt-3.5-turbo', 'openai/gpt-4-turbo-preview', 'groq/llama2-70b-4096', 'groq/llama3-70b-8192', 'groq/llama3-8b-8192', 'groq/mixtral-8x7b-32768', 'groq/gemma-7b-it', 'together/coming-soon']`
  - Options: `{{'forceInput': True}}`
- `temporary` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `api_key`: `STRING`


### Applicability

**Score:** 100/100

**Reason:** This node loads a Tara LLM API key which is essential for accessing the LLM model required for image generation.

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

**Score:** 80/100

**Reason:** This node configures the LLM settings such as temperature and max tokens which are useful but not essential for image generation guided by canny edge detection.

### Metadata

---

### AdaptiveCannyDetector_PoP (`AdaptiveCannyDetector_PoP`)

**Description:**

**Module:** `comfy_PoP`

#### Inputs

- `images` (required): `IMAGE`
- `gaussian_blur_ksize` (required): `INT`
  - Options: `{{'default': 5, 'min': 1, 'max': 31, 'step': 1, 'description': 'Gaussian blur kernel size (if even +1 for odd)'}}`
- `gaussian_blur_sigma` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 10.0, 'step': 0.1, 'description': 'Gaussian blur sigma'}}`
- `adaptive_thresh_method` (required): `['GAUSSIAN_C', 'MEAN_C']`
- `adaptive_thresh_type` (required): `['BINARY', 'BINARY_INV']`
- `adaptive_thresh_blocksize` (required): `INT`
  - Options: `{{'default': 11, 'min': 3, 'max': 51, 'step': 1, 'description': 'Adaptive threshold block size (if even +1 for odd)'}}`
- `adaptive_thresh_C` (required): `INT`
  - Options: `{{'default': 2, 'min': 0, 'max': 10, 'step': 1, 'description': 'Adaptive threshold constant'}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node is specifically designed for adaptive canny edge detection and provides various parameters to customize the process, making it very useful for the specified workflow goal.

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

**Reason:** This node is essential for generating images based on latent samples from a VAE model.

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

**Score:** 100/100

**Reason:** This node is essential for encoding input images into latent space using a VAE model.

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

**Reason:** This node provides a comprehensive text prompt generation system that can be used in conjunction with canny edge detection for image generation.

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

**Reason:** This node integrates both text and vision prompts to generate images, making it highly relevant to the workflow goal.

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

**Reason:** This node provides a vision prompt generation system that can be used in conjunction with canny edge detection for image generation.

### Metadata

---
