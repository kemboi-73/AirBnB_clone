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
        
    def test_base_str_method(self):
        """Tests base class str method"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.__str__, b2.__str__)

    def test_base_save_method(self):
        """Tests if save methid is working correctly"""
        b = BaseModel()
        sleep(2)
        prev_update = b.updated_at
        b.save()
        self.assertLess(prev_update, b.updated_at)

    def test_base_two_saves(self):
        "Tests two instances of save method"""
        b = BaseModel()
        sleep(2)
        update_1 = b.updated_at
        b.save()
        update_2 = b.updated_at
        self.assertLess(update_1, update_2)
        sleep(2)
        b.save()
        self.assertLess(update_2, b.updated_at)

    def test_base_to_dict_method(self):
        """Tests that the dictionary representation of attributes
        is correct"""
        b = BaseModel()
        expected_dict = {
                'id': b.id,
                'created_at': b.created_at.isoformat(),
                'updated_at': b.updated_at.isoformat(),
                '__class__': 'BaseModel',
                }
        self.assertEqual(b.to_dict(), expected_dict)

    def test_base_dict_is_returned(self):
        """Checks that base class returns a dictionary"""
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))

    def test_base_diff_dict_instances(self):
        """Checks that two class instantiations return
        different dicts"""
        b1 = BaseModel()
        sleep(2)
        b2 = BaseModel()
        self.assertNotEqual(b1.to_dict(), b2.to_dict())

    def test_base_to_dict_correct_keys(self):
        """Verifies that dict has correct keys"""
        b = BaseModel()
        self.assertIn('id', b.to_dict())
        self.assertIn('created_at', b.to_dict())
        self.assertIn('updated_at', b.to_dict())
        self.assertIn('__class__', b.to_dict())

    def test_dict_created_at_format(self):
        """Confims the format of 'created_at' attribute"""
        b = BaseModel()
        b1 = b.to_dict()
        _format = b1['created_at']
        self.assertEqual(_format, b.created_at.isoformat())

    def test_dict_updated_at_format(self):
        """Confirms 'updated_at' is string format"""
        b = BaseModel()
        b1 = b.to_dict()
        _format = b1['updated_at']
        self.assertEqual(_format, b.updated_at.isoformat())

