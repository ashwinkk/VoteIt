# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160408_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClUser',
            fields=[
                ('uname', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('pword', models.CharField(max_length=40)),
                ('voters_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pollquestion',
            name='user',
            field=models.ForeignKey(to='users.ClUser'),
        ),
        migrations.DeleteModel(
            name='CUser',
        ),
    ]
