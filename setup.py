#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#setup.py
#Dave Landay
#LAST UPDATED: 01-09-2020

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import sys

class NPMInstall(build_py):
    def run(self):
        self.run_command('npm install --prefix ./app/site/static')
        build_py.run(self)

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(version='1.0.0',
      name='',
      description='',
      author='',
      author_email='',
      packages=find_packages(),
      install_requires=required, 
      cmdclass={'npm_install': NPMInstall},
      test_suite='tests')
