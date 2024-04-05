# Generated by Django 5.0.3 on 2024-04-03 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0007_source_remove_capacity_source_remove_path_source_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacity',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='capacities', to='rules.source'),
        ),
    ]