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
        let content = `
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="margin: 0; color: #333;">✨ ${node.type} ✨</h3>
                <button class="glamour-toggle" style="
                    background: none;
                    border: none;
                    cursor: pointer;
                    font-size: 1.2em;
                    padding: 5px;
                    color: #666;
                ">❌</button>
            </div>`;
        
        // Add widget values section
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

    // Create the overlay
    const overlay = $el("div.glamour-overlay", {
        innerHTML: `
            <div style="
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                animation: glamourPulse 2s infinite;
                box-sizing: border-box;
            ">
                <div style="
                    background: rgba(255,255,255,0.9);
                    padding: 15px;
                    border-radius: 8px;
                    text-align: left;
                    box-sizing: border-box;
                ">
                    ${createNodeContent()}
                </div>
            </div>
            <style>
                @keyframes glamourPulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
                .section {
                    margin: 10px 0;
                    padding: 5px 0;
                    border-top: 1px solid rgba(0,0,0,0.1);
                }
                .section h4 {
                    margin: 0 0 5px 0;
                    color: #444;
                }
            </style>
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
                const widget = node.widgets.find(w => w.name === widgetName);
                if (widget) {
                    widget.value = e.target.value;
                    if (widget.callback) {
                        widget.callback(widget.value);
                    }
                }
            }
        }
    });

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

    return widget;
}

// Register extension
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
                }
            }
            return result;
        };
    }
}); 