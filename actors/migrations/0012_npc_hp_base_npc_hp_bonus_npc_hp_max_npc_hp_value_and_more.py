# Generated by Django 5.0.4 on 2024-04-17 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0011_remove_character_languages_remove_npc_age_and_more'),
        ('rules', '0016_alter_capacity_description_alter_path_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='HP_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='HP_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='HP_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='HP_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='LP_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='LP_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='LP_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='LP_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='MP_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='MP_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='MP_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='MP_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='RP_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='RP_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='RP_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='RP_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='age',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='npc',
            name='background',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='def_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='def_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='def_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='def_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='eyes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='gender',
            field=models.CharField(choices=[('', ''), ('male', 'Homme'), ('female', 'Femme')], default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='npc',
            name='hair',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='height',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='npc',
            name='init_base',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='init_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='init_max',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='init_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_base',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_dm_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_malus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_mod',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='magic_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='INT', max_length=3),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_base',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_dm_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_malus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_mod',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='melee_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='STR', max_length=3),
        ),
        migrations.AddField(
            model_name='npc',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='npcs', to='rules.profile'),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_base',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_dm_bonus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_malus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_mod',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='npc',
            name='ranged_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='DEX', max_length=3),
        ),
        migrations.AddField(
            model_name='npc',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='npcs', to='rules.species'),
        ),
        migrations.AddField(
            model_name='npc',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('', ''), ('male', 'Homme'), ('female', 'Femme')], default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='magic_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='INT', max_length=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='melee_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='STR', max_length=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='ranged_stat',
            field=models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], default='DEX', max_length=3),
        ),
    ]