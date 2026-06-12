from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from agents.security_agent import security_agent
from agents.performance_agent import performance_agent
from agents.quality_agent import quality_agent
from agents.aggregator_agent import aggregator_agent


class ReviewState(TypedDict):
    diff: str
    security_review: dict
    performance_review: dict
    quality_review: dict
    final_review: dict

builder = StateGraph(ReviewState)
builder.add_node("security",security_agent)
builder.add_node("performance",performance_agent)
builder.add_node("quality",quality_agent)
builder.add_node("aggregator",aggregator_agent)
builder.set_entry_point("security")
builder.add_edge("security","performance")
builder.add_edge("performance","quality")
builder.add_edge("quality","aggregator")
builder.add_edge("aggregator",END)

graph = builder.compile()