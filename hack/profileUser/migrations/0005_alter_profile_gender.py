# Generated by Django 5.0 on 2023-12-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0004_remove_certification_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=6, null=True),
        ),
    ]
