import discord

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents = intents)

class MyClient(discord.Client): #erbt von Discord Client

    #Einloggen
    async def on_ready(self): #überschreibt die on_ready
        print('Ich habe mich eingeloggt')

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print('Nachricht von ' + str(message.author) + ' enthält ' + str(message.content))

        if message.author == client.user: #reagiert nicht auf Nachrichten von sich selbst
            return
        
        if message.content.startswith("!bot"):
            await message.channel.send("Hello!!!")
            await message.author.send("Du hast mich kontaktiert, was gibt's?")

        if message.content.startswith("!stats"):
            messages = await message.channel.history(limit = 50).flatten()
            for i in messages:
                print(i.content)
            counter = 0
            async for m in message.channel.history():
                if m.author == client.user and m.content == 'Leider verloren :(':
                    counter = counter + 1
            print(counter)
        else:
            #await message.delete()
            #await message.edit(content = message.content + " - edited by TutoBot")
            await message.pin()
            await message.add_reaction("💩")

        if message.content.startswith("!onlinemembers"):
            members = client.guilds[0].members

            for i in members:
                if i.status == discord.Status.offline:
                    members.remove(i)

            for i in members:
                print(str(i))

    async def on_typing(self, channel, user, when): #wird ausgelöst, wenn jmd. anfängt zu tippen
        #print(str(user) + " tippt gerade in " + str(channel) + " seit " + str(when))
        return

    async def on_message_delete(self, message):
        print("Gelöschte Nachricht " + message.content)
    
    async def on_message_edit(self, before, after):
        print("Changed Message " + before.content + " to " + after.content)

    async def on_reaction_add(self, reaction, user): #In diesem Cache
        await reaction.message.channel.send(str(user) + " reacted on " + reaction.message.content + " with " + reaction.emoji)
        await reaction.message.channel.send("Count: " + str(reaction.count))
    
    async def on_raw_reaction_add(self, payload): #Alle Nachrichten
        print(str(payload))

    async def on_member_join(self, member):
        pass

    async def on_member_remove(self, member):
        pass

    async def on_member_update(self, before, after):
        print(str(before.joined_at))
        print(str(before.activites))
        print(str(before.guild))
        print(str(before.nick))
        print(str(before.mobile_status))
        print(str(before.desktop_status))
        print(str(before.web_status))
        print(str(before.roles))
        
        roles = discord.utils.get(after.guild.roles, name = "Zum Verteilen") #Gehe alle Rollen durch & bekomme Zum Verteilen
        await after.add_roles(roles) #Nachdem mein Status geändert wurde

client = MyClient()
client.run('')