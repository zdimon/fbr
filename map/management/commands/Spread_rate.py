# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
#from litres.tasks import *
from django.utils import translation

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-t", "--temperature",
                    dest="temperature",
                    help=u"Air temperature"),
  #      make_option("-e", "--dateend",
   #                 dest="date_end",
    #                help=u"Start end"),
    )
    def handle(self, *args, **options):
     #   from journal.models.models import Issue
      #  translation.activate('ru')
        temperature = options["temperature"]
      #  date_end = options["date_end"]
      #  logger.error("Start from %s to %s" % (date_start, date_end))
     #   for i in Issue.objects.filter(is_public=True, release_date__lte=date_end, release_date__gte=date_start):
      #      if i.journal.is_export_to_litres:
       #         litres_create_journal(i.journal.id)
        #        litres_create_year(i.id)
         #       litres_create_issue(i.id)
          #      litres_ftpexport(i.id)
           #     litres_loadpdf(i.id)
            #    litres_upload_cover(i.id)
     #   logger.error("Done")
        print temperature
