from django.db import models
from django.conf import settings

from rules.choices import (
    CaracChoice,
    SizeChoice,
    GenderChoice,
    CategoryChoice,
    ArchetypeChoice,
    BossChoice,
)
from rules.models import AbstractCapacity
from rules.choices import Source


class Actor(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    size = models.CharField(
        max_length=100, choices=SizeChoice.choices, default="MEDIUM"
    )

    STR_base = models.PositiveSmallIntegerField(default=10)
    STR_racial = models.SmallIntegerField(default=0)
    STR_bonus = models.SmallIntegerField(default=0)
    STR_mod = models.SmallIntegerField(default=0)
    STR_value = models.SmallIntegerField(default=0)
    STR_tmpmod = models.SmallIntegerField(default=0)
    STR_superior = models.BooleanField(default=False)
    STR_skillbonus = models.SmallIntegerField(default=0)
    STR_skillmalus = models.SmallIntegerField

    DEX_base = models.PositiveSmallIntegerField(default=10)
    DEX_racial = models.SmallIntegerField(default=0)
    DEX_bonus = models.SmallIntegerField(default=0)
    DEX_mod = models.SmallIntegerField(default=0)
    DEX_value = models.SmallIntegerField(default=0)
    DEX_tmpmod = models.SmallIntegerField(default=0)
    DEX_superior = models.BooleanField(default=False)
    DEX_skillbonus = models.SmallIntegerField(default=0)
    DEX_skillmalus = models.SmallIntegerField(default=0)

    CON_base = models.PositiveSmallIntegerField(default=10)
    CON_racial = models.SmallIntegerField(default=0)
    CON_bonus = models.SmallIntegerField(default=0)
    CON_mod = models.SmallIntegerField(default=0)
    CON_value = models.SmallIntegerField(default=0)
    CON_tmpmod = models.SmallIntegerField(default=0)
    CON_superior = models.BooleanField(default=False)
    CON_skillbonus = models.SmallIntegerField(default=0)
    CON_skillmalus = models.SmallIntegerField(default=0)

    INT_base = models.PositiveSmallIntegerField(default=10)
    INT_racial = models.SmallIntegerField(default=0)
    INT_bonus = models.SmallIntegerField(default=0)
    INT_mod = models.SmallIntegerField(default=0)
    INT_value = models.SmallIntegerField(default=0)
    INT_tmpmod = models.SmallIntegerField(default=0)
    INT_superior = models.BooleanField(default=False)
    INT_skillbonus = models.SmallIntegerField(default=0)
    INT_skillmalus = models.SmallIntegerField(default=0)

    WIS_base = models.PositiveSmallIntegerField(default=10)
    WIS_racial = models.SmallIntegerField(default=0)
    WIS_bonus = models.SmallIntegerField(default=0)
    WIS_mod = models.SmallIntegerField(default=0)
    WIS_value = models.SmallIntegerField(default=0)
    WIS_tmpmod = models.SmallIntegerField(default=0)
    WIS_superior = models.BooleanField(default=False)
    WIS_skillbonus = models.SmallIntegerField(default=0)
    WIS_skillmalus = models.SmallIntegerField(default=0)

    CHA_base = models.PositiveSmallIntegerField(default=10)
    CHA_racial = models.SmallIntegerField(default=0)
    CHA_bonus = models.SmallIntegerField(default=0)
    CHA_mod = models.SmallIntegerField(default=0)
    CHA_value = models.SmallIntegerField(default=0)
    CHA_tmpmod = models.SmallIntegerField(default=0)
    CHA_superior = models.BooleanField(default=False)
    CHA_skillbonus = models.SmallIntegerField(default=0)
    CHA_skillmalus = models.SmallIntegerField(default=0)

    language = models.ManyToManyField(to="actors.Language", blank=True)

    PP = models.PositiveSmallIntegerField(default=0)
    GP = models.PositiveSmallIntegerField(default=0)
    SP = models.PositiveSmallIntegerField(default=0)
    CP = models.PositiveSmallIntegerField(default=0)

    # Owner is here because items are attached directly to actors
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class AbstractPJ(Actor):
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(
        max_length=100, choices=GenderChoice.choices, default="NULL"
    )
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255, null=True, blank=True)
    hair = models.CharField(max_length=255, null=True, blank=True)
    background = models.TextField(blank=True)

    melee_enabled = models.BooleanField(default=True)
    melee_base = models.PositiveSmallIntegerField(default=10)
    melee_bonus = models.PositiveSmallIntegerField(default=0)
    melee_malus = models.PositiveSmallIntegerField(default=0)
    melee_mod = models.PositiveSmallIntegerField(default=0)
    melee_dm_bonus = models.PositiveSmallIntegerField(default=0)
    melee_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="STR"
    )

    ranged_enabled = models.BooleanField(default=True)
    ranged_base = models.PositiveSmallIntegerField(default=10)
    ranged_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_malus = models.PositiveSmallIntegerField(default=0)
    ranged_mod = models.PositiveSmallIntegerField(default=0)
    ranged_dm_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="DEX"
    )

    magic_enabled = models.BooleanField(default=True)
    magic_base = models.PositiveSmallIntegerField(default=10)
    magic_bonus = models.PositiveSmallIntegerField(default=0)
    magic_malus = models.PositiveSmallIntegerField(default=0)
    magic_mod = models.PositiveSmallIntegerField(default=0)
    magic_dm_bonus = models.PositiveSmallIntegerField(default=0)
    magic_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="INT"
    )

    init_base = models.PositiveSmallIntegerField(default=0)
    init_bonus = models.PositiveSmallIntegerField(default=0)
    init_value = models.PositiveSmallIntegerField(default=0)
    init_max = models.PositiveSmallIntegerField(default=0)

    HP_base = models.PositiveSmallIntegerField(default=0)
    HP_bonus = models.PositiveSmallIntegerField(default=0)
    HP_value = models.PositiveSmallIntegerField(default=0)
    HP_max = models.PositiveSmallIntegerField(default=0)

    RP_base = models.PositiveSmallIntegerField(default=0)
    RP_bonus = models.PositiveSmallIntegerField(default=0)
    RP_value = models.PositiveSmallIntegerField(default=0)
    RP_max = models.PositiveSmallIntegerField(default=0)

    def_base = models.PositiveSmallIntegerField(default=0)
    def_bonus = models.PositiveSmallIntegerField(default=0)
    def_value = models.PositiveSmallIntegerField(default=0)
    def_max = models.PositiveSmallIntegerField(default=0)

    MP_base = models.PositiveSmallIntegerField(default=0)
    MP_bonus = models.PositiveSmallIntegerField(default=0)
    MP_value = models.PositiveSmallIntegerField(default=0)
    MP_max = models.PositiveSmallIntegerField(default=0)

    LP_base = models.PositiveSmallIntegerField(default=0)
    LP_bonus = models.PositiveSmallIntegerField(default=0)
    LP_value = models.PositiveSmallIntegerField(default=0)
    LP_max = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class Character(AbstractPJ):
    species = models.ForeignKey(
        "rules.Species",
        on_delete=models.PROTECT,
        related_name="characters",
        null=False,
        blank=False,
    )
    profile = models.ForeignKey(
        "rules.Profile",
        on_delete=models.PROTECT,
        related_name="characters",
        null=False,
        blank=False,
    )


class NPC(AbstractPJ):
    species = models.ForeignKey(
        "rules.Species",
        on_delete=models.PROTECT,
        related_name="npcs",
        null=False,
        blank=False,
    )
    profile = models.ForeignKey(
        "rules.Profile",
        on_delete=models.PROTECT,
        related_name="npcs",
        null=False,
        blank=False,
    )
    access = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class Encounter(Actor):
    nc = models.PositiveSmallIntegerField(default=1)
    category = models.CharField(
        max_length=100, null=True, blank=True, choices=CategoryChoice.choices
    )
    archetype = models.CharField(
        max_length=100, null=True, blank=True, choices=ArchetypeChoice.choices
    )
    boss = models.CharField(
        max_length=100, null=True, blank=True, choices=BossChoice.choices
    )

    melee_enabled = models.BooleanField(default=True)
    melee_base = models.PositiveSmallIntegerField(default=10)
    melee_bonus = models.PositiveSmallIntegerField(default=0)
    melee_malus = models.PositiveSmallIntegerField(default=0)
    melee_mod = models.PositiveSmallIntegerField(default=0)
    melee_dm_bonus = models.PositiveSmallIntegerField(default=0)
    melee_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="STR"
    )

    ranged_enabled = models.BooleanField(default=True)
    ranged_base = models.PositiveSmallIntegerField(default=10)
    ranged_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_malus = models.PositiveSmallIntegerField(default=0)
    ranged_mod = models.PositiveSmallIntegerField(default=0)
    ranged_dm_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="DEX"
    )

    magic_enabled = models.BooleanField(default=True)
    magic_base = models.PositiveSmallIntegerField(default=10)
    magic_bonus = models.PositiveSmallIntegerField(default=0)
    magic_malus = models.PositiveSmallIntegerField(default=0)
    magic_mod = models.PositiveSmallIntegerField(default=0)
    magic_dm_bonus = models.PositiveSmallIntegerField(default=0)
    magic_stat = models.CharField(
        max_length=3, choices=CaracChoice.choices, default="INT"
    )

    init_value = models.PositiveSmallIntegerField(default=0)
    init_temp = models.PositiveSmallIntegerField(default=0)

    def_value = models.PositiveSmallIntegerField(default=0)
    def_temp = models.PositiveSmallIntegerField(default=0)

    HP_value = models.PositiveSmallIntegerField(default=0)
    HP_max = models.PositiveSmallIntegerField(default=0)

    RD_value = models.PositiveSmallIntegerField(default=0)
    RD_temp = models.PositiveSmallIntegerField(default=0)

    path = models.ManyToManyField(
        to="rules.Path", blank=True, related_name="encounters"
    )

    capacity = models.ManyToManyField(
        to="rules.Capacity", blank=True, related_name="encounters"
    )

    access = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class Capacity(AbstractCapacity):
    slug = models.SlugField(unique=False, blank=True)
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        related_name="capacities",
        null=True,
        blank=True,
    )
    path = models.ForeignKey(
        "rules.Path",
        on_delete=models.CASCADE,
        related_name="known_capacities",
        null=True,
        blank=True,
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="known_capacities",
        null=True,
        blank=True,
    )
    rank = models.IntegerField(default=0)
    learned = models.BooleanField(default=False)

    def learn(self):
        if self.learned is True:
            return
        self.learned = True
        self.save()


class Language(models.Model):
    name = models.CharField(max_length=255)


class Mini(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    painted = models.BooleanField(default=False)
    pawn = models.BooleanField(default=False)
