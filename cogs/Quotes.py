import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio, Member
from nextcord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os
from json import loads
import requests
from config import XRapidAPIHost, XRapidAPIKEY

def quote_of_the_day():
    url_qotd = "https://quotel-quotes.p.rapidapi.com/quotes/qod"
    payload = {}
    headers = {
        "content-type": "application/json",
        "X-rapidAPI-Host": XRapidAPIHost,
        "X-rapidAPI-Key": XRapidAPIKEY
        }
    #making request for quote
    response = requests.request(method = "POST",
                                        url = url_qotd,
                                        json = payload,
                                        headers = headers)
    #extracting quote
    json_data = response.json()
    
    print(json_data)
    print(type(json_data))

quote_of_the_day()















# class Quotes(commands.Cog):
#     """_summary_

#     Args:
#         commands (_type_): _description_
#     """
    
#     def __init__(self, client):
#         self.client = client
        
#     @nextcord.slash_command(name = 'qotd', description = 'returns the quote of the day')
#     async def quotes(self, interaction: Interaction):
#         await interaction.response.send_message()































# # random quote
# # def radom_quote():
# #     payload = {}
# #     headers = {
# # 	    "content-type": "application/json",
# # 	    "X-RapidAPI-Host": XRapidAPIHost,
# # 	    "X-RapidAPI-Key": XRapidAPIKEY
# #     }
# #     response = requests.request("POST",
# #                                         url_random,
# #                                         json = payload,
# #                                         headers = headers)
# #     return 
