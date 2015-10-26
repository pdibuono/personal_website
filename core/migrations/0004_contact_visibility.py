# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151022_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Ms.'), (2, b'Mrs.'), (3, b'Mr'), (4, b'Dr.')]),
        ),
    ]
