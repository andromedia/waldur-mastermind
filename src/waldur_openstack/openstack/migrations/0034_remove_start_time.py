# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-10 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0033_remove_openstackservice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floatingip',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='network',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='securitygroup',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='subnet',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='start_time',
        ),
    ]
