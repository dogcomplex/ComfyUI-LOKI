import { app } from "../../scripts/app.js";
import { $el } from "../../scripts/ui.js";
import { GlamourImageManager } from "./glamour-images.js";
import { GlamourUI } from "./glamour-ui.js";

// Track all glamours
let allGlamours = new Set();
let isGlamourActive = true;

// Track glamours per node
let glamourStates = new Map(); // node.id -> boolean
let isGlobalGlamourActive = false; // Start with Unveil by default

function updateGlobalControl() {
    const control = document.querySelector('.global-glamour-toggle');
    if (!control) return;
    
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
    if (!node) return;
    
    if (node.widgets?.find(w => w.type === "glamour")) return;
    
    if (!node.widgets) {
        node.widgets = [];
    }

    const isGlamourNode = node.type === GlamourUI.GLAMOUR_NODE_TYPE;
    glamourStates.set(node.id, isGlamourNode);
    updateGlobalControl();
    
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
            const visible = app.canvas.ds.scale > 0.5 && isActive;
            
            if (!isActive) {
                ctx.save();
                ctx.font = "16px Arial";
                ctx.fillStyle = "#666";
                const x = node.size[0] - 30;
                const y = node.size[1] - 25;
                this.pawRegion = [x, y, 20, 20];
                ctx.fillText("🐾", x, y + 15);
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
                    visible
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

    const overlay = $el("div.glamour-overlay", {
        innerHTML: GlamourUI.createOverlayHTML(node, nodeTypeSnake, nodeHash),
        onclick: (e) => {
            if (e.target.classList.contains('glamour-toggle')) {
                glamourStates.set(node.id, false);
                updateGlobalControl();
                app.graph.setDirtyCanvas(true);
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

        if (glamourStates.get(this.id)) {
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

app.registerExtension({
    name: "Comfy.Glamour",
    async setup() {
        console.log("Glamour extension loaded");
        GlamourUI.initialize();
        createGlobalControl();
        
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
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                return onNodeCreated?.apply(this, arguments);
            };
        }
    }
}); 