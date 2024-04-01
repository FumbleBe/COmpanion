from django.db import models, transaction
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


class Actor(models.Model):
    SIZE_CHOICES = [
        ("tiny", "Minuscule"),
        ("really_small", "Très petit"),
        ("small", "Petit"),
        ("medium", "Moyen"),
        ("tall", "Grand"),
        ("huge", "Énorme"),
        ("colossal", "Colossale"),
    ]

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    size = models.CharField(max_length=100, choices=SIZE_CHOICES)

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


class Character(Actor):
    GENDER_CHOICES = [
        ("male", "Homme"),
        ("female", "Femme"),
    ]
    CARAC_CHOICES = [
        ("str", "FOR"),
        ("dex", "DEX"),
        ("con", "CON"),
        ("int", "INT"),
        ("wis", "SAG"),
        ("cha", "CHA")
    ]
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255, null=True, blank=True)
    hair = models.CharField(max_length=255, null=True, blank=True)
    background = models.TextField(blank=True)
    species = models.ForeignKey(
        "rules.Species",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    profile = models.ForeignKey(
        "rules.Profile",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )

    melee_enabled = models.BooleanField(default=True)
    melee_base = models.PositiveSmallIntegerField(default=10)
    melee_bonus = models.PositiveSmallIntegerField(default=0)
    melee_malus = models.PositiveSmallIntegerField(default=0)
    melee_mod = models.PositiveSmallIntegerField(default=0)
    melee_dm_bonus = models.PositiveSmallIntegerField(default=0)
    melee_stat = models.CharField(max_length=3, choices=CARAC_CHOICES)

    ranged_enabled = models.BooleanField(default=True)
    ranged_base = models.PositiveSmallIntegerField(default=10)
    ranged_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_malus = models.PositiveSmallIntegerField(default=0)
    ranged_mod = models.PositiveSmallIntegerField(default=0)
    ranged_dm_bonus = models.PositiveSmallIntegerField(default=0)
    ranged_stat = models.CharField(max_length=3, choices=CARAC_CHOICES)

    magic_enabled = models.BooleanField(default=True)
    magic_base = models.PositiveSmallIntegerField(default=10)
    magic_bonus = models.PositiveSmallIntegerField(default=0)
    magic_malus = models.PositiveSmallIntegerField(default=0)
    magic_mod = models.PositiveSmallIntegerField(default=0)
    magic_dm_bonus = models.PositiveSmallIntegerField(default=0)
    magic_stat = models.CharField(max_length=3, choices=CARAC_CHOICES)

    init = models.ForeignKey(
        "actors.Init",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    HP = models.ForeignKey(
        "actors.HP",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    RP = models.ForeignKey(
        "actors.RP",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    DEF = models.ForeignKey(
        "actors.Def",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    MP = models.ForeignKey(
        "actors.MP",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    LP = models.ForeignKey(
        "actors.LP",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )

    languages = models.ManyToManyField(to="actors.Languages", blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class NPC(Actor):
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255)
    hair = models.CharField(max_length=255)
    languages = models.ManyToManyField(to="actors.Languages")


class Encounter(Actor):
    ARCHETYPE_CHOICES = [("standard", "Standard")]
    CATEGORY_CHOICES = [("", "")]

    nc = models.PositiveSmallIntegerField(default=1)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    archetype = models.CharField(max_length=100, choices=ARCHETYPE_CHOICES)


class Languages(models.Model):
    name = models.CharField(max_length=255)


class Attribute(models.Model):
    base = models.PositiveSmallIntegerField(default=0)
    bonus = models.PositiveSmallIntegerField(default=0)
    value = models.PositiveSmallIntegerField(default=0)
    max = models.PositiveSmallIntegerField(default=0)


class HP(Attribute):
    label = models.CharField(
        max_length=100, default="Points de Vigueur", editable=False
    )
    abbrev = models.CharField(max_length=100, default="PV", editable=False)


class Def(Attribute):
    label = models.CharField(max_length=100, default="Défence", editable=False)
    abbrev = models.CharField(max_length=100, default="Def", editable=False)


class Init(Attribute):
    label = models.CharField(max_length=100, default="Initiative", editable=False)
    abbrev = models.CharField(max_length=100, default="Init", editable=False)


class RP(Attribute):
    label = models.CharField(
        max_length=100, default="Points de Récupération", editable=False
    )
    abbrev = models.CharField(max_length=100, default="PR", editable=False)


class MP(Attribute):
    label = models.CharField(max_length=100, default="Points de Mana", editable=False)
    abbrev = models.CharField(max_length=100, default="PM", editable=False)


class LP(Attribute):
    label = models.CharField(max_length=100, default="Points de Chance", editable=False)
    abbrev = models.CharField(max_length=100, default="PC", editable=False)


class Currency(models.Model):
    qty = models.PositiveSmallIntegerField(default=0)


class PP(Currency):
    label = models.CharField(
        max_length=100, default="Pièces de Platine", editable=False
    )
    abbrev = models.CharField(max_length=100, default="PP", editable=False)


class GP(Currency):
    label = models.CharField(max_length=100, default="Pièces d'Or", editable=False)
    abbrev = models.CharField(max_length=100, default="PM", editable=False)


class SP(Currency):
    label = models.CharField(max_length=100, default="Pièces d'Argent", editable=False)
    abbrev = models.CharField(max_length=100, default="PA", editable=False)


class CP(Currency):
    label = models.CharField(max_length=100, default="Pièces de Cuivre", editable=False)
    abbrev = models.CharField(max_length=100, default="PC", editable=False)


class Mini(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    painted = models.BooleanField(default=False)
    pawn = models.BooleanField(default=False)
