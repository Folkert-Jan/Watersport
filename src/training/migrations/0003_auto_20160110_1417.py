# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20160110_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingen',
            name='Klasse',
            field=models.CharField(max_length=120, verbose_name=b'full name'),
        ),
    ]
