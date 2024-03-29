#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from . import ez_setup
    from setuptools import setup

parent_directory = os.path.abspath(os.path.dirname(__file__))

metafiles = {
    'README.md': None,
    'CHANGES.md': None,
    'LICENSE.md': None,
    'CLASSIFIERS.txt': None
}

for filename in metafiles:
    try:
        current_file = open(os.path.join(parent_directory, filename))
        metafiles[filename] = current_file.read()
        current_file.close()
    except IOError:
        pass

dependencies = []

metadata = {
    'name': 'cliTunes',
    'version': '0.0.3',

    'author': 'Brandon R. Stoner',
    'author_email': 'monokrome@monokro.me',

    'description': 'Python wrapper for tmux',
    'classifiers': metafiles['CLASSIFIERS.txt'],
    'long_description': metafiles['README.md'] + '\n\n' + metafiles['CHANGES.md'],

    'packages': [],
    'scripts': ['bin/clitunes'],

    'install_requires': dependencies
}

setup(**metadata)

