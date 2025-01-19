# Filtered Nodes for: Inpainting workflow with mask input

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

**Reason:** Directly applies fuzzy fast intensity to mask input, a crucial step in the inpainting process.

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

**Score:** 99/100

**Reason:** Generates seam masks from input masks, which is essential for guiding the inpainting algorithm.

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

**Score:** 60/100

**Reason:** This node can manipulate and combine masks, which could be useful in certain inpainting scenarios, but its utility depends on the specific requirements of the workflow.

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

**Reason:** This node is essential for the workflow as it allows extending the mask input with a slider.

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

**Score:** 91/100

**Reason:** This node is very useful for the workflow as it expands the mask input and provides fuzzy feathering feature.

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

**Score:** 95/100

**Reason:** This node is extremely useful for the workflow as it blurs white edges in the mask input with various optional parameters.

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

**Score:** 83/100

**Reason:** This node is very useful for the workflow as it blurs the mask edges with fuzzy weight and blur size options.

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

**Reason:** This node directly enhances the mask input by removing black edges, which is essential for a clear inpainting process.

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

**Score:** 41/100

**Reason:** This custom template node can be used to create or modify templates related to inpainting, but its indirect contribution makes it moderately useful at best.

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

**Score:** 50/100

**Reason:** This node offers various style categories that could influence the inpainting process but may not directly contribute to mask input.

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

**Score:** 80/100

**Reason:** This node provides lens-related settings such as perspective and positioning which can be crucial for inpainting workflows with mask input.

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

**Score:** 81/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it allows users to specify various items and their weights, which can be used to generate high-quality images.

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

**Score:** 100/100

**Reason:** This node stitches image cropping data, which is essential for the inpainting workflow with mask input.

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

**Reason:** This node crops image mask areas and generates coordinates, which are crucial for the inpainting workflow with mask input.

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

**Score:** 40/100

**Reason:** This node can be used to swap integer and float inputs but its relevance is marginal for the specified workflow goal.

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

**Reason:** This node has specific features that would help achieve the inpainting workflow with mask input as it performs arithmetic operations on numbers.

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

**Reason:** This node is essential for determining the size of the input image, which may be necessary for subsequent processing steps in the inpainting workflow.

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

**Reason:** This node loads an image from file and can also generate a mask, making it very useful for the specified workflow goal.

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

**Score:** 95/100

**Reason:** This node can adjust the saturation of an image which could be useful in certain inpainting scenarios where color consistency is important.

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

**Reason:** This node can migrate colors from one image to another which could be used as a preprocessing step for inpainting or to create more realistic results.

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

**Score:** 80/100

**Reason:** This node can adjust the hue of an image which could be useful in certain inpainting scenarios where color consistency is important.

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

**Reason:** This node is very useful as it preserves brightness which might be necessary for an accurate inpainting result.

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

**Reason:** This node has some utility as a supporting node for color adjustments in the inpainting workflow, but its direct relevance is moderate.

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

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it redraws encoder pixels using VAE and mask inputs.

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

**Reason:** This node generates art styles that can be used to create inpainted images with a specific aesthetic.

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

**Score:** 80/100

**Reason:** This node can generate emotional prompts that could be useful in an inpainting workflow, especially if the goal is to create artwork related to emotions.

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

**Reason:** This node loads a pre-trained model and its associated components, which is crucial for an inpainting workflow with mask input.

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

**Score:** 40/100

**Reason:** This node generates prompts but does not directly contribute to the inpainting process. It could be useful for supporting tasks like text analysis or generation.

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

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it can be used to add text to an image, which may be necessary in certain inpainting scenarios.

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

**Reason:** Resizes images but doesn"t directly contribute to inpainting with a mask input.

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

**Reason:** Provides image size information which is crucial for inpainting workflows.

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

**Score:** 100/100

**Reason:** Loads images with mask input, making it essential for this specific inpainting workflow.

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

**Score:** 80/100

**Reason:** This node provides a seed value which can be useful for reproducibility in the inpainting workflow.

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

**Reason:** This node provides multiple condition texts but its relevance to the inpainting workflow with mask input is limited.

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

**Reason:** This node converts integer values to strings which can be used for mask input in the inpainting workflow.

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

**Score:** 40/100

**Reason:** This logic node can be used as a supporting node to control the flow of the inpainting workflow based on certain conditions.

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

**Score:** 85/100

**Reason:** Int to Float is very useful for converting integer masks to float values required by the inpainting algorithm.

### Metadata

---

### String Replace (`DF_String_Replace`)

**Description:**

**Module:** `Derfuu_ComfyUI_ModdedNodes`

#### Inputs

- `Text` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`
- `Pattern` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`
- `Replace_With` (required): `STRING`
  - Options: `{{'default': '', 'multiline': False, 'forceInput': False, 'dynamicPrompts': False}}`
- `Mode` (required): `['Strict', 'RegEx']`
  - Options: `{{'forceInput': False}}`

#### Outputs

- `TEXT`: `STRING`

## DERFUU_NODES/MATH


### Applicability

**Score:** 81/100

**Reason:** Directly relevant to modifying mask inputs in the inpainting workflow.

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

**Reason:** Square root node can be useful in calculating distances or other values within the inpainting process.

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

**Reason:** Subtract node may be marginally useful for subtracting a background value from an image, but it is not directly relevant to inpainting with mask input.

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

**Reason:** This node scales the conditioning area based on a ratio which is relevant for adjusting the inpainting process according to the mask input.

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

**Score:** 81/100

**Reason:** This node is very useful for the specified workflow goal as it allows scaling an image to a specific side length while maintaining aspect ratio and supporting various upscale methods.

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

**Reason:** This node is very useful for the specified workflow goal as it allows scaling latent data to a specific side length while maintaining aspect ratio and supporting various scale methods.

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

**Score:** 100/100

**Reason:** This node is essential for the inpainting workflow with mask input as it allows users to input a float value which can be used to fine-tune the inpainting process.

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

**Score:** 80/100

**Reason:** This node is very useful for the inpainting workflow with mask input as it provides an integer output that can be used to control various parameters of the inpainting algorithm.

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

**Reason:** This node is very useful as it allows scheduling of batch prompts and can be used for various tasks including inpainting.

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

**Score:** 85/100

**Reason:** This node is essential for this workflow as it provides a way to schedule batch prompts with specific settings such as width, height, and target dimensions.

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

**Score:** 95/100

**Reason:** This node is essential for this workflow as it allows scheduling of batch prompts with latent input which can be used for inpainting tasks.

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

**Score:** 100/100

**Reason:** This node directly handles batch value schedules which can be used for inpainting workflows with mask inputs by providing a way to schedule values based on frame numbers.

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

**Score:** 100/100

**Reason:** This node directly handles batch value schedules which can be used for inpainting workflows with mask inputs by providing a way to schedule values based on frame numbers and accepting latent inputs.

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

**Reason:** This node is essential for setting up the frame and text inputs for the inpainting workflow.

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

**Reason:** This node can provide an initial setup for the inpainting workflow but is not directly relevant.

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

**Reason:** Concatenates two strings which could be useful for combining mask information or other metadata in the inpainting workflow.

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

**Reason:** Selects images based on schedule and could be useful for organizing or selecting image inputs in the inpainting workflow.

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

**Score:** 100/100

**Reason:** This node is essential for scheduling prompts in an inpainting workflow with mask input.

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

**Reason:** This node is very useful as it allows encoding SDXL inputs for an inpainting workflow with mask input.

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

**Score:** 60/100

**Reason:** This node is moderately useful as it provides a basic prompt schedule for an inpainting workflow with mask input.

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

**Score:** 100/100

**Reason:** This node is essential for ending the prompt schedule in an inpainting workflow with mask input.

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

**Score:** 40/100

**Reason:** Lerp can be used as a supporting node in the inpainting workflow by interpolating between multiple images based on strength and current frame, but its direct relevance is limited.

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

**Reason:** This node generates a sine wave, but it does not have any parameters that would be specifically useful for inpainting with mask input.

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

**Reason:** This node can generate clothing items that match a specific style or theme, which could be useful for creating realistic textures or backgrounds in an inpainting workflow.

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

**Score:** 60/100

**Reason:** This node can generate epochs or time periods, which could be used to create realistic historical or cultural contexts for the inpainting workflow.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it can generate complex and diverse prompts that can be used as input for inpainting models.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it can mix styles and generate new images based on the input mask.

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

**Reason:** This node can be used as a supporting node by generating a collage image that could potentially be used in the inpainting process.

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

**Reason:** This node loads images from a directory and outputs them as an array of images, which is directly useful for an inpainting workflow with mask input.

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

**Reason:** This node is essential for displaying images in the inpainting workflow with mask input.

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

**Reason:** This node generates spacecraft designs which could be useful for creating complex backgrounds or objects in the inpainting workflow.

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

**Reason:** This node generates technology concepts and can be used to create detailed props or effects in the inpainting workflow, making it very useful.

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

**Reason:** Generates an empty latent image with dimensions but does not directly contribute to inpainting with mask input.

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

**Reason:** Provides a list of predefined dimensions for generating latent images which is relevant for the inpainting workflow.

### Metadata

---

### ImageAndMaskPreview (`ImageAndMaskPreview`)

**Description:**


Preview an image or a mask, when both inputs are used  
composites the mask on top of the image.
with pass_through on the preview is disabled and the  
composite is returned from the composite slot instead,  
this allows for the preview to be passed for video combine  
nodes for example.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask_opacity` (required): `FLOAT`
  - Options: `{{'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `mask_color` (required): `STRING`
  - Options: `{{'default': '255, 255, 255'}}`
- `pass_through` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `image` (optional): `IMAGE`
- `mask` (optional): `MASK`

#### Outputs

- `composite`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** Enables previewing an image or mask with optional compositing which can aid in visualizing the inpainting process.

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

**Score:** 81/100

**Reason:** This node is very useful as it can concatenate multiple strings into one, which could be used to create a custom prompt or description for the inpainting task.

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

**Score:** 61/100

**Reason:** This node is moderately useful as it can append tracking data for use with InstanceDiffusion, which could be used in conjunction with an inpainting model.

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

**Reason:** This node is very useful as it draws the tracking data from CreateInstanceDiffusionTracking-node, which is essential for visualizing and understanding the tracking data in the inpainting workflow.

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

**Reason:** This node converts normalized amplitude to a float list, which could be useful as an intermediate step in the inpainting workflow.

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

**Score:** 91/100

**Reason:** This node creates masks based on the normalized amplitude and takes additional parameters for customization, making it very useful for the specified workflow goal.

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

**Reason:** This node offsets masks based on the normalized amplitude, which is directly relevant to the inpainting workflow with mask input.

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

**Score:** 90/100

**Reason:** This node provides a constant boolean value which could be useful in various steps of the inpainting workflow such as conditional checks or loop control.

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

**Score:** 100/100

**Reason:** This node provides a constant string output which can be used as a fixed value in the inpainting workflow.

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

**Score:** 80/100

**Reason:** This node allows for multiline string constants which can be useful for providing long text inputs to the inpainting workflow.

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

**Reason:** This node is very useful for creating a fade mask which can be used in the inpainting workflow with mask input.

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

**Score:** 70/100

**Reason:** This node is moderately useful for perturbing model weights which can be used in the inpainting workflow with mask input, but its direct relevance is lower than other nodes.

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

**Score:** 100/100

**Reason:** This node can be used to quickly preview images in different formats and qualities, making it very useful for evaluating the output of an inpainting model.

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

**Reason:** This node allows for fine-grained control over individual blocks in a diffusion model, making it essential for tasks like inpainting where precise block-level adjustments are necessary.

### Metadata

---

### Image Grab PIL (`ImageGrabPIL`)

**Description:**


Captures an area specified by screen coordinates.  
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
- `num_frames` (required): `INT`
  - Options: `{{'default': 1, 'min': 1, 'max': 255, 'step': 1}}`
- `delay` (required): `FLOAT`
  - Options: `{{'default': 0.1, 'min': 0.0, 'max': 10.0, 'step': 0.01}}`

#### Outputs

- `image`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node can capture an area specified by screen coordinates which could be useful for capturing a mask or other image data in real-time.

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

**Reason:** This node interpolates coordinates based on a curve, which could be useful for manipulating the mask input in the inpainting workflow.

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

**Reason:** This node is essential for patching the model to load weight patches before compiling it, which is crucial for the inpainting workflow with mask input.

### Metadata

---

### Points Editor (`PointsEditor`)

**Description:**


# WORK IN PROGRESS  
Do not count on this as part of your workflow yet,  
probably contains lots of bugs and stability is not  
guaranteed!!  
  
## Graphical editor to create coordinates

**Shift + click** to add a positive (green) point.
**Shift + right click** to add a negative (red) point.
**Ctrl + click** to draw a box.  
**Right click on a point** to delete it.    
Note that you can't delete from start/end of the points array.  
  
To add an image select the node and copy/paste or drag in the image.  
Or from the bg_image input on queue (first frame of the batch).  

**THE IMAGE IS SAVED TO THE NODE AND WORKFLOW METADATA**  
you can clear the image from the context menu by right clicking on the canvas  



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `points_store` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `coordinates` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `neg_coordinates` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `bbox_store` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `bboxes` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `bbox_format` (required): `['xyxy', 'xywh']`
- `width` (required): `INT`
  - Options: `{{'default': 512, 'min': 8, 'max': 4096, 'step': 8}}`
- `height` (required): `INT`
  - Options: `{{'default': 512, 'min': 8, 'max': 4096, 'step': 8}}`
- `normalize` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `bg_image` (optional): `IMAGE`

#### Outputs

- `positive_coords`: `STRING`
- `negative_coords`: `STRING`
- `bbox`: `BBOX`
- `bbox_mask`: `MASK`
- `cropped_image`: `IMAGE`


### Applicability

**Score:** 90/100

**Reason:** This node is very useful for creating and editing coordinates which are essential for the inpainting workflow with mask input.

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

**Reason:** This node is essential for scheduling azimuth and elevation conditions for SV3D in the inpainting workflow.

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

**Score:** 61/100

**Reason:** Although this node can capture an area specified by screen coordinates, it is only moderately useful for the inpainting workflow with mask input.

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

**Reason:** This node is essential for calling the Stability API in the inpainting workflow with mask input.

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

**Reason:** This node directly applies a style model with adjustable strength to the inpainting task.

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

**Reason:** This node compiles model flux advanced but lacks direct relevance and utility for the specified workflow goal.

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

**Reason:** This node captures frames from a webcam using CV2 and can be used in real-time diffusion with autoqueue, making it very useful for this workflow goal.

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

**Score:** 40/100

**Reason:** This node is marginally relevant to the inpainting workflow with mask input as it enables color transfer across images, but its primary use case is not directly related to inpainting.

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

**Reason:** This node creates a gradient image from coordinates and can be used in various image processing tasks, making it very useful for this workflow goal.

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

**Reason:** This node is very useful for the inpainting workflow with mask input as it allows cross-fading between two images based on an interpolation method and transition parameters.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it extends the functionality of CrossFadeImages to handle multiple images in a batch.

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

**Reason:** Gets image size and count but doesn"t directly contribute to inpainting with mask input.

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

**Reason:** Directly retrieves images from batch indexed by their positions, which is useful for handling multiple images in the inpainting workflow.

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

**Reason:** Essential for creating a batch of images from multiple inputs, which is necessary for inpainting workflows.

### Metadata

---

### Image Concatenate (`ImageConcanate`)

**Description:**


Concatenates the image2 to image1 in the specified direction.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `image1` (required): `IMAGE`
- `image2` (required): `IMAGE`
- `direction` (required): `['right', 'down', 'left', 'up']`
  - Options: `{{'default': 'right'}}`
- `match_image_size` (required): `BOOLEAN`
  - Options: `{{'default': True}}`

#### Outputs

- `IMAGE`: `IMAGE`


### Applicability

**Score:** 61/100

**Reason:** Moderately useful for repeating each image in the batch by a specified number of times, but may not be directly applicable to all inpainting tasks.

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

**Score:** 41/100

**Reason:** Marginally relevant for concatenating images from a batch into a grid, which could potentially be used as part of an inpainting workflow, but is not directly related to the goal.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it crops and resizes an image based on a provided mask.

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

**Score:** 41/100

**Reason:** This node is moderately useful because it can convert a grid of images to a batch, but its direct relevance to inpainting with mask input is limited.

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

**Score:** 81/100

**Reason:** This node is essential for this workflow as it normalizes the images to be in the range [-1, 1], which is often required for deep learning-based inpainting models.

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

**Reason:** This node is very useful as it can resize the input images to a specified width and height, which may be necessary for certain inpainting models or applications.

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

**Reason:** Directly relevant to inpainting workflow with mask input by uncropping images based on provided masks.

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

**Score:** 40/100

**Reason:** Marginally useful as it can upscale images but is not directly related to the inpainting workflow goal.

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

**Reason:** Moderately useful as it can insert images into a batch at specified indices, but may require additional processing steps.

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

**Reason:** This node is essential for preparing the input image and mask for the inpainting workflow by loading and resizing the image.

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

**Reason:** This node can be moderately useful as a supporting node to merge different channels of an image, but it may not directly contribute to the inpainting process.

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

**Reason:** This node can be very useful as a supporting node to remap image values, which could be necessary for preparing the input image or mask for the inpainting process.

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

**Reason:** This node is essential for replacing images in a batch as part of the inpainting workflow with mask input.

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

**Score:** 41/100

**Reason:** This node has moderate utility as it can reverse the order of images in a batch but does not directly contribute to the inpainting process.

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

**Reason:** This node is moderately useful for saving images to the output directory after processing them in the inpainting workflow.

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

**Score:** 91/100

**Reason:** This node is very useful as it saves an image and its corresponding mask as a .PNG file with the mask as the alpha channel, which is crucial for the inpainting process.

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

**Reason:** Directly splits image into channels which can be used as input for inpainting workflow.

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

**Score:** 100/100

**Reason:** Directly segments images using CLIPSeg with mask input, aligning perfectly with the workflow goal.

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

**Reason:** Crops original images from masks, supporting the inpainting workflow by preparing image regions for processing.

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

**Reason:** Advanced version of cropping, providing additional outputs such as combined crop images and masks, making it very useful for the workflow.

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

**Reason:** Uncrops cropped images back to their original size with border blending, supporting the inpainting workflow by restoring image regions after processing.

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

**Score:** 81/100

**Reason:** This node is essential for uncropping images in the inpainting workflow with mask input.

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

**Score:** 91/100

**Reason:** This node is very useful for converting bounding box indices to integer coordinates, which can be used as inputs or outputs in other nodes.

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

**Score:** 61/100

**Reason:** This node is moderately useful for converting RGB values to masks, which can be used as inputs in other nodes, such as the Batch Uncrop Advanced node.

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

**Reason:** Essential for loading CLIPSeg model which is necessary for inpainting.

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

**Score:** 95/100

**Reason:** Very useful for filtering out empty masks and corresponding images, a crucial step in inpainting.

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

**Score:** 85/100

**Reason:** Very useful for getting mask size and count information which can be used to configure other nodes.

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

**Score:** 60/100

**Reason:** Moderately useful for growing the mask with blur, but its relevance depends on the specific requirements of the inpainting workflow.

### Metadata

---

### Mask Batch Multi (`MaskBatchMulti`)

**Description:**


Creates an image batch from multiple masks.  
You can set how many inputs the node has,  
with the **inputcount** and clicking update.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `inputcount` (required): `INT`
  - Options: `{{'default': 2, 'min': 2, 'max': 1000, 'step': 1}}`
- `mask_1` (required): `MASK`
- `mask_2` (required): `MASK`

#### Outputs

- `masks`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** This node is essential for creating a batch of masks from multiple input masks, which is a crucial step in the inpainting workflow.

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

**Score:** 100/100

**Reason:** This node is directly relevant to the workflow goal as it allows offsetting and manipulating the mask, which is necessary for accurate inpainting results.

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

**Reason:** This node is moderately useful as it allows remapping the range of the mask values, but its impact on the overall inpainting process may be limited compared to other nodes.

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

**Score:** 100/100

**Reason:** This node is essential for resizing the mask or batch of masks to a specific width and height, which is often necessary for accurate inpainting results.

### Metadata

---

### Round Mask (`RoundMask`)

**Description:**


Rounds the mask or batch of masks to a binary mask.  
<img src="https://github.com/kijai/ComfyUI-KJNodes/assets/40791699/52c85202-f74e-4b96-9dac-c8bda5ddcc40" width="300" height="250" alt="RoundMask example">



**Module:** `ComfyUI-KJNodes`

#### Inputs

- `mask` (required): `MASK`

#### Outputs

- `MASK`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** Essential for this workflow as it rounds the mask to a binary mask, which is necessary for inpainting.

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

**Score:** 40/100

**Reason:** Marginally relevant as it splits bbox lists but does not directly contribute to the inpainting process.

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

**Reason:** This node bundles multiple conditioning mask and combine nodes into one, making it essential for simplifying the inpainting workflow with a mask input.

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

**Score:** 70/100

**Reason:** Similar to Node 1, this node also bundles multiple conditioning mask and combine nodes but has an additional set of inputs, making it moderately useful for more complex workflows.

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

**Score:** 60/100

**Reason:** This node bundles even more conditioning mask and combine nodes than the previous ones, making it moderately useful for very complex inpainting workflows with multiple masks.

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

**Score:** 90/100

**Reason:** This node creates a batch of masks interpolated between given frames and values, making it essential for creating custom fade masks in the inpainting workflow.

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

**Reason:** This node is essential for creating a fluid mask, which can be used as input for inpainting. It provides various parameters to customize the mask.

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

**Score:** 61/100

**Reason:** This node is moderately useful for creating a gradient mask, but it lacks some features compared to other nodes like Create Fluid Mask or Create Magic Mask.

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

**Score:** 41/100

**Reason:** This node is marginally relevant as it creates a magic mask, but its parameters might not be directly applicable to the inpainting workflow with mask input.

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

**Reason:** This node is essential for creating a shape mask, which can be used as input for inpainting. It provides various parameters to customize the mask and create animated masks.

### Metadata

---

### Create Shape Mask On Path (`CreateShapeMaskOnPath`)

**Description:**


Creates a mask or batch of masks with the specified shape.  
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
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 1}}`
- `shape_height` (required): `INT`
  - Options: `{{'default': 128, 'min': 8, 'max': 4096, 'step': 1}}`
- `size_multiplier` (optional): `FLOAT`
  - Options: `{{'default': [1.0], 'forceInput': True}}`

#### Outputs

- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 81/100

**Reason:** Creates a mask or batch of masks with the specified shape, directly relevant to the inpainting workflow.

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

**Score:** 91/100

**Reason:** Creates a mask or batch of masks with the specified text, directly relevant and useful for the inpainting workflow.

### Metadata

---

### Create Voronoi Mask (`CreateVoronoiMask`)

**Description:**

**Module:** `ComfyUI-KJNodes`

#### Inputs

- `frames` (required): `INT`
  - Options: `{{'default': 16, 'min': 2, 'max': 4096, 'step': 1}}`
- `num_points` (required): `INT`
  - Options: `{{'default': 15, 'min': 1, 'max': 4096, 'step': 1}}`
- `line_width` (required): `INT`
  - Options: `{{'default': 4, 'min': 1, 'max': 4096, 'step': 1}}`
- `speed` (required): `FLOAT`
  - Options: `{{'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}}`
- `frame_width` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`
- `frame_height` (required): `INT`
  - Options: `{{'default': 512, 'min': 16, 'max': 4096, 'step': 1}}`

#### Outputs

- `mask`: `MASK`
- `mask_inverted`: `MASK`


### Applicability

**Score:** 41/100

**Reason:** Generates a Voronoi pattern which could be used as a mask in the inpainting workflow, but its relevance is limited to specific use cases.

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

**Score:** 61/100

**Reason:** Converts float values into masks, moderately useful for the inpainting workflow when working with numerical data.

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

**Reason:** This node can be moderately useful in passing through positive and negative conditioning for the inpainting workflow.

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

**Reason:** This node creates a sigmas tensor from a string of comma-separated values, which is essential for configuring noise schedules in the inpainting workflow.

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

**Reason:** This node adjusts sigmas based on user input, which can be useful for fine-tuning noise schedules in the inpainting workflow. However, it may not be as critical as creating a sigmas tensor from scratch.

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

**Reason:** This node can convert sigmas to float values but does not directly contribute to the inpainting process.

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

**Reason:** This node injects noise into latents which is a crucial step in the inpainting process.

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

**Score:** 61/100

**Reason:** This node can convert sigmas tensors to float values which might be useful for certain inpainting techniques.

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

**Reason:** This node is essential for the Inpainting workflow with mask input as it creates a text mask that can be used for inpainting.

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

**Reason:** This node is essential for generating detailed prompts that can be used as input for text-to-image models in the inpainting workflow.

### Metadata

---

### Widget To String (`WidgetToString`)

**Description:**


Selects a node and it's specified widget and outputs the value as a string.  
If no node id or title is provided it will use the 'any_input' link and use that node.  
To see node id's, enable node id display from Manager badge menu.  
Alternatively you can search with the node title. Node titles ONLY exist if they  
are manually edited!  
The 'any_input' is required for making sure the node you want the value from exists in the workflow.


**Module:** `ComfyUI-KJNodes`

#### Inputs

- `id` (required): `INT`
  - Options: `{{'default': 0}}`
- `widget_name` (required): `STRING`
  - Options: `{{'multiline': False}}`
- `return_all` (required): `BOOLEAN`
  - Options: `{{'default': False}}`
- `any_input` (optional): `*`
- `node_title` (optional): `STRING`
  - Options: `{{'multiline': False}}`

#### Outputs

- `STRING`: `STRING`

## KJNODES/WEIGHTS


### Applicability

**Score:** 61/100

**Reason:** This node is moderately useful for extracting values from nodes and widgets in the workflow, but may require additional setup to achieve the desired outcome.

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

**Reason:** This node is marginally relevant as it can be used to process mask or image batches, but its output type may not directly contribute to the inpainting workflow goal.

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

**Score:** 90/100

**Reason:** This node uses LLMs for image understanding and can provide detailed descriptions of images, which could be useful in an inpainting workflow with mask input.

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

**Reason:** This compare node can be used to validate or adjust the mask input, making it moderately useful for the specified workflow goal.

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

**Score:** 60/100

**Reason:** This float node can be used to adjust or validate numerical values in the inpainting process, making it moderately useful for the specified workflow goal.

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

**Reason:** This node is essential for converting other data types into integers in the inpainting workflow.

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

**Reason:** This node is very useful for handling string inputs and outputs in the inpainting workflow.

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

**Reason:** Moderately useful as a supporting node to adjust conditioning multiplier for inpainting.

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

**Reason:** Essential for normalizing conditioning input in the inpainting workflow.

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

**Reason:** Essential for resizing and preparing the image input for inpainting.

### Metadata

---

### Log (FLOAT) (`LogFloat`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `FLOAT`
  - Options: `{{'forceInput': True}}`
- `prefix` (optional): `STRING`
  - Options: `{{'multiline': True, 'default': 'Value:'}}`

#### Outputs

- `FLOAT`: `FLOAT`


### Applicability

**Score:** 81/100

**Reason:** Essential for logging float values during the inpainting process

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

**Score:** 81/100

**Reason:** Essential for logging integer values during the inpainting process

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

**Reason:** This node could be useful for supporting the inpainting workflow by allowing access to specific lines in a text input, but its relevance is marginal.

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

**Reason:** This node is very useful for converting float values from masks to strings in the inpainting workflow.

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

**Score:** 90/100

**Reason:** This node is essential for converting integer values from masks to strings in the inpainting workflow.

### Metadata

---

### To string (NUMBER) (`RF_NumberToString`)

**Description:**

**Module:** `comfyui-rf-nodes`

#### Inputs

- `value` (required): `NUMBER`
  - Options: `{{'forceInput': True}}`

#### Outputs

- `STRING`: `STRING`


### Applicability

**Score:** 80/100

**Reason:** This node can convert a number to string which might be useful in processing or displaying mask data.

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

**Reason:** This node allows selecting one of multiple options based on an index but its relevance is not clear without more context.

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

**Score:** 80/100

**Reason:** This node can be used to repeat a process multiple times, which could be useful for iterative inpainting tasks.

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

**Reason:** Directly accepts a string value as input which can be used for inpainting with mask input.

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

**Reason:** Replaces text within a given template which can be useful in modifying the inpainted mask or image.

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

**Reason:** This node is very useful as it can convert a VEC2 value into a string format, which could be used in the inpainting workflow with mask input.

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

**Score:** 90/100

**Reason:** This node is essential for this workflow as it can convert a VEC3 value into a string format, which could be used in the inpainting workflow with mask input.

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

**Reason:** Essential for this workflow as it provides advanced options configuration which is crucial for fine-tuning LLMs.

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

**Reason:** Essential for this workflow as it generates the final inpainting result based on the mask input and other parameters.

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

**Score:** 91/100

**Reason:** Very useful for this workflow as it performs differential diffusion which is a key step in inpainting with mask input.

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

**Score:** 81/100

**Reason:** This node blends two latent samples based on a given factor, which is directly relevant to inpainting with mask input.

### Metadata

---

### LoadLatent (`LoadLatent`)

**Description:**

#### Inputs

- `latent` (required): `[[]]`

#### Outputs

- `LATENT`: `LATENT`


### Applicability

**Score:** 41/100

**Reason:** This node loads pre-computed latent values but does not contribute directly to the inpainting process. It can be useful as a supporting node for loading existing latents.

### Metadata

---

### SaveLatent (`SaveLatent`)

**Description:**

#### Inputs

- `samples` (required): `LATENT`
- `filename_prefix` (required): `STRING`
  - Options: `{{'default': 'latents/ComfyUI'}}`


### Applicability

**Score:** 61/100

**Reason:** This node saves computed latent samples, which is moderately relevant to the workflow goal of inpainting with mask input.

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

**Reason:** This node is essential for encoding input images into a latent space that can be used in inpainting workflows.

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

**Score:** 40/100

**Reason:** This node has some indirect relevance to the inpainting workflow as it can load a CLIP model that could be used for image manipulation tasks.

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

**Reason:** This node loads dual CLIP models which are essential for the inpainting workflow with mask input.

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

**Score:** 90/100

**Reason:** This node loads a diffusion model which is necessary for the inpainting workflow with mask input.

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

**Reason:** This node can encode text into a conditioning that guides the diffusion model towards generating specific images, which is useful for an inpainting workflow.

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

**Reason:** This node allows selecting a specific layer from a CLIP model to use as input for the inpainting workflow.

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

**Reason:** This node encodes a text prompt into a conditioning that can be used to guide the diffusion model towards generating specific images, which is essential for an inpainting workflow with mask input.

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

**Reason:** This node is essential for encoding the input image into CLIP Vision space.

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

**Score:** 90/100

**Reason:** This node is very useful for adjusting the strength of one conditioning over another in the inpainting workflow, allowing for more control and flexibility.

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

**Score:** 80/100

**Reason:** This node is essential for combining multiple conditionings in the inpainting workflow, enabling the creation of complex and nuanced results.

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

**Reason:** This node is marginally relevant to the inpainting workflow with mask input. It seems to be a general conditioning concatenation step that might not directly contribute to the specific goal.

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

**Reason:** This node directly sets the area to be inpainted based on user input, which is essential for the Inpainting workflow with mask input.

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

**Reason:** This node allows setting the area to be inpainted as a percentage of the image size, providing flexibility in the Inpainting workflow with mask input.

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

**Score:** 41/100

**Reason:** This node allows setting a custom mask for inpainting but requires additional parameters like set_cond_area, which may be useful in specific scenarios, but is moderately useful overall for the Inpainting workflow with mask input.

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

**Reason:** Essential for this workflow as it prepares the conditioning input for ControlNet.

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

**Score:** 61/100

**Reason:** Moderately useful as it applies the ControlNet to the image but with limited control over the process.

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

**Score:** 41/100

**Reason:** Marginally relevant as it provides advanced features for applying ControlNet but may not be necessary for this workflow.

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

**Score:** 81/100

**Reason:** This node is essential for the inpainting workflow as it conditions the model based on the provided mask and image inputs.

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

**Reason:** This node can be moderately useful in the inpainting workflow by applying a style model to the input image.

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

**Score:** 80/100

**Reason:** This node is very useful for loading multiple images in batches which can be used as inputs for further processing steps in the inpainting workflow.

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

**Reason:** This node is moderately useful as it can invert an image but does not directly contribute to the inpainting process with a mask input.

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

**Score:** 90/100

**Reason:** This node is essential for the inpainting workflow with mask input as it pads the image according to user-defined parameters which is crucial for outpainting and other related tasks.

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

**Reason:** Directly relevant to inpainting with mask input. Provides necessary image padding.

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

**Score:** 61/100

**Reason:** Supports inpainting by allowing target size adjustment, but requires additional nodes for actual inpainting.

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

**Reason:** Essential for the inpainting workflow as it loads the input image necessary for subsequent processing steps.

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

**Reason:** This node is essential for loading images from a folder which is a crucial step in the inpainting workflow.

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

**Score:** 80/100

**Reason:** This node is very useful for upscaling images which may be necessary in the inpainting workflow, especially when working with low-resolution input images.

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

**Reason:** Essential for this workflow as it upscaling the input image which is a crucial step in inpainting.

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

**Reason:** This node is essential for creating empty latent images that will be denoised via sampling, a key component of the inpainting workflow.

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

**Score:** 61/100

**Reason:** Moderately useful for upscaling latent images which can be used in the inpainting process, but its utility is lower than other nodes like EmptyLatentImage.

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

**Reason:** Essential for upscaling latent images before inpainting.

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

**Reason:** Decodes latent images into pixel space, which is necessary for inpainting with a mask input.

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

**Reason:** This node is essential for setting a noise mask in the inpainting workflow with mask input.

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

**Reason:** This node is moderately useful as it encodes images into latent space but requires additional processing steps for inpainting.

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

**Reason:** This node is moderately useful as it can crop latent samples but does not directly contribute to the inpainting process with mask input.

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

**Score:** 80/100

**Reason:** This node can be very useful in adjusting the latent space of the input mask for better inpainting results.

### Metadata

---

### Load CLIP Vision (`CLIPVisionLoader`)

**Description:**

#### Inputs

- `clip_name` (required): `[]`

#### Outputs

- `CLIP_VISION`: `CLIP_VISION`


### Applicability

**Score:** 40/100

**Reason:** This node is marginally relevant as it loads CLIP Vision models, but they might not be directly applicable for inpainting workflows.

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

**Reason:** This node is essential for loading a ControlNet model which can be used in conjunction with a mask input for inpainting.

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

**Reason:** This node has some utility as it loads a ControlNet model but requires an existing model to load from, making it less directly relevant than the Load ControlNet Model node.

### Metadata

---

### Load VAE (`VAELoader`)

**Description:**

#### Inputs

- `vae_name` (required): `['hunyuan_video_vae_bf16.safetensors']`

#### Outputs

- `VAE`: `VAE`


### Applicability

**Score:** 81/100

**Reason:** This node is very useful as it loads a VAE which can be used for inpainting tasks.

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

**Score:** 100/100

**Reason:** This node is essential for this workflow as it loads the unCLIP checkpoint that contains the necessary models and CLIP for inpainting with mask input.

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

**Reason:** This node is essential for this workflow as it loads an image as a mask which can be used directly in the inpainting task.

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

**Score:** 90/100

**Reason:** Very useful because it can handle string inputs which are often used to represent masks in inpainting workflows.

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

**Score:** 61/100

**Reason:** This node can be used to select a sampler algorithm for the inpainting workflow, but it does not directly contribute to the mask input processing.

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

**Score:** 81/100

**Reason:** This node is essential for scheduling the sampling process in the inpainting workflow and selecting a suitable scheduler algorithm.

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

**Reason:** This node is crucial for denoising the latent image using a KSampler algorithm, which is directly relevant to the inpainting workflow with mask input.

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

**Score:** 90/100

**Reason:** This advanced version of the KSampler node provides additional features such as noise control and step customization, making it highly useful for the inpainting workflow with mask input.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it loads the required API key for the Tara LLM model.

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

**Reason:** This node is essential for the inpainting workflow with mask input as it configures the required settings for the Tara LLM model.

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

**Reason:** This node provides a pre-configured LLM configuration which is directly relevant to the inpainting workflow with mask input.

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

**Reason:** Although this node can be used in the inpainting workflow with mask input, it requires additional nodes to generate the necessary inputs (guidance, prompt_positive, prompt_negative).

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

**Reason:** This node is essential for generating images in the inpainting workflow with mask input.

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

**Reason:** This node is essential for encoding images into latent space and preparing them for inpainting.

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

**Reason:** This node provides a comprehensive text generation functionality that can be used to generate prompts for the inpainting workflow.

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

**Reason:** This node combines text and vision capabilities to provide a more comprehensive AI-powered inpainting solution.

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

**Reason:** This node provides a vision-only AI-powered inpainting functionality that can be used in conjunction with the mask input for the workflow.

### Metadata

---
