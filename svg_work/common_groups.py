from svg_sheets.svg_work.constants import BUMPER_PX


def add_name_banners(sheet):
    herald = sheet.add_shape('../shapes/containers/header.svg', 'left_name_banner')
    herald.move(BUMPER_PX, BUMPER_PX)

    right_banner = sheet.add_shape('../shapes/containers/header.svg', 'right_name_banner')
    right_banner.flip(along_x=True)
    right_banner.move_to(*herald.upper_right)
    return herald, right_banner


def add_dodec_banner(sheet, label, value):
    # bg_hex = sheet.add_shape
    return None
