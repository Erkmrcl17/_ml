import ollama

response = ollama.chat(model='llama3:2.3b', messages=[{'role': 'user', 'content': "what is the delicious food in indonesia"}])
print(response["message"]["content"])