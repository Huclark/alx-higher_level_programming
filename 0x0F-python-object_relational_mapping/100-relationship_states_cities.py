#!/usr/bin/python3
"""This script  creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State


def create_state(username, password, database):
    """Creates the State “California” with the
    City “San Francisco” from the database hbtn_0e_100_usa

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
        # create Carlifornia state and San Francisco city
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        session.add(city)
        session.commit()

        # alternate is to append to states
        # state = State(name="California")
        # state.cities.append(City(name="San Fransisco"))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    create_state(argv[1], argv[2], argv[3])
