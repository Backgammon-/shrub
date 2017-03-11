"""Install script for Shrub server."""

from setuptools import setup, find_packages

setup(
    name='shrubbery',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pysqlcipher3'
        'requests'
    ],
    entry_points='''
        [console_scripts]
        shrubbery=shrubbery.scripts.cli:cli
    ''',
)

