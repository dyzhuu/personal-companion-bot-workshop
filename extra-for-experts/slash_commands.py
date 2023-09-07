from typing import Optional

import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

MY_GUILD = discord.Object(id=0)  # replace with your guild id


class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree holds all the application commands.
        self.tree = app_commands.CommandTree(self)

    # Synchronises the app commands to one guild.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def on_ready(self):
        print(f'Logged in as {client.user} 🤖')


intents = discord.Intents.default()
client = DiscordClient(intents=intents)


@client.tree.command()
# see how to use the interaction object here https://discordpy.readthedocs.io/en/latest/interactions/api.html?highlight=interaction#discord.Interaction
# says hello to the user
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
# this describes what the inputs do to the user
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
# The arguments (excluding interaction) are the inputs to the slash command
# adds two numbers together
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


@client.tree.command()
# this changes what appears on discord, so the user sees 'text' instead of 'text_to_send'
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
# sends the text into the current channel
async def send(interaction: discord.Interaction, text_to_send: str):
    await interaction.response.send_message(text_to_send)


# to make an argument optional, you can either give it a default argument or mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
# says when the user joined
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    # if no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # the format_dt function formats the date time into a human readable representation in the official client
    # this message is sent with ephemeral=True, so only the person who invoked the command can see it
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}', ephemeral=True)

# creating a custom embed
# learn more about embeds here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
@client.tree.command()
async def embed(interaction: discord.Interaction, title: str, description: str):
    embed = discord.Embed(title=title, description=description)

    # you can also change elements like this
    # embed.description = description

    embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)


client.run(TOKEN)