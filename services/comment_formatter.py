from models.review_schema import ReviewResponse


def format_comment(review: dict) -> str:

    
    lines = []

    lines.append("## 🤖 AI Multi-Agent Code Review\n")
    lines.append(f"### Summary\n"f"{review['summary']}\n")
    for section in ["security","performance","quality"]:

        items = review.get(section, [])
        if not items:
            continue

        lines.append(f"\n### {section.title()}")

        for item in items:
            lines.append(f"- **{item['issue']}**")
            lines.append(f"  - Severity: {item['severity']}")
            lines.append(f"  - Recommendation: "f"{item['recommendation']}")
    return "\n".join(lines)