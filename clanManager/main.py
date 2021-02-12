import sys

from multiprocessing import Process
from database import getData as api
from database import manageWars, trackMembers
from database import database


def main():
    running = True
    war_manager = Process(target=manageWars.manage_wars)
    player_manager = Process(target=trackMembers.track_members)
    db = database.DataBase()

    while running:
        user_input = input(": ")
        if (user_input == 'start'):
            war_manager.start()
            player_manager.start()
        elif (user_input =='stop'):
            war_manager.terminate()
            player_manager.terminate()
            print("Clan Manager Shutdown")
            running = False

if __name__ == "__main__":
    main()
