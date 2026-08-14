from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class CommerceState(TypedDict):
    question: str
    intent: str
    answer: str


def analyze_question(state):
    question = state["question"]

    if "inventory" in question.lower() or "stock" in question.lower():
        state["intent"] = "inventory"
    elif "revenue" in question.lower():
        state["intent"] = "revenue"  
    else:
        state["intent"] = "general"

    return state

def inventory_node(state):
    state["answer"] = "Checking CommerceOps inventory."
    return state

def revenue_node(state):
    state["answer"] = "Revenue request."
    return state

def general_node(state):
    state["answer"] = "Handling a general question."
    return state


def route_question(state):
    if state["intent"] == "inventory":
        return "inventory"
    elif state["intent"] == "revenue":
        return "revenue"

    return "general"


graph = StateGraph(CommerceState)

graph.add_node(
    "analyze",
    analyze_question
)

graph.add_node(
    "inventory",
    inventory_node
)

graph.add_node(
    "revenue",
    revenue_node
)

graph.add_node(
    "general",
    general_node
)

graph.add_edge(
    START,
    "analyze"
)

graph.add_conditional_edges(
    "analyze",
    route_question,
    {
        "inventory": "inventory",
        "revenue": "revenue",
        "general": "general"
    }
)

graph.add_edge(
    "inventory",
    END
)

graph.add_edge(
    "revenue",
    END
)

graph.add_edge(
    "general",
    END
)

app = graph.compile()


result = app.invoke({
    "question": "Hello, what can you do?",
    "intent": "",
    "answer": ""
})

print(result)