#!/usr/bin/python3

"""sqlalchemy"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

url = "mysql+mysqlconnector://root:@localhost:3306/teest?charset=utf8mb4"


engine = create_engine(url)

Base = declarative_base()
class State(Base):
    __tablename__ = "states"

    id = Column(Integer ,primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)





