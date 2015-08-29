# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follow_tags'),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagereadstate',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagereadstate',
            name='user',
        ),
        migrations.AddField(
            model_name='conversation',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 7, 56, 33, 534525, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='messages', to='accounts.UserProfile', null=True),
        ),
        migrations.DeleteModel(
            name='MessageReadState',
        ),
    ]
