#!/usr/bin/python3
"""
This module contains the class BaseModel which defines all
common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models
import json


class BaseModel():
    """
    BaseModel defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel
        Args:
            id: id generated with uuid
            created_at: time instance was created
            updated_at: time instance was updated
        """
        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            elif not isinstance(kwargs['created_at'], datetime):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            elif not isinstance(kwargs['updated_at'], datetime):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Public instance method that returns a dictionary
        containing all keys/values of __dict__ of an instance
        """
        dict_copy = dict(self.__dict__)
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = datetime.now().isoformat()
        dict_copy['updated_at'] = datetime.now().isoformat()
        return dict_copy

    def __str__(self):
        """String magic method"""
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)
