from svg_sheets.svg_work.constants import BUMPER_PX


def add_name_banners(sheet):
    herald = sheet.add_shape('../shapes/containers/header.svg', 'left_name_banner')
    herald.move(BUMPER_PX, BUMPER_PX)

    right_banner = sheet.add_shape('../shapes/containers/header.svg', 'right_name_banner')
    right_banner.flip(along_x=True)
    right_banner.move_to(*herald.upper_right)
    return herald, right_banner


def add_dodec_banner(sheet, label, value):
    bg_hex = sheet.add_shape('../shapes/containers/hexagon.svg', f'{label}_dodec_bg')
    fg_hex = sheet.add_shape('../shapes/containers/hexagon.svg', f'{label}_dodec_fg')
    fg_hex.rotate(90)
    # TODO, work needed here, not 0,0 based
    # transform="translate(400,400)
    # transform="translate(198,499) rotate(90,1,1) "

    # TODO TODO TODO TODO
    # hmm, maybe abandon this for importing and doing the editing in Inkscape, now that I have the shapes independent.
    # I can mass edit text, font, colors, etc directly in the .svg, or figure out in Inkscape... else you're sorta creating inkscape...
    return bg_hex, fg_hex
