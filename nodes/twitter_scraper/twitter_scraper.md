# twitter_scraper Node Requirements

## DESCRIPTION

Scrapes data from a specific X.com (Twitter) tweet URL.

## INPUTS

- `tweet_url` (STRING): The URL of the tweet to scrape (e.g., "https://x.com/Scrapfly_dev/status/1664267318053179398").

## OUTPUTS

- `tweet_data` (DICT): A dictionary containing parsed data from the tweet.

## NODE_STRATEGY

This node uses Playwright to launch a headless browser, navigate to the tweet URL, intercept background network requests (XHR) containing tweet data, and parse the relevant information using Jmespath. 