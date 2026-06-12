# 🤖 AI GitHub Review Agent

An AI-powered GitHub Pull Request Review System that automatically analyzes code changes, detects issues, posts review comments on GitHub, and provides analytics through a dashboard.

The system uses **FastAPI**, **LangGraph**, **Google Gemini**, **MongoDB**, and **React** to perform automated multi-agent code reviews focused on security, performance, and code quality.

---

## 🚀 Features

### GitHub Integration
- GitHub Webhook Support
- Automatic Pull Request Detection
- Fetch Pull Request Diffs
- Post AI Review Comments to GitHub

### Multi-Agent AI Review
- Security Review Agent
- Performance Review Agent
- Code Quality Review Agent
- Aggregated Final Review

### AI Analysis
- Hardcoded Secret Detection
- SQL Injection Detection
- Authentication Issues
- OWASP Vulnerability Checks
- Performance Bottleneck Detection
- Code Quality Analysis
- Best Practice Recommendations

### Dashboard & Analytics
- Review History
- Pull Request Details
- Analytics Dashboard
- Repository Insights
- Review Statistics

### Database
- Store Reviews
- Store PR Metadata
- Review Analytics

---

# 🏗️ System Architecture

```text
GitHub Pull Request
        │
        ▼
GitHub Webhook
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Workflow
        │
 ┌───────────────┐
 │ Security Agent│
 └───────────────┘
        │
 ┌───────────────┐
 │Performance    │
 │Agent          │
 └───────────────┘
        │
 ┌───────────────┐
 │ Quality Agent │
 └───────────────┘
        │
        ▼
 Final Review
        │
 ┌──────┴───────┐
 ▼              ▼
MongoDB      GitHub Comment
                │
                ▼
         React Dashboard
```

---

# 🛠️ Tech Stack

## Backend
- FastAPI
- Python
- LangGraph
- LangChain
- Google Gemini API
- MongoDB

## Frontend
- React
- Vite
- Tailwind CSS
- Recharts
- Axios
- React Router

## Integrations
- GitHub REST API
- GitHub Webhooks

---

# 📂 Project Structure

```text
github-review-agent/

├── agents/
│   ├── security_agent.py
│   ├── performance_agent.py
│   ├── quality_agent.py
│   ├── aggregator_agent.py
│   └── graph.py
│
├── api/
│   ├── webhook.py
│   └── reviews.py
│
├── services/
│   ├── github_service.py
│   ├── mongo_service.py
│   ├── comment_formatter.py
│   └── langgraph_review_service.py
│
├── models/
│   ├── review_schema.py
│   └── agent_schema.py
│
├── prompts/
│   └── review_prompt.py
│
├── config/
│   └── settings.py
│
├── review-dashboard/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-github-review-agent.git

cd ai-github-review-agent
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_key

GITHUB_TOKEN=your_github_token

GITHUB_WEBHOOK_SECRET=your_webhook_secret

MONGO_URI=your_mongodb_connection_string

DB_NAME=github_review_agent
```

---

# ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# 🌐 Run Frontend

```bash
cd review-dashboard

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔗 Configure GitHub Webhook

Repository Settings

```text
Settings
   ↓
Webhooks
   ↓
Add Webhook
```

Payload URL:

```text
https://your-domain.com/webhook
```

Content Type:

```text
application/json
```

Events:

```text
Pull Requests
```

Secret:

```text
Same value as GITHUB_WEBHOOK_SECRET
```

---

# 📊 API Endpoints

## Webhook

```http
POST /webhook
```

Receives GitHub Pull Request events.

---

## Get Reviews

```http
GET /reviews
```

Returns all stored reviews.

---

## Get Review By PR

```http
GET /reviews/{pr_number}
```

Returns review details.

---

## Analytics

```http
GET /stats
```

Returns dashboard statistics.

---

# 📸 Sample Workflow

```text
Developer Creates PR
         │
         ▼
GitHub Webhook Triggered
         │
         ▼
FastAPI Receives Event
         │
         ▼
Fetch PR Diff
         │
         ▼
LangGraph Multi-Agent Review
         │
         ▼
Generate Review
         │
         ▼
Save To MongoDB
         │
         ▼
Post Comment To GitHub
         │
         ▼
Display Analytics Dashboard
```

---

# 🔮 Future Enhancements

- GitHub App Integration
- Multi-Repository Support
- Inline PR Review Comments
- RAG-Based Security Knowledge Base
- Redis Queue Processing
- Docker Deployment
- Kubernetes Scaling
- Team Analytics Dashboard
- Slack/Discord Notifications

---

# 📈 Resume Highlights

- Built an AI-powered GitHub Pull Request Review Agent using FastAPI, LangGraph, Gemini, MongoDB, and React.
- Designed a multi-agent review workflow for security, performance, and code quality analysis.
- Integrated GitHub Webhooks and GitHub APIs for automated pull request reviews.
- Developed an analytics dashboard for review insights and repository statistics.
- Implemented automated code review generation and GitHub comment posting.

---

# 👨‍💻 Author

**Somanath Bijjargi**

Computer Science Engineering Student

Backend Developer | AI Engineer Aspirant

GitHub: https://github.com/SomanathBijjargi