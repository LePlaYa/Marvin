import os.path
import discord
import sqlite3
import w2g
import temporary_channel
import help
import programming_languages
#import create_channel
intents = discord.Intents.default()
intents.members = True


class MyClient(discord.Client):
    created_channel = {}

    async def on_ready(self):
       print('Logged on as {0}' .format(self.user))

    async def on_message(self, message):
        if(message.content == "?help"):
            await help.helper(self, message)
        elif(message.content.split(' ')[0] == "w2g"):
            await w2g.create_w2g(self, message, watoge_token)
#        elif(message.content.split(' ')[0] == "!create"):
#            await create.create_channel(self.message)

    async def on_voice_state_update(self, member, before, after):
        await temporary_channel.temporary_channel(self, member, before, after)

    async def on_raw_reaction_add(self, payload):
        if(payload.guild_id == 814844899387506712):
            await programming_languages.set_languages(self, payload)
        
    async def on_raw_reaction_remove(self, payload):
        if(payload.guild_id == 814844899387506712):
            await programming_languages.remove_languages(self, payload, await self.fetch_guild(814844899387506712))




client = MyClient(intents=intents)
f = open("token", "r")
watoge_token = open("w2g_token", "r")
wtoken = watoge_token.read()
client.run(f.read())
