# Generated by Django 5.0.4 on 2024-04-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0012_alter_species_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacity',
            name='slug',
            field=models.SlugField(blank=True, unique=False),
        ),
    ]
