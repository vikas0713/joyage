# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to=b'static/uploads/')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('website', models.URLField()),
                ('neighbourhood', models.TextField()),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
