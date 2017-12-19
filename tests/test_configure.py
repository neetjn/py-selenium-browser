import random

from pysbr import Configure
from pysbr.constants import BROWSERS, PLATFORMS
from unittest import TestCase


class TestConfigure(TestCase):

    def test_update(self):
        """test configure updating platform information"""
        browser = random.choice(BROWSERS.browsers)
        platforms = [PLATFORMS.WINDOWS.get('legacy')]
        Configure.update(browser.name, platforms)
        self.assertEqual(browser.platforms, platforms)

    def test_enable_disable(self):
        """test configure enabling and disabling browsers"""
        browser = random.choice(BROWSERS.browsers)
        Configure.enable(browser.name)
        self.assertTrue(browser.enabled)
        Configure.disable(browser.name)
        self.assertFalse(browser.enabled)
