#!/usr/bin/python3
"""This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


def list_all_cities(username, password, database, state_name):
    """Displays all cities of a specified state in a database

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database name
        state_name (str): State to search
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC""",
        (state_name,)
    )
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    # execute function
    list_all_cities(argv[1], argv[2], argv[3], argv[4])
