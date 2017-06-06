#!/usr/bin/env python
'''
This is example for package
'''

from setuptools import setup, find_packages
import vodka

PKG=vodka

setup(
	name="vodka",
	version=vodka.__version__,
	author=vodka.__author__,
	url=vodka.__url__,
	description=vodka.__description__,
	packages = find_packages(),
)

