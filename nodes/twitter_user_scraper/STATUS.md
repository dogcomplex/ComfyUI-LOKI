# Node Status: twitter_user_scraper

## System Prerequisites (Manual Installation Required!)

**IMPORTANT:** Playwright requires specific system-level browser dependencies to function. These **cannot** be installed automatically by this node or pip.

- **Linux/WSL:** You MUST install these dependencies manually using your system's package manager. The recommended command is:
  ```bash
  sudo playwright install-deps
  ```
- **Windows:** Running `playwright install` in your command prompt *should* typically handle necessary browser components, but ensure your OS is up-to-date.
- **Docker:** If running ComfyUI in Docker, these system dependencies **must be added to your Dockerfile** during the image build process. Simply running the command inside a running container will not persist across container restarts. You'll need to modify the Dockerfile to include the installation steps (e.g., add `RUN sudo playwright install-deps && sudo rm -rf /var/lib/apt/lists/*` or the equivalent `apt-get install` commands before installing Python requirements).

Failure to install these system dependencies will result in errors like "Host system is missing dependencies" when the node tries to launch a browser.

---

## Current State

- **Functionality:** Successfully scrapes public user profile information and the most recent ~150 tweets from a user's profile page using Playwright without login (requires system dependencies to be installed manually).
- **Layers Implemented:** ID, REQUIREMENTS, NAME, FUNCTIONALITY (PYTHON), INITIALIZATION, FUNCTIONALITY (COMFY-NODE).
- **Output:** Saves combined profile and tweet data to a JSON file (script mode) or outputs a dictionary (ComfyUI node).
- **Scrolling:** Implements scrolling to attempt loading more tweets, with early stopping if no new tweets are found after 2 attempts.

## TODOs / Future Work

- **[Medium] Refactor Shared Code:** Move `parse_user`, `parse_tweet`, and `find_objects_by_typename` to a shared utility module (e.g., `nodes/utils/twitter_parsing.py`) to be used by `twitter_scraper`, `twitter_thread_scraper`, and `twitter_user_scraper`.
- **[Low] Enhance Error Handling:** Implement more specific exception handling for different scraping failures (e.g., network errors, page structure changes, Cloudflare blocks).
- **[High] Add Login Support (Optional/Risky):** Investigate adding optional browser state injection or cookie loading to allow scraping while logged in. This would bypass public limits but increases complexity and risk of account suspension. Requires careful consideration of security and ToS.
- **[Medium] Implement TEST Layer:** Add `twitter_user_scraper_test.py` with unit tests for parsing functions and integration tests for the scraping process (using mock data or controlled test accounts if possible).
- **[Low] Implement VISUAL Layer:** Design an icon (`icon.png`), card (`card.png`), and potentially a basic `glamour.json` UI.
- **[Low] Improve Configuration:** Explore moving script arguments (`--output`, `--max_tweets`) to a `CONFIG` layer (`twitter_user_scraper.json`) if shared configuration becomes necessary beyond node inputs.

## Known Issues / Limitations

- **Requires Manual System Dependencies:** Playwright browser dependencies must be installed manually on the host system or within the Docker image (see System Prerequisites section).
- Reliant on current X.com website structure and internal API endpoints, which are subject to change without notice.
- Public scraping limit (~150 tweets) cannot be bypassed without login.
- Potential for Cloudflare blocks or rate limiting, especially with frequent use or from server IPs. Headless mode can be less reliable.

## Priority

**Medium.** The node is functional for its core public scraping task but could benefit from refactoring, testing, and potentially more advanced (but riskier) features like login support. Ensuring users understand the manual dependency installation is crucial. 