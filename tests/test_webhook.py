import hashlib
import hmac
import json
from unittest.mock import AsyncMock, patch

import pytest

from api.webhook import verify_signature

SECRET = "test-secret"  # must match conftest.py


def sign(body: bytes, secret: str = SECRET) -> str:
    return "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


def pr_payload(action: str = "opened") -> dict:
    return {
        "action": action,
        "pull_request": {"number": 42},
        "repository": {"name": "hello-world", "owner": {"login": "octocat"}},
    }


def post_webhook(client, payload, event="pull_request", signature="auto"):
    """signature="auto" signs correctly, None omits the header, any other string is sent as-is."""
    body = json.dumps(payload).encode()
    headers = {"X-GitHub-Event": event, "Content-Type": "application/json"}
    if signature == "auto":
        headers["X-Hub-Signature-256"] = sign(body)
    elif signature is not None:
        headers["X-Hub-Signature-256"] = signature
    return client.post("/webhook", content=body, headers=headers)


@pytest.fixture
def mock_process_pr():
    # Replace the background job so tests never hit GitHub, Gemini or MongoDB
    with patch("api.webhook.process_pr", new=AsyncMock()) as mock:
        yield mock


# --- HMAC validation ---

def test_verify_signature_accepts_valid_signature():
    body = b'{"action": "opened"}'
    assert verify_signature(body, sign(body)) is True


def test_verify_signature_rejects_tampered_body_wrong_secret_and_empty():
    body = b'{"action": "opened"}'
    assert verify_signature(body + b" ", sign(body)) is False          # body changed
    assert verify_signature(body, sign(body, secret="wrong")) is False  # wrong secret
    assert verify_signature(body, "") is False                          # no signature


# --- Webhook handler ---

@pytest.mark.parametrize("signature", ["sha256=deadbeef", None])
def test_webhook_returns_401_for_bad_or_missing_signature(client, mock_process_pr, signature):
    response = post_webhook(client, pr_payload(), signature=signature)

    assert response.status_code == 401
    mock_process_pr.assert_not_called()


@pytest.mark.parametrize("action", ["opened", "synchronize"])
def test_webhook_accepts_pr_event_and_queues_review(client, mock_process_pr, action):
    response = post_webhook(client, pr_payload(action))

    assert response.status_code == 200
    assert response.json() == {"status": "accepted"}
    mock_process_pr.assert_called_once_with("octocat", "hello-world", 42)


@pytest.mark.parametrize(
    "event, action",
    [("ping", "opened"), ("pull_request", "closed")],
)
def test_webhook_ignores_irrelevant_events(client, mock_process_pr, event, action):
    response = post_webhook(client, pr_payload(action), event=event)

    assert response.status_code == 200
    assert response.json() == {"status": "ignored"}
    mock_process_pr.assert_not_called()