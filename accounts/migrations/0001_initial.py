# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(max_length=100, blank=True)),
                ('avatar', models.ImageField(upload_to=accounts.models.get_profile_url, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('birthday', models.DateField(null=True)),
                ('gender', models.CharField(blank=True, max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('bio', models.TextField(blank=True)),
                ('rank', models.FloatField(default=0)),
                ('follows_count', models.IntegerField(default=0)),
                ('followers_count', models.IntegerField(default=0)),
                ('follows', models.ManyToManyField(related_name='followers', to='accounts.UserProfile', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
