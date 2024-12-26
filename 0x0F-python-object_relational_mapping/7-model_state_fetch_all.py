#!/usr/bin/python3

"""Sqlalchemy"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":


    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()


    states = session.query(State).order_by(State.id).all()


    for state in states:
        print (f"{state.id}: {state.name}")
