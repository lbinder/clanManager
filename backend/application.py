from app import application
from trackers.trackMembers import track_members
from multiprocessing import Process

member_manager = Process(target=track_members)
member_manager.start()

if __name__=='__main__':
    application.run()