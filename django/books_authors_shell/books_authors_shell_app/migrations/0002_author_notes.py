# Generated by Django 2.2.4 on 2024-07-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_shell_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
