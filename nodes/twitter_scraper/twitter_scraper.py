import json
import jmespath
from playwright.sync_api import sync_playwright
import argparse
import os
import sys
from typing import Dict, List

# Jmespath parsing functions adapted from how_to.txt
# Note: User parsing is included as parse_tweet calls it, but it's not strictly needed
# if only scraping a single tweet's direct data.
def parse_user(data: Dict) -> Dict:
    if data.get("__typename") == "User":
        legacy = data.get("legacy", {})
        result = jmespath.search(
            """{
            created_at: created_at,
            default_profile: default_profile,
            description: description,
            entities: entities,
            fast_followers_count: fast_followers_count,
            favourites_count: favourites_count,
            followers_count: followers_count,
            friends_count: friends_count,
            has_custom_timelines: has_custom_timelines,
            is_translator: is_translator,
            listed_count: listed_count,
            location: location,
            media_count: media_count,
            name: name,
            normal_followers_count: normal_followers_count,
            pinned_tweet_ids_str: pinned_tweet_ids_str,
            possibly_sensitive: possibly_sensitive,
            profile_banner_url: profile_banner_url,
            profile_image_url_https: profile_image_url_https,
            screen_name: screen_name,
            statuses_count: statuses_count,
            translator_type: translator_type,
            verified: verified,
            want_retweets: want_retweets,
            withheld_in_countries: withheld_in_countries
        }""",
            legacy,
        )
        result["id"] = data.get("id")
        result["rest_id"] = data.get("rest_id")
        result["is_blue_verified"] = data.get("is_blue_verified")
    else:
        # Handle cases where user data might be missing or in a different format
        # For now, returning an empty dict or logging a warning might be appropriate
        print(f"Warning: Unexpected user data structure: {data.get('__typename')}")
        result = {}
    return result

def parse_tweet(data: Dict) -> Dict:
    """Parse Twitter tweet JSON dataset for the most important fields"""
    # print(f"DEBUG: Parsing tweet data: {json.dumps(data, indent=2)}") # DEBUG
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
        data, # Note: the original code passed `data`, not `legacy` here. Corrected based on structure.
    )

    # Ensure keys exist even if values are null/missing from jmespath search
    expected_keys = [
        "created_at", "attached_urls", "attached_urls2", "attached_media",
        "tagged_users", "tagged_hashtags", "favorite_count", "bookmark_count",
        "quote_count", "reply_count", "retweet_count", "text", "is_quote",
        "is_retweet", "language", "user_id", "id", "conversation_id", "source", "views"
    ]
    if result is None:
        result = {}
    for key in expected_keys:
        if key not in result:
            result[key] = None # Or appropriate default (e.g., [] for lists, 0 for counts)

    result["poll"] = {}
    poll_data = jmespath.search("card.legacy.binding_values", data) or []
    for poll_entry in poll_data:
        key, value_dict = poll_entry.get("key"), poll_entry.get("value")
        if not key or not value_dict:
            continue

        if "choice" in key and "string_value" in value_dict:
            result["poll"][key] = value_dict["string_value"]
        elif "end_datetime" in key and "string_value" in value_dict:
            result["poll"]["end"] = value_dict["string_value"]
        elif "last_updated_datetime" in key and "string_value" in value_dict:
            result["poll"]["updated"] = value_dict["string_value"]
        elif "counts_are_final" in key and "boolean_value" in value_dict:
            result["poll"]["ended"] = value_dict["boolean_value"]
        elif "duration_minutes" in key and "string_value" in value_dict:
            result["poll"]["duration"] = value_dict["string_value"]

    # Extract user details
    user_results = data.get("core", {}).get("user_results", {}).get("result", {})
    if user_results:
        result["user"] = parse_user(user_results)
    else:
        result["user"] = {}

    # Clean up potentially null list entries from jmespath
    for key in ["attached_urls", "attached_urls2", "attached_media", "tagged_users", "tagged_hashtags"]:
        if result.get(key) is None:
            result[key] = []

    return result

def scrape_tweet_data(url: str, headless: bool = True) -> Dict | None:
    """
    Scrape a single tweet page for Tweet thread details.
    Returns parsed parent tweet data.
    """
    _xhr_calls = []
    tweet_data = None

    def intercept_response(response):
        """capture all background requests and save them"""
        try:
            if response.request.resource_type == "xhr" and "TweetResultByRestId" in response.url:
                # print(f"DEBUG: Intercepted XHR: {response.url}") # DEBUG
                _xhr_calls.append(response)
        except Exception as e:
            print(f"Error intercepting response: {e}")
        return response # Should return response according to Playwright docs

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=headless)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()

            page.on("response", intercept_response)

            print(f"Navigating to {url}...")
            page.goto(url, wait_until="domcontentloaded", timeout=60000) # Increased timeout

            print("Waiting for tweet selector...")
            # Wait for the main tweet content area or a known tweet element
            try:
                 page.wait_for_selector("div[data-testid='primaryColumn']", timeout=30000)
                 page.wait_for_timeout(5000) # Wait for XHR calls
                 print("Tweet container likely loaded. Processing XHR calls.")
            except Exception as e:
                 print(f"Timeout or error waiting for tweet selector: {e}. Proceeding with captured XHR calls if any.")

            # --- Process XHR calls INSIDE the context manager --- START
            if not _xhr_calls:
                print("No relevant XHR calls (TweetResultByRestId) were intercepted.")
            else:
                # Find the main tweet data
                for xhr in reversed(_xhr_calls):
                    try:
                        data = xhr.json()
                        if 'data' in data and 'tweetResult' in data['data'] and 'result' in data['data']['tweetResult']:
                             tweet_payload = data['data']['tweetResult']['result']
                             if tweet_payload.get("__typename") == "Tweet":
                                 print(f"Found main tweet data in {xhr.url}")
                                 tweet_data = tweet_payload
                                 break
                        elif 'data' in data and 'threaded_conversation_with_injections_v2' in data['data']:
                             instructions = data['data']['threaded_conversation_with_injections_v2'].get('instructions', [])
                             for instruction in instructions:
                                  if instruction.get('type') == 'TimelineAddEntries':
                                       entries = instruction.get('entries', [])
                                       for entry in entries:
                                            content = entry.get('content')
                                            if content and content.get('entryType') == 'TimelineTimelineItem':
                                                 item_content = content.get('itemContent')
                                                 if item_content and item_content.get('itemType') == 'TimelineTweet':
                                                      tweet_results = item_content.get('tweet_results', {})
                                                      result = tweet_results.get('result')
                                                      if result and result.get('__typename') == 'Tweet':
                                                          legacy_data = result.get('legacy')
                                                          tweet_id_from_url = url.split('/')[-1].split('?')[0]
                                                          if legacy_data and legacy_data.get('id_str') == tweet_id_from_url:
                                                              print(f"Found main tweet data via TimelineAddEntries in {xhr.url}")
                                                              tweet_data = result
                                                              break
                                       if tweet_data: break
                             if tweet_data: break

                    except Exception as e:
                        # Catch JSON decode errors or other issues for specific XHR
                        print(f"Error processing XHR call from {xhr.url}: {e}")
            # --- Process XHR calls INSIDE the context manager --- END

            browser.close()

    except Exception as e:
        print(f"Playwright error during navigation or setup: {e}")
        # Ensure browser is closed if an error occurs mid-process
        try:
            # Check if browser variable exists and has a close method
            if 'browser' in locals() and hasattr(browser, 'close'):
                browser.close()
        except Exception as close_err:
             print(f"Error trying to close browser after main error: {close_err}")
        return None # Indicate failure

    if tweet_data:
        print("Parsing extracted tweet data...")
        return parse_tweet(tweet_data)
    else:
        print("Could not find valid tweet data in any intercepted XHR call after browser context.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape data from a single X.com (Twitter) tweet URL.')
    parser.add_argument('url', type=str, help='The URL of the tweet to scrape.')
    parser.add_argument('--output', type=str, default=None, help='Output file or directory. If a directory, a default filename is used.')
    parser.add_argument('--visible', action='store_true', help='Run the browser in visible mode (not headless).')
    args = parser.parse_args()

    # Resolve output path: default to <node_folder>/output/tweet_output.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_file = os.path.join(script_dir, 'output', 'tweet_output.json')
    output_arg = args.output
    if output_arg is None:
        resolved_output = default_file
    else:
        # If output is a directory (exists or ends with separator or has no extension), place default filename inside
        is_dir_like = os.path.isdir(output_arg) or output_arg.endswith(os.sep) or os.path.splitext(output_arg)[1] == ''
        resolved_output = os.path.join(output_arg, 'tweet_output.json') if is_dir_like else output_arg

    # Ensure parent directory exists
    try:
        os.makedirs(os.path.dirname(resolved_output), exist_ok=True)
    except Exception as e:
        print(f"Error ensuring output directory exists for {resolved_output}: {e}")
        sys.exit(1)

    print(f"Attempting to scrape: {args.url}")
    scraped_data = scrape_tweet_data(args.url, headless=not args.visible)

    if scraped_data:
        print(f"Successfully scraped and parsed data. Saving to {resolved_output}")
        try:
            with open(resolved_output, 'w', encoding='utf-8') as f:
                json.dump(scraped_data, f, ensure_ascii=False, indent=4)
            print("Output saved.")
            sys.exit(0)
        except Exception as e:
            print(f"Error saving output to {resolved_output}: {e}")
            sys.exit(1)
    else:
        print("Scraping failed.")
        sys.exit(1)