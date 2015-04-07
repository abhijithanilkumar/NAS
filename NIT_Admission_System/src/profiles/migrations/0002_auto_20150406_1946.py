# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(default='NC', max_length=200, verbose_name='Branch Chosen', choices=[('NC', 'Not Chosen'), ('CH', 'Chemical Engineering'), ('CO', 'Computer Engineering'), ('CV', 'Civil Engineering'), ('EC', 'Electronics and Communications Engineering'), ('EE', 'Elelctrical and Electronics Engineering'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('MN', 'Mining Engineering'), ('MT', 'Materials and Metallurgical Engineering')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(default='GH', max_length=30, verbose_name='Student Category', choices=[('GD', 'Day Scholar'), ('GH', 'Hosteller'), ('DA', 'DASA/SAARC')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='fees',
            field=models.IntegerField(default=0, verbose_name='HostelFees'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='JEE(Main) Rank'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='rno',
            field=models.IntegerField(default=0, verbose_name='JEE(Main) Roll No.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email Verified'),
            preserve_default=True,
        ),
    ]
