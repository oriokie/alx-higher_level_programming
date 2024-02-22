#!/usr/bin/python3
"model for the state"

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    "City model"

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
