#!/usr/bin/env python

# Copyright (c) 2008 Adroll.com, Valentino Volonghi
# See LICENSE for details.

"""
Distutils installer for authorize.
"""

try:
    # Load setuptools, to build a specific source package
    import setuptools
except ImportError:
    pass

import sys, os
import authorize

install_requires = [] # ["lxml>=2.0.0"] still required to run tests though

setup = setuptools.setup
find_packages = setuptools.find_packages

description = """\
An API to connect to authorize.net(TM) payment services."""

long_description = file(os.path.join(os.path.dirname(__file__), 'README')).read()

setup(
    name = "authorize",
    author = "Valentino Volonghi",
    author_email = "valentino@adroll.com",
    url = "http://adroll.com/labs",
    description = description,
    long_description = long_description,
    license = "MIT License",
    version=authorize.__version__,
    install_requires=install_requires,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
    ],
    packages=find_packages(exclude=['ez_setup', 'doc'])
)
