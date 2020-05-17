import unittest

from flask import current_app
from kbpc.db.flaskalchemy.database import create
from app.api.parent import dao


class TestBaseDAO(unittest.TestCase):

    def setUp(self):
        self.dao = dao.BaseDAO()

    def test_create(self):
        instance = self.dao.create({'test': 'test'})
        print(instance)
