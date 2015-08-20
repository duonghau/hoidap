# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tag.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('image', models.ImageField(upload_to=tag.models.get_tags_url, blank=True)),
                ('description', models.TextField(blank=True)),
                ('questions_count', models.IntegerField(default=0)),
                ('followers_count', models.IntegerField(default=0)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
