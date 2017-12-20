# py-selenium-browser

[![build](https://travis-ci.org/neetjn/py-selenium-browser.svg?branch=master)](https://travis-ci.org/neetjn/py-selenium-browser)
[![PyPI version](https://badge.fury.io/py/pysbr.svg)](https://badge.fury.io/py/pysbr)
[![codecov](https://codecov.io/gh/neetjn/py-selenium-browser/branch/master/graph/badge.svg)](https://codecov.io/gh/neetjn/py-selenium-browser)

Decorators for provisioning tests with selenium remote webdrivers.

For an all inclusive selenium framework check out [py-component-controller](https://github.com/neetjn/py-component-controller)!

## About

`py-selenium-browser` is a very simple project based off of [nose_parammeterzed](https://github.com/wolever/parameterized). This project provides very simple and easily configurable decorators to parameterize individual tests to run against multiple browser configurations against your stack.

### Usage

`py-selenium-browser` supports both Python 2.7 and 3.6 and can be installed with pip like so,

```python
pip install pysbr
```

Import `Decorators` and `Configure` from `pysbr` to get started,

```python
import os
from selenium import webdriver
from unittest import TestCase

from pysbr import Configure, Decorators


Configure.platforms(name='chrome', platforms=['WIN10'])
Configure.capabilities(name='edge', capabilities={
    'version': '5'
})
Configure.profile(name='safari', profile=None)
Configure.enable(name='firefox')
Configure.disable(name='opera')

COMMAND_EXECUTOR = os.environ.get('COMMAND_EXECUTOR')


class SampleTest(TestCase):

    @Decorators.browsers()
    def test_login(self, capabilities, profile):
        browser = webdriver.Remote(
            COMMAND_EXECUTOR, capabilities, profile)
        ...
        browser.stop_client()
        
    @Decorators.browser(name='chrome', platform='WIN10')
    def test_register(self, capabilities, profile):
        ...
        
    @Decorators.random_browser()
    def test_logout(self, capabilities, profile):
        ...
```

This project supports the Chrome, Firefox, Edge, Safari, and Opera browsers by default -- but other browsers can be defined like so,

```python
from pysbr.constants import BROWSERS

BROWSERS.ANDROID = BROWSERS.BROWSER(
    name, platforms, capabilities=None, profile=None)
BROWSERS.browsers.append(BROWSERS.ANDROID)
```

All browsers also disabled by default, so be sure to enable them prior to use with the decorators.

## Testing

All module related unit tests are in the `tests` subdirectory.

To setup your environment run `make setup`. To run the test suite, use `make test`.

Requirements:
* Python 2.7, 3.6 (with pip)

### Contributors

* **John Nolette** (john@neetgroup.net)

Contributing guidelines are as follows,

* Any new features added must also be unit tested in the `tests` subdirectory.
* Branches for bugs and features should be structued like so, `issue-x-username`.
* Include your name and email in the contributors list.

---
Copyright (c) 2017 John Nolette Licensed under the MIT license.
