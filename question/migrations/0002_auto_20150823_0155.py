# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follow_tags'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvotes',
            field=models.ManyToManyField(related_name='user_question_downvotes', to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(related_name='user_question_votes', to='accounts.UserProfile'),
        ),
    ]
