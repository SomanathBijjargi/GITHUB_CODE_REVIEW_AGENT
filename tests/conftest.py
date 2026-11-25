import os

# Settings() runs at import time and requires all of these,
# so they must be set BEFORE anything imports main/api.webhook.
os.environ["GITHUB_TOKEN"] = "test-token"
os.environ["GEMINI_API_KEY"] = "test-gemini-key"
os.environ["GITHUB_WEBHOOK_SECRET"] = "test-secret"
os.environ["MONGO_URI"] = "mongodb://localhost:27017"
os.environ["DB_NAME"] = "test_db"

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from main import app
    return TestClient(app)