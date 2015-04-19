# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150406_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fees',
        ),
        migrations.AddField(
            model_name='profile',
            name='admfee',
            field=models.IntegerField(null=True, verbose_name='Hostel Admission Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='alumfee',
            field=models.IntegerField(null=True, verbose_name='Alumni Association', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='camdevfee',
            field=models.IntegerField(null=True, verbose_name='Campus Development Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='category2',
            field=models.CharField(default='GH', max_length=30, verbose_name='Student Category', choices=[('GD', 'Day Scholar'), ('GH', 'Hosteller'), ('DA', 'DASA/SAARC')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='cccfee',
            field=models.IntegerField(null=True, verbose_name='Central Computing Facility Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='convofee',
            field=models.IntegerField(null=True, verbose_name='Convocation Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='devfee',
            field=models.IntegerField(null=True, verbose_name='Institute Development Contribution', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='insufee',
            field=models.IntegerField(null=True, verbose_name='Group Insturance Converage of Students', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='libfee',
            field=models.IntegerField(null=True, verbose_name='Library Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='poolfee',
            field=models.IntegerField(null=True, verbose_name='Swimming Pool Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='rent',
            field=models.IntegerField(null=True, verbose_name='Hostel Rent', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='sacfee',
            field=models.IntegerField(null=True, verbose_name='Student Activities Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='secfee',
            field=models.IntegerField(null=True, verbose_name='Security Deposit (Refundable)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='totfee',
            field=models.IntegerField(null=True, verbose_name='Total Amount to be Payed', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='tutfee',
            field=models.IntegerField(null=True, verbose_name='Tution Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Branch Chosen', choices=[('NC', 'Not Chosen'), ('CH', 'Chemical Engineering'), ('CO', 'Computer Engineering'), ('CV', 'Civil Engineering'), ('EC', 'Electronics and Communications Engineering'), ('EE', 'Elelctrical and Electronics Engineering'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('MN', 'Mining Engineering'), ('MT', 'Materials and Metallurgical Engineering')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.CharField(default='GN', max_length=30, verbose_name='Category', choices=[('GN', 'Gen/OBC'), ('SC', 'SC/ST')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(null=True, verbose_name='JEE(Main) Rank', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='rno',
            field=models.IntegerField(null=True, verbose_name='JEE(Main) Roll No.', blank=True),
            preserve_default=True,
        ),
    ]
