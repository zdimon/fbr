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
        max_ef = Slope.objects.all().aggregate(Max('effectiveness'))
        min_ef = Slope.objects.all().aggregate(Min('effectiveness'))
        print min_ef
        
        h = (Decimal( max_ef['effectiveness__max']) - Decimal( min_ef['effectiveness__min'])) / Decimal(5);
        #import pdb; pdb.set_trace()    
        for s in Slope.objects.all():

            if min_ef['effectiveness__min'] <= s.effectiveness < (min_ef['effectiveness__min'] + h):
                s.effectiveness_category = 1
            elif (min_ef['effectiveness__min'] + h) <= s.effectiveness < (min_ef['effectiveness__min'] + 2*h):
                s.effectiveness_category = 2
            elif (min_ef['effectiveness__min'] + Decimal(2)*h) <= s.effectiveness < (min_ef['effectiveness__min'] + 3*h):
                s.effectiveness_category = 3
            elif (min_ef['effectiveness__min'] + Decimal(3)*h) <= s.effectiveness < (min_ef['effectiveness__min'] + 4*h):
                s.effectiveness_category = 4 
            elif (min_ef['effectiveness__min'] + Decimal(4)*h) <= s.effectiveness <= max_ef['effectiveness__max']:
                s.effectiveness_category = 5       
        
                
                
               
            
            s.save()
            print 'proccess.......%s' % s.gid
