# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SemFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name=b'Current Year')),
                ('dasa', models.IntegerField(verbose_name=b'DASA/SAARC Fees')),
                ('daysch', models.IntegerField(verbose_name=b'Day-Scholar Fees')),
                ('hostel', models.IntegerField(verbose_name=b'Hosteller Fees')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rno', models.IntegerField(verbose_name=b'JEE(Main) Roll No.')),
                ('rank', models.IntegerField(verbose_name=b'JEE(Main) Rank')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
