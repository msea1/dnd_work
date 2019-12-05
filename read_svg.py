from svgpathtools import disvg, svg2paths
from svgpathtools.paths2svg import big_bounding_box
from svgwrite.mixins import ViewBox, Transform
from svgwrite.path import Path

from svg_sheets.common import bounding_box, move_cursor_to, move_to_calcs, scaler_calcs


# TODO editor to chop up svg
# TODO, colors
# TODO, multi paths in single image
# TODO, create stable samples of various shapes

def shift_path(read_path, start_x, start_y, end_x=None, end_y=None, bbox=(0, 0), relative_size_x=None, relative_size_y=None):
    new_path = Path()

    # shift
    move_to = move_to_calcs(start_coords=(start_x, start_y), shape_offset=(bbox[0], bbox[2]))
    new_path.push(move_cursor_to(move_to[0], move_to[1]))

    cmd_list = break_up_path_commands(read_path.commands)
    for i in cmd_list:
        new_path.push(i)

    # scale or transform
    scalar_x, scalar_y = scaler_calcs(
        start_coords=(start_x, start_y),
        end_coords=(end_x, end_y),
        shape_size=(81, 58),
        specific_scalars=(relative_size_x, relative_size_y)
    )
    new_path.scale(scalar_x, scalar_y)
    return new_path


def break_up_path_commands(path_cmd_str):
    return []  # maybe not needed


def test_pathtools(filepath):  # works but is def slower than svgwrite
    paths, attr_dict = svg2paths(filepath)
    # svg_doc = disvg(paths, attributes=attr_dict, dimensions=(2000, 2000), filename='testing.svg', paths2Drawing=True)
    # bbox = paths2svg.big_bounding_box(paths)
    # svg_doc.add(bounding_box(svg_doc, x=bbox[0], width=(bbox[1]-bbox[0]), y=bbox[2], height=(bbox[3]-bbox[2]), stroke=5))
    # svg_doc.save()

    # scale example
    # svg_doc.elements[1].scale(.25, .5)

    svg_doc = disvg(paths, attributes=attr_dict, filename='testing.svg', paths2Drawing=True)

    # figure this shit out TODO
    # move to 0,0 or x,y for UL example
    bbox = big_bounding_box(paths)
    # svg_doc.defs.translate(bbox[0], bbox[2])  # nope
    svg_doc.defs.rotate(45)  # nope these never do anything?
    # svg_doc.viewbox(minx=bbox[0], width=(bbox[1] - bbox[0]), miny=bbox[2], height=(bbox[3] - bbox[2]))
    # svg_doc.fit(horiz='left', vert='top')
    # svg_doc.fit()

    # svg_doc.add(bounding_box(svg_doc, x=bbox[0], width=(bbox[1] - bbox[0]), y=bbox[2], height=(bbox[3] - bbox[2]), stroke=5))
    # todo, constrain to x1, y1 for BR
    # svg_doc.viewbox(minx=bbox[0], width=(200), miny=bbox[2], height=(400))
    # svg_doc.fit(horiz='left', vert='top')
    # svg_doc.stretch()
    svg_doc.save(pretty=True)


test_pathtools('/home/mcarruth/Code/personal/svg_sheets/bear.svg')
