import sys

from multiprocessing import Process
from flask import Flask
from database import getData as api
from database import manageData


app = Flask(__name__)


def start_application():
    app.run("0.0.0.0", "80", debug=True)


@app.route('/')
def index():
    return "sup"

def main():
    running = True
    war_manager = Process(target=manageData.manage_wars)
    while running:
        user_input = input(": ")
        if (user_input == 'start'):
            war_manager.start()
        elif (user_input =='stop'):
            war_manager.terminate()
            print("Clan Manager Shutdown")
            running = False
    #app.run(debug=True, port=80, host='0.0.0.0')

if __name__ == "__main__":
    main()