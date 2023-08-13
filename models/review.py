#!/usr/bin/python3

"""
Review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inheriting from BaseModel.
    
    Public class attributes:
    - place_id (str): Empty string. It will be the Place.id.
    - user_id (str): Empty string. It will be the User.id.
    - text (str): Empty string.
    """

    place_id = ""
    user_id = ""
    text = ""

