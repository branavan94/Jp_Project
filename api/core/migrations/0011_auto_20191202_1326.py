# Generated by Django 2.2.6 on 2019-12-02 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191202_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date_act',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chauffeur',
            name='horaire_chauffeur',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_arrival',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_leave',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_debut',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_fin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='date_debut',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='date_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='one_to_one',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 12, 26, 13, 188228, tzinfo=utc)),
        ),
    ]
