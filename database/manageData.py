import time

from database.getData import *
from database.database import *

""" manage_wars
    Controls the war state. Control flow for managing wars
    happens here.
"""
def manage_wars():
    db = DataBase()
    new_war = True
    while True:
        war = get_current_war_information()
        if (war['state'] == 'preparation' and new_war):
            add_new_war(war, db)
            new_war = False

        while (war['state'] == 'inWar'):
            war = get_current_war_information()
            track_war(war, db)
            time.sleep(10)
        
        new_war = True
        time.sleep(10)

""" add_new_war
    war: dictionary of war data
    db: database object
    When a new war is detected this sets up the database for info
    to be added
"""
def add_new_war(war, db):
    members = war['clan']['members']
    enemy_tag = war['opponent']['tag']
    for member in members:
        tag = member['tag']
        name = member['name']
        if not db.entry_exists_war(enemy_tag+tag):
            values = [enemy_tag+tag, name, 'F', None, None, 'F', None, None]
            db.insert_into_wars(values)

"""track_war
    war: dictionary of war data
    db" database object
    When a war is active this updates each players war stats.
"""
def track_war(war, db):
    members = war['clan']['members']
    enemy_tag = war['opponent']['tag']
    for member in members:
        values = parse_values(member)
        if (values != None):
            db.update_attacks(values, enemy_tag+member['tag'])

""" parse_values
    member: dictionary of member information
    Finds how many attacks a member has completed and returns values
    to update that member's information.
"""
def parse_values(member):
    if 'attacks' in member:
        if (len(member['attacks']) == 1):
            values = ['T', 
                      int(member['attacks'][0]['stars']),
                      float(member['attacks'][0]['destructionPercentage']),
                      'F', None, None]
        elif (len(member['attacks']) == 2):
            values = ['T', 
                      int(member['attacks'][0]['stars']),
                      float(member['attacks'][0]['destructionPercentage']),'T', 
                      int(member['attacks'][1]['stars']),
                      float(member['attacks'][1]['destructionPercentage'])]
    else:
        values = None
    return values