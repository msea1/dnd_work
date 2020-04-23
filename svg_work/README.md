# svg_sheets

## Goals
- process or code to easily sub in font/colors into same space
- create graphics / macros (using Inkscape + py functions)
- prune down py code that's useful
- DOCUMENT it! + document Inkscape/svg useful tips

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

fonts to steal/trace from
https://www.fontspace.com/category/blood,dripping
https://www.1001fonts.com/horror+dripping-fonts.html

icons:
https://iconsrepo.com/icons/castle/
https://game-icons.net/1x1/heavenly-dog/defensive-wall.html
iconfinder.com
https://www.svgrepo.com/vectors/tumble/
https://www.onlinewebfonts.com/icon/search?q=wolf
https://www.freesvg.org/search

color:
https://encycolorpedia.com/flags




