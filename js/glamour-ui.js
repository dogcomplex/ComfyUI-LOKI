export class GlamourUI {
    static RAINBOW_GRADIENT = 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d)';
    static AURORA_GRADIENT = 'linear-gradient(90deg, rgba(255, 0, 150, 0.7), rgba(0, 255, 255, 0.5), rgba(0, 255, 255, 0.7))';
    static GLAMOUR_NODE_TYPE = "Glamour 🦊";
    
    static updateOverlayStyles(overlay, transform, nodeWidth, fullHeight, relativeScale, visible, isTransparencyEnabled) {
        console.log(`[Glamour] updateOverlayStyles received isTransparencyEnabled: ${isTransparencyEnabled}, visible: ${visible}`);
        Object.assign(overlay.style, {
            left: `${transform.e + transform.clientRectBound.left}px`,
            top: `${transform.f + transform.clientRectBound.top - transform.headerHeight * transform.d}px`,
            width: `${nodeWidth}px`,
            height: `${fullHeight}px`,
            minHeight: `${fullHeight}px`,
            position: "absolute",
            zIndex: transform.zIndex,
            display: visible ? "block" : "none",
            overflow: "hidden"
        });

        // Scale content relative to node size
        const innerContent = overlay.firstElementChild;
        if (innerContent) {
            // Pass the aurora element specifically, if found
            const auroraElement = innerContent.querySelector('.glamour-aurora');
            this.updateInnerContent(innerContent, auroraElement, isTransparencyEnabled);

            // Find the text element and apply scaling
            const canvasScale = app.canvas.ds.scale; // Get canvas zoom
            const textElement = innerContent.querySelector('.glamour-text');
            if (textElement && canvasScale > 0) { // Add check for canvasScale > 0
                const baseFontSize = 12; // Base font size
                const newSize = baseFontSize * canvasScale;
                textElement.style.fontSize = `${newSize}px`;
                
                // Scale padding proportionally
                const basePadding = 8; // Base padding in pixels
                const newPadding = Math.max(4, basePadding * canvasScale);
                textElement.style.padding = `${newPadding}px ${newPadding * 1.5}px`;
                
                // Scale border radius
                const baseRadius = 8; // Base border radius
                const newRadius = Math.max(4, baseRadius * canvasScale);
                textElement.style.borderRadius = `${newRadius}px`;
                
                // Scale bottom margin
                const baseBottom = 5; // Base bottom position
                const newBottom = Math.max(2, baseBottom * canvasScale);
                textElement.style.bottom = `${newBottom}px`;
                
                // Set up toggle button
                const toggleButton = textElement.querySelector('.glamour-toggle');
                if (toggleButton && !toggleButton.hasInitializedListener) {
                    toggleButton.hasInitializedListener = true;
                    toggleButton.addEventListener('click', (e) => {
                        e.stopPropagation(); // Prevent click from bubbling up
                        e.preventDefault(); // Prevent any default action
                        
                        const nodeId = overlay.getAttribute('data-node-id');
                        console.log(`Glamour toggle clicked for node ${nodeId}`);
                        
                        if (nodeId) {
                            // Get node reference directly
                            const node = app.graph._nodes.find(n => n.id.toString() === nodeId.toString());
                            if (!node) {
                                console.error(`Node ${nodeId} not found`);
                                return;
                            }
                            
                            // Toggle state with strict boolean
                            const currentState = window.glamourStates.get(nodeId) === true;
                            const newState = !currentState;
                            console.log(`Toggling node ${nodeId} glamour: ${currentState} -> ${newState}`);
                            
                            // Set in the global map
                            window.glamourStates.set(nodeId, newState);
                            
                            // Update button UI
                            toggleButton.textContent = newState ? '🌘' : '🌗';
                            toggleButton.title = newState ? 'Disable Glamour' : 'Enable Glamour';
                            
                            // Update global UI
                            if (typeof window.updateBottomRightToggle === 'function') {
                                window.updateBottomRightToggle();
                            }
                            if (typeof window.updateGlamourStateWidget === 'function') {
                                window.updateGlamourStateWidget();
                            }
                            
                            // Force multiple redraws
                            app.graph.setDirtyCanvas(true, true);
                            
                            // Try to trigger a real node redraw 
                            if (node.onDrawBackground) {
                                requestAnimationFrame(() => {
                                    app.graph.setDirtyCanvas(true, true);
                                });
                            }
                        } else {
                            console.error('No nodeId found on overlay element');
                        }
                    });
                    
                    // Initial button state
                    if (window.glamourStates && typeof window.glamourStates.get === 'function') {
                        const nodeId = overlay.getAttribute('data-node-id');
                        if (nodeId) {
                            const isEnabled = window.glamourStates.get(nodeId) === true;
                            toggleButton.textContent = isEnabled ? '🌘' : '🌗';
                            toggleButton.title = isEnabled ? 'Disable Glamour' : 'Enable Glamour';
                        }
                    }
                }
            }
        }
    }

    static updateInnerContent(contentElement, auroraElement, isTransparencyEnabled) {
        Object.assign(contentElement.style, {
            width: "100%",
            height: "100%",
            maxHeight: "100%",
            overflowY: "hidden",
            overflowX: "hidden",
            display: "flex",
            flexDirection: "column",
            boxSizing: "border-box",
            padding: "0",
            background: this.AURORA_GRADIENT,
            backgroundSize: '400% 400%',
            animation: 'northernLights 10s ease-in-out infinite'
        });

        // Apply transparency styles to the main content element
        if (isTransparencyEnabled) {
            Object.assign(contentElement.style, {
                // Using lighten blend mode for the whole container
                mixBlendMode: 'lighten',
                opacity: '0.85' // Slightly transparent container
            });
        } else {
            Object.assign(contentElement.style, {
                mixBlendMode: 'normal',
                opacity: '1' // Fully opaque container
            });
        }

        // Add webkit scrollbar style directly to element
        contentElement.style.setProperty("-webkit-scrollbar", "none");
    }

    static setBackgroundImage(element, imageSrc) {
        const stylesToClear = [
            'background',
            'backgroundImage',
            'backgroundSize',
            'backgroundPosition',
            'backgroundRepeat',
            'animation'
        ];
        
        stylesToClear.forEach(style => element.style[style] = '');
        
        // Find the aurora element (sibling)
        const auroraElement = element.parentElement.querySelector('.glamour-aurora');
        if (auroraElement) {
            // Keep aurora visible but behind the image
            auroraElement.style.zIndex = '1';
        }
        
        // Set image on top with solid background
        Object.assign(element.style, {
            backgroundImage: `url("${imageSrc}")`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
            mixBlendMode: 'normal',
            zIndex: '2',
            opacity: '1'
        });
    }

    static setRainbowBackground(element) {
        const stylesToClear = [
            'background',
            'backgroundImage',
            'backgroundSize',
            'backgroundPosition',
            'backgroundRepeat'
        ];
        
        stylesToClear.forEach(style => element.style[style] = '');
        
        Object.assign(element.style, {
            background: this.RAINBOW_GRADIENT,
            backgroundSize: '400% 400%',
            animation: 'gradientBG 15s ease infinite'
        });
    }

    static getOverlayElement(nodeId) {
        return document.querySelector(`[data-node-id="${nodeId}"] .glamour-image`);
    }

    static createNodeContent(node, nodeTypeSnake, nodeHash) {
        return `
            <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
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
                <div>
                    <button class="glamour-toggle" style="
                        background: none;
                        border: none;
                        font-size: 1.2em;
                        cursor: pointer;
                        padding: 4px;
                        margin: 0;
                        border-radius: 4px;
                        transition: background-color 0.2s;
                        pointer-events: auto;
                    ">🌘</button>
                </div>
            </div>
        `;
    }

    static snakeCase(str) {
        if (!str) return '';
        return str.toLowerCase()
            .replace(/[^\w\s-]/g, '')
            .replace(/[-\s]+/g, '_');
    }

    static initialize() {
        const style = document.createElement('style');
        style.textContent = `
            @keyframes northernLights {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .glamour-content {
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                border-radius: 10px;
                overflow: hidden;
                position: relative;
            }
            
            .glamour-image {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                mix-blend-mode: lighten;
                pointer-events: none;
            }

            .glamour-overlay {
                pointer-events: all;
            }

            .glamour-overlay:hover .glamour-text {
                opacity: 1 !important;
            }

            .glamour-text {
                opacity: 0;
                transition: opacity 0.3s ease;
                pointer-events: auto;
                background: rgba(255,255,255,0.85);
                border-radius: 8px;
                position: absolute;
                bottom: 5px;
                left: 50%;
                transform: translateX(-50%);
                text-align: center;
                z-index: 10;
            }

            .glamour-text .glamour-toggle {
                pointer-events: auto !important;
                cursor: pointer;
            }
            
            .glamour-toggle:hover {
                background-color: rgba(0,0,0,0.1);
            }

            /* Glamour Toggle Button Animation */
            #glamour-toggle-button {
                transition: opacity 0.3s ease, transform 0.3s ease;
                opacity: 1;
                transform: scale(1);
            }
            #glamour-toggle-button.glamour-hidden {
                opacity: 0;
                transform: scale(0.8);
                pointer-events: none;
            }

            /* Veil Icon Animation (applied via JS) */
            .glamour-veil-icon {
                transition: opacity 0.3s ease;
                opacity: 1;
            }
            .glamour-veil-icon.glamour-hidden {
                opacity: 0;
            }
        `;
        document.head.appendChild(style);
    }

    static createOverlayHTML(node, nodeTypeSnake, nodeHash) {
        return `
            <div class="glamour-content" style="
                position: relative;
                padding: 0;
                border-radius: 10px;
                box-shadow: none;
                box-sizing: border-box;
                height: 100%;
                background: transparent;
            ">
                <div class="glamour-aurora" style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border-radius: 10px;
                    z-index: 1;
                    background: ${this.AURORA_GRADIENT};
                    background-size: 400% 400%;
                    animation: northernLights 10s ease-in-out infinite;
                    mask-image: radial-gradient(circle, rgba(0, 0, 0, 1) 60%, rgba(0, 0, 0, 0));
                    -webkit-mask-image: radial-gradient(circle, rgba(0, 0, 0, 1) 60%, rgba(0, 0, 0, 0));
                    mix-blend-mode: lighten;
                    opacity: 0.9;
                    pointer-events: none;
                "></div>
                <div class="glamour-image" style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border-radius: 10px;
                    z-index: 2;
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    pointer-events: none;
                "></div>
                <div class="glamour-text" style="
                    position: relative;
                    background: rgba(255,255,255,0.85);
                    padding: 8px 12px;
                    border-radius: 8px;
                    z-index: 3;
                    opacity: 0;
                    transition: opacity 0.3s ease;
                    pointer-events: none;
                ">
                    ${this.createNodeContent(node, nodeTypeSnake, nodeHash)}
                </div>
            </div>
        `;
    }

    static createOverlay(node, nodeType, nodeHash) {
        const overlay = document.createElement('div');
        overlay.className = 'glamour-overlay';
        overlay.setAttribute('data-node-id', node.id);
        overlay.innerHTML = this.createOverlayHTML(node, nodeType, nodeHash);
        return overlay;
    }
} 