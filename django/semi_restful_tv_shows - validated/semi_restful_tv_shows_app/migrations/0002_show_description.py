# Generated by Django 2.2.4 on 2024-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
