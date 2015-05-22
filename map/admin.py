from django.contrib import admin
from map.models import Cotter, Slope, Radiation, Vegetation, Structure, Veget, Direction, Effectiveness, Ndvi001250, Ndvi209250
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


#class DroughtIndexAdmin(OSMGeoAdmin):
#    list_display = ("gid", "month", "direction", "value")
#    search_fields = ("gid", "value")
   # list_filter = ("struct",)  
#    ordering = ('gid',) 
#    fields = ('gid', 'value') 
#    map_template = 'gis/admin/google.html'
#    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

#admin.site.register(DroughtIndex, DroughtIndexAdmin)



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
    fields = ("structure", "fuel_moisture", "fuel_load", "litter", 'color')
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Structure, StructureAdmin)



class EffectivenessAdmin(OSMGeoAdmin):
    list_display = ("gid", "effectiveness", 'color', 'color_repr')
    list_editable = ('color',)
    search_fields = ("gid",)
    list_filter = ("effectiveness",) 
    ordering = ('gid',)   
    fields = ("effectiveness", 'color')
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Effectiveness, EffectivenessAdmin)




class SlopeAdmin(OSMGeoAdmin):
    list_display = ("id", "gridcode", 'effectiv')
    search_fields = ("gridcode",)
    list_filter = ("gridcode","effectiv") 
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


class Ndvi001250Admin(OSMGeoAdmin):
    list_display = ("gid", "gridcode", 'ndvi_category', 'fuel_load')
    search_fields = ("gridcode",)
    list_filter = ("gridcode","fuel_load") 
    ordering = ('gid',)
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Ndvi001250, Ndvi001250Admin)



class Ndvi209250Admin(OSMGeoAdmin):
    list_display = ("gid", "gridcode", 'ndvi_category', 'fuel_load')
    search_fields = ("gridcode",)
    list_filter = ("gridcode","fuel_load") 
    ordering = ('gid',)
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Ndvi209250, Ndvi209250Admin)

