#!/usr/bin/python3
"""This script lists all states from the hbtn_0e_0_usa database
"""
from sys import argv
import MySQLdb


def list_all_states(username, password, database):
    """Lists all the states from a database

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        db=database,
        port=3306
    )
    # Create a cursor object
    cursor = db.cursor()
    # Query the database
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # Fetch all the rows
    states = cursor.fetchall()
    # Display the results
    for state in states:
        print(state)
    # close the cursor
    cursor.close()
    # disconnect from MySQL server
    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    # execute function
    list_all_states(argv[1], argv[2], argv[3])
