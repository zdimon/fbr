from django.conf.urls import patterns, include, url
from map.views import GetPolygonJsonCotter, GetPolygonJsonRadiation, GetPolygonJsonVegetation, GetPolygonJsonVeget
from map.models import Cotter, Radiation, Vegetation, Veget

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'map.views.radiation', name='home'),
     url(r'^cotter/$', 'map.views.cot', name='cotter'),
     url(r'^vegetation/$', 'map.views.vegetation', name='vegetation'),  
     url(r'^radiation$', 'map.views.radiation', name='radiation'),  
     url(r'^slope$', 'map.views.slope', name='slope'),  
     url(r'^radiation_json$', 'map.views.radiation_json', name='radiation_json'),
     url(r'^vegetation_json$', 'map.views.vegetation_json', name='vegetation_json'),  
    url(r'^crap$', 'map.views.home', name='crap'),  


    url(r'^cotter-json/$', GetPolygonJsonCotter.as_view(model=Cotter,properties=('gid','veg_types'))),

    url(r'^radiation-json/$', GetPolygonJsonRadiation.as_view(model=Radiation,properties=('gid','gridcode'))),
    url(r'^vegetation-json/$', GetPolygonJsonVegetation.as_view(model=Vegetation,properties=('gid','structure'))),
    url(r'^veget-json/$', GetPolygonJsonVeget.as_view(model=Veget,properties=('gid','structure'))),
    


    url(r'^admin/', include(admin.site.urls)),
)
