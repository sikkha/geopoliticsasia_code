import openai
import re
import os

# Initialize the OpenAI API key
#openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to prompt the GPT-3 language model with user input
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        api_key="OPENAI_API_KEY"
        #replace your own openai api in the api_key above, it's better to set it in the OpenAI API key system shell variable
    )
    message = response.choices[0].text.strip()
    return re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', message)

# Define a function to handle the conversation
def chat():
    conversation_history = "Chatbot: Hi, I'm a chatbot. How can I help you?\n"
    print(conversation_history.strip())

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Chatbot: Goodbye!")
            break

        conversation_history += f"You: {user_input}\n"
        conversation_history += "Chatbot: "
        response = ask_gpt(conversation_history)
        print("Chatbot:", response)

        conversation_history += f"{response}\n"

# Start the conversation
chat()
