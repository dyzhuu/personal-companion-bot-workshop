# Example implementation of the Cat Fact API

import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = os.getenv('TOKEN')
catfact_url = "https://meowfacts.herokuapp.com/"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!meow'):
        async with message.channel.typing():
            response = requests.get(catfact_url)

            if response.status_code == 200:
                catfact_data = response.json()
                cat_fact = catfact_data['data'][0]
                await message.channel.send(f"🐱 Fun Cat Fact: {cat_fact}")
            else:
                await message.channel.send("Sorry, I couldn't fetch a cat fact at the moment.")

client.run(TOKEN)