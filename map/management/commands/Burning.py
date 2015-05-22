# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from map.models import *
from decimal import Decimal

#logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start'
        Burning.objects.all().delete()
        o = Radiation.objects.get(pk=939)
        b = Burning()
        b.gid = 1
        b.id = 1
        b.gridcode = o.gridcode
        b.day = 1
        b.time = 1
        b.geom = o.geom
        b.save()

        ###################DISTANCE########################
        from django.contrib.gis.measure import D
        from django.contrib.gis.geos import Point
        from django.contrib.gis.geos import GEOSGeometry
        lon = 148.869028 
        lat = -35.581528
        DISTANCE_LIMIT_METERS = 5000
        input_point = Point(lon, lat, srid=4326)
        input_point.transform(900913)
        #for r in Radiation.objects.filter(geom__dwithin=(input_point , D(km=DISTANCE_LIMIT_METERS))):
        dist = D(m=5000)
        #import pdb; pdb.set_trace()
        objs = Radiation.objects.filter(geom__dwithin=(GEOSGeometry('POINT(-35.581528 148.869028)'), dist))
        for r in objs:
            b = Burning()
            b.gid = 1
            b.id = 1
            b.gridcode = o.gridcode
            b.day = 1
            b.time = 1
            b.geom = o.geom
            b.save()
            print 'adding............%s' % b.gid

       
        
        
        
  #      for s in Slope.objects.all():
 #           sq = Veget.objects.filter(geom__bboverlaps=s.geom)
#            try:
#                if sq[0].structure == 'LOW WOODLAND':
#                    x = 1
#                else:
#                    x = 0 
                
#                eff =  Decimal(s.gridcode) * Decimal('2.606') + Decimal(x) * Decimal(sq[0].struct.litter)
#            except:
 #               pass
                #import pdb; pdb.set_trace()    
#            s.effectiveness = eff
#            s.litter = sq[0].struct.litter
#            s.structure = sq[0].struct.structure
#            s.save()
#            print 'proccess.......%s' % s.gid
