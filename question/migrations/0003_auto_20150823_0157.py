# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follow_tags'),
        ('question', '0002_auto_20150823_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(related_name='user_answer_downvotes', to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.ManyToManyField(related_name='user_answer_votes', to='accounts.UserProfile'),
        ),
    ]
