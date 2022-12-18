import unittest

from my_tinydb import database


class test_database(unittest.TestCase):
    def test_database_variables(self):
        file_location = database.full_path
        path_to_key = database.to_key
        self.assertIsNotNone(file_location)
        self.assertIsNotNone(path_to_key)
        self.assertIsNotNone(database.location)
        self.assertIsNotNone(database.data_base)
        

    def test_main_loop_function(self):
        pass
