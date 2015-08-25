# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_follow_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('participants', models.ManyToManyField(related_name='user_conversations', to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('create', models.DateTimeField(auto_now=True)),
                ('conversation', models.ForeignKey(related_name='conversation_messages', to='messenger.Conversation')),
                ('sender', models.ForeignKey(to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MessageReadState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read_time', models.DateTimeField(null=True)),
                ('message', models.ForeignKey(to='messenger.Message')),
                ('user', models.ForeignKey(related_name='user_messages_state', to='accounts.UserProfile')),
            ],
        ),
    ]
