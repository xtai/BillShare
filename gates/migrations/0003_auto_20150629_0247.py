# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0002_auto_20150629_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='note',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
