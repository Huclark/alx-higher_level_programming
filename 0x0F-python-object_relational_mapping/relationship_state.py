#!/usr/bin/python3
"""This script defines a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """A state class

    Args:
        Base (instance): Instance of declarative_base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
