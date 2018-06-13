#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import pep8
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    Unittest for file_storage.py
    """

    @classmethod
    def setUpClass(cls):
        cls.rev_a = Review()
        cls.rev_a.place_id = "Krypton"
        cls.rev_a.user_id = "Kal El"
        cls.rev_a.text = "Son of Krypton"

    @classmethod
    def tearDown(cls):
        del cls.rev_a

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instantiation(self):
        """
        Tests for proper instantiation
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_all(self):
        """
        Tests all method
        """
        temp_storage = FileStorage()
        inst_dict = temp_storage.all()
        self.assertIsNotNone(inst_dict)
        self.assertEqual(type(inst_dict), dict)
        self.assertIs(inst_dict, temp_storage._FileStorage__objects)

    def test_new(self):
        """
        Test for proper use of new method
        """
        storage = FileStorage()
        inst_dict = storage.all()
        Afa = User()
        Afa.id = 619619
        Afa.name = "Afa"
        storage.new(Afa)
        class_name = Afa.__class__.__name__
        key = "{}.{}".format(class_name, str(Afa.id))
        self.assertIsNotNone(inst_dict[key])

    def test_reload(self):
        """
        Tests for proper use of reload method
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for line in f:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
