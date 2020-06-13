from datetime import datetime
import random
import re
import socket
import string
from cryptography.fernet import Fernet
import uuid
from getmac import get_mac_address as gma

# def get_random_alphaNumeric_string(stringLength=8):
#     lettersAndDigits = string.ascii_uppercase + string.digits
#     return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
#
# print(get_random_alphaNumeric_string(32))
#
# for i in range(0,30):
#     print(get_random_alphaNumeric_string(16))

import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(712460856608423966)
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.set_author(name="Update vX.X.X")
    embed.add_field(name="New Features", value="-Feature 1\n-Feature 2\n", inline=True)
    embed.set_footer(
        text=str(datetime.now().strftime("%I:%M:%S")) + " | Made by: nokiny#8596",
        icon_url="https://cdn.discordapp.com/avatars/164478290168381450/128d382f3a8a3c66d7416fc2d72c68e0.webp?size=128")
    embed.set_image(url="https://gyazo.com/650899670c9b27e0a39c19a83dd0f4af.gif")
    await channel.send(embed=embed)
    file = discord.File(r"D:\Users\Andrew\Downloads\650899670c9b27e0a39c19a83dd0f4af.gif", filename="test.gif")
    await channel.send(file=file)

client.run('NzE3NDY1OTQwMzAzODA2NDg2.XtauXA.u5qRRdoi6V32NtEbWyRQVGWeflU')
