# Generated by Django 4.0.5 on 2022-06-14 21:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
