import sys

from multiprocessing import Process
from flask import Flask, render_template
from database import getData as api
from database import manageWars, trackMembers
from database import database


app = Flask(__name__)


def start_application():
    app.run("0.0.0.0", "80", debug=True)


@app.route('/test')
def index():
    render_template("test.html")

def main():
    running = True
    war_manager = Process(target=manageWars.manage_wars)
    player_manager = Process(target=trackMembers.track_members)
    db = database.DataBase()

    while running:
        user_input = input(": ")
        if (user_input == 'start'):
            war_manager.start()
            player_manager.start()
        elif (user_input =='stop'):
            war_manager.terminate()
            player_manager.terminate()
            print("Clan Manager Shutdown")
            running = False
    # app.run(debug=True, port=80, host='0.0.0.0')

if __name__ == "__main__":
    main()
