import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import time

client = discord.Client() 

token = "PUT TOKEN HERE"

@client.event 
async def on_ready():
    print("Online and Ready to Hang!")
    await client.change_presence(game=discord.Game(name="Hangout | >hangout"))

@client.event
async def on_message(message):

    if message.content == ">hangout":
        if message.author.voice.voice_channel != None:
            voice_channel = message.author.voice.voice_channel.id
            url = "https://discordapp.com/channels/" + str(message.server.id) + "/" + str(voice_channel)
            members = message.author.voice.voice_channel.voice_members
            invite = discord.Embed(description = "You have been invited to a Hangout: \n" + str(url), color = 0x59b1ff)
            for member in members:
                await client.send_message(member, embed = invite)

            complete = discord.Embed(description = "You're invite has been sent out!", color = 0x5adb51)
            await client.send_message(message.channel, embed = complete)
        else:
            failed = discord.Embed(description = "You are not in a voice channel!", color = 0xffa13d)
            await client.send_message(message.channel, embed = failed)





client.run(token)

#https://discordapp.com/channels/417847824873422851/545467222815014913