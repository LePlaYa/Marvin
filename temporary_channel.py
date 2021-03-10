async def temporary_channel(self, member, before, after):
    if(after.channel):
        if(after.channel.name == "join-to-create-temp-channels"):
            self.created_channel.append(await after.channel.guild.create_voice_channel("{0.name}'s Channel".format(member), category=after.channel.category))
            await member.move_to(self.created_channel[-1])

    for channel in self.created_channel:
        if(not len(channel.members)):
            await channel.delete()
            self.created_channel.remove(channel)
