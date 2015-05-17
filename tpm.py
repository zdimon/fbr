@property
    v = '''def thumb(self):
        from fbr.settings import BASE_DIR
        filename = BASE_DIR+'/static/thumbnails/radiation/radiation-%s.png' % str(self.gid)
        import os.path
        if os.path.isfile(BASE_DIR): 
            return mark_safe('<img src="/static/thumbnails/radiation/radiation-%s.png">' % str(self.gid))
        import mapnik
        from mapnik import PostGIS
        
        m = mapnik.Map(100,100)
        m.background = mapnik.Color('steelblue')
        s = mapnik.Style()
        r = mapnik.Rule()
        polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))
        r.symbols.append(polygon_symbolizer)
        line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)
        #f = mapnik.Filter("[gid] = 1")
        #r.filter.append(f)
        r.symbols.append(line_symbolizer)
        s.rules.append(r)

        m.append_style('My Style',s)
        #ds = mapnik.Shapefile(file='vector_data/radiation250.shp')
        layer = mapnik.Layer('world')
        query = "(select geom from map_vegetation where gid="+str(self.gid)+") as data"
        layer.datasource = PostGIS(host='localhost',user='postgres',password='1q2w3e',dbname='fbr',table=query)


        #layer.datasource = ds
        layer.styles.append('My Style')
        m.layers.append(layer)
        m.zoom_all()
        
        mapnik.render_to_file(m,filename, 'png')
        return mark_safe('<img src="/static/thumbnails/radiation/radiation-%s.png">' % str(self.gid))'''
