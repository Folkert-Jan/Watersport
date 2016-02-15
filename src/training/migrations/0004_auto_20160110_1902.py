# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20160110_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingen',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='trainingen',
            name='updated',
        ),
        migrations.AlterField(
            model_name='trainingen',
            name='Datum',
            field=models.CharField(max_length=120, verbose_name=b'Datum'),
        ),
        migrations.AlterField(
            model_name='trainingen',
            name='Klasse',
            field=models.CharField(max_length=120, verbose_name=b'Klasse'),
        ),
        migrations.AlterField(
            model_name='trainingen',
            name='Locatie',
            field=models.CharField(max_length=120, verbose_name=b'Locatie'),
        ),
    ]
