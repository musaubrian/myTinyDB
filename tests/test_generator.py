# tests/test_generator.py
import unittest
import pyperclip
from my_tinydb.generator import generate_password


class TestGeneratePassword(unittest.TestCase):
    def test_generate_password(self):
        # setup
        pyperclip.copy("")

        # test
        generate_password()

        # assert
        self.assertIsNotNone(pyperclip.paste())
        self.assertEqual(len(pyperclip.paste()), 15)

if __name__ == '__main__':
    unittest.main()
