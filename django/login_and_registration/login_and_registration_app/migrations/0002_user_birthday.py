# Generated by Django 2.2.4 on 2024-07-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
