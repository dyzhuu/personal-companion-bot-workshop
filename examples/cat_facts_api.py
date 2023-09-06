# Example implementation of the Cat Fact API

import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv('TOKEN')
catfact_url = "https://catfact.ninja/fact"

@client.command()
async def meow(ctx):
    async with ctx.typing():
        response = requests.get(catfact_url)

        if response.status_code == 200:
            catfact_data = response.json()
            cat_fact = catfact_data['fact']
            await ctx.send(f"🐱 Fun Cat Fact: {cat_fact}")
        else:
            await ctx.send("Sorry, I couldn't fetch a cat fact at the moment.")

client.run(TOKEN)