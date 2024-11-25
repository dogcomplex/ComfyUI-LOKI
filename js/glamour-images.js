import { GlamourUI } from "./glamour-ui.js";

// Track image loading and caching state
const imageLoadQueue = new Map(); // node.id -> {loading: boolean, urls: string[], currentIndex: number}
const glamourImageCache = new Map(); // nodeId -> {hash: string, image: Image}

export class GlamourImageManager {
    static getImageUrls(image_id, node_type) {
        console.log('Attempting to load glamour image:', {
            image_id,
            node_type
        });
        
        // Use GlamourUI's snakeCase
        const fallbackUrl = `/view?filename=${encodeURIComponent(GlamourUI.snakeCase(node_type))}.png&type=output&subfolder=Glamour`;
        
        // Try specific image first
        const specificUrl = `/view?filename=${encodeURIComponent(image_id)}.png&type=output&subfolder=Glamour`;
        
        // Prepare fallback URLs using the same pattern
        const nodeIdUrl = `/view?filename=${encodeURIComponent(image_id.split('_').slice(0, 2).join('_'))}.png&type=output&subfolder=Glamour`;
        
        console.log('Image URLs:', {
            specificUrl,
            nodeIdUrl,
            fallbackUrl
        });
        
        return { specificUrl, nodeIdUrl, fallbackUrl };
    }

    static loadImage(node, ctx, nodeHash, onImageLoaded) {
        const nodeId = node.id;
        
        // Check cache first
        const cached = glamourImageCache.get(nodeId);
        if (cached && cached.hash === nodeHash) {
            onImageLoaded(cached.image, node, ctx);
            return;
        }
        
        // If already loading this hash, skip
        if (imageLoadQueue.get(nodeId)?.loading && imageLoadQueue.get(nodeId)?.hash === nodeHash) {
            return;
        }

        const nodeTypeSnake = node.type.toLowerCase().replace(/[^\w\s-]/g, '').replace(/[-\s]+/g, '_');
        const imageId = `${nodeTypeSnake}_${nodeId}_${nodeHash}`;
        
        const { specificUrl, nodeIdUrl, fallbackUrl } = this.getImageUrls(imageId, node.type);
        const urls = [specificUrl, nodeIdUrl, fallbackUrl];

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
            console.log('Failed to load:', urls[queueEntry.currentIndex]);
            queueEntry.currentIndex++;
            if (queueEntry.currentIndex < urls.length) {
                console.log('Trying next URL:', urls[queueEntry.currentIndex]);
                queueEntry.image.src = urls[queueEntry.currentIndex];
            } else {
                queueEntry.loading = false;
                imageLoadQueue.delete(nodeId);
                this.resetToRainbowBackground(nodeId);
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
            
            onImageLoaded(queueEntry.image, node, ctx);
            imageLoadQueue.delete(nodeId);
        };
        
        queueEntry.image.src = urls[queueEntry.currentIndex];
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
} 