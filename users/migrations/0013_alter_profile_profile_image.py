# Generated by Django 4.1.5 on 2023-01-11 18:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='avatar_hulvhn', max_length=255, null=True, verbose_name='profiles'),
        ),
    ]
