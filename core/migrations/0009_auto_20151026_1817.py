# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151026_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='Last_Name',
        ),
    ]
