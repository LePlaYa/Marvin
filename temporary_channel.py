async def temporary_channel(self, member, before, after):
    if(after.channel):
        if(after.channel.name == "join-to-create-temp-channels"):
            self.created_channel.append(await after.channel.guild.create_voice_channel("{0.name}'s Channel".format(member), category=after.channel.category))
            self.created_channel.update({await after.channel.guild.create_voice_channel("{0.name}'s Channel".format(member), category=after.channel.category) : await after.channel.guild.create_text_channel("{0.name}'s Text Channel".format(member), category=after.channel.category)})
            await member.move_to(list(self.created_channel.keys())[-1])

    for voice, text in self.created_channel.items():
        if(not len(voice.members)):
            await voice.delete()
            await text.delete()
            self.created_channel.pop(voice)
            return
