# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semfee',
            name='dasa',
        ),
        migrations.RemoveField(
            model_name='semfee',
            name='daysch',
        ),
        migrations.RemoveField(
            model_name='semfee',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='semfee',
            name='year',
        ),
        migrations.AddField(
            model_name='semfee',
            name='admfee',
            field=models.IntegerField(null=True, verbose_name=b'Hostel Admission Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='alumfee',
            field=models.IntegerField(null=True, verbose_name=b'Alumni Association', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='camdevfee',
            field=models.IntegerField(null=True, verbose_name=b'Campus Development Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='cat',
            field=models.CharField(default=b'GH', max_length=30, verbose_name=b'Student Category', choices=[(b'GN', b'Gen/OBC'), (b'SC', b'SC/ST')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='cccfee',
            field=models.IntegerField(null=True, verbose_name=b'Central Computing Facility Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='convofee',
            field=models.IntegerField(null=True, verbose_name=b'Convocation Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='devfee',
            field=models.IntegerField(null=True, verbose_name=b'Institute Development Contribution', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='insufee',
            field=models.IntegerField(null=True, verbose_name=b'Group Insturance Converage of Students', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='libfee',
            field=models.IntegerField(null=True, verbose_name=b'Library Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='poolfee',
            field=models.IntegerField(null=True, verbose_name=b'Swimming Pool Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='rent',
            field=models.IntegerField(null=True, verbose_name=b'Hostel Rent', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='sacfee',
            field=models.IntegerField(null=True, verbose_name=b'Student Activities Fee', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='secfee',
            field=models.IntegerField(null=True, verbose_name=b'Security Deposit (Refundable)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semfee',
            name='tutfee',
            field=models.IntegerField(null=True, verbose_name=b'Tution Fees', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='rank',
            field=models.IntegerField(unique=True, verbose_name=b'JEE(Main) Rank'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='rno',
            field=models.IntegerField(unique=True, verbose_name=b'JEE(Main) Roll No.'),
            preserve_default=True,
        ),
    ]
