from svgwrite.text import TSpan, Text

from svg_sheets.svg_work.sheet_builder import Builder

# https://www.w3.org/TR/SVG11/text.html

b = Builder()

# b.create_portrait_doc(doc_width=500, doc_height=500)
#
# right_banner = b.add_shape('./shapes/containers/header.svg', 'right_name_banner')
# right_banner.stretch_to(100, 100)
# right_banner.move(200, 200)
# right_banner.flip(along_x=True)
# right_banner.stretch(stretch_right=150)
# right_banner.rotate(20)

b.create_portrait_doc(doc_width=500, doc_height=500)
right_banner = b.add_shape('../shapes/containers/header.svg', 'right_name_banner')
right_banner.move(20, 20)
right_banner.stretch_to(desired_height=80, desired_width=400)
right_banner.add_visible_bounding_box(in_group=False)

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

right_banner.scale_text(y, buffer_top=0, buffer_bottom=0, buffer_left=10, buffer_right=10)

# FIXME, tested with flipped objects, is troubling
# right_banner.flip(along_x=True)
b.svg_doc.save(pretty=True)

