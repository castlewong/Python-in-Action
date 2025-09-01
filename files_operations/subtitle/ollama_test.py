import ollama

response = ollama.chat(model="gemma:2b", messages=[
    {"role": "system", "content": "You are a translation engine. Always translate text directly without explanation."},
    {"role": "user", "content": "Translate to Japanese: Hello, how are you? Only output the Japanese sentence, nothing else."}
])

print(response["message"]["content"])
