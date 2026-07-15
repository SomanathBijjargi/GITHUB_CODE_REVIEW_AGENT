import json
import time


def invoke_with_retry(llm, prompt, retries=3):
    for attempt in range(retries):
        try:
            response = llm.invoke(prompt)
            text = response.content.strip()
            text = (
                text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )
            return json.loads(text)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)
    return {
        "issues": []
    }