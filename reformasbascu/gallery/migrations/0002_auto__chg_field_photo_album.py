# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.album'
        db.alter_column(u'gallery_photo', 'album_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], null=True))

    def backwards(self, orm):

        # Changing field 'Photo.album'
        db.alter_column(u'gallery_photo', 'album_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Album']))

    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'gallery.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['gallery']