# twitter_user_scraper Node Requirements

## DESCRIPTION

Scrapes public profile data AND the initially visible tweets for a specific X.com (Twitter) user using their profile URL.

**Note:** This node scrapes the publicly visible profile information and the first batch of tweets visible without login. It does not scrape the user's *full* tweet timeline (requiring scrolling) or replies, as that requires login.

## INPUTS

- `profile_url` (STRING): The URL of the user's profile page (e.g., "https://x.com/Scrapfly_dev").

## OUTPUTS

- `user_data` (DICT): A dictionary containing:
    - `profile`: A dictionary with the parsed public profile data.
    - `tweets`: A list of dictionaries, each containing parsed data for an initially visible tweet.

## NODE_STRATEGY

Uses Playwright (without login) to load the user profile page, intercepts background network requests (XHR) for both profile data (`UserByScreenName`/`UserByRestId`) and the initial tweet list (`UserTweets`), and parses the relevant information using Jmespath.

## LIMITATIONS

- **No Full Timeline/Replies:** Cannot scrape the user's full tweet timeline (requiring scrolling) or replies without login.
- **Initial Tweets Only:** The `tweets` list contains only the first batch of tweets loaded publicly, not the entire history.
- **Public Data Only:** Limited to information visible to non-logged-in users. 