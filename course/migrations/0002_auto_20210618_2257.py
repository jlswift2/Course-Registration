# Generated by Django 2.2.23 on 2021-06-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prof',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='prof',
            name='last_name',
        ),
    ]
