import google.generativeai as genai
import os

# Directly use the API key as a string
API_KEY = 'AIzaSyDxmdNcCmXeeAP_9jJBwfmVnFAguyFPnfU'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(name='gemini-1.5-flash')
response = model.generate_content('Teach me about how an LLM works')

print(response.text)