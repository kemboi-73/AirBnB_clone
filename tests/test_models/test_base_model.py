#!/usr/bin/python3
"""This module contains unittests for base class"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Tests usage cases for base class"""
    def test_base_args(self):
        """Tests base instantiation with arbitrary keyword
        arguments
        """
        attributes = {
                    'id': '123',
                    'created_at': '2023-08-08T00:00:00',
                    'updated_at': '2023-08-08T00:00:00',
                    }
        b = BaseModel(**attributes)
        self.assertEqual(b.id, '123')
        self.assertEqual(b.created_at,
                         datetime.fromisoformat('2023-08-08T00:00:00.000000'))
        self.assertEqual(b.updated_at,
                         datetime.fromisoformat('2023-08-08T00:00:00.000000'))

    def test_base_no_args(self):
        """Tests base class instantiation with no args"""
        b = BaseModel()
        self.assertIsNotNone(b.id)
        self.assertIsNotNone(b.created_at)
        self.assertIsNotNone(b.updated_at)
        self.assertEqual(b.created_at, b.updated_at)

    def test_base_unused_args(self):
        """Tests which attributes remain unused in an instance"""
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_base_kwargs_passed(self):
        """Tests instantiation with kwargs"""
        date_time = datetime.now()
        _format = date_time.isoformat()
        b = BaseModel(id='000', created_at=_format, updated_at=_format)
        self.assertEqual(b.id, '000')
        self.assertEqual(b.created_at, date_time)
        self.assertEqual(b.updated_at, date_time)

    def test_base_kwargs_None(self):
        """Tests when None is passed as kwargs values"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_base_id_is_string(self):
        """Tests if id attribute is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_base_id_is_unique(self):
        """Tests if different instances generate unique ids"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_base_created_at_is_datetime(self):
        """Checks if the attribute 'created_at' is a datetime object"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_base_created_at_timestamp(self):
        """ Checks if different class instantiations generate unique
        timestamps
        """
        b1 = BaseModel()
        sleep(2)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_base_updated_at_is_datetime(self):
        """Checks if the attribute 'updated_at' is a datetime object"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_base_updated_at_timestamp(self):
        """Checks idf different instantitions generate unique timestamps"""
        b1 = BaseModel()
        sleep(2)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)
