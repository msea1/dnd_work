from math import ceil
from os.path import join

from svgpathtools import disvg, svg2paths, Arc, Line, QuadraticBezier, CubicBezier, Path as spt_Path
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing
from svgwrite.path import Path

from svg_sheets.common import move_cursor_to, move_to_calcs, scaler_calcs, create_path

from math import ceil
from os.path import join

from svgpathtools import Arc, CubicBezier, Line, Path as spt_Path, QuadraticBezier, svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing

DPI = 96
PAGE_WIDTH_PX = 816
PAGE_HEIGHT_PX = 1056
BUMPER_PX = 20  # printing margin


class Build:
    def __init__(self):
        self.svg_doc = None
        self.groups = {}

    def create_portrait_doc(self, filename='testing.svg'):
        svg_doc = Drawing(filename=filename, size=(f'{PAGE_WIDTH_PX}px', f'{PAGE_HEIGHT_PX}px'))
        svg_doc.save(pretty=True)
        self.svg_doc = svg_doc

    def create_paths(self, paths, stroke='#000000', width=1, fill='#000000'):
        path_objs = []
        for i, p in enumerate(paths):
            if isinstance(p, spt_Path):
                ps = p.d()
            elif type(p) in (Line, QuadraticBezier, CubicBezier, Arc):
                ps = spt_Path(p).d()
            else:  # assume this path, p, was input as a Path d-string
                ps = p
            path_objs.append(self.svg_doc.path(ps, stroke=stroke, stroke_width=f"{width}", fill=fill))
        return path_objs

    def move_group(self, group_name, dx=0, dy=0):
        svg_group, _ = self.groups[group_name]
        svg_group.translate(dx, dy)
        self.svg_doc.elements.remove(svg_group)
        self.svg_doc.add(svg_group)
        self.svg_doc.save(pretty=True)

    def mirror_group_x(self, group_name):
        svg_group, orig_paths = self.groups[group_name]
        svg_group.scale(-1, 1)
        x_min, x_max, _, _ = big_bounding_box(orig_paths)
        dx = x_max - x_min
        self.move_group(group_name, -1 * dx)

    def add_shape(self, filepath, name='name_banner'):
        shape = self.svg_doc.g()
        orig_paths, _ = svg2paths(filepath)
        paths = self.create_paths(orig_paths, fill='none')
        for p in paths:
            shape.add(p)
        self.groups[name] = (shape, orig_paths)
        self.svg_doc.add(shape)
        self.svg_doc.save(pretty=True)


b = Build()
b.create_portrait_doc()
b.add_shape('./shapes/containers/header.svg', 'left_name_banner')
b.add_shape('./shapes/containers/header.svg', 'right_name_banner')
b.mirror_group_x('right_name_banner')
b.move_group('right_name_banner')

