from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError
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
    img = models.ImageField(upload_to="icons/items/", null=True, blank=True)
    subtype = models.CharField(max_length=100, choices=ItemSubtypeChoice.choices)
    trait = models.ManyToManyField(ItemTrait, blank=True)
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

    description = models.TextField(null=True, blank=True)

    protection = models.BooleanField(default=False)  # property
    def_tot = models.PositiveSmallIntegerField(default=0, blank=True)
    def_base = models.PositiveSmallIntegerField(default=0)
    def_bonus = models.PositiveSmallIntegerField(default=0)
    dr = models.BooleanField(default=False)  # property
    dr_value = models.PositiveSmallIntegerField(default=0)

    weapon = models.BooleanField(default=False)  # property
    dmg_tot = models.PositiveSmallIntegerField(default=0)
    dmg_base = models.CharField(max_length=5)
    dmg_stat = models.CharField(max_length=100, choices=CaracChoice.choices)
    dmg_bonus = models.PositiveSmallIntegerField(default=0)
    mod = models.PositiveSmallIntegerField(default=0)
    skill = models.CharField(max_length=100, choices=CaracChoice.choices)
    skillBonus = models.PositiveSmallIntegerField(default=0)
    critrange = models.CharField(max_length=10, default="20")

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
    slug = models.SlugField(unique=True, blank=True)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="items",
        null=True,
        blank=True,
    )
    access = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        self.slug = slugify(self.name)
        if Item.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError(
                {
                    "name": [
                        "Cet objet existe déjà !",
                    ]
                }
            )


class Inventory(AbstractItem):
    actor = models.ForeignKey(
        to="actors.Actor",
        on_delete=models.CASCADE,
        related_name="inventories",
    )
    slug = models.SlugField(unique=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="inventories",
        null=True,
        blank=True,
    )

    def clean_fields(self, exclude=None):
        self.slug = slugify(self.name)

    def __str__(self):
        return self.name
