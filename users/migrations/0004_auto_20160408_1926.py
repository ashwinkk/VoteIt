# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160408_1925'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientUser',
            new_name='CUser',
        ),
    ]
