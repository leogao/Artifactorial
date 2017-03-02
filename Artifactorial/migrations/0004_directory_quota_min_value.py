# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 13:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artifactorial', '0003_make_directory_path_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='quota',
            field=models.BigIntegerField(default=1073741824, help_text='Size limit in Bytes', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
