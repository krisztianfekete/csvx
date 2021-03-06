# coding: utf-8

from setuptools import setup

import sys
PY3 = sys.version_info.major == 3


setup(
    name='tabstream',
    version=':versiontools:tabstream:',
    description=(
        'Library to work with tabular streams with headers (CSV files)'),
    author='Krisztián Fekete',
    author_email='fekete.krisztyan@gmail.com',

    license='MIT License',

    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        ],

    packages=['tabstream'],

    setup_requires=['versiontools >= 1.8'],

    use_2to3=PY3,
    )
