from svgwrite.shapes import Rect
from svgwrite.text import Text, TSpan

from svg_sheets.svgs.sheet_builder import Builder

# https://www.w3.org/TR/SVG11/text.html


def add_visible_bounding_box(group_obj, in_group=True):
    r = Rect()
    r.attribs['stroke'] = 'blue'
    r.attribs['fill'] = 'none'

    if in_group:
        r.attribs['width'] = group_obj.size.x / group_obj.scale.x
        r.attribs['height'] = group_obj.size.y / group_obj.scale.y
        group_obj.group.add(r)
    else:
        r.attribs['x'] = group_obj.position.location.x
        r.attribs['y'] = group_obj.position.location.y
        r.attribs['width'] = group_obj.size.x
        r.attribs['height'] = group_obj.size.y
        group_obj.doc.add(r)


def scale_inside_container(text_obj, container_obj, in_group=True, **kwargs):
    # vertical-axis
    container_height = container_obj.size.y
    dist_from_top = kwargs.get('buffer_top', 0) / 100 * container_height
    dist_to_bot = container_height - (kwargs.get('buffer_bottom', 0) / 100 * container_height)
    font_size = dist_to_bot - dist_from_top
    if font_size < 0:
        raise ValueError('Vertical buffering of sub object is overlapping')
    if in_group:
        text_obj.attribs['font-size'] = font_size * container_obj.scale.y
        text_obj.attribs['y'] = dist_to_bot / container_obj.scale.y
    else:
        text_obj.attribs['font-size'] = font_size * container_obj.scale.y ** 2  # rough approx
        text_obj.attribs['y'] = container_obj.position.location.y + dist_to_bot

    # horizontal-axis
    container_width = container_obj.size.x
    dist_from_left = kwargs.get('buffer_left', 0) / 100 * container_width
    dist_to_right = container_width - (kwargs.get('buffer_right', 0) / 100 * container_width)
    text_length = dist_to_right - dist_from_left
    if text_length < 0:
        raise ValueError('Horizontal buffering of sub object is overlapping')
    if in_group:
        text_obj.attribs['textLength'] = text_length / container_obj.scale.x
        text_obj.attribs['x'] = dist_from_left
    else:
        text_obj.attribs['textLength'] = text_length
        text_obj.attribs['x'] = container_obj.position.location.x + dist_from_left


def center_text_horizontally(group_obj, text_obj):
    container_width = group_obj.size.x
    text_obj.attribs['text-anchor'] = 'middle'
    text_obj.attribs['x'] = group_obj.position.location.x + (container_width * 0.5)


def center_text_vertically(group_obj, text_obj):
    container_height = group_obj.size.y
    vert_buffer = (container_height - text_obj.attribs['font-size'])
    text_obj.attribs['y'] = group_obj.position.location.y + (vert_buffer * 0.5) + text_obj.attribs['font-size']


b = Builder()
b.create_portrait_doc(doc_width=500, doc_height=500)
right_banner = b.add_shape('../shapes/containers/header.svg', 'right_name_banner')
right_banner.move(20, 20)
right_banner.stretch_to(desired_height=80, desired_width=400)
add_visible_bounding_box(right_banner, in_group=False)

y = Text(text='')
ts = TSpan(text='Test word')
y.add(ts)
ts.text += ' and more'

y.attribs['y'] = '50'
y.attribs['fill'] = 'red'
y.attribs['font-family'] = 'Beograd, Soviet Program'
y.attribs['stroke'] = 'black'
y.attribs['stroke-width'] = 1
y.attribs['font-size'] = 20
y.attribs['textLength'] = 250
# y.attribs['letter-spacing'] = 5
# y.attribs['word-spacing'] = 5
y.attribs['lengthAdjust'] = 'spacingAndGlyphs'

right_banner.group.add(y)

scale_inside_container(y, right_banner, buffer_top=0, buffer_bottom=0, buffer_left=10, buffer_right=10)

# FIXME, tested with flipped objects, is troubling
# right_banner.flip(along_x=True)
b.svg_doc.save(pretty=True)

