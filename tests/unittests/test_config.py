__author__ = 'Keith Byrne'

import unittest
import re

from app import config

WATCHLIST_OF_FLAGGED_ENTRIES = [
    'password',
    'PASSWORD',
]


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.development = config.DevelopmentConfig
        self.testing = config.TestingConfig
        self.release = config.ReleaseConfig

    def test_no_credentials_visible(self):
        # A helper test to ensure no sensitive data is available in Config objects
        for environment_manager in [self.development, self.testing, self.release]:
            for config_variable in environment_manager.__dict__.items():
                expression = '(.*key.*)|(.*secret.*)'
                self.assertIsNone(
                    re.search(expression, config_variable[0].lower()),
                    msg='Check {0} config for sensitive variable mappings such as passwords, secrets, keys etc...'
                        .format(str(environment_manager))
                )

    def test_independent_debug_testing_flags(self):
        self.assertTrue(self.development.__dict__['DEBUG'])
        self.assertTrue(self.testing.__dict__['DEBUG'])
        self.assertTrue(self.testing.__dict__['TESTING'])

    def test_release_config(self):
        try:
            self.assertFalse(self.release.__dict__['DEBUG'])
            self.assertFalse(self.release.__dict__['TESTING'])
        except KeyError:
            with self.assertRaises(KeyError):
                self.assertFalse(self.release.__dict__['DEBUG'])
                self.assertFalse(self.release.__dict__['TESTING'])
