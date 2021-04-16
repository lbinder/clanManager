import time
from clashOfClansApi import getClashData
from datetime import date
from database.database import Database


def track_members():
    """Checks to see if new members should be added or removed every 10 minutes
    """
    while True:
        db = Database()
        tags_in_db = parse_tags(db.get_members_table())
        update_members(tags_in_db, db)
        db.close_connection()
        time.sleep(600)


def update_members(tags_in_db, db):
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
        if (not db.member_exists(member['tag'])):
            values = [member['tag'], member['name'], date.today()]
            db.insert_into_members(values)

    delete_members(current_tags, tags_in_db, db)
    

def delete_members(current_tags, tags_in_db, db):
    """Deletes a member from the database if they are no longer in the clan
    Args:
        current_tags: tags of players that are currently in the clan
        tags_in_db: the tags of the players that are currently in the database
    Returns:
        an updated list of tags that reflect any changes made to the database
    """
    for tag in tags_in_db:
        if (tag not in current_tags):
            db.delete_from_members(tag)


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


            