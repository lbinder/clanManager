import requests

from tokens import private


def get_clan_members():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/members",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    clan_members = r.json()
    return clan_members


def get_player_information(player_tag):
    r = requests.get("https:///api.clashofclans.com/v1/players/" + player_tag,
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    player_info = r.json()
    return player_info


def get_current_war_information():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/currentwar",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    war_info = r.json()
    return war_info


def get_cwl_information():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/currentwar/leaguegroup",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    cwl_info = r.json()
    return cwl_info
