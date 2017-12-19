class PLATFORMS:

    WINDOWS = {'default': 'WIN10', 'legacy': 'WINDOWS'}
    MAC = {'default': 'MAC'}

    meta = {'available': ('WINDOWS', 'MAC')}


class BROWSERS:

    class BROWSER(object):

        def __init__(self, name, platforms, capabilities=None, profile=None):
            """
            :Description: Base definition for browsers.
            :param name: Name of browser, will be used in capabilities.
            :type name: basestring
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

    meta = {'available': ('CHROME', 'FIREFOX', 'EDGE', 'SAFARI', 'OPERA')}