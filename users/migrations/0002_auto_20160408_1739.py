# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminacc', '0002_announcements'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=100)),
                ('question', models.ForeignKey(to='adminacc.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='pollquestion',
            name='user',
            field=models.ForeignKey(to='users.User'),
        ),
    ]
