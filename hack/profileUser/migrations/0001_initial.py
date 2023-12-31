# Generated by Django 5.0 on 2023-12-17 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('profileTitle', models.CharField(max_length=255)),
                ('profileDescription', models.TextField()),
                ('phone', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('postalCode', models.CharField(max_length=4)),
                ('birthDate', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(choices=[('m', 'm'), ('w', 'w')], max_length=1, null=True)),
                ('linkedin', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('startDate', models.DateField(blank=True, default=None, null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('description', models.TextField()),
                ('current', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishment', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('current', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('startDate', models.DateField(blank=True, default=None, null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=255)),
                ('platform', models.CharField(default='', max_length=255)),
                ('date', models.DateField(blank=True, default=None)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profileUser.profile')),
            ],
        ),
    ]
