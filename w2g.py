import requests

async def create_w2g(self, message, watoge_token):
    payload = {'w2g_api_key': watoge_token.read(), 'share':message.content.split(' ')[1]}
    r = requests.post('https://w2g.tv/rooms/create.json', data=payload)
    jsres = r.json()
    await message.channel.send('https://w2g.tv/rooms/{0}'.format(jsres["streamkey"]))
    await message.delete()

