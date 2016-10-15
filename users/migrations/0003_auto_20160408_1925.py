# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160408_1739'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='ClientUser',
        ),
    ]
