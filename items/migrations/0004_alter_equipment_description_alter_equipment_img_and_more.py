# Generated by Django 5.0.3 on 2024-04-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_equipment_critrange_alter_equipment_trait_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='icons/items/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='icons/items/'),
        ),
    ]
