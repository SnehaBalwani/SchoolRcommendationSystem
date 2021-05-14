# Generated by Django 3.1.3 on 2020-12-08 14:50

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sch', '0004_auto_20201208_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0),
                                                                 geography=True, srid=4326),
        ),
    ]
