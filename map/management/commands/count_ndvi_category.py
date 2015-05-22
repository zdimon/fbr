# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from map.models import *
from decimal import Decimal
from django.db.models import Max, Min

#logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start'
        max_ef = Ndvi001120.objects.all().aggregate(Max('gridcode'))
        min_ef = Ndvi001120.objects.all().aggregate(Min('gridcode'))
        print min_ef
        
        h = (Decimal( max_ef['gridcode__max']) - Decimal( min_ef['gridcode__min'])) / Decimal(5);
        #import pdb; pdb.set_trace()    
        for s in Ndvi001120.objects.all():

            if min_ef['gridcode__min'] <= s.gridcode < (min_ef['gridcode__min'] + h):
                s.ndvi_category = 1
            elif (min_ef['gridcode__min'] + h) <= s.gridcode < (min_ef['gridcode__min'] + 2*h):
                s.ndvi_category = 2
            elif (min_ef['gridcode__min'] + Decimal(2)*h) <= s.gridcode < (min_ef['gridcode__min'] + 3*h):
                s.ndvi_category = 3
            elif (min_ef['gridcode__min'] + Decimal(3)*h) <= s.gridcode < (min_ef['gridcode__min'] + 4*h):
                s.ndvi_category = 4 
            elif (min_ef['gridcode__min'] + Decimal(4)*h) <= s.gridcode <= max_ef['gridcode__max']:
                s.ndvi_category = 5       
        
                
                
               
            
            s.save()
            print 'proccess.......%s' % s.gid
