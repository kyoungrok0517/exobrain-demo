# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_tripple'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=1024)),
                ('text', models.CharField(max_length=1024)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='web.Question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerTriple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=1024)),
                ('text', models.CharField(max_length=1024)),
                ('score', models.FloatField(default=0.0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_triples', to='web.Question')),
            ],
        ),
    ]
