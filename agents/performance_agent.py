from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import invoke_with_retry
from config.settings import settings
import time
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY
)

def performance_agent(state):
    # time.sleep(10)
    diff = state["diff"]

    prompt = f"""
        Return ONLY JSON.

        Schema:

        {{
            "issues":[
                {{
                    "issue":"",
                    "severity":"",
                    "recommendation":""
                }}
            ]
        }}

        Analyze ONLY:

        1. Inefficient Loops
        2. Memory Usage
        3. Database Performance
        4. Expensive Operations

        Diff:
    {diff}
    """
    review = invoke_with_retry(llm,prompt)
    return {"performance_review":review}