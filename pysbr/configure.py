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
        assert all(platform in [name for name, _ in iteritems(item) \
                    for item in PLATFORMS.platforms] for platform in platforms), \
                    'An error occurred while updating; platform does not exist'
        BROWSERS.find(name, enabled=False).platforms = platforms

    @staticmethod
    def enable(name):
        """
        :Description: Enable an available browser.
        :param name: Name of browser to target.
        :type name: string
        """
        BROWSERS.find(name, enabled=False).enabled = True

    @staticmethod
    def disable(name):
        """
        :Description: Disable an available browser.
        :param name: Name of browser to target.
        :type name: string
        """
        BROWSERS.find(name, enabled=False).enabled = False
