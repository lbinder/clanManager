import mysql.connector
import os

from secret import config
from mysql.connector import errorcode


class Database:
    connection = None

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**config.database_config)
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error with username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(e)

    def close_connection(self):
        self.connection.close()

    def run_query_for_results(self, query):
        """Runs a query
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
            return results
        except mysql.connector.Error as e:
            print(e)
            return None
        finally:
            cursor.close()

    def run_query(self, query, values):
        cursor = self.connection.cursor()
        if values == None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def insert_into_members(self, values):
        """Adds a new member into the members table
        Args:
            values: contains the member's tag, name, and the date they joined (current date)
        Returns:
            Nothing is returned
        Raises:
        mysql.connector.Error: if the member cannot be added to the member table

        """
        query = "INSERT IGNORE INTO members (tag, name, date) VALUES (%s, %s, %s)"
        try:
            self.run_query(query, values)
        except mysql.connector.Error as e:
            print(e)

    def delete_from_members(self, tag):
        """Deletes a member from the members table"""
        query = "DELETE FROM members WHERE tag = '" + tag + "'"
        try:
            self.run_query(query, None)
        except mysql.connector.Error as e:
            print(e)

    def get_member_count(self):
        """Find the amount of members in the clan
        Returns:
            The amount of members in the clan
        """
        query = "SELECT COUNT(*) FROM members"
        return self.run_query_for_results(query)

    def get_members_table(self):
        """Get the data stored in the members table
        Returns:
            A dictionary containing all rows in the members table or None on failure
        """
        query = "SELECT * FROM members"
        return self.run_query_for_results(query)

    def member_exists(self, tag):
        """Checks the members table to see if a row exists specified by the tag
        Returns:
            1 if the row exists and 0 otherwise
        Args:
            tag: identifies a member
        """
        query = "SELECT COUNT(1) FROM members WHERE tag = '" + tag + "' limit 1"
        return self.run_query_for_results(query)[0][0]

    def insert_into_wars(self, tag):
        """Add a new war into the wars table
        Args:
            tag: the tag associated with a given war
        Returns:
            None
        """
        query = "INSERT IGNORE INTO wars (tag) VALUES (%s)"
        try:
            self.run_query(query, tag)
        except mysql.connector.Error as e:
            print(e)

    def insert_into_war_stats(self, values):
        """Adds a new row containing the war stats of a member into the wars table
        Args:
            values: contains a members attackId, name, and stats relating to their war performance
        Returns:
            Nothing is returned
        Raises:
            mysql.connector.Error: if the member's war stats cannot be added to the war table

        """
        query = "INSERT IGNORE INTO war_stats (id, name, attackOneUsed, attackOneStars, attackOneDestruction, attackTwoUsed, attackTwoStars, attackTwoDestruction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.run_query(query, values)
        except mysql.connector.Error as e:
            print(e)

    def update_attacks(self, values, id):
        """Updates a member's war attacks
        Args:
            values: updated attack values
        """
        query = "UPDATE war_stats SET attackOneUsed = %s, attackOneStars = %s, attackOneDestruction = %s, attackTwoUsed = %s, attackTwoStars = %s, attackTwoDestruction = %s WHERE attackID = %s"
        self.run_query(query, values + [id])

    def get_members_war_attacks(self, member_tag):
        """Finds all the attacks a member has completed in wars
        Args:
            member_tag: the tag that identifies a unique member of the clan
        Returns:
            List of a players war attacks
        Raises:
            mysql.connector.Error: if the member's stats cannot be accessed
        """
        query = "SELECT * FROM war_stats WHERE tag LIKE '" + member_tag + "%'"
        return self.run_query_for_results(query)

    def get_wars(self):
        """Finds all tags of wars participated in
        Returns:
            List of war tags
        """
        return self.run_query_for_results("SELECT * FROM wars")
