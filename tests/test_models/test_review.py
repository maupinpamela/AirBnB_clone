"""test for Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import pep8


class Test_Review(unittest.TestCase):
    """Unittest for th Review class"""

    @classmethod
    def setUp(self):
        """sets up for the tests"""
        self.review = Review()
        self.review.place_id = "1612"
        self.review.user_id = "187"
        self.review.text = "Code"

    @classmethod
    def tearDown(self):
        """This will tear down when the test is over"""
        del self.review

    def test_docstring_Review(self):
        """checks for a docstring comment"""
        self.assertIsNotNone(Review.__doc__)

    def test_Pep8_Review(self):
        """checks for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Class_Review(self):
        """checks to see if Review is a class of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_atts_in_dict_Review(self):
        """checks if there are attributes"""
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_save_Review(self):
        """checks to see if save functions"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_init_arg(self):
        """pass in arg to new instance"""
        i = Review(23)
        self.assertEqual(type(i).__name__, "Review")
        self.assertFalse(hasattr(i, "23"))

    def test_str_method(self):
        """Tests to see if each method is printing accurately"""
        i = Review()
        printed = i.__str__()
        self.assertEqual(printed,
                         "[Review] ({}) {}".format(i.id, i.__dict__))

    def test_before_todict(self):
        """Tests instances before using to_dict conversion"""
        i = Review()
        new_dict = i.__dict__
        self.assertEqual(type(i).__name__, "Review")
        self.assertTrue(hasattr(i, '__class__'))
        self.assertEqual(str(i.__class__),
                         "<class 'models.review.Review'>")
        self.assertTrue(type(new_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(new_dict['id']), 'str')

    def test_after_todict(self):
        """Test instances after using to_dict"""
        my_model = Review()
        new_model = Review()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Review)
        self.assertEqual(type(my_model).__name__, "Review")
        self.assertEqual(test_dict['__class__'], "Review")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """checks to see if instances in Basemodel are made correctly"""
        i = Review()
        self.assertTrue(hasattr(i, "__init__"))
        self.assertTrue(hasattr(i, "created_at"))
        self.assertTrue(hasattr(i, "updated_at"))
        self.assertTrue(hasattr(i, "id"))


if __name__ == "__main__":
    unittest.main()
