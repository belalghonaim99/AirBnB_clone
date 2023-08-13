"""Unit tests for the BaseModel class after Task 3."""
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

def test_default_id(testobj, basemodel):
    # id is string
    testobj.assertIs(type(basemodel.id), str)
    testobj.assertIsInstance(basemodel.id, str)

    # id is in uuid format
    UUIDv4_regex = ('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-'
                    '[89ab][a-f0-9]{3}-[a-f0-9]{12}$')
    UUIDv4 = re.compile(UUIDv4_regex, re.IGNORECASE)
    testobj.assertRegex(basemodel.id, UUIDv4)

def test_default_created_at(testobj, basemodel):
    # created_at is a datetime object
    testobj.assertIs(type(basemodel.created_at), datetime.datetime)
    testobj.assertIsInstance(basemodel.created_at, datetime.datetime)

    # created_at in UTC (tzinfo = None)
    testobj.assertIsNone(basemodel.created_at.tzinfo)

    # created_at for new instance matches current time (to the second)
    current = datetime.datetime.now()
    testobj.assertEqual(current.isoformat()[:-6], basemodel.created_at.isoformat()[:-6])

    # created_at can be converted to ISO format string
    ISO_format = '%Y-%m-%dT%H:%M:%S.%f'
    dt_str = basemodel.created_at.strftime(ISO_format)
    testobj.assertEqual(dt_str, basemodel.created_at.isoformat())

def test_default_updated_at(testobj, basemodel):
    # updated_at is a datetime object
    testobj.assertIs(type(basemodel.updated_at), datetime.datetime)
    testobj.assertIsInstance(basemodel.updated_at, datetime.datetime)

    # updated_at in UTC (tzinfo = None)
    testobj.assertIsNone(basemodel.updated_at.tzinfo)

    # updated_at for new instance matches current time (to the second)
    current = datetime.datetime.now()
    testobj.assertEqual(current.isoformat()[:-6],
                        basemodel.updated_at.isoformat()[:-6])

    # updated_at can be converted to ISO format string
    ISO_format = '%Y-%m-%dT%H:%M:%S.%f'
    dt_str = basemodel.updated_at.strftime(ISO_format)
    testobj.assertEqual(dt_str, basemodel.updated_at.isoformat())

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

        # only arg (no kwarg) as an argument
        bm2 = BaseModel(None)
        test_default_init(self, bm2)
        test_default_id(self, bm2)
        test_default_created_at(self, bm2)
        test_default_updated_at(self, bm2)

        # arg and kwarg both passed as arguments
        bm1_kwarg = bm1.to_dict()
        bm3 = BaseModel("Holberton", **bm1_kwarg)
        test_default_init(self, bm3)
        test_default_id(self, bm3)
        self.assertEqual(bm1.id, bm3.id)
        test_default_created_at(self, bm3)
        self.assertEqual(bm1.created_at, bm3.created_at)
        test_default_updated_at(self, bm3)
        self.assertEqual(bm1.updated_at, bm3.updated_at)

        # passing kwarg only + keys not in dictionary
        bm1.name = "Holbie"
        bm1.num = 98
        bm1_kwarg = bm1.to_dict()
        bm4 = BaseModel(**bm1_kwarg)
        test_default_init(self, bm4)
        self.assertIsNotNone(bm4.name)
        self.assertEqual(bm1.name, bm4.name)
        self.assertIsNotNone(bm4.num)
        self.assertEqual(bm1.num, bm4.num)
        test_default_id(self, bm4)
        self.assertEqual(bm1.id, bm4.id)
        test_default_created_at(self, bm4)
        self.assertEqual(bm1.created_at, bm4.created_at)
        test_default_updated_at(self, bm4)
        self.assertEqual(bm1.updated_at, bm4.updated_at)

        # empty dictionary as argument
        empty = {}
        bm5 = BaseModel(**empty)
        test_default_init(self, bm5)
        test_default_id(self, bm5)
        test_default_created_at(self, bm5)
        test_default_updated_at(self, bm5)

        # storage.new() called in BaseModel.__init__ to add obj to __objects
        self.assertIn(bm1, storage._FileStorage__objects.values())

    # Other test methods...

if __name__ == '__main__':
    unittest.main()

