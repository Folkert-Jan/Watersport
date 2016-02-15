# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_auto_20160215_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingen',
            name='Klasse',
            field=models.CharField(max_length=3, choices=[(b'Opt', b'Optimist'), (b'Sps', b'Splash'), (b'Lsr', b'Laser'), (b'Fv', b'Rs Feva'), (b'500', b'Rs 500'), (b'29', b'29er')]),
        ),
    ]
