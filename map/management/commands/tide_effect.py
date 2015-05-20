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
        for s in Slope.objects.all():
            if s.effectiveness_category == '1':
                c = Effectiveness.objects.get(pk=1)
                s.effectiv = c
            elif s.effectiveness_category == '2':
                c = Effectiveness.objects.get(pk=2)
                s.effectiv = c
            elif s.effectiveness_category == '3':
                c = Effectiveness.objects.get(pk=3)
                s.effectiv = c
            elif s.effectiveness_category == '4':
                c = Effectiveness.objects.get(pk=4)
                s.effectiv = c
            elif s.effectiveness_category == '5':
                c = Effectiveness.objects.get(pk=5)
                s.effectiv = c
            c.save()
            print 'proccess.......%s' % s.gid
