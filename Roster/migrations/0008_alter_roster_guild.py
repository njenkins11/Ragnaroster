# Generated by Django 4.0.5 on 2022-06-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0007_roster_realm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='guild',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
