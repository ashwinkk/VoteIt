# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminacc', '0003_auto_20160408_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
