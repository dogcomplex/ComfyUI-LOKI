import { app } from "../../scripts/app.js";
import { $el } from "../../scripts/ui.js";

// Track all glamours
let allGlamours = new Set();
let isGlamourActive = true;

// Track glamours per node
let glamourStates = new Map(); // node.id -> boolean
let isGlobalGlamourActive = false; // Start with Unveil by default

function updateGlobalControl() {
    const control = document.querySelector('.global-glamour-toggle');
    if (!control) return;
    
    // Check if ANY glamour is active
    const hasActiveGlamour = Array.from(glamourStates.values()).some(state => state);
    const textSpan = control.querySelector('.global-glamour-text');
    textSpan.textContent = hasActiveGlamour ? "🧿 Unveil" : "🦊 Glamour";
}

function createGlobalControl() {
    const control = $el("div", {
        innerHTML: `
            <button class="global-glamour-toggle" style="
                position: fixed;
                left: 20px;
                bottom: 70px;
                z-index: 9999;
                background: rgba(0,0,0,0.7);
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 12px;
                cursor: pointer;
                font-size: 14px;
                display: flex;
                align-items: center;
                gap: 5px;
                transition: background 0.3s ease;
            ">
                <span class="global-glamour-text">🦊 Glamour</span>
            </button>
        `,
        onclick: (e) => {
            if (e.target.closest('.global-glamour-toggle')) {
                const hasActiveGlamour = Array.from(glamourStates.values()).some(state => state);
                
                // Toggle all glamours off if any are active, otherwise turn all on
                allGlamours.forEach(widget => {
                    glamourStates.set(widget.parent.id, !hasActiveGlamour);
                });
                
                updateGlobalControl();
                app.graph.setDirtyCanvas(true);
            }
        }
    });
    
    document.body.appendChild(control);
    updateGlobalControl();
}

function snakeCase(str) {
    return str.toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/[-\s]+/g, '_');
}

function generateNodeHash(node) {
    const stableValues = {
        type: node.type,
        inputs: {},
        widgets: {},
        connections: {}
    };

    // Add ALL input values and connections
    if (node.inputs) {
        for (const [key, input] of Object.entries(node.inputs)) {
            // Store the input value if it exists
            if (input.value !== undefined) {
                stableValues.inputs[key] = input.value;
            }
            
            // Store connection information
            if (input.link != null) {
                const linkedNode = node.graph._nodes.find(n => 
                    n.outputs && n.outputs.some(o => o.links && o.links.includes(input.link))
                );
                if (linkedNode) {
                    stableValues.connections[key] = {
                        nodeType: linkedNode.type,
                        nodeId: linkedNode.id,
                        linkId: input.link
                    };
                }
            }
        }
    }

    // Add ALL widget values (except glamour widgets)
    if (node.widgets) {
        node.widgets.forEach(widget => {
            // Skip glamour widgets
            if (widget.type === "glamour") return;
            
            // Store widget value and type
            stableValues.widgets[widget.name] = {
                type: widget.type,
                value: widget.value,
                // For combo widgets, store options too
                options: widget.options,
                // For number widgets, store min/max
                min: widget.min,
                max: widget.max
            };
        });
    }

    // Create deterministic string with stable sorting
    const contentStr = JSON.stringify(stableValues, (key, value) => {
        if (value && typeof value === 'object') {
            // Sort object keys
            return Object.keys(value).sort().reduce((sorted, key) => {
                if (value[key] !== undefined && value[key] !== null) {
                    sorted[key] = value[key];
                }
                return sorted;
            }, {});
        }
        return value;
    });
    
    // Debug log to see what's being hashed
    // console.log('Hashing content for node:', node.type, contentStr);
    
    // Use a more robust hashing algorithm
    let hash = 0;
    for (let i = 0; i < contentStr.length; i++) {
        const char = contentStr.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash; // Convert to 32-bit integer
    }
    
    const finalHash = Math.abs(hash).toString(16).padStart(8, '0');
    // console.log('Generated hash:', finalHash);
    
    return finalHash;
}

function createGlamourOverlay(node, inputName, inputData, app) {
    // Skip if node already has a glamour
    if (node.widgets?.find(w => w.type === "glamour")) return;
    
    // Set initial state - only true for Glamour node
    const isGlamourNode = node.type === "Glamour 🦊";
    glamourStates.set(node.id, isGlamourNode);
    
    // Update global control to reflect new state
    updateGlobalControl();
    
    const headerHeight = LiteGraph.NODE_TITLE_HEIGHT;
    
    const createNodeContent = () => {
        const nodeTypeSnake = snakeCase(node.type);
        const nodeHash = generateNodeHash(node);
        
        let content = `
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <h3 style="margin: 0; color: #333;">✨ ${node.type} ✨</h3>
                    <div class="node-hash" style="
                        font-size: 0.8em;
                        color: #666;
                        margin-top: 4px;
                        font-family: monospace;
                        word-break: break-all;
                    ">${nodeTypeSnake}_${node.id}_${nodeHash}</div>
                </div>
                <button class="glamour-toggle" style="
                    background: none;
                    border: none;
                    cursor: pointer;
                    font-size: 1.2em;
                    padding: 5px;
                    color: #666;
                ">❌</button>
            </div>`;
        
        // Add widget values section (removed Glamour node check)
        const widgets = node.widgets || [];
        if (widgets.length) {
            content += '<div class="section"><h4>🎛️ Values</h4>';
            widgets.forEach(widget => {
                if (widget.type === "button" || widget.type === "glamour") return;
                content += `
                    <div class="widget-input">
                        <label>🔹 ${widget.name}: </label>
                        <input type="text" 
                            class="glamour-input" 
                            data-widget="${widget.name}"
                            value="${widget.value || ''}"
                            style="
                                background: rgba(255,255,255,0.9);
                                border: 1px solid #ccc;
                                border-radius: 4px;
                                padding: 2px 5px;
                                margin-left: 5px;
                            "
                        />
                    </div>`;
            });
            content += '</div>';
        }
        
        return content;
    };

    // Function to update hash display
    const updateHashDisplay = (overlay) => {
        const hashDisplay = overlay.querySelector('.node-hash');
        if (hashDisplay) {
            const nodeTypeSnake = snakeCase(node.type);
            const newHash = generateNodeHash(node);
            hashDisplay.textContent = `${nodeTypeSnake}_${node.id}_${newHash}`;
        }
    };

    // Function to update input field value
    const updateInputField = (widgetName, value) => {
        const input = overlay.querySelector(`input[data-widget="${widgetName}"]`);
        if (input && input.value !== value) {
            input.value = value;
            // Update hash after input field changes
            updateHashDisplay(overlay);
        }
    };

    // Function to update widget value
    const updateWidgetValue = (widgetName, value) => {
        const widget = node.widgets.find(w => w.name === widgetName);
        if (widget && widget.value !== value) {
            widget.value = value;
            if (widget.callback) {
                widget.callback(value);
            }
            // Update hash after widget value changes
            updateHashDisplay(overlay);
        }
    };

    const widget = {
        type: "glamour",
        name: `w${inputName}`,
        
        draw: function(ctx, node, widgetWidth, y, widgetHeight) {
            // Get state for this node
            const isActive = glamourStates.get(node.id) ?? true; // default to true
            const visible = app.canvas.ds.scale > 0.5 && isActive;
            
            // Draw the paw emoji without affecting layout
            if (!isActive) {
                ctx.save();
                ctx.font = "16px Arial";
                ctx.fillStyle = "#666";
                
                // Position in bottom-right with padding
                const x = node.size[0] - 30;
                const y = node.size[1] - 25;
                
                this.pawRegion = [x, y, 20, 20];
                ctx.fillText("🐾", x, y + 15);
                ctx.restore();
            }
            
            // Update overlay visibility and position
            if (this.overlay) {
                const clientRectBound = ctx.canvas.getBoundingClientRect();
                const transform = new DOMMatrix()
                    .scaleSelf(
                        clientRectBound.width / ctx.canvas.width,
                        clientRectBound.height / ctx.canvas.height
                    )
                    .multiplySelf(ctx.getTransform());
                
                const nodeWidth = node.size[0] * transform.a;
                const fullHeight = (node.size[1] + headerHeight) * transform.d;
                
                // Calculate the relative scale based on base node size
                const baseNodeWidth = 400; // approximate base width of a node
                const relativeScale = (nodeWidth / transform.a) / baseNodeWidth;
                
                Object.assign(this.overlay.style, {
                    left: `${transform.e + clientRectBound.left}px`,
                    top: `${transform.f + clientRectBound.top - headerHeight * transform.d}px`,
                    width: `${nodeWidth}px`,
                    height: `${fullHeight}px`,
                    minHeight: `${fullHeight}px`,
                    position: "absolute",
                    zIndex: app.graph._nodes.indexOf(node),
                    display: visible ? "block" : "none",
                    overflow: "hidden"
                });

                // Scale content relative to node size
                const innerContent = this.overlay.firstElementChild;
                if (innerContent) {
                    Object.assign(innerContent.style, {
                        width: "100%",
                        height: "100%",
                        maxHeight: "100%",
                        overflowY: "auto",
                        overflowX: "hidden",
                        display: "flex",
                        flexDirection: "column",
                        boxSizing: "border-box",
                        padding: "10px",
                        fontSize: `${12 * relativeScale}px`  // Scale font with node size
                    });

                    // Scale all child elements proportionally
                    Array.from(innerContent.children).forEach(child => {
                        Object.assign(child.style, {
                            transform: "none",
                            fontSize: "inherit",
                            padding: `${5 * relativeScale}px`,
                            margin: `${5 * relativeScale}px`
                        });
                    });
                }
            }
        },
        
        computeSize: function() {
            return [0, 0];
        },
        
        onRemoved: function() {
            // ... existing removal code ...
        },
        
        // New click handler
        onMouseDown: function(e, local_pos, global_pos, graphCanvas) {
            if (!glamourStates.get(this.parent.id) && this.pawRegion) {
                const [x, y, w, h] = this.pawRegion;
                if (local_pos[0] > x && local_pos[0] < x + w &&
                    local_pos[1] > y && local_pos[1] < y + h) {
                    glamourStates.set(this.parent.id, true);
                    updateGlobalControl();
                    app.graph.setDirtyCanvas(true);
                    return true;
                }
            }
            return false;
        }
    };

    // Create the overlay with enhanced event handling
    const overlay = $el("div.glamour-overlay", {
        innerHTML: `
            <div class="glamour-content" style="
                position: relative;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                box-sizing: border-box;
                height: 100%;
            ">
                <div class="glamour-image" style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border-radius: 10px;
                    z-index: 0;
                    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d);
                    background-size: 400% 400%;
                    animation: gradientBG 15s ease infinite;
                "></div>
                <div style="
                    position: relative;
                    background: rgba(255,255,255,0.85);
                    padding: 15px;
                    border-radius: 8px;
                    text-align: left;
                    box-sizing: border-box;
                    z-index: 1;
                ">
                    ${createNodeContent()}
                </div>
            </div>
        `,
        onclick: (e) => {
            if (e.target.classList.contains('glamour-toggle')) {
                glamourStates.set(node.id, false);
                updateGlobalControl();
                app.graph.setDirtyCanvas(true);
            }
        },
        onchange: (e) => {
            if (e.target.classList.contains('glamour-input')) {
                const widgetName = e.target.dataset.widget;
                const value = e.target.value;
                
                // Update widget value when input changes
                updateWidgetValue(widgetName, value);
                
                // Update canvas
                app.graph.setDirtyCanvas(true);
            }
        }
    });

    // Make sure to set the data-node-id attribute
    overlay.setAttribute('data-node-id', node.id);

    // Add observer for widget value changes in parent node
    const originalSetValue = node.setPropertyValue;
    if (originalSetValue) {
        node.setPropertyValue = function(name, value) {
            const result = originalSetValue.call(this, name, value);
            
            // Update input field when widget changes
            updateInputField(name, value);
            
            // Update canvas
            app.graph.setDirtyCanvas(true);
            return result;
        };
    }

    // Add observer for widget value changes directly
    node.widgets.forEach(widget => {
        if (widget.type !== "glamour") {
            const originalCallback = widget.callback;
            widget.callback = function(value) {
                if (originalCallback) {
                    originalCallback.call(this, value);
                }
                
                // Update input field when widget changes
                updateInputField(widget.name, value);
                
                // Update canvas
                app.graph.setDirtyCanvas(true);
            };
        }
    });

    // Add observer for input value changes
    const originalOnInputChanged = node.onInputChanged;
    node.onInputChanged = function() {
        if (originalOnInputChanged) {
            originalOnInputChanged.apply(this, arguments);
        }
        // Update hash when inputs change
        updateHashDisplay(overlay);
        app.graph.setDirtyCanvas(true);
    };

    // Initial sync of values and hash
    node.widgets.forEach(widget => {
        if (widget.type !== "glamour") {
            updateInputField(widget.name, widget.value);
        }
    });
    updateHashDisplay(overlay);

    widget.overlay = overlay;
    widget.parent = node;
    allGlamours.add(widget);
    document.body.appendChild(overlay);

    // Add widget to node
    node.addCustomWidget(widget);

    // Override node's default widget handling
    const originalGetNodeMenuOptions = node.getMenuOptions;
    node.getMenuOptions = function(graphCanvas) {
        const options = originalGetNodeMenuOptions ? originalGetNodeMenuOptions.call(this, graphCanvas) : [];
        return options;
    };

    // Make sure widget gets mouse events
    node.onMouseDown = function(e, local_pos, global_pos, graphCanvas) {
        for (let w of this.widgets || []) {
            if (w.type === "glamour" && w.onMouseDown) {
                if (w.onMouseDown(e, local_pos, global_pos, graphCanvas)) {
                    return true;
                }
            }
        }
        return false;
    };

    // Add image loading capability to the node
    const originalDrawBackground = node.onDrawBackground;
    node.onDrawBackground = function(ctx) {
        if (originalDrawBackground) {
            originalDrawBackground.apply(this, arguments);
        }

        // Only attempt to draw if glamour is active for this node
        if (glamourStates.get(this.id)) {
            loadGlamourImage(this, ctx);
        }
    };

    return widget;
}

function getGlamourImageUrl(image_id, node_type) {
    console.log('Attempting to load glamour image:', {
        image_id,
        node_type
    });
    
    // Try specific image first
    const specificUrl = `/view?filename=${encodeURIComponent(image_id)}.png&type=output&subfolder=Glamour`;
    console.log('Trying specific URL:', specificUrl);
    
    // Also prepare fallback URLs using the same pattern
    const nodeIdUrl = `/view?filename=${encodeURIComponent(image_id.split('_').slice(0, 2).join('_'))}.png&type=output&subfolder=Glamour`;
    const fallbackUrl = `/view?filename=${encodeURIComponent(snakeCase(node_type))}.png&type=output&subfolder=Glamour`;
    
    console.log('Fallback URLs:', {
        nodeIdUrl,
        fallbackUrl
    });
    
    return { specificUrl, nodeIdUrl, fallbackUrl };
}

// Image loading queue management
const imageLoadQueue = new Map(); // node.id -> {loading: boolean, urls: string[], currentIndex: number}

// Cache for loaded images
const glamourImageCache = new Map(); // nodeId -> {hash: string, image: Image}

function loadGlamourImage(node, ctx) {
    const nodeId = node.id;
    const nodeHash = generateNodeHash(node);
    
    // Check cache first
    const cached = glamourImageCache.get(nodeId);
    if (cached && cached.hash === nodeHash) {
        // Draw cached image
        drawGlamourImage(cached.image, node, ctx);
        return;
    }
    
    // If already loading this hash, skip
    if (imageLoadQueue.get(nodeId)?.loading && imageLoadQueue.get(nodeId)?.hash === nodeHash) {
        return;
    }

    const nodeTypeSnake = snakeCase(node.type);
    const imageId = `${nodeTypeSnake}_${nodeId}_${nodeHash}`;
    
    console.log('Loading new image for node:', {
        nodeId,
        hash: nodeHash,
        cached: !!cached
    });
    
    const { specificUrl, nodeIdUrl, fallbackUrl } = getGlamourImageUrl(imageId, node.type);
    const urls = [specificUrl, nodeIdUrl, fallbackUrl];

    // Initialize or update queue entry
    const queueEntry = {
        loading: true,
        hash: nodeHash,
        urls,
        currentIndex: 0,
        image: new Image()
    };
    
    imageLoadQueue.set(nodeId, queueEntry);
    
    queueEntry.image.onerror = () => {
        console.log('Failed to load:', urls[queueEntry.currentIndex]);
        queueEntry.currentIndex++;
        if (queueEntry.currentIndex < urls.length) {
            console.log('Trying next URL:', urls[queueEntry.currentIndex]);
            queueEntry.image.src = urls[queueEntry.currentIndex];
        } else {
            queueEntry.loading = false;
            imageLoadQueue.delete(nodeId);
            // Reset to rainbow background if all image loads fail
            resetToRainbowBackground(nodeId);
        }
    };
    
    queueEntry.image.onload = () => {
        console.log('Successfully loaded:', queueEntry.image.src);
        queueEntry.loading = false;
        
        // Cache the successfully loaded image
        glamourImageCache.set(nodeId, {
            hash: nodeHash,
            image: queueEntry.image
        });
        
        // Draw the image
        drawGlamourImage(queueEntry.image, node, ctx);
        
        // Clean up queue
        imageLoadQueue.delete(nodeId);
    };
    
    console.log('Starting image load with:', urls[queueEntry.currentIndex]);
    queueEntry.image.src = urls[queueEntry.currentIndex];
}

function drawGlamourImage(img, node, ctx) {
    // Save context state
    ctx.save();
    
    // Calculate dimensions maintaining aspect ratio
    const scale = Math.min(
        node.size[0] / img.width,
        node.size[1] / img.height
    );
    
    const width = img.width * scale;
    const height = img.height * scale;
    const x = (node.size[0] - width) / 2;
    const y = (node.size[1] - height) / 2;
    
    // Clear the background where the image will be
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = 'rgba(0,0,0,1)';
    ctx.fillRect(x, y, width, height);
    
    // Reset composite operation for drawing the image
    ctx.globalCompositeOperation = 'source-over';
    
    // Add slight glow effect
    ctx.shadowColor = 'rgba(255,255,255,0.2)';
    ctx.shadowBlur = 10;
    
    // Draw the image
    ctx.drawImage(img, x, y, width, height);
    
    // Restore context state
    ctx.restore();
    
    // Mark canvas as dirty
    app.graph.setDirtyCanvas(true, true);

    console.log('Drawing glamour image:', {
        src: img.src,
        nodeId: node.id,
        loaded: img.complete
    });

    // Update the overlay image
    const overlayImage = document.querySelector(`[data-node-id="${node.id}"] .glamour-image`);
    if (overlayImage) {
        console.log('Found overlay element:', overlayImage);
        
        // First, clear all background-related styles
        const stylesToClear = [
            'background',
            'backgroundImage',
            'backgroundSize',
            'backgroundPosition',
            'backgroundRepeat',
            'animation'
        ];
        
        stylesToClear.forEach(style => {
            overlayImage.style[style] = '';
        });
        
        // Then set the new styles
        const newStyles = {
            backgroundImage: `url("${img.src}")`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat'
        };
        
        Object.assign(overlayImage.style, newStyles);
        
        console.log('Applied styles:', {
            backgroundImage: overlayImage.style.backgroundImage,
            backgroundSize: overlayImage.style.backgroundSize,
            computedStyle: window.getComputedStyle(overlayImage).backgroundImage
        });
    } else {
        console.warn('Overlay element not found for node:', node.id);
    }
    
    // Mark canvas as dirty
    app.graph.setDirtyCanvas(true, true);
}

// Add a function to reset to rainbow background if image load fails
function resetToRainbowBackground(nodeId) {
    const overlayImage = document.querySelector(`[data-node-id="${nodeId}"] .glamour-image`);
    if (overlayImage) {
        console.log('Resetting to rainbow background for node:', nodeId);
        
        // Clear all existing background styles
        const stylesToClear = [
            'background',
            'backgroundImage',
            'backgroundSize',
            'backgroundPosition',
            'backgroundRepeat'
        ];
        
        stylesToClear.forEach(style => {
            overlayImage.style[style] = '';
        });
        
        // Set rainbow gradient
        Object.assign(overlayImage.style, {
            background: 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d)',
            backgroundSize: '400% 400%',
            animation: 'gradientBG 15s ease infinite'
        });
    }
}

// Update the addGlamourImageSupport function
function addGlamourImageSupport(node) {
    const originalDrawBackground = node.onDrawBackground;
    node.onDrawBackground = function(ctx) {
        // Only draw original background if no glamour is active
        if (!glamourStates.get(this.id)) {
            if (originalDrawBackground) {
                originalDrawBackground.apply(this, arguments);
            }
            return;
        }
        
        // If glamour is active, load and draw the image
        loadGlamourImage(this, ctx);
    };
}

app.registerExtension({
    name: "Comfy.Glamour",
    async setup() {
        console.log("Glamour extension loaded");
        createGlobalControl();
        
        // Add glamours to all existing nodes
        app.graph._nodes.forEach(node => {
            const glamourWidget = createGlamourOverlay(node, node.name, {}, app);
            if (glamourWidget) {
                node.addCustomWidget(glamourWidget);
                addGlamourImageSupport(node);  // Add image support
            }
        });
        
        // Handle new nodes being added
        const originalAddNode = app.graph.add;
        app.graph.add = function(node) {
            const result = originalAddNode.apply(this, arguments);
            if (node) {
                const glamourWidget = createGlamourOverlay(node, node.name, {}, app);
                if (glamourWidget) {
                    node.addCustomWidget(glamourWidget);
                    addGlamourImageSupport(node);  // Add image support
                }
            }
            return result;
        };
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Glamour 🦊") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            
            nodeType.prototype.onNodeCreated = function() {
                const result = onNodeCreated?.apply(this, arguments);
                return result;
            };
        }
    }
}); 

// Make sure we have the gradient animation defined
const style = document.createElement('style');
style.textContent = `
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}`;
document.head.appendChild(style); 