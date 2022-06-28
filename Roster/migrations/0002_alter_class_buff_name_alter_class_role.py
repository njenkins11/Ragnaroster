# Generated by Django 4.0.5 on 2022-06-06 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='buff_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Roster.spell'),
        ),
        migrations.AlterField(
            model_name='class',
            name='role',
            field=models.CharField(choices=[('Tank', 'Tank'), ('Ranged DPS', 'Ranged Dps'), ('Melee DPS', 'Melee Dps'), ('Healer', 'Healer')], max_length=200),
        ),
    ]
