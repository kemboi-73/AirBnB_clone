#!/usr/bin/python3
"""File Storage Class
This module is in charge of the storage of the
classes and their management."""

import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """ FileStorage class to manage instances
    This is the File Storage module.
    Attributes:
        __file_path (str): This is the path of the JSON file in which
            the contents of the `__objects` variable will be stored.
        __objects (dict): This store all the instances data
        """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """Saves a new object in the `__objects` class attribute
        Args:
            obj (inst): The object to adds in the `__objects` class attribute
        Sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id.
        """
        class_name  = obj.__class__.__name__ 
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serializes the content of `__objects` class attribute
        The content of `__objects` class attribute will be serialized
        to the path of `__file_path` class attribute in JSON format
        with the `created_at` and `updated_at` formatted.
        """
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
           json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file in `__file_path` class attribute
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`
        class attribute like an instance with the object data.
        """
        _class ={
            'BaseModel': BaseModel,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User,
            }

        try:
            with open(FileStorage.__file_path, "r") as f:
                _dict = json.load(f)
                for k, v in _dict.items():
                    class_name, _id = k.split(".")
                    FileStorage.__objects[k] = globals()[class_name](**v)

        except FileNotFoundError:
            pass
