#!/usr/bin/python3
"""
This module contains the class FileStorage that serializes instances
to a JSON file and deserializes JSON files to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    This class serializes/deserializes JSON instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns a dictionary of __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new - sets obj with <obj class name>.id in __objects
        Args:
            obj: object to be set
        """
        obj_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        file_name = FileStorage.__file_path
        dict_storage = {}
        for obj_id, obj in FileStorage.__objects.items():
            dict_storage[obj_id] = obj.to_dict()
        with open(file_name, mode='w', encoding='utf-8') as f:
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes JSON file to __objects if it exists
        """
        file_name = FileStorage.__file_path
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                loaded_objs = json.load(f)
                for k, v in loaded_objs.items():
                    self.new(eval(v["__class__"])(**v))
        except:
            pass
