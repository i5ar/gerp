# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0016_auto_20170706_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.IntegerField(verbose_name='Column')),
                ('row', models.IntegerField(verbose_name='Row')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelves.Container')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
        migrations.RemoveField(
            model_name='bin',
            name='shelf',
        ),
        migrations.RemoveField(
            model_name='binder',
            name='bin',
        ),
        migrations.DeleteModel(
            name='Bin',
        ),
        migrations.AddField(
            model_name='binder',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shelves.Board'),
        ),
    ]