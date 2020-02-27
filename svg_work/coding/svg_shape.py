from svgwrite.shapes import Rect

from svg_sheets.svg_work.utils import center_of_group, determine_scale


class Dimension:
    def __init__(self, width, height):
        self.x = width
        self.y = height

    def __str__(self):
        return f'Width (X): {self.x}, Height (Y): {self.y}'


class Position:
    def __init__(self, right, down):
        self.origin = Dimension(right, down)
        self.location = Dimension(right, down)


class Shape:
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

    @property
    def upper_left(self):
        return (
            self.position.location.x,
            self.position.location.y
        )

    @property
    def upper_right(self):
        return (
            self.position.location.x + self.size.x,
            self.position.location.y
        )

    @property
    def bottom_left(self):
        return (
            self.position.location.x,
            self.position.location.y + self.size.y
        )

    @property
    def bottom_right(self):
        return (
            self.position.location.x + self.size.x,
            self.position.location.y + self.size.y
        )

    def adjust_in_doc(self):
        self.doc.elements.remove(self.group)
        self.create_translations()
        self.doc.add(self.group)
        self.doc.save(pretty=True)

    def create_translations(self):
        refreshed = f"translate({self.position.origin.x},{self.position.origin.y}) "
        if self.rotation != 0:
            shape_center_x, shape_center_y = center_of_group(self.size, self.scale)
            refreshed += f"rotate({self.rotation},{shape_center_x},{shape_center_y}) "
        if self.scale.x != 1 or self.scale.y != 1:
            refreshed += f"scale({self.scale.x},{self.scale.y}) "
        if len(refreshed) > 0:
            self.group.attribs['transform'] = refreshed

    def move(self, move_right=0, move_down=0):
        self.position.location.x += move_right
        self.position.location.y += move_down
        self.position.origin.x += move_right
        self.position.origin.y += move_down
        self.adjust_in_doc()

    def move_to(self, new_x, new_y):
        dx = new_x - self.position.location.x
        dy = new_y - self.position.location.y

        self.position.origin.x += dx
        self.position.origin.y += dy

        self.position.location.x = new_x
        self.position.location.y = new_y
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
        self.adjust_in_doc()

    def stretch(self, stretch_right=0, stretch_down=0):
        if (stretch_right < 0 and abs(stretch_right) >= self.size.x) or (
                stretch_down < 0 and abs(stretch_down) >= self.size.y):
            print(f'unable to stretch into negative space')
            return

        # scale
        scale_x = determine_scale(stretch_right, self.size.x)
        scale_y = determine_scale(stretch_down, self.size.y)

        self.scale.x *= scale_x
        self.scale.y *= scale_y

        # size
        self.size.x += stretch_right
        self.size.y += stretch_down

        # move
        dx = 0 if self.positive_right else stretch_right
        dy = 0 if self.positive_down else stretch_down

        # adjust position for scale
        self.position.location.x -= dx
        self.position.location.y -= dy

        self.move(dx, dy)

    def stretch_to(self, desired_width=None, desired_height=None):
        dx = desired_width - self.size.x if desired_width else 0
        dy = desired_height - self.size.y if desired_height else 0
        self.stretch(dx, dy)

    def rotate(self, deg=0):
        self.rotation = deg
        self.adjust_in_doc()

    def add_visible_bounding_box(self, in_group=True):
        bbox = Rect()
        bbox.attribs['stroke'] = 'blue'
        bbox.attribs['fill'] = 'none'
    
        if in_group:
            bbox.attribs['width'] = self.size.x / self.scale.x
            bbox.attribs['height'] = self.size.y / self.scale.y
            self.group.add(bbox)
        else:
            bbox.attribs['x'] = self.position.location.x
            bbox.attribs['y'] = self.position.location.y
            bbox.attribs['width'] = self.size.x
            bbox.attribs['height'] = self.size.y
            self.doc.add(bbox)

    def scale_text(self, text_obj, in_group=True, **kwargs):
        # vertical-axis
        container_height = self.size.y
        dist_from_top = kwargs.get('buffer_top', 0) / 100 * container_height
        dist_to_bot = container_height - (kwargs.get('buffer_bottom', 0) / 100 * container_height)
        font_size = dist_to_bot - dist_from_top
        if font_size < 0:
            raise ValueError('Vertical buffering of sub object is overlapping')
        if in_group:
            text_obj.attribs['font-size'] = font_size * self.scale.y
            text_obj.attribs['y'] = dist_to_bot / self.scale.y
        else:
            text_obj.attribs['font-size'] = font_size * self.scale.y ** 2  # rough approx
            text_obj.attribs['y'] = self.position.location.y + dist_to_bot
    
        # horizontal-axis
        # note: generalized form, we could center more easily by utilizing 'text-anchor' = 'middle'
        container_width = self.size.x
        dist_from_left = kwargs.get('buffer_left', 0) / 100 * container_width
        dist_to_right = container_width - (kwargs.get('buffer_right', 0) / 100 * container_width)
        text_length = dist_to_right - dist_from_left
        if text_length < 0:
            raise ValueError('Horizontal buffering of sub object is overlapping')
        if in_group:
            text_obj.attribs['textLength'] = text_length / self.scale.x
            text_obj.attribs['x'] = dist_from_left
        else:
            text_obj.attribs['textLength'] = text_length
            text_obj.attribs['x'] = self.position.location.x + dist_from_left
