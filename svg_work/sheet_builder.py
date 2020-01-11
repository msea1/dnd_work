from svgpathtools import svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing

from svg_sheets.svg_work.common_groups import add_dodec_banner, add_name_banners
from svg_sheets.svg_work.constants import PAGE_HEIGHT_PX, PAGE_WIDTH_PX
from svg_sheets.svg_work.svg_shape import Dimension, Shape
from svg_sheets.svg_work.utils import create_paths


class Builder:
    def __init__(self):
        self.svg_doc = None
        self.shapes = {}

    def create_portrait_doc(self, doc_width=PAGE_WIDTH_PX, doc_height=PAGE_HEIGHT_PX, filename='testing.svg'):
        svg_doc = Drawing(filename=filename, size=(f'{doc_width}px', f'{doc_height}px'), profile='tiny')
        svg_doc.save(pretty=True)
        self.svg_doc = svg_doc

    def add_shape(self, filepath, shape_name='shape_name'):
        shape = Shape(shape_name, self.svg_doc)
        self.shapes[shape_name] = shape
        orig_paths, _ = svg2paths(filepath)
        x_min, x_max, y_min, y_max = big_bounding_box(orig_paths)
        shape.size = Dimension(width=x_max - x_min, height=y_max - y_min)
        paths = create_paths(orig_paths, shape.size, fill='none', min_width=0.5)
        for p in paths:
            shape.group.add(p)
        self.svg_doc.add(shape.group)
        self.svg_doc.save(pretty=True)
        return shape


if __name__ == '__main__':
    b = Builder()
    b.create_portrait_doc()
    left_name, right_name = add_name_banners(b)
    initiative = add_dodec_banner(b, 'INITIATIVE', '+5')
    b.svg_doc.save(pretty=True)
