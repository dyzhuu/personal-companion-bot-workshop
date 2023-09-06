import discord
import os

from chatgpt import chatgpt_response
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_ID = int(os.getenv('BOT_ID'))

MAX_MEMORY_SIZE = 10

class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.memory = []

    async def on_ready(self):
        print(f'Logged in as {client.user} 🤖')

    async def on_message(self, message):
        # return if the author of the message is the bot, so we avoid a infinite loop
        if message.author == client.user:
            return
        try:
            # check if the message tags the bot
            if message.mentions[0].id == BOT_ID:
                # the line below shows the `Bot is typing...` message when loading
                async with message.channel.typing():
                    # invokes the chatgpt function and generates a message
                    response = chatgpt_response(message.content, self.memory)
                    await message.channel.send(response)
        except:
            pass

        # Truncate message history to decrease api token usage
        if len(self.memory) > MAX_MEMORY_SIZE:
            self.memory = self.memory[-MAX_MEMORY_SIZE:]


intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)