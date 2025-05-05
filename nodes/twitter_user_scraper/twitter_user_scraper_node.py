import json
from .twitter_user_scraper import scrape_user_profile_and_tweets # Import from the user scraper script
from typing import Optional, Dict

class TwitterUserScraper:
    """ 
    LOKI Node: Scrapes public profile data AND initial tweets for a specific X.com user.
    Input: profile_url (STRING)
    Output: user_data_json (STRING - JSON formatted dict: {'profile':{...}, 'tweets':[...]})
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "profile_url": ("STRING", {"multiline": False, "default": "https://x.com/Scrapfly_dev"}),
                "max_tweets": ("INT", {"default": 20, "min": 1, "max": 200}),
            },
             "optional": {
                 "run_headless": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("user_data_json",)
    FUNCTION = "scrape_user_and_tweets"
    CATEGORY = "LOKI 🦊/Web"
    OUTPUT_NODE = True

    def scrape_user_and_tweets(self, profile_url: str, max_tweets: int, run_headless: bool = True):
        print(f"[LokiUserScraper] Attempting to scrape profile & up to {max_tweets} tweets: {profile_url}")
        scraped_combined_dict: Optional[Dict] = scrape_user_profile_and_tweets(
            profile_url, 
            max_tweets=max_tweets,
            headless=run_headless
        )

        # --- Basic Debugging --- 
        print(f"[LokiUserScraper] Raw data returned from scrape_user_profile_and_tweets: {type(scraped_combined_dict)}")
        # --- End Debugging ---

        if scraped_combined_dict:
            profile_found = bool(scraped_combined_dict.get("profile"))
            tweets_found = len(scraped_combined_dict.get("tweets", []))
            print(f"[LokiUserScraper] Successfully scraped data (Profile: {profile_found}, Tweets: {tweets_found}). Attempting JSON conversion.")
            try:
                json_output = json.dumps(scraped_combined_dict, indent=4)
                print(f"[LokiUserScraper] JSON conversion successful. Output length: {len(json_output)}")
                return (json_output,)
            except Exception as e:
                print(f"[LokiUserScraper] Error converting scraped data to JSON: {e}")
                return ("{}",) # Return empty JSON object string on error
        else:
            print("[LokiUserScraper] Profile and initial tweets scraping failed.")
            return ("{}",) # Return empty JSON object string on failure 