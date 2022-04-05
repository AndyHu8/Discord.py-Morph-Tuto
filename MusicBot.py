import discord
from discord.utils import get
import time

class MyClient(discord.Client): #erbt von Discord Client

    #Einloggen
    async def on_ready(self): #überschreibt die on_ready
        print('Ich habe mich eingeloggt')

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):

        if message.author == client.user:
            return
        
        if message.content == "!help":
            print("Help")

        if message.content.startswith("!play"): #!play General
            where = message.content.split(" ")[1] #Channel
            channel = get(message.guild.channels, name = where)
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio('Datei'))

            while voicechannel.is_playing(): #solange Musik abspielen
                time.sleep(5)
            voicechannel.play(discord.FFmpegPCMAudio('Datei'))

            if voicechannel.is_paused(): #wenn nichts abspielen
                pass
       
            

client = MyClient()
client.run('')