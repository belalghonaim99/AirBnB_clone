file_storage.py--------------

#!/usr/bin/python3
"""
Define the FileStorage class for serialization and deserialization.
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    FileStorage class for serializing instances to JSON and deserializing JSON to instances.

    Attributes:
    - __file_path: string - path to the JSON file (e.g., file.json)
    - __objects: dictionary - stores objects by <class name>.id (e.g., BaseModel.12121212)
    """

    __file_path = "object_contents.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_objects = {}
        for key in self.__objects:
            new_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_objects))

    def reload(self):
        """
        Deserializes the JSON file to __objects, only if the JSON file __file_path exists;
        otherwise, no action is taken. If the file doesn't exist, no exception should be raised.
        """
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    new_objects = json.load(file)
                for key, value in new_objects.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
            except:
                pass

