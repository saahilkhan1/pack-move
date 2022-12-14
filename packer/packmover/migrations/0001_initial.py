# Generated by Django 4.1.1 on 2022-11-22 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.CharField(blank=True, max_length=15, null=True)),
                ('mdate', models.DateField(blank=True, null=True)),
                ('isread', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('shiftingloc', models.CharField(blank=True, max_length=200, null=True)),
                ('briefitem', models.CharField(blank=True, max_length=200, null=True)),
                ('item', models.CharField(blank=True, max_length=500, null=True)),
                ('professional', models.CharField(blank=True, max_length=200, null=True)),
                ('requestdate', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('updationdate', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
