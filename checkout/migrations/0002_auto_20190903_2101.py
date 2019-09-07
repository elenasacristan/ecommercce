# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-03 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_add1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_add2',
            new_name='street_address2',
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(max_length=40),
        ),
    ]