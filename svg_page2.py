from xml.dom import minidom

import svgwrite
from svgwrite import Drawing
from svgwrite.path import Path

# COLORS
from svg_sheets.shapes.viper3 import viper_3

TEXT_PRIMARY = "green"
TEXT_SECONDARY = "green"

BG_PRIMARY = "green"
BG_SECONDARY = "green"

LABEL_PRIMARY = "green"
LABEL_SECONDARY = "green"


# FONTS

svg_doc = svgwrite.Drawing(filename="viper_1.svg", size=(500, 800))

# svg_doc.add(shapes.test_curve())
# svg_doc.add(viper_2(0, 0, relative_size_x=1, relative_size_y=0.7))
# svg_doc.add(viper_2(0, 0, end_x=150, end_y=200))

# testing shapes
svg_doc.add(viper_3(0, 0, relative_size_x=1, relative_size_y=1))
# svg_doc.add(bounding_box(svg_doc, 104, 146, 81, 58))  # TODO replace with curve math at some point
# offset start = first x,y subtracted from shape

svg_doc.save()

# TODO: wrap everything in layers


def test_svgwrite(filepath):  # works but no bounding box ability
    path_obj = read_from_file(filepath)
    svg_doc = Drawing(filename="testing.svg", size=(5000, 5000))
    svg_doc.add(path_obj)
    svg_doc.save()


def read_from_file(filepath):
    if not filepath.endswith('.svg'):
        raise ValueError(f'Need to pass an svg file, you passed {filepath}')

    doc = minidom.parse(filepath)  # parseString also exists
    path_strings = [
        path.getAttribute('d') for path in doc.getElementsByTagName('path')
    ]
    doc.unlink()
    path_obj = Path()
    path_obj.push(path_strings[0])
    return path_obj

