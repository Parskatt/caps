# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()


setup(
    name='caps',
    version='0.0.1',
    description='CAPS',
    long_description=readme,
    author='Qianqian Wang',
    author_email='qw246@cornell.edu',
    url='https://github.com/qianqianwang68/caps',
    packages=['CAPS']
)
