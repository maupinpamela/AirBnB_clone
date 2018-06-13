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

    def test_init_arg(self):
        """pass in arg to new instance"""
        i = Amenity(23)
        self.assertEqual(type(i).__name__, "Amenity")
        self.assertFalse(hasattr(i, "23"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        i = Amenity()
        printed = i.__str__()
        self.assertEqual(printed,
                         "[Amenity] ({}) {}".format(i.id, i.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        i = Amenity()
        new_dict = i.__dict__
        self.assertEqual(type(i).__name__, "Amenity")
        self.assertTrue(hasattr(i, '__class__'))
        self.assertEqual(str(i.__class__),
                         "<class 'models.amenity.Amenity'>")
        self.assertTrue(type(new_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict"""
        my_model = Amenity()
        new_model = Amenity()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Amenity)
        self.assertEqual(type(my_model).__name__, "Amenity")
        self.assertEqual(test_dict['__class__'], "Amenity")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """checks to see if instances in Basemodel are made correctly"""
        i = Amenity()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "created_at"))
        self.assertTrue(hasattr(i, "updated_at"))
        self.assertTrue(hasattr(i, "id"))

if __name__ == "__main__":
    unittest.main()
