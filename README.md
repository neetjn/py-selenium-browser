# py-selenium-browser

[![build](https://travis-ci.org/neetjn/pysbr.svg?branch=master)](https://travis-ci.org/neetjn/pysbr)
[![PyPI version](https://badge.fury.io/py/pysbr.svg)](https://badge.fury.io/py/pysbr)
[![Code Health](https://landscape.io/github/neetjn/pysbr/master/landscape.svg?style=flat)](https://landscape.io/github/neetjn/pysbr/master)
[![codecov](https://codecov.io/gh/neetjn/pysbr/branch/master/graph/badge.svg)](https://codecov.io/gh/neetjn/pysrb)

Decorators for provisioning tests with selenium remote webdrivers.

## About

`py-selenium-browser` is a very simple project based off of [nose_parammeterzed](https://github.com/wolever/parameterized). This project provides very simple and easily configurable decorators to parameterize individual tests to run against multiple browser configurations against your stack.

### Usage

`py-component-controller` supports both Python 2.7 and 3.6 and can be installed with pip like so,

```python
pip install pysbr
```

Import `Decorators` and `Configure` from `pysb` to get started,

```python
import os
from selenium import webdriver
from unittest import TestCase

from pysbr import Configure, Decorators
from pysbr.constants import BROWSERS, PLATFORMS


Configure.update(name=BROWSERS.CHROME.name, platforms=[
    PLATFORMS.WINDOWS.get('default'f)
])
Configure.enable(name=BROWSERS.FIREFOX.name)
Configure.disable(name=BROWSERS.OPERA.name)

COMMAND_EXECUTOR = os.environ.get('COMMAND_EXECUTOR')


class SampleTest(TestCase):

    def bootstrap(capabilities, profile):
        return webdriver.Remote(
            COMMAND_EXECUTOR, capabilities, profile)

    @Decorators.browsers()
    def test_login(self, capabilities, profile):
        browser = self.bootstrap(capabilities, profile)
        ...
        browser.stop_client()
```

## Testing

All module related unit tests are in the `tests` subdirectory. To setup your environment run `make setup`. To run the test suite, use `make test`.

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
