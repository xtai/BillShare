# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='action',
        ),
        migrations.AlterField(
            model_name='record',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver'),
        ),
    ]
