__author__ = 'Keith Byrne'

import unittest

from app import create_app
from app.database import create


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('TEST')

    def test_create(self):
        with self.app.app_context():
            create()

    def test_persist(self):
        pass