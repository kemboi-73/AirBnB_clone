#!/usr/bin/python3
"""Defines a base subclass"""
from models.base_model import BaseModel

class Review(BaseModel):
    """The review class"""
    place_id = ""
    user_id =""
    text = ""
