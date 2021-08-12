#!/usr/bin/python3
"""Module for test User class"""
import unittest
import pep8
import json
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Checks type """
        new = self.value(first_name="Aitor")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Checks type """
        new = self.value(last_name="Tilla")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Checks type """
        new = self.value(email="a@bcd.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Checks type """
        new = self.value(password="123456")
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
