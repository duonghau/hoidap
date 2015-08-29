# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_auto_20150827_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
