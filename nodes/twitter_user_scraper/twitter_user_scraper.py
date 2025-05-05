import json
import jmespath
from playwright.sync_api import sync_playwright
import argparse
from typing import Dict, Optional, List, Tuple, Any

# --- Reusing parsing function from twitter_scraper --- 
# (Ideally, this would be in a shared utility file)
def parse_user(data: Dict) -> Dict:
    """Parses the user data from the GraphQL response."""
    if data.get("__typename") == "User":
        legacy = data.get("legacy", {})
        result = jmespath.search(
            """{
            created_at: created_at, default_profile: default_profile, description: description,
            entities: entities, fast_followers_count: fast_followers_count, favourites_count: favourites_count,
            followers_count: followers_count, friends_count: friends_count, has_custom_timelines: has_custom_timelines,
            is_translator: is_translator, listed_count: listed_count, location: location,
            media_count: media_count, name: name, normal_followers_count: normal_followers_count,
            pinned_tweet_ids_str: pinned_tweet_ids_str, possibly_sensitive: possibly_sensitive,
            profile_banner_url: profile_banner_url, profile_image_url_https: profile_image_url_https,
            screen_name: screen_name, statuses_count: statuses_count, translator_type: translator_type,
            verified: verified, want_retweets: want_retweets, withheld_in_countries: withheld_in_countries
        }""",
            legacy,
        )
        result = result if isinstance(result, dict) else {}
        result["id"] = data.get("id") # GraphQL ID
        result["rest_id"] = data.get("rest_id") # Numeric ID
        result["is_blue_verified"] = data.get("is_blue_verified")
        # Add potentially missing professional details
        professional = data.get("professional", {})
        result["professional_type"] = professional.get("professional_type")
        result["category"] = professional.get("category", []) 
        
    elif data.get("__typename") == "UserUnavailable":
         print("User unavailable (suspended, deleted, etc.)")
         result = {"error": "UserUnavailable", "message": data.get("reason")}
    else:
        print(f"Warning: Unexpected user data type: {data.get('__typename')}")
        result = {"error": "UnknownDataType", "type": data.get('__typename')}
    return result

def parse_tweet(data: Dict) -> Dict:
    """Parse Twitter tweet JSON dataset for the most important fields"""
    legacy = data.get("legacy", {})
    core = data.get("core", {})
    card = data.get("card", {})
    views = data.get("views", {})

    result = jmespath.search(
        """{
        created_at: legacy.created_at,
        attached_urls: legacy.entities.urls[].expanded_url,
        attached_urls2: legacy.entities.url.urls[].expanded_url,
        attached_media: legacy.entities.media[].media_url_https,
        tagged_users: legacy.entities.user_mentions[].screen_name,
        tagged_hashtags: legacy.entities.hashtags[].text,
        favorite_count: legacy.favorite_count,
        bookmark_count: legacy.bookmark_count,
        quote_count: legacy.quote_count,
        reply_count: legacy.reply_count,
        retweet_count: legacy.retweet_count,
        text: note_tweet.note_tweet_results.result.text || legacy.full_text,
        is_quote: legacy.is_quote_status,
        is_retweet: legacy.retweeted,
        language: legacy.lang,
        user_id: legacy.user_id_str,
        id: legacy.id_str,
        conversation_id: legacy.conversation_id_str,
        source: source,
        views: views.count
    }""",
        data,
    )

    expected_keys = [
        "created_at", "attached_urls", "attached_urls2", "attached_media",
        "tagged_users", "tagged_hashtags", "favorite_count", "bookmark_count",
        "quote_count", "reply_count", "retweet_count", "text", "is_quote",
        "is_retweet", "language", "user_id", "id", "conversation_id", "source", "views"
    ]
    if result is None: result = {}
    for key in expected_keys:
        if key not in result:
            result[key] = None # Default for missing values

    result["poll"] = {}
    poll_data = jmespath.search("card.legacy.binding_values", data) or []
    for poll_entry in poll_data:
        key, value_dict = poll_entry.get("key"), poll_entry.get("value")
        if not key or not value_dict: continue
        if "choice" in key and "string_value" in value_dict: result["poll"][key] = value_dict["string_value"]
        elif "end_datetime" in key and "string_value" in value_dict: result["poll"]["end"] = value_dict["string_value"]
        elif "last_updated_datetime" in key and "string_value" in value_dict: result["poll"]["updated"] = value_dict["string_value"]
        elif "counts_are_final" in key and "boolean_value" in value_dict: result["poll"]["ended"] = value_dict["boolean_value"]
        elif "duration_minutes" in key and "string_value" in value_dict: result["poll"]["duration"] = value_dict["string_value"]

    # Use the existing parse_user, assuming it might be nested within tweet data sometimes
    user_results = core.get("user_results", {}).get("result", {})
    result["user"] = parse_user(user_results) if user_results else {}

    for key in ["attached_urls", "attached_urls2", "attached_media", "tagged_users", "tagged_hashtags"]:
        if result.get(key) is None: result[key] = [] # Ensure lists are lists

    return result
# --- End of reused parsing functions ---

# --- NEW: Helper function for recursive search --- 
def find_objects_by_typename(data: Any, target_typename: str) -> List[Dict]:
    """Recursively search dicts/lists for objects with a specific __typename."""
    found_objects = []
    if isinstance(data, dict):
        if data.get("__typename") == target_typename:
            # Basic check to see if it looks like a tweet payload
            if target_typename == "Tweet" and (data.get("legacy") or data.get("core")):
                 found_objects.append(data)
            # Add checks for other typenames if needed later
            # elif target_typename == "SomeOtherType" and ...:
            #     found_objects.append(data)
            
        for key, value in data.items():
            found_objects.extend(find_objects_by_typename(value, target_typename))
            
    elif isinstance(data, list):
        for item in data:
            found_objects.extend(find_objects_by_typename(item, target_typename))
            
    return found_objects
# --- END Helper function ---

def scrape_user_profile_and_tweets(profile_url: str, max_tweets: int = 20, headless: bool = True) -> Optional[Dict]:
    """
    Scrapes public user profile data AND tweets from a user's profile page,
    simulating scrolling to potentially capture more than the initial batch.
    Returns a combined dictionary: {'profile': {...}, 'tweets': [...]}
    """
    profile_xhr_calls = []
    tweets_xhr_calls = []
    
    profile_data = None
    initial_tweets = []

    def intercept_response(response):
        nonlocal profile_xhr_calls, tweets_xhr_calls
        try:
            if response.request.resource_type == "xhr" and ("UserByScreenName" in response.url or "UserByRestId" in response.url):
                # print(f"[Scraper Info] Intercepted Profile XHR: {response.url}") # Optional Info
                profile_xhr_calls.append(response)
            elif response.request.resource_type == "xhr" and "/UserTweets" in response.url:
                 # print(f"[Scraper Info] Intercepted Tweets XHR: {response.url}") # Optional Info
                 tweets_xhr_calls.append(response)
        except Exception as e:
            print(f"Error intercepting response: {e}")
        return response

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=headless)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.on("response", intercept_response)

            print(f"Navigating to profile: {profile_url}...")
            page.goto(profile_url, wait_until="domcontentloaded", timeout=60000)
            print("Waiting for profile content selector...")
            try:
                 page.wait_for_selector("div[data-testid='primaryColumn']", timeout=30000)
                 print("Initial profile container loaded. Waiting briefly...")
                 page.wait_for_timeout(5000) # Initial wait 

                 # --- RE-ADD SCROLLING --- 
                 scroll_attempts = 10 
                 print(f"[Scraper Debug] Will attempt up to {scroll_attempts} scrolls to find up to {max_tweets} tweets.")
                 consecutive_scrolls_with_no_new_tweets = 0 # Counter for early stopping
                 
                 for i in range(scroll_attempts):
                     # --- Process currently intercepted XHRs --- 
                     current_tweet_count = len(initial_tweets)
                     # --- Process Profile XHRs (Subset - only find profile once) ---
                     if not profile_data and profile_xhr_calls: 
                         # ... (Same profile processing logic as before, only run once) ...
                         for xhr in reversed(profile_xhr_calls): 
                             try: 
                                 data = xhr.json() 
                                 user_payload = jmespath.search("data.user.result", data) 
                                 if user_payload: 
                                     parsed_profile = parse_user(user_payload) 
                                     if parsed_profile and not parsed_profile.get("error"): 
                                         profile_data = parsed_profile 
                                         print("Successfully parsed valid user profile data.") 
                                         break 
                             except Exception as e: print(f"Error processing Profile XHR {xhr.url}: {e}") 
                         profile_xhr_calls = [] # Clear processed profile calls
                         
                     # --- Process Tweets XHRs (Incremental) --- 
                     if tweets_xhr_calls: 
                         print(f"[Scraper Debug] Processing {len(tweets_xhr_calls)} new Tweets XHRs before scroll {i+1}...")
                         new_tweets_in_batch = 0
                         for xhr in reversed(tweets_xhr_calls): 
                             if len(initial_tweets) >= max_tweets: break 
                             try: 
                                 data = xhr.json() 
                                 payloads = find_objects_by_typename(data, "Tweet") 
                                 if payloads: 
                                     for p in payloads: 
                                         if len(initial_tweets) >= max_tweets: break 
                                         parsed = parse_tweet(p) 
                                         if parsed and parsed.get('id') and not any(t['id'] == parsed['id'] for t in initial_tweets): 
                                             initial_tweets.append(parsed) 
                                             new_tweets_in_batch += 1
                             except Exception as e: print(f"Error processing Tweets XHR {xhr.url}: {e}") 
                         if new_tweets_in_batch > 0: 
                             print(f"[Scraper Debug] Added {new_tweets_in_batch} tweets from recent XHRs. Total now: {len(initial_tweets)}.")
                         tweets_xhr_calls = [] # Clear processed tweet calls for this iteration

                     tweets_added_this_iteration = len(initial_tweets) - current_tweet_count
                     
                     # --- Early stopping logic --- 
                     if tweets_added_this_iteration == 0:
                         consecutive_scrolls_with_no_new_tweets += 1
                         print(f"[Scraper Debug] No new tweets found in XHRs after scroll {i}. ({consecutive_scrolls_with_no_new_tweets} consecutive)")
                     else:
                         consecutive_scrolls_with_no_new_tweets = 0 # Reset counter if new tweets found

                     if consecutive_scrolls_with_no_new_tweets >= 2:
                         print("[Scraper Debug] Stopping scroll early: No new tweets found in last 2 attempts.")
                         break
                     # --- End Early stopping --- 
                         
                     # --- Now check max_tweets limit and scroll --- 
                     if len(initial_tweets) >= max_tweets:
                         print(f"[Scraper Debug] Reached max_tweets ({max_tweets}). Stopping scroll loop.") # Changed log slightly
                         break 
                         
                     print(f"[Scraper Debug] Scrolling down attempt {i+1}/{scroll_attempts} (currently have {len(initial_tweets)} tweets)...")
                     page.evaluate("window.scrollTo(0, document.body.scrollHeight)") # Scroll to bottom
                     print(f"[Scraper Debug] Waiting after scroll {i+1}...")
                     page.wait_for_timeout(5000) # Longer wait after scroll
                     
                 if len(initial_tweets) < max_tweets and consecutive_scrolls_with_no_new_tweets < 2:
                    print("[Scraper Debug] Finished scroll attempts loop. Processing any remaining XHRs...")
                 # --- END SCROLLING --- 

                 print(f"Finished scroll/load phase. Processing final XHRs...") # Updated log
            except Exception as e:
                 print(f"Timeout or error waiting for selector/scroll: {e}. Proceeding with captured XHRs.")

            # --- Final XHR Processing (ensure everything caught is processed) --- 
            # Process profile one last time if missed
            if not profile_data and profile_xhr_calls:
                # ... (Same profile processing logic as above) ...
                 for xhr in reversed(profile_xhr_calls): 
                     try: 
                         data = xhr.json() 
                         user_payload = jmespath.search("data.user.result", data) 
                         if user_payload: 
                             parsed_profile = parse_user(user_payload) 
                             if parsed_profile and not parsed_profile.get("error"): 
                                 profile_data = parsed_profile 
                                 print("Successfully parsed valid user profile data (final check).") 
                                 break 
                     except Exception as e: print(f"Error processing Profile XHR {xhr.url} (final check): {e}") 

            # Process tweets one last time
            if tweets_xhr_calls:
                print(f"[Scraper Debug] Final processing of {len(tweets_xhr_calls)} remaining Tweets XHRs...")
                new_tweets_in_batch = 0
                for xhr in reversed(tweets_xhr_calls):
                     if len(initial_tweets) >= max_tweets: break
                     try: 
                         data = xhr.json() 
                         payloads = find_objects_by_typename(data, "Tweet") 
                         if payloads: 
                             for p in payloads: 
                                 if len(initial_tweets) >= max_tweets: break 
                                 parsed = parse_tweet(p) 
                                 if parsed and parsed.get('id') and not any(t['id'] == parsed['id'] for t in initial_tweets): 
                                     initial_tweets.append(parsed) 
                                     new_tweets_in_batch +=1
                     except Exception as e: print(f"Error processing Tweets XHR {xhr.url} (final check): {e}") 
                if new_tweets_in_batch > 0:
                    print(f"[Scraper Debug] Added {new_tweets_in_batch} tweets from final XHR processing. Final total: {len(initial_tweets)}.")
            # --- End Final XHR Processing ---

            browser.close()

    except Exception as e:
        print(f"Playwright error during navigation or setup: {e}")
        try:
            if 'browser' in locals() and hasattr(browser, 'close'): browser.close()
        except Exception as close_err: print(f"Error closing browser: {close_err}")
        return None # Indicate failure

    # --- Combine Results (Sort and Trim) --- 
    if profile_data or initial_tweets:
        # Sort tweets by date (newest first) before trimming
        try:
            initial_tweets.sort(key=lambda t: t.get('created_at', ''), reverse=True)
        except Exception as sort_e:
             print(f"[Scraper Warning] Could not sort tweets by date: {sort_e}")
             
        # Trim to max_tweets
        trimmed_tweets = initial_tweets[:max_tweets]
        
        combined_result = {
            "profile": profile_data or {},
            "tweets": trimmed_tweets 
        }
        print(f"Successfully scraped. Profile found: {bool(profile_data)}, Tweets returned: {len(trimmed_tweets)} (max requested: {max_tweets})")
        return combined_result
    else:
        print(f"Could not find profile or initial tweets.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape public profile data and recent tweets from an X.com user URL.')
    parser.add_argument('url', type=str, help='The URL of the user profile to scrape.')
    parser.add_argument('--max_tweets', type=int, default=20, help='Maximum number of tweets to attempt to scrape.')
    parser.add_argument('--output', type=str, default='user_profile_output.json', help='File path to save the output JSON.')
    parser.add_argument('--visible', action='store_true', help='Run the browser in visible mode.')
    args = parser.parse_args()

    print(f"Attempting to scrape profile and up to {args.max_tweets} tweets: {args.url}")
    scraped_data = scrape_user_profile_and_tweets(args.url, max_tweets=args.max_tweets, headless=not args.visible)

    if scraped_data:
        print(f"Successfully scraped data. Saving to {args.output}")
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(scraped_data, f, ensure_ascii=False, indent=4)
            print("Output saved.")
        except Exception as e:
            print(f"Error saving output to {args.output}: {e}")
    else:
        print("Profile and initial tweets scraping failed.") 