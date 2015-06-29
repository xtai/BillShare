# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0003_auto_20150629_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='record_date',
            new_name='last_change_date',
        ),
        migrations.AddField(
            model_name='project',
            name='last_change_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 3, 45, 36, 760281, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 3, 45, 39, 968326, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
