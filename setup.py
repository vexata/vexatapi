import os
from setuptools import (setup, find_packages)
import vexatapi

NAME = 'vexatapi'
DESCRIPTION = 'Python API for Vexata Storage Arrays'
VERSION = vexatapi.version
REQUIRES = [
    'requests',
]

pwd = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(pwd, 'README.rst'), 'r') as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    license='Apache 2.0',
    author='Sandeep Kasargod',
    author_email='python-dev@vexata.com',
    url='https://github.com/vexata/vexatapi',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=REQUIRES,
)
