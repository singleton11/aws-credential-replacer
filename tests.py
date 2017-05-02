#!/usr/bin/env python
import os
import sys
from unittest import TestCase

from credentials_replacer.replacer import render_with_credentials

if sys.version_info[0] == 3:
    from unittest.mock import patch
elif sys.version_info[0] == 2:
    from mock import patch


class TestReplacer(TestCase):
    """A test case for replacer"""

    def setUp(self):
        """Make test file

        Create file which has ``file_path`` path with content with jinja2 
        placeholders

        """
        self.file_path = 'tmp/test.json'

        template = '{"cred1": "{{ TEST_CRED1 }}", "cred2": "{{ TEST_CRED2 }}"}'

        os.makedirs('tmp')
        with open(self.file_path, 'w') as f:
            f.write(template)

    def tearDown(self):
        """Remove temporary created file"""
        os.unlink(self.file_path)
        os.rmdir('tmp')

    @patch('credentials_replacer.replacer.listSecrets', return_value=[
        {
            'name': 'TEST_CRED1',
        },
        {
            'name': 'TEST_CRED2',
        },
    ])
    @patch('credentials_replacer.replacer.getSecret',
           side_effect=['test_value1', 'test_value2'])
    def test_credentials_render(self, _1, _2):
        """Ensure that credentials obtained and template renders correctly"""
        self.assertEqual(render_with_credentials(self.file_path),
                         '{"cred1": "test_value1", "cred2": "test_value2"}')
