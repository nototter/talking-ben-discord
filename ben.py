import random
import string
from nacl.utils import *
import subprocess
import discord
from discord.ext import commands
import asyncio
import random
import sys
import time
import requests
from discord.utils import get

# I UNDERSTAND THIS CODE IS DOGSHIT AND I CAN MAKE IT BETTER BUT I DO NOT WANT TO
# please give credits if you do use this though thanks :pray:

beninplace = "no"

class MyClient(discord.Client):
    global beninplace

    async def on_message(self, message):
        global beninplace
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('ben'):
            if beninplace == "no":
                print("started a call")

                def is_correct(m):
                    return m.author == message.author

                while True:
                    beninplace = "yes" # to prevent multiple bens

                    beanchance = range(0, 20)

                    endcallchance = range(68, 70)

                    gifchance = range(31,32)

                    bentalk = random.randint(1,4)
                    bengif = random.randint(30,40)
                    end = random.randint(1,100)

                    if bengif != 32:
                        if bentalk == 1:
                            await message.channel.send("yes")
                        elif bentalk == 2:
                            await message.channel.send("no")
                        elif bentalk == 3:
                            await message.channel.send("hohoho")
                        elif bentalk == 4:
                            await message.channel.send("**blugh**")
                        if end in endcallchance:
                            print(end)
                            await message.channel.send("***ben ended the call***")
                            beninplace = "no"
                            return
                        if end in beanchance:
                            await message.channel.send("***ben eats can of beans***")

                    elif bengif == 32:
                        await message.channel.send("https://tenor.com/view/ben-talking-ben-gif-24982337")

                    print(end)

                    try:
                        guess = await self.wait_for('message', timeout=30.0)
                    except asyncio.TimeoutError:              
                        beninplace = "no"
                        print("ended the call due to nobody responding")
                        await message.channel.send('**ben ended the call**')
                        return

                        

bot = MyClient()

bot.run('tokenhere')
