# Generated by Django 5.0.7 on 2024-08-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solo_project_app', '0002_auto_20240803_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
