# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_auto_20150419_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='semfee',
            name='dasa',
            field=models.IntegerField(null=True, verbose_name=b'Dasa Fee', blank=True),
            preserve_default=True,
        ),
    ]
