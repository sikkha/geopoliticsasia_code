from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate a response using GPT-2
def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs, 
        max_length=150, 
        num_return_sequences=1,
        temperature=0.8,  # Adjust the temperature to control randomness
        top_p=0.9,  # Use nucleus sampling to reduce repetition
        repetition_penalty=1.2,  # Apply a repetition penalty to discourage repeating phrases
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Interactive chat loop
print("Chatbot is ready to talk! (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break

    response = generate_response(user_input)
    print("Chatbot: " + response)

