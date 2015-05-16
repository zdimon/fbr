from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from colorful.fields import RGBColorField
from django.utils.safestring import mark_safe

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


class Structure(models.Model):
    structure = models.CharField(_(u'Structure'), max_length=25, null=True, blank=True, default='')
    fuel_moisture = models.CharField(_(u'Fuel moisture'), max_length=25, null=True, blank=True)
    fuel_load = models.CharField(_(u'Fuel load'), max_length=25, null=True, blank=True)
    color = RGBColorField()
    def __unicode__(self):
        return '%s  (%s)' % (self.structure,self.fuel_moisture)
    @property
    def color_repr(self):
        return mark_safe('<div style="width: 50px; height: 50px; background-color: %s"></div>' % self.color)
    class Meta:
        verbose_name=_(u'Structure')
        verbose_name_plural=_(u'Structures')  
        
        

class Veget(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    gridcode = models.IntegerField(_(u'Gridcode'))  
    
    structure = models.CharField(_(u'Structure'), max_length=25, null=True, blank=True)
    struct = models.ForeignKey(Structure, null=True, blank=True)

    geom = models.MultiPolygonField(null=True, blank=True)
    def __unicode__(self):
        return 'Vegetation_ #%s  (%s)' % (self.gid,self.struct)

    class Meta:
        verbose_name=_(u'Vegetation structure')
        verbose_name_plural=_(u'Vegetation structures')
  
    
    

class Vegetation(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    objectid = models.IntegerField(_(u'Objectid'))
    area = models.DecimalField(_(u'Area'), max_digits=15, decimal_places=3, null=True, blank=True)
    perimeter = models.DecimalField(_(u'Perimeter'), max_digits=25, decimal_places=15, null=True, blank=True)
    veg = models.DecimalField(_(u'Veg'), max_digits=10, decimal_places=5, null=True, blank=True)
    veg_id = models.DecimalField(_(u'Veg_id'), max_digits=10, decimal_places=5, null=True, blank=True)
    veg_sp_1 = models.CharField(_(u'Veg_sp_1'), max_length=25, null=True, blank=True)
    veg_sp_2 = models.CharField(_(u'Veg_sp_2'), max_length=25, null=True, blank=True)
    veg_sp_3 = models.CharField(_(u'Veg_sp_3'), max_length=25, null=True, blank=True) 
    
    structure = models.CharField(_(u'Structure'), max_length=25, null=True, blank=True)
    struct = models.ForeignKey(Structure, null=True, blank=True, verbose_name='structure')

    
    class1 = models.IntegerField(_(u'Class'), null=True, blank=True)
    symbol = models.DecimalField(_(u'Symbol'), max_digits=20, decimal_places=15, null=True, blank=True)
    state = models.CharField(_(u'State'), max_length=6, null=True, blank=True)
    fueltype = models.IntegerField(_(u'Fuel type'), null=True, blank=True)
    fuelcode_v = models.CharField(_(u'Fuel code'), max_length=50, null=True, blank=True)
    acres = models.DecimalField(_(u'Acres'), max_digits=20, decimal_places=15, null=True, blank=True)
    hectares = models.DecimalField(_(u'Hectares'), max_digits=25, decimal_places=15, null=True, blank=True)      
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
