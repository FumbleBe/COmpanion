# Generated by Django 5.0.2 on 2024-02-24 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('size', models.CharField(choices=[('small', 'Petit'), ('medium', 'Moyen')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('base', models.PositiveSmallIntegerField(default=10)),
                ('bonus', models.PositiveSmallIntegerField(default=0)),
                ('malus', models.PositiveSmallIntegerField(default=0)),
                ('mod', models.PositiveSmallIntegerField(default=0)),
                ('dm_bonus', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.PositiveSmallIntegerField(default=0)),
                ('bonus', models.PositiveSmallIntegerField(default=0)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('max', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Charisme', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='CHA', editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CON',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Constitution', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='CON', editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DEX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Dextérité', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='DEX', editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nc', models.PositiveSmallIntegerField(default=1)),
                ('category', models.CharField(choices=[('', '')], max_length=100)),
                ('archetype', models.CharField(choices=[('standard', 'Standard')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='INT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Intelligence', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='INT', editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('painted', models.BooleanField(default=False)),
                ('pawn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.PositiveSmallIntegerField(default=10)),
                ('racial', models.SmallIntegerField(default=0)),
                ('bonus', models.SmallIntegerField(default=0)),
                ('mod', models.SmallIntegerField(default=0)),
                ('value', models.SmallIntegerField(default=0)),
                ('tmpmod', models.SmallIntegerField(default=0)),
                ('superior', models.BooleanField(default=False)),
                ('skillbonus', models.SmallIntegerField(default=0)),
                ('skillmalus', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Sagesse', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='WIS', editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Def',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.attribute')),
                ('label', models.CharField(default='Défence', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='Def', editable=False, max_length=100)),
            ],
            bases=('actors.attribute',),
        ),
        migrations.CreateModel(
            name='HP',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.attribute')),
                ('label', models.CharField(default='Points de Vigueur', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PV', editable=False, max_length=100)),
            ],
            bases=('actors.attribute',),
        ),
        migrations.CreateModel(
            name='Init',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.attribute')),
                ('label', models.CharField(default='Initiative', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='Init', editable=False, max_length=100)),
            ],
            bases=('actors.attribute',),
        ),
        migrations.CreateModel(
            name='MP',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.attribute')),
                ('label', models.CharField(default='Points de Mana', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PM', editable=False, max_length=100)),
            ],
            bases=('actors.attribute',),
        ),
        migrations.CreateModel(
            name='RP',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.attribute')),
                ('label', models.CharField(default='Points de Récupération', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PR', editable=False, max_length=100)),
            ],
            bases=('actors.attribute',),
        ),
        migrations.CreateModel(
            name='CP',
            fields=[
                ('currency_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.currency')),
                ('label', models.CharField(default='Pièces de Cuivre', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PC', editable=False, max_length=100)),
            ],
            bases=('actors.currency',),
        ),
        migrations.CreateModel(
            name='GP',
            fields=[
                ('currency_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.currency')),
                ('label', models.CharField(default="Pièces d'Or", editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PM', editable=False, max_length=100)),
            ],
            bases=('actors.currency',),
        ),
        migrations.CreateModel(
            name='PP',
            fields=[
                ('currency_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.currency')),
                ('label', models.CharField(default='Pièces de Platine', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PP', editable=False, max_length=100)),
            ],
            bases=('actors.currency',),
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('currency_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.currency')),
                ('label', models.CharField(default="Pièces d'Argent", editable=False, max_length=100)),
                ('abbrev', models.CharField(default='PA', editable=False, max_length=100)),
            ],
            bases=('actors.currency',),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField(default=1)),
                ('weight', models.PositiveSmallIntegerField(default=1)),
                ('height', models.PositiveSmallIntegerField(default=1)),
                ('eyes', models.CharField(max_length=255)),
                ('hair', models.CharField(max_length=255)),
                ('languages', models.ManyToManyField(to='actors.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Magic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Magique', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='Mag', editable=False, max_length=100)),
                ('object_id', models.PositiveBigIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Melee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Mellée', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='CaC', editable=False, max_length=100)),
                ('object_id', models.PositiveBigIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField(default=1)),
                ('weight', models.PositiveSmallIntegerField(default=1)),
                ('height', models.PositiveSmallIntegerField(default=1)),
                ('eyes', models.CharField(max_length=255)),
                ('hair', models.CharField(max_length=255)),
                ('languages', models.ManyToManyField(to='actors.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Ranged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Distance', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='Dist', editable=False, max_length=100)),
                ('object_id', models.PositiveBigIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='STR',
            fields=[
                ('statistic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actors.statistic')),
                ('label', models.CharField(default='Force', editable=False, max_length=100)),
                ('abbrev', models.CharField(default='FOR', editable=False, max_length=100)),
            ],
            bases=('actors.statistic',),
        ),
        migrations.AddField(
            model_name='statistic',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='actors.character'),
        ),
    ]
