#!/usr/bin/env python

from distutils.core import setup

required = [
    'credstash',
    'jinja2',
    'click'
]

setup(
    name='aws_credentials_replacer',
    version='0.1.2',
    description='AWS credentials replacer',
    author='Anton Prokhorov',
    author_email='betrayer11@gmail.com',
    url='https://github.com/singleton11/aws-credential-replacer',
    packages=['credentials_replacer'],
    requires=required,
    install_requires=required,
)
