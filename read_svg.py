from xml.dom import minidom

from svgwrite import Drawing
from svgwrite.path import Path


# be able to move to top-left
# be able to bound size
# be able to slace/transform
# editor to chop up svg

def test(filepath):
    path_obj = read_from_file(filepath)
    svg_doc = Drawing(filename="testing.svg", size=(5000, 5000))
    svg_doc.add(path_obj)
    svg_doc.save()


def convert_absolutes_in_path_to_relative(path_str):
    pass


def move_to_ul_corner():
    pass


def read_from_file(filepath):
    if not filepath.endswith('.svg'):
        raise ValueError(f'Need to pass an svg file, you passed {filepath}')

    doc = minidom.parse(filepath)  # parseString also exists
    path_strings = [
        path.getAttribute('d') for path in doc.getElementsByTagName('path')
    ]
    doc.unlink()
    path_obj = Path()
    # [f"M {upper_left_pixel_horizontal}, {upper_left_pixel_vertical}"]
    path_obj.push(path_strings[0])
    return path_obj


test('/home/mcarruth/Code/personal/svg_sheets/bear.svg')
