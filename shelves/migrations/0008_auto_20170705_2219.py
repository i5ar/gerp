# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0007_auto_20170705_2207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegularBin',
            new_name='Bin',
        ),
    ]
