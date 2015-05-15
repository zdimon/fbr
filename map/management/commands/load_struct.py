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
        for i in Vegetat.objects.all():
            try:
                s = Structure.objects.get(structure=i.structure)            
                i.struct = s
                i.save()
            except:
                pass
            print 'proccess.......%s' % i.gid
