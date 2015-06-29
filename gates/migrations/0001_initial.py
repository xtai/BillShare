# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(max_length=200)),
                ('action', models.CharField(choices=[('F', 'Pay for'), ('T', 'Pay to'), ('S', 'Split')], max_length=1)),
                ('record_date', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(to='gates.Project')),
                ('payer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='payer')),
                ('receiver', models.ForeignKey(blank=True, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
