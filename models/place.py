#!/usr/bin/python3
"""
Defines the Place class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Represents a place, inheriting from the BaseModel class.

    Attributes:
        city_id (str): The identifier of the associated city.
        user_id (str): The identifier of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of identifiers for associated amenities.
    """

    city_id = ""
    """The identifier of the associated city."""
    user_id = ""
    """The identifier of the user who owns the place."""
    name = ""
    """The name of the place."""
    description = ""
    """A description of the place."""
    number_rooms = 0
    """The number of rooms in the place."""
    number_bathrooms = 0
    """The number of bathrooms in the place."""
    max_guest = 0
    """The maximum number of guests the place can accommodate."""
    price_by_night = 0
    """The price per night for the place."""
    latitude = 0.0
    """The latitude coordinate of the place."""
    longitude = 0.0
    """The longitude coordinate of the place."""
    amenity_ids = []
    """A list of identifiers for associated amenities."""
