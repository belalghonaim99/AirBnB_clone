#!/usr/bin/python3
"""
Defines the User class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a user, inheriting from the BaseModel class.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    """The email address of the user."""
    password = ""
    """The password of the user."""
    first_name = ""
    """The first name of the user."""
    last_name = ""
