
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.review_prompt import REVIEW_PROMPT
from config.settings import settings
from models.review_schema import ReviewResponse


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature = 0
)

structured_llm = llm.with_structured_output(
    ReviewResponse
)


def review_code(diff: str) -> ReviewResponse:
    try:
        prompt = REVIEW_PROMPT.format(diff=diff[:8000])  # token safety limit
        review = structured_llm.invoke(prompt)
        # Strip markdown fences if model adds them
    except Exception as e:
        print( f"Review generation failed: {e}")
        return ReviewResponse(
            summary="Review generation failed",
            bugs=[],
            security=[],
            performance=[],
            quality=[],
            score={
                "security": 0,
                "quality": 0,
                "performance": 0
            }
        )
    return review