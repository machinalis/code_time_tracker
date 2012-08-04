#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('README.rst') as readme:
    __doc__ = readme.read()

from distutils.core import setup

setup(
    name='code_time_tracker',
    version='0.1',
    description=u'A very simple decorator that tracks running time',
    long_description=__doc__,
    author = u'Javier Mansilla',
    author_email = 'jmansilla@machinalis.com',
    url='https://github.com/machinalis/code_time_tracker',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: ',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet ::',
      ]
)
