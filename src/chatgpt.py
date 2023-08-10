import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('API_KEY')

if not os.path.exists('prompt.txt'):
    raise Exception('No prompt.txt file found')

"""Enter custom system prompt to change the bot's personality"""
with open('prompt.txt', 'r') as file:
    SYSTEM_PROMPT = file.read().replace('\n', ' ')

def chatgpt_response(prompt: str, memory):
    memory.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, *memory],
        max_tokens=100,
        temperature=1
    )
    message_content = response['choices'][0]['message']
    memory.append(message_content.to_dict())
    return message_content['content']
