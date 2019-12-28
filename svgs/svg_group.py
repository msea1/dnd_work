from svg_sheets.svgs.properties import Dimension, Position
from svg_sheets.utils import determine_scale, center_of_group


class Group:
    def __init__(self, name, svg_doc):
        self.ref_id = name
        self.doc = svg_doc
        self.group = svg_doc.g()

        self.position = Position(0, 0)
        self.size = Dimension(0, 0)
        self.scale = Dimension(1, 1)
        self.skew = Dimension(0, 0)
        self.rotation = 0

        self.positive_right = True
        self.positive_down = True

    def adjust_in_doc(self):
        self.doc.elements.remove(self.group)
        self.create_translations()
        self.doc.add(self.group)
        self.doc.save(pretty=True)

    def create_translations(self):
        # current = self.group.attribs.get('transform')
        refreshed = ""
        if self.position.location.x > 0 or self.position.location.y > 0:
            refreshed += f"translate({self.position.location.x},{self.position.location.y}) "
        if self.rotation != 0:
            origin_x, origin_y = center_of_group(self.size)
            refreshed += f"rotate({self.rotation},{origin_x + self.position.location.x},{origin_y + self.position.location.y}) "
        if self.scale.x > 0 or self.scale.y > 0:
            refreshed += f"scale({self.scale.x},{self.scale.y}) "
        if len(refreshed) > 0:
            self.group.attribs['transform'] = refreshed

    def move(self, move_right=0, move_down=0):
        self.position.location.x += move_right
        self.position.location.y += move_down

        dx = move_right if self.positive_right else -move_right
        dy = move_down if self.positive_down else -move_down

        self.position.origin.x += dx
        self.position.origin.y += dy
        # self.group.translate(dx, dy)
        self.adjust_in_doc()

    def flip(self, along_x=False, along_y=False):
        if not (along_x or along_y):
            return
        if along_x:
            self.positive_right = not self.positive_right
            self.scale.x *= -1
            if self.positive_right:  # moved from neg --> pos
                self.position.location.x = self.position.origin.x
            else:  # moved from pos --> neg
                self.position.location.x = self.position.origin.x - self.size.x
        if along_y:
            self.positive_down = not self.positive_down
            self.scale.y *= -1
            if self.positive_down:  # moved from neg --> pos
                self.position.location.y = self.position.origin.y
            else:  # moved from pos --> neg
                self.position.location.y = self.position.origin.y - self.size.y
        # self.group.scale(-1 if along_x else 1, -1 if along_y else 1)
        self.adjust_in_doc()

    def stretch(self, stretch_right=0, stretch_down=0):
        if (stretch_right < 0 and abs(stretch_right) >= self.size.x) or (
                stretch_down < 0 and abs(stretch_down) >= self.size.y):
            print(f'unable to stretch into negative space')
            return

        # size
        self.size.x += stretch_right
        self.size.y += stretch_down

        # scale
        scale_x = determine_scale(stretch_right, self.size.x)
        scale_y = determine_scale(stretch_down, self.size.y)

        self.scale.x *= scale_x
        self.scale.y *= scale_y
        # self.group.scale(scale_x, scale_y)

        # move
        dx = 0 if self.positive_right else stretch_right
        dy = 0 if self.positive_down else stretch_down
        self.move(dx, dy)

        self.adjust_in_doc()

    def stretch_to(self, desired_width=None, desired_height=None):
        dx = desired_width - self.size.x if desired_width else 0
        dy = desired_height - self.size.y if desired_height else 0
        self.stretch(dx, dy)

    def rotate(self, deg=0, offset=None):
        # current = self.group.attribs.get('transform')
        # The positive direction of rotation is clockwise.
        # self.group.rotate(45, (100, 100))
        pass
