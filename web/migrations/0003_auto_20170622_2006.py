# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170622_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='sort_order',
            field=models.BooleanField(verbose_name='Destacada'),
        ),
    ]