import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

token = "PUT TOKEN HERE"

client = discord.Client() 

@client.event 
async def on_ready():
    print("Online and Ready to Hang!")
    await client.change_presence(activity = discord.Game("Hangout | >hangout"))

@client.event
async def on_message(message):
    if message.content == ">hangout":
        if message.author.voice != None:
            voice_channel = message.author.voice.channel.id
            url = "https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(voice_channel)
            members = message.author.voice.channel.members
            invite = discord.Embed(description = "You have been invited to a Hangout: \n" + str(url), color = 0x59b1ff)
            for member in members:
                if member.dm_channel == None:
                   await member.create_dm()
                await member.dm_channel.send(embed = invite)
            complete = discord.Embed(description = "You're invite has been sent out!", color = 0x5adb51)
            await message.channel.send(embed = complete)
        else:
            failed = discord.Embed(description = "You are not in a voice channel!", color = 0xffa13d)
            await message.channel.send(embed = failed)

client.run(token)
