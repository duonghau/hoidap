# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20150823_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
    ]
