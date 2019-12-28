
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
