# Generated by Django 4.0.5 on 2022-06-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='core.author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='coverImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='related_articles',
            field=models.ManyToManyField(blank=True, null=True, to='core.article'),
        ),
    ]