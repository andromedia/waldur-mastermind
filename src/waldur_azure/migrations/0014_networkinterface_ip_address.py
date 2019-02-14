# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waldur_azure', '0013_publicip_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkinterface',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, default=None, null=True, protocol='IPv4'),
        ),
    ]