#!/usr/bin/python3
""" This module contains a base class known as BaseModel
from which all other classes inherit common attributes and methods
"""
from datetime import datetime, date
import uuid
import json
import models


class BaseModel:
    """This is a base class that contains common objects shared by other
    child classes
    """
    def __init__(self, *args, **kwargs):
        """Intializes attributed of base class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
			setattr(self, key, value)
			continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the Base Class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
	models.storage.new(self)
	models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
