"""test for amenity"""
import unittest
from models.state import State
from models.base_model import BaseModel
import pep8


class Test_State(unittest.TestCase):
    """Unittest for the State class"""

    @classmethod
    def setUp(self):
        """sets up for the tests"""
        self.state = State()
        self.state.name = "Nevada"

    @classmethod
    def tearDown(self):
        """This will tear down when the test is over"""
        del self.state

    def test_docstring_State(self):
        """checks for a docstring comment"""
        self.assertIsNotNone(State.__doc__)

    def test_Pep8_State(self):
        """checks for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_State(self):
        """checks to see if Amenity is a class of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_atts_in_dict_State(self):
        """checks if there are attributes"""
        self.assertTrue('name' in self.state.__dict__)

    def test_save_State(self):
        """checks to see if save functions"""
        self.state.save()

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
