import discord
import random
import os
import json

client = discord.Client()
answers = ['хд', 'xd', 'xdddddd', 'xdxd', 'хдхдхд']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(el in message.content for el in ['xd', 'хд']):
        if random.randint(0, 1) == 1:
            random_anwer = random.choice(answers)
            await message.channel.send(random_anwer)
        else:
            file = random.choice(os.listdir("files"))
            with open(f'files/{file}', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
token_file = open('config.json', 'r')
client.run(json.loads(token_file.read()).get('token'))
token_file.close()