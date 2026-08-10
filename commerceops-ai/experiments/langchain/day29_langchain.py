from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

model = ChatOpenAI(
    model=MODEL,
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0.2
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are CommerceOps AI.

        Explain business concepts clearly to employees.
        """
    ),
    (
        "human",
        """
        Explain {concept}.

        Employee experience level:
        {experience}

        Keep the explanation under {words} words.
        """
    )
])

chain = prompt | model

response = chain.invoke({
    "concept": "semantic search",
    "experience": "beginner",
    "words": 75
})

print(response.content)

# response = chain.invoke({
#     "concept": "inventory management",
#     "experience": "beginner",
#     "words": 100
# })

# print(response.content)

# response = model.invoke(
#     "Explain embeddings in simple terms."
# )

# print(response.content)

# prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in simple terms."
# )

# chain = prompt | model

# response = chain.invoke({
#     "topic": "embeddings"
# })

# print(response.content)

# prompt = ChatPromptTemplate.from_template(
#     """
#     Explain {topic} to a {audience}.
#     Keep the explanation under {words} words.
#     """
# )

# messages = prompt.format_messages(
#     topic="RAG",
#     audience="beginner",
#     words=100
# )

# print(messages[0].content)