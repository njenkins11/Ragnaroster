# Generated by Django 4.0.5 on 2022-06-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0006_alter_roster_faction'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='realm',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
