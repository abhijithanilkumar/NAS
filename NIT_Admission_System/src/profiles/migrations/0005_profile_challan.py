# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150419_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='challan',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Challan', blank=True),
            preserve_default=True,
        ),
    ]
