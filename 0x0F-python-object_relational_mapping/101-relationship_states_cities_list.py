#!/usr/bin/python3
"""This script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base
from relationship_state import State


def states_and_cities(username, password, database):
    """Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa

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
    # initialize database schema
    Base.metadata.create_all(engine)
    # create a session and bind it to engine
    session_maker = sessionmaker(bind=engine)

    with session_maker() as session:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    states_and_cities(argv[1], argv[2], argv[3])
