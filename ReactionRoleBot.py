import discord

welcome_channel_id = 958066697045164133
class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("EINGELOCHT")
        welcome_channel = client.get_channel(welcome_channel_id)
        await welcome_channel.send("Hallo, willkommen! Bitte reagiere mit 🐍 für Python und 💩 für Kotlin.")

    #Channel auslesen
    async def on_reaction_add(self, reaction, user):
        python = discord.utils.get(user.guild.roles, name = "Python")
        kotlin = discord.utils.get(user.guild.roles, name = "Kotlin")

        if str(reaction.emoji) == "🐍":
            await user.add_roles(python)
        
        if str(reaction.emoji) == "💩":
            await user.add_roles(kotlin)
        

client = MyClient()
client.run("")