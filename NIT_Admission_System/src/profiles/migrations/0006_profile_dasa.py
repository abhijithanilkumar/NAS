# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_challan'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dasa',
            field=models.IntegerField(null=True, verbose_name='Dasa Fee', blank=True),
            preserve_default=True,
        ),
    ]
