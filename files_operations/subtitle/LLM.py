from ollama_test import chat

# simple example
response = chat(model="gemma-3-1b-it", messages=[{"role": "user", "content": "Translate 'Hello' to Chinese."}])
print(response)
