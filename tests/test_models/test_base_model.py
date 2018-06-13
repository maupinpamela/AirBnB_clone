#!/usr/bin/python3
"""
This module contains a unittest for the BaseModel Class
"""
import unittest
import pep8
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Unittest for BaseModel Class
    """
    @classmethod
    def setUpClass(cls):
        cls.base_a = BaseModel()
        cls.base_a.name = "Afa"
        cls.base_a.my_number = 69

    @classmethod
    def tearDownClass(cls):
        del cls.base_a
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.base_a, BaseModel))

    def test_save(self):
        self.base_a.save()
        self.assertNotEqual(self.base_a.created_at, self.base_a.updated_at)

    def test_to_dict(self):
        base_a_dict = self.base_a.to_dict()
        self.assertEqual(self.base_a.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_a_dict['created_at'], str)
        self.assertIsInstance(base_a_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
