# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150419_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='insufee',
            field=models.IntegerField(null=True, verbose_name='Group Insturance Coverage of Students', blank=True),
            preserve_default=True,
        ),
    ]
