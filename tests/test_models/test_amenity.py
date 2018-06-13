"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class Test_Amenity(unittest.TestCase):
    """Unittest for th Amenity class"""

    @classmethod
    def setUp(self):
        """sets up for the tests"""
        self.amenity = Amenity()
        self.amenity.name = "Shoelaces"

    @classmethod
    def tearDown(self):
        """This will tear down when the test is over"""
        del self.amenity

    def test_docstring_Amenity(self):
        """checks for a docstring comment"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_Pep8_Amenity(self):
        """checks for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_Amenity(self):
        """checks to see if Amenity is a class of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_atts_in_dict_Amenity(self):
        """checks if there are attributes"""
        self.assertTrue('name' in self.amenity.__dict__)

    def test_save_Amenity(self):
        """checks to see if save functions"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
