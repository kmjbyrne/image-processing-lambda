__author__ = 'Keith Byrne'

import unittest

from app import create_app
from app.web.mail_service import send_email


class TestMailIntegration(unittest.TestCase):

    def setUp(self):
        self.app = create_app('TEST')
        self.test_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_mail_route(self):
        with self.app.app_context():
            html = "TEST"
            send_email(["keithmbyrne@gmail.com"], "TEST", html, "keithmbyrne@gmail.com")


