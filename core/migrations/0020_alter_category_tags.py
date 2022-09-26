# Generated by Django 4.0.5 on 2022-08-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_category_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(related_name='categories', to='core.tags'),
        ),
    ]