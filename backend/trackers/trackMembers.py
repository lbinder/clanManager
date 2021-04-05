import time

from clashOfClansApi import getClashData
from datetime import date
from database.database import Database


db = Database()


def track_members():
    """Checks to see if new members should be added or removed every 10 seconds
    """
    members_tracked = db.get_members_table()
    tags_in_db = parse_tags(members_tracked)

    while True:
        tags_in_db = update_members(tags_in_db)
        time.sleep(600)


def update_members(tags_in_db):
    """Updates the database with members that are in the clan
    Args:
        tags_in_db: the tags of the players that are currently in the database
    Returns:
        an updated list of tags that reflect any changes made to the database
    """
    current_members = getClashData.get_clan_members()
    current_tags = []
    
    for member in current_members['items']:
        current_tags.append(member['tag'])
        add_members(member, tags_in_db)

    current_tags = delete_members(current_tags, tags_in_db)
    
    return current_tags


def add_members(member, tags_in_db):
    """Adds a member to the database if they are not currently in it
    Args:
        member: a player to add to the database
        tags_in_db: the tags of the players that are currently in the database
    Returns:
        an updated list of tags that reflect any changes made to the database
    """
    if (len(tags_in_db) == 0 or member['tag'] not in tags_in_db):
            values = [member['tag'], member['name'], date.today()]
            db.insert_into_members(values)


def delete_members(current_tags, tags_in_db):
    """Deletes a member from the database if they are no longer in the clan
    Args:
        current_tags: tags of players that are currently in the clan
        tags_in_db: the tags of the players that are currently in the database
    Returns:
        an updated list of tags that reflect any changes made to the database
    """
    updated_tags = []

    for tag in tags_in_db:
        if (tag not in current_tags):
            print(tag)
            db.delete_from_members(tag)
        else:
            updated_tags.append(tag)

    return updated_tags


def parse_tags(members):
    """Finds the tags of members
    Args:
        members: a list of members
    Returns:
        a list of every players tag that is currently in the database
    """
    tags = []

    for member in members:
        tags.append(member[0])

    return tags


            