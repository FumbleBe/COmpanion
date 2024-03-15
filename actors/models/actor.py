from django.db import models, transaction
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
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    size = models.CharField(max_length=100, choices=SIZE_CHOICES)


class Character(Actor):
    GENDER_CHOICES = [
        ("male", "Homme"),
        ("female", "Femme"),
    ]
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(default=1)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    eyes = models.CharField(max_length=255, null=True, blank=True)
    hair = models.CharField(max_length=255, null=True, blank=True)
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
    STR = models.ForeignKey(
        "actors.STR",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    DEX = models.ForeignKey(
        "actors.DEX",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    CON = models.ForeignKey(
        "actors.CON",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    INT = models.ForeignKey(
        "actors.INT",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    WIS = models.ForeignKey(
        "actors.WIS",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    CHA = models.ForeignKey(
        "actors.CHA",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    melee = models.ForeignKey(
        "actors.Melee",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    ranged = models.ForeignKey(
        "actors.Ranged",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
    magic = models.ForeignKey(
        "actors.Magic",
        on_delete=models.PROTECT,
        related_name="characters",
        null=True,
        blank=True,
    )
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
    STR = models.ForeignKey(
        "actors.STR",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )
    DEX = models.ForeignKey(
        "actors.DEX",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )
    CON = models.ForeignKey(
        "actors.CON",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )
    INT = models.ForeignKey(
        "actors.INT",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )
    WIS = models.ForeignKey(
        "actors.WIS",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )
    CHA = models.ForeignKey(
        "actors.CHA",
        on_delete=models.PROTECT,
        related_name="encounters",
        null=True,
        blank=True,
    )


class Languages(models.Model):
    name = models.CharField(max_length=255)


class Statistic(models.Model):
    base = models.PositiveSmallIntegerField(default=10)
    racial = models.SmallIntegerField(default=0)
    bonus = models.SmallIntegerField(default=0)
    mod = models.SmallIntegerField(default=0)
    value = models.SmallIntegerField(default=0)
    tmpmod = models.SmallIntegerField(default=0)
    superior = models.BooleanField(default=False)
    skillbonus = models.SmallIntegerField(default=0)
    skillmalus = models.SmallIntegerField(default=0)


class STR(Statistic):
    label = models.CharField(max_length=100, default="Force", editable=False)
    abbrev = models.CharField(max_length=100, default="FOR", editable=False)


class DEX(Statistic):
    label = models.CharField(max_length=100, default="Dextérité", editable=False)
    abbrev = models.CharField(max_length=100, default="DEX", editable=False)


class CON(Statistic):
    label = models.CharField(max_length=100, default="Constitution", editable=False)
    abbrev = models.CharField(max_length=100, default="CON", editable=False)


class INT(Statistic):
    label = models.CharField(max_length=100, default="Intelligence", editable=False)
    abbrev = models.CharField(max_length=100, default="INT", editable=False)


class WIS(Statistic):
    label = models.CharField(max_length=100, default="Sagesse", editable=False)
    abbrev = models.CharField(max_length=100, default="WIS", editable=False)


class CHA(Statistic):
    label = models.CharField(max_length=100, default="Charisme", editable=False)
    abbrev = models.CharField(max_length=100, default="CHA", editable=False)


class Attack(models.Model):
    enabled = models.BooleanField(default=True)
    base = models.PositiveSmallIntegerField(default=10)
    bonus = models.PositiveSmallIntegerField(default=0)
    malus = models.PositiveSmallIntegerField(default=0)
    mod = models.PositiveSmallIntegerField(default=0)
    dm_bonus = models.PositiveSmallIntegerField(default=0)


class Melee(Attack):
    label = models.CharField(max_length=100, default="Mellée", editable=False)
    abbrev = models.CharField(max_length=100, default="CaC", editable=False)
    content_type = models.ForeignKey(
        to=ContentType, on_delete=models.SET_NULL, null=True
    )
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()


class Ranged(Attack):
    label = models.CharField(max_length=100, default="Distance", editable=False)
    abbrev = models.CharField(max_length=100, default="Dist", editable=False)
    content_type = models.ForeignKey(
        to=ContentType, on_delete=models.SET_NULL, null=True
    )
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()


class Magic(Attack):
    label = models.CharField(max_length=100, default="Magique", editable=False)
    abbrev = models.CharField(max_length=100, default="Mag", editable=False)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveBigIntegerField()
    stat = GenericForeignKey()


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
