#!/usr/bin/python3
"""This script prints all City objects from the
database hbtn_0e_14_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def all_cities(username, password, database):
    """Prints all City objects from the database hbtn_0e_14_usa

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
        # cities = session.query(City).order_by(City.id).all()
        # for city in cities:
        #     state = session.query(State).filter_by(id=city.state_id).first()
        #     print("{}: ({}) {}".format(state.name, city.id, city.name))
        cities = session.query(City).join(State).order_by(City.id).all()
        for city in cities:
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    all_cities(argv[1], argv[2], argv[3])
