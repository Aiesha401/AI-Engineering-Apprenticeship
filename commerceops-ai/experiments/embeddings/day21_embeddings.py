from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-embed-1b"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def cosine_similarity(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1,vec2)/ (
        np.linalg.norm(vec1) *
        np.linalg.norm(vec2)
    )

def get_embedding(text):
    response = client.embeddings.create(
        model=MODEL,
        input=text
    )
    return response.data[0].embedding


embedding1 = get_embedding("I love AI.")
embedding2 = get_embedding("I enjoy artificial intelligence.")
embedding3 = get_embedding("Pizza is delicious.")

print(cosine_similarity(embedding1,embedding2))
print(cosine_similarity(embedding2,embedding3))

# response = client.embeddings.create(
#     model=MODEL,
#     input="I love artificial intelligence."
# )

# embedding = response.data[0].embedding

# print(type(embedding))
# print(len(embedding))
# print(embedding[:10])