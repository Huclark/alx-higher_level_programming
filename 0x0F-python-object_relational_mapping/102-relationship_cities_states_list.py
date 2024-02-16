#!/usr/bin/python3
"""This script lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def all_cities(username, password, database):
    """Lists all City objects from the database hbtn_0e_101_usa

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
        # This works:
        # states = session.query(State).join(City).order_by(City.id).all()
        # for state in states:
        #     for city in state.cities:
        #         print("{}: {} -> {}".format(city.id, city.name, state.name))

        # but this is concise:
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    all_cities(argv[1], argv[2], argv[3])
