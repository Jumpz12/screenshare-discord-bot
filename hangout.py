import discord
import asyncio
import os
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
    if message.author == client.user:
        return False
    server = message.guild
    os.chdir(os.path.dirname(__file__))
    location = os.getcwd()+"/servers/"
    if not os.path.exists(location):
        os.makedirs(location)
    if not os.path.exists(location+str(server.id)):
        os.makedirs(location+str(server.id))

    file_name = location+str(server.id)+r"\prefix.txt"
    file = open(file_name, "a+")
    file.close
    file = open(file_name, "r")
    length = sum(1 for line in file)
    if length == 0:
        file.close
        file = open(file_name, "w")
        file.write(">")
        file.close
        file = open(file_name, "r")
        file.close
    else:
        file.close

    file = open(file_name, "r")
    line = file.readline()
    prefix = line
    file.close
    
    if message.content == prefix + "hangout":
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

    elif message.content == prefix + "prefix":
        if not message.channel.permissions_for(message.author).manage_messages:
            prefix_permissions_failed = discord.Embed(description = "You do not have the correct permissions to change the prefix", color = 0xffa13d)
            await message.channel.send(embed = prefix_permissions_failed)
        else:
            prefix_change = discord.Embed(description = "What would you like to change the prefix to?", color = 0x59b1ff)
            await message.channel.send(embed = prefix_change)

            def check(m):
                return m.author == message.author and m.channel == message.channel          

            reply = await client.wait_for('message', check = check)
            file = open(file_name, "w")
            file.write(reply.content)
            file.close
            prefix = reply.content
            prefix_success = discord.Embed(description = "Prefix changed to " + prefix, color = 0x5adb51)
            await message.channel.send(embed = prefix_success)
 

client.run(token)
