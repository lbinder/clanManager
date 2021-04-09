from app import application
from trackers.trackMembers import track_members
from multiprocessing import Process


if __name__=='__main__':
    member_manager = Process(target=track_members)
    member_manager.daemon=True
    member_manager.start()
    application.run()