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

        self.previous_iter = 0
        self.current_iter = 0

    @Decorators.random_browser()
    def test_random(self, capabilities, profile):
        """test decorator random browser construction"""
        self.assertFalse(self.random_browser)
        self.random_browser = True  # make sure we only have 1 iteration
        self.assertIsInstance(capabilities, dict)
        self.assertIsNone(profile)

    @Decorators.browser(name=BROWSERS.CHROME.name)
    def test_browser(self, capabilities, profile):
        """test decorator single browser construction"""
        # self.assertEqual(capabilities[])

    @Decorators.browser(name=BROWSERS.CHROME.name, iterations=5)
    def test_browser_iter(self, capabilities, profile):
        """test decorator single browser construction with iterations"""
        self.assertIsInstance(capabilities, dict)
        self.assertIsNone(profile)


    @Decorators.browser(name=BROWSERS.CHROME.name)
    def test_browsers(self, capabilities, profile):
        """test decorator all browsers construction"""
        pass
