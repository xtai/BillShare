# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0007_auto_20150702_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
