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
        min_ef = Slope.objects.all).aggregate(Min('effectiveness'))
        h = (max_ef - min_ef) / 5;
        
        for s in Slope.objects.all():
            try:
                if min_ef <= s.effectiveness < (min_ef + h):
                    s.effectiveness_category = 1
                elif (min_ef + h) <= s.effectiveness < (min_ef + 2*h):
                    s.effectiveness_category = 2
                elif (min_ef + 2*h) <= s.effectiveness < (min_ef + 3*h):
                    s.effectiveness_category = 3
                elif (min_ef + 3*h) <= s.effectiveness < (min_ef + 4*h):
                    s.effectiveness_category = 4 
                elif (min_ef + 4*h) <= s.effectiveness <= max_ef:
                    s.effectiveness_category = 5       
    
                
                
            except:
                pass
                #import pdb; pdb.set_trace()    
            
            s.save()
            print 'proccess.......%s' % s.gid
