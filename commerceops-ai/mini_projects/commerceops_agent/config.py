from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)