# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:20:47 2021

@author: Axel
"""

# first test using tuto https://realpython.com/how-to-make-a-discord-bot-python/#what-is-a-bot

#Spyder and async conflict, https://github.com/erdewit/nest_asyncio solved

import os

import nest_asyncio
nest_asyncio.apply() # spyder conflict solution, needs to be put before importing discord /!\, just after asyncio import
import discord
from dotenv import load_dotenv
from discord.ext import commands



# loads .env file in the current directory to add 'local' environment variables to my shell
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!') # use with bot decorator

"""
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            break

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content == '!spyLis': # ask Spydis to listen in the voice channel the user is connected to
        response = "Will listen where "+str(message.author)+" is connected : "
        #print(response)
        await message.channel.send(response)
    
"""

@bot.command(name='spylis')
async def goListen(ctx):
    print("call goListen")
    sChannel = "Not connected to any voice channel"
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            sChannel = str(ctx.author.voice.channel)
    response = "Will listen where "+str(ctx.author.display_name)+" is connected : "+sChannel
    print(response)
    await ctx.send(response)


@bot.command(name='spymic')
async def goTell(ctx):
    sChannel = "Not connected to any voice channel"
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            sChannel = str(ctx.author.voice.channel)
    response = "Will transmit sound from listeners to where "+str(ctx.author.display_name)+" is connected : "+sChannel
    await ctx.send(response)












#client.run(TOKEN)
bot.run(TOKEN)









































