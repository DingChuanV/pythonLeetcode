"""


"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

import strategy.mymodule


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = "baidu.com"
        expected_url = '{}://{}.{}\n'.format([protocol, host, domain])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            strategy.mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)
