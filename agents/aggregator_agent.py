from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import invoke_with_retry
from config.settings import settings

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=settings.GEMINI_API_KEY
)

def aggregator_agent(state):

    prompt = f"""
        Return ONLY JSON.
        Schema:{{"summary":"","security":[],"performance":[],"quality":[]}}
        Security Findings: {state["security_review"]}
        Performance Findings:{state["performance_review"]}
        Quality Findings:{state["quality_review"]}
        Create a concise final review.
    """
    review = invoke_with_retry(llm,prompt)
    return {"final_review":review }