# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0005_auto_20150701_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='last_change_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
