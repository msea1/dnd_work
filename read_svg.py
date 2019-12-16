from svgpathtools import disvg, svg2paths
from svgpathtools.paths2svg import big_bounding_box


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


def isolate_path(filepath_in, filename_out):
    paths, _ = svg2paths(filepath_in)
    paths = remove_canvas(paths)
    paths = break_up_paths(paths)
    paths = [p for p in paths if len(p) > 0]
    svg_doc = disvg(paths, filename=filename_out, paths2Drawing=True)
    bbox = big_bounding_box(paths)
    svg_doc.viewbox(minx=bbox[0], width=bbox[1] - bbox[0], miny=bbox[2], height=bbox[3] - bbox[2])
    svg_doc.save(pretty=True)


isolate_path('./alignment.png', 'shapes/testing.svg')
