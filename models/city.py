#!/usr/bin/python3
"""
Defines the City class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city, inheriting from the BaseModel class.

    Attributes:
        state_id (str): The identifier of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    """The identifier of the state associated with the city."""
    name = ""
    """The name of the city."""

