#!/usr/bin/python3
"""Defines base subclass"""

from models.base_model import BaseModel

class City(BaseModel):
    """Defines a city class"""
    state_id = ""
    name = ""
