# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmanual',
            name='equipment',
            field=models.ForeignKey(help_text='equipment this manual is for', on_delete=django.db.models.deletion.CASCADE, to='equipment.HackerEquipment'),
        ),
        migrations.AlterField(
            model_name='trainingmanual',
            name='notes',
            field=models.TextField(blank=True, default='', help_text='optional notes'),
            preserve_default=False,
        ),
    ]
