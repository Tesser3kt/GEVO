from datetime import datetime as dt, timedelta as td
import discord

TOKEN = 'MTA2MjgyNjA5OTIyNDA5MjczMg.GoFrE0.Gxps1zynVGrmJ57fNyklU4ZBGhcPS-bjevMEdM'
USER_ID = 865664712842018848
CHAR_LIMIT = 100
WORD_LIMIT = 10
MAX_WARNINGS = 5

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

user = None
chars_written = 0
words_written = 0
time_banned = None
max_warnings = 0


@client.event
async def on_ready():
    global user
    user = await client.fetch_user(USER_ID)
    await user.send(f"Dear {user.name}, Your private word-counting "
                    f"butler is ready to serve you!")


@client.event
async def on_message(message):
    global chars_written
    global words_written
    global time_banned
    global max_warnings
    if message.author == user:
        if time_banned and dt.now() - time_banned > td(days=1):
            chars_written = 0
            words_written = 0
        chars_written += len(message.content)
        words_written += len(message.content.split())
        if chars_written > CHAR_LIMIT:
            await message.delete()
            chars_written -= len(message.content)
            words_written -= len(message.content.split())
            time_banned = dt.now()
            if max_warnings < MAX_WARNINGS:
                await message.channel.send(f"Dear {user.name}, You have exceeded the character limit for today!")
                max_warnings += 1
        if words_written > WORD_LIMIT:
            await message.delete()
            chars_written -= len(message.content)
            words_written -= len(message.content.split())
            time_banned = dt.now()
            if max_warnings < MAX_WARNINGS:
                await message.channel.send(f"Dear {user.name}, You have exceeded the word limit for today!")
                max_warnings += 1

client.run(TOKEN)
