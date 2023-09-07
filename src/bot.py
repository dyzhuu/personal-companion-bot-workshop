import discord
import os

from chatgpt import chatgpt_response
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_ID = int(os.getenv('BOT_ID'))

class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged in as {client.user} 🤖')

    async def on_message(self, message):
        # return if the author of the message is the bot, so we avoid a infinite loop
        if message.author == client.user:
            return

        # TODO: Check if the message tags the bot

        response = chatgpt_response(message.content)

        # TODO: Send the response to the channel the message was sent in
        


intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)