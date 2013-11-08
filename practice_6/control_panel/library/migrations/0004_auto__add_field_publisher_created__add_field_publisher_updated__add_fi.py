# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publisher.created'
        db.add_column(u'library_publisher', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Publisher.updated'
        db.add_column(u'library_publisher', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'BooksImage.created'
        db.add_column(u'library_booksimage', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'BooksImage.updated'
        db.add_column(u'library_booksimage', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.created'
        db.add_column(u'library_book', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.updated'
        db.add_column(u'library_book', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Author.created'
        db.add_column(u'library_author', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Author.updated'
        db.add_column(u'library_author', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 11, 7, 0, 0), db_index=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Publisher.created'
        db.delete_column(u'library_publisher', 'created')

        # Deleting field 'Publisher.updated'
        db.delete_column(u'library_publisher', 'updated')

        # Deleting field 'BooksImage.created'
        db.delete_column(u'library_booksimage', 'created')

        # Deleting field 'BooksImage.updated'
        db.delete_column(u'library_booksimage', 'updated')

        # Deleting field 'Book.created'
        db.delete_column(u'library_book', 'created')

        # Deleting field 'Book.updated'
        db.delete_column(u'library_book', 'updated')

        # Deleting field 'Author.created'
        db.delete_column(u'library_author', 'created')

        # Deleting field 'Author.updated'
        db.delete_column(u'library_author', 'updated')

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        u'library.booksimage': {
            'Meta': {'object_name': 'BooksImage'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'small_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'zoomed_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['library']
