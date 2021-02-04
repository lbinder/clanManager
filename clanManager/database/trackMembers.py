from datetime import date
from database.getData import *
from database.database import *


def track_members():
    db = DataBase()
    members = get_clan_members()
    while True:
        update_members

def update_members(db, members):
    for member in members['items']:
            if (not db.entry_exists_members(member['tag'])):
                db.insert_into_members([member['tag'], 
                                        member['name'], 
                                        date.today()])