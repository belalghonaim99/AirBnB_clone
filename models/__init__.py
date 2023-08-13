#!/usr/bin/python3

"""
Create a variable to instantiate a unique FileStorage instance for your application.
"""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload data from files (if any)
storage.reload()

