from svgpathtools import Arc, CubicBezier, Line, Path as spt_Path, QuadraticBezier
from svgwrite.path import Path

SVG_SHAPE_PARTS = ("start", "end", "radius", "control", "control1", "control2")
SVG_TRANSFORMATIONS = ("translate", "rotate", "scale", "skewX", "skewY", "matrix")


def create_paths(paths, _full_size, stroke='#000000', min_width=1, fill='#000000'):
    path_objs = []
    for i, p in enumerate(paths):
        if isinstance(p, spt_Path):
            ps = p.d()
        elif type(p) in (Line, QuadraticBezier, CubicBezier, Arc):
            ps = spt_Path(p).d()
        else:  # assume this path, p, was input as a Path d-string
            ps = p
        # pen_width = determine_stroke_width(p, full_size, min_width)
        path_objs.append(Path(ps, stroke=stroke, stroke_width=f"{min_width}", fill=fill))
    return path_objs


def center_of_group(size, scale):
    return (
        round(size.x / 2, 2) * -1 if scale.x < 0 else 1,
        round(size.y / 2, 2) * -1 if scale.y < 0 else 1
    )


def convert_in_to_px(inch_value, dpi):
    return inch_value * dpi


def determine_scale(scalar, existing_dimension):
    new_dimension = existing_dimension + scalar
    return round(new_dimension / existing_dimension, 2)


def determine_stroke_width(path, full_size, min_width):
    return max(min_width, round(path.length() * 50 / (full_size.x * full_size.y), 1))


def invert_y_axis(page_height, inkscape_value):
    return page_height - inkscape_value
