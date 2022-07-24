import nextcord
from nextcord.ext import commands
from nextcord import Interaction, FFmpegPCMAudio, member
from nextcord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os
import random

greetings = ["sup", "hey!", "hello!", "hi"]

class Greetings(commands.Cog):
    """_summary_

    Args:
        commands (_type_): _description_
    """
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(name = 'hello', description = 'returns a random greating')
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message(random.choice(greetings))
        
def setup(client):
    client.add_cog(Greetings(client))