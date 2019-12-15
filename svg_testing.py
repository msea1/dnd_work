from math import ceil
from os.path import join

from svgpathtools import disvg, svg2paths, Arc, Line, QuadraticBezier, CubicBezier, Path as spt_Path
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing
from svgwrite.path import Path

from svg_sheets.common import move_cursor_to, move_to_calcs, scaler_calcs

from math import ceil
from os.path import join

from svgpathtools import Arc, CubicBezier, Line, Path as spt_Path, QuadraticBezier, svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite import Drawing


def create_doc(filename, all_paths):
    xmin, xmax, ymin, ymax = big_bounding_box(all_paths)
    dx = xmax - xmin
    dy = ymax - ymin

    # adding a small buffer
    # determine stroke_widths to use
    # sw = max(dx, dy) * 1e-3
    # stroke_widths = [sw]*len(all_paths)
    # max_stroke_width = sw

    # xmin -= 0.1 * dx + max_stroke_width / 2
    # ymin -= 0.1 * dy + max_stroke_width / 2
    # dx += 2 * 0.1 * dx + max_stroke_width
    # dy += 2 * 0.1 * dy + max_stroke_width

    # max dimension, if want to constrain
    max_dim = 400
    if dx > dy:
        szx = str(max_dim) + 'px'
        szy = str(int(ceil(max_dim * dy / dx))) + 'px'
    else:
        szx = str(int(ceil(max_dim * dx / dy))) + 'px'
        szy = str(max_dim) + 'px'
    dimensions = szx, szy

    viewbox = f"{xmin} {ymin} {dx} {dy}"
    return Drawing(filename=filename, size=(dx, dy), viewBox=viewbox)


def create_path(dwg, paths):
    for i, p in enumerate(paths):
        if isinstance(p, spt_Path):
            ps = p.d()
        elif type(p) in (Line, QuadraticBezier, CubicBezier, Arc):
            ps = spt_Path(p).d()
        else:  # assume this path, p, was input as a Path d-string
            ps = p
        return dwg.path(ps, stroke='#000000', stroke_width="1", fill='#000000')


svg_dir = '/home/mcarruth/Code/personal/svg_sheets/shapes/'
all_paths, _ = svg2paths(join(svg_dir, 'bear.svg'))
# bbox = big_bounding_box(bear_paths)
raven_paths, _ = svg2paths(join(svg_dir, 'viper2.svg'))
# bbox2 = big_bounding_box(raven_paths)

all_paths.extend(raven_paths)
svg_doc = create_doc('testing.svg', all_paths)
p1 = create_path(svg_doc, [all_paths[0]])
p2 = create_path(svg_doc, [all_paths[1]])
g1 = svg_doc.g()
g2 = svg_doc.g()
g1.add(p1)
g2.add(p2)
svg_doc.add(g1)
svg_doc.add(g2)

# move, scale, etc
g2.translate(150, 5)
g1.scale(.8, 1)
g2.rotate(90)

# redo viewbox bound post mixins
# TODO -
#  could use g1.attribs.get('transform', {}).get('scale')
#  and then do math on the bbox, but it won't account for all groups, complicated - ultimately not super needed?
# bbox = big_bounding_box(all_paths)
# print(bbox)

svg_doc.save(pretty=True)