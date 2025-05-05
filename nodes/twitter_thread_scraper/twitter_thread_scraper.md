# twitter_thread_scraper Node Requirements

## DESCRIPTION

Attempts to scrape tweet data from an X.com (Twitter) thread, starting from a given tweet URL. Prioritizes following the main author's thread replies.

**Note:** Due to X.com restrictions for non-logged-in users, this node can typically only retrieve the **starting tweet** and potentially 1-2 immediate replies if they load initially. Full thread scraping requires login, which is not implemented due to Terms of Service violations and account suspension risks.

## INPUTS

- `thread_start_url` (STRING): The URL of the first tweet in the thread.
- `max_tweets` (INT): The maximum number of tweets to *attempt* to return (effective limit may be much lower due to login restrictions).

## OUTPUTS

- `thread_data_list` (LIST[DICT]): A list containing parsed data for the tweets successfully retrieved (often only the first tweet).

## NODE_STRATEGY

Uses Playwright (without login) to load the initial tweet page, intercepts background network requests (XHR), and parses available tweet data. It tries to follow the author's sequence based on the limited data available in the initial page load XHRs.

## LIMITATIONS

- **Requires Login for Full Threads:** X.com requires users to be logged in to view full threads and replies beyond the first few. This scraper operates without login to avoid ToS violations and account risks.
- **Limited Reply Depth:** Consequently, this node usually only retrieves the starting tweet. It cannot reliably access the full conversation history visible to logged-in users.
- **No Scrolling for More Replies:** Even simulated scrolling does not reliably trigger the loading of further replies for non-logged-in sessions based on current testing. 