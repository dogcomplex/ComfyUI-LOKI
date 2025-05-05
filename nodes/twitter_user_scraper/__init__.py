import subprocess
import sys
import os
from .twitter_user_scraper_node import TwitterUserScraper # Import the new node class

# --- Playwright check (Keep as is, maybe make shared later) --- 
# We might not strictly need this for the user scraper if it doesn't use playwright yet,
# but keeping it doesn't hurt for now.
did_playwright_install_check = False
def ensure_playwright_chromium():
    global did_playwright_install_check
    # ... (existing playwright check function placeholder) ...
    pass 

# ensure_playwright_chromium()

# --- Node Registration --- 
NODE_CLASS_MAPPINGS = {
    "TwitterUserScraper": TwitterUserScraper
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "TwitterUserScraper": "🐦👤 Scrape User Profile (LOKI)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[34mLOKI Nodes: \033[93mLoaded Twitter User Scraper node logic\033[0m") 