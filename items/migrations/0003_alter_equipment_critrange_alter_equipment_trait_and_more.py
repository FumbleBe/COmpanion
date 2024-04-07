# Generated by Django 5.0.3 on 2024-04-05 13:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_access'),
        ('rules', '0010_itemtrait_alter_source_options_alter_species_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='critrange',
            field=models.CharField(default='20', max_length=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='trait',
            field=models.ManyToManyField(blank=True, to='rules.itemtrait'),
        ),
        migrations.AlterField(
            model_name='item',
            name='access',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='critrange',
            field=models.CharField(default='20', max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='trait',
            field=models.ManyToManyField(blank=True, to='rules.itemtrait'),
        ),
    ]