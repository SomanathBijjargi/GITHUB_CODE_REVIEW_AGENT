# api/webhook.py
import hmac, hashlib
from datetime import datetime
from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from services.github_service import github_service
from services.review_service import review_code
from services.langgraph_review_service import (review_code_with_agents)
from services.mongo_service import save_review
from services.comment_formatter import format_comment
from config.settings import settings

router = APIRouter()

def verify_signature(payload: bytes, signature: str) -> bool:
    expected = "sha256=" + hmac.new(
        settings.GITHUB_WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

async def process_pr(owner: str, repo: str, pr_number: int):
    print("PROCESS_PR STARTED")
    try:
        diff = github_service.get_pr_diff(owner, repo, pr_number)
        pr_details = github_service.get_pr_details(owner,repo,pr_number)
        print("Fetching diff...")

        review = review_code_with_agents(diff)
        print("Generating review...")

        formatted = format_comment(review)
        save_review({"owner" : owner, 
                    "repo": repo,
                    "pr_number": pr_number,
                    "pr_title":pr_details["title"], 
                    "pr_url":pr_details["html_url"],
                    "author":pr_details["user"]['login'],
                    "source_branch":pr_details["head"]["ref"],
                    "target_branch":pr_details["base"]["ref"],
                    "review": review,
                    "created_at": datetime.utcnow()
        })
        print("Saving review...")

        github_service.post_comment(owner, repo, pr_number, formatted)
        print("Posting comment...")
    except Exception as e:
        print(f"Review failed for PR #{pr_number}: {e}")

@router.post("/webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    signature = request.headers.get("X-Hub-Signature-256", "")
    body = await request.body()

    if not verify_signature(body, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    # body = await request.body()

    # print("Received Webhook")
    # print(body.decode())

    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")

    # Only handle opened/synchronize PR events
    if event != "pull_request":
        return {"status": "ignored"}
    if payload.get("action") not in ("opened", "synchronize"):
        return {"status": "ignored"}

    pr = payload["pull_request"]
    owner = payload["repository"]["owner"]["login"]
    repo = payload["repository"]["name"]
    pr_number = pr["number"]

    # Run review in background so webhook returns fast
    print("Webhook Received")
    background_tasks.add_task(process_pr, owner, repo, pr_number)
    print("task added")
    return {"status": "accepted"}