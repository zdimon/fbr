# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
#from litres.tasks import *
from django.utils import translation
from decimal import Decimal

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-t", "--temperature",
                    dest="temperature",
                    help=u"Air temperature"),
        make_option("-u", "--humidity",
                    dest="humidity",
                    help=u"Relitive humidity"),
        make_option("-i", "--drought",
                    dest="drought",
                    help=u"Drought index"),
        make_option("-n", "--rain",
                    dest="rain",
                    help=u"Time rain"),  
        make_option("-p", "--precipitation",
                    dest="precipitation",
                    help=u"Precipittion"),
                                                                       
    )
    def handle(self, *args, **options):
     #   from journal.models.models import Issue
      #  translation.activate('ru')
        t = options["temperature"]
        u = options["humidity"]
        i = options["drought"]
        n = options["rain"]
        p = options["precipitation"]
        
        d = ((Decimal('0.191')) * (Decimal(i) + Decimal('104')) * (Decimal(n) + Decimal('1'))**(Decimal('1.5'))) / (Decimal('3.5')*(Decimal(n) + Decimal('1'))**(Decimal('1.5')) + Decimal(p) - Decimal('1'))
     #   d = (Decimal('0.191') * (Decimal(i) + Decimal('104')) * (Decimal(n) + Decimal('1'))**(Decimal('1.5'))) / (Decimal('3.5') * (Decimal(n) + Decimal(1'))**(Decimal('1.5')) + Decimal(P) - Decimal('1'))
        
        print d
