"""test for City"""
import unittest
from models.city import City
from models.base_model import BaseModel
import pep8


class Test_City(unittest.TestCase):
    """Unittest for th City class"""

    @classmethod
    def setUp(self):
        """sets up for the tests"""
        self.city = City()
        self.city.name = "Pasadena"
        self.city._state_id = "California"

    @classmethod
    def tearDown(self):
        """This will tear down when the test is over"""
        del self.city

    def test_docstring_City(self):
        """checks for a docstring comment"""
        self.assertIsNotNone(City.__doc__)

    def test_Pep8_City(self):
        """checks for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_City(self):
        """checks to see if City is a class of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_atts_in_dict_City(self):
        """checks if there are attributes"""
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_save_City(self):
        """checks to see if save functions"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
