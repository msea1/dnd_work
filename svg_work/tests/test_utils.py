import unittest

from svg_sheets.svg_work import utils


class UtilsTests(unittest.TestCase):
    def test_scale(self):
        self.assertEqual(0.9, utils.determine_scale(-10, 100))
        self.assertEqual(1.0, utils.determine_scale(0, 100))
        self.assertEqual(1.1, utils.determine_scale(10, 100))
