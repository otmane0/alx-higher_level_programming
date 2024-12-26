#!/usr/bin/python3

"""Sqlalchemy"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}?charset=utf8mb4"


    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()


    states = session.query(State).filter(State.name == state_name_to_search).first()


    if states:
        print(f"{states.id}")
    else:
        print("Not found")

