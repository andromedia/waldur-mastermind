# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import nodeconductor.core.fields
import nodeconductor.core.validators
import nodeconductor.structure.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('structure', '0052_customer_subnets'),
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('name', models.CharField(max_length=150, validators=[nodeconductor.core.validators.validate_name], verbose_name='name')),
                ('uuid', nodeconductor.core.fields.UUIDField()),
                ('state', models.CharField(choices=[('requested', 'Requested'), ('responded', 'Responded'), ('active', 'Active'), ('cancelled', 'Cancelled'), ('finished', 'Finished')], default='requested', max_length=30)),
                ('type', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, help_text='The user which has created this request.')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(nodeconductor.structure.models.StructureLoggableMixin, models.Model),
        ),
    ]
