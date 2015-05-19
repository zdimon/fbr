from django.contrib import admin
from map.models import Cotter, Slope, Radiation, Vegetation, Structure, Veget, Direction
from djgeojson.views import GeoJSONLayerView
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from django.conf import settings
# Register your models here.











class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization


#class CotterAdmin(OSMGeoAdmin):
#    map_template = 'gis/admin/google.html'
#    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % #settings.GOOGLE_MAPS_API_KEY]

#admin.site.register(Cotter, CotterAdmin)


class VegetationAdmin(OSMGeoAdmin):
    list_display = ("gid", "struct", "objectid", "area", "perimeter", "veg", "veg_id", "veg_sp_1", "veg_sp_2", "veg_sp_3", "state", "fueltype", "fuelcode_v", "hectares")
    search_fields = ("gid", "objectid")
    list_filter = ("struct",)  
    ordering = ('gid',) 
    fields = ('gid', 'objectid', 'area', 'perimeter', 'veg', 'veg_id', 'veg_sp_1', 'veg_sp_2', 'veg_sp_3', 'struct', 'class1', 'symbol', 'state', 'fueltype', 'fuelcode_v', 'acres', 'hectares', 'geom') 
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Vegetation, VegetationAdmin)


class DirectionAdmin(OSMGeoAdmin):
    list_display = ("gid", "direction")
    search_fields = ("gid", "direction")
   # list_filter = ("struct",)  
    ordering = ('gid',) 
    fields = ('gid', 'direction') 
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Direction, DirectionAdmin)



class VegetAdmin(OSMGeoAdmin):
    list_display = ("gid", "struct")
    search_fields = ("gid",)
    list_filter = ("struct",) 
    ordering = ('gid',)   
    fields = ('gid', 'gridcode', 'struct', 'geom')    
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Veget, VegetAdmin)


class StructureAdmin(OSMGeoAdmin):
    list_display = ("structure", "fuel_moisture", "fuel_load", "litter", 'color', 'color_repr')
    list_editable = ('color',)
    search_fields = ("id",)
    list_filter = ("fuel_load",) 
    ordering = ('id',)   
    fields = ("structure", "fuel_moisture", "fuel_load", "litter", 'color', 'color_repr')
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Structure, StructureAdmin)



class SlopeAdmin(OSMGeoAdmin):
    list_display = ("id", "gridcode")
    search_fields = ("gridcode",)
    list_filter = ("gridcode",) 
    ordering = ('id',)
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Slope, SlopeAdmin)



class RadiationAdmin(OSMGeoAdmin):
    list_display = ("id", "gridcode")
    search_fields = ("gridcode",)
    list_filter = ("gridcode",)
    ordering = ('id',)
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Radiation, RadiationAdmin)

