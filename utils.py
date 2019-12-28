
def determine_scale(scalar, existing_dimension):
    new_dimension = existing_dimension + scalar
    return round(new_dimension / existing_dimension, 2)


def determine_stroke_width(path, full_size, min_width):
    return max(min_width, round(path.length() * 100 / (full_size.x * full_size.y), 1))


def invert_y_axis(page_height, inkscape_value):
    return page_height - inkscape_value


def convert_in_to_px(inch_value, dpi):
    return inch_value * dpi
