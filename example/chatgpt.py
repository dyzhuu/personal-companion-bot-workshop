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
def chatgpt_response(prompt: str, memory):
    memory.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        # this is the pre-trained model used to
        model="gpt-3.5-turbo",
        # this is the input message. Notice that we prepend the system prompt to set the bot's 'personality'
        # the API recognises the current message as being at the end of the list, and uses the other messages for context
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, *memory],
        # sets the maximum tokens in the response
        max_tokens=100,
        # adjusts the model temperature (how 'creative' it can be with its responses)
        temperature=1
    )
    # use this syntax to traverse JSON
    message_content = response['choices'][0]['message']
    # once we have the message, append it to the memory list.
    memory.append(message_content.to_dict())
    return message_content['content']
