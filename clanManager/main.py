from multiprocessing import Process
from database import getData
from database import manageWars
from database import trackMembers


def main():
    running = True
    war_manager = Process(target=manageWars.manage_wars)
    member_tracker = Process(target=trackMembers.track_members)
    while running:
        user_input = input(": ")
        if (user_input == 'start'):
            war_manager.start()
            member_tracker.start()
        elif (user_input =='stop'):
            war_manager.terminate()
            member_tracker.terminate()
            print("Clan Manager Shutdown")
            running = False

if __name__ == "__main__":
    main()
