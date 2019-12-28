# painting attr: https://www.w3.org/TR/SVG/painting.html
# svgwrite docs: https://svgwrite.readthedocs.io/en/master/
# potential way to create gifs - https://pypi.org/project/drawSvg/ or https://github.com/mozman/svgwrite/blob/master/svgwrite/animate.py
# examples: https://drive.google.com/drive/u/0/folders/0BwFQiTKfux0qY1Y2d1hRdndtSEk
# docs http://tutorials.jenkov.com/svg/svg-transformation.html
# translations: https://www.sarasoueidan.com/blog/svg-transformations/


from svgpathtools import Arc, CubicBezier, Line, Path as spt_Path, QuadraticBezier
from svgwrite.path import Path

from svg_sheets.utils import determine_stroke_width

SVG_SHAPE_PARTS = ("start", "end", "radius", "control", "control1", "control2")
SVG_TRANSFORMATIONS = ("translate", "rotate", "scale", "skewX", "skewY", "matrix")

# DIAGNOSTICS
CURRENT_X = 0
CURRENT_Y = 0
MIN_X = 0
MIN_Y = 0
MAX_X = 0
MAX_Y = 0


def create_paths(paths, full_size, stroke='#000000', min_width=1, fill='#000000'):
    path_objs = []
    for i, p in enumerate(paths):
        if isinstance(p, spt_Path):
            ps = p.d()
        elif type(p) in (Line, QuadraticBezier, CubicBezier, Arc):
            ps = spt_Path(p).d()
        else:  # assume this path, p, was input as a Path d-string
            ps = p
        path_len = determine_stroke_width(p, full_size, min_width)
        path_objs.append(Path(ps, stroke=stroke, stroke_width=f"{path_len}", fill=fill))
    return path_objs


def bounding_box(svg, x, y, width, height, stroke=1):
    return svg.rect(insert=(x, y),
                    size=(width, height),
                    stroke_width=f"{stroke}",
                    stroke="green",
                    fill_opacity="0")


# BELOW likely unused
def move_cursor_to(upper_left_pixel_horizontal, upper_left_pixel_vertical):
    global CURRENT_X, CURRENT_Y
    CURRENT_X = upper_left_pixel_horizontal
    CURRENT_Y = upper_left_pixel_vertical
    return [f"M {upper_left_pixel_horizontal}, {upper_left_pixel_vertical}"]


def relative_move(upper_left_pixel_horizontal, upper_left_pixel_vertical):
    global CURRENT_X, CURRENT_Y
    CURRENT_X += upper_left_pixel_horizontal
    CURRENT_Y += upper_left_pixel_vertical
    return [f"m {upper_left_pixel_horizontal}, {upper_left_pixel_vertical}"]


def draw_relative_line(upper_left_pixel_horizontal, upper_left_pixel_vertical):
    global CURRENT_X, CURRENT_Y
    CURRENT_X += upper_left_pixel_horizontal
    CURRENT_Y += upper_left_pixel_vertical
    return [f"l {upper_left_pixel_horizontal}, {upper_left_pixel_vertical}"]


def draw_absolute_line(upper_left_pixel_horizontal, upper_left_pixel_vertical):
    global CURRENT_X, CURRENT_Y
    CURRENT_X += upper_left_pixel_horizontal
    CURRENT_Y += upper_left_pixel_vertical
    return [f"L {upper_left_pixel_horizontal}, {upper_left_pixel_vertical}"]


def create_curve(start_cp_x, start_cp_y, end_cp_x, end_cp_y, end_point_x, end_point_y):
    global CURRENT_X, CURRENT_Y
    CURRENT_X = end_point_x
    CURRENT_Y = end_point_y
    return [
        f'c {start_cp_x},{start_cp_y} '
        f'{end_cp_x},{end_cp_y} '
        f'{end_point_x},{end_point_y}'
    ]


def create_absolute_curve(start_cp_x, start_cp_y, end_cp_x, end_cp_y, end_point_x, end_point_y):
    global CURRENT_X, CURRENT_Y
    CURRENT_X = end_point_x
    CURRENT_Y = end_point_y
    return [
        f'C {start_cp_x},{start_cp_y} '
        f'{end_cp_x},{end_cp_y} '
        f'{end_point_x},{end_point_y}'
    ]


def curve_math():
    pass  # TODO


def add_closure():
    return ['z']


def parse_svg_d_info(input_str):
    shape = Path()
    # (-*\d+\.*\d*), *(-*\d+\.*\d*) (-*\d+\.*\d*), *(-*\d+\.*\d*) (-*\d+\.*\d*), *(-*\d+\.*\d*)
    # viper.push(create_curve($1, $2, $3, $4, $5, $6))\n
    return shape


def move_to_calcs(start_coords, shape_offset):
    return [start_coords[0] + shape_offset[0], start_coords[1] + shape_offset[1]]


def scaler_calcs(start_coords, end_coords, shape_size, specific_scalars):
    if specific_scalars[0] and specific_scalars[1]:
        scalar_x = specific_scalars[0]
        scalar_y = specific_scalars[1]
    elif end_coords[0] and end_coords[1]:
        scalar_x = (end_coords[0] - start_coords[0]) / shape_size[0]
        scalar_y = (end_coords[1] - start_coords[1]) / shape_size[1]
    else:
        scalar_x = 1
        scalar_y = 1
    return scalar_x, scalar_y
