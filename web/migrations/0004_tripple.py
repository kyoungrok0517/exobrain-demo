# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170823_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tripple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(default='', max_length=1024)),
                ('subject_text', models.CharField(default='', max_length=1024)),
                ('subject_id', models.CharField(default='', max_length=1024)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripples', to='web.Question')),
            ],
        ),
    ]
