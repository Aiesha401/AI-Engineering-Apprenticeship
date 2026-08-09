from openai import OpenAI
from dotenv import load_dotenv
import chromadb
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
EMBED_MODEL = "nvidia/nemotron-3-embed-1b"

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.getenv("NVIDIA_API_KEY")
)

def get_embedding(text):
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return response.data[0].embedding

documents = [
    "Employees may work remotely two days per week.",
    "Customers may return products and receive a full refund within 30 days of purchase.",
    "Orders over $100 receive free shipping.",
    "Inventory is updated every hour.",
    "After purchasing a product, customers receive an email confirmation.",
    "Invoices must be submitted within 14 days of the purchase date.",
    "Managers must approve invoices above $5,000.",
    "Customer support tickets should be answered within 24 hours."
]

embeddings = [get_embedding(document) for document in documents]

db = chromadb.Client()

collection = db.create_collection(
    name="commerceops_final"
)

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5",
        "doc6",
        "doc7",
        "doc8"
    ]
)

# query = "How quickly should customer support respond to a customer asking about a refund?"

# query_embedding = get_embedding(query)

# results = collection.query(
#     query_embeddings=[query_embedding],
#     n_results=3
# )

# print(results["documents"])
# print(results["distances"])

# documents_found = results["documents"][0]
# distances = results["distances"][0]

# MAX_DISTANCE = 0.8

# filtered_documents = []

# for document, distance in zip(documents_found,distances):
#     if distance < MAX_DISTANCE:
#         filtered_documents.append(document)

# # print("Filtered documents:")
# # print(filtered_documents)

# context = "\n".join(
#     filtered_documents
# )

# # print(context)

# response = client.chat.completions.create(
#     model=MODEL,
#     messages=[
#         {
#             "role": "system",
#             "content": (
#                 "You are CommerceOps AI.\n"
#                 "Answer only using the provided context.\n"
#                 "If the answer is not present in the context, say "
#                 "'I don't have enough information in the provided documents.'"
#             )
#         },
#         {
#             "role": "user",
#             "content": f"""
# Context:

# {context}

# Question:

# {query}
# """
#         }
#     ]
# )

# print(response.choices[0].message.content)

questions = [
    "How long do I have to submit an invoice?",
    "Who needs to approve large invoices?",
    "How quickly should customer support respond?",
    "Can employees work from home?",
    "How often is inventory updated?",
    "Do customers receive an email after purchasing?",
]

for question in questions:
    query_embedding = get_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    documents_found = results["documents"][0]
    distances = results["distances"][0]

    MAX_DISTANCE = 0.8

    filtered_documents = []

    for document, distance in zip(documents_found, distances):
        if distance < MAX_DISTANCE:
            filtered_documents.append(document)
    
    context = "\n".join(
        filtered_documents
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages =[
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
                "role": "user",
                "content": f"""
                            Context:

                            {context}

                            Question:

                            {question}
                
                            """
            }
        ]
    )
    print("=="*50)
    print(question)
    print(response.choices[0].message.content)
