import { app } from "../../scripts/app.js";
import { $el } from "../../scripts/ui.js";
import { GlamourImageManager } from "./glamour-images.js";
import { GlamourUI } from "./glamour-ui.js";

// Track all glamours
let allGlamours = new Set();

// Track glamours per node
let glamourStates = new Map(); // node.id -> boolean

// Master Glamour control state
let isGlamourMasterEnabled = true;
let glamourNodeInstance = null; // Keep track of the Glamour node

// Reference to the new button group toggle
let bottomRightToggleButton = null;
// Reference to the custom tooltip element
let glamourTooltipElement = null;
// Reference to the glamour_state widget on the Glamour node
let glamourStateWidget = null;

// Flag to prevent widget callback loops
let settingWidgetInternally = false;

function updateBottomRightToggle() {
    if (!bottomRightToggleButton) return;

    const hasActiveGlamour = Array.from(glamourStates.values()).some(state => state);
    const iconSpan = bottomRightToggleButton.querySelector('.p-button-icon');
    const icon = hasActiveGlamour ? "🧿" : "🦊";
    const label = hasActiveGlamour ? "Veil All" : "Glamour All"; // Changed Unveil to Veil

    if (iconSpan) {
        iconSpan.textContent = icon;
        // Keep aria-label for accessibility
        bottomRightToggleButton.setAttribute('aria-label', label);
        // Apply hidden class based on master state
        if (bottomRightToggleButton) {
            bottomRightToggleButton.classList.toggle('glamour-hidden', !isGlamourMasterEnabled);
        }
    } else {
         // Fallback if icon span structure changes
         bottomRightToggleButton.textContent = icon; // Less ideal, might mess up styling
         bottomRightToggleButton.setAttribute('aria-label', label);
    }
}

function generateNodeHash(node) {
    const stableValues = {
        type: node.type,
        inputs: {},
        widgets: {},
        connections: {}
    };

    if (node.inputs) {
        for (const [key, input] of Object.entries(node.inputs)) {
            if (input.value !== undefined) {
                stableValues.inputs[key] = input.value;
            }
            
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

    if (node.widgets) {
        node.widgets.forEach(widget => {
            if (widget.type === "glamour") return;
            
            stableValues.widgets[widget.name] = {
                type: widget.type,
                value: widget.value,
                options: widget.options,
                min: widget.min,
                max: widget.max
            };
        });
    }

    const contentStr = JSON.stringify(stableValues, (key, value) => {
        if (value && typeof value === 'object') {
            return Object.keys(value).sort().reduce((sorted, key) => {
                if (value[key] !== undefined && value[key] !== null) {
                    sorted[key] = value[key];
                }
                return sorted;
            }, {});
        }
        return value;
    });
    
    let hash = 0;
    for (let i = 0; i < contentStr.length; i++) {
        const char = contentStr.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }
    
    return Math.abs(hash).toString(16).padStart(8, '0');
}

function createGlamourOverlay(node, inputName, inputData, app) {
    if (!node || typeof node.addCustomWidget !== 'function') {
        console.warn('Node does not support custom widgets:', node?.type);
        return null;
    }
    
    // Initialize widgets array if it doesn't exist
    if (!node.widgets) {
        node.widgets = [];
    }
    
    // Check for existing glamour widget and remove it if found
    const existingGlamourIndex = node.widgets.findIndex(w => w.type === "glamour");
    if (existingGlamourIndex !== -1) {
        node.widgets.splice(existingGlamourIndex, 1);
    }
    
    // Remove any existing glamour overlay elements
    const existingOverlay = document.querySelector(`[data-node-id="${node.id}"] .glamour-content`);
    if (existingOverlay) {
        existingOverlay.remove();
    }

    const isGlamourNode = node.type === GlamourUI.GLAMOUR_NODE_TYPE;
    // Set initial state, default to true unless it's the specific Glamour node type
    if (!glamourStates.has(node.id) || !isGlamourMasterEnabled) {
        glamourStates.set(node.id, !isGlamourNode && isGlamourMasterEnabled);
    }

    const headerHeight = LiteGraph.NODE_TITLE_HEIGHT;
    const nodeTypeSnake = GlamourUI.snakeCase(node.type);
    const nodeHash = generateNodeHash(node);

    const updateHashDisplay = (overlay) => {
        const hashDisplay = overlay.querySelector('.node-hash');
        if (hashDisplay) {
            const nodeTypeSnake = GlamourUI.snakeCase(node.type);
            const newHash = generateNodeHash(node);
            hashDisplay.textContent = `${nodeTypeSnake}_${node.id}_${newHash}`;
        }
    };

    const updateInputField = (widgetName, value) => {
        const input = overlay.querySelector(`input[data-widget="${widgetName}"]`);
        if (input && input.value !== value) {
            input.value = value;
            updateHashDisplay(overlay);
        }
    };

    const updateWidgetValue = (widgetName, value) => {
        const widget = node.widgets.find(w => w.name === widgetName);
        if (widget && widget.value !== value) {
            widget.value = value;
            if (widget.callback) {
                widget.callback(value);
            }
            updateHashDisplay(overlay);
        }
    };

    const widget = {
        type: "glamour",
        name: `w${inputName}`,
        
        draw: function(ctx, node, widgetWidth, y, widgetHeight) {
            const isActive = glamourStates.get(node.id) ?? true;
            // Only draw veil icon if master enabled and node is inactive
            if (isGlamourMasterEnabled && !isActive) {
                ctx.save();
                ctx.font = "16px Arial"; // Keep font size reasonable for title bar
                ctx.fillStyle = "#AAA"; // Slightly lighter color might look better on title
                ctx.textAlign = "right";

                const titleHeight = LiteGraph.NODE_TITLE_HEIGHT;
                const x = node.size[0] - 10;
                const y_icon = -titleHeight + titleHeight / 2 + 7;

                this.veilRegion = [node.size[0] - 25, -titleHeight, 25, titleHeight];
                ctx.fillText("🌑", x, y_icon);
                ctx.restore();
            }
            
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
                const relativeScale = (nodeWidth / transform.a) / 400;
                
                GlamourUI.updateOverlayStyles(
                    this.overlay,
                    {
                        e: transform.e,
                        f: transform.f,
                        clientRectBound,
                        headerHeight,
                        d: transform.d,
                        zIndex: app.graph._nodes.indexOf(node)
                    },
                    nodeWidth,
                    fullHeight,
                    relativeScale,
                    isActive
                );
            }
        },
        
        computeSize: function() {
            return [0, 0];
        },
        
        onRemoved: function() {
            if (this.overlay && this.overlay.parentElement) {
                this.overlay.parentElement.removeChild(this.overlay);
            }
            allGlamours.delete(this);
        },
        
        onMouseDown: function(e, local_pos, global_pos, graphCanvas) {
            if (!glamourStates.get(this.parent.id) && this.veilRegion) {
                const [x, y, w, h] = this.veilRegion;
                if (local_pos[0] > x && local_pos[0] < x + w &&
                    local_pos[1] > y && local_pos[1] < y + h) {
                    glamourStates.set(this.parent.id, true);
                    updateBottomRightToggle(); // Update the global toggle state representation
                    updateGlamourStateWidget(); // Update the combo box state
                    app.graph.setDirtyCanvas(true);
                    return true;
                }
            }
            return false;
        }
    };

    const overlay = $el("div.glamour-overlay", {
        style: { display: 'none' },
        innerHTML: GlamourUI.createOverlayHTML(node, nodeTypeSnake, nodeHash),
        onclick: (e) => {
            if (e.target.classList.contains('glamour-toggle')) {
                glamourStates.set(node.id, false);
                updateBottomRightToggle(); // Update the global toggle state representation
                updateGlamourStateWidget(); // Update the combo box state
                app.graph.setDirtyCanvas(true);

                // If tooltip is currently visible, update its text immediately
                if (glamourTooltipElement && glamourTooltipElement.style.display === 'block') {
                    const currentLabel = "Veil All";
                    glamourTooltipElement.textContent = currentLabel;
                    // Reposition slightly in case text length change affected width
                    const groupRect = bottomRightToggleButton.parentElement?.getBoundingClientRect();
                    if (groupRect) {
                        glamourTooltipElement.style.left = `${groupRect.left - glamourTooltipElement.offsetWidth - 5}px`;
                    }
                }
            }
        },
        onchange: (e) => {
            if (e.target.classList.contains('glamour-input')) {
                updateWidgetValue(e.target.dataset.widget, e.target.value);
                app.graph.setDirtyCanvas(true);
            }
        }
    });

    overlay.setAttribute('data-node-id', node.id);

    const originalSetValue = node.setPropertyValue;
    if (originalSetValue) {
        node.setPropertyValue = function(name, value) {
            const result = originalSetValue.call(this, name, value);
            updateInputField(name, value);
            app.graph.setDirtyCanvas(true);
            return result;
        };
    }

    if (Array.isArray(node.widgets)) {
        node.widgets.forEach(widget => {
            if (widget?.type !== "glamour") {
                const originalCallback = widget.callback;
                widget.callback = function(value) {
                    if (originalCallback) {
                        originalCallback.call(this, value);
                    }
                    updateInputField(widget.name, value);
                    app.graph.setDirtyCanvas(true);
                };
            }
        });
    }

    const originalOnInputChanged = node.onInputChanged;
    node.onInputChanged = function() {
        if (originalOnInputChanged) {
            originalOnInputChanged.apply(this, arguments);
        }
        updateHashDisplay(overlay);
        app.graph.setDirtyCanvas(true);
    };

    if (Array.isArray(node.widgets)) {
        node.widgets.forEach(widget => {
            if (widget?.type !== "glamour" && widget?.name && widget?.value !== undefined) {
                updateInputField(widget.name, widget.value);
            }
        });
    }
    updateHashDisplay(overlay);

    widget.overlay = overlay;
    widget.parent = node;
    allGlamours.add(widget);
    document.body.appendChild(overlay);

    node.addCustomWidget(widget);

    const originalGetNodeMenuOptions = node.getMenuOptions;
    node.getMenuOptions = function(graphCanvas) {
        return originalGetNodeMenuOptions ? originalGetNodeMenuOptions.call(this, graphCanvas) : [];
    };

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

    const originalDrawBackground = node.onDrawBackground;
    node.onDrawBackground = function(ctx) {
        if (originalDrawBackground) {
            originalDrawBackground.apply(this, arguments);
        }

        // Only load/draw image if node's glamour is active AND master is enabled
        if (isGlamourMasterEnabled && glamourStates.get(this.id)) {
            loadGlamourImage(this, ctx);
        }
    };

    return widget;
}

function loadGlamourImage(node, ctx) {
    const nodeHash = generateNodeHash(node);
    GlamourImageManager.loadImage(node, ctx, nodeHash, drawGlamourImage);
}

function drawGlamourImage(img, node, ctx) {
    ctx.save();
    
    const scale = Math.min(
        node.size[0] / img.width,
        node.size[1] / img.height
    );
    
    const width = img.width * scale;
    const height = img.height * scale;
    const x = (node.size[0] - width) / 2;
    const y = (node.size[1] - height) / 2;
    
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = 'rgba(0,0,0,1)';
    ctx.fillRect(x, y, width, height);
    
    ctx.globalCompositeOperation = 'source-over';
    ctx.shadowColor = 'rgba(255,255,255,0.2)';
    ctx.shadowBlur = 10;
    ctx.drawImage(img, x, y, width, height);
    ctx.restore();
    
    app.graph.setDirtyCanvas(true, true);
    GlamourImageManager.updateOverlayImage(node.id, img.src);
}

function addGlamourImageSupport(node) {
    const originalDrawBackground = node.onDrawBackground;
    node.onDrawBackground = function(ctx) {
        if (!glamourStates.get(this.id)) {
            if (originalDrawBackground) {
                originalDrawBackground.apply(this, arguments);
            }
            return;
        }
        loadGlamourImage(this, ctx);
    };
}

// Add a function to handle the master toggle logic
function handleMasterGlamourToggle(enabled) {
    if (enabled === isGlamourMasterEnabled) return; // No change

    isGlamourMasterEnabled = enabled;

    if (!enabled) {
        // Disable: Veil all nodes
        console.log("Disabling Glamour globally.");
        allGlamours.forEach(widget => {
            glamourStates.set(widget.parent.id, false);
        });
        if (bottomRightToggleButton) {
            bottomRightToggleButton.classList.add('glamour-hidden');
            // After animation, remove from layout
            setTimeout(() => {
                if (bottomRightToggleButton) { // Check again in case state changed fast
                    bottomRightToggleButton.style.display = 'none';
                }
            }, 300); // Match CSS transition duration
        }
    } else {
        // Enable: Restore nodes to a veiled state initially
        // (Could potentially restore previousGlamourStates if implemented)
        console.log("Enabling Glamour globally.");
        allGlamours.forEach(widget => {
            // Set to false (veiled), except for the Glamour node itself if present
            const isGlamourNode = widget.parent.type === GlamourUI.GLAMOUR_NODE_TYPE;
            glamourStates.set(widget.parent.id, false);
        });
        if (bottomRightToggleButton) {
            // Set display before removing hidden class for animation
            bottomRightToggleButton.style.display = ''; // Reset display (or use 'block', 'flex', etc. if needed)

            // Force reflow to ensure display applies before animation starts
            void bottomRightToggleButton.offsetHeight;

            // Remove hidden class to trigger fade-in
            bottomRightToggleButton.classList.remove('glamour-hidden');
        }
    }

    updateBottomRightToggle(); // Update button icon/aria-label/visibility class
    app.graph.setDirtyCanvas(true); // Redraw canvas
}

// Function to update the state widget based on current glamourStates
function updateGlamourStateWidget() {
    if (!glamourStateWidget || !glamourNodeInstance || !isGlamourMasterEnabled) {
        // If widget/node not found or master disabled, set to Mixed or appropriate state
        if (glamourStateWidget) {
           settingWidgetInternally = true;
           glamourStateWidget.value = "Mixed"; 
           settingWidgetInternally = false;
        }
       return;
    }

    const states = Array.from(glamourStates.values());
    const allGlamoured = states.every(s => s === true);
    const allVeiled = states.every(s => s === false);

    let newState;
    if (allGlamoured) {
        newState = "All Glamoured";
    } else if (allVeiled) {
        newState = "All Veiled";
    } else {
        newState = "Mixed";
    }

    // Prevent callback loop when setting programmatically
    if (glamourStateWidget.value !== newState) {
       settingWidgetInternally = true;
       glamourStateWidget.value = newState;
       // ComfyUI might need a nudge to visually update the widget if just setting value
       if (glamourNodeInstance.setDirtyCanvas) {
           glamourNodeInstance.setDirtyCanvas(true, true);
       }
       settingWidgetInternally = false;
    }
}

app.registerExtension({
    name: "Comfy.Glamour",
    async setup() {
        console.log("Glamour extension loaded");
        GlamourUI.initialize();

        // Create and append the tooltip element once
        if (!document.getElementById('glamour-custom-tooltip')) {
            glamourTooltipElement = $el("span", {
                id: "glamour-custom-tooltip",
                className: "p-tooltip p-component p-tooltip-text",
                style: {
                    position: 'fixed',
                    display: 'none',
                    zIndex: 1001, // Above the button group
                    pointerEvents: 'none', // Prevent tooltip from blocking clicks
                    whiteSpace: 'nowrap'
                }
            });
            document.body.appendChild(glamourTooltipElement);
        }

        // Function to add the toggle button to the ComfyUI group
        const addGlamourToggleButton = () => {
            // Selector for the vertical button group in the bottom right
            // Need to escape brackets for querySelector
            const buttonGroup = document.querySelector('.p-buttongroup.p-buttongroup-vertical.absolute.bottom-\\[10px\\].right-\\[10px\\]');

            if (buttonGroup && !document.getElementById('glamour-toggle-button')) {
                console.log("Found button group, adding Glamour toggle.");
                bottomRightToggleButton = $el("button", {
                    id: "glamour-toggle-button",
                    // Add initial hidden class if master is disabled at setup
                    className: `p-button p-component p-button-icon-only p-button-secondary ${!isGlamourMasterEnabled ? 'glamour-hidden' : ''}`,
                    // Add initial display:none style if master is disabled at setup
                    style: {
                        display: !isGlamourMasterEnabled ? 'none' : '' // Start hidden from layout if disabled
                    },
                    type: "button",
                    "data-pc-name": "button",
                    "data-pc-section": "root",
                    // aria-label will be set dynamically by updateBottomRightToggle
                    onclick: () => {
                        const currentStateIsGlamour = Array.from(glamourStates.values()).some(state => state);
                        const newState = !currentStateIsGlamour;
                        // Toggle all nodes
                        allGlamours.forEach(widget => {
                            glamourStates.set(widget.parent.id, newState);
                        });
                        updateBottomRightToggle(); // Update the button state
                        app.graph.setDirtyCanvas(true);

                        // If tooltip is currently visible, update its text immediately
                        if (glamourTooltipElement && glamourTooltipElement.style.display === 'block') {
                            const currentLabel = newState ? "Veil All" : "Glamour All";
                            glamourTooltipElement.textContent = currentLabel;
                            // Reposition slightly in case text length change affected width
                            const groupRect = bottomRightToggleButton.parentElement?.getBoundingClientRect();
                            if (groupRect) {
                                glamourTooltipElement.style.left = `${groupRect.left - glamourTooltipElement.offsetWidth - 5}px`;
                            }
                        }

                        updateGlamourStateWidget(); // Update the combo box state
                    },
                    onmouseenter: () => {
                        if (!glamourTooltipElement) return;
                        const hasActiveGlamour = Array.from(glamourStates.values()).some(state => state);
                        const label = hasActiveGlamour ? "Veil All" : "Glamour All";
                        glamourTooltipElement.textContent = label;

                        // Make element part of layout but hidden for measurement
                        glamourTooltipElement.style.visibility = 'hidden';
                        glamourTooltipElement.style.display = 'block';

                        const groupRect = bottomRightToggleButton.parentElement?.getBoundingClientRect(); // Get rect of the parent group
                        const rect = bottomRightToggleButton.getBoundingClientRect(); // Get rect of the button itself for vertical alignment

                        if (!groupRect) return; // Exit if parent isn't found somehow

                        // Dynamic positioning: Align right edge of tooltip with left edge of group, with a small gap
                        glamourTooltipElement.style.left = `${groupRect.left - glamourTooltipElement.offsetWidth - 5}px`;
                        // Dynamic positioning: Vertically center relative to the button
                        glamourTooltipElement.style.top = `${rect.top + (rect.height / 2) - (glamourTooltipElement.offsetHeight / 2)}px`;

                        // Now make it visible at the calculated position
                        glamourTooltipElement.style.visibility = 'visible';
                    },
                    onmouseleave: () => {
                        if (glamourTooltipElement) {
                            glamourTooltipElement.style.display = 'none';
                            glamourTooltipElement.style.visibility = 'hidden'; // Also hide visibility
                        }
                    }
                }, [
                     $el("span", { className: "p-button-icon"}), // Placeholder for icon
                     $el("span", { className: "p-button-label"}, " ") // Empty label like others
                ]);

                updateBottomRightToggle(); // Set initial state (icon + aria-label) BEFORE appending
                buttonGroup.appendChild(bottomRightToggleButton);

                // Also update the state widget initially if needed
                setTimeout(updateGlamourStateWidget, 0); // Defer slightly

            } else if (!buttonGroup) {
                console.log("Button group not found yet, retrying...");
                // Retry if the group isn't found immediately (might be added later by ComfyUI)
                setTimeout(addGlamourToggleButton, 500);
            }
        };

        // Initial attempt to add the button
        addGlamourToggleButton();

        app.graph._nodes.forEach(node => {
            const glamourWidget = createGlamourOverlay(node, node.name, {}, app);
            if (glamourWidget) {
                node.addCustomWidget(glamourWidget);
                addGlamourImageSupport(node);
            }
        });
        
        const originalAddNode = app.graph.add;
        app.graph.add = function(node) {
            const result = originalAddNode.apply(this, arguments);
            if (node) {
                const glamourWidget = createGlamourOverlay(node, node.name, {}, app);
                if (glamourWidget) {
                    node.addCustomWidget(glamourWidget);
                    addGlamourImageSupport(node);
                }
            }
            return result;
        };

        // Add configuration to the app's settings
        app.ui.settings.addSetting({
            id: "Comfy.Glamour.polling",
            name: "Glamour Image Polling",
            type: "boolean",
            defaultValue: true,
            onChange(value) {
                GlamourImageManager.updatePollingConfig({ enabled: value });
            }
        });

        app.ui.settings.addSetting({
            id: "Comfy.Glamour.pollingInterval",
            name: "Glamour Polling Interval (ms)",
            type: "number",
            defaultValue: 1000,
            min: 100,
            max: 10000,
            step: 100,
            onChange(value) {
                GlamourImageManager.updatePollingConfig({ interval: value });
            }
        });
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === GlamourUI.GLAMOUR_NODE_TYPE) {
            // Hook into configure to get widget reference and attach callback
            const onConfigure = nodeType.prototype.onConfigure;
            const onNodeCreated = nodeType.prototype.onNodeCreated; // Store original onNodeCreated
            nodeType.prototype.onNodeCreated = function() {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                glamourNodeInstance = this; // Store reference
                if (this.widgets) { 
                    const enableWidget = this.widgets.find(w => w.name === "enable_controls");
                    if (enableWidget) {
                        // Store original callback if exists
                        const originalEnableCallback = enableWidget.callback;
                        enableWidget.callback = (value) => {
                            // Defer execution slightly
                            setTimeout(() => handleMasterGlamourToggle(value), 0);
                            // Call original callback if it existed
                            if (originalEnableCallback) {
                                return originalEnableCallback.call(this, value);
                            }
                        };
                        // Trigger initial state based on default widget value (also deferred)
                        setTimeout(() => handleMasterGlamourToggle(enableWidget.value), 0);
                    }

                    glamourStateWidget = this.widgets.find(w => w.name === "glamour_state");

                    if (glamourStateWidget) {
                        const originalStateCallback = glamourStateWidget.callback;
                        glamourStateWidget.callback = (value) => {
                            if (settingWidgetInternally) return; // Prevent loop

                            console.log(`Glamour state widget changed to: ${value}`);
                            if (value === "All Glamoured") {
                                allGlamours.forEach(widget => glamourStates.set(widget.parent.id, true));
                            } else if (value === "All Veiled") {
                                allGlamours.forEach(widget => glamourStates.set(widget.parent.id, false));
                            } // "Mixed" does nothing when selected

                            updateBottomRightToggle(); // Update button appearance
                            app.graph.setDirtyCanvas(true);

                            if (originalStateCallback) {
                                return originalStateCallback.call(this, value);
                            }
                        };
                        // Set initial widget state based on current nodes
                        setTimeout(updateGlamourStateWidget, 0); // Defer slightly
                    }
                }
                return r;
            };

            // Handle cases where widget value might change externally (e.g., loading workflow)
            const onPropertyChanged = nodeType.prototype.onPropertyChanged;
            nodeType.prototype.onPropertyChanged = function(property, value) {
                const r = onPropertyChanged ? onPropertyChanged.apply(this, arguments) : undefined;
                if (property === "enable_controls") {
                    // Defer execution slightly
                    setTimeout(() => handleMasterGlamourToggle(value), 0);
                } else if (property === "glamour_state") {
                    // If loaded from workflow, update internal state display if needed
                    // but generally let the callback handle user changes.
                    // We might need to call updateGlamourStateWidget here if the loaded
                    // value doesn't match the actual node states.
                    setTimeout(updateGlamourStateWidget, 50); // Update widget based on actual state after a small delay
                }
                return r;
            }
        }
    }
}); 