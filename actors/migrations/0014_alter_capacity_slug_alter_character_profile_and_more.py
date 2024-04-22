# Generated by Django 5.0.4 on 2024-04-17 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0013_rename_languages_language_and_more'),
        ('rules', '0016_alter_capacity_description_alter_path_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacity',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='profile',
            field=models.ForeignKey(default=495, on_delete=django.db.models.deletion.PROTECT, related_name='characters', to='rules.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='species',
            field=models.ForeignKey(default=250, on_delete=django.db.models.deletion.PROTECT, related_name='characters', to='rules.species'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='npc',
            name='profile',
            field=models.ForeignKey(default=495, on_delete=django.db.models.deletion.PROTECT, related_name='npcs', to='rules.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='npc',
            name='species',
            field=models.ForeignKey(default=250, on_delete=django.db.models.deletion.PROTECT, related_name='npcs', to='rules.species'),
            preserve_default=False,
        ),
    ]