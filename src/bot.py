import discord
import os

from discord import Intents

from chatgpt import chatgpt_response
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_ID = int(os.getenv('BOT_ID'))

MAX_MEMORY_SIZE = 10

class DiscordClient(discord.Client):

    def __init__(self, *, intents: Intents, **options):
        super().__init__(intents=intents, **options)
        self.memory = []

    async def on_ready(self):
        print(f'Logged in as {client.user} 🤖')

    async def on_message(self, message):
        if message.author == client.user:
            return
        try:
            if message.mentions[0].id == BOT_ID:
                async with message.channel.typing():
                    response = chatgpt_response(message.content, self.memory)
                    await message.channel.send(response)
        except:
            pass

        """Truncate message history to decrease api token usage"""
        if len(self.memory) > MAX_MEMORY_SIZE:
            self.memory = self.memory[-MAX_MEMORY_SIZE:]


intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
