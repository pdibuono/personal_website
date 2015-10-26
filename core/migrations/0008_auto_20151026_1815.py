# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151026_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
