#!/usr/bin/env python

from distutils.core import setup

setup(
    name='aws_credentials_replacer',
    version='0.1',
    description='AWS credentials replacer',
    author='Anton Prokhorov',
    author_email='betrayer11@gmail.com',
    url='https://github.com/singleton11/aws-credential-replacer',
    packages=['credentials_replacer'],
    requires=['credstash', 'jinja2', 'click']
)
