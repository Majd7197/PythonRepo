# Generated by Django 2.2.4 on 2024-07-10 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_shell_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='updated_at',
        ),
    ]
