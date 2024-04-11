import requests
import pandas as pd
import json
import time
import csv


api_key = "RGAPI-0c181667-494e-418a-93ae-956f20d7b213"
region = "euw1"


summonerID_list = []
#Function that pulls a page of summoner IDs ranked Diamond 1-4
def find_summoner_id (div, tier, page):
    api_url_sum = "https://{}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{}/{}?page={}&api_key={}".format(region,div,tier,page,api_key)
    list_of_profiles = requests.get(api_url_sum).json()
    num_profiles = len(list_of_profiles)

    for prof in range(0,num_profiles):
        summonerID_list.append(list_of_profiles[prof]['summonerId'])

#For loop that calls to find_summoner_id with what Division and tier we are looking for
for tier in ["I"]:
    for page in range(1, 2):
        time.sleep(1.5)
        find_summoner_id("DIAMOND", tier, page)

df_sID = pd.DataFrame(summonerID_list, columns=["Summoner ID"])
df_sID.to_csv('summonerID.csv', mode= 'a', index=False)



summoner_IDs = pd.read_csv("summonerID.csv")
puuid_list = []


#Function that finds the puuid given a summoner id
def find_summoner_puuid (summoner_id):
    api_url_puuid = "https://{}.api.riotgames.com/lol/summoner/v4/summoners/{}?api_key={}".format(region, summoner_id, api_key)
    summoner_info = requests.get(api_url_puuid).json()
    puuid_list.append(summoner_info["puuid"])


summID_list = summoner_IDs["Summoner ID"]
for summoner_id in range(0, len(summID_list)):
    time.sleep(1.5)
    if summID_list[summoner_id] == "Summoner ID":
        pass
    else:
        find_summoner_puuid(summID_list[summoner_id])
        print("Done fetching IDs")


df_pID = pd.DataFrame(puuid_list, columns=["Puuid"])
df_pID.to_csv('puuid.csv', mode='a', index=False)



puuids = pd.read_csv("puuid.csv")
type = "ranked"
match_list = []
fetch_errors = []
list_of_puuids = puuids["Puuid"]
region2 = "europe"

def find_match_ids(puuid, type):
    api_url_matchid = "https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?type={}&start=0&count=20&api_key={}".format(region2, puuid, type, api_key)
    match_history = requests.get(api_url_matchid).json()

    for match_id in match_history:
        match_list.append(match_id)

for puuid in range(0, len(list_of_puuids)):
    time.sleep(1.5)
    if list_of_puuids[puuid] == "Puuid":
        pass
    else:
        find_match_ids(list_of_puuids[puuid], type)
        print("Fetched match_id")

df_mID = pd.DataFrame(match_list, columns=["Match ID"])
df_mID.to_csv('matchID.csv', mode = 'a', index=False)

print("All ids fetched")

