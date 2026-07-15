from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import invoke_with_retry
from config.settings import settings
import time

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=settings.GEMINI_API_KEY
# )

def aggregator_agent(state):

    return {
        "final_review": {
            "summary":"Multi-agent review completed.",
            "security":state["security_review"].get("issues", [] ),
            "performance":state["performance_review"].get("issues", []),
            "quality":state["quality_review"].get("issues", [])
        }
    }    