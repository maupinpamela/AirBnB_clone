#!/usr/bin/python3
"""
This module contains the class FileStorage that serializes instances
to a JSON file and deserializes JSON files to instances
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    This class serializes/deserializes JSON instances
    """
    __file_path = 'file.json'
    __objects = {}
    __class_names = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Place": Place,
                   "Amenity": Amenity,
                   "Review": Review}

    def all(self):
        """
        returns a dictionary of __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        new - sets obj with <obj class name>.id in __objects
        Args:
            obj: object to be set
        """
        if obj:
            obj_id = "{}.{}".format(str(type(obj).__name__), obj.id)
            self.__objects[obj_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_storage = {}
        for obj_id, obj in self.__objects.items():
            dict_storage[obj_id] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes JSON file to __objects if it exists
        """
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                loaded_objs = json.load(f)
            for k, v in loaded_objs.items():
                obj = self.__class_names[v["__class__"]](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass
