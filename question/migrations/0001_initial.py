# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('votes_count', models.IntegerField(default=0)),
                ('downvotes_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(related_name='user_answers', to='accounts.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('votes_count', models.IntegerField(default=0)),
                ('downvotes_count', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('author', models.ForeignKey(related_name='user_questions', to='accounts.UserProfile')),
                ('tags', models.ManyToManyField(related_name='tag_questions', to='tag.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='question_answers', to='question.Question'),
        ),
    ]
