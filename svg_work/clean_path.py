from svgpathtools import disvg, svg2paths

from svg_sheets.svg_work.utils import SVG_SHAPE_PARTS


def remove_canvas(path_list):
    rects = []
    for p in path_list:
        if len(p) == 4:
            rects.append(p)
    for r in rects:
        path_list.remove(r)
    return path_list


def remove_inkscape_attributes(attribute_dict):
    for attr in attribute_dict:
        keys = list(attr.keys())
        for k in keys:
            if 'inkscape' in k:
                del attr[k]
    return attribute_dict


def break_up_paths(path_list):
    new_paths = []
    for p in path_list:
        new_paths.extend(p.continuous_subpaths())
    return new_paths


def clean_path(path, places=1):
    setattr(path, 'start', round(path.start.real, places) + 1j * round(path.start.imag, places))
    setattr(path, 'end', round(path.end.real, places) + 1j * round(path.end.imag, places))
    for s in path._segments:
        for a in SVG_SHAPE_PARTS:
            if hasattr(s, a):
                cur_val = getattr(s, a)
                setattr(s, a, round(cur_val.real, places) + 1j * round(cur_val.imag, places))
    return path


def isolate_path(filepath_in, filename_out):
    paths, _ = svg2paths(filepath_in)
    # paths = remove_canvas(paths)
    paths = break_up_paths(paths)
    paths = [p for p in paths if len(p) > 0]
    paths = [clean_path(p) for p in paths]
    svg_doc = disvg(
        paths=paths,
        stroke_widths=[0.3] * len(paths),
        margin_size=0,
        filename=filename_out,
        paths2Drawing=True,
        mindim=200
    )
    # bbox = paths2svg.big_bounding_box(paths)
    # svg_doc.viewbox(minx=0, width=bbox[1] - bbox[0], miny=0, height=bbox[3] - bbox[2])
    # svg_doc.viewbox(minx=bbox[0], width=bbox[1] - bbox[0], miny=bbox[2], height=bbox[3] - bbox[2])
    svg_doc.save(pretty=True)


isolate_path('./input.svg', './output.svg')
