import discord
# import requests
# import json
import python2

client = discord.Client()

bp = '*'
# def get_quote():
#    response = requests.get("https://zenquotes.io/api/random")
#    json_data = json.loads(response.text)
#    quote = json_data[0]['q'] + " -" + json_data[0]['a']
#    return(quote)

words_list = ['sed', 'sucks', 'bad', 'trash', 'suck']
response = 'deal with it.'
nou = ['nou', 'n ou', 'no u', 'no you', 'NOU', 'N OU', 'NO U', 'NO YOU', 'noob', 'NOOB', 'lul', 'nub', 'NUB']
nou_r = 'no u'
words_list2 = ['back', 'BACK', 'returned', 'RETURNED', 'bak', 'BAK']
words_list2_r = 'so?'
words_list3 = ['hehe', ':<', ':>', 'shut up', 'SHUT UP']
words_list3_r = 'shut up'


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith(bp + 'hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(bp + 'noob'):
        await message.channel.send('no u')
    #    if message.content.startswith(bp + 'quote'):
    #       quote = get_quote()
    #        await message.channel.send(quote)
    if any(word in msg for word in words_list):
        await message.channel.send(response)
    if any(word in msg for word in nou):
        await message.channel.send(nou_r)
    if any(word in msg for word in words_list2):
        await message.channel.send(words_list2_r)
    if any(word in msg for word in words_list3):
        await message.channel.send(words_list3_r)


client.run(python2.token)
