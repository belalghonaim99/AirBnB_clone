#!/usr/bin/python3
"""Unit tests for the Amenity class after Task 9."""
import unittest
import json
import os
from shutil import copy2

from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""
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
            del a1, a2
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        if os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

    def test_amenity_class(self):
        """Tests the Amenity class after Task 9."""
        # Normal use: no args
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

        # Attribute `name` defaults to an empty string
        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, '')

        # Amenity can be serialized to JSON by FileStorage
        a1.name = 'test'
        self.assertIn(a1, storage._FileStorage__objects.values())
        a1.save()
        with open(storage._FileStorage__file_path, encoding='utf-8') as file:
            content = file.read()
        key = a1.__class__.__name__ + '.' + a1.id
        self.assertIn(key, json.loads(content))

        # Amenity can be deserialized from JSON by FileStorage
        self.assertIn(key, storage._FileStorage__objects.keys())
        storage._FileStorage__objects = dict()
        storage.reload()
        self.assertIn(key, storage._FileStorage__objects.keys())

if __name__ == '__main__':
    unittest.main()

