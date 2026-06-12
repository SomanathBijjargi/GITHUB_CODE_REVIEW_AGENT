from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import invoke_with_retry
from config.settings import settings


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=settings.GEMINI_API_KEY
)


def security_agent(state):

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
        1. Hardcoded Secrets
        2. SQL Injection
        3. Authentication Issues
        4. OWASP Vulnerabilities
        Diff:
        {diff}
    """

    review = invoke_with_retry(llm,prompt)

    return {"security_review": review }