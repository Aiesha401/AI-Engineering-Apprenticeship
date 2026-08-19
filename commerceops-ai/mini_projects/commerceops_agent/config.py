from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    raise ValueError(
        "NVIDIA_API_KEY is not set."
    )


client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY
)