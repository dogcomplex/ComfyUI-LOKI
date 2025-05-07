# STATUS: Scribe Node

## STATUS

-   Initial Implementation / Under Development

## PRIORITY

-   Medium (Core utility node for workflow understanding and sharing)

## CURRENT LIMITATIONS

-   Requires network connectivity to fetch external documentation.
-   External documentation fetching assumes a specific URL structure (`<base_url>/<NodeType>.md`) and retrieves raw Markdown content without parsing.
-   Error handling for network requests is basic.
-   Mapping of `widgets_values` back to named widgets is not implemented; values are listed by index or raw dictionary structure.
-   Documentation output is saved to a node-specific `./output/` subfolder, which might not be easily discoverable by users.
-   Does not fully adhere to LOKI `NODE_SPECIFICATIONS.md` yet (e.g., config files not fully utilized).

## TODO / FUTURE WORK

-   [x] Refactor class name from `ScribeNode` to `Scribe` in `scribe_node.py`.
-   [x] Update node `CATEGORY` to `LOKI 🦊/Documentation` in `scribe_node.py`.
-   [ ] Refactor `__init__.py` to load mappings from `scribe.json` / `scribe_name.md`.
-   [x] Implement `NODE_DISPLAY_NAME_MAPPINGS` using `scribe_name.md` conventions.
-   [x] Moved output file saving to main ComfyUI output dir (`<comfy_output>/LOKI/Scribe/output/`).
-   [x] Resolved workflow data access issue by using hidden `PROMPT` input.
-   [ ] Enhance `get_node_info` to map `widgets_values` to widget names if feasible.
-   [ ] Improve robustness of `fetch_node_docs` (handle 404s, timeouts, parse Markdown).
-   [ ] Add `scribe_test.py` for basic tests.
-   [ ] Add `scribe_workflow.json` example usage.
-   [ ] Develop Glamour layer (`glamour.json`, `icon.png`).
-   [ ] Utilize `scribe.json` config file more effectively (e.g., load defaults). 