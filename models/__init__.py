#!/usr/bin/python3
"""
Initialization magic method for the models directory.
"""

from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload data into the storage
storage.reload()

