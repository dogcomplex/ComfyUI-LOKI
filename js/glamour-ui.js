export class GlamourUI {
    static RAINBOW_GRADIENT = 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96c93d)';
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
            overflowY: "auto",
            overflowX: "hidden",
            display: "flex",
            flexDirection: "column",
            boxSizing: "border-box",
            padding: "10px",
            fontSize: `${12 * scale}px`
        });

        // Scale all child elements proportionally
        Array.from(element.children).forEach(child => {
            Object.assign(child.style, {
                transform: "none",
                fontSize: "inherit",
                padding: `${5 * scale}px`,
                margin: `${5 * scale}px`
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
        
        Object.assign(element.style, {
            backgroundImage: `url("${imageSrc}")`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat'
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
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }`;
        document.head.appendChild(style);
    }

    static createOverlayHTML(node, nodeTypeSnake, nodeHash) {
        return `
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
                    background: ${this.RAINBOW_GRADIENT};
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
                    ${this.createNodeContent(node, nodeTypeSnake, nodeHash)}
                </div>
            </div>
        `;
    }
} 