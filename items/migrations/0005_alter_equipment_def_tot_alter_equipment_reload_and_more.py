# Generated by Django 5.0.3 on 2024-04-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_equipment_description_alter_equipment_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='def_tot',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='reload',
            field=models.CharField(choices=[('', "Pas d'action"), ('s', 'Action simple (S)'), ('l', 'Action limitée (L)')], max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='def_tot',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='reload',
            field=models.CharField(choices=[('', "Pas d'action"), ('s', 'Action simple (S)'), ('l', 'Action limitée (L)')], max_length=100),
        ),
    ]
