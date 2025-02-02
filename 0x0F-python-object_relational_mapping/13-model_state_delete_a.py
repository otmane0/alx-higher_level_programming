#!/usr/bin/python3
""" Get a state
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    all_a = session.query(State).filter(State.name.like('%a%\
')).all()
    for one in all_a:
        session.delete(one)
    session.commit()
    session.close()
