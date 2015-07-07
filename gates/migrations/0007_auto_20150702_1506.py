# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0006_auto_20150702_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='last_change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
