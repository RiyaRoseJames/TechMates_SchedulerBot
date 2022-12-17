import discord
import random
import os
from dotenv import load_dotenv
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
load_dotenv()
# token imported from .env file
token=os.getenv('token')
#to enable and disable certain gateway events from triggering and being send
intents=discord.Intents.all()               
client = discord.Client(intents=intents) 
@client.event         #event handler
async def on_ready():
    # succesfull login of the bot
    print('We have logged in as {0.user} '.format(client))
     
@client.event
async def on_message(message): 
    print("message->", message.content)
    if message.author == client.user:
         return
    #spliting and assigning values to variables
    if message.content.startswith('bot'):
        message_body = message.content.split(' ')
        meeting_name = message_body[1]
        email_id = message_body[2]
        time_t = message_body[3]
        msg = f"meeting name -> {meeting_name}\t mail id - {email_id}, time - {time_t}"
        #bot response
        await message.channel.send(msg)
    


client.run(token)
