from datetime import datetime as dt, timedelta as td
import discord
import translators as ts
import translators.server as tss

TOKEN = 'MTA2MjgyNjA5OTIyNDA5MjczMg.GoFrE0.Gxps1zynVGrmJ57fNyklU4ZBGhcPS-bjevMEdM'
USER_IDS = [688786931748044821, 939276662024056832]
ERIC = 763720075227299870
CHAR_LIMITS = {
    688786931748044821: 100,
    939276662024056832: 100
}
WORD_LIMITS = {
    688786931748044821: 10,
    939276662024056832: 10
}
MAX_WARNINGS = {
    688786931748044821: 3,
    939276662024056832: 3
}

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.reactions = True

client = discord.Client(intents=intents)

users = []
chars_written = {}
words_written = {}
times_banned = {}
max_warnings = {}
eric = None


@client.event
async def on_ready():
    global user, eric
    global chars_written
    global words_written
    global times_banned
    global max_warnings
    for id in USER_IDS:
        try:
            user = await client.fetch_user(id)
            users.append(user)
            times_banned[id] = None
            chars_written[id] = 0
            words_written[id] = 0
            max_warnings[id] = 0
            # await user.send(f"Dear {user.name}, Your private word-counting "
            #                 f"butler is ready to serve you!")
        except Exception as e:
            pass

    try:
        eric = await client.fetch_user(ERIC)
        await eric.send("Avek sa kan dan la man.")
    except Exception as e:
        pass


@client.event
async def on_message(message):
    global users
    global chars_written
    global words_written
    global time_banned
    global max_warnings
    author = message.author
    if author in users:
        id = author.id
        if times_banned[id] and dt.now() - times_banned[id] > td(days=1):
            chars_written[id] = 0
            words_written[id] = 0
            max_warnings[id] = 0
        chars_written[id] += len(message.content)
        words_written[id] += len(message.content.split())
        if chars_written[id] > CHAR_LIMITS[id]:
            await message.delete()
            chars_written[id] -= len(message.content)
            words_written[id] -= len(message.content.split())
            times_banned[id] = dt.now()
            if max_warnings[id] < MAX_WARNINGS[id]:
                await message.channel.send(f"Dear {user.name}, You have exceeded the character limit for today!")
                max_warnings[id] += 1
        if words_written[id] > WORD_LIMITS[id]:
            await message.delete()
            chars_written[id] -= len(message.content)
            words_written[id] -= len(message.content.split())
            times_banned[id] = dt.now()
            if max_warnings[id] < MAX_WARNINGS[id]:
                await message.channel.send(f"Dear {user.name}, You have exceeded the word limit for today!")
                max_warnings[id] += 1

    if author.id == ERIC:
        if len(message.content) > 200:
            return
        await message.add_reaction("🇫🇷")
        phrase = message.content
        translated = tss.google(phrase, from_language="cs", to_language="fr")
        await message.reply(translated)


client.run(TOKEN)
