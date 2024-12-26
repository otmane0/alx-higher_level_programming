
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

    url = f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}?charset=utf8mb4"


    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()


    for state in states:
        session.delete(state)

    session.commit()
    session.close()
