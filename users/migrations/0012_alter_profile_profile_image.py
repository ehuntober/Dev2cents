# Generated by Django 4.1.5 on 2023-01-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='profiles/'),
        ),
    ]
