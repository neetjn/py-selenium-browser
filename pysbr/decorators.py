import random
from nose_parameterized import parameterized

from pysb.constants import BROWSERS, PLATFORMS


class Decorators(parameterized):
    """
    :Description: All-in-one decorators for provisioning remote selenium webdrivers.
    :Example: https://github.com/neetjn/nose-parameterized-wrapper-example
    """

    @classmethod
    def browsers(cls, platform=None, development=False):
        """
        :Description: Runs test against all browser combinatorics.
        :param platform: Platform specification for target browsers.
        :type platform: basestring
        :param development: If specified, will target first available browser on hub.
        :type development: bool
        """

        if development:

            # We patch for firefox, assuming Firefox is the only edge case
            # where a profile is necessary and this profile does not effect
            # any other webdriver

            return super(Decorators, cls).expand([({}, None)])

        else:

            combinations = []

            if platform:
                platforms = [getattr(PLATFORMS, name) for name in PLATFORMS.meta['available']]
                assert next(items for items in platforms if platform in items.itervalues())

            for browser in BROWSERS.meta['available']:
                browser = getattr(BROWSERS, browser)

                if platform and platform not in browser.platforms:
                    # filter out platforms
                    continue

                if platform:
                    capabilities = dict.copy(browser.capabilities)
                    capabilities.setdefault('platform', platform)
                    combinations.append([capabilities, None])
                else:
                    for _platform in browser.platforms:
                        capabilities = dict.copy(browser.capabilities)
                        capabilities.setdefault('platform', _platform)
                        combinations.append([capabilities, None])

            return super(Decorators, cls).expand([combination for combination in combinations])

    @classmethod
    def browser(cls, name, iterations=1, platform=None, capabilities=None, profile=None):
        """
        :Description: Runs test against given browser specification.
        :Warning: If a platform is not specified, selenium hub will decide first available.
        :param iterations: Number of times to run test.
        :type iterations: Integer
        :param platform: Platform to target.
        :type platform: basestring
        :param capabilities: Capabilities of remote webdriver.
        :type capabilities: dict
        :param profile: Profile for remote webdriver.
        :type profile: FirefoxProfile, ChromeOptions, ...
        """

        browser = next(browser for browser in BROWSERS.meta['available'] \
            if getattr(BROWSERS, browser).name == name)
        browser = getattr(BROWSERS, browser)
        capabilities = capabilities or {}

        if platform:
            assert platform in browser.platforms
            # update platform in capabilities if not specified
            capabilities.setdefault('platform', platform)

        _capabilities = dict.copy(browser.capabilities)
        _capabilities.update(capabilities)

        return super(Decorators, cls).expand([(_capabilities, None)]*iterations)

    @classmethod
    def random_browser(cls):
        """
        :Description: Runs test against random browser on a random available platform.
        """

        browsers = []

        for browser in BROWSERS.meta['available']:
            browser = getattr(BROWSERS, browser)
            browsers.append(browser)

        browser = random.choice(browsers)

        capabilities = dict.copy(browser.capabilities)
        capabilities.setdefault('platform', random.choice(browser.platforms))

        return super(Decorators, cls).expand([(capabilities, None)])
