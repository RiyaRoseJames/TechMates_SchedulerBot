import discord
import random
# discord bot token added

TOKEN= "MTA1MzU0NjgwMDI5Mzg4Mzk2NA.GM8VOO.PPa4wjCCcikj5bmaNFsbFtrVOsedjEb3K0xpRw"
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
     
    # client message
    if message.channel.send('/can we conduct meeting at 10'): 
        # bot reply
       
     await message.channel.send("please text your email id")
    


client.run(TOKEN)



