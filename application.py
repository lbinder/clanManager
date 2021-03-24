import sys
import trackMembers

from flask import Flask
from flask_restplus import Resource, Api
from multiprocessing import Process
from database import Database

db = Database()
application = Flask(__name__)
api = Api(application,
          version='0.1',
          title='Clan Manager',
          description='Get clan stats'
)

@api.route('/get_members')
class WarStats(Resource):
    def get(self):
        return db.get_members_table()


if __name__=='__main__':
    member_manager = Process(target=trackMembers.track_members, args=(db.get_members_table))
    application.run(debug=True)