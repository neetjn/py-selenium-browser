import random

from pysbr import Decorators
from pysbr.constants import BROWSERS
from unittest import TestCase


for browser in BROWSERS.browsers:
    browser.enabled = True


class TestConfigure(TestCase):

    def setUp(self):
        self.random_browser = False
        self.browser = False
        self.browsers = 0

    @Decorators.random_browser()
    def test_random(self, capabilities, profile):
        """test configure updating platform information"""
        self.assertFalse(self.random_browser)
        self.random_browser = True  # make sure we only have 1 iteration
        self.assertIsInstance(capabilities, dict)
        self.assertIsNone(profile)
