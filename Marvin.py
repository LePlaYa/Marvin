import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
       print('Logged on as {0}' .format(self.user))

    async def on_message(self, message):
        #print('Message from {0.author}:{0.content}'.format(message))
        if(message.content == "Hallo"):
            await message.channel.send('Hi @{0.author}, schön das du da bist!'.format(message))
        elif(message.content.split(' ')[0] == "w2g"):
            payload = {'w2g_api_key': watoge_token.read(), 'share':message.content.split(' ')[1]}
            r = requests.post('https://w2g.tv/rooms/create.json', data=payload)
            jsres = r.json()
            await message.channel.send('https://w2g.tv/rooms/{0}'.format(jsres["streamkey"]))
        elif(message.content == "richtig?"):
            await message.channel.send('falsch')


client = MyClient()
f = open("token", "r")
watoge_token = open("w2g_token", "r")
wtoken = watoge_token.read()
client.run(f.read())