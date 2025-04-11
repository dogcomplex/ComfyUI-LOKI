import requests
import json
from typing import Dict

# Default constants can be overridden by inputs
DEFAULT_LLM_API_URL = "http://localhost:12345/v1/chat/completions"
DEFAULT_LLM_MODEL = "meta-llama2-3.1-8b-instruct"
DEFAULT_MAX_RETRIES = 3
DEFAULT_TIMEOUT = 60

class LLMQueryAPINode:
    """
    Sends a single prompt to a generic LLM API (OpenAI compatible)
    and returns the raw response content string.
    Handles retries on failure. Also provides a static method for reuse.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_prompt": ("STRING", {"multiline": True}),
                "system_prompt": ("STRING", {"multiline": True, "default": "You are a helpful assistant."}),
            },
            "optional": {
                "api_url": ("STRING", {"default": DEFAULT_LLM_API_URL}),
                "model": ("STRING", {"default": DEFAULT_LLM_MODEL}),
                "temperature": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 2.0, "step": 0.1}),
                "max_retries": ("INT", {"default": DEFAULT_MAX_RETRIES, "min": 0}),
                "timeout": ("INT", {"default": DEFAULT_TIMEOUT, "min": 5}),
                 # Optional trigger
                 "trigger": ("*", {}),
            }
        }

    RETURN_TYPES = ("STRING",) # Raw response content string (usually JSON)
    RETURN_NAMES = ("llm_response_content",)
    FUNCTION = "query_llm_api"
    CATEGORY = "utils/llm"
    OUTPUT_NODE = False

    @staticmethod
    def _static_query_llm_single(user_prompt: str, system_prompt: str, api_url: str, model: str, temperature: float, max_retries: int, timeout: int) -> str:
        """Static method containing the core LLM API query logic with retries."""
        if not user_prompt:
            print("Error (_static_query_llm_single): User prompt is empty.")
            return json.dumps({"error": "User prompt cannot be empty."})

        headers = {"Content-Type": "application/json"}
        data = {"model": model, "messages": [{"role": "system", "content": system_prompt},{"role": "user", "content": user_prompt}], "temperature": temperature}
        retry_count = 0
        response = None # Initialize response to handle potential error in JSONDecodeError block

        while retry_count <= max_retries:
            attempt = retry_count + 1
            print(f"Attempt {attempt}/{max_retries + 1} to query LLM API at {api_url}...")
            try:
                response = requests.post(api_url, headers=headers, json=data, timeout=timeout)
                response.raise_for_status()
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0 and "message" in result["choices"][0] and "content" in result["choices"][0]["message"]:
                    content = result["choices"][0]["message"]["content"]
                    print("LLM API call successful.")
                    return content
                else:
                    print("Error: Unexpected LLM API response structure.")
                    return json.dumps(result)
            except requests.exceptions.Timeout: print(f"Attempt {attempt}: Request timed out after {timeout} seconds.")
            except requests.exceptions.HTTPError as e: print(f"Attempt {attempt}: HTTP Error querying LLM API: {e}")
            except requests.exceptions.RequestException as e: print(f"Attempt {attempt}: Request Exception querying LLM API: {e}")
            except json.JSONDecodeError as e:
                 # Use response.text if available, otherwise indicate inability to decode
                 response_text = getattr(response, 'text', '<response object not available>')
                 print(f"Attempt {attempt}: Failed to decode LLM API response JSON: {e}")
                 return json.dumps({"error": f"JSONDecodeError: {e}", "response_text": response_text})
            except Exception as e: print(f"Attempt {attempt}: Unexpected error during LLM query: {e}")

            retry_count += 1
            if retry_count > max_retries: break

        error_message = f"LLM API query failed after {max_retries + 1} attempts."
        print(error_message)
        return json.dumps({"error": error_message})

    def query_llm_api(self, user_prompt: str, system_prompt: str, api_url: str = DEFAULT_LLM_API_URL, model: str = DEFAULT_LLM_MODEL, temperature: float = 0.3, max_retries: int = DEFAULT_MAX_RETRIES, timeout: int = DEFAULT_TIMEOUT, trigger=None) -> tuple[str]:
        """Node execution function: Calls the static query method."""
        result_content = self._static_query_llm_single(
            user_prompt=user_prompt,
            system_prompt=system_prompt,
            api_url=api_url,
            model=model,
            temperature=temperature,
            max_retries=max_retries,
            timeout=timeout
        )
        return (result_content,) 