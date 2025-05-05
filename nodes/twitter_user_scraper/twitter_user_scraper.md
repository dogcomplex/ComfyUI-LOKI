# twitter_user_scraper Node Requirements

## DESCRIPTION

Scrapes public profile data AND the most recent ~150 tweets for a specific X.com (Twitter) user using their profile URL. Operates without requiring login.

## INPUTS

- `profile_url` (STRING): The full URL of the target user's profile page (e.g., "https://x.com/someuser").
- `max_tweets` (INT): The maximum number of tweets to attempt to retrieve (default: 50). Note that the actual number returned is often limited by Twitter (~150 for public scraping).
- `run_visible` (BOOLEAN): If true, runs the Playwright browser in non-headless (visible) mode, which can sometimes help bypass anti-bot measures (default: false).

## OUTPUTS

- `user_data` (DICT): A dictionary containing:
    - `profile`: (Dict) Parsed public profile data (name, bio, counts, etc.) or an empty dict if not found.
    - `tweets`: (List[Dict]) A list of dictionaries, each representing a parsed tweet, sorted newest first, up to `max_tweets` or the public limit.

## NODE_STRATEGY

1.  Launches a Playwright browser instance (headless or visible).
2.  Navigates to the provided `profile_url`.
3.  Intercepts background network requests (XHR) specifically listening for:
    - Profile data endpoints (`UserByScreenName`, `UserByRestId`).
    - Tweet data endpoints (`UserTweets`).
4.  Waits for the main profile content to load.
5.  Attempts to scroll down the page (`window.scrollTo(0, document.body.scrollHeight)`) up to 10 times, waiting briefly after each scroll.
6.  Processes intercepted XHR responses after each scroll attempt, parsing profile data (once) and newly found tweets using Jmespath and helper functions (`parse_user`, `parse_tweet`, `find_objects_by_typename`).
7.  Stops scrolling early if the `max_tweets` limit is reached OR if 2 consecutive scroll attempts yield no new tweets.
8.  Performs final processing of any remaining intercepted XHR calls.
9.  Closes the browser.
10. Sorts the collected tweets by `created_at` (descending).
11. Trims the tweet list to `max_tweets`.
12. Returns the combined `profile` and `tweets` data in a dictionary.

## LIMITATIONS

- **No Full Timeline/Replies:** Cannot scrape the user's full tweet history or replies without login.
- **Public Data Only:** Limited to information visible to non-logged-in users.
- **Tweet Limit:** Non-logged-in scraping seems strictly limited to retrieving only the ~150 most recent tweets visible on the profile page, regardless of scrolling attempts beyond the initial load.
- **Website Changes:** Highly dependent on current X.com website structure and private API endpoints, which can break the scraper without notice.
- **Blocking/Rate Limiting:** Susceptible to Cloudflare challenges and rate limiting, especially with frequent/automated use. Running non-headless (`run_visible=True`) may improve reliability sometimes.

## Usage (Standalone Script)

```bash
python nodes/twitter_user_scraper/twitter_user_scraper.py <profile_url> [--max_tweets N] [--output file.json] [--visible]
```

*   `<profile_url>`: Full URL of the Twitter profile.
*   `--max_tweets N` (optional): Max tweets to return (default: 20 for script, 50 for node). Actual number may be lower.
*   `--output file.json` (optional): File to save JSON output (default: `user_profile_output.json`).
*   `--visible` (optional): Runs the browser visibly (non-headless). 