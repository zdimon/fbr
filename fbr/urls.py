from django.conf.urls import patterns, include, url
from map.vews import GetPolygonJsonCotter
from map.models import Cotter

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'map.views.home', name='home'),
    url(r'^cotter/$', GetPolygonJsonCotter.as_view(model=Cotter,properties=('gid','veg_types')), name='cotter'),

    url(r'^admin/', include(admin.site.urls)),
)
