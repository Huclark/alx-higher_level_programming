#!/usr/bin/python3
"""This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def first_state(username, password, database, state_name):
    """Displays the state object

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database name
    """
    # create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database),
        pool_pre_ping=True
    )
    # create a session and bind it to engine
    session_maker = sessionmaker(bind=engine)

    with session_maker() as session:
        # query the database
        states = session.query(State).filter_by(
            name=state_name).order_by(State.id).all()
        if states:
            for state in states:
                print(state.id)
        else:
            print("Not found")


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    first_state(argv[1], argv[2], argv[3], argv[4])
