# Generated by Django 4.0.4 on 2022-05-03 00:45

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(null=True, upload_to=api.models.upload_to),
        ),
    ]
