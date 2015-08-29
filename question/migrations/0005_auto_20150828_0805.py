# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20150825_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='rank',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='rank',
            field=models.FloatField(default=0),
        ),
    ]
