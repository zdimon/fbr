# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass


    def backwards(self, orm):
        # Deleting model 'Cotter'
        db.delete_table(u'map_cotter')

        # Deleting model 'Slope'
        db.delete_table(u'map_slope')

        # Deleting model 'Radiation'
        db.delete_table(u'map_radiation')


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
        }
    }

    complete_apps = ['map']
