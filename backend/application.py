from app import application, start_trackers
from trackers.trackMembers import track_members
from multiprocessing import Process


if __name__=='__main__':
    start_trackers()
    application.run()