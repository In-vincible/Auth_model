# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-06 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='features',
            fields=[
                ('feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('feature_name', models.CharField(max_length=50)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='modules',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=50)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.AddField(
            model_name='features',
            name='feature_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_app.modules'),
        ),
    ]
