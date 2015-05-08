from django.conf.urls import patterns, include, url
from map.views import GetPolygonJsonCotter, GetPolygonJsonRadiation
from map.models import Cotter, Radiation

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'map.views.radiation_json', name='home'),
     url(r'^cotter$', 'map.views.cot', name='cotter'),  
     url(r'^radiation$', 'map.views.radiation', name='radiation'),  
     url(r'^slope$', 'map.views.slope', name='slope'),  
     url(r'^radiation_json$', 'map.views.radiation_json', name='radiation_json'),  
    #url(r'^test$', 'map.views.test', name='test'),  


    url(r'^cotter-json/$', GetPolygonJsonCotter.as_view(model=Cotter,properties=('gid','veg_types'))),

    url(r'^radiation-json/$', GetPolygonJsonRadiation.as_view(model=Radiation,properties=('gid','gridcode'))),


    url(r'^admin/', include(admin.site.urls)),
)
