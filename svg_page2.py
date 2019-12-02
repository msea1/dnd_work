import svgwrite

from svg_sheets import shapes
from svg_sheets.common import PAGE_HEIGHT_PX, PAGE_WIDTH_PX
from svg_sheets.shapes.viper import viper_1, viper_2
# COLORS
from svg_sheets.shapes.viper3 import viper_3

TEXT_PRIMARY = "green"
TEXT_SECONDARY = "green"

BG_PRIMARY = "green"
BG_SECONDARY = "green"

LABEL_PRIMARY = "green"
LABEL_SECONDARY = "green"


# FONTS

def bounding_box(svg, x, y, width, height):
    return svg.rect(insert=(x, y),
                    size=(width, height),
                    stroke_width="0.25",
                    stroke="green",
                    fill_opacity="0")


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
