# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0007_offering_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='product_code',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
