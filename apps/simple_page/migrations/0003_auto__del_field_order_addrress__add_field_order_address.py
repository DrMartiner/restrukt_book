# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Order.addrress'
        db.delete_column(u'simple_page_order', 'addrress')

        # Adding field 'Order.address'
        db.add_column(u'simple_page_order', 'address',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=246),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Order.addrress'
        db.add_column(u'simple_page_order', 'addrress',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=246),
                      keep_default=False)

        # Deleting field 'Order.address'
        db.delete_column(u'simple_page_order', 'address')


    models = {
        u'pay2pay.payment': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'RUB'", 'max_length': '8'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512'}),
            'error_msg': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2669'}),
            'order_id': ('django.db.models.fields.CharField', [], {'default': "'317c5257-f31f-4c'", 'max_length': '16'}),
            'paymode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'test_mode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trans_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.3'", 'max_length': '8'})
        },
        u'simple_page.order': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Order'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '246'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pay2pay.Payment']", 'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'simple_page.video': {
            'Meta': {'ordering': "('show',)", 'object_name': 'Video'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['simple_page']