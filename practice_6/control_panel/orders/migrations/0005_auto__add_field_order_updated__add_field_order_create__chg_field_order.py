# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.updated'
        db.add_column(u'orders_order', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.create'
        db.add_column(u'orders_order', 'create',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now),
                      keep_default=False)

        # Changing field 'Order.created'
        db.alter_column(u'orders_order', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding index on 'Order', fields ['created']
        db.create_index(u'orders_order', ['created'])

        # Adding field 'Customer.created'
        db.add_column(u'orders_customer', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Customer.updated'
        db.add_column(u'orders_customer', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Removing index on 'Order', fields ['created']
        db.delete_index(u'orders_order', ['created'])

        # Deleting field 'Order.updated'
        db.delete_column(u'orders_order', 'updated')

        # Deleting field 'Order.create'
        db.delete_column(u'orders_order', 'create')

        # Changing field 'Order.created'
        db.alter_column(u'orders_order', 'created', self.gf('django.db.models.fields.DateField')())
        # Deleting field 'Customer.created'
        db.delete_column(u'orders_customer', 'created')

        # Deleting field 'Customer.updated'
        db.delete_column(u'orders_customer', 'updated')

    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'orders.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order'},
            'create': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Customer']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']
