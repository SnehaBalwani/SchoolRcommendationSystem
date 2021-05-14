# Generated by Django 3.1.2 on 2020-11-18 12:54

from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('sch', '0001_initial'),
    ]

    operations = [
        CreateExtension('postgis'),
        migrations.CreateModel(
            name='School_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=1000, null=True)),
                ('gender_allowed', models.CharField(max_length=1000, null=True)),
                ('type_school', models.CharField(max_length=1000, null=True)),
                ('board', models.CharField(max_length=1000, null=True)),
                ('fees', models.CharField(max_length=1000, null=True)),
                ('grade', models.CharField(max_length=1000, null=True)),
                ('min_age', models.CharField(max_length=1000, null=True)),
                ('medium', models.CharField(max_length=1000, null=True)),
                ('avg_class_strength', models.CharField(max_length=1000, null=True)),
                ('estd', models.CharField(max_length=1000, null=True)),
                ('school_strength', models.CharField(max_length=1000, null=True)),
                ('swimming_pool', models.CharField(max_length=1000, null=True)),
                ('indoor_sports', models.CharField(max_length=1000, null=True)),
                ('ac_classes', models.CharField(max_length=1000, null=True)),
                ('transportation', models.CharField(max_length=1000, null=True)),
                ('outdoor_sports', models.CharField(max_length=1000, null=True)),
                ('annual_fees', models.CharField(max_length=1000, null=True)),
                ('admission_fees', models.CharField(max_length=1000, null=True)),
                ('phone1', models.CharField(max_length=1000, null=True)),
                ('phone2', models.CharField(max_length=1000, null=True)),
                ('phone3', models.CharField(max_length=1000, null=True)),
                ('phone4', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]