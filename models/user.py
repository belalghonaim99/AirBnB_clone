#!/usr/bin/python3
"""
Define the User class with public class attributes.
"""

from .base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Defines attributes for `User`:
    - email: string (empty by default)
    - password: string (empty by default)
    - first_name: string (empty by default)
    - last_name: string (empty by default)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
