#!/usr/bin/python3
"""This script deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def delete_state(username, password, database):
    """Deletes all State objects with a name containing the letter
    'a'

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
        states = session.query(State).filter(
            State.name.like("%a%")).order_by(State.id).all()
        for state in states:
            session.delete(state)
        session.commit()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    # execute function
    delete_state(argv[1], argv[2], argv[3])
