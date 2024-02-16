#!/usr/bin/python3
"""This script lists all State objects from the
database hbtn_0e_6_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def list_all_states(username, password, database):
    """Displays all states in a database

    Args:
        username (str): Username
        password (str): User's password
        database (str): Database name
    """
    # create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database.strip()),
        pool_pre_ping=True
    )
    # create a session and bind it to engine
    session_maker = sessionmaker(bind=engine)

    with session_maker() as session:
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))

    # alternate approach
    # session = session_maker()
    # query the database
    # for state in session.query(State).order_by(State.id):
    #     print("{}: {}".format(state.id, state.name))
    # close session
    # session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        sys.exit(1)
    # execute function
    list_all_states(argv[1], argv[2], argv[3])
