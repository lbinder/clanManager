import sys

from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api
from multiprocessing import Process
from database.database import Database
from trackers.trackMembers import track_members
from trackers.trackWars import manage_wars


application = Flask(__name__)
CORS(application)
api = Api(
    application, version="0.2", title="Clan Manager", description="Get clan stats"
)


@api.route("/members")
class Members(Resource):
    def get(self):
        db = Database()
        members = db.get_members_table()
        db.close_connection()
        return members


@api.route("/members_count")
class Count(Resource):
    def get(self):
        db = Database()
        count = db.get_member_count()
        db.close_connection()
        return count


@api.route("/wars")
class Wars(Resource):
    def get(self):
        db = Database()
        wars = db.get_wars()
        return wars
        db.close_connection()


def start_trackers():
    member_manager = Process(target=track_members)
    war_manager = Process(target=manage_wars)
    member_manager.daemon = True
    war_manager.daemon = True
    member_manager.start()
    war_manager.start()


def main():
    start_trackers()
    application.run(debug=True)


if __name__ == "__main__":
    main()