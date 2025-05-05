# Node Status: list_available_nodes

## Current Status

- **Refactored:** Core logic separated, node wrapper updated to match `list_installed_nodes` format.
- **Documentation:** Basic spec files generated.

## Priority

- **Medium:** Useful utility for node discovery and ecosystem analysis.

## TODO

- [ ] Add more robust error handling for network issues or invalid JSON.
- [ ] Consider adding options to filter the list based on keywords, author, etc. (would likely happen in a separate filter node).
- [ ] Improve automatic detection of ComfyUI-Manager path if possible.
- [ ] Add test cases (`list_available_nodes_test.py`) - needs mocking for network requests/cache files.
- [ ] Add visual/glamour layers. 