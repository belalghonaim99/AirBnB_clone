#!/usr/bin/python3

"""
City class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inheriting from BaseModel
    Attributes:
        state_id (str): Public class attribute representing the state ID of the city.
        name (str): Public class attribute representing the name of the city.
    """

    state_id = ""
    name = ""

