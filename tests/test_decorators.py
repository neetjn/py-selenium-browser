import random
from unittest import TestCase
from pysbr import Decorators
from pysbr.constants import BROWSERS


for b in BROWSERS.browsers:
    b.enabled = True

class TestConfigure(TestCase):

    def setUp(self):
        self.random_browser = False
        self.browser = False
        self.browsers = 0

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
        self.assertEqual(capabilities['browserName'], BROWSERS.CHROME.name)
        self.assertEqual(profile, BROWSERS.CHROME.profile)

    @Decorators.browser(name=BROWSERS.OPERA.name, iterations=5)
    def test_browser_iter(self, capabilities, profile):
        """test decorator single browser construction with iterations"""
        self.assertEqual(capabilities['browserName'], BROWSERS.OPERA.name)
        self.assertEqual(profile, BROWSERS.OPERA.profile)

    @Decorators.browsers()
    def test_browsers(self, capabilities, profile):
        """test decorator all browsers construction"""
        browser = BROWSERS.find(name=capabilities['browserName'])
        self.assertEqual(browser.profile, profile)
