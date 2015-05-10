from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

class Cotter(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    veg_key = models.IntegerField(_(u'Veg key'))
    veg_types = models.IntegerField(_(u'Veg key'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Cotter #%s  (%s)' % (self.gid,self.veg_types)

    class Meta:
        verbose_name=_(u'Cotter')
        verbose_name_plural=_(u'Cotters')


class Slope(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    id = models.IntegerField(_(u'Id'))
    gridcode = models.IntegerField(_(u'Grid code'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Slope #%s' % self.gridcode

    class Meta:
        verbose_name=_(u'Slope')
        verbose_name_plural=_(u'Slope')


class Radiation(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    id = models.IntegerField(_(u'Id'))
    gridcode = models.IntegerField(_(u'Grid code'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Radiation #%s' % self.gridcode
#        return u'%s %s' % (self.id, self.gridcode)

    class Meta:
        verbose_name=_(u'Radiation')
        verbose_name_plural=_(u'Radiation')
