#! /usr/bin/env python

import os
import re

from setuptools import setup


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(CURRENT_DIR, "README.rst")) as file:
    README = file.read()

with open(os.path.join(CURRENT_DIR, 'LICENSE')) as file:
    LICENSE = file.read()

with open(os.path.join(CURRENT_DIR, 'catzzz', '__init__.py')) as file:
    version_line = ''
    for line in file.readlines():
        if '__version__' in line:
            version_line = line
            break

    version_line = version_line.strip()

    match = re.match("__version__ = '(\d+\.\d+\.\d+)'", version_line)

    if not match:
        raise ValueError('No catzzz version info found.')

    version = match.group(1)


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python'
]


setup(name='catzzz',
      version=version,
      author='Paul Logston',
      author_email='code@logston.me',
      url='http://github.com/logston/catzzz',
      description='A package for getting more cats into your code.',
      long_description=README,
      license=LICENSE,
      classifiers=CLASSIFIERS,
      packages=['catzzz'],
      include_package_data=True,
      package_data={'': ['LICENSE', 'README.rst']})