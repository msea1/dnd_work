import svgwrite
from svgwrite.path import Path

# COLORS
TEXT_PRIMARY = "green"
TEXT_SECONDARY = "green"

BG_PRIMARY = "green"
BG_SECONDARY = "green"

LABEL_PRIMARY = "green"
LABEL_SECONDARY = "green"

# FONTS


# DIMENSIONS
DPI = 96
PAGE_WIDTH_PX = 816
PAGE_HEIGHT_PX = 1056
BUMBER_PX = 20  # printing margin


def invert_y_axis(inkscape_value):
    return PAGE_HEIGHT_PX - inkscape_value


def convert_in_to_px(inch_value):
    return inch_value * DPI


def rounded_rectangle(drawing, x, y, width, height):
    return drawing.rect(insert=(x, y), size=(width, height), rx="20", ry="20",
                        stroke_width="1",
                        stroke="green",
                        fill="rgb(255,255,0)")


def create_path():
    return Path(
        d="m 53.962048,239.21297 c 0,1.56896 -1.053656,3.03781 -2.343637,3.23904 -14.608462,2.27415 -29.397008,2.27415 -44.0051933,0 -1.2899845,-0.20123 -2.3439149,-1.67008 -2.3439149,-3.23904 V 68.534573 c 0,-1.569301 1.0594713,-2.854041 2.3541653,-2.854712 H 51.608159 c 1.294695,6.71e-4 2.353889,1.285411 2.353889,2.854712 z",
        style="fill:none;fill-opacity:1;fill-rule:nonzero;stroke:#080808;stroke-width:0.38058412;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1")


svg_doc = svgwrite.Drawing(filename="test-svgwrite.svg", size=(PAGE_WIDTH_PX, PAGE_HEIGHT_PX))
svg_doc.add(rounded_rectangle(svg_doc, BUMBER_PX, BUMBER_PX, BUMBER_PX * 2, BUMBER_PX * 2))
svg_doc.add(create_path())
print(svg_doc.tostring())
svg_doc.save()
