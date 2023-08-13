#!/usr/bin/python3
"""
Create a unique instance of FileStorage for your application.
"""

from models.engine.file_storage import FileStorage

# Initialize a FileStorage instance to manage data storage
storage = FileStorage()

# Reload any existing data to make it available for use
storage.reload()
