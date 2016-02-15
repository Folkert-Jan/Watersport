# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_trainingen_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingen',
            name='Info',
        ),
        migrations.AlterField(
            model_name='trainingen',
            name='Klasse',
            field=models.CharField(max_length=1, choices=[(b'O', b'Optimist'), (b'S', b'Splash'), (b'L', b'Laser'), (b'F', b'Rs Feva'), (b'5', b'Rs 500'), (b'2', b'29er')]),
        ),
    ]
