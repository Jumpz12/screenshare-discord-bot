import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import time

client = discord.Client() 

@client.event 
async def on_ready():
    print("Online and Ready to Hang!")
    await client.change_presence(game=discord.Game(name="Hangout | #hangout"))