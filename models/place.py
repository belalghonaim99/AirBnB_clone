#!/usr/bin/python3

"""
Place class
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class inheriting from BaseModel.
    
    Public class attributes:
    - city_id (str): Empty string. It will be the City.id.
    - user_id (str): Empty string. It will be the User.id.
    - name (str): Empty string.
    - description (str): Empty string.
    - number_rooms (int): 0.
    - number_bathrooms (int): 0.
    - max_guest (int): 0.
    - price_by_night (int): 0.
    - latitude (float): 0.0.
    - longitude (float): 0.0.
    - amenity_ids (list of str): Empty list. It will be the list of Amenity.id values later.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

