import os 
from setuptools import setup, find_packages


__version__ = '1.0.1'
requirements = open('requirements.txt').readlines()

setup(
        name = 'chun_img_browser',
        version=__version__,
        author='chi-chun',
        author_email='justin11223350@gmai.com',
        url='',
        description='Doing some data process',
        packages= find_packages(exclude=["test","util"]),
        python_rquires = '>=3.8.0', 
        install_requires = requirements
        )
