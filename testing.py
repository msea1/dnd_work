from svgwrite.path import Path

from svg_sheets.common import create_curve, move_cursor_to


def test_triangle():
    test_path = Path()
    test_path.push(['M 100,100'])
    test_path.push(['L 300,100'])
    test_path.push(['L 200,300'])
    test_path.push(['z'])
    test_path.update({"fill": "red", "stroke": "blue", "stroke-width": "3"})
    return test_path


def test_curve():
    test_path = Path()
    test_path.push(move_cursor_to(0, 100))
    test_path.push(create_curve(0, -100, 150, -100, 150, 0))
    test_path.update({"stroke": "red", "stroke-width": 5})
    return test_path


def test_round_rect(drawing, x, y, width, height):
    return drawing.rect(insert=(x, y), size=(width, height), rx="20", ry="20",
                        stroke_width="1",
                        stroke="green",
                        fill="rgb(255,255,0)")
