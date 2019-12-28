from svgpathtools import svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing

from svg_sheets.svgs.common import create_paths
from svg_sheets.svgs.properties import Dimension
from svg_sheets.svgs.svg_group import Group

DPI = 96
PAGE_WIDTH_PX = 816
PAGE_HEIGHT_PX = 1056
BUMPER_PX = 20  # printing margin


class Builder:
    def __init__(self):
        self.svg_doc = None
        self.groups = {}

    def create_portrait_doc(self, doc_width=PAGE_WIDTH_PX, doc_height=PAGE_HEIGHT_PX, filename='testing.svg'):
        svg_doc = Drawing(filename=filename, size=(f'{doc_width}px', f'{doc_height}px'), profile='tiny')
        svg_doc.save(pretty=True)
        self.svg_doc = svg_doc

    def create_group(self, name):
        group = Group(name, self.svg_doc)
        self.groups[name] = group
        return group

    def add_shape(self, filepath, name='shape_name'):
        shape = self.create_group(name)
        orig_paths, _ = svg2paths(filepath)
        x_min, x_max, y_min, y_max = big_bounding_box(orig_paths)
        shape.size = Dimension(width=x_max - x_min, height=y_max - y_min)
        paths = create_paths(orig_paths, shape.size, fill='none')
        for p in paths:
            shape.group.add(p)
        self.svg_doc.add(shape.group)
        self.svg_doc.save(pretty=True)
        return shape


b = Builder()
b.create_portrait_doc(doc_width=500, doc_height=500)
# left_banner = b.add_shape('./shapes/containers/banner.svg', 'left_name_banner')

right_banner = b.add_shape('./shapes/containers/header.svg', 'right_name_banner')
right_banner.stretch_to(100, 100)
# right_banner.move(250, 250)
# right_banner.flip(along_x=True)
# right_banner.stretch(stretch_right=150)  # scale(1.39,1.0) translate(-150,0)  # FIXME


# FIXME, test cases
# mirror, move, mirror
# move, matrix
# move, mirror, move <-- flipping of signs, latter move has to be 'negative'
# slowness to render
