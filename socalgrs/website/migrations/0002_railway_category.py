# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='railway',
            name='category',
            field=models.CharField(blank=True, choices=[('garden', 'Garden Layouts'), ('public', 'Public Displays'), ('archive', 'Archive')], max_length=100),
        ),
    ]