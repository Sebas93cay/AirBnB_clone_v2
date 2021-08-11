#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
or DBStorage depending on the enviroment HBNB_TYPE_STORAGE
"""

import os
STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')

if STORAGE_TYPE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
