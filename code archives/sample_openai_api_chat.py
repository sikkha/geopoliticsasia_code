import openai
import re
import os

# Initialize the OpenAI API key
#openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to prompt the GPT-3 language model with user input

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
        api_key="YOUROWNOPENAIAPI" 
	#replace your own openai api in the api_key above, it's better to set it in the OpenAI API key system shell variable
    )
    message = response.choices[0].text.strip()
    return re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', message)

# Define a function to handle the conversation
def chat():
    print("Hi, I'm a chatbot. How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        response = ask_gpt(user_input)
        print("Chatbot:", response)

# Start the conversation
chat()

