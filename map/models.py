from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from colorful.fields import RGBColorField
from django.utils.safestring import mark_safe
from datetime import date

class Cotter(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    veg_key = models.IntegerField(_(u'Veg key'))
    veg_types = models.IntegerField(_(u'Veg key'))
    geom = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return 'Vegetation_ #%s  (%s)' % (self.gid,self.veg_types)

    class Meta:
        verbose_name=_(u'Vegetation')
        verbose_name_plural=_(u'Vegeobjects = models.GeoManager()tation')


class Structure(models.Model):
    structure = models.CharField(_(u'Structure'), max_length=25, null=True, blank=True, default='')
    fuel_moisture = models.CharField(_(u'Fuel moisture'), max_length=25, null=True, blank=True)
    fuel_load = models.CharField(_(u'Fuel load'), max_length=25, null=True, blank=True)
    litter = models.DecimalField(_(u'Litter before burning'), max_digits=6, decimal_places=2, null=True, blank=True)
    color = RGBColorField()
    def __unicode__(self):
  #      return '%s  (%s)' % (self.structure,self.fuel_moisture)
        return '%s' % (self.structure)
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
    objects = models.GeoManager()
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
    objects = models.GeoManager()
    def __unicode__(self):
        return 'Vegetation_ #%s  (%s)' % (self.gid,self.veg_sp_1)

    class Meta:
        verbose_name=_(u'Vegetation')
        verbose_name_plural=_(u'Vegetation')



        


class Slope(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    id = models.IntegerField(_(u'Id'))
    gridcode = models.IntegerField(_(u'Grid code'))
    effectiveness = models.DecimalField(_(u'Burning effectiveness'), max_digits=10, decimal_places=3, null=True, blank=True)
    geom = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()
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
    objects = models.GeoManager()
    def __unicode__(self):
#        return 'Radiation #%s' % self.gridcode
        return u'id - %s gridcode - %s' % (self.id, self.gridcode)
    

    class Meta:
        verbose_name=_(u'Radiation')
        verbose_name_plural=_(u'Radiation')
        
        
        
        
        
class Direction(models.Model):
    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
    direction = models.CharField(_(u'Direction'), max_length=20, null=True, blank=True)
    def __unicode__(self):
#        return 'Radiation #%s' % self.gridcode
        return u'id - %s gridcode - %s' % (self.gid, self.direction)
    

    class Meta:
        verbose_name=_(u'Direction')
        verbose_name_plural=_(u'Directions')        
        
        
       
        
        
#class Fires(models.Model):
#    gid = models.IntegerField(_(u'Primary key'), db_index=True, primary_key=True)
#    plot_name = models.CharField(_(u'Plot name'), max_length=10, null=True, blank=True)
#    tsf = models.CharField(_(u'TSF'), max_length=4, null=True, blank=True)
#    struct = models.ForeignKey(Structure, null=True, blank=True, verbose_name='structure')
#    tree_density = models.CharField(_(u'Tree density'), max_length=250, null=True, blank=True)
#    twi = models.CharField(_(u'TWI'), max_length=250, null=True, blank=True)
#    litter = models.CharField(_(u'Litter (t/ha)'), max_length=250,  null=True, blank=True)
#    cwd = models.CharField(_(u'CWD'), max_length=250, null=True, blank=True)
#    fuel_hazard = models.CharField(_(u'Fuel hazard'), max_length=250, null=True, blank=True)
#    fuel_moisture = models.CharField(_(u'Fuel moisture'), max_length=250,  null=True, blank=True)
#    fire_date = models.CharField(_(u'Date time'), max_length=250, null=True, blank=True)
  #  ndvi = models.MultiPolygonField(null=True, blank=True)
#    slope_degree = models.CharField(_(u'Slope degree'), max_length=250,  null=True, blank=True)
#    aspect = models.CharField(_(u'Aspect'), max_length=250, null=True, blank=True)
#    elevation = models.CharField(_(u'Elevation'), max_length=250,  null=True, blank=True)
#    radiation = models.CharField(_(u'Radiatihttp://hntu.com.ua:8008/admin/map/structure/on'), max_length=250, null=True, blank=True)
#    
#    fuel_type = models.CharField(_(u'Fuel type'), max_length=250, null=True, blank=True)
#    lai_over = models.CharField(_(u'LAI over'), max_length=250,  null=True, blank=True)
#    lai_under = models.CharField(_(u'LAI under'), max_length=250, null=True, blank=True)
    
#    def __unicode__(self):
#        return 'Fires_ #%s  (%s)' % (self.gid,self.plot_name)

#    class Meta:
#        verbose_name=_(u'Fire')
#        verbose_name_plural=_(u'Fires')
        
