# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-12 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MILK', '0018_auto_20170312_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='payeeID',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='requestID',
        ),
    ]
