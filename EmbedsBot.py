from datetime import datetime
from sqlite3 import Timestamp
import discord
from discord.utils import get
import datetime

class MyClient(discord.Client): #erbt von Discord Client

    #Einloggen
    async def on_ready(self): #überschreibt die on_ready
        print('Ich habe mich eingeloggt')

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):

        if message.author == client.user:
            return
        
        embed = discord.Embed(
            title = "Titel",
            discription = "Desc",
            color = 0XFF00FF,
            timestamp = datetime.datetime.utcnow()
        )
        embed.add_field(
            name = "Field1Name",
            value = "Fiel1Value",
            inline = True
        )
        embed.add_field(
            name = "Field2Name",
            value = "Fiel2Value",
            inline = True
        )
        embed.set_image(url = "")
        embed.set_footer(
            text = "Footer",
            icon_url = ""
        )
        embed.set_author(
            name = "Andy",
            url = "",
            icon_url = ""
        )
        await message.channel.send(embed = embed)
            
client = MyClient()
client.run('')