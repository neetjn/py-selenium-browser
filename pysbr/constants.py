class PLATFORMS(object):  #pylint: disable=too-few-public-methods

    WINDOWS = {
        'default': 'WIN10',
        'legacy': 'WINDOWS'
    }

    MAC = {
        'default': 'MAC'
    }

    platforms = [WINDOWS, MAC]


class BROWSERS(object):  #pylint: disable=too-few-public-methods

    class BROWSER(object):  #pylint: disable=too-few-public-methods

        def __init__(self, name, platforms, capabilities=None, profile=None):
            """
            :Description: Base definition for browsers.
            :param name: Name of browser, will be used in capabilities.
            :type name: string
            :param platforms: Supported platforms.
            :type platforms: tuple, list
            :param capabilities: Capabilities for browser instances.
            :type capabilities: dict
            :param profile: Profile instance to be used by constructed browser.
            :type profile: FirefoxProfile, ChromeOptions, ...
            """
            self.name = name
            self.platforms = platforms
            self.capabilities = capabilities or {
                "browserName": name,
                "version": "",
                "javascriptEnabled": True
            }
            self.profile = profile
            self.enabled = False


    @staticmethod
    def find(name, enabled=True):
        """
        :Description: Find a browser by it's given name.
        :param name: Name of browser to search for.
        :type name: string
        :param enabled: Only find enabled browsers.
        :type enabled: bool
        :return: BROWSER
        """
        return next(browser for browser in BROWSERS.browsers \
            if browser.name == name and (browser.enabled if enabled else True))

    CHROME = BROWSER(
        name='chrome',
        platforms=[PLATFORMS.WINDOWS.get('default'), PLATFORMS.MAC.get('default')])

    FIREFOX = BROWSER(
        name='firefox',
        platforms=[PLATFORMS.WINDOWS.get('default'), PLATFORMS.MAC.get('default')])

    EDGE = BROWSER(
        name='edge',
        platforms=[PLATFORMS.WINDOWS.get('default')])

    SAFARI = BROWSER(
        name='safari',
        platforms=[PLATFORMS.MAC.get('default')])

    OPERA = BROWSER(
        name='opera',
        platforms=[PLATFORMS.WINDOWS.get('default'), PLATFORMS.MAC.get('default')])

    browsers = [CHROME, FIREFOX, EDGE, SAFARI, OPERA]
