#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import versioneer


versioneer.VCS = 'git'
versioneer.versionfile_source = 'passgen/_version.py'
versioneer.versionfile_build = 'passgen/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = 'passgen-'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

cmd_classes = versioneer.get_cmdclass()
cmd_classes['test'] = PyTest


setup(
    name="kinderstadt-passgen",
    version=versioneer.get_version(),
    cmdclass=cmd_classes,
    packages=find_packages(),
    install_requires=[
        'alembic==0.7.5.post2',
        'BaseHash==2.1.0',
        'CairoSVG==1.0.13',
        'click==4.0',
        'Flask-Celery-Helper==1.1.0',
        'flask-marshmallow==0.6.0',
        'Flask-Migrate==1.4.0',
        'Flask-SQLAlchemy==2.0',
        'Flask-WTF==0.11',
        'Flask==0.10.1',
        'marshmallow-sqlalchemy==0.2.0',
        'marshmallow==2.0.0b2',
        'path.py==7.3',
        'pgcli==0.16.3',
        'pyPdf==1.13',
        'PyPDF2==1.24',
        'python-stdnum==1.1',
        'uWSGI==2.0.10',
    ],
    extras_require={
        'devel': [
            'ansible',
            'autopep8',
            'flake8',
            'ipython',
        ]
    },
    tests_require=[
        'pytest',
        'testing.postgresql'],
    entry_points={
        'console_scripts': [
            'passgen=passgen.cli:main'],
    },
)
