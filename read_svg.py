from svgpathtools import disvg, svg2paths
from svgpathtools.paths2svg import big_bounding_box


def isolate_path(filepath_in, filename_out):
    paths, attr_dict = svg2paths(filepath_in)

    svg_doc = disvg(paths, attributes=attr_dict, filename=filename_out, paths2Drawing=True)
    bbox = big_bounding_box(paths)
    svg_doc.viewbox(minx=bbox[0], width=bbox[1] - bbox[0], miny=bbox[2], height=bbox[3] - bbox[2])
    # svg_doc.save()
    svg_doc.save(pretty=True)  # TODO, work around the inkscape tag thing


isolate_path('/home/mcarruth/Code/personal/svg_sheets/shapes/images/viper_2.svg', 'testing.svg')
