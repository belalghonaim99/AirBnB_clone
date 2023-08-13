#!/usr/bin/python3
"""
Define the Review class with public class attributes.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Public class attributes:
    - place_id: string (empty by default) - represents the associated Place.id
    - user_id: string (empty by default) - represents the associated User.id
    - text: string (empty by default)
    """

    place_id = ""
    user_id = ""
    text = ""
