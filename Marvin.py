import discord
import w2g

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
        #print("{}:{}:{}".format(member, before, after))
        if(after.channel):
            if(after.channel.name == "create-room"):
                self.created_channel.append(await after.channel.guild.create_voice_channel("{0.name}'s Channel".format(member), category=after.channel.category))
                await member.move_to(self.created_channel[-1])

        for channel in self.created_channel:
            if(not len(channel.members)):
                await channel.delete()
                self.created_channel.remove(channel)


client = MyClient()
f = open("token", "r")
watoge_token = open("w2g_token", "r")
wtoken = watoge_token.read()
client.run(f.read())

