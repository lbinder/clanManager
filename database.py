import mysql.connector
import config

from mysql.connector import errorcode


class Database:
    connection = None

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**config.config)
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error with username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(e)
    

    def run_query(self, query):
        """ Runs a query
        Args:
            query: a string that contains the query to run
        Returns:
            the results of executing the query
        Raises:
            mysql.connector.Error: if query fails
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
            return None
        finally:
            cursor.close()


    def insert_into_members(self, values):
        """Adds a new member into the members table
        Args:
            values: contains the players tag, name, and the date they joined (current date)
        Returns:
            Nothing is returned
        Raises:
        mysql.connector.Error: if the member cannot be added to the member table

        """
        query = "INSERT INTO members (tag, name, joined) VALUES (%s, %s, %s)"
        try:
            self.execute(query, values)
        except mysql.connector.Error as e:
            print(e)
    

    def get_members_table(self):
        """Get the data stored in the members table
        Returns: 
            A dictionary containing all rows in the members table or None on failure
        """
        query = "SELECT * FROM members"
        return run_query(query)


    def insert_into_wars(self, values):
        """Adds a new row containing the war stats of a player into the wars table
        Args:
            values: contains a members attackId, name, and stats relating to their war performance
        Returns:
            Nothing is returned
        Raises:
            mysql.connector.Error: if the members war stats cannot be added to the war table

        """
        query = "INSERT INTO wars (attackId, name, attackOneUsed, attackOneStars, attackOneDestruction, attackTwoUsed, attackTwoStars, attackTwoDestruction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.execute(query, values)
        except mysql.connector.Error as e:
            print(e)
        

    def get_member_war_attacks(self, tag):
        """Finds all the wars that a member has participated in
        Args:
            tag: unique identifier for a member
        Returns:
            dictionary containing the war stats of a member.
        """
        query = "SELECT * FROM wars WHERE attackId LIKE '%" + tag + "'"
        return run_query(query)

    
        
