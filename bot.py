import discord
import os
from dotenv import load_dotenv

import random
load_dotenv()
token =os.getenv('token')
# discord bot token added

# from config import token
intents=discord.Intents(messages=True)
client = discord.Client(intents=intents) 
# discord login
@client.event 
async def on_ready():
     print('We have logged in as {0.user} '.format(client))
     
@client.event
async def on_message(message):
    if message.author == client.user:
         return
      
    
    async def meet(ctx):
        await ctx.send(ctx.author)
        await client.say({}.format(arg))
        await ctx.channel.send(arg)
    
    


client.run(token)

