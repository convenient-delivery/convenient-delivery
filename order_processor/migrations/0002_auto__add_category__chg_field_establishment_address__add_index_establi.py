# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'order_processor_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'order_processor', ['Category'])


        # Renaming column for 'Establishment.address' to match new field type.
        db.rename_column(u'order_processor_establishment', 'address', 'address_id')
        # Changing field 'Establishment.address'
        db.alter_column(u'order_processor_establishment', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order_processor.Address'], null=True))
        # Adding index on 'Establishment', fields ['address']
        db.create_index(u'order_processor_establishment', ['address_id'])


    def backwards(self, orm):
        # Removing index on 'Establishment', fields ['address']
        db.delete_index(u'order_processor_establishment', ['address_id'])

        # Deleting model 'Category'
        db.delete_table(u'order_processor_category')


        # User chose to not deal with backwards NULL issues for 'Establishment.address'
        raise RuntimeError("Cannot reverse this migration. 'Establishment.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Renaming column for 'Establishment.address' to match new field type.
        db.rename_column(u'order_processor_establishment', 'address_id', 'address')
        # Changing field 'Establishment.address'
        db.alter_column(u'order_processor_establishment', 'address', self.gf('django.db.models.fields.TextField')(max_length=255))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'order_processor.address': {
            'Meta': {'object_name': 'Address'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'order_processor.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'order_processor.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'currently_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'order_processor.driver': {
            'Meta': {'object_name': 'Driver'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.City']"}),
            'currently_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'order_processor.establishment': {
            'Meta': {'object_name': 'Establishment'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.Address']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'order_processor.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'establishment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.Establishment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'order_processor.order': {
            'Meta': {'object_name': 'Order'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.City']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.Driver']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.TextField', [], {}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.Profile']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'q'", 'max_length': '255'}),
            'work_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'order_processor.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.Address']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'order_processor.saleitem': {
            'Meta': {'object_name': 'SaleItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['order_processor.ItemCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '2'})
        }
    }

    complete_apps = ['order_processor']