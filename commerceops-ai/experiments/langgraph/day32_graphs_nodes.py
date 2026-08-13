from langgraph.graph import StateGraph,START,END

def first_node(state):
    print("Running first node")
    return state


def second_node(state):
    print("Running second node")
    return state

graph = StateGraph(dict)

graph.add_node("first", first_node)
graph.add_node("second", second_node)

graph.add_edge(START, "first")
graph.add_edge("first", "second")
graph.add_edge("second", END)

app = graph.compile()

# app.invoke({})

# for CommerceOps

state = {
    "question": "How many iPhone 16 units are in stock?"
}

def receive_question(state):
    print("Question:", state["question"])
    return state


def generate_answer(state):
    print("Generating answer.")
    return state

graph = StateGraph(dict)

graph.add_node(
    "receive_question",
    receive_question
)

graph.add_node(
    "generate_answer",
    generate_answer
)

graph.add_edge(
    START,
    "receive_question"
)

graph.add_edge(
    "receive_question",
    "generate_answer"
)

graph.add_edge(
    "generate_answer",
    END
)

app = graph.compile()

# app.invoke({
#     "question": "How many iPhone 16 units are in stock?"
# })

# better example -> Stateful graph execution

def receive_question(state):
    state["received"] = True
    return state


def analyze_question(state):
    state["intent"] = "inventory"
    return state


def generate_answer(state):
    state["answer"] = "The question is about inventory."
    return state

graph = StateGraph(dict)

graph.add_node(
    "receive_question",
    receive_question
)
graph.add_node(
    "analyze_question",
    analyze_question
)

graph.add_node(
    "generate_answer",
    generate_answer
)

graph.add_edge(
    START,
    "receive_question"
)

graph.add_edge(
    "receive_question",
    "analyze_question"
)

graph.add_edge(
    "analyze_question",
    "generate_answer"
)

graph.add_edge(
    "generate_answer",
    END
)

app = graph.compile()

result = app.invoke({
    "question": "How many iPhone 16 units are in stock?"
})

# print(result)

# CommerceOps example with inventory check

def check_inventory(state):
    inventory = {
        "iPhone 16": 42,
        "Samsung S24": 18
    }

    product = state["product"]

    state["inventory"] = inventory.get(
        product,
        "Product not found"
    )

    return state

def format_result(state):
    state["answer"] = (
        f"{state['product']} has "
        f"{state['inventory']} units in stock."
    )

    return state

graph = StateGraph(dict)

graph.add_node(
    "check_inventory",
    check_inventory
)

graph.add_node(
    "format_result",
    format_result
)

graph.add_edge(
    START,
    "check_inventory"
)

graph.add_edge(
    "check_inventory",
    "format_result"
)

graph.add_edge(
    "format_result",
    END
)

app = graph.compile()

result = app.invoke({
    "product": "iPhone 16"
})

# print(result)