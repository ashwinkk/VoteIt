# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160408_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='option',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
