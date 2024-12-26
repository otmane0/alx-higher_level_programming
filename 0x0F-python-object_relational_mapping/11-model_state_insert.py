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

    url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}?charset=utf8mb4"


    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name = "Louisiana")

    session.add(new_state)

    session.commit()
    print(new_state.id)


