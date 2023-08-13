#!/usr/bin/python3
"""
Defines the Review class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review, inheriting from the BaseModel class.

    Attributes:
        place_id (str): The identifier of the associated place.
        user_id (str): The identifier of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    """The identifier of the associated place."""
    user_id = ""
    """The identifier of the user who wrote the review."""
    text = ""
    """The content of the review."""
