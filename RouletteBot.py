import discord
import random

class MyClient(discord.Client): #erbt von Discord Client

    #Einloggen
    async def on_ready(self): #überschreibt die on_ready
        print('Ich habe mich eingeloggt')

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print('Nachricht von ' + str(message.author) + ' enthält ' + str(message.content))

        if message.author == client.user: #reagiert nicht auf Nachrichten von sich selbst
            return

        if message.content == "$help":
            await message.channel.send('''Für Roulette: $roulette Gesetzt eingeben, wobei Gesetzt =
            \n black \n red \n number''')
        
        if message.content.startswith("$roulette"):
            gesetzt = message.content.split(' ')[1]
            gesetzt_parameter = -3

            if gesetzt.lower() == "black":
                gesetzt_parameter = -1
            elif gesetzt.lower() == "red":
                gesetzt_parameter = -2
            else:
                try:
                    gesetzt_parameter = int(gesetzt)
                except:
                    gesetzt_parameter = -3
            
            if gesetzt_parameter == -3:
                await message.channel.send("Ungültige Eingabe")
                return
            
            result = random.randint(0, 36)
            print(result)
            if gesetzt_parameter == -1:
                won = result % 2 == 0 and not result == 0 #Gerade Zahlen, außer 0
            elif gesetzt_parameter == -2:
                won = result % 2 == 1 #Ungerade Zahlen
            else:
                won = result == gesetzt_parameter
            
            if won:
                await message.channel.send("$$$ Du hast gewonnen $$$")
            else:
                await message.channel.send("Leider verloren :(")

client = MyClient()
client.run('')