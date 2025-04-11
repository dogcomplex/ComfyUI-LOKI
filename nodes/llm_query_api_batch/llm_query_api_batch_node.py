import requests
import json
import re
from typing import List, Dict

# Default constants can be overridden by inputs
DEFAULT_LLM_API_URL = "http://localhost:12345/v1/chat/completions"
DEFAULT_LLM_MODEL = "meta-llama2-3.1-8b-instruct"
DEFAULT_MAX_RETRIES = 3
DEFAULT_TIMEOUT = 120 # Longer timeout for batch
DEFAULT_BATCH_SIZE = 4
DEFAULT_TEMPERATURE = 0.7

class LLMQueryAPIBatchNode:
    """
    Sends multiple prompts to a generic LLM API (OpenAI compatible) in batches.
    Expects the LLM to return a structured response (e.g., JSON array for filter node use case).
    Handles retries on failure. Provides a static method for reuse.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Takes a list of prompts (e.g., joined by a delimiter or as a JSON list string)
                "user_prompts": ("STRING", {"multiline": True, "default": '["Prompt 1", "Prompt 2"]'}),
                "system_prompt": ("STRING", {"multiline": True, "default": "You are a helpful assistant processing batch requests."}),
            },
            "optional": {
                "api_url": ("STRING", {"default": DEFAULT_LLM_API_URL}),
                "model": ("STRING", {"default": DEFAULT_LLM_MODEL}),
                "temperature": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 2.0, "step": 0.1}),
                "batch_size": ("INT", {"default": DEFAULT_BATCH_SIZE, "min": 1}),
                "max_retries": ("INT", {"default": DEFAULT_MAX_RETRIES, "min": 0}),
                "timeout": ("INT", {"default": DEFAULT_TIMEOUT, "min": 10}),
                # Trigger optional
                "trigger": ("*", {}),
            }
        }

    RETURN_TYPES = ("STRING",) # JSON string representing the list of results
    RETURN_NAMES = ("batch_response_json",)
    FUNCTION = "query_llm_api_batch"
    CATEGORY = "utils/llm"
    OUTPUT_NODE = False

    # --- Static Helper Methods ---
    @staticmethod
    def _static_parse_input_prompts(prompts_input: str) -> List[str]:
        """Static: Attempts to parse the input string into a list of prompts."""
        prompts_input = prompts_input.strip()
        try:
            # Try parsing as JSON list
            if prompts_input.startswith('[') and prompts_input.endswith(']'):
                parsed = json.loads(prompts_input)
                if isinstance(parsed, list) and all(isinstance(p, str) for p in parsed):
                    return parsed
                else:
                     print("Warning: Input looks like JSON list but failed validation.")
        except json.JSONDecodeError:
            print("Warning: Input is not a valid JSON list. Trying newline splitting.")

        # Fallback: Split by newline (ignoring empty lines)
        return [line for line in prompts_input.splitlines() if line.strip()]

    @staticmethod
    def _static_format_batch_request_prompt(batch_prompts: List[str]) -> str:
         """Static: Formats a list of prompts into a single string for the batch API call."""
         # This formatting might need adjustment depending on how the target LLM handles batch requests.
         # For the filter use case, we used numbered blocks.
         formatted_prompt = "Process the following requests based on the system instructions. Provide a response for each request, ideally in a structured format like a JSON array:\n\n"
         formatted_prompt += "\n\n".join([
             f"--- Request {idx + 1} ---\n{p}\n--- End Request {idx + 1} ---"
             for idx, p in enumerate(batch_prompts)
         ])
         return formatted_prompt

    @staticmethod
    def _static_query_llm_batch(prompts_list: List[str], system_prompt: str, api_url: str, model: str, temperature: float, batch_size: int, max_retries: int, timeout: int) -> List[Dict]:
        """Static method containing the core batch query logic."""
        all_results = []
        headers = {"Content-Type": "application/json"}

        for i in range(0, len(prompts_list), batch_size):
            current_batch_prompts = prompts_list[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            print(f"Processing Batch {batch_num} ({len(current_batch_prompts)} prompts)...")

            # Format the request for the batch API call
            # IMPORTANT: This assumes the LLM endpoint can handle a single combined prompt
            # representing the batch. If the API requires separate calls per item,
            # this node should instead iterate and call the single LLMQueryAPI logic.
            # For now, we assume a combined prompt approach.
            combined_request_prompt = LLMQueryAPIBatchNode._static_format_batch_request_prompt(current_batch_prompts)

            data = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": combined_request_prompt}
                ],
                "temperature": temperature
            }

            retry_count = 0
            batch_success = False
            response = None # Initialize response

            while retry_count <= max_retries:
                attempt = retry_count + 1
                print(f"  Batch {batch_num} - Attempt {attempt}/{max_retries + 1}...")
                try:
                    response = requests.post(api_url, headers=headers, json=data, timeout=timeout)
                    response.raise_for_status()
                    response_json = response.json()
                    content = response_json["choices"][0]["message"]["content"]

                    # --- Response Parsing Logic ---
                    # This is crucial and depends heavily on the expected output format
                    # For the filter use case, we expect a JSON array string matching the batch size.
                    print(f"  Batch {batch_num} - Raw LLM content received (length: {len(content)}).")
                    content = content.strip()
                    start_idx = content.find('[')
                    end_idx = content.rfind(']')

                    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                        json_str = content[start_idx:end_idx + 1]
                        json_str = json_str.replace("'", '"') # Basic cleaning
                        json_str = re.sub(r",\s*]", "]", json_str) # Handle trailing commas

                        try:
                            parsed_batch_results = json.loads(json_str)
                            if isinstance(parsed_batch_results, list):
                                print(f"  Batch {batch_num} - Successfully parsed {len(parsed_batch_results)} results from LLM response.")
                                # Basic validation and padding (optional, depends on strictness needed)
                                validated_results = []
                                for result in parsed_batch_results:
                                     # Add more specific validation if needed (e.g., check for 'score', 'reason')
                                     if isinstance(result, dict):
                                         validated_results.append(result)
                                     else:
                                         print(f"Warning: Invalid item format in batch {batch_num}: {result}")
                                         validated_results.append({"error": "Invalid item format", "raw": result})
                                # Pad if LLM didn't return enough items
                                while len(validated_results) < len(current_batch_prompts):
                                     print(f"Warning: Padding missing results for batch {batch_num}.")
                                     validated_results.append({"error": "Missing response for this item."})

                                all_results.extend(validated_results[:len(current_batch_prompts)]) # Ensure not too many results added
                                batch_success = True
                                break # Success for this batch
                            else:
                                print(f"  Batch {batch_num} - Attempt {attempt}: Parsed JSON is not a list.")
                                retry_count += 1 # Retry if structure is wrong

                        except json.JSONDecodeError as e:
                            print(f"  Batch {batch_num} - Attempt {attempt}: Batch JSON parsing error - {e}\nContent sample: {json_str[:200]}...")
                            retry_count += 1
                    else:
                        print(f"  Batch {batch_num} - Attempt {attempt}: No valid JSON array '[]' found in response.\nContent sample: {content[:200]}...")
                        retry_count += 1

                # --- Error Handling for Requests ---
                except requests.exceptions.Timeout:
                    print(f"  Batch {batch_num} - Attempt {attempt}: Request timed out.")
                    retry_count += 1
                except requests.exceptions.HTTPError as e:
                    print(f"  Batch {batch_num} - Attempt {attempt}: HTTP Error: {e}")
                    retry_count += 1
                except requests.exceptions.RequestException as e:
                    print(f"  Batch {batch_num} - Attempt {attempt}: Request Exception: {e}")
                    retry_count += 1
                except Exception as e:
                    print(f"  Batch {batch_num} - Attempt {attempt}: Unexpected error: {e}")
                    retry_count += 1

                if retry_count > max_retries:
                    print(f"Error: Batch {batch_num} failed after {max_retries + 1} attempts.")
                    # Add error placeholders for each prompt in the failed batch
                    all_results.extend([{"error": f"LLM query failed for this item after {max_retries + 1} retries."}] * len(current_batch_prompts))
                    break # Move to the next batch

            # Ensure loop terminates if batch fails
            if not batch_success and retry_count > max_retries:
                print(f"Moving to next batch after failure of batch {batch_num}.")

        return all_results # Return the list of dictionaries

    # --- Node Execution Methods ---
    def query_llm_api_batch(self, user_prompts: str, system_prompt: str, api_url: str = DEFAULT_LLM_API_URL, model: str = DEFAULT_LLM_MODEL, temperature: float = 0.3, batch_size: int = DEFAULT_BATCH_SIZE, max_retries: int = DEFAULT_MAX_RETRIES, timeout: int = DEFAULT_TIMEOUT, trigger=None) -> tuple[str]:
        """Node execution function: Parses input, calls static batch query, returns JSON string."""
        prompts_list = self._static_parse_input_prompts(user_prompts)
        if not prompts_list:
            print("Error: No valid prompts found in input.")
            return (json.dumps({"error": "No valid prompts provided."}),)

        print(f"Processing {len(prompts_list)} prompts in batches of {batch_size}...")
        results_list = self._static_query_llm_batch(
            prompts_list=prompts_list,
            system_prompt=system_prompt,
            api_url=api_url,
            model=model,
            temperature=temperature,
            batch_size=batch_size,
            max_retries=max_retries,
            timeout=timeout
        )

        # Return all collected results as a single JSON string array
        try:
             final_json_output = json.dumps(results_list, indent=2) # Pretty print optional
             return (final_json_output,)
        except TypeError as e:
             print(f"Error serializing final batch results: {e}")
             # Attempt to return partial results if serialization fails
             try:
                 partial_json = json.dumps({"error": f"Failed to serialize final results: {e}", "partial_results": results_list[:10]}, default=str)
                 return (partial_json,)
             except: # Final fallback
                 return ('{"error": "Failed to serialize final results and partial results."}',) 