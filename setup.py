#!/usr/bin/env python
from setuptools import setup, find_packages
import codecs
import os

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'txlib', 'version.txt'),
    mode='rb',
    encoding='utf8',
) as _version_file:
    __version__ = _version_file.read().strip()

setup(
    version=__version__,

    name="txlib",
    author="Indifex Ltd.",
    author_email="info@indifex.com",

    description="A python library for Transifex",
    url="http://www.indifex.com",

    packages=find_packages(),
    install_requires=[
        "requests",
        "six"
    ],

    long_description=open('README.rst').read(),

    classifiers=[
        'Development Status :: 3 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=(
        'translation',
        'localization',
        'internationalization',
    ),
    license='LGPL3',
)
