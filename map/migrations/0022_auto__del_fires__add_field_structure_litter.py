# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Fires'
        #db.delete_table(u'map_fires')

        # Adding field 'Structure.litter'
        db.add_column(u'map_structure', 'litter',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Fires'
        db.create_table(u'map_fires', (
            ('fuel_hazard', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('elevation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('struct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Structure'], null=True, blank=True)),
            ('fire_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tsf', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('radiation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('fuel_type', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('twi', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('fuel_moisture', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('ndvi', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('plot_name', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('litter', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('aspect', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('lai_over', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('lai_under', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('gid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_index=True)),
            ('slope_degree', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('cwd', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
            ('tree_density', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=10, blank=True)),
        ))
        db.send_create_signal(u'map', ['Fires'])

        # Deleting field 'Structure.litter'
        db.delete_column(u'map_structure', 'litter')


    models = {
        u'map.cotter': {
            'Meta': {'object_name': 'Cotter'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'veg_key': ('django.db.models.fields.IntegerField', [], {}),
            'veg_types': ('django.db.models.fields.IntegerField', [], {})
        },
        u'map.direction': {
            'Meta': {'object_name': 'Direction'},
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'})
        },
        u'map.radiation': {
            'Meta': {'object_name': 'Radiation'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'gridcode': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'map.slope': {
            'Meta': {'object_name': 'Slope'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'gridcode': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'map.structure': {
            'Meta': {'object_name': 'Structure'},
            'color': (u'colorful.fields.RGBColorField', [], {}),
            'fuel_load': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'fuel_moisture': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'litter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'map.veget': {
            'Meta': {'object_name': 'Veget'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'gridcode': ('django.db.models.fields.IntegerField', [], {}),
            'struct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Structure']", 'null': 'True', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'map.vegetation': {
            'Meta': {'object_name': 'Vegetation'},
            'acres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '15', 'blank': 'True'}),
            'area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '3', 'blank': 'True'}),
            'class1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuelcode_v': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fueltype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'hectares': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '25', 'decimal_places': '15', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {}),
            'perimeter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '25', 'decimal_places': '15', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'struct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Structure']", 'null': 'True', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '15', 'blank': 'True'}),
            'veg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_id': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_sp_1': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_2': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_3': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['map']
