# setup.py
from setuptools import setup

setup(
    name='enrollment',
    version='0.1',
    py_modules=['enrollment'],
    install_requires=[
        'click',
        'sqlalchemy',
    ],
    entry_points='''
        [console_scripts]
        enrollment=enrollment.cli:cli
    ''',
)