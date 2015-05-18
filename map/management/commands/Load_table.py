import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from litres.tasks import *
from django.utils import translation

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-f", "--file",
                    dest="file",
                    help=u"File"),
    )
    def handle(self, *args, **options):
        from journal.models.models import Issue
        translation.activate('ru')
        filename = options["file"]
        logger.error("Start with %s" % filename)
        with open(filename) as f:
            #import pdb; pdb.set_trace()
            for line in f:
                print line
                f = line.replace('\n','')
                i = Issue.objects.get(uuid_key=str(f))
                print i.name
                #litres_ftpexport(i.pk)
                #litres_create_year(i.id)
                #litres_create_issue(i.id)
                #litres_loadpdf(i.id)
                #litres_upload_cover(i.id)

                litres_create_journal(i.journal.id)
                litres_create_year(i.id)
                litres_create_issue(i.id)
                litres_ftpexport(i.id)
                litres_loadpdf(i.id)
                litres_upload_cover(i.id)
        logger.error("Done")
