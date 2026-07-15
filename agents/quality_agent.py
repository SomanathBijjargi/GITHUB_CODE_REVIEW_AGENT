from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import invoke_with_retry
from config.settings import settings
import time

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY
)


def quality_agent(state):
    time.sleep(15)
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

        1. Readability
        2. Maintainability
        3. Naming Conventions
        4. Code Smells

        Diff:

    {diff}
    """
    review =invoke_with_retry(llm,prompt)
    return { "quality_review": review}