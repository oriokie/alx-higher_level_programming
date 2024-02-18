#!/usr/bin/python3
"""
State Module for geting all state objects
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def fetch_all_states():
    """Function for fetching all the states"""
    username = argv[1]
    password = argv[2]
    db = argv [3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()

    Session.configure(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name__ == "__main__":
    fetch_all_states()
