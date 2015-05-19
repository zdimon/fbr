# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from map.models import *

#logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start'
        for s in Slope.objects.all():
            sq = Veget.objects.filter(geom__bboverlaps=s.geom)
            if sq[0].structure == 'LOW WOODLAND':
                x = 1
            else:
                x = 0 
            eff =  s.gridcode * 2.606 + x * s.struct.litter
            s.effectiveness = eff
            s.save()
            print 'proccess.......%s' % s.gid
