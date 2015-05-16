from django.contrib import admin
from map.models import Cotter, Slope, Radiation, Vegetation, Structure, Veget
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
    list_display = ("gid", "struct", "objectid", "area", "perimeter", "veg", "veg_id", "veg_sp_1", "veg_sp_1", "veg_sp_1", "state", "fueltype", "fuelcode_v", "hectares")
    search_fields = ("gid", "objectid")
    list_filter = ("struct",)  
    ordering = ('gid',)  
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Vegetation, VegetationAdmin)


class VegetAdmin(OSMGeoAdmin):
    list_display = ("gid", "struct")
    search_fields = ("gid",)
    list_filter = ("struct",) 
    ordering = ('gid',)   
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]

admin.site.register(Veget, VegetAdmin)


class StructureAdmin(OSMGeoAdmin):
    list_display = ("id", "structure", "fuel_moisture", "fuel_load")
    search_fields = ("id",)
    list_filter = ("fuel_load",) 
    ordering = ('id',)   
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

