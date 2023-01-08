# Generated by Django 4.1.5 on 2023-01-08 22:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cents', '0006_remove_cent_loves_cent_hearts_cent_user_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cent',
            name='user_likes',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]