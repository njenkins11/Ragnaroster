# Generated by Django 4.0.5 on 2022-06-06 04:32

import _queue
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(choices=[('Druid', 'Druid'), ('DeathKnight', 'Deathknight'), ('Hunter', 'Hunter'), ('Rogue', 'Rogue'), ('Paladin', 'Paladin'), ('Priest', 'Priest'), ('Mage', 'Mage'), ('Shaman', 'Shaman'), ('Warrior', 'Warrior'), ('Warlock', 'Warlock')], default='Druid', max_length=200)),
                ('spec', models.CharField(choices=[('Restoration', 'Resto'), ('Feral', 'Feral'), ('Balance', 'Balance'), ('Blood', 'Blood'), ('Frost', 'Frost'), ('Unholy', 'Unholy'), ('Survival', 'Survival'), ('Marksman', 'Marksman'), ('Beast Master', 'Beast Master'), ('Combat', 'Combat'), ('Assassination', 'Assassination'), ('Subtlety', 'Subtlety'), ('Holy', 'Holy'), ('Retribution', 'Retribution'), ('Protection', 'Protection'), ('Shadow', 'Shadow'), ('Discipline', 'Discipline'), ('Fire', 'Fire'), ('Arcane', 'Arcane'), ('Elemental', 'Elemental'), ('Enhancement', 'Enhancement'), ('Fury', 'Fury'), ('Arms', 'Arms'), ('Destruction', 'Destruction'), ('Demology', 'Demology'), ('Affliction', 'Affliction')], default='Affliction', max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Roster.class')),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('spell_id', models.AutoField(primary_key=True, serialize=False)),
                ('buff_name', models.CharField(max_length=200)),
                ('buff_description', models.CharField(max_length=200)),
                ('buff_type', models.CharField(choices=[('Agility and Strength', 'Agil And Str'), ('Armor Percent', 'Armor Perc'), ('Attack Power', 'Atck Pow'), ('Attack Power Percent', 'Atck Pow Perc'), ('Heroism', 'Hero'), ('Damage Percent', 'Damage Perc'), ('Damage Reduction Percent', 'Damage Reduct Perc'), ('Haste Percent', 'Haste Perc'), ('Healing Recieved Percent', 'Healing Rec Perc'), ('Heath', 'Health'), ('Intellect', 'Int'), ('Mana Per Second', 'Mana Per'), ('Melee Critical Percent', 'Mele Crit Perc'), ('Melee Haste Percent', 'Mele Haste Perc'), ('Replenishment', 'Replinish')], default=_queue.Empty, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('roster_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roster.player')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='buff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Roster.spell'),
        ),
    ]
