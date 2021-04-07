import sys

from flask import Flask
from flask_restplus import Resource, Api
from multiprocessing import Process
from database.database import Database
from trackers.trackMembers import track_members


application = Flask(__name__)
api = Api(application,
          version='0.1',
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


if __name__=='__main__':
    # member_manager = Process(target=track_members)
    # member_manager.start()
    application.run(debug=True)