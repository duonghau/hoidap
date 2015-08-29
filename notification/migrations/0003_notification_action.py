# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20150825_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='action',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
