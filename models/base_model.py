#!/usr/bin/python3
"""
Defines the BaseModel class, which serves as the foundation for other classes.
"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Represents the fundamental class for the HBnB project.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The creation date and time of the instance.
        updated_at (datetime): The date and time of the last update to the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime and save the instance.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair `__class__` representing the class name of the object.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

