import os
from unittest import TestCase
from unittest.mock import patch

from replacer import render_with_credentials


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

    @patch('replacer.listSecrets', return_value=[
        {
            'name': 'TEST_CRED1',
        },
        {
            'name': 'TEST_CRED2',
        },
    ])
    @patch('replacer.getSecret', side_effect=['test_value1', 'test_value2'])
    def test_credentials_render(self, _1, _2):
        """Ensure that credentials obtained and template renders correctly"""
        self.assertEqual(render_with_credentials(self.file_path),
                         '{"cred1": "test_value1", "cred2": "test_value2"}')
