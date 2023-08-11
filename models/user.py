#!/usr/bin/python3
"""Defines User subclass"""

from models.base_model import BaseModel


class User(BaseModel):
    """The user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
