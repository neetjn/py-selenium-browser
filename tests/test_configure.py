import random

from pysbr import Configure
from pysbr.constants import BROWSERS
from unittest import TestCase


class TestConfigure(TestCase):

    def test_update(self):
        """test configure updating platform information"""
        browser = random.choice(BROWSERS.browsers)
        Configure.update(browser.name, {

        })

    def test_enable_disable(self):
        """test configure enabling and disabling browsers"""
        browser = random.choice(BROWSERS.browsers)
        Configure.enable(browser.name)
        self.assertTrue(browser.enabled)
        Configure.disable(browser.name)
        self.assertFalse(browser.enabled)
