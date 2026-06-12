# prompts/review_prompt.py
REVIEW_PROMPT = """
You are a senior code reviewer. Analyze the following git diff and return ONLY valid JSON.

Format:
{{
  "summary": "one sentence overview",
  "bugs": [{{"line": "description", "severity": "high|medium|low"}}],
  "security": [{{"issue": "description", "recommendation": "fix"}}],
  "performance": [{{"issue": "description", "recommendation": "fix"}}],
  "quality": [{{"issue": "description", "recommendation": "fix"}}],
  "score": {{"security": 0-100, "quality": 0-100, "performance": 0-100}}
}}

Diff:
{diff}
"""