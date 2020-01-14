# svg_sheets

## Goals
- building shapes
    - clean path
    
- building a sheet
    - cleaning up inkscape SVGs
    - scaling text
    - snapping groups

- sprucing up
    - testing
    - how to share / profit?
    - timeit to speed up


## Image to SVG/Path
- download image
- open in gimp
- select portion
- copy into new image
- paste, enter
- layer --> autocrop layer
- image --> fit canvas to layers
- export as png

- load into Inkscape
- select image, shift-alt-b to trace bitmap, up thresholds
- drag result over, select original image, delete
- In Document Properties (shift-ctrl-D), set viewbox to 0,0
- (Extensions -- Arrange -- Deep Ungroup)
- ctrl + L to simplify path (optionally)
- select trace, shift-ctrl-r to resize, save

- run through clean_path.py
- rename output svg


### Links
painting attr: https://www.w3.org/TR/SVG/painting.html
svgwrite docs: https://svgwrite.readthedocs.io/en/master/
potential way to create gifs - https://pypi.org/project/drawSvg/ or https://github.com/mozman/svgwrite/blob/master/svgwrite/animate.py
examples: https://drive.google.com/drive/u/0/folders/0BwFQiTKfux0qY1Y2d1hRdndtSEk
docs http://tutorials.jenkov.com/svg/svg-transformation.html
translations: https://www.sarasoueidan.com/blog/svg-transformations/

