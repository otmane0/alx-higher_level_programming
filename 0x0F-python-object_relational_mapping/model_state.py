#!/usr/bin/python3

"""Sqlalchemy"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base



Base = declarative_base()
class State(Base):
    """
    First class
    """
    __tablename__ = "states"

    id = Column(Integer ,primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


