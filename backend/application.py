from app import application, start_trackers
from trackers.trackMembers import track_members
from multiprocessing import Process

start_trackers()

if __name__ == "__main__":
    application.run()
