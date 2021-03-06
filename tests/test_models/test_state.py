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
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_State(self):
        """checks to see if State is a class of BaseModel"""
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

    def test_init_arg(self):
        """pass in arg to new instance"""
        i = State(23)
        self.assertEqual(type(i).__name__, "State")
        self.assertFalse(hasattr(i, "23"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        i = State()
        printed = i.__str__()
        self.assertEqual(printed,
                         "[State] ({}) {}".format(i.id, i.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        i = State()
        new_dict = i.__dict__
        self.assertEqual(type(i).__name__, "State")
        self.assertTrue(hasattr(i, '__class__'))
        self.assertEqual(str(i.__class__),
                         "<class 'models.state.State'>")
        self.assertTrue(type(new_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict"""
        my_model = State()
        new_model = State()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, State)
        self.assertEqual(type(my_model).__name__, "State")
        self.assertEqual(test_dict['__class__'], "State")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """checks to see if instances in Basemodel are made correctly"""
        i = State()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "created_at"))
        self.assertTrue(hasattr(i, "updated_at"))
        self.assertTrue(hasattr(i, "id"))


if __name__ == "__main__":
    unittest.main()
