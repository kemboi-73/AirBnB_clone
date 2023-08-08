#!/usr/bin/python3
"""This module contains unittests for base class"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests usage cases for base class"""
    def test_base_attributes_instantiation(self):
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
