from six import iteritems

from pysbr.constants import BROWSERS, PLATFORMS


class Configure(object):

    @staticmethod
    def capabilities(name, capabilities):
        """
        :Description: Update an available browser's capabilities.
        :Warning: A browser's platform is automatically constructed when a test is decorated.
        :param capabilities: Capabilities to patch.
        :type capabilities: dict
        """
        BROWSERS.find(name, enabled=False)\
            .capabilities\
            .update(capabilities)

    @staticmethod
    def platforms(name, platforms):
        """
        :Description: Update an available browser's attributes.
        :param name: Name of browser to target.
        :type name: string
        :param platforms: List of browser's available platforms.
        :type platforms: tuple, list
        """
        available = [platform for item in PLATFORMS.platforms for _, platform in iteritems(item)]
        assert all(platform in available for platform in platforms), \
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
