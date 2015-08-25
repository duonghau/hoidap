# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 25, 10, 7, 54, 173613, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
