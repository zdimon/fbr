#! /usr/bin/python


import mapnik
from mapnik import PostGIS

m = mapnik.Map(600,600)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
#ds = mapnik.Shapefile(file='vector_data/radiation250.shp')
layer = mapnik.Layer('world')
layer.datasource = PostGIS(host='localhost',user='postgres',password='1q2w3e',dbname='fbr',table='map_vegetation')


#layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.png', 'png')
print "rendered image to 'world.png'"

