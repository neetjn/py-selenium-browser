from setuptools import setup, find_packages


setup(
    name='pysbr',
    description='Decorators for provisioning tests with remote webdrivers.',
    version='0.0.1',
    url='https://neetjn.github.io/py-selenium-browser',
    author='John Nolette',
    author_email='john@neetgroup.net',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'nose',
        'nose_parameterized',
        'six'
    ],
    packages=['pysbr']
)
