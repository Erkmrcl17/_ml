import ollama

def chat_llama(prompt):
    response = ollama.chat(model='llama3:2.3b', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

print("Chatbot Llama 3")
while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: bye!")
        break
    response = chat_llama(user_input)
    print("Bot:", response)
