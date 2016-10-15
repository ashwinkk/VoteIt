# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('polls', models.CharField(max_length=500, blank=True)),
                ('activity', models.IntegerField(default=0)),
            ],
        ),
    ]
