# Generated by Django 4.1.5 on 2023-01-07 23:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cent',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]