from django.conf.urls import patterns, include, url
from map.views import GetPolygonJsonCotter
from map.models import Cotter

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'map.views.home', name='home'),
     url(r'^cotter$', 'map.views.cotter', name='cotter'),  
     url(r'^radiation$', 'map.views.cotter', name='radiation'),  
     url(r'^slope$', 'map.views.cotter', name='slope'),  


    #url(r'^cotter/$', GetPolygonJsonCotter.as_view(model=Cotter,properties=('gid','veg_types')), name='cotter'),

    url(r'^admin/', include(admin.site.urls)),
)
