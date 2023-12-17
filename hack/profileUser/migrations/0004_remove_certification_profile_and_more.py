# Generated by Django 5.0 on 2023-12-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certification',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='community',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='language',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='certifications',
            field=models.ManyToManyField(blank=True, to='profileUser.certification'),
        ),
        migrations.AddField(
            model_name='profile',
            name='communities',
            field=models.ManyToManyField(blank=True, to='profileUser.community'),
        ),
        migrations.AddField(
            model_name='profile',
            name='educations',
            field=models.ManyToManyField(blank=True, to='profileUser.education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='experiences',
            field=models.ManyToManyField(blank=True, to='profileUser.experience'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, to='profileUser.interests'),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(blank=True, to='profileUser.language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='profileUser.skill'),
        ),
    ]