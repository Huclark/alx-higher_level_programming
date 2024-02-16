#!/usr/bin/python3
"""This script defines a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """A state class

    Args:
        Base (intance): Instance of declarative_base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
