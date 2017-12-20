import random
from unittest import TestCase
from pysbr import Configure
from pysbr.constants import BROWSERS, PLATFORMS
from selenium import webdriver
from six import iteritems


for b in BROWSERS.browsers:
    b.enabled = True

class TestConfigure(TestCase):

    def test_capabilities(self):
        """test configure updating platform information"""
        browser = random.choice(BROWSERS.browsers)
        capabilities = {
            'version': '62'
        }
        Configure.capabilities(browser.name, capabilities)
        for label, capability in iteritems(capabilities):
            self.assertEqual(browser.capabilities.get(label), capability)

    def test_platforms(self):
        """test configure updating platform information"""
        browser = random.choice(BROWSERS.browsers)
        platforms = [PLATFORMS.WINDOWS.get('legacy')]
        Configure.platforms(browser.name, platforms)
        self.assertEqual(browser.platforms, platforms)

    def test_profile(self):
        """test configuring profile information"""
        browser = BROWSERS.find(BROWSERS.FIREFOX.name)
        profile = webdriver.FirefoxProfile()
        profile.set_preference('security.enterprise_roots.enabled', True)
        Configure.profile(browser.name, profile)
        for attr, value in iteritems(profile.__dict__):
            self.assertEqual(getattr(browser.profile, attr), value)
        Configure.profile(browser.name, None)
        self.assertIsNone(browser.profile)

    def test_enable_disable(self):
        """test configure enabling and disabling browsers"""
        browser = random.choice(BROWSERS.browsers)
        Configure.disable(browser.name)
        self.assertFalse(browser.enabled)
        Configure.enable(browser.name)
        self.assertTrue(browser.enabled)
