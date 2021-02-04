import mysql.connector

from mysql.connector import errorcode
from database.tokens import private

class DataBase:
    connection = None
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**private.config)
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error with username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(e)

    def close_connection(self):
        self.connection.close()

    def execute(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def get_table(self, name):
        query = "SELECT * FROM " + name
        cursor = self.connection.cursor()
        cursor.execute(query)
        table = cursor.fetchall()
        cursor.close()
        return table

    def insert_into_wars(self, values):
        query = "INSERT INTO WARS (attackId, name, attackOneUsed, attackOneStars, attackOneDestruction, attackTwoUsed, attackTwoStars, attackTwoDestruction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, values)

    def insert_into_members(self, values):
        query = "INSERT INTO members (tag, name, dateJoined) VALUES (%s, %s, %s)"
        self.execute(query, values)

    def update_attacks(self, values, id):
            query = "UPDATE wars SET attackOneUsed = %s, attackOneStars = %s, attackOneDestruction = %s, attackTwoUsed = %s, attackTwoStars = %s, attackTwoDestruction = %s WHERE attackID = %s"
            self.execute(query, values+[id])

    def entry_exists_war(self, attackID):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT attackID, COUNT(*) FROM wars WHERE attackID = %s GROUP BY attackID",
            (attackID,)
        )
        results = cursor.fetchone()
        if not results:
            return False
        else:
            return True

    def entry_exists_members(self, tag):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT tag, COUNT(*) FROM members WHERE tag = %s GROUP BY tag",
            (tag,)
        )
        results = cursor.fetchone()
        if not results:
            return False
        else:
            return True
