# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from map.models import Fires, Structure

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-f", "--file",
                    dest="file",
                    help=u"Start date"),
       
    )
    def handle(self, *args, **options):
        import os
        f = options["file"]
        path = os.path.abspath(f)
        print 'import from %s ' % path
        Fires.objects.all().delete()
        for l in open(path).readlines():
            print 'process.....%s' % l
            array = l.split(',')
            if array[2] == 'lowland forest':
                structure = Structure.objects.get(pk=2)
            elif array[2] == 'dry forest':
                structure = Structure.objects.get(pk=5)
            elif array[2] == 'open forest':
                structure = Structure.objects.get(pk=4)
            elif array[2] == 'tall open forest':
                structure = Structure.objects.get(pk=6)
            else:
                structure = Structure.objects.get(pk=2)


            f = Fires()
            f.plot_name = array[0]
            f.tsf = array[1]
            f.struct = structure
            f.tree_density = array[3]
            f.twi = array[4]
            f.litter = array[5]
            f.cwd = array[6]
            f.fuel_hazard = array[7]
            f.fuel_moisture = array[8]
            f.fire_date = array[9]
            f.ndvi = array[10]
            f.slope_degree = array[11]
            f.aspect = array[12]
            f.elevation = array[13]
            f.radiation = array[14]
            f.fuel_type = array[15]
            f.lai_over = array[16]
            f.lai_under = array[17]
            f.save()
            print array[0]


         
