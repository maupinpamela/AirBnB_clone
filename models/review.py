#!/usr/bin/python3
"""
This module contains the class Review, which inherits from
BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review - class that inherits from BaseModel
    Public Class Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
