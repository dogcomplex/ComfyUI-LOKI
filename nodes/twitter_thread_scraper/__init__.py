import subprocess
import sys
import os
from .twitter_thread_scraper_node import TwitterThreadScraper # Import the new node class

# --- Playwright check (Keep as is, maybe make shared later) --- 
did_playwright_install_check = False
def ensure_playwright_chromium():
    global did_playwright_install_check
    # ... (keep existing playwright check function) ...
    pass # Placeholder, keep the existing function body

# Run the check when this sub-module is loaded
# ensure_playwright_chromium() # Maybe only run if needed by this node?

# --- Node Registration --- 
NODE_CLASS_MAPPINGS = {
    "TwitterThreadScraper": TwitterThreadScraper
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "TwitterThreadScraper": "🐦🧵 Scrape Thread (LOKI)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[34mLOKI Nodes: \033[93mLoaded Twitter Thread Scraper node logic\033[0m") 