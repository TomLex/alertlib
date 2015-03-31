from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
    
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='alertlib',
    version='0.1.0',
    description='library for sending alerts for various platforms',
    url='',
    author='Tomas Varga',
    author_email='tomi.varga727@gmail.com',
    license='MIT',
    keywords='alert slack pagerduty',
    packages=find_packages(),
    install_requires=requirements
)