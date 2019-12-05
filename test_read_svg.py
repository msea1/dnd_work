import unittest

from svg_sheets import read_svg


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_fx(self):
        paths, attr_dict = read_svg.svg2paths('/home/mcarruth/Code/personal/svg_sheets/bear.svg')
        resp = read_svg.break_up_path_commands('aaaa.png')
