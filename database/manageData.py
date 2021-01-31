import time

from database.getData import *


def manage_wars():
    while True:
        war = get_current_war_information()
        time.sleep(1)
        if (war['state'] == 'preparation'):
            add_new_war(war)
        elif (war['state'] == 'attacking'):
            track_war()


# Only add if there isn't a war against this clan
def add_new_war(war):
    members = war['clan']['members']
    enemy_tag = war['opponent']['tag']
    for member in members:
        tag = member['tag']
        print("adding " + str(tag) + " to war against " + enemy_tag)


def track_war():
    active = True
    while active:
        war = get_current_war_information()
        time.sleep(1)
        if (war['state'] == 'notInWar'):
            active = False
        else:
            members = war['clan']['members']
            enemy_tag = war['opponent']['tag']
            for member in members:
                print("updating " + str(member['tag']) + " attacks in war against " + enemy_tag)

