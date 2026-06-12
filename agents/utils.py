import time


def invoke_with_retry(llm,prompt,retries=3):
    for attempt in range(retries):
        try:
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)
    return "Review unavailable"