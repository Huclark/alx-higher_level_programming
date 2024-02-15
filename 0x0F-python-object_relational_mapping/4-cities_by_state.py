#!/usr/bin/python3
"""This script lists all cities from the hbtn_0e_4_usa database
"""
from sys import argv
import MySQLdb


def list_all_cities(username, password, database):
    """Displays all cities in a database

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database name
    """
    db = MySQLdb.connect(
        host="localhost", user=username, password=password, database=database, port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC"""
    )
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    # execute function
    list_all_cities(argv[1], argv[2], argv[3])
