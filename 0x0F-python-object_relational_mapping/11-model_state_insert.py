#!/usr/bin/python3
"""This script adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def add_state(username, password, database):
    """Adds the State object “Louisiana” to
    the database hbtn_0e_6_usa

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
        # create the state object
        state = State(name="Louisiana")
        # add the session
        session.add(state)
        # commit the session
        session.commit()
        # print new object
        print(state.id)


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    add_state(argv[1], argv[2], argv[3])
