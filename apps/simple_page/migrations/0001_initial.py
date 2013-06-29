# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'simple_page_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'simple_page', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'simple_page_video')


    models = {
        u'simple_page.video': {
            'Meta': {'ordering': "('show',)", 'object_name': 'Video'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['simple_page']