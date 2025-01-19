# Filtered Nodes for: Generate large images using tiled vae decode

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

**Reason:** This node applies fuzzy intensity to a mask but doesn"t directly contribute to generating large images.

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

**Score:** 81/100

**Reason:** This node generates a seam mask based on input parameters which is crucial for the workflow goal of generating large images using tiled VAE decode.

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

**Score:** 61/100

**Reason:** This node exchanges or copies image and mask data between inputs and outputs but doesn"t directly contribute to generating large images.

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

**Reason:** This node allows for arbitrary operations on masks and images but its direct relevance to the workflow goal is limited.

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

**Reason:** This node directly affects image size by allowing extension of the mask.

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

**Reason:** This node is marginally relevant as it expands the mask but lacks a clear impact on image size.

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

**Score:** 92/100

**Reason:** This node has multiple options to blur or expand edges which can significantly affect the image size and quality.

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

**Reason:** This node blurs the mask edges but its relevance is moderate as it does not directly impact image size.

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

**Score:** 95/100

**Reason:** This node is highly relevant to generating large images using tiled VAE decode, as it provides a wide range of scene settings that can be used to create detailed and realistic backgrounds.

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

**Score:** 80/100

**Reason:** This node is moderately useful for the workflow goal, as it allows users to control lighting effects in their scenes, which can add depth and realism to the generated images.

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

**Score:** 85/100

**Reason:** This node is very useful for generating large images using tiled VAE decode, as it provides a wide range of style categories that can be used to create unique and visually appealing art styles.

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

**Score:** 90/100

**Reason:** This node is highly relevant to the workflow goal, as it allows users to control lens effects in their scenes, which can add depth and realism to the generated images.

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

**Score:** 100/100

**Reason:** This node is directly related to character generation, which can be used as a supporting node for the workflow goal of generating large images using tiled VAE decode.

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

**Score:** 61/100

**Reason:** This node generates a random prompt which could be useful as input for other nodes in the workflow.

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

**Reason:** This node stitches cropped images together, directly contributing to generating large images using tiled VAE decode.

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

**Score:** 41/100

**Reason:** This node crops an image based on a mask, which could be useful as a supporting node for the workflow, but is not directly related to the goal.

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

**Reason:** This node adds text watermarks to images, which is essential for adding metadata and visual identifiers to large images generated using tiled VAE decode.

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

**Reason:** This node can swap integer, float, and text inputs which could be useful for processing image data in the workflow.

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

**Reason:** This node provides image size information which can be useful in determining the optimal tile size for decoding.

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

**Score:** 90/100

**Reason:** This node loads an image from a file path, which is necessary as input to the tiled vae decode process.

### Metadata

---

### 2🐕Image scaling lock (`EG_TX_SFBLS`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `image` (required): `IMAGE`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 10000, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 0, 'max': 10000, 'step': 1}}`
- `crop` (required): `['disabled', 'center']`
- `upscale_method` (optional): `['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']`
- `lock_aspect_ratio` (optional): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `image`: `IMAGE`
- `width`: `INT`
- `height`: `INT`

## 2🐕/🖼️IMAGE/🎨COLOR PROCESSING


### Applicability

**Score:** 81/100

**Reason:** This node is essential for scaling images to a larger size using tiled VAE decode.

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

**Score:** 40/100

**Reason:** This node can be used as a supporting node by adjusting the strength of color migration, but it is not directly relevant to the workflow goal.

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

**Reason:** This node is very useful as it preserves brightness which might be necessary for the workflow goal.

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

**Score:** 90/100

**Reason:** This node is essential for this workflow as it allows color adjustment of the image, a crucial step in generating large images using tiled VAE decode.

### Metadata

---

### 2🐕Free input box (`EG_ZY_WBK`)

**Description:**

**Module:** `Comfyui-ergouzi-Nodes`

#### Inputs

- `number1` (required): `STRING`
  - Options: `{{'multiline': True, 'default': ''}}`

#### Outputs

- `result_int`: `INT`
- `result_float`: `FLOAT`
- `result_str`: `STRING`

## 2🐕/🤿LATENT


### Applicability

**Score:** 40/100

**Reason:** This node provides a free input box but its relevance to the workflow goal is limited due to its generic nature and lack of specific features for image generation.

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

**Reason:** This node directly generates latent variables with specified dimensions, which is essential for generating large images using tiled VAE decode.

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

**Reason:** This node is directly responsible for generating large images using tiled VAE decode.

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

**Reason:** This node generates art styles that can be used in conjunction with other nodes to create large images using tiled VAE decode.

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

**Reason:** This node generates an emotion prompt which can be used to condition the VAE decoder for specific emotions in the generated image.

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

**Score:** 90/100

**Reason:** This node loads a model and its associated components (VAE, CLIP, etc.) which are essential for the specified workflow goal of generating large images using tiled VAE decode.

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

**Score:** 60/100

**Reason:** This node generates prompts that can be used to condition the generation of large images using tiled VAE decode, but it is not directly necessary for the process.

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

**Score:** 100/100

**Reason:** This node is directly responsible for saving generated images.

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

**Score:** 40/100

**Reason:** This node adds text to an image but does not contribute to generating large images using tiled vae decode.

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

**Reason:** This node is essential for resizing images to a larger size as part of the tiled VAE decode process.

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

**Reason:** This node provides some useful information about image sizes but does not directly contribute to generating large images.

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

**Reason:** This node is moderately useful for loading an initial image that can be used as input for other nodes in the workflow.

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

**Reason:** This node is essential for providing a fixed seed value required by the workflow goal of generating large images using tiled VAE decode.

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

**Reason:** This node is essential for the workflow goal as it converts integer values into strings that can be used in the image generation process.

### Metadata

---

### Get latent size (`DF_Get_latent_size`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `latent` (required): `LATENT`
  - Options: `{{'forceInput': False}}`
- `original` (required): `[False, True]`

#### Outputs

- `WIDTH`: `INT`
- `HEIGHT`: `INT`


### Applicability

**Score:** 100/100

**Reason:** This node retrieves latent size information which is directly relevant to generating large images using tiled VAE decode.

### Metadata

---

### Int to Float (`DF_Int_to_Float`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value` (required): `INT`
  - Options: `{{'default': 1, 'min': -9223372036854775807, 'max': 9223372036854775807, 'step': 1, 'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`

## DERFUU_NODES/FUNCTIONS/STRING OPERATIONS


### Applicability

**Score:** 80/100

**Reason:** Int to Float can convert the image size from integer to float format which is necessary for tiled VAE decode.

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

**Score:** 70/100

**Reason:** The square root operation can be used to calculate the size of the image or other parameters for the tiled VAE decode process.

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

**Reason:** Summing values can be used to combine multiple parameters for the tiled VAE decode process, making it moderately useful for this workflow goal.

### Metadata

---

### Sinus (`DF_Sinus`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `value` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 0.01, 'forceInput': False}}`
- `type_` (required): `['RAD', 'DEG']`
  - Options: `{{'forceInput': False}}`
- `arcSin` (required): `[False, True]`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 41/100

**Reason:** Sine function can be used in image generation and processing, particularly for tasks involving frequency analysis or wave manipulation, making it moderately useful for this workflow goal.

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

**Score:** 61/100

**Reason:** Conditioning area scale by ratio can be used to adjust the size and proportions of generated images, making it very useful for this workflow goal.

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

**Score:** 100/100

**Reason:** Directly scales images to desired size using tiled VAE decode.

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

**Score:** 80/100

**Reason:** Supports scaling images by side length, but requires manual calculation of upscale ratio.

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

**Score:** 90/100

**Reason:** Scales latent space by ratio, useful for adjusting image size without affecting detail.

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

**Score:** 70/100

**Reason:** Supports scaling latent space to a specific side length, but may require additional processing steps.

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

**Score:** 90/100

**Reason:** This node can provide a float value that could be used as an input for the tiled vae decode process.

### Metadata

---

### Integer (`DF_Integer`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Value` (required): `FLOAT`
  - Options: `{{'default': 1, 'min': -1.7976931348623157e+308, 'max': 1.7976931348623157e+308, 'step': 1, 'forceInput': False}}`

#### Outputs

- `INT`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node can provide an integer value, but it may not be directly useful for generating large images using tiled vae decode without further processing.

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

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it allows scheduling of batch prompts and can handle various inputs such as text, clip, max frames, etc.

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

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it also allows scheduling of batch prompts and can handle various inputs such as width, height, target width, target height, etc.

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

**Score:** 80/100

**Reason:** This node is very useful for generating large images using tiled VAE decode as it allows scheduling of batch prompts with latent input and can handle various inputs such as text, clip, num latents, etc.

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

**Score:** 90/100

**Reason:** This node provides a batch prompt schedule with latent input, which is directly relevant to generating large images using tiled VAE decode.

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

**Score:** 80/100

**Reason:** This node provides a batch value schedule with latent input, which is moderately useful for generating large images using tiled VAE decode.

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

**Reason:** This node is essential for generating large images using tiled vae decode as it allows for the creation of a FizzFrame which can be used to initialize the decoding process.

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

**Score:** 61/100

**Reason:** This node is moderately useful for generating large images using tiled vae decode as it concatenates frames but does not directly contribute to the generation of large images.

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

**Reason:** This node is marginally relevant for generating large images using tiled vae decode as it initializes a FizzFrame with text and frame information but can be bypassed if an existing FizzFrame is available.

### Metadata

---

### Calculate Frame Offset 📅🅕🅝 (`CalculateFrameOffset`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `current_frame` (required): `INT`
  - Options: `{{'default': 0, 'min': 0}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 18, 'min': 0}}`
- `num_latent_inputs` (required): `INT`
  - Options: `{{'default': 4, 'min': 0}}`
- `index` (required): `INT`
  - Options: `{{'default': 4, 'min': 0}}`

#### Outputs

- `INT`: `INT`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it calculates frame offsets, which are crucial for image generation.

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

**Score:** 61/100

**Reason:** This node is very useful as it selects images based on a schedule and current frame number, which can help in generating large images using tiled VAE decode by selecting relevant images at specific frames.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it schedules the prompt.

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

**Score:** 61/100

**Reason:** This node is moderately useful for generating large images using tiled VAE decode as it allows for encoding SDXL prompts but lacks specific features for this goal.

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

**Score:** 41/100

**Reason:** This node is marginally relevant for generating large images using tiled VAE decode as it schedules the prompt flow but does not provide any specific features for this goal.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it schedules the prompt flow end and provides necessary inputs.

### Metadata

---

### Value Schedule 📅🅕🅝 (`ValueSchedule`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `text` (required): `STRING`
  - Options: `{{'multiline': True, 'default': '0:(0),\n11:(0),\n23:(0),\n35:(0),\n47:(0),\n59:(0),\n71:(0),\n83:(0),\n95:(0),\n107:(0),\n119:(0)\n'}}`
- `max_frames` (required): `INT`
  - Options: `{{'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0, 'forceInput': True}}`
- `print_output` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`

## FIZZNODES 📅🅕🅝/WAVENODES


### Applicability

**Score:** 80/100

**Reason:** This node seems very useful for the specified workflow goal as it can generate values based on input text and schedule them. The output FLOAT and INT can be used in the VAE decode process.

### Metadata

---

### AbsCosWave 📅🅕🅝 (`AbsCosWave`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `phase` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `amplitude` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}}`
- `x_translation` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `max_value` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant to generating large images using tiled VAE decode. It generates a wave pattern that could potentially be used as an input for the VAE decode process, but its direct relevance is unclear.

### Metadata

---

### AbsSinWave 📅🅕🅝 (`AbsSinWave`)

**Description:**

**Module:** `ComfyUI_FizzNodes`

#### Inputs

- `phase` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `amplitude` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}}`
- `x_translation` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`
- `max_value` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}}`
- `current_frame` (required): `INT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}}`

#### Outputs

- `FLOAT`: `FLOAT`
- `INT`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant to generating large images using tiled VAE decode. It also generates a wave pattern similar to AbsCosWave, which could potentially be used as an input for the VAE decode process, but its direct relevance is unclear.

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

**Score:** 81/100

**Reason:** This node is directly relevant to generating large images using tiled VAE decode as it can be used to control wave-like patterns.

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

**Score:** 81/100

**Reason:** This node is similar to CosWave and also directly relevant to generating large images using tiled VAE decode.

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

**Score:** 81/100

**Reason:** This node is similar to CosWave and InvCosWave, and can be used to control wave-like patterns in the image generation process.

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

**Score:** 60/100

**Reason:** This node generates a sine wave which could be useful for creating patterns in the image generation process.

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

**Score:** 60/100

**Reason:** This node generates a square wave which could be useful for creating patterns in the image generation process.

### Metadata

---

### TriangleWave 📅🅕🅝 (`TriangleWave`)

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

## IMPACTFRAMES💥🎞️/UTILS


### Applicability

**Score:** 60/100

**Reason:** This node generates a triangle wave which could be useful for creating patterns in the image generation process.

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

**Score:** 90/100

**Reason:** This node can generate multiple prompts for image generation tasks, which could be useful in creating diverse and varied images for the workflow goal of generating large images using tiled VAE decode.

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

**Score:** 80/100

**Reason:** This node generates clothing items that could potentially be used as input to a VAE model for image synthesis. However, it may not directly contribute to generating large images using tiled VAE decode.

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

**Reason:** This node can generate epochs or time periods that could be used as input to a VAE model for image synthesis. However, it may not directly contribute to generating large images using tiled VAE decode.

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

**Reason:** This node can generate a prompt for a mega image that can be used with tiled VAE decode to create large images.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it enhances the input prompt to improve image quality.

### Metadata

---

### ⚔️ Isulion Artifact Generator (`IsulionArtifactGenerator`)

**Description:**

**Module:** `ComfyUI_Isulion`

#### Inputs

- `randomize` (required): `['enable', 'disable']`
- `artifact` (required): `['legendary sword', 'mystic staff', 'enchanted bow', 'divine spear', 'dragon slayer blade', 'phoenix feather wand', 'thunder hammer', 'frost axe', 'soul reaver', 'starforged blade', 'crystal dagger', 'void staff', 'light bringer', 'shadow blade', 'power amulet', 'magic ring', 'crystal crown', 'soul gem', 'dragon heart pendant', 'phoenix eye necklace', 'moonstone ring', 'sunfire crown', 'starlight tiara', 'void crystal', 'eternity band', 'wisdom pendant', "fate's circlet", 'dream catcher', 'seeing glass', 'teleport stone', 'wisdom scroll', 'healing chalice', 'truth mirror', 'fate dice', 'levitation boots', 'cloak of shadows', 'bag of holding', 'time turner', 'memory crystal', 'dreamcatcher', 'compass of desires', 'book of secrets', 'ancient tablet', 'dragon scale', 'phoenix feather', 'unicorn horn', "mermaid's tear", "giant's tooth", 'fairy dust', "demon's heart", "angel's feather", "dragon's eye", "witch's grimoire", "wizard's orb", 'elemental crystal', 'void shard']`
- `seed` (optional): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 18446744073709551615}}`
- `type` (optional): `['any', 'weapon', 'jewelry', 'tool', 'relic']`
  - Options: `{{'default': 'any'}}`

#### Outputs

- `artifact`: `STRING`
- `seed`: `INT`


### Applicability

**Score:** 40/100

**Reason:** This node has some utility in generating large images using tiled VAE decode as it can generate artifacts that could be used in the image, but its relevance is limited to specific use cases.

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

**Reason:** This node can generate a collage of multiple images which could be used as input for the tiled VAE decode process.

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

**Reason:** This node loads images from a directory but does not directly contribute to generating large images using tiled VAE decode.

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

**Score:** 100/100

**Reason:** This node directly displays large images using tiled VAE decode from Civitai.

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

**Score:** 80/100

**Reason:** This node can generate alien worlds with various features that could be used as backgrounds for large image generation.

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

**Score:** 40/100

**Reason:** This node generates spacecraft designs but may not have a direct impact on the workflow goal of generating large images using tiled VAE decode.

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

**Score:** 81/100

**Reason:** Directly generates latent images with specified dimensions, essential for generating large images using tiled VAE decode.

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

**Score:** 100/100

**Reason:** Provides a list of predefined dimensions, making it easy to generate large images using tiled VAE decode.

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

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it provides intrinsic Lora sampling which is a key component of the process.

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

**Reason:** This node is very useful as it draws the tracking data from CreateInstanceDiffusionTracking-node, which is essential for visualizing and understanding the image generation process.

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

**Score:** 41/100

**Reason:** This node creates masks based on normalized amplitude but does not directly contribute to image generation. It could be used as a supporting node.

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

**Reason:** This node is very useful as it perturbs weights in a model, which can be used to fine-tune or modify the behavior of the model during the image generation process using tiled VAE decode.

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

**Reason:** This node can be used as a supporting node for fine-tuning or modifying the diffusion model before decoding.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it allows scheduling GLIGEN text box positions in a batch.

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

**Reason:** This node is essential for capturing an area specified by screen coordinates which can be used with the tiled VAE decode workflow.

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

**Score:** 81/100

**Reason:** This node is essential for generating large images using tiled vae decode as it patches the model to load weight patches (LoRAs) before compiling, which is a crucial step in this workflow.

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

**Score:** 40/100

**Reason:** This node has some relevance but its utility is limited as it only patches attention mode and may not directly contribute to generating large images using tiled vae decode.

### Metadata

---

### Plot Coordinates (`PlotCoordinates`)

**Description:**


Plots coordinates to sequence of images using Matplotlib.  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `text` (required): `STRING`
  - Options: `{{'default': 'title', 'multiline': False}}`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 8, 'max': 4096, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 8, 'max': 4096, 'step': 8}}`
- `bbox_width` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 8}}`
- `bbox_height` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 8}}`
- `size_multiplier` (optional): `FLOAT`
  - Options: `{{'default': [1.0], 'forceInput': True}}`

#### Outputs

- `images`: `IMAGE`
- `width`: `INT`
- `height`: `INT`
- `bbox_width`: `INT`
- `bbox_height`: `INT`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for visualizing the coordinates generated in the workflow goal, making it a critical component of this process.

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

**Score:** 100/100

**Reason:** Directly schedules azimuth and elevation conditions for SV3D, aligning with the workflow goal of generating large images using tiled VAE decode.

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

**Reason:** Calls StabilityAI API for image generation, aligning with the workflow goal of generating large images using tiled VAE decode.

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

**Score:** 90/100

**Reason:** Schedules azimuth and elevation conditions for Stable Zero123, contributing to generating large images using tiled VAE decode, but lacks direct relevance compared to Node 1.

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

**Reason:** This node is essential as it applies the style model with strength parameter which is directly relevant to generating large images.

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

**Score:** 40/100

**Reason:** This node has some relevance but its utility is limited as it only compiles the control net without any specific parameters for large image generation.

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

**Score:** 61/100

**Reason:** This node has some relevance and utility as it compiles a model with advanced parameters such as full graph mode and dynamic mode which could be helpful in generating large images.

### Metadata

---

### TorchCompileVAE (`TorchCompileVAE`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `vae` (required): `VAE`
- `backend` (required): `['inductor', 'cudagraphs']`
- `fullgraph` (required): `BOOLEAN`
  - Enable full graph mode
  - Options: `{{'default': False, 'tooltip': 'Enable full graph mode'}}`
- `mode` (required): `['default', 'max-autotune', 'max-autotune-no-cudagraphs', 'reduce-overhead']`
  - Options: `{{'default': 'default'}}`
- `compile_encoder` (required): `BOOLEAN`
  - Compile encoder
  - Options: `{{'default': True, 'tooltip': 'Compile encoder'}}`
- `compile_decoder` (required): `BOOLEAN`
  - Compile decoder
  - Options: `{{'default': True, 'tooltip': 'Compile decoder'}}`

#### Outputs

- `VAE`: `VAE`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it compiles the VAE model which is a prerequisite for decoding.

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

**Score:** 40/100

**Reason:** This node is marginally useful as it can create a gradient image which might be used as input for the VAE model, but its direct relevance to the workflow goal is limited.

### Metadata

---

### Create Shape Image On Path (`CreateShapeImageOnPath`)

**Description:**


Creates an image or batch of images with the specified shape.  
Locations are center locations.  


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `shape` (required): `['circle', 'square', 'triangle']`
  - Options: `{{'default': 'circle'}}`
- `coordinates` (required): `STRING`
  - Options: `{{'forceInput': True}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `shape_width` (required): `INT`
  - Options: `{{'default': 128, 'min': 2, 'max': 4096, 'step': 1}}`
- `shape_height` (required): `INT`
  - Options: `{{'default': 128, 'min': 2, 'max': 4096, 'step': 1}}`
- `shape_color` (required): `STRING`
  - Options: `{{'default': 'white'}}`
- `bg_color` (required): `STRING`
  - Options: `{{'default': 'black'}}`
- `blur_radius` (required): `FLOAT`
  - Options: `{{'default': 0.0, 'min': 0.0, 'max': 100, 'step': 0.1}}`
- `intensity` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.01, 'max': 100.0, 'step': 0.01}}`
- `size_multiplier` (optional): `FLOAT`
  - Options: `{{'default': [1.0], 'forceInput': True}}`
- `trailing` (optional): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `image`: `IMAGE`
- `mask`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it can create an image or batch of images with a specified shape.

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

**Score:** 40/100

**Reason:** This node is moderately useful as it can perform a multi-image cross fade, but its utility depends on the number of input images and the complexity of the workflow.

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

**Score:** 81/100

**Reason:** Essential for determining image size and count.

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

**Score:** 41/100

**Reason:** Moderately useful for selecting specific images from a batch.

### Metadata

---

### Image Batch Multi (`ImageBatchMulti`)

**Description:**


Creates an image batch from multiple images.  
You can set how many inputs the node has,  
with the **inputcount** and clicking update.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 1000, 'step': 1}}`
- `image_1` (required): `IMAGE`
- `image_2` (required): `IMAGE`

#### Outputs

- `images`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Directly generates a batch of images which can be used as input for tiled VAE decode.

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

**Score:** 96/100

**Reason:** Essential for repeating each image in the batch to create larger images using tiled VAE decode.

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

**Score:** 98/100

**Reason:** Directly concatenates a batch of images into a grid which can be used as input for tiled VAE decode.

### Metadata

---

### Image Concatenate Multi (`ImageConcatMulti`)

**Description:**


Creates an image from multiple images.  
You can set how many inputs the node has,  
with the **inputcount** and clicking update.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 1000, 'step': 1}}`
- `image_1` (required): `IMAGE`
- `image_2` (required): `IMAGE`
- `direction` (required): `['right', 'down', 'left', 'up']`
  - Options: `{{'default': 'right'}}`
- `match_image_size` (required): `BOOLEAN`
  - Options: `{{'default': False}}`

#### Outputs

- `images`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for combining multiple images into a single large image, which is directly relevant to the workflow goal.

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

**Score:** 100/100

**Reason:** This node is essential for combining four input images into a single 2x2 grid image, which aligns with the workflow goal of generating large images.

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

**Score:** 100/100

**Reason:** This node is essential for combining nine input images into a single 3x3 grid image, which directly supports the workflow goal of generating large images.

### Metadata

---

### Image Grid To Batch (`ImageGridtoBatch`)

**Description:**

Converts a grid of images to a batch of images.

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image` (required): `IMAGE`
- `columns` (required): `INT`
  - The number of columns in the grid.
  - Options: `{{'default': 3, 'min': 1, 'max': 8, 'tooltip': 'The number of columns in the grid.'}}`
- `rows` (required): `INT`
  - The number of rows in the grid. Set to 0 for automatic calculation.
  - Options: `{{'default': 0, 'min': 1, 'max': 8, 'tooltip': 'The number of rows in the grid. Set to 0 for automatic calculation.'}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Directly relevant to generating large images by converting a grid of images to a batch.

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

**Score:** 100/100

**Reason:** Essential for normalizing images to the range [-1, 1] required by tiled VAE decode.

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

**Score:** 61/100

**Reason:** Moderately useful for resizing images, but may not be necessary if the goal is to generate large images using tiled VAE decode.

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

**Score:** 80/100

**Reason:** Directly relevant to uncrop large images using tiled vae decode.

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

**Score:** 90/100

**Reason:** Essential for upscaling images using a model in the workflow.

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

**Score:** 40/100

**Reason:** Marginally useful for inserting images into a batch at specific indices, but not directly applicable to tiled vae decode.

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

**Score:** 100/100

**Reason:** Directly loads and resizes images to desired dimensions.

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

**Score:** 80/100

**Reason:** Very useful as it allows remapping of image values to a specified range which is essential in generating high-quality large images using tiled VAE decode.

### Metadata

---

### Replace Images In Batch (`ReplaceImagesInBatch`)

**Description:**


Replaces the images in a batch, starting from the specified start index,  
with the replacement images.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `original_images` (required): `IMAGE`
- `replacement_images` (required): `IMAGE`
- `start_index` (required): `INT`
  - Options: `{{'default': 1, 'min': 0, 'max': 4096, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 81/100

**Reason:** Essential for replacing original images with replacement images in a batch.

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

**Score:** 61/100

**Reason:** Very useful for saving generated images to the output directory.

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

**Score:** 41/100

**Reason:** Moderately useful for saving an image and mask as a .PNG with alpha channel, but may not be necessary in this workflow goal.

### Metadata

---

### Shuffle Image Batch (`ShuffleImageBatch`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `images` (required): `IMAGE`
- `seed` (required): `INT`
  - Options: `{{'default': 123, 'min': 0, 'max': 18446744073709551615, 'step': 1}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 41/100

**Reason:** Shuffles image batch but doesn"t directly contribute to generating large images using tiled VAE decode.

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

**Reason:** Splits image channels into individual images which can be useful for processing and decoding large images.

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

**Score:** 100/100

**Reason:** This node is essential for the workflow as it allows cropping of images from masks, which can be used in conjunction with tiled VAE decode to generate large images.

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

**Score:** 90/100

**Reason:** This node is very useful for the workflow as it provides advanced features such as combining cropped images and masks, making it a crucial step in generating large images using tiled VAE decode.

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

**Reason:** This node is essential for the workflow as it allows uncropping of images from their cropped versions, which can be used to generate large images using tiled VAE decode.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it uncrops and combines cropped images.

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

**Score:** 81/100

**Reason:** Directly downloads and loads CLIPSeg model required for image generation.

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

**Score:** 91/100

**Reason:** Filters out empty masks and corresponding images, essential for processing and decoding large images.

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

**Reason:** Returns mask size and count, moderately useful but not directly relevant to the workflow goal.

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

**Score:** 61/100

**Reason:** Grows mask with blur, very useful as a supporting node for image generation and decoding.

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

**Score:** 90/100

**Reason:** Offsets the mask by a specified amount which can be useful for creating larger images by duplicating and offsetting the mask.

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

**Reason:** Resizes the mask or batch of masks which can be useful for creating larger images by resizing the mask to a specified width and height.

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

**Reason:** This node splits bounding boxes into two lists at a specified index, which can be useful for processing and organizing data in the workflow.

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

**Score:** 61/100

**Reason:** This node combines multiple conditioning nodes into one, potentially simplifying the workflow by reducing the number of nodes to manage.

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

**Reason:** Essential for combining multiple conditioning masks into one, which is necessary for generating large images using tiled VAE decode.

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

**Score:** 81/100

**Reason:** Essential for combining multiple conditioning masks into one, which is necessary for generating large images using tiled VAE decode. This node has more inputs than the first one, allowing for even more complex mask combinations.

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

**Score:** 81/100

**Reason:** Essential for combining multiple conditioning masks into one, which is necessary for generating large images using tiled VAE decode. This node also allows for five conditioning masks to be combined, making it a good choice if the workflow requires this level of complexity.

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

**Score:** 61/100

**Reason:** Moderately useful for creating fade masks that can be used in conjunction with other nodes to generate large images using tiled VAE decode. However, its utility is more indirect compared to the conditioning mask combination nodes.

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

**Reason:** This node directly generates a fluid mask which can be used as input for tiled VAE decode to generate large images.

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

**Reason:** This node creates a gradient mask but it does not support the required functionality of generating large images using tiled VAE decode.

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

**Reason:** This node generates a magic mask which can be used as input for tiled VAE decode to generate large images, but its parameters are less intuitive than Create Fluid Mask.

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

**Score:** 81/100

**Reason:** This node directly creates a shape mask which can be used as input for tiled VAE decode to generate large images with specific shapes and animations.

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

**Reason:** This node can create text on a path which could be useful in generating large images with text.

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

**Reason:** This node can convert float values into masks but may not be directly useful for generating large images using tiled VAE decode without additional context.

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

**Score:** 61/100

**Reason:** Useful as a supporting node to bypass inputs in the workflow

### Metadata

---

### ModelPass (`ModelPassThrough`)

**Description:**


    Simply passes through the model,
    workaround for Set node not allowing bypassed inputs.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `model` (optional): `MODEL`

#### Outputs

- `model`: `MODEL`


### Applicability

**Score:** 61/100

**Reason:** Useful as a supporting node to bypass model inputs in the workflow

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

**Reason:** This node generates sigmas tensors from a string of comma-separated values which can be used in the tiled VAE decode process.

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

**Reason:** This node adjusts and manipulates sigmas tensors which is crucial for fine-tuning the tiled VAE decode process.

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

**Reason:** This node is moderately useful as it can convert float values to sigmas tensor, which might be necessary for some steps in generating large images using tiled VAE decode.

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

**Score:** 91/100

**Reason:** This node is very useful as it generates noise that can be used as empty latents on samplers with add_noise off, a crucial step in generating large images using tiled VAE decode.

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

**Score:** 81/100

**Reason:** This node is essential for this workflow as it injects noise into the latent space, which is necessary for generating diverse and high-quality images.

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

**Reason:** This node is moderately useful as it can convert sigmas tensors to float values, but its direct relevance to the workflow goal is limited compared to other nodes.

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

**Score:** 100/100

**Reason:** This node creates a text mask which can be used as input for tiled VAE decode.

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

**Reason:** This node is essential for generating detailed prompts that can be used to produce large images using tiled VAE decode.

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

**Reason:** While this node could potentially provide useful information for other parts of the workflow, it is not directly relevant to the goal of generating large images.

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

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it uses LLMs to generate detailed image descriptions based on user prompts.

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

**Reason:** This node is very useful for generating large images using tiled VAE decode as it uses LLMs Vision to understand and describe the input image.

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

**Score:** 40/100

**Reason:** This node can be used as a supporting node to compare values in the workflow, but it may not be directly applicable to generating large images.

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

**Score:** 61/100

**Reason:** This node can be used to set an integer value which could be useful for specifying image dimensions or other parameters in the workflow.

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

**Score:** 81/100

**Reason:** This node allows setting a string value which is likely necessary for specifying file paths or other text-based inputs in the workflow.

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

**Score:** 100/100

**Reason:** This node directly generates aspect ratios and dimensions based on user input, making it essential for generating large images with specific resolutions.

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

**Reason:** This node can be used to adjust the conditioning multiplier, but its direct relevance to generating large images is limited.

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

**Reason:** This node normalizes the conditioning input, which is crucial for the tiled VAE decode process and thus essential for this workflow.

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

**Score:** 100/100

**Reason:** This node resizes images to a specified megapixel value, directly contributing to generating large images as per the workflow goal.

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

**Reason:** This node might be marginally useful for logging integer values during the workflow but does not contribute significantly to achieving the goal.

### Metadata

---

### Log (VEC2) (`LogVec2`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `VEC2`
  - Options: `{{'forceInput': True}}`
- `prefix` (optional): `STRING`
  - Options: `{{'multiline': True, 'default': 'Value:'}}`

#### Outputs

- `VEC2`: `VEC2`


### Applicability

**Score:** 40/100

**Reason:** This node could potentially be useful if the log output contains information about the tiled VAE decode process, but its relevance depends on the specific implementation and data being logged.

### Metadata

---

### Log (VEC3) (`LogVec3`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `VEC3`
  - Options: `{{'forceInput': True}}`
- `prefix` (optional): `STRING`
  - Options: `{{'multiline': True, 'default': 'Value:'}}`

#### Outputs

- `VEC3`: `VEC3`


### Applicability

**Score:** 60/100

**Reason:** Similar to Node 2, this node might be useful if it logs relevant information about the tiled VAE decode process. However, without more context, its utility is moderate at best.

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

**Score:** 80/100

**Reason:** This node can convert float values to strings which might be necessary during the tiled VAE decode process.

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

**Score:** 70/100

**Reason:** This node can convert integer values to strings which might be necessary during the tiled VAE decode process.

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

**Reason:** This node can select one option from multiple choices and return it as a string. It might be useful if the workflow goal involves selecting a specific option for image generation.

### Metadata

---

### Repeat (NUMBER) (`RF_RangeNumber`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `start` (required): `NUMBER`
  - Options: `{{'default': 0}}`
- `step` (required): `NUMBER`
  - Options: `{{'default': 1}}`
- `count` (required): `NUMBER`
  - Options: `{{'default': 10}}`

#### Outputs

- `values`: `NUMBER` (LIST)


### Applicability

**Score:** 40/100

**Reason:** Similar to Node 1, this node can be used for repetition but it doesn"t directly contribute to the workflow goal.

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

**Reason:** This node provides a way to input text which can be used as a template for the tiled vae decode process.

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

**Reason:** This node can replace text in a string, but it does not directly contribute to generating large images using tiled vae decode. It could be useful if the replacement text is related to image generation.

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

**Score:** 61/100

**Reason:** This node is very useful for the specified workflow goal as it can convert VEC2 values to strings, which might be necessary for image generation.

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

**Score:** 81/100

**Reason:** This node is essential for the specified workflow goal as it can convert VEC3 values to strings, which are likely required for generating large images using tiled vae decode.

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

**Reason:** This node provides advanced options configuration that can be used to fine-tune the LLM model for generating large images.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it takes in text input and produces the generated image.

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

**Reason:** This node is moderately useful for generating large images using tiled VAE decode as it provides options for differential diffusion and can be used in conjunction with other nodes.

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

**Reason:** This node is directly responsible for blending latent vectors to generate large images using tiled VAE decode.

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

**Reason:** This node directly generates large images using tiled VAE decode by decoding latent samples.

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

**Reason:** This node is essential for generating large images using tiled VAE decode as it encodes input pixels into a latent space that can be decoded by subsequent nodes.

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

**Reason:** This node loads dual CLIP models which are essential for the specified workflow goal.

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

**Reason:** This node is essential for encoding text into a format that can be used to guide the diffusion model towards generating specific images.

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

**Reason:** This node is essential for encoding text into a format that can be used to guide the diffusion model towards generating specific images.

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

**Reason:** This node is essential for the specified workflow goal as it allows adjusting the conditioning strength for average keep magnitude.

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

**Reason:** This node calculates an average of two conditioning inputs, which could be useful for combining information from multiple sources in the generation process.

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

**Reason:** This node combines two conditioning inputs, which is directly relevant to generating large images using tiled VAE decode by allowing the combination of different conditioning signals.

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

**Reason:** Directly sets area in CONDITIONING for large image generation.

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

**Score:** 61/100

**Reason:** Sets area with percentage in CONDITIONING but requires manual scaling to achieve large images.

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

**Reason:** Only adjusts strength of conditioning, which may not be sufficient for generating large images.

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

**Reason:** This node is very useful as it applies ControlNet to the input image, which can be used for generating large images using tiled VAE decode.

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

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled VAE decode as it provides advanced control over the ControlNet application process.

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

**Score:** 61/100

**Reason:** This node is moderately useful as it allows setting the type of ControlNet to be used in the workflow, but its relevance depends on the specific requirements of the workflow goal.

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

**Reason:** This node is essential for generating large images using tiled vae decode as it applies a GLIGEN text box model to generate conditioning.

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

**Reason:** This node is moderately useful for the workflow goal as it conditions an image using inpainting but does not directly contribute to generating large images.

### Metadata

---

### EmptyImage (`EmptyImage`)

**Description:**

#### Inputs

- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 1, 'max': 16384, 'step': 1}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 1, 'max': 16384, 'step': 1}}`
- `batch_size` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 4096}}`
- `color` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16777215, 'step': 1, 'display': 'color'}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 100/100

**Reason:** This node is essential for generating large images using tiled vae decode as it provides the initial image dimensions.

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

**Reason:** This node is very useful for generating large images using tiled vae decode as it allows padding and outpainting of images.

### Metadata

---

### Image Pad For Outpaint Masked (`ImagePadForOutpaintMasked`)

**Description:**

**Module:** `ComfyUI-KJNodes`

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
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 1}}`
- `mask` (optional): `MASK`

#### Outputs

- `IMAGE`: `IMAGE`
- `MASK`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for padding images to a specific size for outpainting, which is crucial for generating large images using tiled VAE decode.

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

**Score:** 90/100

**Reason:** This node is very useful as it allows for precise control over the output image size and upscale method, making it ideal for generating large images using tiled VAE decode.

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

**Score:** 100/100

**Reason:** This node is essential for loading images from a folder which is a necessary step in generating large images using tiled VAE decode.

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

**Reason:** This node is essential for upscaling images in the workflow.

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

**Reason:** This node is crucial for generating empty latent images to be denoised via sampling, which is a necessary step in the workflow.

### Metadata

---

### Latent Composite (`LatentComposite`)

**Description:**

#### Inputs

- `samples_to` (required): `LATENT`
- `samples_from` (required): `LATENT`
- `x` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `y` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`
- `feather` (required): `INT`
  - Options: `{{'default': 0, 'min': 0, 'max': 16384, 'step': 8}}`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 40/100

**Reason:** This node can be used to combine multiple latent samples, but it may not directly contribute to upscaling large images using tiled VAE decode.

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

**Reason:** This node is very useful for upsampling latent images in the workflow, allowing for flexible scaling and cropping options.

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

**Score:** 100/100

**Reason:** Directly upscaling latent images is essential for generating large images using tiled VAE decode.

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

**Reason:** Decoding latent images into pixel space images is crucial for the specified workflow goal.

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

**Score:** 81/100

**Reason:** Directly repeats latent batch to generate large images.

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

**Score:** 40/100

**Reason:** Sets a noise mask on input samples but does not directly contribute to generating large images.

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

**Score:** 60/100

**Reason:** Crops the latent space to a specified size which could be useful in conjunction with other nodes to generate large images.

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

**Score:** 81/100

**Reason:** This node can be very useful in rotating latent space samples before decoding them into large images.

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

**Reason:** Loads a diffusion model checkpoint which is essential for generating large images using tiled VAE decode.

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

**Score:** 80/100

**Reason:** Loads a ControlNet model which can be used to guide the generation of large images using tiled VAE decode, but requires additional setup with a loaded model.

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

**Reason:** This node is very useful for the specified workflow goal as it loads a VAE model which is crucial for decoding and generating large images.

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

**Score:** 81/100

**Reason:** This node provides a sampler that can be used to generate large images using tiled VAE decode. It has various options for sampling algorithms and schedulers.

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

**Score:** 41/100

**Reason:** This node is a scheduler that can be used in conjunction with the sampler from Node 1 to control how noise is gradually removed to form the image.

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

**Score:** 100/100

**Reason:** This node provides a KSampler that uses the provided model, positive and negative conditioning to denoise the latent image. It has various options for sampling algorithms and schedulers, making it very useful for generating large images using tiled VAE decode.

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

**Score:** 81/100

**Reason:** This node is an advanced version of the KSampler from Node 3, providing additional features such as noise control and step control, making it essential for generating large images using tiled VAE decode.

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

**Reason:** This node directly generates large images using tiled VAE decode by composing a prompt with LLM.

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

**Reason:** This node provides the necessary configuration for generating large images using tiled VAE decode by setting up an LLM model and parameters.

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

**Score:** 81/100

**Reason:** This node provides a pre-configured LLM configuration which is directly relevant to generating large images using tiled VAE decode.

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

**Score:** 41/100

**Reason:** This node requires an existing LLM configuration as input which may not be directly relevant to generating large images using tiled VAE decode.

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

**Reason:** This node is essential for the workflow goal as it directly provides the input required by the VAE decoder.

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

**Reason:** This node provides a text prompt that can be used in conjunction with a CLIP model to generate large images using tiled VAE decode.

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

**Score:** 95/100

**Reason:** This node combines the functionality of Auto-LLM-Text and Auto-LLM-Vision nodes to provide a more comprehensive solution for generating large images using tiled VAE decode.

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

**Reason:** This node provides an LLM vision component that can be used in conjunction with a CLIP model to generate large images using tiled VAE decode.

### Metadata

---
