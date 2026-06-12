from agents.graph import graph

def review_code_with_agents(diff: str):

    result = graph.invoke({
        "diff": diff[:8000]
    })

    review = result["final_review"]

    if isinstance(review, str):
        return {
            "summary": review,
            "security": [],
            "performance": [],
            "quality": []
        }

    print("RESULT TYPE:", type(result))
    print("FINAL REVIEW TYPE:", type(result["final_review"]))
    print("FINAL REVIEW:", result["final_review"])
    return review