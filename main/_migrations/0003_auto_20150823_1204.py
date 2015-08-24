# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_speedmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedmodel',
            name='down_votes',
            field=models.ManyToManyField(related_name='down_votes', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='up_votes',
            field=models.ManyToManyField(related_name='up_votes', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
