from io import open

from setuptools import find_packages, setup

with open('userpath/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = ['click']

setup(
    name='userpath',
    version=version,
    description='Cross-platform tool for adding locations to the user PATH',
    long_description=readme,
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/userpath',
    license='MIT',

    keywords=[
        'user path',
        'path',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    packages=['userpath'],
    entry_points={
        'console_scripts': [
            'userpath = userpath.cli:userpath',
        ],
    },
)
