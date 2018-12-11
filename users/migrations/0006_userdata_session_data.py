# Generated by Django 2.1.4 on 2018-12-10 10:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_anondata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='session_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]