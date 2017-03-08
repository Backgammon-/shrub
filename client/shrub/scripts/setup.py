"""Install script for Shrub client."""

from setuptools import setup, find_packages

setup(
    name='shrub',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        shrub=shrub.scripts.cli:cli
    ''',
)

