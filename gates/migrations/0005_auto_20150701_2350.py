# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gates', '0004_auto_20150629_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField()),
                ('last_change_date', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.AlterField(
            model_name='record',
            name='group',
            field=models.ForeignKey(to='gates.Group'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
