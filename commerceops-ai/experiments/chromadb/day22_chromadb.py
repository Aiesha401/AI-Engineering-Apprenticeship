import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="commerceops"
)

collection.add(
    documents=[
        "Employees may work remotely two days per week.",
        "Refunds are accepted within 30 days.",
        "Orders over $100 receive free shipping.",
        "Inventory is updated every hour.",
        "Customers receive email notifications after purchase."
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5"
    ]
)

results = collection.query(
    query_texts=[
        "Can I return my order?",
        "Do you offer free delivery?",
        "Will I get an email after buying?",
        "How often is stock updated?"
    ],

    n_results=1
)

questions = [
    "Can I return my order?",
    "Do you offer free delivery?",
    "Will I get an email after buying?",
    "How often is stock updated?"
]

for question, answer in zip(
    questions,
    results["documents"]
):
    print(f"Question: {question}")
    print(f"Retrieved: {answer[0]}")
    print()