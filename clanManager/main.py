import sys

from multiprocessing import Process
from database import manageWars, trackMembers


def main():
    war_manager = Process(target=manageWars.manage_wars)
    player_manager = Process(target=trackMembers.track_members)

    war_manager.start()
    player_manager.start()
   
if __name__ == "__main__":
    main()
