# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160408_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='option',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
