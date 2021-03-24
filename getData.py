import requests


""" get_clan_members
    Returns all members in the clan and information related to each member
"""
def get_clan_members():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/members",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    clan_members = r.json()
    return clan_members

""" get_member_information
    player_tag: unique identifier for a player in Clash of Clans.
    Returns information relating to a member in the clan.
"""
def get_member_information(player_tag):
    r = requests.get("https:///api.clashofclans.com/v1/players/" + player_tag,
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    member_info = r.json()
    return member_info

""" get_current_war_information
    Returns information relating to the current war.
"""
def get_current_war_information():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/currentwar",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    war_info = r.json()
    return war_info


def get_war_log():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/warlog",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    war_log = r.json()
    return war_log


""" get_cwl_information
    Returns information relating to the current clan war league
"""
def get_cwl_information():
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + private.clan_tag + "/currentwar/leaguegroup",
                     headers={"Authorization": "Bearer " + private.bearer_th},
                     params={"clanTag": private.clan_tag})
    cwl_info = r.json()
    return cwl_info
