import subprocess
import sys
import os
from .twitter_scraper_node import LokiTweetScraper

did_playwright_install_check = False

def ensure_playwright_chromium():
    global did_playwright_install_check
    if did_playwright_install_check:
        return
    try:
        # Check if playwright is installed first before trying to run its command
        import playwright
        print("--- [Twitter Scraper] Ensuring Playwright Chromium is installed ---")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True, capture_output=True)
        print("--- [Twitter Scraper] Playwright Chromium check complete ---")
    except ImportError:
        # This should ideally not happen if root requirements are processed first,
        # but good to have a check.
        print("\033[91mERROR: Playwright module not found in twitter_scraper init. Cannot check/install browser.[0m")
    except FileNotFoundError:
         print("\033[91mERROR: Could not execute playwright command (playwright not found in PATH?). Cannot check/install browser.[0m")
    except subprocess.CalledProcessError as e:
        # Log the error, but don't necessarily stop ComfyUI loading
        # Use triple quotes for the f-string to allow the newline from stderr
        print(f"""[93mWARNING: Playwright install command failed (might be okay if browser already exists):
{e.stderr.decode()} [0m""")
    except Exception as e:
         print(f"\033[91mERROR: An unexpected error occurred during Playwright install check: {e} [0m")
    finally:
         did_playwright_install_check = True

# Run the check when this sub-module is loaded
ensure_playwright_chromium()

# Placeholder for ComfyUI node registration
NODE_CLASS_MAPPINGS = {
    "LokiTweetScraper": LokiTweetScraper
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "LokiTweetScraper": "🐦📜 Scrape Tweet (LOKI)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[34mLOKI Nodes: \033[93mLoaded Twitter Scraper node logic\033[0m") # Optional: Add a print statement 