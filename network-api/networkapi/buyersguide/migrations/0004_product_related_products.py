# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-27 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0003_auto_20180927_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(null=True, related_name='rps', to='buyersguide.Update'),
        ),
    ]