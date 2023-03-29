import openai
import re
import os
import requests
import json


# Initialize the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to prompt the GPT-3 language model with user input
def ask_gpt(prompt, engine_name):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }
    data = {
        "model": engine_name,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        #"max_tokens": 1024,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    response_json = response.json()
    
    if 'choices' in response_json and len(response_json['choices']) > 0:
        message = response_json['choices'][0]['message']['content'].strip()
    else:
        message = "Sorry, I couldn't generate a response."

    # return re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', message)
    return message  # Return the message without filtering characters


# Define a function to handle the conversation
def chat(engine_name):
    conversation_history = "Chatbot: Hi, I'm a chatbot. How can I help you?\n"
    print(conversation_history.strip())

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Chatbot: Goodbye!")
            break

        conversation_history += f"You: {user_input}\n"
        conversation_history += "Chatbot: "
        response = ask_gpt(conversation_history, engine_name)
        # print("History: [", conversation_history, "]")
        print("Chatbot:", response)

        conversation_history += f"{response}\n"

# Start the conversation with a specific engine
engine_name = "gpt-4"  
chat(engine_name)


