import sys

from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api
from multiprocessing import Process
from database.database import Database
from trackers.trackMembers import track_members


application = Flask(__name__)
CORS(application)
api = Api(application,
          version='0.2',
          title='Clan Manager',
          description='Get clan stats'
)

@api.route('/members')
class Members(Resource):
    def get(self):
        db = Database()
        members = db.get_members_table()
        db.close_connection()
        return members


@api.route('/members_count')
class Count(Resource):
    def get(self):
        db = Database()
        count = db.get_member_count()
        db.close_connection()
        return count


def main():
    member_manager = Process(target=track_members)
    member_manager.daemon=True
    member_manager.start()
    application.run(debug=True)


if __name__=='__main__':
    main()