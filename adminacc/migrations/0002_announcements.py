# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminacc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('annid', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('message', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
