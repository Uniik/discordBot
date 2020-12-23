# bot.py
import asyncio
import os
import sys
from datetime import datetime

import discord
from dotenv import load_dotenv

sys.setrecursionlimit(10**9)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
NAHWA = os.getenv('DISCORD_NAHWA')
ASSIM = os.getenv('DISCORD_ASSIM')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents.default()
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)


async def warn_nahwa(recidives):
    guild = await client.fetch_guild(SERVER)
    user = 0
    for member in client.get_all_members():
        did = int(NAHWA)
        if member.id == did:
            user = member
    status = user.status
    await user.create_dm()

    if user.raw_status != 'offline':
        if recidives == 1:
            await user.dm_channel.send(
                'Hi, its your darling telling you that it is getting really late and you should go to bed'
            )

        if recidives == 2:
            await user.dm_channel.send(
                'Babe! it is 1am! Please go to bed!'
            )

        if recidives == 3:
            await user.dm_channel.send(
                '2am... I will be really mad if you stay until 3am, i will call my master and wake him up :c'
            )
            master = await client.fetch_user(ASSIM)
            await master.create_dm()
            await master.dm_channel.send(
                'Master! your darling fucked up her sleep schedule! But dont forget you love her so dont stay mad too '
                'long '
            )


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await check_time()


async def check_time():
    # This function runs periodically every 1 second
    while True:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        if current_time == '23:59:00':  # check if matches with the desired time
            await warn_nahwa(1)

        if current_time == '01:00:00':  # check if matches with the desired time
            await warn_nahwa(2)

        if current_time == '02:00:00':  # check if matches with the desired time
            await warn_nahwa(3)

        await asyncio.sleep(1)



client.run(TOKEN)
