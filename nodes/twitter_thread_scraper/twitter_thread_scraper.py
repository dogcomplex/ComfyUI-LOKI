import json
import jmespath
from playwright.sync_api import sync_playwright
import argparse
from typing import Dict, List, Optional

# --- Reusing parsing functions from twitter_scraper ---
# (Ideally, these would be in a shared utility file)
def parse_user(data: Dict) -> Dict:
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
        # Ensure result is a dict even if search fails
        result = result if isinstance(result, dict) else {}
        result["id"] = data.get("id")
        result["rest_id"] = data.get("rest_id")
        result["is_blue_verified"] = data.get("is_blue_verified")
    else:
        print(f"Warning: Unexpected user data structure: {data.get('__typename')}")
        result = {}
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
        text: legacy.full_text,
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

    user_results = core.get("user_results", {}).get("result", {})
    result["user"] = parse_user(user_results) if user_results else {}

    for key in ["attached_urls", "attached_urls2", "attached_media", "tagged_users", "tagged_hashtags"]:
        if result.get(key) is None: result[key] = [] # Ensure lists are lists

    return result
# --- End of reused parsing functions ---


def scrape_thread_data(url: str, max_tweets: int = 10, headless: bool = True) -> Optional[List[Dict]]:
    """
    Scrape a Twitter thread starting from the given URL.
    Returns a list of parsed tweet dictionaries.
    """
    _xhr_calls = []
    thread_tweets = None
    start_tweet_id = url.split('/')[-1].split('?')[0] # Extract tweet ID from URL
    original_author_id = None

    def intercept_response(response):
        try:
            # --- DEBUG: Log all XHR --- 
            if response.request.resource_type == "xhr":
                print(f"[Scraper Debug] Intercepted XHR: {response.url}") 
            # --- END DEBUG ---

            # Target the endpoint known to contain tweet details / conversation
            if response.request.resource_type == "xhr" and ("TweetResultByRestId" in response.url or "TweetDetail" in response.url):
                # print(f"DEBUG: Adding relevant XHR: {response.url}") # Keep this commented unless needed
                _xhr_calls.append(response)
        except Exception as e:
            print(f"Error intercepting response: {e}")
        return response

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=headless)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.on("response", intercept_response)

            print(f"Navigating to thread start: {url}...")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            print("Waiting for tweet selector...")
            try:
                 page.wait_for_selector("div[data-testid='primaryColumn']", timeout=30000)
                 print("Initial tweet container loaded. Waiting briefly...")
                 page.wait_for_timeout(5000) # Initial wait 

                 # --- ADD SCROLLING (Multiple) --- 
                 scroll_attempts = 3
                 for i in range(scroll_attempts):
                     print(f"[Scraper Debug] Scrolling down attempt {i+1}/{scroll_attempts}...")
                     page.evaluate("window.scrollBy(0, window.innerHeight * 1.5)") # Scroll down 1.5 viewports
                     print(f"[Scraper Debug] Waiting after scroll {i+1}...")
                     page.wait_for_timeout(3000) # Wait a bit after each scroll
                 print("[Scraper Debug] Finished scrolling attempts. Waiting a final time...")
                 page.wait_for_timeout(5000) # Longer final wait
                 # --- END SCROLLING --- 

                 print("Processing XHR calls after scrolling.")
            except Exception as e:
                 print(f"Timeout or error waiting for selector/scroll: {e}. Proceeding.")

            # Process XHR calls to find the thread data
            if not _xhr_calls:
                print("No relevant XHR calls (TweetResultByRestId/TweetDetail) intercepted.")
            else:
                print(f"[Scraper Debug] Processing {_xhr_calls} relevant XHR calls.")
                all_potential_tweet_payloads = [] # Store raw payloads from all relevant XHRs
                original_author_id = None # Reset before loop
                start_tweet_payload = None # Reset before loop

                # --- Pass 1: Find Start Tweet & Author ID, Collect all potential payloads --- 
                for i, xhr in enumerate(reversed(_xhr_calls)):
                    print(f"[Scraper Debug] --- Analyzing XHR Call #{len(_xhr_calls)-i} (URL: {xhr.url}) --- First Pass --- ")
                    try:
                        data = xhr.json()
                        # Collect *all* tweet-like objects from this XHR's known structures
                        current_xhr_payloads = jmespath.search("data.threaded_conversation_with_injections_v2.instructions[?type=='TimelineAddEntries'].entries[].content.itemContent.tweet_results.result || data.tweetResult.result || []", data)
                        # Flatten potential nested lists/results
                        if isinstance(current_xhr_payloads, list):
                            all_potential_tweet_payloads.extend([p for p in current_xhr_payloads if p and p.get("__typename") == "Tweet"])
                        elif current_xhr_payloads and current_xhr_payloads.get("__typename") == "Tweet":
                             all_potential_tweet_payloads.append(current_xhr_payloads)
                        
                        # Find the starting tweet specifically within this XHR to get author ID (only need once)
                        if not original_author_id:
                            query = f"data.threaded_conversation_with_injections_v2.instructions[?type=='TimelineAddEntries'].entries[?entryId=='tweet-{start_tweet_id}'].content.itemContent.tweet_results.result || data.tweetResult.result"
                            found_payload = jmespath.search(query, data)
                            if isinstance(found_payload, list):
                                found_payload = found_payload[0] if found_payload else None
                            
                            if found_payload and found_payload.get("__typename") == "Tweet":
                                start_tweet_payload = found_payload # Keep track of the specific start payload
                                author_info = start_tweet_payload.get('core', {}).get('user_results', {}).get('result', {})
                                original_author_id = author_info.get('rest_id')
                                print(f"[Scraper Debug] Found starting tweet in {xhr.url}. Extracted original_author_id: {original_author_id}")

                    except json.JSONDecodeError:
                        print(f"[Scraper Debug] Could not decode JSON from XHR: {xhr.url}")
                    except Exception as e:
                        print(f"[Scraper Debug] Error processing XHR call (Pass 1) from {xhr.url}: {e}")
                # --- End Pass 1 --- 

                # --- Pass 2: Parse all collected payloads and reconstruct thread --- 
                if original_author_id and all_potential_tweet_payloads:
                     print(f"[Scraper Debug] --- Reconstructing Thread --- Found {len(all_potential_tweet_payloads)} potential tweet payloads across all XHRs. Author ID: {original_author_id}")
                     parsed_tweets = {} # {tweet_id: parsed_data}
                     for tweet_payload in all_potential_tweet_payloads:
                          parsed = parse_tweet(tweet_payload)
                          if parsed and parsed.get('id') and parsed['id'] not in parsed_tweets: # Avoid duplicates
                               parsed_tweets[parsed['id']] = parsed
                     
                     # Reconstruct logic (simplified - assuming parsed_tweets now holds all candidates)
                     thread_result = []
                     current_tweet_id = start_tweet_id
                     processed_ids = set()

                     while current_tweet_id in parsed_tweets and len(thread_result) < max_tweets and current_tweet_id not in processed_ids:
                          current_tweet_data = parsed_tweets[current_tweet_id]
                          thread_result.append(current_tweet_data)
                          processed_ids.add(current_tweet_id)

                          # Heuristic: Find the *first* subsequent tweet in our parsed list by the same author
                          # This relies on the assumption that timeline entries often preserve some order
                          found_current = False
                          next_tweet_id = None
                          for tweet_id, tweet_data in parsed_tweets.items():
                               if tweet_id == current_tweet_id:
                                    found_current = True
                                    continue
                               if found_current and tweet_data.get('user',{}).get('rest_id') == original_author_id and tweet_id not in processed_ids:
                                    next_tweet_id = tweet_id
                                    break # Take the first one found after the current one
                          
                          if next_tweet_id:
                               current_tweet_id = next_tweet_id
                          else:
                               break # No further tweet by author found

                     thread_tweets = thread_result # Assign the final reconstructed list
                     if thread_tweets:
                         print(f"[Scraper Debug] Successfully reconstructed thread with {len(thread_tweets)} tweets.")
                     else:
                          print("[Scraper Debug] Failed to reconstruct thread from parsed tweets.")

                elif not original_author_id:
                     print("[Scraper Debug] Could not find original author ID in any relevant XHR call.")
                elif not all_potential_tweet_payloads:
                     print("[Scraper Debug] No tweet payloads were collected from relevant XHR calls.")
                # --- End Pass 2 --- 

            browser.close()

    except Exception as e:
        print(f"Playwright error during navigation or setup: {e}")
        try:
            if 'browser' in locals() and hasattr(browser, 'close'): browser.close()
        except Exception as close_err: print(f"Error closing browser: {close_err}")
        return None

    if thread_tweets:
        print(f"Returning thread with {len(thread_tweets)} tweets (max requested: {max_tweets}).")
        return thread_tweets
    else:
        print("Could not find valid thread data in any intercepted XHR call.")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape a Twitter thread starting from a specific tweet URL.')
    parser.add_argument('url', type=str, help='The URL of the first tweet in the thread.')
    parser.add_argument('--max', type=int, default=10, help='Maximum number of tweets to scrape from the thread.')
    parser.add_argument('--output', type=str, default='thread_output.json', help='File path to save the output JSON list.')
    parser.add_argument('--visible', action='store_true', help='Run the browser in visible mode.')
    args = parser.parse_args()

    print(f"Attempting to scrape thread from: {args.url} (max: {args.max})")
    scraped_thread = scrape_thread_data(args.url, max_tweets=args.max, headless=not args.visible)

    if scraped_thread:
        print(f"Successfully scraped thread. Saving {len(scraped_thread)} tweets to {args.output}")
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(scraped_thread, f, ensure_ascii=False, indent=4)
            print("Output saved.")
        except Exception as e:
            print(f"Error saving output to {args.output}: {e}")
    else:
        print("Thread scraping failed.") 