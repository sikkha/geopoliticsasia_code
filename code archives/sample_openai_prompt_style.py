import openai
import re
import os


openai.api_key = "YOUR_KEY_HERE"
response = openai.Completion.create(
#  engine="text-davinci-002",
  engine="text-davinci-002",
#  prompt="What is the current geopolitical situation between China and the United States?",
  temperature=0.7,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
)

generated_text = response.choices[0].text.strip()
print(generated_text)
