from svg_sheets.common import create_paths

from svgpathtools import svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing

from svg_sheets.common import create_paths

DPI = 96
PAGE_WIDTH_PX = 816
PAGE_HEIGHT_PX = 1056
BUMPER_PX = 20  # printing margin


class Group:
    def __init__(self, name, svg_doc):
        self.ref_id = name
        self.doc = svg_doc
        self.group = svg_doc.g()
        self.position = [0, 0]
        self.size = [0, 0]

    def adjust_in_doc(self):
        self.doc.elements.remove(self.group)
        self.doc.add(self.group)
        self.doc.save(pretty=True)

    def move(self, dx=0, dy=0):
        # TODO translations and scales keep stacking, would be nive to simplyify them
        self.position[0] += dx
        self.position[1] += dy
        self.group.translate(dx, dy)
        self.adjust_in_doc()

    def scale(self, sx=1, sy=1):
        self.size[0] *= abs(sx)
        self.size[1] *= abs(sy)
        if sx < 0:
            self.position[0] -= self.size[0]
        if sy < 0:
            self.position[1] -= self.size[1]  # TODO check these
        self.group.scale(sx, sy)
        self.adjust_in_doc()

    def mirror_x(self):
        self.scale(sx=-1)
        self.move(dx=-self.size[0])
        self.adjust_in_doc()

    def matrix(self):
        cx = self.position[0]
        cy = self.position[1]
        # TODO, related to above stacking and such, matrix needs to be simplified
        self.group.matrix(-1, 0, 0, 1, cx - -1 * cx, cy - 1 * cy)
        self.move(dx=-self.size[0])
        self.adjust_in_doc()


class Build:
    def __init__(self):
        self.svg_doc = None
        self.groups = {}

    def create_portrait_doc(self, filename='testing.svg'):
        svg_doc = Drawing(filename=filename, size=(f'{PAGE_WIDTH_PX}px', f'{PAGE_HEIGHT_PX}px'))
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
        dx = x_max - x_min
        dy = y_max - y_min
        shape.size = [dx, dy]
        paths = create_paths(orig_paths, fill='none')
        for p in paths:
            shape.group.add(p)
        self.svg_doc.add(shape.group)
        self.svg_doc.save(pretty=True)
        return shape


b = Build()
b.create_portrait_doc()
left_banner = b.add_shape('./shapes/containers/header.svg', 'left_name_banner')
left_banner.move(20, 20)
right_banner = b.add_shape('./shapes/containers/header.svg', 'right_name_banner')
right_banner.move(20, 20)
right_banner.mirror_x()
right_banner.move(-1 * left_banner.size[0])
right_banner.mirror_x()
left_banner.mirror_x()
# right_banner.matrix()


# FIXME, test cases
# mirror, move, mirror
# move, matrix
# move, mirror, move <-- flipping of signs, latter move has to be 'negative'
# slowness to render
