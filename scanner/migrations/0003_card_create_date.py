# Generated by Django 3.0.6 on 2020-05-12 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_card_source_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 7, 42, 33, 438503)),
        ),
    ]