# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0003_auto_20170701_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info_contacto',
            name='timestamp',
        ),
    ]
