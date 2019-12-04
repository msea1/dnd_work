import unittest

from svg_sheets import read_svg


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_fails_on_non_svg(self):
        with self.assertRaises(ValueError):
            read_svg.read_file('aaaa.png')
