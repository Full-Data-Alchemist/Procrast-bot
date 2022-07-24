import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from config import TOKEN
import os


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '/')


@client.event
async def on_ready():
    print('the bot is up and ready')
    
initial_extensions = []

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        initial_extensions.append('cogs.' + filename[:-3])


if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)
    client.run(TOKEN)