import discord
import w2g
import temporary_channel

class MyClient(discord.Client):
    created_channel = []

    async def on_ready(self):
       print('Logged on as {0}' .format(self.user))

    async def on_message(self, message):
        if(message.content == "Hallo"):
            await message.channel.send('Hi {0}, schön das du da bist!'.format(message.author.mention))
        elif(message.content.split(' ')[0] == "w2g"):
            await w2g.create_w2g(self, message, watoge_token)
        elif(message.content == "richtig?"):
            await message.channel.send('falsch')

    async def on_voice_state_update(self, member, before, after):
        await temporary_channel.temporary_channel(self, member, before, after)


client = MyClient()
f = open("token", "r")
watoge_token = open("w2g_token", "r")
wtoken = watoge_token.read()
client.run(f.read())

