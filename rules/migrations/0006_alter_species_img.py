# Generated by Django 5.0.2 on 2024-03-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0005_alter_species_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
