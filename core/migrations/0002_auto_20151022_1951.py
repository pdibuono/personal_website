# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
