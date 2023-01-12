import discord
import datetime

USER_ID = 688786931748044821
CHAR_LIMIT = 100
WORD_LIMIT = 10

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

user = None
chars_


@client.event
async def on_ready():
    global user
    user = await client.fetch_user(USER_ID)
    print(f"")
