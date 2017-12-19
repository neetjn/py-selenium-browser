from six import iteritems

from pysbr.constants import BROWSERS, PLATFORMS


class Configure(object):

    @staticmethod
    def update(name, platforms):
        """
        :Description: Update an available browser's attributes.
        :param name: Name of browser to target.
        :type name: string
        :param platforms: List of browser's available platforms.
        :type platforms: tuple, list
        """
        for browser in BROWSERS.browsers:
            if browser.name == name:
                assert all(platform in [name for name, _ in iteritems(item) \
                    for item in PLATFORMS.platforms] for platform in platforms), \
                    'An error occurred while updating; platform does not exist'
                browser.platforms = platforms
                return True

        return False

    @staticmethod
    def enable(name):
        """
        :Description: Enable an available browser.
        :param name: Name of browser to target.
        :type name: string
        """
        for browser in BROWSERS.browsers:
            if browser.name == name:
                browser.enabled = True
                return True

        return False

    @staticmethod
    def disable(name):
        """
        :Description: Disable an available browser.
        :param name: Name of browser to target.
        :type name: string
        """
        for browser in BROWSERS.browsers:
            if browser.name == name:
                browser.enabled = False
                return True

        return False
