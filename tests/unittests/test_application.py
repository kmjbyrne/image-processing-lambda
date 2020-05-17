__author__ = 'Keith Byrne'

import unittest
import app


class TestApplicationInit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_app(self):
        # Test no params first, should return DEV app by default
        resp = app.create_app()
        self.assertEquals(resp.config['NAME'], 'Development Configuration')
        resp = app.create_app('DEV')
        self.assertEquals(resp.config['NAME'], 'Development Configuration')
        resp = app.create_app('TEST')
        self.assertEquals(resp.config['NAME'], 'Testing/Staging Configuration')
        resp = app.create_app('RELEASE')
        self.assertEquals(resp.config['NAME'], 'Release Configuration')