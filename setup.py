#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='peafowl',
      version='0.4',
      description='A light weight server for reliable distributed message passing.',
      long_description="Peafowl is a powerful but simple messaging server that enables reliable distributed queuing with an absolutely minimal overhead. It speaks the MemCache protocol for maximum cross-platform compatibility. Any language that speaks MemCache can take advantage of Peafowl's queue facilities.",
      author='Timothee Peignier',
      author_email='tim@tryphon.org',
      url='http://code.google.com/p/peafowl/',
      license = 'MIT License',
      platforms = ["Unix",],
      keywords = "peafowl queue messaging distributed memcache starling",
      classifiers = [ "Development Status :: 4 - Beta",
                      "License :: OSI Approved :: MIT License",
                      "Operating System :: Unix",
                      "Programming Language :: Python" ],
      packages = ['peafowl'],
      scripts=['bin/peafowl'],
      test_suite='tests'
)
