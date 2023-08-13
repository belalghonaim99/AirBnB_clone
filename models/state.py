#!/usr/bin/python3
"""
Define the State class with a public class attribute.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Public class attributes:
    - name: string (empty by default)
    """

    name = ""
