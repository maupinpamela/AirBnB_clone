#!/usr/bin/python3
"""
This module contains a unittest for the BaseModel Class
"""
from unittest import TestCase
import pep8
import os
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """
    Unittest for BaseModel Class
    """
    @classmethod
    def setUp(cls):
        cls.base_a = BaseModel()
        cls.base_a = "Afa"
