# Generated by Django 2.2.24 on 2021-11-28 21:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('userName', models.CharField(blank=True, max_length=30, null=True)),
                ('userBio', models.TextField(blank=True, max_length=500, null=True)),
                ('userBirthDate', models.DateField(blank=True, null=True)),
                ('userLocation', models.CharField(blank=True, max_length=100, null=True)),
                ('userCredits', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerCreatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('offerDescription', models.TextField()),
                ('offerName', models.TextField()),
                ('offerDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('offerLocation', models.CharField(blank=True, max_length=100, null=True)),
                ('offerCapacity', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(100)])),
                ('offerIsActive', models.BooleanField(default=True)),
                ('offerOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyClub.Offer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventCreatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventName', models.TextField()),
                ('eventDescription', models.TextField()),
                ('eventLocation', models.CharField(blank=True, max_length=100, null=True)),
                ('eventDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventCapacity', models.IntegerField()),
                ('eventIsActive', models.BooleanField(default=True)),
                ('eventOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
