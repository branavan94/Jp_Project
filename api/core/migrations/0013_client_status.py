# Generated by Django 2.2.6 on 2019-12-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191202_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('mn', 'Modification Necessary'), ('al', 'All Good')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
