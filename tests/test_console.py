#!/usr/bin/python3
"""This module has the test for the base class"""
from tests import reader
import models
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import time
import os
import threading
import signal


class MyTestCase(unittest.TestCase):
    """
    Test console commands
    """

    def setUp(self):
        """
        set up the enviroment to read from stdout
        """
        reader.readed = 0
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def tearDown(self):
        """
        remove file.json when done with test
        """
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test_quit(self):
        """Test quiting the console"""
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd('quit')

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().onecmd('help')
            self.assertEqual(stdout.getvalue(),
                             '\nDocumented commands (type help <topic>):\n\
========================================\nEOF  all\
  count  create  destroy  help  quit  show  update\n\n')

    def test_help_show(self):
        """Test show command"""
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().onecmd('help show')
            self.assertEqual(stdout.getvalue(),
                             'Shows an individual instance of a class\n[Usage]:' +
                             ' show <className> <objectId>\n\n')

    def test_show_function(self):
        """
        test shwo function
        """
        with patch('sys.stdout', new=StringIO()) as stdout:
            HBNBCommand().onecmd('create User')
            User_id = reader.read(stdout)[:-1]
            HBNBCommand().onecmd('show User '+User_id)
            self.assertEqual(reader.read(stdout),
                             str(models.storage.all()['User.'+User_id])+"\n")

    @unittest.skip("user.count() not implemented in this version")
    def test_count_function(self):
        """
        test count function
        """
        with patch('sys.stdout', new=StringIO()) as stdout:
            HBNBCommand().onecmd('create User')
            User_id = reader.read(stdout)[:-1]
            HBNBCommand().onecmd('User.count()')
            self.assertEqual(reader.read(stdout=stdout), '1\n')

    def test_kwargs_User(self):
        """
        test create User using kwargs
        """
        with patch('sys.stdout', new=StringIO()) as stdout:
            HBNBCommand().onecmd('create User name="Juancho" age=34 averageScore=-3.6 extra="extra"__"')
            User_id = reader.read(stdout)[:-1]
            u1 = storage.all()['User.'+User_id]
            self.assertEqual(u1.name, "Juancho")
            self.assertEqual(u1.age, 34)
            self.assertEqual(u1.averageScore, -3.6)
            with self.assertRaises(AttributeError):
                u1.extra
