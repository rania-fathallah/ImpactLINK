# Generated by Django 5.0 on 2023-12-17 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_employeeaccount_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeaccount',
            name='profile',
        ),
    ]
