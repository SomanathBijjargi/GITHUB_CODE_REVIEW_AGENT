from fastapi import APIRouter
from bson import ObjectId
from services.mongo_service import reviews
from collections import Counter
from datetime import datetime, timedelta

router = APIRouter()


@router.get("/reviews")
def get_reviews():

    data = list(
        reviews.find(
            {},
            {"_id": 0}
        )
    )

    return data

@router.get("/stats")
def stats():

    docs = list(reviews.find({},{"_id": 0}))

    total_reviews = len(docs)

    repo_counter = Counter()

    now = datetime.utcnow()

    week_reviews = 0
    month_reviews = 0

    for doc in docs:

        repo_counter[doc.get("repo", "Unknown")] += 1

        created = doc.get("created_at")
        if created:
            if (now - created).days <= 7:
                week_reviews += 1
            if (now - created).days <= 30:
                month_reviews += 1

    top_repo = (
        repo_counter.most_common(1)[0][0]
        if repo_counter
        else "N/A"
    )

    return {
        "total_reviews":total_reviews,
        "top_repository":top_repo,
        "reviews_this_week": week_reviews,
        "reviews_this_month":month_reviews
    }

@router.get("/reviews/{pr_number}")
def get_review(pr_number: int):

    review = reviews.find_one(
        {"pr_number": pr_number},
        {"_id": 0}
    )

    if not review:
        return {"message": "Review not found"}

    return review