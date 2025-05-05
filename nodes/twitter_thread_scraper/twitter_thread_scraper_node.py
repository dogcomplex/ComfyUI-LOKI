import json
from .twitter_thread_scraper import scrape_thread_data # Import from the thread scraper script
from typing import List, Dict

class TwitterThreadScraper:
    """ 
    LOKI Node: Scrapes tweet data from an entire X.com (Twitter) thread using Playwright.
    Input: thread_start_url (STRING), max_tweets (INT)
    Output: thread_data_json (STRING - JSON formatted list)
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "thread_start_url": ("STRING", {"multiline": False, "default": ""}),
                "max_tweets": ("INT", {"default": 10, "min": 1, "max": 100}), # Add reasonable limits
            },
            "optional": {
                 "run_headless": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("thread_data_json",)
    FUNCTION = "scrape_thread"
    CATEGORY = "LOKI 🦊/Web"
    OUTPUT_NODE = True

    def scrape_thread(self, thread_start_url: str, max_tweets: int, run_headless: bool = True):
        print(f"[LokiThreadScraper] Attempting to scrape thread: {thread_start_url} (max: {max_tweets})")
        scraped_thread_list: Optional[List[Dict]] = scrape_thread_data(
            thread_start_url, 
            max_tweets=max_tweets, 
            headless=run_headless
        )

        # --- Basic Debugging --- 
        print(f"[LokiThreadScraper] Raw data returned from scrape_thread_data: {type(scraped_thread_list)}")
        if isinstance(scraped_thread_list, list):
            print(f"[LokiThreadScraper] Number of tweets returned: {len(scraped_thread_list)}")
        # --- End Debugging ---

        if scraped_thread_list:
            print(f"[LokiThreadScraper] Successfully scraped thread data. Attempting JSON conversion.")
            try:
                # Output the list of tweet dicts as a JSON string
                json_output = json.dumps(scraped_thread_list, indent=4)
                print(f"[LokiThreadScraper] JSON conversion successful. Output length: {len(json_output)}")
                return (json_output,)
            except Exception as e:
                print(f"[LokiThreadScraper] Error converting scraped thread data to JSON: {e}")
                return ("[]",) # Return empty JSON list string on error
        else:
            print("[LokiThreadScraper] Thread scraping failed (scrape_thread_data returned None or empty list).")
            return ("[]",) # Return empty JSON list string on failure 