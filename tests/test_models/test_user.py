"""test for User"""
import unittest
from models.user import User
from models.base_model import BaseModel
import pep8


class Test_User(unittest.TestCase):
    """Unittest for th User class"""

    @classmethod
    def setUp(self):
        """sets up for the tests"""
        self.user = User()
        self.user.place_id = "1612"
        self.user.user_id = "187"
        self.user.text = "Code"

    @classmethod
    def tearDown(self):
        """This will tear down when the test is over"""
        del self.user

    def test_docstring_User(self):
        """checks for a docstring comment"""
        self.assertIsNotNone(User.__doc__)

    def test_Pep8_User(self):
        """checks for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_User(self):
        """checks to see if User is a class of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_atts_in_dict_User(self):
        """checks if there are attributes"""
        self.assertTrue('place_id' in self.user.__dict__)
        self.assertTrue('user_id' in self.user.__dict__)
        self.assertTrue('text' in self.user.__dict__)

    def test_save_User(self):
        """checks to see if save functions"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.place_id), str)
        self.assertEqual(type(self.user.user_id), str)
        self.assertEqual(type(self.user.text), str)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_init_arg(self):
        """pass in arg to new instance"""
        i = User(23)
        self.assertEqual(type(i).__name__, "User")
        self.assertFalse(hasattr(i, "23"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        i = User()
        printed = i.__str__()
        self.assertEqual(printed,
                         "[User] ({}) {}".format(i.id, i.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        i = User()
        new_dict = i.__dict__
        self.assertEqual(type(i).__name__, "User")
        self.assertTrue(hasattr(i, '__class__'))
        self.assertEqual(str(i.__class__),
                         "<class 'models.user.User'>")
        self.assertTrue(type(new_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict"""
        my_model = User()
        new_model = User()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, User)
        self.assertEqual(type(my_model).__name__, "User")
        self.assertEqual(test_dict['__class__'], "User")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """checks to see if instances in Basemodel are made correctly"""
        i = User()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "created_at"))
        self.assertTrue(hasattr(i, "updated_at"))
        self.assertTrue(hasattr(i, "id"))


if __name__ == "__main__":
    unittest.main()
