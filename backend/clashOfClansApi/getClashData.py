import requests

from secret import config


def get_clan_members():
    """Call to the clash of clans API to retrieve members of the clan
    Returns:
        all members in the clan and information related to each member
    """
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + config.clan_tag + "/members",
                     headers={"Authorization": "Bearer " + config.bearer},
                     params={"clanTag": config.clan_tag})
    clan_members = r.json()

    return clan_members


def get_member_information(player_tag):
    """ Call to the clash of clans API to retrieve specific information relating to a member
    Args:
        player_tag: unique identifier for a player in Clash of Clans
    Returns:
        information relating to a member in the clan
    """
    r = requests.get("https:///api.clashofclans.com/v1/players/" + player_tag,
                     headers={"Authorization": "Bearer " + config.bearer},
                     params={"clanTag": config.clan_tag})
    member_info = r.json()
    return member_info


def get_current_war_information():
    """ Call to the clash of clans API to retrieve information on the current war
    Returns:
        information relating to the current war
    """
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + config.clan_tag + "/currentwar",
                     headers={"Authorization": "Bearer " + config.bearer},
                     params={"clanTag": config.clan_tag})
    war_info = r.json()
    return war_info


def get_war_log():
    """Call to the clash of clans API to retrieve the clan's war log
    Returns:
        the clan's war log
    """
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + config.clan_tag + "/warlog",
                     headers={"Authorization": "Bearer " + config.bearer},
                     params={"clanTag": config.clan_tag})
    war_log = r.json()
    return war_log


def get_cwl_information():
    """Call to the clash of clans API to retrieve clan war information
    Returns:
        information relating to the current clan war league
    """
    r = requests.get("https://api.clashofclans.com/v1/clans/%23" + config.clan_tag + "/currentwar/leaguegroup",
                     headers={"Authorization": "Bearer " + config.bearer},
                     params={"clanTag": config.clan_tag})
    cwl_info = r.json()
    return cwl_info
