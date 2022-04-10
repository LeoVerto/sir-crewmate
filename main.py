import re

import discord
import logging

import config

logging.basicConfig(level=logging.INFO)
client = discord.Client()


def get_emoji(guild, name):
    for emoji in guild.emojis:
        if emoji.name == name:
            return f"<{name}:{emoji.id}>"


@client.event
async def on_ready():
    logging.info(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.match(r"(amo(ng ?|g)|s)us", message.content):
        await message.add_reaction(get_emoji(message.guild, "crewmite"))

client.run(config.DISCORD_TOKEN)
