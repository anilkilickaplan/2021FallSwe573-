# Generated by Django 2.2.24 on 2021-12-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0002_auto_20211209_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
