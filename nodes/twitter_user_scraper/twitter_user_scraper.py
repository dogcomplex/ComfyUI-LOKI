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

def scrape_user_profile_and_tweets(profile_url: str, headless: bool = True) -> Optional[Dict]:
    """
    Scrapes public user profile data AND the initially visible tweets from a given URL.
    Returns a combined dictionary: {'profile': {...}, 'tweets': [...]}
    """
    profile_xhr_calls = []
    tweets_xhr_calls = []
    
    profile_data = None
    initial_tweets = []

    def intercept_response(response):
        """Capture relevant background requests for profile and tweets."""
        nonlocal profile_xhr_calls, tweets_xhr_calls
        try:
            # Profile Data Endpoints
            if response.request.resource_type == "xhr" and ("UserByScreenName" in response.url or "UserByRestId" in response.url):
                print(f"[Scraper Debug] Intercepted Profile XHR: {response.url}")
                profile_xhr_calls.append(response)
            # Initial Tweets Endpoint (based on user finding)
            elif response.request.resource_type == "xhr" and "/UserTweets" in response.url:
                 print(f"[Scraper Debug] Intercepted Tweets XHR: {response.url}")
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
                 print("Profile container likely loaded. Waiting for XHRs...")
                 page.wait_for_timeout(7000) # Slightly longer wait to catch both types of XHR
            except Exception as e:
                 print(f"Timeout or error waiting for selector: {e}. Proceeding.")

            # --- Process Profile XHRs --- 
            if not profile_xhr_calls:
                print("No relevant User Profile XHR calls intercepted.")
            else:
                print(f"[Scraper Debug] Processing {len(profile_xhr_calls)} Profile XHR calls.")
                for xhr in reversed(profile_xhr_calls):
                    print(f"[Scraper Debug] Analyzing Profile XHR: {xhr.url}")
                    try:
                        data = xhr.json()
                        user_payload = jmespath.search("data.user.result", data)
                        if user_payload:
                            print(f"[Scraper Debug] Found user payload in {xhr.url}")
                            parsed_profile = parse_user(user_payload)
                            if parsed_profile and not parsed_profile.get("error"):
                                profile_data = parsed_profile # Store the valid profile
                                print("[Scraper Debug] Successfully parsed valid user profile data.")
                                break # Found profile, stop checking profile XHRs
                    except Exception as e:
                        print(f"[Scraper Debug] Error processing Profile XHR {xhr.url}: {e}")
            
            # --- Process Tweets XHRs (Using Python traversal) --- 
            if not tweets_xhr_calls:
                 print("No relevant User Tweets XHR calls intercepted.")
            else:
                 print(f"[Scraper Debug] Processing {len(tweets_xhr_calls)} UserTweets XHR calls.")
                 for xhr in reversed(tweets_xhr_calls):
                      print(f"[Scraper Debug] Analyzing Tweets XHR: {xhr.url}")
                      try:
                          data = xhr.json()
                          
                          # --- Use Python Recursive Search for Tweets --- 
                          potential_tweet_payloads = find_objects_by_typename(data, "Tweet")
                          # --- End Python Recursive Search --- 
                          
                          if not potential_tweet_payloads:
                              print("[Scraper Debug] No potential tweet results found via recursive search in this Tweets XHR.")
                              continue
                          
                          print(f"[Scraper Debug] Found {len(potential_tweet_payloads)} potential tweet results via recursive search in {xhr.url}.")
                          tweet_payloads = potential_tweet_payloads # Already filtered slightly by helper
                                
                          if tweet_payloads:
                              print(f"[Scraper Debug] Processing {len(tweet_payloads)} plausible tweet payloads from this XHR.")
                              for payload in tweet_payloads:
                                   parsed = parse_tweet(payload)
                                   if parsed and parsed.get('id'):
                                       if not any(t['id'] == parsed['id'] for t in initial_tweets):
                                           initial_tweets.append(parsed)
                              if initial_tweets:
                                   print(f"[Scraper Debug] Added/updated {len(initial_tweets)} unique tweets from {xhr.url}.")
                                   # Optionally break if only one XHR usually contains tweets
                                   # break 
                                   
                      except json.JSONDecodeError:
                          print(f"[Scraper Debug] Could not decode JSON from Tweets XHR: {xhr.url}")
                      except Exception as e:
                          print(f"[Scraper Debug] Error processing Tweets XHR {xhr.url}: {e}")

            browser.close()

    except Exception as e:
        print(f"Playwright error during navigation or setup: {e}")
        try:
            if 'browser' in locals() and hasattr(browser, 'close'): browser.close()
        except Exception as close_err: print(f"Error closing browser: {close_err}")
        return None # Indicate failure

    # --- Combine Results --- 
    if profile_data or initial_tweets:
        combined_result = {
            "profile": profile_data or {}, # Use empty dict if profile not found
            "tweets": initial_tweets    # Will be empty list if tweets not found
        }
        print(f"Successfully scraped. Profile found: {bool(profile_data)}, Tweets found: {len(initial_tweets)}")
        return combined_result
    else:
        print(f"Could not find profile or initial tweets.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape public profile data from an X.com user URL.')
    parser.add_argument('url', type=str, help='The URL of the user profile to scrape (e.g., https://x.com/elonmusk).')
    parser.add_argument('--output', type=str, default='user_profile_output.json', help='File path to save the output JSON.')
    parser.add_argument('--visible', action='store_true', help='Run the browser in visible mode.')
    args = parser.parse_args()

    print(f"Attempting to scrape profile and initial tweets: {args.url}")
    scraped_data = scrape_user_profile_and_tweets(args.url, headless=not args.visible)

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