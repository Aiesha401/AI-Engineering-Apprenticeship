# Day 4

## What did I build?

Today I built my first multi-turn AI chatbot. Instead of asking the LLM one question at a time, I created a chatbot that stores the entire conversation history in a `messages` list. The chatbot keeps chatting until I type `exit` and remembers previous messages during the conversation.

## What did I learn?

- How conversation memory works in LLM applications.
- LLMs do not actually remember anything by themselves.
- The application is responsible for storing and sending previous messages.
- Why both the user's messages and the assistant's responses need to be stored.
- Why `messages` is a list and why we use `append()`.
- Why `while True` is the best choice for a chatbot.
- How `break` exits the conversation loop.
- What a context window is and why sending the entire conversation becomes expensive.
- How Python list slicing like `messages[-10:]` can be used to send only recent messages.
- Why model selection matters and that a smaller model can sometimes give a much better user experience.
- How `load_dotenv()` loads environment variables from the `.env` file.

## Biggest challenge today

The biggest challenge was understanding how an AI chatbot remembers previous messages. I initially thought the model itself remembered the conversation. Another challenge was waiting for responses because the 70B model was extremely slow.

## How did I solve it?

I learned that the chatbot remembers because my Python program stores every message in a list and sends the complete conversation back to the model on every request. Later, I switched from the 70B model to the Llama 3.1 8B model, which made the responses almost instant while still maintaining the conversation.

## What surprised me?

The biggest surprise was discovering that the model doesn't actually have memory. I proved this by restarting the program. After restarting, the `messages` list became empty, and the model immediately forgot my name. That experiment made me understand that the application's memory is what makes the chatbot appear intelligent.

## One thing I still don't understand

I still want to learn how applications like ChatGPT remember conversations even after I close and reopen them. I know it isn't the model itself, so I'm excited to learn how databases, persistent memory, vector databases, and RAG solve this problem.