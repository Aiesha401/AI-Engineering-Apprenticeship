from openai import OpenAI
from dotenv import load_dotenv
import chromadb
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-embed-1b"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_embedding(text):
    response = client.embeddings.create(
        model=MODEL,
        input=text
    )
    return response.data[0].embedding

db = chromadb.Client()

collection = db.create_collection(
    name="commerceops_custom"
)

documents = [
    "Employees may work remotely two days per week.",
    "Customers may return products and receive a full refund within 30 days of purchase.",
    "Orders over $100 receive free shipping.",
    "Inventory is updated every hour.",
    "After purchasing a product, customers receive an email confirmation."
]

embeddings = []

for document in documents:
    embeddings.append(
        get_embedding(document)
    )

print(len(embeddings))

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5"
    ]
)

query = "How many days do i have for refund?"

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[
        query_embedding
    ],
    n_results=1
)

print(results["documents"])

questions = [
    "Can I return my order?",
    "Do you offer free delivery?",
    "Will I get an email after buying?",
    "How often is stock updated?"
]

for question in questions:
    query_embedding = get_embedding(question)
    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=1
    )
    print(results["documents"])