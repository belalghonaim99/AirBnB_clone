#!/usr/bin/python3

"""
Amenity class
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class inheriting from BaseModel.
    
    Attributes:
        name (str): Public class attribute representing the name of the amenity.
    """
    
    name = ""

