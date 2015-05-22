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
        for r in Radiation.objects.all():
            b = Burning()
            b.id = r.id
            b.gid = r.gid
            b.gridcode = r.gridcode
            b.geom = r.geom
            b.save()
            print 'proccess.......%s' % b.gid
