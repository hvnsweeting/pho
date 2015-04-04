#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pho

requisites = []

setup(
    name='mpho',
    version=pho.__version__,
    description='PytHon utility for Organizing tasks',
    scripts=['scripts/pho'],
    long_description=open('README.rst').read(),
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/pho',
    packages=['pho'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
