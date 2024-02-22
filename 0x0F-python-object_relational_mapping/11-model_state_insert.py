#!/usr/bin/python3
"""
This module prints the state object with the name passed as an argument
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """Main Function"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    """create tables defined in the models"""
    Base.metadata.create_all(engine)

    """create session factory to connect to the database"""
    Session = sessionmaker(bind=engine)

    """create session"""
    session = Session()

    fresh_state = State(name='Louisiana')
    session.add(fresh_state)
    session.commit()
    print(fresh_state.id)

    session.close()


if __name__ == "__main__":
    main()
