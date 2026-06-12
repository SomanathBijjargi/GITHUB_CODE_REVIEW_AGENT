from agents.graph import graph

result = graph.invoke({
    "diff": """
    password = "admin123"

    query = "SELECT * FROM users WHERE id=" + user_id
    """
})

print(result["final_review"])