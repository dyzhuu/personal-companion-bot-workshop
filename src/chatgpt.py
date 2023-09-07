import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('API_KEY')

path = os.path.join(os.path.dirname(__file__), "prompt.txt")

if not os.path.exists(path):
    raise Exception('No prompt.txt file found')

# Enter custom system prompt to change the bot's personality
with open(path, 'r') as file:
    SYSTEM_PROMPT = file.read().replace('\n', ' ')

# this is the main funciton for generating a response
def chatgpt_response(prompt: str):
    # TODO: Implement chatgpt_response function via openai chat completion api
    # https://platform.openai.com/docs/guides/gpt/chat-completions-api
    pass