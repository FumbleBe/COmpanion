from django.db import models
from rules.choices import RarityChoice, Source

class Category(models.Model):
    name = models.CharField(max_length=255)

# class Item(models.Model):
#     # RARITY_CHOICES = [("", ""),
#     #                   ("common", "Commun"),
#     #                   ("moderate", "Modéré"),
#     #                   ("rare", "Rare"),
#     #                   ("very-rare", "Très rare"),
#     #                   ("unique", "Unique")]
#     # SOURCE_CHOICES = [("", "")]


#     name = models.CharField(max_length=255)
#     img = models.ImageField(null=True, blank=True)
#     type = 
#     rarity = models.CharField(max_length=100, choices=RarityChoice.choices)
#     price = models.PositiveSmallIntegerField(default=0)
#     value = models.PositiveSmallIntegerField(default=0)
#     qty = models.PositiveSmallIntegerField(default=1)
#     description = models.TextField()
#     source = models.ForeignKey(
#         Source,
#         on_delete=models.PROTECT,
#         related_name="sources",
#         null=True,
#         blank=True,
#     )

# class Weapon(models.Model):
#     melee
#     ranged
#     ammunition
#     subtype = 
#     "dmg": "",
#     "dmgBase": "",
#     "dmgStat": "",
#     "dmgBonus": 0,
#     "mod": 0,
#     "skill": "",
#     "skillBonus": 0,
#     "critrange": "20",
#     "hands": 1,
#     "range": 0,
#     "reload": "",

# class Armor(models.Model):
#     shield
#     armor
#     subtype =
#     "def": 0,
#     "defBase": 0,
#     "defBonus": 0,

# <select name="data.subtype" data-type="String" style="width:100%"
# "other"Divers
# "armor"Armure
# "shield" selected=""Bouclier
# "melee"Arme de contact
# "ranged"Arme à distance
# "spell"Sort
# "jewel"Bijou
# "scroll"Parchemin
# "wand"Baguette
# "ammunition"Munition
# "consumable"Consommable
# "container"Contenant
# "mount"Monture
# "currency"Monnaie
# "trapping"Equipement
# </select