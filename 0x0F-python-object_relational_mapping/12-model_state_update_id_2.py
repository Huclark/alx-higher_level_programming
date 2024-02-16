#!/usr/bin/python3
"""This script changes the name of a State object
from the database hbtn_0e_6_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def update_state(username, password, database):
    """changes the name of a State object
from the database

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
        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = "New Mexico"
            # commit the session
            session.commit()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    update_state(argv[1], argv[2], argv[3])
