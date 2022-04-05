import discord
import datetime
from discord.utils import get
import time
import asyncio

async def add_senior_role():
    while True:
        try:
            guild = get(client.guilds, name = "Kaiheila")
            members = guild.members
            seniorRole = get(guild.roles, name = "Kotlin")
            members = [i for i in members if not i.bot and not seniorRole in i.roles] #Neue Liste ohne den Bot und Seniors

            for i in members:
                if datetime.datetime.now() - i.joined_at > datetime.timedelta(days = 30): #Wenn Member länger als 30 Tage dabei ist
                    await i.add_roles(seniorRole)
                    print("Added Senior Role: " + i.name)
            print(members)
            await asyncio.sleep(60)
        except:
            pass

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

        if message.content == "!seniorBot":
            while True:
                members = message.guild.members
                seniorRole = get(message.guild.roles, name = "Kotlin")
                members = [i for i in members if not i.bot and not seniorRole in i.roles] #Neue Liste ohne den Bot und Seniors

                for i in members:
                    if datetime.datetime.now() - i.joined_at > datetime.timedelta(days = 30): #Wenn Member länger als 30 Tage dabei ist
                        await i.add_roles(seniorRole)
                        print("Added Senior Role: " + i.name)
                print(members)
                time.sleep(60*60*24) #Alle 24h einmal laufen lassen
            

client = MyClient()
client.loop.create_task(add_senior_role())
client.run('')