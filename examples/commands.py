from typing import Optional

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

# if you are not using a class, you can instanstiate the client in one line:
# client = commands.Bot(command_prefix="!", intents=intents)

# make sure you are using commands.Bot instead of discord.Client
# commands.Bot is a subclass of discord.Client so many of the same methods still work
class DiscordClient(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f'Logged in as {client.user} 🤖')

    async def on_message(self, message):
        # this line is absolutely mandatory if you are using commands with on_message, otherwise commands won't process
        await self.process_commands(message)

        pass # proceed to process the message

client = DiscordClient(intents=intents)

@client.command()
# says hello back to the user
async def hello(ctx):
    await ctx.send(f'Hi, {ctx.author.mention}')

@client.command()
# finds a random number between 1 and the provided number e.g. !random 6
async def random(ctx, upper: int):
    await ctx.send(randint(1, upper))

@client.command()
# adds numbers together e.g. !add 1 2 3
# the function only takes the first argument of the command, to take multiple arguments, use *args
async def add(ctx, *args: int): # *args is a tuple
    await ctx.send(f'{" + ".join(map(str, args))} = {sum(args)}')

client.run(TOKEN)