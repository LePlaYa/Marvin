# <emoji-name> : <group_id>
languages = {
    "clang"     : 817699214222032947,
    "cpp"       : 817415333261869087,
    "csharp"    : 817415401637543966,
    "php"       : 817415432885370921,
    "html"      : 817415456238600263,
    "css"       : 817415492004216872,
    "python"    : 817675746221883402,
    "go"        : 817675778019819530,
    "javascript": 817675806205411338,
    "mysql"     : 817675845475893248,
    "lua"       : 817675899080146965,
    "julia"     : 817675950871412747,
    "rust"      : 817675987231178752,
    "kotlin"    : 817676030394761236,
    "java"      : 817676073960996896,
    "graphql"   : 817682434526281769,
    "kubernetes": 817682751690899466,
    "ruby"      : 817722351260401714,
    "dart"      : 821117356599148544
}

async def set_languages(self, payload):
    if(payload.message_id == 817684497424318486):
        if(languages.get(payload.emoji.name)):
            await payload.member.add_roles(payload.member.guild.get_role(languages.get(payload.emoji.name)))

async def remove_languages(self, payload, guild):
    if(payload.message_id == 817684497424318486):
        if(languages.get(payload.emoji.name)):
            mem = await guild.fetch_member(payload.user_id)
            await mem.remove_roles(guild.get_role(languages.get(payload.emoji.name)))
