from svgwrite.text import Text

from svg_sheets.svgs.sheet_builder import Builder


def center_text_horizontally(group, text):
    t = Text(text, stroke_width=25)
    group.group.add(t)


b = Builder()
b.create_portrait_doc(doc_width=500, doc_height=500)
right_banner = b.add_shape('../shapes/containers/header.svg', 'right_name_banner')
right_banner.move(20, 20)
center_text_horizontally(right_banner, 'Darya Firahel')
right_banner.adjust_in_doc()
