import time

from datetime import date
from database import Database

db = Database()

def track_members(members_tracked):
    while True:
        time.sleep(10)
        update_members(db, members_tracked)


def update_members(members_tracked):
    member = []
    for member in members['items']:
        if (member['tag'] not in members_tracked):
            values = [member['tag'], member['name'], date.today()]
            db.insert_into_members(values)