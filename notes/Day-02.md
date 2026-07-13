# Day 2

## What did I build?

My first AI application that connected to NVIDIA's Llama 3.3 70B model using the OpenAI-compatible SDK. I successfully sent a prompt to the model and received a generated response.

## What did I learn?

What an API is.
Why API keys are needed.
Why we store secrets in a .env file.
How python-dotenv loads environment variables.
What an API client is.
Difference between configuration and execution.
Why messages is a list.
Why LLMs don't remember conversations between API calls.
Difference between a request and a response.
Basic HTTP errors like 504 Gateway Timeout.
Why real-world APIs can fail even when our code is correct.

## Biggest challenge today

Understanding why load_dotenv() returned None even though the API key was present.

## How did I solve it?

I discovered that my experiments folder was outside my project folder, so Python couldn't find the .env file. After moving it inside the project and running the script from the project root, the API key loaded successfully.

Later, I also learned that a 504 Gateway Timeout was a server-side issue, not a coding mistake.

## What surprised me?

I was surprised that even a correctly written program can fail because of network or server issues. I also learned that the model doesn't actually "remember" previous conversations—our application has to send the conversation history every time.

## One thing I still don't understand:

I still want to understand how ChatGPT remembers an entire conversation if LLMs don't have memory. I also want to understand what's inside the response object beyond the generated text.