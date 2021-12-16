import discord
import random
import os


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

client.run('OTIwOTQxNDQ3ODU3OTYzMDI5.Ybrrjw.9YQ6VMrL5g5-OUGIR9XXsOD8vZ8')

