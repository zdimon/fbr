from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

class Cotter(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    veg_key = models.IntegerField(_(u'Veg key'))
    veg_types = models.IntegerField(_(u'Veg key'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Vegetation_ #%s  (%s)' % (self.gid,self.veg_types)

    class Meta:
        verbose_name=_(u'Vegetation')
        verbose_name_plural=_(u'Vegetation')


class Vegetation(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    objectid = models.IntegerField(_(u'Objectid'))
    area = models.DecimalField(_(u'Area'), max_digits=15, decimal_places=3, null=True, blanc=True)
    perimeter = models.DecimalField(_(u'Perimeter'), max_digits=25, decimal_places=15, null=True, blanc=True)
    veg_ = models.DecimalField(_(u'Veg'), max_digits=10, decimal_places=5, null=True, blanc=True)
    veg_id = models.DecimalField(_(u'Veg'), max_digits=10, decimal_places=5, null=True, blanc=True)
    veg_sp_1 = models.CharField(_(u'Veg_sp_1'), max_kength=25, null=True, blanc=True)
    veg_sp_2 = models.CharField(_(u'Veg_sp_1'), max_kength=25, null=True, blanc=True)
    veg_sp_3 = models.CharField(_(u'Veg_sp_1'), max_kength=25, null=True, blanc=True) 
    structure = models.CharField(_(u'Veg_sp_1'), max_kength=20, null=True, blanc=True)
    class1 = models.IntegerField(_(u'Class'), null=True, blanc=True)
    symbol = models.DecimalField(_(u'Symbol'), max_digits=20, decimal_places=15, null=True, blanc=True)
    state = models.CharField(_(u'State'), max_kength=6, null=True, blanc=True)
    fueltype = models.IntegerField(_(u'Fuel type'), null=True, blanc=True)
    fuelcode_v = models.CharField(_(u'Fuel code'), max_kength=50, null=True, blanc=True)
    acres = models.DecimalField(_(u'Acres'), max_digits=20, decimal_places=15, null=True, blanc=True)
    hectares = models.DecimalField(_(u'Hectares'), max_digits=25, decimal_places=15, null=True, blanc=True)      
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Vegetation_ #%s  (%s)' % (self.gid,self.veg_sp_1)

    class Meta:
        verbose_name=_(u'Vegetation')
        verbose_name_plural=_(u'Vegetation')
        


class Slope(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    id = models.IntegerField(_(u'Id'))
    gridcode = models.IntegerField(_(u'Grid code'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
    #    return 'Slope #%s' % self.gridcode
        return u'id - %s gridcode - %s' % (self.id, self.gridcode)

    class Meta:
        verbose_name=_(u'Slope')
        verbose_name_plural=_(u'Slope')


class Radiation(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    id = models.IntegerField(_(u'Id'))
    gridcode = models.IntegerField(_(u'Grid code'))
    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
#        return 'Radiation #%s' % self.gridcode
        return u'id - %s gridcode - %s' % (self.id, self.gridcode)

    class Meta:
        verbose_name=_(u'Radiation')
        verbose_name_plural=_(u'Radiation')
