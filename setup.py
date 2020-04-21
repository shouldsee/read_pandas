#!/usr/bin/env python
#from setuptools import setup
### dummy touch
from distutils.core import setup
import os,glob,sys
assert sys.version_info >= (3,5),('Requires python>=3.5, found python==%s'%('.'.join([str(x) for x in sys.version_info[:3]])))

config = dict(
	name='read_pandas',
	version = '0.0.1',
	packages=['.'],
	license='MIT',
	author='Feng Geng',
	author_email='feng.geng.14@ucl.ac.uk',
	long_description ='''
	presets for reading pandas dataframe.
	'''
	# long_description=open('README.md').read(),
	classifiers = [
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.7',
	],
	install_requires=open("requirements.txt","r").read().strip().splitlines(),
)
setup(**config)

