#!/usr/bin/python3
"""This script displays all states with a name starting with
N from the hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def list_states(username, password, database, state_name):
    """Lists all states which starts with letter N

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database name
        state_name (str): State name
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        db=database,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE name = '{state_name}'")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    # execute function
    list_states(argv[1], argv[2], argv[3], argv[4])
