# Generated by Django 5.0.4 on 2024-04-09 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0010_remove_character_owner_actor_owner'),
        ('items', '0006_alter_equipment_dmg_base_alter_item_dmg_base'),
        ('rules', '0011_profile_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='icons/items/')),
                ('subtype', models.CharField(choices=[('other', 'Divers'), ('armor', 'Armure'), ('shield', 'Bouclier'), ('melee', 'Arme de contact'), ('ranged', 'Arme à distance'), ('spell', 'Sort'), ('jewel', 'Bijou'), ('scroll', 'Parchemin'), ('wand', 'Baguette'), ('ammunition', 'Munition'), ('consumable', 'Consommable'), ('container', 'Contenant'), ('mount', 'Monture'), ('currency', 'Monnaie'), ('equipment', 'Equipement')], max_length=100)),
                ('rarity', models.CharField(choices=[('common', 'Commun'), ('moderate', 'Modéré'), ('rare', 'Rare'), ('very-rare', 'Très rare'), ('unique', 'Unique')], max_length=100)),
                ('unique', models.BooleanField(default=False)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('equipment', models.BooleanField(default=False)),
                ('stackable', models.BooleanField(default=False)),
                ('qty', models.PositiveSmallIntegerField(default=1)),
                ('stacksize', models.PositiveSmallIntegerField(default=1)),
                ('deleteWhen0', models.BooleanField(default=False)),
                ('tailored', models.BooleanField(default=False)),
                ('two_handed', models.BooleanField(default=False)),
                ('consumable', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('protection', models.BooleanField(default=False)),
                ('def_tot', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('def_base', models.PositiveSmallIntegerField(default=0)),
                ('def_bonus', models.PositiveSmallIntegerField(default=0)),
                ('dr', models.BooleanField(default=False)),
                ('dr_value', models.PositiveSmallIntegerField(default=0)),
                ('weapon', models.BooleanField(default=False)),
                ('dmg_tot', models.PositiveSmallIntegerField(default=0)),
                ('dmg_base', models.CharField(max_length=5)),
                ('dmg_stat', models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], max_length=100)),
                ('dmg_bonus', models.PositiveSmallIntegerField(default=0)),
                ('mod', models.PositiveSmallIntegerField(default=0)),
                ('skill', models.CharField(choices=[('STR', 'Force'), ('DEX', 'Dextérité'), ('CON', 'Constitution'), ('INT', 'Intelligence'), ('WIS', 'Sagesse'), ('CHA', 'Charisme')], max_length=100)),
                ('skillBonus', models.PositiveSmallIntegerField(default=0)),
                ('critrange', models.CharField(default='20', max_length=10)),
                ('ranged', models.BooleanField(default=False)),
                ('range', models.PositiveSmallIntegerField(default=0)),
                ('reloadable', models.BooleanField(default=False)),
                ('reload', models.CharField(choices=[('', "Pas d'action"), ('s', 'Action simple (S)'), ('l', 'Action limitée (L)')], max_length=100)),
                ('bow', models.BooleanField(default=False)),
                ('crossbow', models.BooleanField(default=False)),
                ('powder', models.BooleanField(default=False)),
                ('throwing', models.BooleanField(default=False)),
                ('sling', models.BooleanField(default=False)),
                ('spell', models.BooleanField(default=False)),
                ('equipable', models.BooleanField(default=False)),
                ('worn', models.BooleanField(default=False)),
                ('slot', models.CharField(choices=[('hand', 'Main'), ('head', 'Tête'), ('ear', 'Oreille'), ('neck', 'Cou'), ('shoulders', 'Épaules'), ('chest', 'Torse'), ('back', 'Dos'), ('arm', 'Bras'), ('finger', 'Doigt'), ('wrist', 'Poignet'), ('waist', 'Taille'), ('legs', 'Jambes'), ('feet', 'Pieds'), ('belt', 'À la ceinture'), ('backpack', 'Sac-à-dos'), ('quiver', 'Carquois')], max_length=100)),
                ('slug', models.SlugField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='actors.actor')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inventories', to='rules.source')),
                ('trait', models.ManyToManyField(blank=True, to='rules.itemtrait')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
    ]
