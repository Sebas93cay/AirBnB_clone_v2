#!/usr/bin/python3
"""Module for test Place class"""
import unittest
import pep8
import models
import json
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test State class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Checks type """
        new = self.value(city_id="12345678s9")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Checks type """
        new = self.value(user_id="12345678s9")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Checks type """
        new = self.value(name="Holberton")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Checks type """
        new = self.value(description="Lorem Ipsum")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Checks type """
        new = self.value(number_rooms=2)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Checks type """
        new = self.value(number_bathrooms=1)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Checks type """
        new = self.value(max_guest=4)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Checks type """
        new = self.value(price_by_night=40)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Checks type """
        new = self.value(latitude=123456789.0)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Checks type """
        new = self.value(latitude=2.2)
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Checks type"""
        new = self.value(amenity_ids=["Wifi", "Tv", "AC"])
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
