# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vegetation'
        db.create_table(u'map_vegetation', (
            ('gid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_index=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=3, blank=True)),
            ('perimeter', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=25, decimal_places=15, blank=True)),
            ('veg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5, blank=True)),
            ('veg_id', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5, blank=True)),
            ('veg_sp_1', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('veg_sp_2', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('veg_sp_3', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('class1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('symbol', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=15, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('fueltype', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fuelcode_v', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('acres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=15, blank=True)),
            ('hectares', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=25, decimal_places=15, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'map', ['Vegetation'])


    def backwards(self, orm):
        # Deleting model 'Vegetation'
        db.delete_table(u'map_vegetation')


    models = {
        u'map.cotter': {
            'Meta': {'object_name': 'Cotter'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'veg_key': ('django.db.models.fields.IntegerField', [], {}),
            'veg_types': ('django.db.models.fields.IntegerField', [], {})
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
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '15', 'blank': 'True'}),
            'veg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_id': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_sp_1': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_2': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_3': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['map']