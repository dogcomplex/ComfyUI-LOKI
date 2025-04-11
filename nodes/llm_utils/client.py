import requests
import json
import re
from typing import List, Dict

# --- Constants ---
LLM_API_URL = "http://localhost:12345/v1/chat/completions" # Or your LLM API endpoint
LLM_MODEL = "meta-llama2-3.1-8b-instruct" # Or your desired model
LLM_HEADERS = {"Content-Type": "application/json"}
LLM_TEMPERATURE = 0.3
MAX_RETRIES = 3
BATCH_SIZE = 4 # Default batch size for LLM calls

SYSTEM_PROMPT_FILTER = """You are an expert at analyzing ComfyUI nodes and determining their relevance to specific workflow tasks.
Your job is to evaluate each node's description and determine how useful it would be for a given workflow goal.

Please analyze the node based on:
1. Direct relevance to the workflow goal
2. Utility as a supporting node for the workflow
3. Specific features that would help achieve the goal

Rate the node's applicability from 0-100 where:
0-20: Not relevant
21-40: Marginally relevant
41-60: Moderately useful
61-80: Very useful
81-100: Essential for this workflow

Return only a JSON response in this format:
{
    "score": <0-100>,
    "reason": "<brief 1-2 sentence explanation>"
}"""

SYSTEM_PROMPT_FILTER_BATCH = f"""{SYSTEM_PROMPT_FILTER}

You will be given multiple nodes to analyze in one request.
You must respond with only a valid JSON array containing one JSON object (with 'score' and 'reason') for each node provided in the prompt, in the same order. Format: [{{'score': number, 'reason': 'string'}}, ...]"""


# --- Functions ---

def query_llm(prompt: str, system_prompt: str = SYSTEM_PROMPT_FILTER) -> Dict:
    """Query the LLM API with a single prompt."""
    data = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": LLM_TEMPERATURE
    }

    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            response = requests.post(LLM_API_URL, headers=LLM_HEADERS, json=data, timeout=60) # Added timeout
            response.raise_for_status()
            result = response.json()
            content = result["choices"][0]["message"]["content"]

            try:
                # Attempt to parse the JSON response
                parsed_result = json.loads(content)
                if isinstance(parsed_result, dict) and "score" in parsed_result and "reason" in parsed_result:
                    return parsed_result
                raise ValueError("Invalid JSON format in LLM response content")
            except (json.JSONDecodeError, ValueError) as parse_error:
                print(f"Attempt {retry_count + 1}: Invalid JSON response: {parse_error}\nContent: {content}")
                retry_count += 1
                continue

        except requests.exceptions.RequestException as e:
            print(f"Attempt {retry_count + 1}: Error querying LLM API: {e}")
            retry_count += 1
            if retry_count == MAX_RETRIES:
                return {"score": 0, "reason": f"Error processing node: API request failed after {MAX_RETRIES} retries."}
            continue
        except Exception as e:
            print(f"Attempt {retry_count + 1}: Unexpected error during LLM query: {e}")
            retry_count += 1
            if retry_count == MAX_RETRIES:
                 return {"score": 0, "reason": f"Error processing node: Unexpected error after {MAX_RETRIES} retries."}
            continue # Reraise unexpected errors or handle differently

    return {"score": 0, "reason": f"Error processing node: Failed after {MAX_RETRIES} retries."}


def query_llm_batch(prompts: List[str], system_prompt: str = SYSTEM_PROMPT_FILTER_BATCH, batch_size: int = BATCH_SIZE) -> List[Dict]:
    """Query the LLM API with a batch of prompts."""
    results = []

    for i in range(0, len(prompts), batch_size):
        batch_prompts_data = prompts[i:i + batch_size]

        # Create a structured prompt for batch processing
        combined_prompt = "Analyze these nodes based on the criteria provided in the system message. Return a JSON array:\n\n"
        combined_prompt += "\n\n".join([
            f"--- Node {idx + 1} ---\n{p}\n--- End Node {idx + 1} ---"
            for idx, p in enumerate(batch_prompts_data)
        ])

        data = {
            "model": LLM_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": combined_prompt}
            ],
            "temperature": LLM_TEMPERATURE
        }

        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                response = requests.post(LLM_API_URL, headers=LLM_HEADERS, json=data, timeout=120) # Longer timeout for batch
                response.raise_for_status()
                content = response.json()["choices"][0]["message"]["content"]
                content = content.strip()

                # Attempt to extract the JSON array
                start_idx = content.find('[')
                end_idx = content.rfind(']')

                if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                    json_str = content[start_idx:end_idx + 1]
                    # Basic cleaning for common LLM formatting issues
                    json_str = json_str.replace("'", '"')
                    # Handle potential trailing commas before ']'
                    json_str = re.sub(r",\s*]", "]", json_str)
                    # Handle potential comments if any (simple case)
                    json_str = re.sub(r'//.*?\n', '\n', json_str)

                    try:
                        parsed_batch_results = json.loads(json_str)
                        if isinstance(parsed_batch_results, list):
                             # Validate and pad results
                            validated_results = []
                            for result in parsed_batch_results:
                                if isinstance(result, dict) and "score" in result and "reason" in result:
                                     validated_results.append(result)
                                else:
                                     print(f"Warning: Invalid item in batch response: {result}")
                                     validated_results.append({"score": 0, "reason": "Invalid response format for this item."})

                            # Ensure the number of results matches the number of prompts sent
                            while len(validated_results) < len(batch_prompts_data):
                                validated_results.append({"score": 0, "reason": "Missing response for this item."})

                            results.extend(validated_results[:len(batch_prompts_data)]) # Add validated results for this batch
                            break # Success for this batch, move to next

                    except json.JSONDecodeError as e:
                        print(f"Attempt {retry_count + 1}: Batch JSON parsing error - {e}\nContent: {json_str[:500]}...")
                        retry_count += 1
                else:
                    print(f"Attempt {retry_count + 1}: No valid JSON array found in batch response.\nContent: {content[:500]}...")
                    retry_count += 1

            except requests.exceptions.RequestException as e:
                 print(f"Attempt {retry_count + 1}: Error querying LLM API for batch: {e}")
                 retry_count += 1
                 if retry_count == MAX_RETRIES:
                     results.extend([{"score": 0, "reason": f"Failed to process node: API error after {MAX_RETRIES} retries."} for _ in batch_prompts_data])
                 continue # Continue to next retry or fail the batch
            except Exception as e:
                print(f"Attempt {retry_count + 1}: Unexpected error during batch LLM query: {e}")
                retry_count += 1
                if retry_count == MAX_RETRIES:
                    results.extend([{"score": 0, "reason": f"Failed to process node: Unexpected error after {MAX_RETRIES} retries."} for _ in batch_prompts_data])
                continue

        # If loop finishes without breaking (i.e., all retries failed)
        if retry_count == MAX_RETRIES:
             print(f"Batch failed after {MAX_RETRIES} retries.")
             # Ensure placeholders are added if not already done
             if len(results) < i + len(batch_prompts_data):
                results.extend([{"score": 0, "reason": f"Failed to process node after {MAX_RETRIES} retries."} for _ in range(len(batch_prompts_data) - (len(results) - i))])


    return results 