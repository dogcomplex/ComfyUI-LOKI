import { GlamourUI } from "./glamour-ui.js";

// Add configuration settings at the top
const GLAMOUR_CONFIG = {
    pollingEnabled: true,
    pollingInterval: 1000, // 1 second in milliseconds
    imagePollers: new Map(), // Track polling timers per node
};

// Track image loading and caching state
const imageLoadQueue = new Map(); // node.id -> {loading: boolean, urls: string[], currentIndex: number}

export class GlamourImageManager {
    static getImageUrls(image_id, node_type, cacheBust = false) {
        console.log('Attempting to load glamour image:', {
            image_id,
            node_type,
            cacheBust
        });
        
        // Add cache busting parameter if requested
        const cacheParam = cacheBust ? `&t=${Date.now()}` : '';
        
        // Return array of URLs directly instead of an async getter
        const specificUrl = `/view?filename=${encodeURIComponent(image_id)}.png&type=output&subfolder=Glamour${cacheParam}`;
        const nodeTypeUrl = `/view?filename=${encodeURIComponent(GlamourUI.snakeCase(node_type))}.png&type=output&subfolder=Glamour${cacheParam}`;
        
        console.log('Generated URLs:', {
            specificUrl,
            nodeTypeUrl
        });
        
        return [specificUrl, nodeTypeUrl];
    }

    static async loadImage(node, ctx, nodeHash, onImageLoaded, forceCacheBust = false) {
        const nodeId = node.id;
        
        // Clear existing poller if any
        this.clearImagePoller(nodeId);
        
        // Remove cache check - we want to always load fresh images
        const nodeTypeSnake = GlamourUI.snakeCase(node.type);
        const imageId = `${nodeTypeSnake}_${nodeId}_${nodeHash}`;
        
        const urls = this.getImageUrls(imageId, node.type, true); // Always use cache busting
        
        if (!urls || urls.length === 0) {
            console.log('No valid image URLs found');
            this.resetToRainbowBackground(nodeId);
            return;
        }

        // Initialize queue entry
        const queueEntry = {
            loading: true,
            hash: nodeHash,
            urls,
            currentIndex: 0,
            image: new Image()
        };
        
        imageLoadQueue.set(nodeId, queueEntry);
        
        queueEntry.image.onerror = () => {
            console.warn('Failed to load:', urls[queueEntry.currentIndex]);
            queueEntry.currentIndex++;
            if (queueEntry.currentIndex < urls.length) {
                queueEntry.image.src = urls[queueEntry.currentIndex];
            } else {
                queueEntry.loading = false;
                imageLoadQueue.delete(nodeId);
                this.resetToRainbowBackground(nodeId);
            }
        };

        queueEntry.image.onload = () => {
            queueEntry.loading = false;
            onImageLoaded(queueEntry.image, node, ctx);
            imageLoadQueue.delete(nodeId);

            if (GLAMOUR_CONFIG.pollingEnabled) {
                this.startImagePoller(nodeId, nodeHash, node, ctx, onImageLoaded);
            }
        };
        
        queueEntry.image.src = urls[0];
    }

    static resetToRainbowBackground(nodeId) {
        const overlayImage = GlamourUI.getOverlayElement(nodeId);
        if (overlayImage) {
            console.log('Resetting to rainbow background for node:', nodeId);
            GlamourUI.setRainbowBackground(overlayImage);
        }
    }

    static updateOverlayImage(nodeId, imageSrc) {
        const overlayImage = GlamourUI.getOverlayElement(nodeId);
        if (overlayImage) {
            GlamourUI.setBackgroundImage(overlayImage, imageSrc);
        }
    }

    static startImagePoller(nodeId, nodeHash, node, ctx, onImageLoaded) {
        this.clearImagePoller(nodeId);

        const pollImage = async () => {
            const imageId = `${GlamourUI.snakeCase(node.type)}_${nodeId}_${nodeHash}`;
            
            try {
                const response = await fetch(`/glamour/check_glamour_timestamp?` + new URLSearchParams({
                    image_id: imageId,
                    node_type: node.type,
                    t: Date.now()
                }));
                
                if (response.ok) {
                    // If the file exists, reload the image
                    this.loadImage(node, ctx, nodeHash, onImageLoaded, true);
                }
            } catch (error) {
                console.warn('Failed to poll for image updates:', error);
            }
        };

        const timerId = setInterval(pollImage, GLAMOUR_CONFIG.pollingInterval);
        GLAMOUR_CONFIG.imagePollers.set(nodeId, timerId);
    }

    static clearImagePoller(nodeId) {
        const existingPoller = GLAMOUR_CONFIG.imagePollers.get(nodeId);
        if (existingPoller) {
            clearInterval(existingPoller);
            GLAMOUR_CONFIG.imagePollers.delete(nodeId);
        }
    }

    static updatePollingConfig({ enabled, interval }) {
        if (enabled !== undefined) {
            GLAMOUR_CONFIG.pollingEnabled = enabled;
            if (!enabled) {
                // Clear all existing pollers
                for (const [nodeId] of GLAMOUR_CONFIG.imagePollers) {
                    this.clearImagePoller(nodeId);
                }
            }
        }
        
        if (interval !== undefined) {
            GLAMOUR_CONFIG.pollingInterval = interval;
            // Restart all pollers with new interval
            if (GLAMOUR_CONFIG.pollingEnabled) {
                for (const [nodeId] of imageLoadQueue) {
                    const node = app.graph._nodes.find(n => n.id === nodeId);
                    if (node) {
                        const hash = generateNodeHash(node);
                        this.clearImagePoller(nodeId);
                        this.startImagePoller(nodeId, hash, node, null, drawGlamourImage);
                    }
                }
            }
        }
    }
} 