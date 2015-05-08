from django.conf.urls import patterns, include, url
from map.views import GetPolygonJsonCotter
from map.models import Cotter

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'map.views.home', name='home'),
     url(r'^cotter$', 'map.views.cot', name='cotter'),  
     url(r'^radiation$', 'map.views.radiation', name='radiation'),  
     url(r'^slope$', 'map.views.slope', name='slope'),  
    #url(r'^test$', 'map.views.test', name='test'),  


    url(r'^cotter-json/$', GetPolygonJsonCotter.as_view(model=Cotter,properties=('gid','veg_types'))),

    url(r'^admin/', include(admin.site.urls)),
)
