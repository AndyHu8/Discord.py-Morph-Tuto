import discord

class MyClient(discord.Client): #erbt von Discord Client

    #Einloggen
    async def on_ready(self): #überschreibt die on_ready
        print('Ich habe mich eingeloggt')

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print('Nachricht von ' + str(message.author) + ' enthält ' + str(message.content))

        if message.author == client.user: #reagiert nicht auf Nachrichten von sich selbst
            return
        
        if message.content.startswith("hello bot"):
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

    async def on_typing(self, channel, user, when): #wird ausgelöst, wenn jmd. anfängt zu tippen
        #print(str(user) + " tippt gerade in " + str(channel) + " seit " + str(when))
        return

    async def on_message_delete(self, message):
        print("Gelöschte Nachricht " + message.content)
    
    async def on_message_edit(self, before, after):
        print("Changed Message " + before.content + " to " + after.content)

client = MyClient()
client.run('')