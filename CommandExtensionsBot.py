from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import asyncio
import datetime
import json

intents = discord.Intents.all()

def get_config(name):
    with open("config.json", "r") as f:
        json_file = json.load(f)
    return json_file[name]

client = commands.Bot(
    command_prefix = get_config("command_prefix"), #Bot damit ansprechen
    help_command = None,
    intents = intents
)

@client.event
async  def on_ready():
    print("Bin eingeloggt")
    client.loop.create_task(change_status())

@client.command(
    name = "ping",
    aliases = ["p"],
    desciption = "Sendet testweise Pong! zurück",
    help = "ping"
)
async def ping(ctx: Context):
    await ctx.channel.send(f"Pong! an {ctx.author.mention}")
    embed = discord.Embed(
            title = "Titel",
            discription = "Desc",
            color = int(get_config("colors")["embed_color"], 16), #In Hex konvertieren
        )
    write_ping()

def write_ping(author):
    with open("ping.json", "w") as f:
        json.dump({
            "author": author,
            "time": datetime.datetime.utcnow().strf("%d %B %Y - %H:%M:%S")
        }, f)

async def change_status(): #Status im Loop ändern
    while True:
        try:

            await client.change_presence(activity = discord.Activity(
                type = discord.ActivityType.watching,
                name = "Guckt ein Tuto an.",
                status = discord.Status.online))
            await asyncio.sleep(10)
            await client.change_presence(activity = discord.Game("!help"), status = discord.Status.online)
            await asyncio.sleep(10)

        except:
            pass

client.run('')