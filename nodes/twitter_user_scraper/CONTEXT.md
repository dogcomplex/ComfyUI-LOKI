# Context: twitter_user_scraper

## Internal Context (ComfyUI-LOKI)

- **Relation to `twitter_scraper`:** This node (`twitter_user_scraper`) focuses on scraping a *user's profile page* to retrieve their profile details and their most recent publicly visible tweets (~150). In contrast, the `twitter_scraper` node targets a *specific tweet URL* to scrape that single tweet and potentially its replies/thread.
- **Relation to `twitter_thread_scraper`:** The `twitter_thread_scraper` builds upon `twitter_scraper` to specifically follow conversation IDs and reconstruct entire threads, whereas `twitter_user_scraper` only gets the latest tweets *from the user's profile view*.
- **Shared Logic:** All Twitter scraping nodes currently share similar parsing logic (`parse_user`, `parse_tweet`) implemented within each script. A refactoring TODO exists (see `STATUS.md`) to move this into a shared utility module (`nodes/utils/twitter_parsing.py`).
- **Dependencies:** Relies on Playwright for browser automation and Jmespath for JSON parsing. These dependencies are declared in the node's `requirements.txt`.

## External Context

- **Twitter/X.com Scraping Challenges:** Scraping X.com is notoriously difficult due to:
    - Frequent changes to the website's structure and internal GraphQL API endpoints.
    - Aggressive anti-bot measures (Cloudflare, login walls for extended access).
    - Rate limiting based on IP address or account activity.
- **Public vs. Logged-in:** This node performs *public* scraping, which does not violate Twitter's ToS regarding automation but is limited in the data accessible (e.g., tweet count limit, no access to full timelines, replies, or private accounts). Logged-in scraping provides more data but requires handling authentication and carries the risk of account suspension.
- **Alternative Approaches:** 
    - **Official API:** Twitter's official API has become heavily restricted and expensive for most use cases.
    - **Nitter:** Open-source alternative front-ends like Nitter previously offered easier scraping but are often unreliable or blocked.
    - **Commercial Scraping Services:** Services like ScrapFly (see `nodes/twitter_scraper/context/how_to.txt`), Bright Data, etc., offer robust scraping infrastructure (proxy rotation, CAPTCHA solving, browser farms) but come at a cost.
- **Justification:** Implementing a basic public scraper within LOKI provides a free, integrated way to fetch recent user activity, useful for downstream analysis or generation tasks, despite its inherent limitations. 