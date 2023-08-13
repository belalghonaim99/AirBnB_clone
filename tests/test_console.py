#!/usr/bin/python3
"""Unit tests for the console module (Task 17)."""
import unittest
import json
import os
from shutil import copy2
import cmd

from console import HBNBCommand
from models import storage

class TestConsole(unittest.TestCase):
    """Tests the functionality of the console command interpreter."""
    __objects_backup = storage._FileStorage__objects
    json_file = storage._FileStorage__file_path
    json_file_backup = storage._FileStorage__file_path + '.bup'

    @classmethod
    def setUpClass(cls):
        """Set up before all tests in the module."""
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
            del (s1, s2)
        except NameError:
            pass
        storage._FileStorage__objects = dict()
        if os.path.exists(type(self).json_file):
            os.remove(type(self).json_file)

    def test_console_initialization(self):
        """Test the initialization of the console command interpreter."""
        self.assertIsNotNone(HBNBCommand())

