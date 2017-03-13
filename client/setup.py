"""Install script for Shrub client."""

from setuptools import setup, find_packages

setup(
    name='shrub',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Paramiko'
    ],
    entry_points='''
        [console_scripts]
        shrub=shrub.scripts.shrub_cmd:invoke_cli
    ''',
)

