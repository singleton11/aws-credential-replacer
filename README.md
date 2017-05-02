# AWS Credentials replacer

[![PyPI version](https://badge.fury.io/py/aws_credentials_replacer.svg)](https://badge.fury.io/py/aws_credentials_replacer)
[![Build Status](https://travis-ci.org/singleton11/aws-credential-replacer.svg?branch=master)](https://travis-ci.org/singleton11/aws-credential-replacer)
[![Coverage Status](https://coveralls.io/repos/github/singleton11/aws-credential-replacer/badge.svg?branch=master)](https://coveralls.io/github/singleton11/aws-credential-replacer?branch=master)
[![Requirements Status](https://requires.io/github/singleton11/aws-credential-replacer/requirements.svg?branch=master)](https://requires.io/github/singleton11/aws-credential-replacer/requirements/?branch=master)

A CLI tool which obtains data from [credstash](https://github.com/fugue/credstash) and renders it with 
[Jinja2](http://jinja.pocoo.org/)

## Requirements

There is `credstash` have to be configured by 
[this](https://github.com/fugue/credstash/blob/master/README.md#quick-installation) manual.

## Installation
```
pip install aws_credential_replacer
```

## Usage

Imagine, you have a file with following content:

```json
{
  "hello": "{{ TEST_CRED }}",
  "world": "{{ TEST_CRED1 }}"
}
```

And output of `credstash list` is:

```bash
TEST_CRED  -- version 0000000000000000000
TEST_CRED1 -- version 0000000000000000000
```

To replace data in json to actual credentials data you have to type `credentials_replacer creds.json`. You
will obtain following output:
```json
{
  "hello": "test",
  "world": "test1"
}
```
where `test` and `test1` is actual data values of `TEST_CRED` and `TEST_CRED1` accordingly.

PS: You also can use any jinja2 syntax you want

Happy aws project building :smile: