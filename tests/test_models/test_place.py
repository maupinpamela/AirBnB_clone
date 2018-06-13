#!/usr/bin/python3
"""
This module contains a unittest for the Place Class
"""
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Unittest for Place Class
    """
    @classmethod
    def setUpClass(cls):
        cls.place_a = Place()
        cls.place_a.city_id = "This is America"
        cls.place_a.user_id = "Donald Glover"
        cls.place_a.name = "Gambino"
        cls.place_a.description = "Childish"
        cls.place_a.number_rooms = 0
        cls.place_a.number_bathrooms = 0
        cls.place_a.max_guest = 0
        cls.place_a.price_by_night = 0
        cls.place_a.latitude = 0.0
        cls.place_a.longitude = 0.0
        cls.place_a.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.place_a
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instantiation(self):
        self.assertIsInstance(self.place_a, Place)

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.place_a.__class__, BaseModel), True)

    def test_check_documentation(self):
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_present(self):
        self.assertTrue('id' in self.place_a.__dict__)
        self.assertTrue('created_at' in self.place_a.__dict__)
        self.assertTrue('updated_at' in self.place_a.__dict__)
        self.assertTrue('city_id' in self.place_a.__dict__)
        self.assertTrue('user_id' in self.place_a.__dict__)
        self.assertTrue('name' in self.place_a.__dict__)
        self.assertTrue('description' in self.place_a.__dict__)
        self.assertTrue('number_rooms' in self.place_a.__dict__)
        self.assertTrue('number_bathrooms' in self.place_a.__dict__)
        self.assertTrue('max_guest' in self.place_a.__dict__)
        self.assertTrue('price_by_night' in self.place_a.__dict__)
        self.assertTrue('latitude' in self.place_a.__dict__)
        self.assertTrue('longitude' in self.place_a.__dict__)
        self.assertTrue('amenity_ids' in self.place_a.__dict__)

    def test_attribute_type(self):
        self.assertEqual(type(self.place_a.city_id), str)
        self.assertEqual(type(self.place_a.user_id), str)
        self.assertEqual(type(self.place_a.name), str)
        self.assertEqual(type(self.place_a.description), str)
        self.assertEqual(type(self.place_a.number_rooms), int)
        self.assertEqual(type(self.place_a.number_bathrooms), int)
        self.assertEqual(type(self.place_a.max_guest), int)
        self.assertEqual(type(self.place_a.price_by_night), int)
        self.assertEqual(type(self.place_a.latitude), float)
        self.assertEqual(type(self.place_a.longitude), float)
        self.assertEqual(type(self.place_a.amenity_ids), list)

    def test_save(self):
        self.place_a.save()
        self.assertNotEqual(self.place_a.created_at, self.place_a.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place_a), True)


if __name__ == "__main__":
    unittest.main()
