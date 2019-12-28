from xml.dom import minidom

from svgwrite.path import Path

from svg_sheets.svgs.common import add_closure, move_cursor_to, \
    move_to_calcs, relative_move, scaler_calcs




def abcdef(start_x, start_y, end_x=None, end_y=None, relative_size_x=None, relative_size_y=None):
    path = Path()
    move_to = move_to_calcs(start_coords=(start_x, start_y), shape_offset=(23, 167))
    path.push(move_cursor_to(move_to[0], move_to[1]))

    path.push(relative_move(27.827651, 240.09871))

    path.push(add_closure())

    scalar_x, scalar_y = scaler_calcs(
        start_coords=(start_x, start_y),
        end_coords=(end_x, end_y),
        shape_size=(143, 167),
        specific_scalars=(relative_size_x, relative_size_y)
    )
    path.scale(scalar_x, scalar_y)
    return path


def read_from_file(filepath):
    if not filepath.endswith('.svg'):
        raise ValueError(f'Need to pass an svg file, you passed {filepath}')

    doc = minidom.parse(filepath)  # parseString also exists
    path_strings = [
        path.getAttribute('d') for path in doc.getElementsByTagName('path')
    ]
    doc.unlink()
    path_obj = Path()
    path_obj.push(path_strings[0])
    return path_obj
