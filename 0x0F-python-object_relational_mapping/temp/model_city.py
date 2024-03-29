#!/usr/bin/python3
"""
Contains the class definition of a City
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import ForeignKey


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
