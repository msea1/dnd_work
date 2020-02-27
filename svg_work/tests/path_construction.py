
# DIAGNOSTICS
CURRENT_X = 0
CURRENT_Y = 0
MIN_X = 0
MIN_Y = 0
MAX_X = 0
MAX_Y = 0


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


def add_closure():
    return ['z']


def move_to_calcs(start_coords, shape_offset):
    return [start_coords[0] + shape_offset[0], start_coords[1] + shape_offset[1]]


def scalar_calcs(start_coords, end_coords, shape_size, specific_scalars):
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
