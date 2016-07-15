import sys
import os
from setuptools import setup
from pastdoc import __version__


if sys.version_info[0] < 3:
    sys.exit("You should install PASTDoc with Python 3")


description = """
PASTDoc. Python Doc Generator, working with AST.
"""


# get requirements list
current = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current, 'requirements', 'main.txt')) as fp:
    requirements = fp.read().splitlines()


setup(
    name="pastdoc",
    url="https://github.com/prokaktus/pastdoc",
    version=__version__,
    description=description.strip(),
    author="Filipenko Maxim",
    author_email="mfilipenko@yandex.ru",
    packages=[
        'pastdoc'
    ],
    install_requires=[
        requirements
    ],
    entry_points={
        'console_scripts': ['pastdoc=pastdoc.cli:main']
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
