# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob', '0005_auto_20171111_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lottery_month', models.CharField(max_length=100)),
                ('lottery_date', models.CharField(max_length=100)),
                ('lottery_time', models.CharField(max_length=100)),
                ('lottery_id', models.IntegerField()),
                ('lottery_number', models.CharField(max_length=500)),
            ],
        ),
    ]
