from openai import OpenAI
from dotenv import load_dotenv
import chromadb
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
EMBED_MODEL = "nvidia/nemotron-3-embed-1b"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_embedding(text):
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )

    return response.data[0].embedding

db = chromadb.Client()

collection = db.create_collection(
    name="commerceops_rag"
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

query = "Can I return my laptop?"

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

# print(results["documents"])

context = "\n".join(
    results["documents"][0]
)

# print(context)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
    "role": "system",
    "content": (
        "You are CommerceOps AI.\n"
        "Answer only using the provided context.\n"
        "If the answer is not present in the context, say "
        "'I don't have enough information in the provided documents.'"
            )
        },
        {
            "role":"user",
            "content":f"""
                        Context:

                        {context}

                        Question:

                        {query}
            
                        """
        }
    ]
)

print(response.choices[0].message.content)