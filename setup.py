# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='userpath',
    version='1.9.1',
    description='Cross-platform tool for adding locations to the user PATH',
    author_email='Ofek Lev <oss@ofek.dev>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'userpath = userpath.cli:userpath',
        ],
    },
    packages=[
        'userpath',
    ],
)
