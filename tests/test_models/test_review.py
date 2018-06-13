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


if __name__ == "__main__":
    unittest.main()
