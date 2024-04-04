from django.db import models
from rules.choices import (
    RarityChoice,
    Source,
    CaracChoice,
    ItemTrait,
    ReloadChoice,
    SlotChoice,
    ItemSubtypeChoice,
)


class Category(models.Model):
    name = models.CharField(max_length=255)


class AbstractItem(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)
    img = models.ImageField(null=True, blank=True)
    subtype = models.CharField(max_length=100, choices=ItemSubtypeChoice.choices)
    trait = models.ManyToManyField(
        ItemTrait,
    )
    rarity = models.CharField(max_length=100, choices=RarityChoice.choices)
    unique = models.BooleanField(default=False)  # property
    price = models.PositiveSmallIntegerField(default=0)
    value = models.PositiveSmallIntegerField(default=0)

    equipment = models.BooleanField(default=False)  # property
    stackable = models.BooleanField(default=False)  # property
    qty = models.PositiveSmallIntegerField(default=1)
    stacksize = models.PositiveSmallIntegerField(default=1)
    deleteWhen0 = models.BooleanField(default=False)
    tailored = models.BooleanField(default=False)  # property
    two_handed = models.BooleanField(default=False)  # property
    consumable = models.BooleanField(default=False)  # property

    description = models.TextField()

    protection = models.BooleanField(default=False)  # property
    def_tot = models.PositiveSmallIntegerField(default=0)
    def_base = models.PositiveSmallIntegerField(default=0)
    def_bonus = models.PositiveSmallIntegerField(default=0)
    dr = models.BooleanField(default=False)  # property
    dr_value = models.PositiveSmallIntegerField(default=0)

    weapon = models.BooleanField(default=False)  # property
    dmg_tot = models.PositiveSmallIntegerField(default=0)
    dmg_base = models.PositiveSmallIntegerField(default=0)
    dmg_stat = models.CharField(max_length=100, choices=CaracChoice.choices)
    dmg_bonus = models.PositiveSmallIntegerField(default=0)
    mod = models.PositiveSmallIntegerField(default=0)
    skill = models.CharField(max_length=100, choices=CaracChoice.choices)
    skillBonus = models.PositiveSmallIntegerField(default=0)
    critrange = models.CharField(max_length=10)

    ranged = models.BooleanField(default=False)  # property
    range = models.PositiveSmallIntegerField(default=0)
    reloadable = models.BooleanField(default=False)  # property
    reload = models.CharField(max_length=100, choices=ReloadChoice.choices)
    bow = models.BooleanField(default=False)  # property
    crossbow = models.BooleanField(default=False)  # property
    powder = models.BooleanField(default=False)  # property
    throwing = models.BooleanField(default=False)  # property
    sling = models.BooleanField(default=False)  # property
    spell = models.BooleanField(default=False)  # property

    equipable = models.BooleanField(default=False)  # property
    worn = models.BooleanField(default=False)
    slot = models.CharField(max_length=100, choices=SlotChoice.choices)

    class Meta:
        abstract = True


class Item(AbstractItem):
    slug = models.SlugField(unique=True)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="items",
        null=True,
        blank=True,
    )


class Equipment(AbstractItem):
    actor = models.ForeignKey(
        to="actors.Actor",
        on_delete=models.CASCADE,
        related_name="equipments",
    )
    slug = models.SlugField(unique=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="equipments",
        null=True,
        blank=True,
    )
