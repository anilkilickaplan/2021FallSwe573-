# Generated by Django 2.2.24 on 2022-01-02 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0023_auto_20220102_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='userratings',
            name='ratingDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
