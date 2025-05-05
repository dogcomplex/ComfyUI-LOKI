import json
from .twitter_scraper import scrape_tweet_data # Import from the same directory

class TwitterScraper:
    """ 
    LOKI Node: Scrapes data from a specific X.com (Twitter) tweet URL using Playwright.
    Input: tweet_url (STRING)
    Output: tweet_data (STRING - JSON formatted)
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "tweet_url": ("STRING", {"multiline": False, "default": "https://x.com/Scrapfly_dev/status/1664267318053179398"}),
            },
            "optional": {
                 "run_headless": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tweet_data_json",)
    FUNCTION = "scrape_tweet"
    CATEGORY = "LOKI 🦊/Web"
    OUTPUT_NODE = True # Useful for nodes that primarily produce final output data

    def scrape_tweet(self, tweet_url: str, run_headless: bool = True):
        print(f"[LokiTweetScraper] Attempting to scrape: {tweet_url}")
        scraped_data_dict = scrape_tweet_data(tweet_url, headless=run_headless)

        # --- ADDED DEBUGGING --- 
        print(f"[LokiTweetScraper] Raw data returned from scrape_tweet_data: {type(scraped_data_dict)}")
        # Avoid printing potentially huge dicts directly, check if it's None or empty first
        if isinstance(scraped_data_dict, dict):
            print(f"[LokiTweetScraper] Keys in returned data: {list(scraped_data_dict.keys())}")
        else:
            print(f"[LokiTweetScraper] Scraped data is not a dictionary (or is None).")
        # --- END DEBUGGING ---

        if scraped_data_dict:
            print(f"[LokiTweetScraper] Successfully scraped and parsed data. Attempting JSON conversion.")
            # ComfyUI primarily works with basic types; return JSON string
            try:
                json_output = json.dumps(scraped_data_dict, indent=4)
                print(f"[LokiTweetScraper] JSON conversion successful. Output length: {len(json_output)}") # DEBUG
                return (json_output,)
            except Exception as e:
                print(f"[LokiTweetScraper] Error converting scraped data to JSON: {e}")
                # Return an empty JSON object string or similar indicator of error
                return ("{}",)
        else:
            print("[LokiTweetScraper] Scraping failed (scrape_tweet_data returned None or empty).")
            # Return an empty JSON object string or similar indicator of failure
            return ("{}",) 

# Dictionary that ComfyUI uses to map node names to classes
# NODE_CLASS_MAPPINGS = {
#     "LokiTweetScraper": LokiTweetScraper
# }

# # A dictionary that contains the friendly/humanly readable titles for the nodes
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "LokiTweetScraper": "🐦📜 Scrape Tweet (LOKI)"
# } 