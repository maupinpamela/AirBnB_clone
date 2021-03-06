#!/usr/bin/python3
"""
This module contains the class City, which inherits from
BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City - class that inherits from BaseModel
    Public Class Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
