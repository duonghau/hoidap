# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follow_tags'),
        ('messenger', '0004_auto_20150826_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='participants',
        ),
        migrations.AddField(
            model_name='conversation',
            name='user_one',
            field=models.ForeignKey(related_name='user_ones', to='accounts.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user_two',
            field=models.ForeignKey(related_name='user_twos', to='accounts.UserProfile', null=True),
        ),
    ]
