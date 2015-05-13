# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vegetation.structure'
        db.add_column(u'map_vegetation', 'structure',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Structure'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vegetation.structure'
        db.delete_column(u'map_vegetation', 'structure_id')


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
        u'map.structure': {
            'Meta': {'object_name': 'Structure'},
            'fuel_load': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'fuel_moisture': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'})
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
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Structure']", 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '15', 'blank': 'True'}),
            'veg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_id': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'veg_sp_1': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_2': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'veg_sp_3': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['map']