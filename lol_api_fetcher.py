import requests
import pandas as pd
import json
import time


api_key = "RGAPI-991551fd-437e-4c63-8a72-b91bdfcbb990"
region = "EUW"


def find_summoner_id (div, tier, page):
    api_url_sum = "https://{}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{}/{}?page={}&api_key={}".format(region,div,tier,page,api_key)
    list_of_profiles = requests.GET(api_url_sum).json()
    num_profiles = len(list_of_profiles)
    summonerID_list = []

    for prof in range(0,num_profiles):
        summonerID_list.append(list_of_profiles[prof]['summonerID'])

    
