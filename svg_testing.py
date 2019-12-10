from math import ceil
from os.path import join

from svgpathtools import disvg, svg2paths, Arc, Line, QuadraticBezier, CubicBezier, Path as spt_Path
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing
from svgwrite.path import Path

from svg_sheets.common import move_cursor_to, move_to_calcs, scaler_calcs


# TODO editor to chop up existing svg
# TODO, colors
# TODO, create stable samples of various shapes
