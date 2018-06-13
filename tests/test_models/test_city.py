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
        self.city.state_id = "California"

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
        self.assertTrue('state_id' in self.city.__dict__)

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

    def test_init_arg(self):
        """pass in arg to new instance"""
        i = City(23)
        self.assertEqual(type(i).__name__, "City")
        self.assertFalse(hasattr(i, "23"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        i = City()
        printed = i.__str__()
        self.assertEqual(printed,
                         "[City] ({}) {}".format(i.id, i.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        i = City()
        new_dict = i.__dict__
        self.assertEqual(type(i).__name__, "City")
        self.assertTrue(hasattr(i, '__class__'))
        self.assertEqual(str(i.__class__),
                         "<class 'models.city.City'>")
        self.assertTrue(type(new_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict"""
        my_model = City()
        new_model = City()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, City)
        self.assertEqual(type(my_model).__name__, "City")
        self.assertEqual(test_dict['__class__'], "City")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """checks to see if instances in Basemodel are made correctly"""
        i = City()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "created_at"))
        self.assertTrue(hasattr(i, "updated_at"))
        self.assertTrue(hasattr(i, "id"))


if __name__ == "__main__":
    unittest.main()
