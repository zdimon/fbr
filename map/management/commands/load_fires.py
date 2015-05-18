# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

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
        #LitresDownloaded.objects.all().delete()
        for l in open(path).readlines():
            print 'process.....%s' % l
            array = l.split(',')
            print array[0]
         
