export class GlamourUI {
    static RAINBOW_GRADIENT = 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d)';
    static AURORA_GRADIENT = 'linear-gradient(90deg, rgba(255, 0, 150, 0.7), rgba(0, 255, 255, 0.5), rgba(0, 255, 255, 0.7))';
    static GLAMOUR_NODE_TYPE = "Glamour 🦊";
    
    static updateOverlayStyles(overlay, transform, nodeWidth, fullHeight, relativeScale, visible) {
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
            this.updateInnerContent(innerContent, relativeScale);
        }
    }

    static updateInnerContent(element, scale) {
        Object.assign(element.style, {
            width: "100%",
            height: "100%",
            maxHeight: "100%",
            overflowY: "hidden",
            overflowX: "hidden",
            display: "flex",
            flexDirection: "column",
            boxSizing: "border-box",
            padding: "0",
            fontSize: `${12 * scale}px`,
            background: this.AURORA_GRADIENT,
            backgroundSize: '400% 400%',
            animation: 'northernLights 10s ease-in-out infinite',
            maskImage: 'radial-gradient(circle, rgba(0, 0, 0, 1) 60%, rgba(0, 0, 0, 0))',
            WebkitMaskImage: 'radial-gradient(circle, rgba(0, 0, 0, 1) 60%, rgba(0, 0, 0, 0))',
            mixBlendMode: 'lighten',
            opacity: '0.9'
        });

        // Add webkit scrollbar style directly to element
        element.style.setProperty("-webkit-scrollbar", "none");
        
        // Scale all child elements proportionally
        Array.from(element.children).forEach(child => {
            Object.assign(child.style, {
                transform: "none",
                fontSize: "inherit",
                padding: "0",
                margin: "0"
            });
        });
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
            auroraElement.style.opacity = '0.9';
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
            </div>
        `;
    }

    static snakeCase(str) {
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
                pointer-events: all;
            }

            .glamour-text {
                opacity: 0;
                transition: opacity 0.3s ease;
                pointer-events: none;
                background: rgba(255,255,255,0.85);
                padding: 15px;
                border-radius: 8px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                z-index: 10;
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
                    padding: 15px;
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
} 