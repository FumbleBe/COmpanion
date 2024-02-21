from django.db import models, transaction
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey

class Actor(models.Model):
    SIZE_CHOICES = [('small', 'Petit'),('medium', 'Moyen')]

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField(blank=True)

    size = models.CharField(choices=SIZE_CHOICES)

class Character(models.Model):
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255)
    hair = models.CharField(max_length=255)
    languages = models.ManyToManyField(to="actors.Languages")


class NPC(models.Model):
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255)
    hair = models.CharField(max_length=255)
    languages = models.ManyToManyField(to="actors.Languages")

class Encounter(models.Model):
    ARCHETYPE_CHOICES = [('standard','Standard')]
    CATEGORY_CHOICES = [('', '')]

    nc = models.PositiveSmallIntegerField(default=1)
    category = models.CharField(
        choices=CATEGORY_CHOICES
    )
    archetype = models.CharField(choices=ARCHETYPE_CHOICES)

class Languages(models.Model):
    name = models.CharField(max_length=255)

class Statistic(models.Model):
    base = models.PositiveSmallIntegerField(default=10)
    racial = models.SmallIntegerField(default=0)
    bonus = models.SmallIntegerField(default=0)
    mod = models.SmallIntegerField(max=3, default=0)
    value = models.SmallIntegerField(default=0)
    tmpmod = models.SmallIntegerField(default=0)
    superior = models.BooleanField(default=False)
    skillbonus = models.SmallIntegerField(default=0)
    skillmalus = models.SmallIntegerField(default=0)
    actor = models.ForeignKey('actors.Character', on_delete=models.CASCADE, related_name='statistics')

class STR(Statistic):
    label = models.CharField(default="Force", editable=False)
    abbrev = models.CharField(default="FOR", editable=False)

class DEX(models.Model):
    label = models.CharField(default="Dextérité", editable=False)
    abbrev = models.CharField(default="DEX", editable=False)

class CON(models.Model):
    label = models.CharField(default="Constitution", editable=False)
    abbrev = models.CharField(default="CON", editable=False)

class INT(models.Model):
    label = models.CharField(default="Intelligence", editable=False)
    abbrev = models.CharField(default="INT", editable=False)

class WIS(models.Model):
    label = models.CharField(default="Sagesse", editable=False)
    abbrev = models.CharField(default="WIS", editable=False)

class CHA(models.Model):
    label = models.CharField(default="Charisme", editable=False)
    abbrev = models.CharField(default="CHA", editable=False)

class Attack(models.Model): 
    enabled = models.BooleanField(default=True)
    base = models.PositiveSmallIntegerField(default=10)
    bonus = models.PositiveSmallIntegerField(default=0)
    malus = models.PositiveSmallIntegerField(default=0)
    mod = models.PositiveSmallIntegerField(default=0)
    dm_bonus = models.PositiveSmallIntegerField(default=0)

class Melee(models.Model):
    label = models.CharField(default="Mellée", editable=False)
    abbrev = models.CharField(default="CaC", editable=False)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.SET_NULL)
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()

class Ranged(models.Model):
    label = models.CharField(default="Distance", editable=False)
    abbrev = models.CharField(default="Dist", editable=False)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.SET_NULL)
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()

class Magic(models.Model):
    label = models.CharField(default="Magique", editable=False)
    abbrev = models.CharField(default="Mag", editable=False)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.SET_NULL)
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()

class Attribute(models.Model):
    base = models.PositiveSmallIntegerField(default=0)
    bonus = models.PositiveSmallIntegerField(default=0)
    value = models.PositiveSmallIntegerField(default=0)
    max = models.PositiveSmallIntegerField(default=0)

class HP(Attribute):
    label = models.CharField(default="Points de Vigueur", editable=False)
    abbrev = models.CharField(default="PV", editable=False)

class Def(Attribute):
    label = models.CharField(default="Défence", editable=False)
    abbrev = models.CharField(default="Def", editable=False)

class Init(Attribute):
    label = models.CharField(default="Initiative", editable=False)
    abbrev = models.CharField(default="Init", editable=False)

class RP(Attribute):
    label = models.CharField(default="Points de Récupération", editable=False)
    abbrev = models.CharField(default="PR", editable=False)

class MP(Attribute):
    label = models.CharField(default="Points de Mana", editable=False)
    abbrev = models.CharField(default="PM", editable=False)

class Currency(models.Model):
    qty = models.PositiveSmallIntegerField(default=0)

class PP(Currency):
    label = models.CharField(default="Pièces de Platine", editable=False)
    abbrev = models.CharField(default="PP", editable=False)

class GP(Currency):
    label = models.CharField(default="Pièces d'Or", editable=False)
    abbrev = models.CharField(default="PM", editable=False)

class SP(Currency):
    label = models.CharField(default="Pièces d'Argent", editable=False)
    abbrev = models.CharField(default="PA", editable=False)

class CP(Currency):
    label = models.CharField(default="Pièces de Cuivre", editable=False)
    abbrev = models.CharField(default="PC", editable=False)

class Mini(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    painted = models.BooleanField(default=False)
    pawn = models.BooleanField(default=False)

# class Category(models.Model):

#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

#     @transaction.atomic
#     def disable(self):
#         if self.active is False:
#             return
#         self.active = False
#         self.save()
#         self.products.update(active=False)


# class Product(models.Model):

#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     active = models.BooleanField(default=False)

#     category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, related_name='products')

#     def __str__(self):
#         return self.name

#     @transaction.atomic
#     def disable(self):
#         if self.active is False:
#             return
#         self.active = False
#         self.save()
#         self.articles.update(active=False)

#     def call_external_api(self, method, url):
#         return

#     @property
#     def ecoscore(self):
#         response = self.call_external_api('GET', 'https://world.openfoodfacts.org/api/v0/product/3229820787015.json')
#         if response.status_code == 200:
#             return response.json()['product']['ecoscore_grade']


# class Article(models.Model):

#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     active = models.BooleanField(default=False)
#     price = models.DecimalField(max_digits=4, decimal_places=2)

#     product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='articles')

#     def __str__(self):
#         return self.name
