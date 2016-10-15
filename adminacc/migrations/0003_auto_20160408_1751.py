# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminacc', '0002_announcements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
