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
        for s in Slope.objects.all():
            sq = Veget.objects.filter(geom__bboverlaps=s.geom)
            try:
                if sq[0].structure == 'LOW WOODLAND':
                    x = 1
                else:
                    x = 0 
                
                eff =  Decimal(s.gridcode) * Decimal('2.606') + Decimal(x) * Decimal(sq[0].struct.litter)
            except:
                pass
                #import pdb; pdb.set_trace()    
            s.effectiveness = eff
            s.litter = sq[0].struct.litter
            s.structure = sq[0].struct.structure
            s.save()
            print 'proccess.......%s' % s.gid
