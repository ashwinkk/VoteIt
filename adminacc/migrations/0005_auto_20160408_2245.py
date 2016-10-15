# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminacc', '0004_question_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='annid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
