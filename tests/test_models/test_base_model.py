"""
Unit tests for the BaseModel class after Task 3.
"""

import datetime
import json
import os
import re
from shutil import copy2
import unittest

from models.base_model import BaseModel
from models import storage

def test_default_init(testobj, basemodel):
    # obj is an instance of BaseModel
    testobj.assertIsInstance(basemodel, BaseModel)

    # obj was assigned with UUID, created_at and updated_at
    testobj.assertIsNotNone(basemodel.id)
    testobj.assertIsNotNone(basemodel.created_at)
    testobj.assertIsNotNone(basemodel.updated_at)

# Other test functions...

class TestBaseModel(unittest.TestCase):
    """Tests the `BaseModel` class."""

    __objects_backup = storage._FileStorage__objects
    json_file = storage._FileStorage__file_path
    json_file_backup = storage._FileStorage__file_path + '.bup'

    @classmethod
    def setUpClass(cls):
        """Set up for all tests in the module."""
        storage._FileStorage__objects = dict()
        if os.path.exists(cls.json_file):
            copy2(cls.json_file, cls.json_file_backup)
            os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        """Tear down after all tests in the module."""
        storage._FileStorage__objects = cls.__objects_backup
        if os.path.exists(cls.json_file_backup):
            copy2(cls.json_file_backup, cls.json_file)
            os.remove(cls.json_file_backup)

    def tearDown(self):
        """Clean up after each test method."""
        try:
            del bm1, bm2, bm3, bm4, bm5
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        if os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

    def test_BaseModel(self):
        """Task 3. BaseModel; Task 5. Store first object
        Tests instantiation and type of class `BaseModel`.
        """
        # Normal use: no args
        bm1 = BaseModel() 
        test_default_init(self, bm1)

        # Other test cases...

if __name__ == '__main__':
    unittest.main()
