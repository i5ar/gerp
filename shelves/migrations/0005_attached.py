# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-01 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0004_auto_20180115_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('file', models.FileField(upload_to='docs')),
                ('binder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelves.Binder')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
    ]
